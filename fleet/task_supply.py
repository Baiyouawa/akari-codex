"""Fleet task supply scanning and starvation detection.

Aligned with upstream fleet-supply.ts:
  - scanTaskSupply: snapshot of ready/blocked/untagged tasks
  - detectDecompositionTrigger: heuristic for decomposable tasks
  - formatTaskSupply: markdown-style supply report
  - checkFleetSupplyWarning: starvation alert
"""

from __future__ import annotations

import re
from pathlib import Path

from .config import FleetConfig, TaskSupplySnapshot
from .task_scanner import parse_tasks_file, read_project_priority

FLEET_SUPPLY_WARNING_RATIO = 1.5


def detect_decomposition_trigger(text: str) -> str | None:
    """Detect if a requires-opus task could be decomposed for fleet.

    Returns trigger type or None.
    """
    lower = text.lower()
    step_indicators = ["then", "after", "next", "finally", "first", "second", "step"]
    if sum(1 for s in step_indicators if s in lower) >= 2:
        return "multiple-steps"

    file_indicators = ["across", "all files", "every", "each file", "refactor"]
    if any(f in lower for f in file_indicators):
        return "multiple-files"

    mixed = ["and", "also", "plus", "additionally"]
    if sum(1 for m in mixed if m in lower) >= 2:
        return "mixed-work"

    return None


def scan_task_supply(repo_root: Path) -> TaskSupplySnapshot:
    """Scan all projects and produce a supply snapshot."""
    snap = TaskSupplySnapshot()
    projects_dir = repo_root / "projects"

    if not projects_dir.is_dir():
        return snap

    for project_dir in sorted(projects_dir.iterdir()):
        if not project_dir.is_dir():
            continue

        tasks_file = project_dir / "TASKS.md"
        if not tasks_file.is_file():
            continue

        project_name = project_dir.name
        content = tasks_file.read_text(errors="replace")
        tasks = parse_tasks_file(content, project_name, project_dir)

        project_stats = {
            "fleet_eligible_unblocked": 0,
            "fleet_eligible_blocked": 0,
            "untagged": 0,
            "requires_opus": 0,
        }

        for task in tasks:
            if task.requires_opus:
                project_stats["requires_opus"] += 1
                snap.total_requires_opus += 1
                if not task.blocked:
                    trigger = detect_decomposition_trigger(task.text)
                    if trigger:
                        snap.decomposable_tasks.append({
                            "text": task.text,
                            "project": project_name,
                            "trigger": trigger,
                        })
            elif task.fleet_eligible:
                if task.blocked:
                    project_stats["fleet_eligible_blocked"] += 1
                    snap.total_blocked += 1
                    snap.blocked_summary.append(
                        f"[{project_name}] {task.text[:80]}"
                    )
                else:
                    project_stats["fleet_eligible_unblocked"] += 1
                    snap.total_ready += 1
            else:
                project_stats["untagged"] += 1
                snap.total_untagged += 1

        snap.by_project[project_name] = project_stats

    return snap


def format_task_supply(snap: TaskSupplySnapshot) -> str:
    """Format supply snapshot as markdown report."""
    lines = ["## Fleet Task Supply\n"]
    lines.append(f"Ready: {snap.total_ready} | "
                 f"Blocked: {snap.total_blocked} | "
                 f"Requires-Opus: {snap.total_requires_opus} | "
                 f"Untagged: {snap.total_untagged}\n")

    if snap.by_project:
        lines.append("### By Project\n")
        for project, stats in snap.by_project.items():
            ready = stats["fleet_eligible_unblocked"]
            blocked = stats["fleet_eligible_blocked"]
            opus = stats["requires_opus"]
            lines.append(f"- **{project}**: {ready} ready, {blocked} blocked, {opus} opus")

    if snap.decomposable_tasks:
        lines.append("\n### Decomposable (requires-opus candidates)\n")
        for dt in snap.decomposable_tasks:
            lines.append(f"- [{dt['trigger']}] {dt['text'][:80]} ({dt['project']})")

    if snap.blocked_summary:
        lines.append("\n### Blocked Tasks\n")
        for b in snap.blocked_summary[:10]:
            lines.append(f"- {b}")

    return "\n".join(lines)


def get_task_supply_summary(snap: TaskSupplySnapshot) -> str:
    """One-line supply summary."""
    return (
        f"Supply: {snap.total_ready} ready, "
        f"{snap.total_blocked} blocked, "
        f"{snap.total_requires_opus} opus-only "
        f"across {len(snap.by_project)} projects"
    )


def check_fleet_supply_warning(
    unblocked_count: int,
    fleet_size: int,
) -> str | None:
    """Return warning message if supply is dangerously low."""
    if fleet_size <= 0:
        return None
    if unblocked_count < fleet_size * FLEET_SUPPLY_WARNING_RATIO:
        return (
            f"Fleet supply low: {unblocked_count} ready tasks "
            f"for {fleet_size} workers "
            f"(ratio {unblocked_count/fleet_size:.1f}, "
            f"threshold {FLEET_SUPPLY_WARNING_RATIO})"
        )
    return None
