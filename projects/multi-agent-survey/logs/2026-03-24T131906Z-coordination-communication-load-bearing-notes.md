# Session Log — Coordination & Communication load-bearing literature notes

- Timestamp: 2026-03-24T13:19:06Z
- Project: `projects/multi-agent-survey`
- Task: `projects/multi-agent-survey/TASKS.md` — 精读 Phase 1 中标记为 load-bearing 的论文（Coordination & Communication 类）
- Classification: ROUTINE
- Status: completed

## Summary

Completed the assigned Coordination & Communication reading task by first making the repository's load-bearing paper set explicit, then writing one literature note for each selected paper. The resulting note set covers communication hierarchy, interpretable language grounding, teammate diversity for coordination, hypergraph grouping, communication-efficiency pipelines, theory-oriented limits of communication, and topology generation for LLM-based multi-agent systems.

## Findings

1. The repository previously had no explicit load-bearing selection artifact for the Coordination & Communication bucket, which is why earlier sessions remained blocked.
   - Provenance: prior blocked logs `projects/multi-agent-survey/logs/2026-03-24T034315Z-coordination-communication-load-bearing-blocked.md` and `projects/multi-agent-survey/logs/2026-03-24T040926Z-coordination-communication-load-bearing-blocked.md` both recorded the absence of a Coordination/Communication `load-bearing` artifact.

2. Existing Phase 1 artifacts already contained enough provenance to define a coordination/communication load-bearing set without external retrieval.
   - Provenance: selected papers were drawn from `projects/multi-agent-survey/literature/neurips-2024-2025.md`, `projects/multi-agent-survey/literature/icml-2024-2025.md`, `projects/multi-agent-survey/literature/iclr-2025-2026.md`, and `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`, then recorded in `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md`.

3. The current Coordination & Communication load-bearing set contains 7 papers.
   - Provenance: `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md` lists 7 papers.
   - Inline arithmetic: 2 NeurIPS 2024 papers + 2 ICML 2025 papers + 2 ICLR 2025-2026 papers + 1 recent arXiv paper = 7.

4. The note set shows a method progression from communication as a MARL mechanism to communication as a systems-design and topology-optimization problem for LLM agents.
   - Provenance: notes added in this session cover `multi-level-communication-note.md`, `language-grounded-communication-note.md`, `hygma-note.md`, `cut-the-crap-note.md`, `benefits-limitations-communication-note.md`, and `goagent-note.md`.

5. Cost-aware communication and topology design are already explicit in the in-repo 2025-2026 paper pool, suggesting that communication is no longer treated only as a capability issue but also as a runtime-efficiency and routing problem.
   - Provenance: `Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems` appears in `projects/multi-agent-survey/literature/iclr-2025-2026.md`, 2025 entry 13; `GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems` appears in `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`, 2026-03 entry 12.

6. One of the strongest in-repo candidates for the project's open boundary question is `Benefits and Limitations of Communication in Multi-Agent Reasoning` because its title directly targets when communication helps versus hurts.
   - Provenance: `projects/multi-agent-survey/literature/iclr-2025-2026.md`, 2026 entry 65; note added as `projects/multi-agent-survey/literature/benefits-limitations-communication-note.md`.

## Actions taken

1. Wrote `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md` to explicitly mark the Coordination & Communication load-bearing set.
2. Added 7 literature notes:
   - `projects/multi-agent-survey/literature/multi-level-communication-note.md`
   - `projects/multi-agent-survey/literature/language-grounded-communication-note.md`
   - `projects/multi-agent-survey/literature/teammate-generation-note.md`
   - `projects/multi-agent-survey/literature/hygma-note.md`
   - `projects/multi-agent-survey/literature/cut-the-crap-note.md`
   - `projects/multi-agent-survey/literature/benefits-limitations-communication-note.md`
   - `projects/multi-agent-survey/literature/goagent-note.md`
3. Updated `projects/multi-agent-survey/TASKS.md` to mark the Coordination & Communication Phase 2 task complete.
4. Added a project README log entry for this completed task.

## Verification

Verified repository outputs by direct file creation and cross-check against the task done-when condition:
- `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md` exists and enumerates the selected paper set.
- Each selected paper now has a corresponding literature note file.
- `projects/multi-agent-survey/TASKS.md` now marks the Coordination & Communication task `[x]` with evidence paths.

## Next step

Use these notes in the Phase 3 trend analysis, especially for the open questions on communication paradigms, multi-agent cost/benefit boundaries, and whether topology generation should be treated as its own 2026 method class.