"""Minimal local scheduler for Codex sessions.

Supports:
  - Single job execution (manual trigger)
  - Periodic scheduling via configurable interval
  - Job definitions with project path, task selector, model, budget, approval policy
  - Run loop: pick task → assemble prompt → invoke backend → write logs → update state

This is intentionally simpler than the upstream TypeScript scheduler.
The goal is to validate the single-session loop before scaling.

Usage:
    python -m runner.scheduler run-once --job jobs/default.json
    python -m runner.scheduler start --job jobs/default.json --interval 3600
"""

from __future__ import annotations

import argparse
import json
import signal
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .codex_session_runner import SessionRunner
from .config import CodexConfig


@dataclass
class JobDefinition:
    """Describes a scheduled job."""
    job_id: str
    project_path: str
    task_selector: str = "auto"       # "auto" or a specific task file path
    frequency_seconds: int = 3600     # default: every hour
    model: str = ""                   # empty = use config default
    max_budget_usd: float = 10.0
    approval_policy: str = "standard" # "standard" or "permissive"
    output_location: str = "logs/sessions"
    enabled: bool = True

    @classmethod
    def from_file(cls, path: Path) -> JobDefinition:
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            job_id=data.get("job_id", path.stem),
            project_path=data.get("project_path", "."),
            task_selector=data.get("task_selector", "auto"),
            frequency_seconds=data.get("frequency_seconds", 3600),
            model=data.get("model", ""),
            max_budget_usd=data.get("max_budget_usd", 10.0),
            approval_policy=data.get("approval_policy", "standard"),
            output_location=data.get("output_location", "logs/sessions"),
            enabled=data.get("enabled", True),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "job_id": self.job_id,
            "project_path": self.project_path,
            "task_selector": self.task_selector,
            "frequency_seconds": self.frequency_seconds,
            "model": self.model,
            "max_budget_usd": self.max_budget_usd,
            "approval_policy": self.approval_policy,
            "output_location": self.output_location,
            "enabled": self.enabled,
        }


@dataclass
class SchedulerState:
    """Tracks scheduler run history."""
    runs: list[dict[str, Any]] = field(default_factory=list)
    total_tokens_used: int = 0
    total_cost_estimate_usd: float = 0.0
    consecutive_failures: int = 0

    def record_run(self, session_result: Any, job: JobDefinition) -> None:
        entry = {
            "job_id": job.job_id,
            "task_id": session_result.task_id,
            "success": session_result.success,
            "tokens": session_result.token_usage.total_tokens,
            "latency_seconds": round(session_result.latency_seconds, 2),
            "error": session_result.error,
        }
        self.runs.append(entry)
        self.total_tokens_used += session_result.token_usage.total_tokens

        if session_result.success:
            self.consecutive_failures = 0
        else:
            self.consecutive_failures += 1

    def budget_remaining(self, job: JobDefinition) -> bool:
        """Rough estimate: $0.01 per 1k tokens (conservative)."""
        self.total_cost_estimate_usd = self.total_tokens_used / 1000 * 0.01
        return self.total_cost_estimate_usd < job.max_budget_usd

    def should_circuit_break(self) -> bool:
        return self.consecutive_failures >= 3


class Scheduler:
    """Minimal local scheduler that runs Codex sessions."""

    def __init__(self, config: CodexConfig, job: JobDefinition):
        self.config = config
        self.job = job
        self.state = SchedulerState()
        self._shutdown = False

        if job.model:
            object.__setattr__(self.config, "model", job.model)

    def run_once(self) -> dict[str, Any]:
        """Execute a single session for this job."""
        if not self.job.enabled:
            return {"status": "skipped", "reason": "job disabled"}

        if not self.state.budget_remaining(self.job):
            return {"status": "skipped", "reason": "budget exhausted"}

        if self.state.should_circuit_break():
            return {
                "status": "circuit-break",
                "reason": f"{self.state.consecutive_failures} consecutive failures",
            }

        task_path = None if self.job.task_selector == "auto" else self.job.task_selector

        runner = SessionRunner(self.config)
        result = runner.run(task_path=task_path)
        self.state.record_run(result, self.job)

        return {
            "status": "completed",
            "success": result.success,
            "session_id": runner.session_id,
            "task_id": result.task_id,
            "tokens": result.token_usage.total_tokens,
            "error": result.error,
            "budget_used_usd": round(self.state.total_cost_estimate_usd, 4),
        }

    def start(self) -> None:
        """Run in a loop with the configured interval. Ctrl+C to stop."""

        def _handle_signal(signum: int, frame: Any) -> None:
            print("\n[scheduler] Received shutdown signal, draining...")
            self._shutdown = True

        signal.signal(signal.SIGINT, _handle_signal)
        signal.signal(signal.SIGTERM, _handle_signal)

        print(f"[scheduler] Starting job '{self.job.job_id}'")
        print(f"  Interval: {self.job.frequency_seconds}s")
        print(f"  Budget cap: ${self.job.max_budget_usd}")
        print(f"  Model: {self.config.model}")
        print()

        while not self._shutdown:
            result = self.run_once()
            print(f"[scheduler] Run result: {json.dumps(result, default=str)}")

            if result["status"] in ("circuit-break",):
                print("[scheduler] Circuit breaker tripped. Stopping.")
                break
            if result["status"] == "skipped" and result.get("reason") == "budget exhausted":
                print("[scheduler] Budget exhausted. Stopping.")
                break

            if not self._shutdown:
                print(f"[scheduler] Sleeping {self.job.frequency_seconds}s until next run...")
                for _ in range(self.job.frequency_seconds):
                    if self._shutdown:
                        break
                    time.sleep(1)

        print(f"[scheduler] Shut down. Total runs: {len(self.state.runs)}, "
              f"Tokens: {self.state.total_tokens_used}, "
              f"Est. cost: ${self.state.total_cost_estimate_usd:.4f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="OpenAkari-Codex Scheduler")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_once = subparsers.add_parser("run-once", help="Execute a single session")
    run_once.add_argument("--job", required=True, help="Path to job definition JSON")

    start = subparsers.add_parser("start", help="Run scheduled loop")
    start.add_argument("--job", required=True, help="Path to job definition JSON")
    start.add_argument("--interval", type=int, help="Override interval (seconds)")

    args = parser.parse_args()

    try:
        config = CodexConfig.from_env()
    except EnvironmentError as e:
        print(f"Config error: {e}", file=sys.stderr)
        sys.exit(1)

    job_path = Path(args.job)
    if not job_path.is_file():
        print(f"Job file not found: {args.job}", file=sys.stderr)
        sys.exit(1)

    job = JobDefinition.from_file(job_path)
    if args.command == "start" and args.interval:
        job.frequency_seconds = args.interval

    scheduler = Scheduler(config, job)

    if args.command == "run-once":
        result = scheduler.run_once()
        print(json.dumps(result, indent=2, default=str))
        sys.exit(0 if result.get("success", False) else 1)
    elif args.command == "start":
        scheduler.start()


if __name__ == "__main__":
    main()
