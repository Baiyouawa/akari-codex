"""Fleet metrics tracking and status reporting.

Aligned with upstream fleet-status.ts:
  - FleetMetricsTracker: records launches, completions, concurrency hits
  - format_fleet_status: formatted report for CLI/QQ/GitHub display
  - Rolling utilization with configurable window
"""

from __future__ import annotations

import time
import threading
from dataclasses import dataclass, field
from typing import Any

from .config import FleetStatusSnapshot, FleetWorkerResult


@dataclass
class _ActiveWorker:
    worker_id: str
    session_id: str
    project: str
    task_id: str
    started_at: float
    is_idle: bool = False
    exploration_type: str | None = None
    task_text: str = ""


class FleetMetricsTracker:
    """Thread-safe metrics tracker for fleet operations."""

    def __init__(self, max_workers: int = 32):
        self._lock = threading.Lock()
        self._max_workers = max_workers
        self._active: dict[str, _ActiveWorker] = {}
        self._total_launched = 0
        self._total_completed = 0
        self._total_ok = 0
        self._total_failed = 0
        self._durations: list[float] = []
        self._by_project: dict[str, int] = {}
        self._by_skill: dict[str, int] = {}
        self._idle_stats: dict[str, dict[str, int]] = {}
        self._concurrency_hits: dict[str, int] = {}
        self._launch_times: list[float] = []

    def record_launch(
        self,
        worker_id: str,
        session_id: str,
        project: str,
        task_id: str,
        is_idle: bool = False,
        exploration_type: str | None = None,
        task_text: str = "",
    ) -> None:
        with self._lock:
            self._active[worker_id] = _ActiveWorker(
                worker_id=worker_id,
                session_id=session_id,
                project=project,
                task_id=task_id,
                started_at=time.time(),
                is_idle=is_idle,
                exploration_type=exploration_type,
                task_text=task_text,
            )
            self._total_launched += 1
            self._launch_times.append(time.time())

            if is_idle and exploration_type:
                if exploration_type not in self._idle_stats:
                    self._idle_stats[exploration_type] = {
                        "launched": 0, "completed": 0, "ok": 0, "failed": 0,
                    }
                self._idle_stats[exploration_type]["launched"] += 1

    def record_completion(self, worker_id: str, result: FleetWorkerResult) -> None:
        with self._lock:
            self._active.pop(worker_id, None)
            self._total_completed += 1
            self._durations.append(result.duration_seconds)

            if result.ok:
                self._total_ok += 1
            else:
                self._total_failed += 1

            if result.project:
                self._by_project[result.project] = (
                    self._by_project.get(result.project, 0) + 1
                )

            if result.skill_type:
                skill_key = result.skill_type.value if hasattr(result.skill_type, 'value') else str(result.skill_type)
                self._by_skill[skill_key] = self._by_skill.get(skill_key, 0) + 1

            if result.is_idle and result.idle_exploration_type:
                etype = result.idle_exploration_type
                if etype in self._idle_stats:
                    self._idle_stats[etype]["completed"] += 1
                    if result.ok:
                        self._idle_stats[etype]["ok"] += 1
                    else:
                        self._idle_stats[etype]["failed"] += 1

    def record_concurrency_limit_hit(self, project: str) -> None:
        with self._lock:
            self._concurrency_hits[project] = (
                self._concurrency_hits.get(project, 0) + 1
            )

    def get_active_count(self) -> int:
        with self._lock:
            return len(self._active)

    def get_active_per_project(self) -> dict[str, int]:
        with self._lock:
            counts: dict[str, int] = {}
            for w in self._active.values():
                counts[w.project] = counts.get(w.project, 0) + 1
            return counts

    def get_utilization_rate(self, window_seconds: float = 3600) -> float:
        """Rolling utilization over the given window."""
        with self._lock:
            if not self._launch_times or self._max_workers == 0:
                return 0.0
            now = time.time()
            cutoff = now - window_seconds
            recent_launches = sum(1 for t in self._launch_times if t > cutoff)
            active = len(self._active)
            return active / self._max_workers

    def get_snapshot(self) -> FleetStatusSnapshot:
        with self._lock:
            avg_dur = (
                sum(self._durations) / len(self._durations)
                if self._durations
                else 0.0
            )
            success_rate = (
                self._total_ok / self._total_completed
                if self._total_completed > 0
                else 0.0
            )

            active_list = []
            for w in self._active.values():
                elapsed = time.time() - w.started_at
                active_list.append({
                    "worker_id": w.worker_id,
                    "session_id": w.session_id,
                    "project": w.project,
                    "task_id": w.task_id[:12],
                    "task_text": w.task_text,
                    "elapsed_seconds": round(elapsed, 1),
                    "is_idle": w.is_idle,
                })

            return FleetStatusSnapshot(
                active_workers=len(self._active),
                max_workers=self._max_workers,
                total_launched=self._total_launched,
                total_completed=self._total_completed,
                total_ok=self._total_ok,
                total_failed=self._total_failed,
                success_rate=round(success_rate, 3),
                avg_duration_seconds=round(avg_dur, 1),
                active_list=active_list,
                by_project=dict(self._by_project),
                by_skill=dict(self._by_skill),
                idle_stats={k: dict(v) for k, v in self._idle_stats.items()},
                utilization_rate=round(
                    len(self._active) / max(self._max_workers, 1), 3
                ),
            )


def format_fleet_status(snapshot: FleetStatusSnapshot) -> str:
    """Format fleet status as a readable report."""
    lines = [
        "## Fleet Status\n",
        f"Workers: {snapshot.active_workers}/{snapshot.max_workers} active "
        f"({snapshot.utilization_rate:.0%} utilization)\n",
        f"Total: {snapshot.total_launched} launched, "
        f"{snapshot.total_completed} completed "
        f"({snapshot.success_rate:.0%} success rate)\n",
        f"Avg duration: {snapshot.avg_duration_seconds:.0f}s\n",
    ]

    if snapshot.active_list:
        lines.append("### Active Workers\n")
        for w in snapshot.active_list:
            idle_tag = " [idle]" if w["is_idle"] else ""
            lines.append(
                f"- {w['worker_id']}: {w['project']}/{w['task_id']} "
                f"({w['elapsed_seconds']:.0f}s){idle_tag}"
            )

    if snapshot.by_project:
        lines.append("\n### Completions by Project\n")
        for proj, count in sorted(snapshot.by_project.items(), key=lambda x: -x[1]):
            lines.append(f"- {proj}: {count}")

    if snapshot.by_skill:
        lines.append("\n### Completions by Skill\n")
        for skill, count in sorted(snapshot.by_skill.items(), key=lambda x: -x[1]):
            lines.append(f"- {skill}: {count}")

    if snapshot.idle_stats:
        lines.append("\n### Idle Exploration\n")
        for etype, stats in snapshot.idle_stats.items():
            lines.append(
                f"- {etype}: {stats.get('launched', 0)} launched, "
                f"{stats.get('ok', 0)} ok, {stats.get('failed', 0)} failed"
            )

    return "\n".join(lines)
