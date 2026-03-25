#!/usr/bin/env python3
"""Classify repo-available multi-agent survey entries into synthesis themes.

Provenance scope:
- projects/multi-agent-survey/literature/icml-2023-2025.md
- projects/multi-agent-survey/literature/iclr-2025-2026.md
- projects/multi-agent-survey/literature/neurips-2024-2025.md

The rules are intentionally title/tag based and may assign multiple themes.
They are meant for high-level survey synthesis, not definitive ontology labeling.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "ICML": ROOT / "literature" / "icml-2023-2025.md",
    "ICLR": ROOT / "literature" / "iclr-2025-2026.md",
    "NeurIPS": ROOT / "literature" / "neurips-2024-2025.md",
}

THEMES = [
    "协作规划",
    "通信",
    "博弈/对齐",
    "工具使用",
    "多智能体LLM系统",
    "训练与评测",
]

TITLE_PATTERNS = {
    "协作规划": [
        r"\bplan(?:ning)?\b",
        r"pathfinding",
        r"path gen",
        r"pathgen",
        r"scheduling",
        r"coordination",
        r"cooperation",
        r"collaboration",
        r"trajectory",
        r"teamwork",
        r"world models?",
        r"traffic signal control",
        r"travel planning",
        r"option discovery",
    ],
    "通信": [
        r"communication",
        r"debate",
        r"discussion",
        r"semantic communication",
        r"kv sharing",
        r"information bottleneck",
        r"summarize by learning to quiz",
        r"message",
    ],
    "博弈/对齐": [
        r"game[- ]theoretic",
        r"game",
        r"stackelberg",
        r"equilibr",
        r"alignment",
        r"preference",
        r"human values",
        r"social dilemma",
        r"adversar",
        r"robust",
        r"deception",
        r"collusion",
        r"fair",
        r"welfare",
    ],
    "工具使用": [
        r"tool[- ]use",
        r"computer-using",
        r"gui",
        r"coding",
        r"software development",
        r"text-to-sql",
        r"automl",
        r"github issue resolution",
        r"issue resolution",
        r"mobile device operation",
        r"world model by writing code",
    ],
    "多智能体LLM系统": [
        r"\bllm\b",
        r"large language model",
        r"language models?",
        r"graph-of-agents",
        r"multi-agent systems?",
        r"agentic",
        r"society",
        r"swarm",
        r"multi-llm",
        r"reasoning",
        r"debater",
    ],
    "训练与评测": [
        r"benchmark",
        r"evaluation",
        r"eval",
        r"suite",
        r"training",
        r"fine-tun",
        r"post-training",
        r"distill",
        r"curriculum",
        r"failure attribution",
        r"debug",
        r"security benchmark",
        r"test-time",
    ],
}

TAG_HINTS = {
    "Communication": "通信",
    "Coordination": "协作规划",
    "Evaluation": "训练与评测",
}

ENTRY_RE = re.compile(r"^\d+\. \*\*(.+?)\*\*", re.M)
YEAR_RE = re.compile(r"- Year: (\d{4})")
AUTH_RE = re.compile(r"- Authors?: (.+)")
TAG_RE = re.compile(r"- Tags?: (.+)")


def parse_entries(text: str):
    entries = []
    matches = list(ENTRY_RE.finditer(text))
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        block = text[start:end]
        title = match.group(1).strip()
        year_match = YEAR_RE.search(block)
        tags_match = TAG_RE.search(block)
        venue = None
        entries.append(
            {
                "title": title,
                "year": int(year_match.group(1)) if year_match else None,
                "tags": [t.strip() for t in tags_match.group(1).split(",")] if tags_match else [],
                "block": block,
            }
        )
    return entries


def classify(entry):
    title = entry["title"].lower()
    themes = set()
    for tag in entry["tags"]:
        for key, theme in TAG_HINTS.items():
            if key.lower() in tag.lower():
                themes.add(theme)
    for theme, patterns in TITLE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, title):
                themes.add(theme)
                break
    if not themes:
        if "agent" in title:
            themes.add("多智能体LLM系统")
        else:
            themes.add("协作规划")
    return sorted(themes)


def top_examples(entries, theme, n=8):
    picked = []
    for e in entries:
        if theme in e["themes"]:
            picked.append({"title": e["title"], "year": e["year"], "venue": e["venue"]})
        if len(picked) >= n:
            break
    return picked


def main():
    all_entries = []
    venue_counts = {}
    for venue, path in FILES.items():
        text = path.read_text(encoding="utf-8")
        entries = parse_entries(text)
        for e in entries:
            e["venue"] = venue
            e["themes"] = classify(e)
        all_entries.extend(entries)
        venue_counts[venue] = len(entries)

    theme_counts = Counter()
    venue_theme_counts = defaultdict(Counter)
    year_theme_counts = defaultdict(Counter)
    for e in all_entries:
        for theme in e["themes"]:
            theme_counts[theme] += 1
            venue_theme_counts[e["venue"]][theme] += 1
            if e["year"] is not None:
                year_theme_counts[str(e["year"])][theme] += 1

    result = {
        "files": {k: str(v.relative_to(ROOT)) for k, v in FILES.items()},
        "entry_count": len(all_entries),
        "venue_counts": venue_counts,
        "theme_counts": dict(theme_counts),
        "venue_theme_counts": {k: dict(v) for k, v in venue_theme_counts.items()},
        "year_theme_counts": {k: dict(v) for k, v in year_theme_counts.items()},
        "examples": {theme: top_examples(all_entries, theme) for theme in THEMES},
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
