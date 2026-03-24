#!/usr/bin/env python3
"""Harvest NeurIPS multi-agent candidates from Crossref.

Provenance:
- Source API: https://api.crossref.org/works
- Retrieval heuristic: query within NeurIPS proceedings container title and keyword-match
  titles/abstract surrogates from the returned records.
- This script intentionally preserves an explicit note when 2025 venue-constrained
  retrieval does not return NeurIPS proceedings records in the current index snapshot.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request
from collections import OrderedDict
from pathlib import Path

USER_AGENT = "OpenAkari-Codex/0.1 (mailto:research@example.com)"
CROSSREF = "https://api.crossref.org/works"
CONTAINER = "Advances in Neural Information Processing Systems"
KEYWORDS = [
    "multi-agent",
    "multi agent",
    "agent",
    "agents",
    "coordination",
    "communication",
    "cooperative",
    "teamwork",
    "collaboration",
    "reinforcement learning",
]
QUERIES = [
    "multi-agent",
    "agent",
    "cooperative",
    "coordination",
    "communication",
    "teamwork",
    "collaboration",
    '"reinforcement learning"',
]


def fetch(params: dict) -> dict:
    url = CROSSREF + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def normalize_title(item: dict) -> str:
    title = (item.get("title") or [""])[0]
    return " ".join(title.split())


def authors(item: dict) -> str:
    names = []
    for a in item.get("author", []):
        given = a.get("given", "").strip()
        family = a.get("family", "").strip()
        full = " ".join(x for x in [given, family] if x)
        if full:
            names.append(full)
    return ", ".join(names)


def year_of(item: dict) -> str:
    for key in ("published-print", "published-online", "issued"):
        date = item.get(key, {}).get("date-parts")
        if date and date[0]:
            return str(date[0][0])
    return "unknown"


def score(title: str) -> int:
    lower = title.lower()
    return sum(1 for kw in KEYWORDS if kw in lower)


def classify(title: str) -> list[str]:
    lower = title.lower()
    tags = []
    if any(k in lower for k in ["framework", "system", "collaboration", "assistant"]):
        tags.append("Architecture")
    if any(k in lower for k in ["coordination", "teamwork", "allocation"]):
        tags.append("Coordination")
    if any(k in lower for k in ["communication", "message", "memory"]):
        tags.append("Communication")
    if any(k in lower for k in ["benchmark", "evaluation", "assessing"]):
        tags.append("Evaluation")
    if any(k in lower for k in ["software", "mathematical", "mobile", "device", "health"]):
        tags.append("Application")
    if any(k in lower for k in ["game", "regret", "equilibr", "learning"]):
        tags.append("Theory/MARL")
    if not tags:
        tags.append("Unclassified")
    return tags


def harvest(year: int) -> tuple[list[dict], list[str]]:
    rows = []
    notes = []
    seen = OrderedDict()
    for q in QUERIES:
        params = {
            "query": q,
            "query.container-title": CONTAINER,
            "filter": f"from-pub-date:{year}-01-01,until-pub-date:{year}-12-31",
            "rows": "50",
        }
        try:
            data = fetch(params)
        except Exception as exc:  # noqa: BLE001
            notes.append(f"query={q!r} failed with {type(exc).__name__}: {exc}")
            continue
        items = data.get("message", {}).get("items", [])
        matched_container = 0
        for item in items:
            container = (item.get("container-title") or [""])[0]
            title = normalize_title(item)
            if not title:
                continue
            if "advances in neural information processing systems" not in container.lower():
                continue
            matched_container += 1
            if score(title) <= 0:
                continue
            doi = item.get("DOI", "")
            key = doi or title.lower()
            if key in seen:
                continue
            seen[key] = {
                "title": title,
                "authors": authors(item),
                "year": year_of(item),
                "link": f"https://doi.org/{doi}" if doi else item.get("URL", ""),
                "tags": classify(title),
                "query": q,
            }
        notes.append(
            f"query={q!r}: {len(items)} items returned, {matched_container} with NeurIPS container-title"
        )
        time.sleep(1.0)
    rows = sorted(seen.values(), key=lambda x: (-score(x["title"]), x["title"].lower()))
    if year == 2025 and not rows:
        notes.append(
            "No NeurIPS 2025 records survived venue-constrained Crossref retrieval in this session;"
            " likely indexing lag or proceedings metadata mismatch."
        )
    return rows, notes


def render(year_to_rows: dict[int, list[dict]], year_to_notes: dict[int, list[str]]) -> str:
    total = sum(len(v) for v in year_to_rows.values())
    lines = [
        "# NeurIPS 2024-2025 Multi-Agent candidate list",
        "",
        "Source: Crossref `works` API queried by `projects/multi-agent-survey/scripts/harvest_neurips_crossref.py`.",
        "",
        "Method:",
        f"- Venue filter: container-title contains `{CONTAINER}`.",
        "- Year filter: publication year 2024 and 2025 separately.",
        f"- Query set: {', '.join(QUERIES)}.",
        "- Relevance heuristic: keep titles containing at least one agent/MAS-related keyword; assign lightweight topic tags from title tokens.",
        "- Caveat: this is a retrieval snapshot, not a claim of exhaustive conference coverage.",
        "",
        f"Total harvested candidates: {total}.",
        "",
    ]
    for year in sorted(year_to_rows):
        lines.append(f"## {year}")
        lines.append("")
        lines.append("Retrieval notes:")
        for note in year_to_notes[year]:
            lines.append(f"- {note}")
        lines.append("")
        rows = year_to_rows[year]
        if not rows:
            lines.append("No candidates harvested for this year in the current Crossref snapshot.")
            lines.append("")
            continue
        for i, row in enumerate(rows, 1):
            lines.append(f"{i}. **{row['title']}**")
            lines.append(f"   - Authors: {row['authors'] or 'not returned by Crossref'}")
            lines.append(f"   - Link: {row['link']}")
            lines.append(f"   - Tags: {', '.join(row['tags'])}")
            lines.append(f"   - Retrieved via query: `{row['query']}`")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    out = Path("projects/multi-agent-survey/literature/neurips-2024-2025.md")
    year_to_rows = {}
    year_to_notes = {}
    for year in (2024, 2025):
        rows, notes = harvest(year)
        year_to_rows[year] = rows
        year_to_notes[year] = notes
    text = render(year_to_rows, year_to_notes)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out}")
    for year, rows in year_to_rows.items():
        print(year, len(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
