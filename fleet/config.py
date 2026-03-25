"""Fleet configuration and core data types.

Aligned with upstream types.ts: FleetWorkerConfig, FleetTask,
FleetWorkerResult, SkillType, WorkerRole.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class SkillType(str, Enum):
    RECORD = "record"
    PERSIST = "persist"
    GOVERN = "govern"
    EXECUTE = "execute"
    DIAGNOSE = "diagnose"
    ANALYZE = "analyze"
    ORIENT = "orient"
    MULTI = "multi"


class WorkerRole(str, Enum):
    KNOWLEDGE = "knowledge"
    IMPLEMENTATION = "implementation"
    DEFAULT = "default"


class TaskPriority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass(frozen=True)
class FleetConfig:
    """Fleet-level configuration (aligned with FleetWorkerConfig in types.ts)."""

    max_workers: int = 32
    max_per_project: int = 4
    poll_interval_seconds: int = 30
    worker_max_turns: int = 64
    worker_timeout_seconds: int = 900
    max_consecutive_failures: int = 3
    idle_exploration_enabled: bool = True
    idle_cooldown_seconds: int = 21600  # 6 hours
    project_filter: frozenset[str] = frozenset()  # empty = all projects

    @classmethod
    def from_env(cls) -> FleetConfig:
        return cls(
            max_workers=int(os.environ.get("FLEET_SIZE", str(cls.max_workers))),
            max_per_project=int(
                os.environ.get("FLEET_MAX_PER_PROJECT", str(cls.max_per_project))
            ),
            poll_interval_seconds=int(
                os.environ.get("FLEET_POLL_INTERVAL", str(cls.poll_interval_seconds))
            ),
            worker_max_turns=int(
                os.environ.get("FLEET_WORKER_MAX_TURNS", str(cls.worker_max_turns))
            ),
            worker_timeout_seconds=int(
                os.environ.get(
                    "FLEET_WORKER_TIMEOUT", str(cls.worker_timeout_seconds)
                )
            ),
            idle_exploration_enabled=os.environ.get(
                "FLEET_IDLE_EXPLORATION", "1"
            ) == "1",
        )


@dataclass
class FleetTask:
    """A single task parsed from TASKS.md that can be assigned to a fleet worker."""

    task_id: str
    text: str
    project: str
    priority: TaskPriority = TaskPriority.MEDIUM
    fleet_eligible: bool = True
    requires_opus: bool = False
    zero_resource: bool = False
    skill_type: SkillType | None = None
    done_when: str = ""
    why: str = ""
    blocked: bool = False
    in_progress: bool = False
    approval_needed: bool = False


@dataclass
class FleetWorkerResult:
    """Result from a single fleet worker execution."""

    task_id: str
    project: str
    session_id: str
    ok: bool
    duration_seconds: float = 0.0
    error: str | None = None
    total_tokens: int = 0
    turns: int = 0
    is_idle: bool = False
    idle_exploration_type: str | None = None
    skill_type: SkillType | None = None
    worker_role: WorkerRole = WorkerRole.DEFAULT
    blocked: bool = False
    blocked_reason: str = ""
    push_result: str = ""  # pushed | branch-fallback | nothing-to-push | error
    head_before: str = ""
    head_after: str = ""


@dataclass
class TaskSupplySnapshot:
    """Snapshot of fleet task supply across all projects."""

    total_ready: int = 0
    total_blocked: int = 0
    total_untagged: int = 0
    total_requires_opus: int = 0
    by_project: dict[str, dict[str, int]] = field(default_factory=dict)
    decomposable_tasks: list[dict[str, str]] = field(default_factory=list)
    blocked_summary: list[str] = field(default_factory=list)


@dataclass
class FleetStatusSnapshot:
    """Point-in-time fleet status for reporting."""

    active_workers: int = 0
    max_workers: int = 32
    total_launched: int = 0
    total_completed: int = 0
    total_ok: int = 0
    total_failed: int = 0
    success_rate: float = 0.0
    avg_duration_seconds: float = 0.0
    active_list: list[dict[str, Any]] = field(default_factory=list)
    by_project: dict[str, int] = field(default_factory=dict)
    by_skill: dict[str, int] = field(default_factory=dict)
    idle_stats: dict[str, int] = field(default_factory=dict)
    utilization_rate: float = 0.0
