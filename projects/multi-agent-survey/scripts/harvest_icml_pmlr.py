#!/usr/bin/env python3
"""Harvest ICML 2023-2025 multi-agent papers from PMLR proceedings pages.

Provenance:
- ICML 2023: https://proceedings.mlr.press/v202/
- ICML 2024: https://proceedings.mlr.press/v235/
- ICML 2025: https://proceedings.mlr.press/v267/
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "literature" / "icml-2023-2025.md"
YEAR_TO_VOLUME = {2023: 202, 2024: 235, 2025: 267}
USER_AGENT = "Mozilla/5.0 (OpenAkari-Codex research agent)"

INCLUSION_PATTERNS = [
    re.compile(r"\bmulti[ -]?agent(?:s|ic)?\b", re.I),
    re.compile(r"\bagent-to-agent\b", re.I),
    re.compile(r"\bgraph-of-agents\b", re.I),
    re.compile(r"\bagentic collaboration\b", re.I),
    re.compile(r"\bagents?['’]?\s+room\b", re.I),
    re.compile(r"\bmulti-llm-agents?\b", re.I),
]
EXCLUSION_PATTERNS = [re.compile(r"\bsingle-agent\b", re.I)]


@dataclass
class Paper:
    year: int
    title: str
    authors: str
    proceedings_page: str | None
    pdf_url: str | None
    openreview_url: str | None
    tags: list[str]
    source_url: str


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def include_title(title: str) -> bool:
    if any(p.search(title) for p in EXCLUSION_PATTERNS):
        return False
    return any(p.search(title) for p in INCLUSION_PATTERNS)


def infer_tags(title: str) -> list[str]:
    t = title.lower()
    tags: list[str] = []
    if any(k in t for k in ["benchmark", "bench", "evaluation", "suite"]):
        tags.append("Evaluation")
    if any(k in t for k in ["communication", "debate", "discussion", "agent-to-agent", "graph-of-agents"]):
        tags.append("Communication")
    if any(k in t for k in ["cooperation", "cooperative", "coordination", "self-play", "team", "teams"]):
        tags.append("Coordination")
    if any(k in t for k in ["reinforcement learning", "policy", "value", "stochastic game", "marl"]):
        tags.append("Theory/MARL")
    if any(k in t for k in ["traffic", "robot", "robotics", "gui", "medical", "science", "pathology", "search", "visual", "document", "travel"]):
        tags.append("Application")
    if any(k in t for k in ["framework", "system", "systems", "collaboration", "design", "topolog", "llm", "agentic"]):
        tags.append("Architecture")
    return tags or ["Architecture"]


def fetch(year: int, volume: int) -> list[Paper]:
    url = f"https://proceedings.mlr.press/v{volume}/"
    response = requests.get(url, timeout=30, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    papers: list[Paper] = []
    for block in soup.select("div.paper"):
        title_node = block.select_one("p.title")
        authors_node = block.select_one("span.authors")
        if not title_node or not authors_node:
            continue
        title = normalize_ws(title_node.get_text(" ", strip=True))
        if not include_title(title):
            continue
        authors = normalize_ws(authors_node.get_text(" ", strip=True))
        proceedings_page = None
        pdf_url = None
        openreview_url = None
        for link in block.select("p.links a[href]"):
            href = link.get("href")
            label = normalize_ws(link.get_text(" ", strip=True)).lower()
            if label == "abs":
                proceedings_page = href
            elif "pdf" in label:
                pdf_url = href
            elif "openreview" in label or (href and "openreview.net" in href):
                openreview_url = href
        papers.append(Paper(year, title, authors, proceedings_page, pdf_url, openreview_url, infer_tags(title), url))
    papers.sort(key=lambda p: p.title.lower())
    return papers


def build_markdown(all_papers: dict[int, list[Paper]]) -> str:
    total = sum(len(v) for v in all_papers.values())
    lines: list[str] = []
    lines.append("# ICML 2023-2025 Multi-Agent literature list")
    lines.append("")
    lines.append("Source: public Proceedings of Machine Learning Research (PMLR) pages for ICML 2023-2025, harvested by `projects/multi-agent-survey/scripts/harvest_icml_pmlr.py`.")
    lines.append("")
    lines.append("Method:")
    lines.append("- Parsed `div.paper` entries from the ICML PMLR proceedings pages for 2023/2024/2025.")
    lines.append("- Extracted title, authors, proceedings/abstract page, PDF download URL, and OpenReview URL when present in the page card.")
    lines.append("- Kept only titles matching explicit multi-agent cues: `multi-agent`, `multi agent`, `multiagent`, `agent-to-agent`, `graph-of-agents`, `agentic collaboration`, `agents' room`, or `multi-LLM-agents`.")
    lines.append("- Excluded explicit `single-agent` titles.")
    lines.append("- Assigned lightweight topical tags from title keywords; tags are heuristic and not mutually exclusive.")
    lines.append("")
    lines.append("Coverage summary:")
    for year in sorted(all_papers):
        lines.append(f"- {year} papers listed: {len(all_papers[year])}")
    lines.append(f"- Total listed: {total}")
    lines.append(f"- Inline arithmetic: {' + '.join(str(len(all_papers[y])) for y in sorted(all_papers))} = {total}")
    lines.append("")
    lines.append("## Retrieval notes")
    for year, volume in YEAR_TO_VOLUME.items():
        lines.append(f"- {year}: `https://proceedings.mlr.press/v{volume}/`")
    lines.append("")
    for year in sorted(all_papers):
        lines.append(f"## {year}")
        lines.append("")
        if not all_papers[year]:
            lines.append("No matching papers found for this year under the title-screening rule.")
            lines.append("")
            continue
        for idx, paper in enumerate(all_papers[year], start=1):
            lines.append(f"{idx}. **{paper.title}**")
            lines.append(f"   - Authors: {paper.authors}")
            lines.append(f"   - Year: {paper.year}")
            lines.append(f"   - Proceedings page: {paper.proceedings_page or 'Not exposed on page card'}")
            lines.append(f"   - PDF: {paper.pdf_url or 'Not exposed on page card'}")
            lines.append(f"   - OpenReview: {paper.openreview_url or 'Not exposed on page card'}")
            lines.append(f"   - Tags: {', '.join(paper.tags)}")
            lines.append(f"   - Retrieved via: {paper.source_url}")
            lines.append("")
    lines.append("## Quick takeaways")
    lines.append("")
    lines.append("1. PMLR proceedings pages are sufficient to recover venue-verified ICML paper title, authors, proceedings page, PDF, and usually OpenReview metadata without paid APIs.")
    lines.append("   - Provenance: each listed entry comes from one of the three PMLR volume pages above, whose `div.paper` cards expose `abs`, `Download PDF`, and `OpenReview` links.")
    lines.append("")
    lines.append("2. This ICML artifact is intentionally conservative: it captures papers with explicit multi-agent wording in the title, which makes it suitable as a high-precision base list but likely under-recalls implicit collaboration papers.")
    lines.append("   - Provenance: inclusion rule documented above in this file and implemented in `projects/multi-agent-survey/scripts/harvest_icml_pmlr.py`.")
    lines.append("")
    lines.append("3. The PMLR `abs` page can serve as the required conference/proceedings page for the task, while OpenReview remains separately recorded when available.")
    lines.append("   - Provenance: direct HTML inspection in this session showed `div.paper` cards like `... [ abs ][ Download PDF ][ OpenReview ]` on `https://proceedings.mlr.press/v202/`.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    all_papers = {year: fetch(year, volume) for year, volume in YEAR_TO_VOLUME.items()}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_markdown(all_papers), encoding="utf-8")
    for year in sorted(all_papers):
        print(year, len(all_papers[year]))
    print("total", sum(len(v) for v in all_papers.values()))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
