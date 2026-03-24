# Literature Note — HYGMA: Hypergraph Coordination Networks with Dynamic Grouping for Multi-Agent Reinforcement Learning

- Timestamp: 2026-03-24T13:19:06Z
- Category: Coordination, Communication
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 25.
  - Repository-internal tags in that artifact: `Coordination, Communication, MARL`.

## Citation

Chiqiang Liu, Dazi Li. **HYGMA: Hypergraph Coordination Networks with Dynamic Grouping for Multi-Agent Reinforcement Learning**. ICML 2025. PMLR: `https://proceedings.mlr.press/v267/liu25af.html`. DBLP: `https://dblp.org/rec/conf/icml/LiuL25`.

## What this paper studies

From the verified title and tags, the paper studies MARL coordination using hypergraph coordination networks and dynamic grouping.

## Key contributions we can verify from repository state

1. The work is explicitly about **coordination** in **MARL**.
2. It also carries a **communication** tag, indicating that interaction structure is part of the method.
3. The distinctive mechanism is a **hypergraph** formulation with **dynamic grouping**, implying higher-order rather than merely pairwise interaction modeling.

## Evidence from source

Verified title from `projects/multi-agent-survey/literature/icml-2024-2025.md`:
> "HYGMA: Hypergraph Coordination Networks with Dynamic Grouping for Multi-Agent Reinforcement Learning"

Repository metadata from the same artifact:
- Tags: `Coordination, Communication, MARL`
- Retrieved via: `coordination`

## Why it matters for the survey

- Hypergraph coordination is a strong candidate answer to how multi-agent systems scale beyond pairwise relations.
- Dynamic grouping suggests that useful communication may occur in subsets or coalitions rather than globally across all agents.
- This makes HYGMA relevant both to classical MARL and to LLM-agent systems where grouping/topology selection is becoming important.

## Method lens

The paper appears to represent coordination as higher-order structure:
- identify or form groups,
- model group interactions via a hypergraph,
- use that structure to improve coordination in MARL.

## Limits / caveats

1. Repository evidence currently verifies title, venue, and tags, but not the exact mathematical formulation or benchmark results.
2. We therefore do not claim specific gains or complexity reductions.
3. A later deep read should verify whether dynamic grouping is learned online, predefined, or induced from state.

## Relevance to open questions

- **Agent-to-agent communication 的最新范式是什么？** HYGMA supports the move from pairwise messaging to group-structured communication.
- **什么时候值得用多智能体？** Especially when tasks require higher-order coordination patterns that a single monolithic policy may not represent cleanly.

## One-sentence takeaway

HYGMA is load-bearing because it treats scalable coordination as a higher-order grouping problem rather than a collection of pairwise interactions.