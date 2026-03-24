# Session Log — arXiv Multi-Agent Subdirection Synthesis

- Timestamp: 2026-03-23T16:40:00Z
- Project: `projects/multi-agent-survey`
- Task: investigate the open question "最近三个月 arXiv 上的 multi-agent 论文主要集中在哪些子方向？"
- Classification: ROUTINE
- Status: completed

## Summary

Used the existing in-repo arXiv harvest artifact to answer the project’s open question without new external retrieval. The current 2026-01-01 to 2026-03-23 snapshot indicates that recent arXiv multi-agent papers are concentrated primarily in architecture/orchestration, secondarily in evaluation-heavy agent systems, with MARL-backed coordination remaining a strong but blended stream.

## Findings

1. The reproducible in-repo arXiv harvest contains 396 unique MAS-relevant records in the 2026-01-01 to 2026-03-23 window.
   - Provenance: `projects/multi-agent-survey/scripts/harvest_arxiv_recent.py`; recorded in `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md` and `projects/multi-agent-survey/logs/2026-03-23T163400Z-arxiv-harvest.md`.

2. The selected 32-paper subset is dominated by architecture and evaluation tags.
   - Provenance: `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md` harvest summary.
   - Counts: `Architecture = 28`, `Evaluation = 21`, `Theory/MARL = 15`, `Coordination = 14`, `Communication = 8`, `Application = 8`, `Theory = 4`.

3. The strongest near-term subdirection is system architecture/orchestration rather than isolated communication-only work.
   - Provenance: the tag counts above plus representative papers in `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`, including `MiTa`, `Dual Latent Memory for Visual Multi-agent System`, `DIG to Heal`, `Helix`, and `GoAgent`.

4. Evaluation-heavy work is a major concentration area, often attached to agent frameworks or domain deployments.
   - Provenance: the same artifact; examples include `DIG to Heal`, `TSC`, `WorldAgents`, `An Agentic Approach to Generating XAI-Narratives`, and `An Agentic Multi-Agent Architecture for Cybersecurity Risk Management`.

5. MARL remains a major stream, but the recent snapshot suggests it is increasingly intertwined with LLM-agent collaboration and practical system design.
   - Provenance: `Theory/MARL = 15` and `Coordination = 14` in the selected subset; examples include `Learning Decentralized LLM Collaboration with Multi-Agent Actor Critic`, `Self-Compression of Chain-of-Thought via Multi-Agent Reinforcement Learning`, and multiple cooperative-control / driving / wireless-network papers.

6. The harvested pool is increasingly March-heavy, suggesting rapid acceleration in the number of recent submissions.
   - Provenance: `projects/multi-agent-survey/logs/2026-03-23T163400Z-arxiv-harvest.md`.
   - Counts: `2026-01 = 55`, `2026-02 = 89`, `2026-03 = 252`.
   - Inline arithmetic: `55 + 89 + 252 = 396`.

## Answer

基于仓库内已生成的 arXiv 快照，最近三个月（2026-01-01 至 2026-03-23）arXiv 上的 multi-agent 论文主要集中在三类子方向：

1. **Architecture / Orchestration**：最强主线。重点是分层协作、记忆增强、角色分工、通信拓扑设计与 agent workflow 组织。
2. **Evaluation-heavy Agent Systems**：第二主线。很多论文不仅提框架，还把重点放在 benchmark、稳健性、可解释性或特定领域评测上。
3. **MARL-backed Coordination**：仍然很强，但更多与 LLM-agent 协作、推理压缩、分布式决策等结合，呈现“MARL + agent systems”融合趋势。

相对而言，**Communication** 作为独立子方向存在，但在当前样本中更多是 architecture/coordination 的组成部分，而不是单独占主导的论文簇。

## Actions taken

1. Updated `projects/multi-agent-survey/README.md` with a dated log entry answering the open question.
2. Narrowed the README open-question list so it now asks which representative load-bearing papers within the identified dominant subdirections should be prioritized next.

## Verification

Read and cross-checked:
- `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`
- `projects/multi-agent-survey/logs/2026-03-23T163400Z-arxiv-harvest.md`
- `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md`

## Next step

Prioritize literature notes for representative papers in the two currently dominant arXiv subdirections: (a) architecture/topology/orchestration and (b) evaluation-heavy agent systems.
