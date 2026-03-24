# Load-bearing papers for Phase 2 — Coordination & Communication

Timestamp: 2026-03-24T13:19:06Z

Purpose: make the repository-level `load-bearing` set explicit for the Phase 2 task `精读 Phase 1 中标记为 load-bearing 的论文（Coordination & Communication 类）`.

Selection rule used in this session:
- Start from Phase 1 artifacts already present in `projects/multi-agent-survey/literature/`.
- Prefer papers explicitly tagged `Coordination` and/or `Communication` in those artifacts.
- Prioritize papers that appear load-bearing for the survey's central question: what extra capability, efficiency, or robustness does multi-agent coordination/communication provide beyond strong single-agent baselines?
- Keep coverage across conference years and paper styles: benchmarked coordination methods, communication-mechanism papers, and 2026 topology/control directions.
- Use only repository-local evidence in this selection step; no external retrieval was required.

## Selected load-bearing papers

1. **Multi-Agent Coordination via Multi-Level Communication**
   - Bucket: Coordination, Communication
   - Why load-bearing: the title directly places communication structure as the mechanism for coordination, making it a clean anchor for the survey's core distinction between multi-agent and single-agent systems.
   - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md`, entry 3.

2. **Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication**
   - Bucket: Communication
   - Why load-bearing: interpretable communication is a key bridge between emergent MARL communication and LLM-era agent systems where messages are inspectable and potentially auditable.
   - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md`, entry 2.

3. **LLM-Assisted Semantically Diverse Teammate Generation for Efficient Multi-agent Coordination**
   - Bucket: Coordination
   - Why load-bearing: explicitly treats teammate diversity as a lever for coordination efficiency, which is central to ad-hoc and zero-shot collaboration.
   - Provenance: `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 24.

4. **HYGMA: Hypergraph Coordination Networks with Dynamic Grouping for Multi-Agent Reinforcement Learning**
   - Bucket: Coordination, Communication
   - Why load-bearing: upgrades pairwise coordination to hypergraph/group-level interaction structure, which is a strong candidate mechanism for scaling beyond simple all-to-all communication.
   - Provenance: `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 25.

5. **Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems**
   - Bucket: Communication
   - Why load-bearing: directly addresses the token-cost side of agent communication, which is crucial for the survey's practical boundary question of when multi-agent systems are actually worth using.
   - Provenance: `projects/multi-agent-survey/literature/iclr-2025-2026.md`, 2025 entry 13.

6. **Benefits and Limitations of Communication in Multi-Agent Reasoning**
   - Bucket: Communication, Theory
   - Why load-bearing: the title directly promises evidence on when communication helps versus hurts, making it highly relevant to the project's open boundary question.
   - Provenance: `projects/multi-agent-survey/literature/iclr-2025-2026.md`, 2026 entry 65.

7. **GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems**
   - Bucket: Communication, Architecture, Coordination
   - Why load-bearing: the existing repo already identified this as a potentially new 2026 subdirection where the communication graph itself becomes a learned/generated object.
   - Provenance: `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`, 2026-03 entry 12; prior horizon-scan note in `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md`.

## Coverage note

This session marks 7 papers as the repository's current load-bearing set for the Coordination & Communication bucket.
- Inline arithmetic: 2 NeurIPS 2024 papers + 2 ICML 2025 papers + 2 ICLR 2025-2026 papers + 1 recent arXiv paper = 7 total.

## Scope boundary

This file only defines the load-bearing set for the Coordination & Communication task. It does not claim to settle the load-bearing set for Architecture or to replace the existing Evaluation & Application load-bearing artifact.