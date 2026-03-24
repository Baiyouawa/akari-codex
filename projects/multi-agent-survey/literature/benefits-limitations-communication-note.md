# Literature Note — Benefits and Limitations of Communication in Multi-Agent Reasoning

- Timestamp: 2026-03-24T13:19:06Z
- Category: Communication, Theory
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/iclr-2025-2026.md`, 2026 entry 65.
  - Repository-internal tags in that artifact: `Communication, Theory`.

## Citation

Michael Rizvi-Martel, Satwik Bhattamishra, Neil Rathi, Guillaume Rabusseau, Michael Hahn. **Benefits and Limitations of Communication in Multi-Agent Reasoning**. ICLR 2026 Poster. OpenReview: `https://openreview.net/forum?id=0aPIVJUz5T`.

## What this paper studies

From the verified title and tags, the paper studies not only the benefits but also the limits of communication in multi-agent reasoning.

## Key contributions we can verify from repository state

1. The paper is explicitly centered on **communication**.
2. It is also tagged **Theory**, suggesting it aims at a general claim rather than only a benchmark trick.
3. The title directly aligns with the project's open question about when multi-agent communication helps and when it may not.

## Evidence from source

Verified title from `projects/multi-agent-survey/literature/iclr-2025-2026.md`:
> "Benefits and Limitations of Communication in Multi-Agent Reasoning"

Repository metadata from the same artifact:
- Presentation: `Poster`
- Tags: `Communication, Theory`
- Retrieved via: `ICLR 2026 Poster schedule page`

## Why it matters for the survey

- Many multi-agent papers assume more communication is better; this title suggests a more balanced framing.
- A paper about both benefits and limitations is especially valuable for the survey's boundary question against strong single-agent baselines.
- It may provide principled conditions under which communication helps, saturates, or harms reasoning.

## Theory lens

This paper should be read as a boundary-setting communication paper:
- identify gains from interaction,
- identify failure modes or diminishing returns,
- clarify whether communication is necessary or only sometimes useful.

## Limits / caveats

1. The repository verifies title, venue, and tags, but not the abstract or formal results.
2. We therefore avoid claiming specific theorems, benchmarks, or effect sizes.
3. A future deeper note should verify what kinds of reasoning tasks were studied and how "limitation" was operationalized.

## Relevance to open questions

- **Multi-Agent 与 Single-Agent + tools 的性能边界在哪里？什么时候值得用多智能体？** This is the most directly relevant paper in the current repo to that question.
- **Agent-to-agent communication 的最新范式是什么？** It may help distinguish useful communication from wasteful or harmful interaction.

## One-sentence takeaway

This paper is load-bearing because it appears to ask the survey's central question directly: when does communication actually improve multi-agent reasoning, and when does it not?