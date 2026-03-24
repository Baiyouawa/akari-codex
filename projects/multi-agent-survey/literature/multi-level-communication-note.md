# Literature Note — Multi-Agent Coordination via Multi-Level Communication

- Timestamp: 2026-03-24T13:19:06Z
- Category: Coordination, Communication
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/neurips-2024-2025.md`, entry 3.
  - Repository-internal tags in that artifact: `Coordination, Communication`.

## Citation

Ziluo Ding, Zhirui Fang, Zeyuan Liu, Zongqing Lu, Kefan Su, Liwen Zhu. **Multi-Agent Coordination via Multi-Level Communication**. NeurIPS 2024. DOI: `https://doi.org/10.52202/079017-3763`.

## What this paper studies

From the verified title and repository tags, this paper studies coordination in multi-agent systems by structuring communication across multiple levels rather than treating communication as a flat one-shot exchange.

## Key contributions we can verify from repository state

1. The paper is explicitly about **coordination**.
2. Its proposed mechanism is **multi-level communication**.
3. It is a direct fit for the survey's core question of how communication design affects coordination quality.

## Evidence from source

Verified title from `projects/multi-agent-survey/literature/neurips-2024-2025.md`:
> "Multi-Agent Coordination via Multi-Level Communication"

Repository metadata from the same artifact:
- Tags: `Coordination, Communication`
- Retrieved via query: `multi-agent`

## Why it matters for the survey

- It is a clean anchor paper for the claim that communication structure is itself a method class in multi-agent research.
- Multi-level communication suggests that effective coordination may depend on hierarchical or staged information flow rather than simple all-to-all chat.
- That is directly relevant to the boundary between multi-agent and single-agent systems: if structured communication is doing real work, multi-agent gains may come from information-routing topology rather than just more copies of the same model.

## Method lens

This paper is best read as a coordination-through-communication paper:
- coordination is the target behavior,
- communication is the intervention,
- multi-level structure is the distinguishing design choice.

## Limits / caveats

1. In this session, the repository verifies title, authors, DOI, and tags, but not the abstract or quantitative gains.
2. The note therefore establishes conceptual relevance rather than a validated numerical claim.
3. A future deeper read should verify what the levels are: temporal, hierarchical, role-based, or topology-based.

## Relevance to open questions

- **Agent-to-agent communication 的最新范式是什么？** This paper supports multi-level communication as a distinct paradigm beyond undifferentiated message passing.
- **什么时候值得用多智能体？** Potentially when the task benefits from structured information flow across levels rather than one model reasoning internally.

## One-sentence takeaway

This paper is load-bearing because it treats communication hierarchy itself as the mechanism that enables stronger multi-agent coordination.