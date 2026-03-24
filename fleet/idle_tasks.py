"""Idle exploration tasks for fleet workers when the task queue is empty.

Aligned with upstream idle-tasks.ts + ADR 0048:
  - Exploration types: horizon-scan, self-audit, stale-blocker-check, open-question
  - Weighted random selection with per-project+type cooldown
  - Curated prompt templates per exploration type
  - Zero-commit is valid behavior
"""

from __future__ import annotations

import json
import random
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .prompt_builder import extract_project_context

IDLE_COOLDOWN_SECONDS = 21600  # 6 hours default

TYPE_WEIGHTS: dict[str, int] = {
    "horizon-scan": 3,
    "self-audit": 1,
    "stale-blocker-check": 1,
    "open-question": 2,
}

TYPE_COOLDOWNS: dict[str, int] = {
    "horizon-scan": 21600,
    "self-audit": 21600,
    "stale-blocker-check": 43200,  # 12 hours
    "open-question": 21600,
}


@dataclass
class ExplorationTopic:
    type: str
    project: str
    context: str
    weight: int = 1


def topic_key(topic: ExplorationTopic) -> str:
    return f"{topic.project}:{topic.type}"


def load_cooldown_map(repo_root: Path, now: float | None = None) -> dict[str, float]:
    """Load cooldown map from .fleet/idle-cooldown.json, pruning expired entries."""
    if now is None:
        now = time.time()
    path = repo_root / ".fleet" / "idle-cooldown.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}

    pruned = {k: v for k, v in data.items() if v > now - max(TYPE_COOLDOWNS.values())}
    return pruned


def save_cooldown_map(repo_root: Path, cooldown_map: dict[str, float]) -> None:
    path = repo_root / ".fleet" / "idle-cooldown.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cooldown_map, indent=2), encoding="utf-8")


def gather_exploration_topics(repo_root: Path) -> list[ExplorationTopic]:
    """Gather exploration topics from all projects."""
    topics: list[ExplorationTopic] = []
    projects_dir = repo_root / "projects"

    if not projects_dir.is_dir():
        return topics

    for project_dir in sorted(projects_dir.iterdir()):
        if not project_dir.is_dir():
            continue

        project_name = project_dir.name
        readme = project_dir / "README.md"
        readme_content = ""
        if readme.is_file():
            readme_content = readme.read_text(errors="replace")

        mission_match = re.search(r"Mission:\s*(.+)", readme_content, re.IGNORECASE)
        mission = mission_match.group(1).strip() if mission_match else ""

        if mission:
            topics.append(ExplorationTopic(
                type="horizon-scan",
                project=project_name,
                context=f"Mission: {mission}",
                weight=TYPE_WEIGHTS["horizon-scan"],
            ))

        topics.append(ExplorationTopic(
            type="self-audit",
            project=project_name,
            context=f"Audit conventions and quality for {project_name}",
            weight=TYPE_WEIGHTS["self-audit"],
        ))

        tasks_file = project_dir / "TASKS.md"
        if tasks_file.is_file():
            tasks_content = tasks_file.read_text(errors="replace")
            blocked_lines = [
                l.strip() for l in tasks_content.splitlines()
                if "[blocked-by:" in l and "external" in l.lower()
            ]
            for bl in blocked_lines[:3]:
                topics.append(ExplorationTopic(
                    type="stale-blocker-check",
                    project=project_name,
                    context=f"Verify: {bl[:120]}",
                    weight=TYPE_WEIGHTS["stale-blocker-check"],
                ))

        open_qs = re.search(
            r"## Open questions\s*\n((?:(?!##).+\n)*)", readme_content
        )
        if open_qs:
            questions = [
                q.strip().lstrip("- ")
                for q in open_qs.group(1).strip().splitlines()
                if q.strip() and q.strip() != "(to be filled)"
            ]
            for q in questions[:3]:
                topics.append(ExplorationTopic(
                    type="open-question",
                    project=project_name,
                    context=q,
                    weight=TYPE_WEIGHTS["open-question"],
                ))

    return topics


def _is_on_cooldown(key: str, cooldown_map: dict[str, float], now: float) -> bool:
    last = cooldown_map.get(key)
    if last is None:
        return False
    topic_type = key.split(":")[-1] if ":" in key else ""
    cooldown = TYPE_COOLDOWNS.get(topic_type, IDLE_COOLDOWN_SECONDS)
    return (now - last) < cooldown


def select_topics(
    topics: list[ExplorationTopic],
    cooldown_map: dict[str, float],
    count: int,
    now: float | None = None,
) -> list[ExplorationTopic]:
    """Select topics with cooldown filtering and weighted random sampling."""
    if now is None:
        now = time.time()

    eligible = [
        t for t in topics
        if not _is_on_cooldown(topic_key(t), cooldown_map, now)
    ]

    if not eligible:
        return []

    selected: list[ExplorationTopic] = []
    remaining = list(eligible)

    for _ in range(min(count, len(remaining))):
        if not remaining:
            break
        weights = [t.weight for t in remaining]
        total = sum(weights)
        if total == 0:
            break
        r = random.uniform(0, total)
        cumulative = 0
        for i, t in enumerate(remaining):
            cumulative += t.weight
            if r <= cumulative:
                selected.append(t)
                remaining.pop(i)
                break

    return selected


PROMPT_TEMPLATES: dict[str, str] = {
    "horizon-scan": """\
You are performing a horizon scan for project "{project}".

{project_context}

## Your Task
Scan for new developments related to: {context}

1. Search existing literature/ for what we already know
2. Identify any gaps or new directions not yet captured
3. If you find something genuinely new, write a brief note to literature/
4. If nothing new, make zero commits — that is correct behavior

## Constraints
- Maximum 1 literature note per session
- Do not create new tasks
- Focus on quality over quantity
""",

    "self-audit": """\
You are performing a self-audit for project "{project}".

{project_context}

## Your Task
{context}

1. Check that README.md conventions are followed
2. Verify TASKS.md formatting is consistent
3. Look for stale or contradictory information
4. If you find real issues, fix them in-place
5. If everything looks good, make zero commits

## Constraints
- Only fix genuine issues, not cosmetic preferences
- Do not restructure or rewrite working content
- Add a brief log entry to README if you fixed something
""",

    "stale-blocker-check": """\
You are verifying an external blocker for project "{project}".

{project_context}

## Your Task
{context}

1. Check if this blocker is still valid
2. If the blocker is resolved, update the TASKS.md tag
3. If still blocked, leave as-is
4. Do NOT remove blockers you cannot verify

## Constraints
- Be conservative — only unblock if you have evidence
- Note your finding in a brief comment
""",

    "open-question": """\
You are investigating an open question for project "{project}".

{project_context}

## Your Task
Investigate: {context}

1. Search existing project files for relevant context
2. Synthesize what we know
3. If you can provide a useful answer, write it to the README log
4. If more research is needed, note what specifically

## Constraints
- Do not create new tasks
- One log entry maximum
- If the question requires external research beyond repo, note that and exit
""",
}


def build_idle_prompt(
    topic: ExplorationTopic,
    session_id: str,
    repo_root: Path,
) -> str:
    """Build a prompt for an idle exploration session."""
    readme_path = repo_root / "projects" / topic.project / "README.md"
    project_context = extract_project_context(readme_path)

    template = PROMPT_TEMPLATES.get(topic.type, PROMPT_TEMPLATES["self-audit"])
    return template.format(
        project=topic.project,
        project_context=project_context,
        context=topic.context,
        session_id=session_id,
    )
