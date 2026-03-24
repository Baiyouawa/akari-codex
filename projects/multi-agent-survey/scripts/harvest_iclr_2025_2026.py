#!/usr/bin/env python3
"""Harvest ICLR 2025-2026 multi-agent papers from public ICLR schedule pages.

Source pages:
- https://iclr.cc/Conferences/2025/Schedule?type=Poster
- https://iclr.cc/Conferences/2025/Schedule?type=Oral
- https://iclr.cc/Conferences/2026/Schedule?type=Poster
- https://iclr.cc/Conferences/2026/Schedule?type=Oral

The schedule HTML exposes per-paper title, author list, OpenReview link, and presentation type
(Poster / Oral). The Spotlight pages were reachable but returned empty placeholder cards during
this session, so this script records spotlight coverage as an observed zero-result condition rather
than asserting that no relevant ICLR spotlight papers exist.
"""
from __future__ import annotations

import html
import re
import urllib.request
from collections import Counter
from pathlib import Path

OUTPUT = Path("projects/multi-agent-survey/literature/iclr-2025-2026.md")

URLS = {
    (2025, "Poster"): "https://iclr.cc/Conferences/2025/Schedule?type=Poster",
    (2025, "Oral"): "https://iclr.cc/Conferences/2025/Schedule?type=Oral",
    (2026, "Poster"): "https://iclr.cc/Conferences/2026/Schedule?type=Poster",
    (2026, "Oral"): "https://iclr.cc/Conferences/2026/Schedule?type=Oral",
}

SPOTLIGHT_URLS = {
    2025: "https://iclr.cc/Conferences/2025/Schedule?type=Spotlight",
    2026: "https://iclr.cc/Conferences/2026/Schedule?type=Spotlight",
}

TITLE_KEYWORDS = [
    "multi-agent",
    "multi agent",
    "multiagent",
    "llm swarm",
    "graph-of-agents",
    "society",
    "debate",
    "coordination",
    "cooperation",
    "cooperative",
    "collaboration",
    "communication",
]

TAG_RULES = [
    ("Architecture", ["framework", "systems", "system", "graph-of-agents", "topologies", "topological", "swarm"]),
    ("Coordination", ["coordination", "cooperation", "cooperative", "joint actions", "subteams"]),
    ("Communication", ["communication", "debate", "discussion", "visual flow"]),
    ("Evaluation", ["benchmark", "bench", "debugging", "bias", "security"]),
    ("Application", ["traffic", "medical", "single-cell", "travel", "chemical", "pathology", "gui", "research"]),
    ("Theory", ["policy optimization", "value factorization", "game", "flow matching", "imitation", "bandit"]),
]

CARD_PATTERN = re.compile(
    r'<div class="maincard narrower (?P<cls>poster|oral)"[^>]*>'
    r'\s*<div class=.float-end maincardHeader maincardType.>(?P<type>.*?)</div>'
    r'\s*<div class="maincardHeader">(?P<header>.*?)</div>'
    r'\s*<div class="maincardBody">(?P<title>.*?)</div>'
    r'\s*.*?<div class="maincardFooter">(?P<authors>.*?)</div>'
    r'.*?<a href="(?P<link>[^"]+)" class="btn btn btn-outline-dark btn-sm href_URL" title="OpenReview">',
    re.S,
)


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "ignore")


def clean(text: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", " ", text)).replace("\xa0", " ").strip()


def parse_cards(year: int, kind: str, html_text: str):
    rows = []
    for match in CARD_PATTERN.finditer(html_text):
        typ = clean(match.group("type"))
        title = clean(match.group("title"))
        authors = clean(match.group("authors"))
        link = match.group("link")
        if not link.startswith("http"):
            link = "https://iclr.cc" + link
        rows.append(
            {
                "year": year,
                "schedule_type": kind,
                "presentation": typ,
                "title": title,
                "authors": authors,
                "openreview": link,
            }
        )
    return rows


def is_relevant(title: str) -> bool:
    lower = title.lower()
    return any(keyword in lower for keyword in TITLE_KEYWORDS)


def tags_for(title: str) -> list[str]:
    lower = title.lower()
    tags = []
    for tag, cues in TAG_RULES:
        if any(cue in lower for cue in cues):
            tags.append(tag)
    return tags or ["Architecture"]


def dedupe(rows):
    best = {}
    score = {"Oral": 2, "Poster": 1, "Blog Track Poster": 0, "Blog Post Poster": 0}
    for row in rows:
        key = (row["year"], row["title"].lower())
        prev = best.get(key)
        if prev is None or score.get(row["presentation"], 0) > score.get(prev["presentation"], 0):
            best[key] = row
    return sorted(best.values(), key=lambda r: (r["year"], r["presentation"] != "Oral", r["title"].lower()))


def spotlight_observation(year: int, html_text: str) -> str:
    populated = html_text.count('class="maincard narrower spotlight"') + html_text.count('class="maincard narrower oral"') + html_text.count('class="maincard narrower poster"')
    placeholders = html_text.count('data-event-id="None"')
    return f"{year}: populated spotlight cards detected = {populated}; placeholder cards detected = {placeholders}."


def main() -> None:
    raw_rows = []
    retrieval_notes = []
    for (year, kind), url in URLS.items():
        html_text = fetch(url)
        rows = parse_cards(year, kind, html_text)
        raw_rows.extend(rows)
        retrieval_notes.append(f"- {year} {kind}: parsed {len(rows)} schedule cards from `{url}`")

    filtered = [row for row in raw_rows if is_relevant(row["title"])]
    deduped = dedupe(filtered)

    spotlight_notes = []
    for year, url in SPOTLIGHT_URLS.items():
        html_text = fetch(url)
        spotlight_notes.append("- " + spotlight_observation(year, html_text) + f" Source: `{url}`")

    year_counts = Counter(row["year"] for row in deduped)
    presentation_counts = Counter(row["presentation"] for row in deduped)

    lines = []
    lines.append("# ICLR 2025-2026 Multi-Agent literature list")
    lines.append("")
    lines.append("Source: public ICLR schedule pages (`iclr.cc/Conferences/<year>/Schedule`) harvested by `projects/multi-agent-survey/scripts/harvest_iclr_2025_2026.py` in this session.")
    lines.append("")
    lines.append("Method:")
    lines.append("- Retrieved populated paper cards from the 2025 and 2026 `Poster` and `Oral` schedule pages.")
    lines.append("- Parsed per-card fields exposed in the HTML: presentation label, title, authors, and OpenReview link.")
    lines.append("- Kept titles matching explicit multi-agent cues (`multi-agent`, `multi agent`, `multiagent`, `collaboration`, `cooperation`, `coordination`, `communication`, `debate`, `graph-of-agents`, `society`, `swarm`).")
    lines.append("- Deduplicated by `(year, lowercase title)`, preferring `Oral` over `Poster` when a paper appeared on both pages.")
    lines.append("- Caveat: the accessible `type=Spotlight` schedule pages returned only placeholder cards during this session, so this artifact contains verified `Oral` and `Poster` labels only and records the spotlight-page observation separately.")
    lines.append("")
    lines.append("Coverage summary:")
    lines.append(f"- 2025 papers listed: {year_counts.get(2025, 0)}")
    lines.append(f"- 2026 papers listed: {year_counts.get(2026, 0)}")
    lines.append(f"- Total listed: {len(deduped)}")
    lines.append(f"- Presentation labels in listed set: {dict(sorted(presentation_counts.items()))}")
    lines.append(f"- Inline arithmetic: {year_counts.get(2025, 0)} + {year_counts.get(2026, 0)} = {len(deduped)}")
    lines.append("")
    lines.append("## Retrieval notes")
    lines.extend(retrieval_notes)
    lines.append("")
    lines.append("## Spotlight-page observation")
    lines.extend(spotlight_notes)
    lines.append("")

    current_year = None
    for idx, row in enumerate(deduped, 1):
        if row["year"] != current_year:
            current_year = row["year"]
            lines.append(f"## {current_year}")
            lines.append("")
        tags = ", ".join(tags_for(row["title"]))
        lines.append(f"{idx}. **{row['title']}**")
        lines.append(f"   - Presentation: {row['presentation']}")
        lines.append(f"   - Authors: {row['authors']}")
        lines.append(f"   - Tags: {tags}")
        lines.append(f"   - OpenReview: {row['openreview']}")
        lines.append(f"   - Retrieved via: ICLR {row['year']} {row['schedule_type']} schedule page")
        lines.append("")

    lines.append("## Quick takeaways")
    lines.append("")
    lines.append("1. The public ICLR schedule pages are sufficient to build a venue-verified 2025-2026 Multi-Agent inventory without external paid APIs.")
    lines.append("   - Provenance: the four schedule URLs listed above were fetched directly by `projects/multi-agent-survey/scripts/harvest_iclr_2025_2026.py`.")
    lines.append("")
    lines.append("2. ICLR 2026 shows a visibly larger multi-agent surface area than ICLR 2025 in this title-screened inventory.")
    lines.append(f"   - Provenance: coverage summary above reports {year_counts.get(2025, 0)} papers for 2025 and {year_counts.get(2026, 0)} for 2026; inline arithmetic difference = {year_counts.get(2026, 0)} - {year_counts.get(2025, 0)} = {year_counts.get(2026, 0) - year_counts.get(2025, 0)}.")
    lines.append("")
    lines.append("3. ICLR 2026 includes multiple explicit evaluation/benchmark papers relevant to the project open question on multi-agent evaluation.")
    lines.append("   - Provenance: listed 2026 entries include `Benchmarking Multi-Agent Reinforcement Learning in Power Grid Operations`, `SocialJax: An Evaluation Suite for Multi-agent Reinforcement Learning in Sequential Social Dilemmas`, `Collaborative Gym: A Framework for Enabling and Evaluating Human-Agent Collaboration`, `A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems`, and `LiveResearchBench: Benchmarking Single- and Multi-Agent Systems for Citation-Grounded Deep Research`.")
    lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    print(f"Total deduped papers: {len(deduped)}")
    print(f"2025 papers: {year_counts.get(2025, 0)}")
    print(f"2026 papers: {year_counts.get(2026, 0)}")
    print(f"Presentation counts: {dict(sorted(presentation_counts.items()))}")


if __name__ == "__main__":
    main()
