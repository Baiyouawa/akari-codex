"""Fleet scheduler: refill loop, worker lifecycle management, CLI entry.

Aligned with upstream fleet-scheduler.ts + ADR 0042-v2:
  - Every poll_interval: assess demand, claim tasks, spawn workers
  - Per-project concurrency cap K (default 4)
  - Idle exploration when task queue is empty (ADR 0048)
  - Kill switch via FLEET_SIZE=0
  - Graceful drain: stop spawning, wait for active workers
"""

from __future__ import annotations

import argparse
import logging
import os
import signal
import sys
import threading
import time
import uuid
from concurrent.futures import ProcessPoolExecutor, Future
from multiprocessing import Manager, Queue
from pathlib import Path
from typing import Any

from .config import FleetConfig, FleetTask, FleetWorkerResult, WorkerRole, SkillType
from .dashboard import DashboardRenderer
from .executor import FleetExecutionOpts, execute_fleet_worker, execute_idle_worker
from .idle_tasks import (
    build_idle_prompt,
    gather_exploration_topics,
    load_cooldown_map,
    save_cooldown_map,
    select_topics,
    topic_key,
)
from .prompt_builder import build_fleet_prompt
from .rebase_push import cleanup_session_branches
from .status import FleetMetricsTracker, format_fleet_status
from .task_claims import TaskClaimStore
from .task_scanner import scan_available_tasks
from .task_supply import check_fleet_supply_warning, scan_task_supply

logger = logging.getLogger("fleet.scheduler")


def _generate_worker_id(index: int, role: str = "default") -> str:
    from runner.persona import get_agent_display_name
    name = get_agent_display_name(role, index)
    return f"{name}-{index:02d}"


def _generate_session_id(worker_id: str) -> str:
    return f"{worker_id}-{int(time.time())}-{uuid.uuid4().hex[:6]}"


def _infer_worker_role(task: FleetTask) -> WorkerRole:
    """Map task skill type to worker role."""
    if task.skill_type in (SkillType.RECORD, SkillType.PERSIST, SkillType.ANALYZE):
        return WorkerRole.KNOWLEDGE
    if task.skill_type in (SkillType.EXECUTE, SkillType.DIAGNOSE):
        return WorkerRole.IMPLEMENTATION
    return WorkerRole.DEFAULT


class FleetScheduler:
    """Manages the fleet worker pool with a periodic refill loop."""

    def __init__(
        self,
        repo_root: Path,
        fleet_config: FleetConfig | None = None,
    ):
        self.repo_root = repo_root
        self.config = fleet_config or FleetConfig.from_env()
        self.claims = TaskClaimStore(repo_root)
        self.metrics = FleetMetricsTracker(max_workers=self.config.max_workers)

        self._running = False
        self._draining = False
        self._worker_counter = 0
        self._worker_counter_lock = threading.Lock()

        self._futures: dict[str, Future] = {}
        self._futures_lock = threading.Lock()

        self._pool: ProcessPoolExecutor | None = None
        self._last_supply_warning_time = 0.0
        self._last_branch_cleanup_time = 0.0
        self._consecutive_failures = 0
        self._last_failure_time = 0.0
        self._has_ever_launched = False

        self._manager: Manager | None = None
        self._event_queue: Queue | None = None
        self._dashboard: DashboardRenderer | None = None

        self._blocked_notifications: list[dict[str, str]] = []
        self._blocked_lock = threading.Lock()

    def _next_worker_id(self, role: str = "default") -> str:
        with self._worker_counter_lock:
            self._worker_counter += 1
            return _generate_worker_id(self._worker_counter % self.config.max_workers, role)

    def start(self) -> None:
        """Start the fleet scheduler loop."""
        if self.config.max_workers <= 0:
            logger.info("Fleet disabled (FLEET_SIZE=0)")
            return

        logger.info(
            "Fleet scheduler starting: max_workers=%d, poll=%ds, max_per_project=%d",
            self.config.max_workers,
            self.config.poll_interval_seconds,
            self.config.max_per_project,
        )

        self._running = True
        self._pool = ProcessPoolExecutor(max_workers=self.config.max_workers)

        self._manager = Manager()
        self._event_queue = self._manager.Queue()
        self._dashboard = DashboardRenderer(
            self._event_queue, max_workers=self.config.max_workers
        )
        self._dashboard.start()

        self.claims.cleanup_stale()

        try:
            while self._running and not self._draining:
                self._tick()
                self._collect_completed()
                self._maybe_branch_cleanup()

                for _ in range(self.config.poll_interval_seconds):
                    if not self._running or self._draining:
                        break
                    time.sleep(1)

        except KeyboardInterrupt:
            logger.info("Fleet scheduler interrupted")
        finally:
            self._shutdown()

    def stop(self) -> None:
        """Signal the scheduler to stop after current workers finish."""
        logger.info("Fleet scheduler stopping...")
        self._draining = True

    def shutdown_now(self) -> None:
        """Immediately stop spawning and shut down."""
        self._running = False
        self._draining = True

    def _shutdown(self) -> None:
        global _scheduler_instance

        logger.info("Fleet shutting down, waiting for %d active workers...",
                     self.metrics.get_active_count())
        self._draining = True
        self._running = False

        if self._pool:
            self._pool.shutdown(wait=True, cancel_futures=False)
            self._pool = None

        if self._dashboard:
            self._dashboard.stop()
            self._dashboard = None

        if self._manager:
            self._manager.shutdown()
            self._manager = None

        if _scheduler_instance is self:
            _scheduler_instance = None

        logger.info("Fleet scheduler stopped")

    def _tick(self) -> None:
        """One iteration of the refill loop (ADR 0042-v2 algorithm)."""
        active_count = self.metrics.get_active_count()

        if active_count >= self.config.max_workers:
            return

        if self._consecutive_failures >= self.config.max_consecutive_failures:
            cooldown = 60 * (1 + self._consecutive_failures - self.config.max_consecutive_failures)
            elapsed_since_fail = time.time() - self._last_failure_time
            if elapsed_since_fail < cooldown:
                logger.warning(
                    "Circuit breaker: %d consecutive failures, cooldown %.0fs remaining",
                    self._consecutive_failures,
                    cooldown - elapsed_since_fail,
                )
                return
            logger.info(
                "Circuit breaker cooldown expired (%.0fs), resetting and retrying",
                elapsed_since_fail,
            )
            self._consecutive_failures = 0

        available = scan_available_tasks(self.repo_root)
        claimed_ids = self.claims.get_claimed_task_ids()
        pf = self.config.project_filter
        unclaimed = [
            t for t in available
            if t.task_id not in claimed_ids
            and t.fleet_eligible
            and not t.blocked
            and (not pf or t.project in pf)
        ]

        project_active = self.metrics.get_active_per_project()
        assignable = []
        for task in unclaimed:
            proj_count = project_active.get(task.project, 0)
            if proj_count >= self.config.max_per_project:
                self.metrics.record_concurrency_limit_hit(task.project)
                continue
            assignable.append(task)
            project_active[task.project] = proj_count + 1

        slots = self.config.max_workers - active_count
        to_launch = assignable[:slots]

        for task in to_launch:
            self._spawn_worker(task)

        if not to_launch and active_count == 0 and self._has_ever_launched:
            logger.info("All tasks completed, no active workers — entering drain")
            self._draining = True
            return

        remaining_slots = slots - len(to_launch)
        if remaining_slots > 0 and to_launch and self.config.idle_exploration_enabled:
            self._spawn_idle_workers(remaining_slots)

        self._check_supply_warning()

    def _spawn_worker(self, task: FleetTask) -> None:
        """认领任务并派遣工作Agent。"""
        worker_role = _infer_worker_role(task)
        worker_id = self._next_worker_id(worker_role.value)
        session_id = _generate_session_id(worker_id)

        claim_id = self.claims.try_claim(
            task_id=task.task_id,
            worker_id=worker_id,
            session_id=session_id,
            project=task.project,
        )
        if not claim_id:
            logger.debug("Task %s already claimed, skipping", task.task_id[:8])
            return

        prompt = build_fleet_prompt(
            task=task,
            session_id=session_id,
            repo_root=self.repo_root,
            worker_role=worker_role,
            max_turns=self.config.worker_max_turns,
        )

        opts = FleetExecutionOpts(
            task=task,
            session_id=session_id,
            claim_id=claim_id,
            prompt=prompt,
            repo_root=self.repo_root,
            worker_role=worker_role,
            max_turns=self.config.worker_max_turns,
            timeout_seconds=self.config.worker_timeout_seconds,
        )

        self._has_ever_launched = True
        self.metrics.record_launch(
            worker_id=worker_id,
            session_id=session_id,
            project=task.project,
            task_id=task.task_id,
        )

        if self._pool is None:
            return

        future = self._pool.submit(
            execute_fleet_worker,
            opts,
            self.config,
            self.claims,
            None,  # codex_config
            self._event_queue,
        )

        with self._futures_lock:
            self._futures[worker_id] = future

        logger.info(
            "Spawned worker %s for task %s (project=%s, role=%s)",
            worker_id,
            task.task_id[:8],
            task.project,
            worker_role.value,
        )

    def _spawn_idle_workers(self, count: int) -> None:
        """Spawn idle exploration workers to fill empty slots (ADR 0048)."""
        cooldown_map = load_cooldown_map(self.repo_root)
        topics = gather_exploration_topics(self.repo_root)
        selected = select_topics(topics, cooldown_map, count)

        now = time.time()
        for topic in selected:
            worker_id = self._next_worker_id("idle")
            session_id = _generate_session_id(worker_id)
            prompt = build_idle_prompt(topic, session_id, self.repo_root)

            self.metrics.record_launch(
                worker_id=worker_id,
                session_id=session_id,
                project=topic.project,
                task_id=f"idle-{topic.type}",
                is_idle=True,
                exploration_type=topic.type,
            )

            cooldown_map[topic_key(topic)] = now

            if self._pool is None:
                continue

            future = self._pool.submit(
                execute_idle_worker,
                session_id,
                prompt,
                topic.type,
                topic.project,
                self.repo_root,
                self.config,
                self.claims,
                None,  # codex_config
                self._event_queue,
            )

            with self._futures_lock:
                self._futures[worker_id] = future

            logger.info(
                "Spawned idle worker %s: %s for %s",
                worker_id,
                topic.type,
                topic.project,
            )

        save_cooldown_map(self.repo_root, cooldown_map)

    def _collect_completed(self) -> None:
        """Collect results from completed workers."""
        with self._futures_lock:
            done_workers = [
                wid for wid, fut in self._futures.items() if fut.done()
            ]

        for worker_id in done_workers:
            with self._futures_lock:
                future = self._futures.pop(worker_id, None)

            if future is None:
                continue

            try:
                result: FleetWorkerResult = future.result(timeout=5)
                self.metrics.record_completion(worker_id, result)

                if result.blocked:
                    self._enqueue_blocked(result)

                if result.ok:
                    self._consecutive_failures = 0
                else:
                    self._consecutive_failures += 1
                    self._last_failure_time = time.time()
                    logger.warning(
                        "Worker %s failed: %s (consecutive=%d)",
                        worker_id,
                        result.error,
                        self._consecutive_failures,
                    )

            except Exception as e:
                logger.exception("Worker %s raised exception", worker_id)
                self._consecutive_failures += 1
                self._last_failure_time = time.time()
                error_result = FleetWorkerResult(
                    task_id="unknown",
                    project="unknown",
                    session_id="unknown",
                    ok=False,
                    error=str(e),
                )
                self.metrics.record_completion(worker_id, error_result)

    def _check_supply_warning(self) -> None:
        """Check for fleet supply starvation (ADR 0047, max once per 30min)."""
        now = time.time()
        if now - self._last_supply_warning_time < 1800:
            return

        snap = scan_task_supply(self.repo_root)
        warning = check_fleet_supply_warning(snap.total_ready, self.config.max_workers)
        if warning:
            logger.warning("FLEET SUPPLY: %s", warning)
            self._last_supply_warning_time = now

    def _maybe_branch_cleanup(self) -> None:
        """Periodic session branch cleanup (ADR 0055, every 6 hours)."""
        now = time.time()
        if now - self._last_branch_cleanup_time < 21600:
            return

        self._last_branch_cleanup_time = now
        try:
            deleted = cleanup_session_branches(str(self.repo_root))
            if deleted:
                logger.info("Branch cleanup: removed %d session branches", len(deleted))
        except Exception:
            logger.exception("Branch cleanup failed")

    def add_project_filter(self, project: str) -> None:
        """Add a project to the filter set (thread-safe via frozen replace)."""
        from dataclasses import replace
        new_filter = self.config.project_filter | {project}
        self.config = replace(self.config, project_filter=new_filter)

    def clear_project_filter(self) -> None:
        """Remove project filter — all projects become eligible."""
        from dataclasses import replace
        self.config = replace(self.config, project_filter=frozenset())

    def _enqueue_blocked(self, result: FleetWorkerResult) -> None:
        """Record a blocked worker notification for owner escalation."""
        with self._blocked_lock:
            self._blocked_notifications.append({
                "worker": result.session_id,
                "project": result.project,
                "task_id": result.task_id,
                "reason": result.blocked_reason or "未说明原因",
            })
        logger.warning(
            "Worker %s BLOCKED on task %s: %s",
            result.session_id, result.task_id[:8],
            result.blocked_reason[:120] if result.blocked_reason else "unknown",
        )

    def drain_blocked_notifications(self) -> list[dict[str, str]]:
        """Pop all pending blocked notifications (thread-safe).

        Called by the onebot_client polling loop to forward to the owner.
        """
        with self._blocked_lock:
            items = list(self._blocked_notifications)
            self._blocked_notifications.clear()
            return items

    def get_status(self) -> str:
        """Get formatted fleet status."""
        snapshot = self.metrics.get_snapshot()
        return format_fleet_status(snapshot)

    def get_status_snapshot(self) -> dict[str, Any]:
        """Get raw status data for programmatic access."""
        snap = self.metrics.get_snapshot()
        return {
            "active": snap.active_workers,
            "max": snap.max_workers,
            "launched": snap.total_launched,
            "completed": snap.total_completed,
            "ok": snap.total_ok,
            "failed": snap.total_failed,
            "success_rate": snap.success_rate,
            "utilization": snap.utilization_rate,
            "draining": self._draining,
        }


_scheduler_instance: FleetScheduler | None = None


def get_fleet_scheduler() -> FleetScheduler | None:
    """Get the global fleet scheduler instance (if running)."""
    return _scheduler_instance


def start_fleet(
    repo_root: Path | None = None,
    fleet_config: FleetConfig | None = None,
    background: bool = True,
) -> FleetScheduler:
    """Start the fleet scheduler.

    If background=True, starts in a daemon thread.
    Returns the scheduler instance.
    """
    global _scheduler_instance

    if _scheduler_instance is not None and _scheduler_instance._running and not _scheduler_instance._draining:
        return _scheduler_instance

    if _scheduler_instance is not None and (_scheduler_instance._draining or not _scheduler_instance._running):
        _scheduler_instance = None

    if repo_root is None:
        repo_root = Path(os.environ.get("OPENAKARI_HOME", str(Path.cwd())))

    scheduler = FleetScheduler(repo_root, fleet_config)
    _scheduler_instance = scheduler

    if background:
        thread = threading.Thread(
            target=scheduler.start,
            name="fleet-scheduler",
            daemon=True,
        )
        thread.start()
        time.sleep(0.5)
    else:
        scheduler.start()

    return scheduler


def stop_fleet() -> str:
    """Stop the fleet scheduler gracefully."""
    global _scheduler_instance
    if _scheduler_instance is None:
        return "Fleet is not running"
    _scheduler_instance.stop()
    status = _scheduler_instance.get_status()
    _scheduler_instance = None
    return f"Fleet stopping...\n\n{status}"


def fleet_status() -> str:
    """Get current fleet status."""
    if _scheduler_instance is None:
        return "Fleet is not running. Use fleet_start to launch."
    return _scheduler_instance.get_status()


def main() -> None:
    """CLI entry point for fleet scheduler."""
    parser = argparse.ArgumentParser(description="OpenAkari Fleet Scheduler")
    parser.add_argument(
        "--max-workers", type=int, default=None,
        help="Maximum fleet workers (default: from FLEET_SIZE env or 32)",
    )
    parser.add_argument(
        "--repo", type=str, default=None,
        help="Repository root (default: from OPENAKARI_HOME or cwd)",
    )
    parser.add_argument(
        "--poll-interval", type=int, default=None,
        help="Poll interval in seconds (default: 30)",
    )
    parser.add_argument(
        "--status-only", action="store_true",
        help="Print current fleet status and exit",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    repo_root = Path(args.repo) if args.repo else Path(
        os.environ.get("OPENAKARI_HOME", str(Path.cwd()))
    )

    config_kwargs: dict[str, Any] = {}
    if args.max_workers is not None:
        config_kwargs["max_workers"] = args.max_workers
    if args.poll_interval is not None:
        config_kwargs["poll_interval_seconds"] = args.poll_interval

    if config_kwargs:
        base = FleetConfig.from_env()
        from dataclasses import replace
        config = replace(base, **config_kwargs)
    else:
        config = FleetConfig.from_env()

    if args.status_only:
        scheduler = FleetScheduler(repo_root, config)
        snap = scan_task_supply(repo_root)
        from .task_supply import format_task_supply
        print(format_task_supply(snap))
        return

    scheduler = FleetScheduler(repo_root, config)

    def _signal_handler(sig: int, frame: Any) -> None:
        logger.info("Received signal %d, initiating drain...", sig)
        scheduler.stop()

    signal.signal(signal.SIGINT, _signal_handler)
    signal.signal(signal.SIGTERM, _signal_handler)

    print(f"Fleet Scheduler starting with {config.max_workers} workers")
    print(f"Repository: {repo_root}")
    print(f"Poll interval: {config.poll_interval_seconds}s")
    print(f"Per-project cap: {config.max_per_project}")
    print(f"Kill switch: set FLEET_SIZE=0 to disable")
    print()

    scheduler.start()


if __name__ == "__main__":
    main()
