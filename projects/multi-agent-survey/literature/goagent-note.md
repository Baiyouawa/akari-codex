# Literature Note — GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems

- Timestamp: 2026-03-24T13:19:06Z
- Category: Communication, Architecture, Coordination
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md`
- Source provenance:
  - Listing metadata and abstract snippet from `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`, 2026-03 entry 12.
  - Prior repository note: `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md`.

## Citation

Hongjiang Chen, Xin Zheng, Yixin Liu, Pengfei Jiao, Shiyuan Li, Huan Liu, Zhidong Zhao, Ziqi Xu, Ibrahim Khalil, Shirui Pan. **GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems**. arXiv preprint `http://arxiv.org/abs/2603.19677v1`, published 2026-03-20T06:21:32Z.

## What this paper studies

From the verified title and repository-preserved abstract snippet, the paper studies how to generate communication topologies for LLM-based multi-agent systems rather than assuming a fixed topology.

## Key contributions we can verify from repository state

1. The paper is about **communication topology generation** for LLM-based MAS.
2. The arXiv harvest classifies it as `Architecture, Coordination, Communication, Evaluation`.
3. The stored abstract snippet explicitly says MAS effectiveness depends heavily on the underlying communication topology.
4. The earlier repo horizon-scan note already identified this paper as potentially representing a new 2026 subdirection.

## Evidence from source

Verified title from `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`:
> "GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems"

Repository abstract snippet from the same artifact:
> "Large language model (LLM)-based multi-agent systems (MAS) have demonstrated exceptional capabilities in solving complex tasks, yet their effectiveness depends heavily on the underlying communication topology that coordinates agent..."

Additional repo interpretation from `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md`:
- the communication graph itself becomes a learned/generated object rather than a fixed design choice.

## Why it matters for the survey

- It sharpens a major 2026 trend candidate: communication topology as an optimization target.
- This is highly relevant to the survey's question about whether multi-agent value comes from role diversity, from tools, or from structured information routing.
- If topology generation matters, then multi-agent systems may justify themselves precisely when communication sparsity or hierarchy must be adapted to the task.

## Method lens

This paper is best read as topology-as-method:
- do not fix all-to-all or manager-worker communication in advance,
- generate a group-level communication structure,
- treat topology choice as part of solving the task.

## Limits / caveats

1. This note is still based on title, metadata, and repository-preserved abstract snippet rather than a full-paper extraction.
2. Exact optimization procedure, baselines, and metrics remain unverified in repo state.
3. A future pass should verify whether topology is generated offline, online, or per-instance.

## Relevance to open questions

- **Agent-to-agent communication 的最新范式是什么？** GoAgent supports topology generation as a distinct paradigm.
- **什么时候值得用多智能体？** Potentially when the task benefits from adaptive routing structures that a single-agent pipeline cannot express as naturally.

## One-sentence takeaway

GoAgent is load-bearing because it reframes communication topology from a hand-designed implementation detail into a learnable design variable for multi-agent systems.