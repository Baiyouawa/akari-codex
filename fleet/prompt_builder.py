"""Build fleet worker prompts per task and worker role.

Aligned with upstream fleet-prompt.ts:
  - extractProjectContext: pull Status/Priority/Mission/recent log from README
  - buildFleetPrompt: task + role → self-contained worker system prompt
  - SHARED_CONSTRAINTS: safety boundaries all fleet workers must follow
"""

from __future__ import annotations

import re
from pathlib import Path

from .config import FleetTask, WorkerRole

SHARED_CONSTRAINTS = """\
## Fleet Worker Constraints

1. Only modify files within your assigned write_scope.
2. Commit messages must include [fleet/{session_id}].
3. Do NOT run /orient, /compound, or meta-reasoning skills.
4. Do NOT modify AGENTS.md, decisions/, or fleet/ configuration.
5. If you produce nothing of value, make zero commits — that is correct behavior.
6. Complete your assigned task, then stop. Do not pick up additional tasks.
7. If blocked, report the blocker and exit cleanly.
8. Keep session under {max_turns} turns.
"""


def extract_project_context(readme_path: Path) -> str:
    """Extract Status/Priority/Mission and recent log entries from README.md."""
    if not readme_path.is_file():
        return "(no project README)"

    content = readme_path.read_text(errors="replace")
    parts: list[str] = []

    for field in ("Status", "Priority", "Mission"):
        match = re.search(rf"{field}:\s*(.+)", content, re.IGNORECASE)
        if match:
            parts.append(f"{field}: {match.group(1).strip()}")

    log_match = re.search(r"## Log\s*\n((?:### .+\n(?:(?!##).+\n)*)+)", content)
    if log_match:
        log_entries = re.findall(r"### (\d{4}-\d{2}-\d{2})\n((?:(?!###).+\n)*)", log_match.group(1))
        for date, body in log_entries[:3]:
            summary = body.strip()[:200]
            parts.append(f"Log {date}: {summary}")

    done_when = re.search(r"Done when:\s*(.+)", content, re.IGNORECASE)
    if done_when:
        parts.append(f"Done when: {done_when.group(1).strip()}")

    open_qs = re.search(r"## Open questions\s*\n((?:(?!##).+\n)*)", content)
    if open_qs:
        questions = [
            q.strip().lstrip("- ")
            for q in open_qs.group(1).strip().splitlines()
            if q.strip() and q.strip() != "(to be filled)"
        ]
        if questions:
            parts.append(f"Open questions: {'; '.join(questions[:3])}")

    return "\n".join(parts) or "(minimal project context)"


def _build_task_details(task: FleetTask) -> str:
    """Format task details for inclusion in prompt."""
    lines = [f"Task: {task.text}"]
    if task.done_when:
        lines.append(f"Done when: {task.done_when}")
    if task.why:
        lines.append(f"Why: {task.why}")
    if task.skill_type:
        lines.append(f"Skill type: {task.skill_type.value}")
    if task.zero_resource:
        lines.append("Note: This is a zero-resource task (no external API calls needed)")
    return "\n".join(lines)


def _build_knowledge_prompt(
    task: FleetTask,
    project_context: str,
    session_id: str,
    constraints: str,
) -> str:
    return f"""\
You are a fleet knowledge worker (session: {session_id}).
Your role: research, analyze, and produce knowledge artifacts.

## Project Context
{project_context}

## Assignment
{_build_task_details(task)}

## Your Approach
1. Search existing literature/ and analysis/ for prior work
2. Gather information using read_file and search_text
3. Synthesize findings into a clear, structured document
4. Write output to the project's literature/ or analysis/ directory
5. If you find important follow-up questions, note them but do NOT create new tasks

{constraints}
"""


def _build_implementation_prompt(
    task: FleetTask,
    project_context: str,
    session_id: str,
    constraints: str,
) -> str:
    return f"""\
You are a fleet implementation worker (session: {session_id}).
Your role: write code, tests, and technical artifacts.

## Project Context
{project_context}

## Assignment
{_build_task_details(task)}

## Your Approach
1. Read relevant existing code to understand the current state
2. Plan your changes (keep them minimal and focused)
3. Implement the changes
4. Verify your changes work (run tests if applicable)
5. Commit with a clear message including [fleet/{session_id}]

{constraints}
"""


def _build_default_prompt(
    task: FleetTask,
    project_context: str,
    session_id: str,
    constraints: str,
) -> str:
    return f"""\
You are a fleet worker (session: {session_id}).
Complete the assigned task efficiently and accurately.

## Project Context
{project_context}

## Assignment
{_build_task_details(task)}

## Your Approach
1. Understand the task requirements
2. Gather context from existing files
3. Execute the task
4. Verify your work
5. Commit results with [fleet/{session_id}] in the message

{constraints}
"""


def build_fleet_prompt(
    task: FleetTask,
    session_id: str,
    repo_root: Path,
    worker_role: WorkerRole = WorkerRole.DEFAULT,
    max_turns: int = 64,
) -> str:
    """Build a self-contained prompt for a fleet worker.

    Pulls project context from README.md, selects role-specific template,
    and appends shared constraints.
    """
    readme_path = repo_root / "projects" / task.project / "README.md"
    project_context = extract_project_context(readme_path)
    constraints = SHARED_CONSTRAINTS.format(
        session_id=session_id,
        max_turns=max_turns,
    )

    builders = {
        WorkerRole.KNOWLEDGE: _build_knowledge_prompt,
        WorkerRole.IMPLEMENTATION: _build_implementation_prompt,
        WorkerRole.DEFAULT: _build_default_prompt,
    }

    builder = builders.get(worker_role, _build_default_prompt)
    return builder(task, project_context, session_id, constraints)
