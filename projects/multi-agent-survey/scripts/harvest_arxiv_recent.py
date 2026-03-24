#!/usr/bin/env python3
"""Harvest recent arXiv multi-agent preprints for the survey project.

Method:
- Query arXiv Atom API with several MAS-related search strings.
- Keep entries published within 2026-01-01 to 2026-03-23.
- Deduplicate by arXiv id.
- Require at least one MAS keyword in title+summary.
- Assign lightweight topic tags from title/summary heuristics.
- Emit a month-grouped markdown artifact.

This script is designed for provenance-first literature collection, not for
claiming exhaustive coverage of all arXiv papers.
"""

from __future__ import annotations

import textwrap
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

OUTPUT = Path("projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md")
START = datetime(2026, 1, 1, tzinfo=timezone.utc)
END = datetime(2026, 3, 23, 23, 59, 59, tzinfo=timezone.utc)
MAX_RESULTS = 100
TARGET_PER_MONTH = {"2026-01": 10, "2026-02": 10, "2026-03": 12}

QUERIES = [
    'all:"multi-agent"',
    'all:multiagent',
    'all:"multi-agent system"',
    'all:"multi-agent reinforcement learning"',
    'all:MARL',
    'all:"agent collaboration"',
    'all:"cooperative agents"',
]

MAS_KEYWORDS = [
    "multi-agent",
    "multi agent",
    "multiagent",
    "marl",
    "agent collaboration",
    "cooperative agents",
    "group-of-agents",
]

NS = {"a": "http://www.w3.org/2005/Atom"}
ARXIV_NS = {**NS, "arxiv": "http://arxiv.org/schemas/atom"}


def fetch_query(query: str):
    params = {
        "search_query": query,
        "start": 0,
        "max_results": MAX_RESULTS,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as response:
        data = response.read()
    root = ET.fromstring(data)
    return url, root.findall("a:entry", NS)


def normalize(text: str) -> str:
    return " ".join((text or "").split())


def parse_authors(entry) -> str:
    authors = [normalize(a.findtext("a:name", default="", namespaces=NS)) for a in entry.findall("a:author", NS)]
    return ", ".join([a for a in authors if a])


def classify(text: str):
    text = text.lower()
    tags = []
    if any(k in text for k in ["framework", "architecture", "system", "topology", "orchestration", "group-of-agents"]):
        tags.append("Architecture")
    if any(k in text for k in ["coordination", "collaboration", "task allocation", "team", "co-evolutionary"]):
        tags.append("Coordination")
    if any(k in text for k in ["communication", "message", "shared memory", "protocol"]):
        tags.append("Communication")
    if any(k in text for k in ["benchmark", "evaluation", "metric", "assess", "judge", "critic"]):
        tags.append("Evaluation")
    if any(k in text for k in ["cybersecurity", "physics", "robot", "uav", "driving", "inspection", "satellite", "software", "prompt optimization"]):
        tags.append("Application")
    if any(k in text for k in ["game", "theory", "equilibrium", "prisoner", "potential game"]):
        tags.append("Theory")
    if any(k in text for k in ["reinforcement learning", "marl", "policy", "q-learning", "value estimation"]):
        tags.append("Theory/MARL")
    if not tags:
        tags.append("Unclassified")
    out = []
    for tag in tags:
        if tag not in out:
            out.append(tag)
    return out


def is_mas_relevant(title: str, summary: str) -> bool:
    text = (title + " " + summary).lower()
    return any(k in text for k in MAS_KEYWORDS)


def format_counter(counter: Counter) -> str:
    return ", ".join(f"{k} = {counter[k]}" for k in sorted(counter))


def main():
    records = {}
    query_hit_counts = {}

    for query in QUERIES:
        url, entries = fetch_query(query)
        kept = 0
        for entry in entries:
            published = normalize(entry.findtext("a:published", default="", namespaces=NS))
            if not published:
                continue
            published_dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
            if published_dt < START or published_dt > END:
                continue

            title = normalize(entry.findtext("a:title", default="", namespaces=NS))
            summary = normalize(entry.findtext("a:summary", default="", namespaces=NS))
            if not is_mas_relevant(title, summary):
                continue

            arxiv_id_url = normalize(entry.findtext("a:id", default="", namespaces=NS))
            short_id = arxiv_id_url.rsplit("/", 1)[-1]
            primary_category = ""
            primary = entry.find("a:primary_category", ARXIV_NS)
            if primary is not None:
                primary_category = primary.attrib.get("term", "")
            authors = parse_authors(entry)
            comment = normalize(entry.findtext("arxiv:comment", default="", namespaces=ARXIV_NS))
            rec = records.setdefault(
                short_id,
                {
                    "id": short_id,
                    "id_url": arxiv_id_url,
                    "published": published,
                    "title": title,
                    "summary": summary,
                    "authors": authors,
                    "primary_category": primary_category,
                    "comment": comment,
                    "queries": set(),
                },
            )
            rec["queries"].add(query)
            kept += 1
        query_hit_counts[query] = {"url": url, "kept": kept}

    month_groups = defaultdict(list)
    for rec in records.values():
        month_groups[rec["published"][:7]].append(rec)

    selected = {}
    selected_all = []
    for month, target in TARGET_PER_MONTH.items():
        bucket = sorted(month_groups.get(month, []), key=lambda r: (r["published"], r["id"]), reverse=True)
        selected[month] = bucket[:target]
        selected_all.extend(selected[month])

    selected_total = sum(len(v) for v in selected.values())
    harvested_total = len(records)
    month_counts = Counter(rec["published"][:7] for rec in records.values())
    selected_tag_counts = Counter()
    monthly_tag_counts = {}
    for month, bucket in selected.items():
        counter = Counter()
        for rec in bucket:
            tags = classify(rec["title"] + " " + rec["summary"])
            rec["tags"] = tags
            counter.update(tags)
            selected_tag_counts.update(tags)
        monthly_tag_counts[month] = counter

    lines = []
    lines.append("# arXiv Multi-Agent preprints (2026-01 to 2026-03)")
    lines.append("")
    lines.append("Source: arXiv Atom API, harvested by `projects/multi-agent-survey/scripts/harvest_arxiv_recent.py` in this session.")
    lines.append("")
    lines.append("Method:")
    lines.append("- Time window: 2026-01-01 to 2026-03-23 UTC.")
    lines.append(f"- Query set ({len(QUERIES)}): " + ", ".join(f"`{q}`" for q in QUERIES) + ".")
    lines.append("- Retrieval: `sortBy=submittedDate`, `sortOrder=descending`, `max_results=100` for each query.")
    lines.append("- Deduplication: arXiv identifier.")
    lines.append("- Relevance filter: title+abstract must contain at least one MAS keyword (`multi-agent`, `multi agent`, `multiagent`, `MARL`, `agent collaboration`, `cooperative agents`, `group-of-agents`).")
    lines.append("- Selection for this artifact: keep the most recent month-grouped subset (10 papers for 2026-01, 10 for 2026-02, 12 for 2026-03) to satisfy the survey task while preserving provenance of the broader harvest.")
    lines.append("- Caveat: this is a reproducible retrieval snapshot, not a claim of exhaustive arXiv coverage.")
    lines.append("")
    lines.append("Harvest summary:")
    lines.append(f"- Unique relevant records harvested in window: {harvested_total}.")
    lines.append(f"- Month counts from the harvested pool: 2026-01 = {month_counts.get('2026-01', 0)}, 2026-02 = {month_counts.get('2026-02', 0)}, 2026-03 = {month_counts.get('2026-03', 0)}.")
    lines.append(f"- Records selected into this literature list: {selected_total} = 10 + 10 + 12.")
    lines.append(f"- Classification counts across the 32 selected papers: {format_counter(selected_tag_counts)}.")
    lines.append("")
    lines.append("Query provenance:")
    for query in QUERIES:
        lines.append(f"- {query}: kept {query_hit_counts[query]['kept']} in-window relevant records via `{query_hit_counts[query]['url']}`")
    lines.append("")

    for month in ["2026-01", "2026-02", "2026-03"]:
        lines.append(f"## {month}")
        lines.append("")
        bucket = selected.get(month, [])
        lines.append(f"Selected papers: {len(bucket)} (from {month_counts.get(month, 0)} harvested records in this month).")
        lines.append(f"Classification counts in selected subset: {format_counter(monthly_tag_counts.get(month, Counter()))}.")
        lines.append("")
        for idx, rec in enumerate(bucket, 1):
            tags = ", ".join(rec["tags"])
            lines.append(f"{idx}. **{rec['title']}**")
            lines.append(f"   - Published: {rec['published']}")
            lines.append(f"   - Authors: {rec['authors']}")
            lines.append(f"   - arXiv: {rec['id_url']}")
            lines.append(f"   - Primary category: {rec['primary_category'] or 'n/a'}")
            lines.append(f"   - Tags: {tags}")
            lines.append(f"   - Matched queries: {', '.join(sorted(rec['queries']))}")
            if rec["comment"]:
                lines.append(f"   - Comment: {rec['comment']}")
            lines.append(f"   - Abstract snippet: {textwrap.shorten(rec['summary'], width=240, placeholder='...')}")
        lines.append("")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    print(f"Harvested unique records: {harvested_total}")
    print(f"Selected classification counts: {format_counter(selected_tag_counts)}")
    for month in ["2026-01", "2026-02", "2026-03"]:
        print(f"{month}: harvested {month_counts.get(month, 0)}, selected {len(selected.get(month, []))}, tags {format_counter(monthly_tag_counts.get(month, Counter()))}")


if __name__ == "__main__":
    main()
