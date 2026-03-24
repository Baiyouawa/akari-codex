# Literature Note — Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication

- Timestamp: 2026-03-24T13:19:06Z
- Category: Communication
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/neurips-2024-2025.md`, entry 2.
  - Repository-internal tags in that artifact: `Communication, Theory/MARL`.

## Citation

Behdad Chalaki, Kwonjoon Lee, Michael Lewis, Huao Li, Hossein Mahjoub, Ehsan Moradi-Pari, Katia Sycara, Vaishnav Tadiparthi. **Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication**. NeurIPS 2024. DOI: `https://doi.org/10.52202/079017-2790`.

## What this paper studies

From the verified title and tags, the paper studies communication in MARL where messages are both language-grounded and human-interpretable.

## Key contributions we can verify from repository state

1. The work sits at the intersection of **communication** and **MARL**.
2. It explicitly emphasizes **human-interpretable communication**, not only latent learned protocols.
3. It therefore bridges classic emergent-communication research and newer LLM-centered agent communication work.

## Evidence from source

Verified title from `projects/multi-agent-survey/literature/neurips-2024-2025.md`:
> "Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication"

Repository metadata from the same artifact:
- Tags: `Communication, Theory/MARL`
- Retrieved via query: `multi-agent`

## Why it matters for the survey

- Interpretable communication is one of the strongest possible differentiators between useful multi-agent coordination and opaque coordination.
- It matters for debugging, trust, and comparison against single-agent-plus-tools systems, where intermediate reasoning is often inspectable.
- The paper likely marks a trend from purely emergent symbols toward communication channels that humans can audit.

## Method lens

This paper is best read as a communication-design paper with an interpretability objective:
- ground messages in language,
- preserve usefulness for coordination,
- expose communication in a form humans can inspect.

## Limits / caveats

1. The repository currently verifies title, DOI, and tags, but not the abstract or detailed experimental setup.
2. We therefore avoid claims about exact benchmarks or measured gains.
3. A future pass should verify whether the human-interpretable channel improves coordination, interpretability, or both.

## Relevance to open questions

- **Agent-to-agent communication 的最新范式是什么？** This paper points to language-grounded, interpretable messaging as a major paradigm.
- **什么时候值得用多智能体？** More plausibly when communication can be externally inspected and corrected rather than remaining latent and brittle.

## One-sentence takeaway

This paper is load-bearing because it frames agent communication as something that should coordinate effectively while remaining intelligible to humans.