# Literature Note — Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems

- Timestamp: 2026-03-24T13:19:06Z
- Category: Communication
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/iclr-2025-2026.md`, 2025 entry 13.
  - Repository-internal tags in that artifact: `Architecture, Communication`.

## Citation

Guibin Zhang, Yanwei Yue, Zhixun Li, Sukwon Yun, Guancheng Wan, Kun Wang, Dawei Cheng, Jeffrey Yu, Tianlong Chen. **Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems**. ICLR 2025 Poster. OpenReview: `https://openreview.net/forum?id=LkzuPorQ5L`.

## What this paper studies

From the verified title and tags, the paper studies how to make communication in LLM-based multi-agent systems more economical.

## Key contributions we can verify from repository state

1. The paper is explicitly about a **communication pipeline** for **LLM-based multi-agent systems**.
2. Its defining objective is **economy/efficiency**, implying reduced communication overhead.
3. It straddles `Architecture` and `Communication`, suggesting that communication cost is a systems-design issue rather than just a prompt-format issue.

## Evidence from source

Verified title from `projects/multi-agent-survey/literature/iclr-2025-2026.md`:
> "Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems"

Repository metadata from the same artifact:
- Presentation: `Poster`
- Tags: `Architecture, Communication`
- Retrieved via: `ICLR 2025 Poster schedule page`

## Why it matters for the survey

- Token and latency cost are a central practical objection to multi-agent systems.
- A paper directly targeting communication economy is therefore load-bearing for answering when multi-agent systems are worth their cost.
- It also indicates that by 2025, communication efficiency had become a first-class research target in LLM-agent systems.

## System lens

This paper is best read as a runtime-efficiency intervention:
- keep multi-agent collaboration,
- redesign the communication pipeline,
- reduce waste in exchanged information.

## Limits / caveats

1. The repository currently verifies title, authors, presentation label, link, and tags, but not abstract text or exact savings.
2. We therefore do not claim any specific token, latency, or accuracy numbers.
3. A future pass should verify whether "economical" means message compression, filtering, selective routing, or protocol redesign.

## Relevance to open questions

- **什么时候值得用多智能体？** Only when coordination gains exceed communication cost; this paper directly addresses that tradeoff.
- **Multi-Agent 与 Single-Agent + tools 的性能边界在哪里？** Communication overhead is one of the main reasons single-agent baselines may remain competitive.

## One-sentence takeaway

This paper is load-bearing because it targets the most practical bottleneck in LLM multi-agent systems: communication has to be cheap enough to justify collaboration.