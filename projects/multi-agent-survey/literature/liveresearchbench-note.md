# Literature Note — LiveResearchBench: Benchmarking Single- and Multi-Agent Systems for Citation-Grounded Deep Research

- Timestamp: 2026-03-24T21:34:46+08:00
- Category: Evaluation
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/iclr-2025-2026.md`, entry 103.
  - Novelty check from `search_text("A2ASecBench|LiveResearchBench|Collaborative Gym|DoVer|EduVisAgent|SocialJax", "projects/multi-agent-survey", max_results=50)`, which returned no matches before this note was written.

## Citation

Jiayu Wang, Yifei Ming, Riya Dulepet, Qinglin Chen, Austin Xu, Zixuan Ke, Frederic Sala, Aws Albarghouthi, Caiming Xiong, Shafiq Joty. **LiveResearchBench: Benchmarking Single- and Multi-Agent Systems for Citation-Grounded Deep Research**. ICLR 2026 Poster. OpenReview: `https://openreview.net/forum?id=ghwbZ3uhEd`.

## What this paper appears to study

From the verified title and repository tags, this paper benchmarks both **single-agent** and **multi-agent** systems on **citation-grounded deep research** tasks. That makes it directly relevant to two core project questions: whether ICLR 2026 contains new multi-agent evaluation benchmark work, and where the practical boundary lies between single-agent and multi-agent setups.

## What we can verify from current repository state

1. It is an explicit **benchmarking** paper rather than only an application demo.
2. Its comparison target includes both **single-agent** and **multi-agent** systems.
3. Its task framing is **citation-grounded deep research**, which is highly relevant to agentic workflows that require retrieval, synthesis, and source attribution.
4. The repository currently tags it as `Architecture, Evaluation, Application`.
5. It is listed as an **ICLR 2026 Poster** in the venue-constrained harvest.

## Evidence from source

Verified metadata from `projects/multi-agent-survey/literature/iclr-2025-2026.md`, entry 103:
> **LiveResearchBench: Benchmarking Single- and Multi-Agent Systems for Citation-Grounded Deep Research**
>
> Presentation: Poster
>
> Tags: Architecture, Evaluation, Application
>
> OpenReview: https://openreview.net/forum?id=ghwbZ3uhEd

## Why it matters for the survey

- This is the clearest in-repo ICLR 2026 evidence so far for a benchmark that **directly compares single-agent and multi-agent systems** rather than evaluating only one side.
- It therefore bears directly on the survey's open boundary question: when does multi-agent structure outperform a strong single-agent baseline with tools?
- It also suggests that by 2026, evaluation is moving from generic task success toward **source-grounded research-style workflows**, where citation fidelity is part of the benchmark target.

## Limits / caveats

1. In this session, the repository can verify the title, venue label, tags, and OpenReview link, but not the full abstract or results table, because direct OpenReview access returned HTTP 403 in this environment.
   - Provenance: `python3` requests to `https://openreview.net/forum?id=ghwbZ3uhEd` and `https://api.openreview.net/notes?forum=ghwbZ3uhEd` returned `403 Forbidden` during this session.
2. This note should therefore be treated as a **provisional load-bearing candidate note**, not yet a full deep-reading note.
3. Whether it should enter the repository's final `load-bearing` set depends on later abstract/result extraction and comparison against other ICLR 2026 benchmark papers such as `A2ASecBench` and `SocialJax` already listed in `iclr-2025-2026.md`.

## Relevance to open questions

- **ICLR 2026 是否有关于 multi-agent evaluation benchmark 的新工作？** Yes: the repository now has a verified ICLR 2026 benchmark candidate with an explicit single-vs-multi-agent comparison framing.
- **Multi-Agent 与 Single-Agent + tools 的性能边界在哪里？什么时候值得用多智能体？** This paper is one of the strongest current candidates for answering that question empirically.

## One-sentence takeaway

LiveResearchBench is a high-value new benchmark candidate because it appears to evaluate the single-agent vs multi-agent boundary on citation-grounded deep-research tasks, which is exactly the comparison the survey still needs.