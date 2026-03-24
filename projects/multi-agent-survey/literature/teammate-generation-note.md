# Literature Note — LLM-Assisted Semantically Diverse Teammate Generation for Efficient Multi-agent Coordination

- Timestamp: 2026-03-24T13:19:06Z
- Category: Coordination
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 24.
  - Repository-internal tags in that artifact: `Coordination, LLM, Collaboration`.

## Citation

Lihe Li, Lei Yuan, Pengsen Liu, Tao Jiang, Yang Yu. **LLM-Assisted Semantically Diverse Teammate Generation for Efficient Multi-agent Coordination**. ICML 2025. PMLR: `https://proceedings.mlr.press/v267/li25dq.html`. DBLP: `https://dblp.org/rec/conf/icml/Li0LJ025`.

## What this paper studies

From the verified title and tags, the paper studies efficient multi-agent coordination by generating semantically diverse teammates with LLM assistance.

## Key contributions we can verify from repository state

1. The paper is explicitly about **efficient multi-agent coordination**.
2. Its central mechanism is **semantically diverse teammate generation**.
3. It uses **LLM assistance**, making it relevant to the current shift from pure MARL toward LLM-mediated agent design.

## Evidence from source

Verified title from `projects/multi-agent-survey/literature/icml-2024-2025.md`:
> "LLM-Assisted Semantically Diverse Teammate Generation for Efficient Multi-agent Coordination"

Repository metadata from the same artifact:
- Tags: `Coordination, LLM, Collaboration`
- Retrieved via: `coordination`

## Why it matters for the survey

- It suggests that coordination quality may depend not only on policy learning but on the composition of the team itself.
- Teammate diversity is especially relevant for ad-hoc coordination and zero-shot partner matching, both central survey themes.
- The use of LLMs for teammate generation shows a new interface between language models and coordination research: LLMs can shape agent populations, not just act as agents.

## Method lens

This paper is best read as a coordination-through-team-design paper:
- generate teammates,
- enforce semantic diversity,
- seek more efficient coordination outcomes.

## Limits / caveats

1. The current repository verifies the title, venue links, and tags, but not the abstract or numeric results.
2. The exact meaning of "efficient" is not yet verified: sample efficiency, coordination success, or compute/token efficiency.
3. A deeper read should verify whether diversity is measured behaviorally, semantically, or both.

## Relevance to open questions

- **什么时候值得用多智能体？** More likely when teammate diversity creates complementary behaviors a single agent cannot emulate cheaply.
- **Multi-Agent 与 Single-Agent + tools 的性能边界在哪里？** This paper suggests one potential multi-agent advantage is controlled diversity across collaborators.

## One-sentence takeaway

This paper is load-bearing because it makes teammate diversity an explicit design variable for improving multi-agent coordination efficiency.