"""Scan TASKS.md files to find fleet-assignable tasks.

Aligned with upstream fleet-tasks.ts:
  - classify_task_skill: heuristic skill classification (ADR 0062)
  - parse_tasks_file: parse open tasks, filter blocked/in-progress
  - scan_available_tasks: scan all projects, sort by priority
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from .config import FleetTask, SkillType, TaskPriority

_TAG_RE = re.compile(r"\[([^\]]+)\]")
_DONE_WHEN_RE = re.compile(r"Done when:\s*(.+)", re.IGNORECASE)
_WHY_RE = re.compile(r"Why:\s*(.+)", re.IGNORECASE)

_SKILL_PATTERNS: list[tuple[SkillType, list[str]]] = [
    (SkillType.DIAGNOSE, ["debug", "diagnose", "fix", "error", "bug", "troubleshoot"]),
    (SkillType.ANALYZE, ["analyze", "analysis", "compare", "evaluate", "benchmark"]),
    (SkillType.RECORD, ["literature", "survey", "review", "paper", "search", "cite"]),
    (SkillType.PERSIST, ["write", "document", "note", "summarize", "report"]),
    (SkillType.EXECUTE, ["implement", "build", "create", "code", "test", "refactor"]),
    (SkillType.GOVERN, ["policy", "decision", "governance", "convention", "audit"]),
]


def task_id_from_text(text: str) -> str:
    """Generate a stable task ID from task text (aligned with taskIdFromText)."""
    normalized = re.sub(r"\s+", " ", text.strip().lower())
    return hashlib.sha256(normalized.encode()).hexdigest()[:16]


def classify_task_skill(text: str) -> SkillType | None:
    """Heuristic skill classification (aligned with ADR 0062)."""
    lower = text.lower()
    for skill, keywords in _SKILL_PATTERNS:
        if any(kw in lower for kw in keywords):
            return skill
    return None


def read_project_priority(project_dir: Path) -> TaskPriority:
    """Read priority from project README.md."""
    readme = project_dir / "README.md"
    if not readme.is_file():
        return TaskPriority.MEDIUM
    content = readme.read_text(errors="replace")
    match = re.search(r"Priority:\s*(high|medium|low)", content, re.IGNORECASE)
    if match:
        return TaskPriority(match.group(1).lower())
    return TaskPriority.MEDIUM


def parse_tasks_file(
    content: str,
    project: str,
    project_dir: Path | None = None,
) -> list[FleetTask]:
    """Parse open tasks from a TASKS.md file.

    Filters out:
      - Completed tasks (``[x]``)
      - Tasks marked ``[in-progress]``
      - Tasks with ``[approval-needed]`` that haven't been approved
      - Tasks marked ``[blocked-by: ...]``

    ``fleet_eligible`` is True unless ``[requires-opus]`` is present
    (aligned with fleet-tasks.ts logic).
    """
    tasks: list[FleetTask] = []
    lines = content.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line.startswith("- [ ]"):
            i += 1
            continue

        task_text = line[5:].strip()
        tags = set(_TAG_RE.findall(task_text))

        if "in-progress" in tags:
            i += 1
            continue
        if "approval-needed" in tags:
            i += 1
            continue

        blocked = any(t.startswith("blocked-by") for t in tags)
        requires_opus = "requires-opus" in tags
        zero_resource = "zero-resource" in tags
        fleet_eligible = not requires_opus

        done_when = ""
        why = ""
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("- "):
            continuation = lines[i].strip()
            dw_match = _DONE_WHEN_RE.match(continuation)
            if dw_match:
                done_when = dw_match.group(1).strip()
            why_match = _WHY_RE.match(continuation)
            if why_match:
                why = why_match.group(1).strip()
            i += 1

        clean_text = _TAG_RE.sub("", task_text).strip()
        skill = classify_task_skill(clean_text)

        tasks.append(FleetTask(
            task_id=task_id_from_text(clean_text),
            text=clean_text,
            project=project,
            fleet_eligible=fleet_eligible,
            requires_opus=requires_opus,
            zero_resource=zero_resource,
            blocked=blocked,
            skill_type=skill,
            done_when=done_when,
            why=why,
        ))

    return tasks


def scan_available_tasks(repo_root: Path) -> list[FleetTask]:
    """Scan all projects for fleet-assignable tasks.

    Returns tasks sorted by:
      1. Project priority (high > medium > low)
      2. fleet_eligible first
      3. Unblocked first
    """
    all_tasks: list[FleetTask] = []
    projects_dir = repo_root / "projects"

    if not projects_dir.is_dir():
        return all_tasks

    for project_dir in sorted(projects_dir.iterdir()):
        if not project_dir.is_dir():
            continue

        tasks_file = project_dir / "TASKS.md"
        if not tasks_file.is_file():
            continue

        project_name = project_dir.name
        project_priority = read_project_priority(project_dir)
        content = tasks_file.read_text(errors="replace")
        tasks = parse_tasks_file(content, project_name, project_dir)

        for task in tasks:
            task.priority = project_priority

        all_tasks.extend(tasks)

    priority_order = {TaskPriority.HIGH: 0, TaskPriority.MEDIUM: 1, TaskPriority.LOW: 2}
    all_tasks.sort(key=lambda t: (
        priority_order.get(t.priority, 1),
        0 if t.fleet_eligible else 1,
        0 if not t.blocked else 1,
    ))

    return all_tasks
