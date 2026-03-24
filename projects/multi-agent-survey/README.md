# Multi-Agent Systems Survey

Priority: high
Status: active
Mission: 系统调研近两年（2024-2026）Multi-Agent 领域的研究进展，覆盖三大 AI 顶会（NeurIPS、ICML、ICLR）+ 最新 ICLR 2026 + 近三个月 arXiv 论文。
Done when: (1) 三大顶会 2024-2025 相关论文梳理完成并分类建档 (2) ICLR 2026 accepted papers 中 Multi-Agent 方向论文全面盘点 (3) 近三个月 arXiv 论文趋势分析完成 (4) 综述文档产出包含方法分类、关键发现、研究趋势、未来方向 (5) 每篇 load-bearing 论文有 literature note

## Context

Multi-Agent Systems (MAS) 是当前 AI 领域最活跃的研究方向之一。LLM-based Multi-Agent 框架（如 AutoGen、CrewAI、MetaGPT、ChatDev）在 2024-2025 年爆发式增长，同时学术界在 multi-agent communication、coordination、evaluation 等方面产出了大量高质量工作。

本项目旨在系统性地收集、分类、分析这些工作，产出一份结构化的文献综述。

## Scope

### 会议论文
- **NeurIPS 2024, 2025**: multi-agent, LLM agent collaboration, cooperative AI
- **ICML 2024, 2025**: multi-agent reinforcement learning, agent communication, agent systems
- **ICLR 2024, 2025, 2026**: multi-agent, agent framework, agent evaluation

### arXiv 预印本
- **时间窗口**: 2026-01-01 至 2026-03-23
- **关键词**: multi-agent, LLM agent, agent collaboration, agent framework, cooperative agents

### 分类维度
1. **Architecture**: 框架设计、agent 拓扑、通信协议
2. **Coordination**: 任务分配、协作策略、冲突解决
3. **Communication**: 消息传递、共享记忆、tool sharing
4. **Evaluation**: benchmark、metrics、human evaluation
5. **Application**: 代码生成、科学发现、游戏、机器人
6. **Theory**: 博弈论、社会选择、emergence

## Log

### 2026-03-23

项目创建。定义了调研范围、分类体系和产出目标。

- 2026-03-23T16:14:41Z — Harvested the first NeurIPS literature artifact into `projects/multi-agent-survey/literature/neurips-2024-2025.md` using Crossref venue-constrained retrieval logic mirrored from `projects/multi-agent-survey/scripts/harvest_neurips_crossref.py`. This session produced 138 NeurIPS 2024 candidates with title/author/link/tag metadata and 0 NeurIPS 2025 venue-matched records in the current Crossref snapshot, so `projects/multi-agent-survey/TASKS.md` was decomposed into a completed 2024 task and a blocked 2025 follow-up.
- 2026-03-23T16:29:00Z — Added `projects/multi-agent-survey/literature/icml-2024-2025.md` using DBLP venue-constrained retrieval (`stream:conf/icml:` with queries `multi-agent`, `coordination`, `cooperative`, and `agent collaboration`). The artifact records 24 ICML 2024-2025 papers with authors, PMLR links, DBLP links, lightweight tags, and per-paper retrieval-query provenance; the resulting mix suggests ICML 2024 is more MARL/theory-heavy while ICML 2025 adds more LLM-agent benchmark and systems work.
- 2026-03-23T16:34:00Z — Added `projects/multi-agent-survey/scripts/harvest_arxiv_recent.py` and generated `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md` from the arXiv Atom API. The reproducible harvest deduplicated 396 MAS-relevant records in the 2026-01-01 to 2026-03-23 window and selected 32 month-grouped papers (10 in January, 10 in February, 12 in March) with source queries, dedup rules, and classification counts recorded inline.
- 2026-03-23T16:35:00Z — Scanned recent arXiv results via the arXiv Atom API and added `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md` for **GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems** (`https://arxiv.org/abs/2603.19677v1`). This appears to surface a new subdirection not yet captured in the repo: communication-topology generation as an explicit multi-agent design variable.
- 2026-03-23T17:05:00Z — Investigated the open question “ICLR 2026 是否有关于 multi-agent evaluation benchmark 的新工作？” and found that the current repository cannot answer it yet. Provenance: recursive listing of `projects/multi-agent-survey/literature/` shows only `neurips-2024-2025.md`, `icml-2024-2025.md`, `arxiv-2026-01-to-2026-03.md`, and `2026-03-23-goagent-communication-topology.md`; `search_text` for `ICLR`, `OpenReview`, `benchmark`, and `evaluation` under `projects/multi-agent-survey/literature`, `projects/multi-agent-survey/logs`, and `projects/multi-agent-survey/README.md` returned no matches relevant to ICLR 2026. Current answer: no in-repo evidence confirms any ICLR 2026 multi-agent evaluation benchmark paper. Specific external research still needed: an authoritative ICLR 2026 accepted-paper source (official proceedings or OpenReview accepted submissions), followed by title/abstract screening for multi-agent evaluation/benchmark work and, if candidates exist, per-paper notes with benchmark scope, metrics, and whether the benchmark is for LLM-based MAS versus MARL.
- 2026-03-23T17:20:00Z — Self-audit fixed two real convention issues: `## Scope` now matches the mission/done-when requirement by listing `ICLR 2024, 2025, 2026`, and `projects/multi-agent-survey/TASKS.md` now tracks the corresponding ICLR coverage task as `2024-2026` rather than `2025-2026`. Provenance: inline comparison between the mission/done-when lines in this README and the Phase 1 ICLR task text in `projects/multi-agent-survey/TASKS.md` before the fix.

### 2026-03-24

- 2026-03-24T03:55:00Z — Added `projects/multi-agent-survey/scripts/harvest_iclr_2025_2026.py` and generated `projects/multi-agent-survey/literature/iclr-2025-2026.md` from the public ICLR 2025 and 2026 schedule pages. The resulting venue-constrained inventory contains 146 deduplicated Multi-Agent papers, including 54 from 2025 and 92 from 2026, with verified `Oral`/`Poster` labels, authors, and OpenReview links. Provenance: `python3 projects/multi-agent-survey/scripts/harvest_iclr_2025_2026.py` wrote the artifact and printed `Total deduped papers: 146`, `2025 papers: 54`, `2026 papers: 92`; see also `projects/multi-agent-survey/logs/2026-03-24T035500Z-iclr-2025-2026-harvest.md`.
- 2026-03-24T03:56:31Z — Re-checked the blocked Phase 2 Architecture literature-note task and confirmed the blocker still stands. Provenance: `projects/multi-agent-survey/TASKS.md` still marks the Architecture note task as `[blocked-by: Phase 1 检索完成]`, Phase 1 still has open tasks for NeurIPS 2025 and ICLR spotlight-label verification, `search_text("load-bearing", "projects/multi-agent-survey", max_results=200)` found no literature artifact that explicitly marks Architecture papers as `load-bearing`, and `search_text("Literature Note|literature note|## Citation|## Summary|## Method|## Key Findings", ".", max_results=200)` found no reusable standardized note template. Session log: `projects/multi-agent-survey/logs/2026-03-24T035631Z-architecture-load-bearing-blocked.md`.
- 2026-03-24T04:05:15Z — Verified that the remaining ICLR blocker is specifically spotlight-label provenance rather than conference coverage volume. Provenance: `projects/multi-agent-survey/literature/iclr-2025-2026.md` already covers 92 ICLR 2026 papers, exceeding the task minimum of 20, but the same artifact records `2025: populated spotlight cards detected = 0; placeholder cards detected = 1` and `2026: populated spotlight cards detected = 0; placeholder cards detected = 1` for the official `type=Spotlight` pages; `projects/multi-agent-survey/TASKS.md` now tracks spotlight verification as the remaining follow-up.

## Open questions

- Multi-Agent 与 Single-Agent + tools 的性能边界在哪里？什么时候值得用多智能体？
- ICLR 2026 是否有关于 multi-agent evaluation benchmark 的新工作？当前仓库内已有初步证据指向“有”，但仍需进一步筛选哪些 benchmark/evaluation 论文属于 load-bearing。
- 最近三个月 arXiv 上的 multi-agent 论文主要集中在哪些子方向？
- Agent-to-agent communication 的最新范式是什么？shared memory vs message passing vs tool use?
- 除 Crossref 之外，NeurIPS 2025 应优先采用哪个可验证来源（OpenReview / 官方 proceedings / DBLP）以补齐论文池？
- Communication-topology generation 是否会成为 2026 年 LLM multi-agent 的独立方法类，还是只是现有 architecture/coordination 类的一种实现？
- ICLR 官方还有哪个可验证页面或导出能稳定提供 2025-2026 Spotlight 标签，以便把 `iclr-2025-2026.md` 从 `Oral/Poster verified` 提升到 `Oral/Spotlight/Poster verified`？
