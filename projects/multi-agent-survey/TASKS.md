# Multi-Agent Survey — Tasks

## Phase 1: 顶会论文检索与建档

- [x] 检索 NeurIPS 2024 Multi-Agent 相关论文 [skill: orient] [zero-resource]
  Why: 先建立可验证的 NeurIPS 候选池，为后续精读建立候选集
  Completed: 2026-03-23T16:14:41Z
  Evidence: `projects/multi-agent-survey/literature/neurips-2024-2025.md` contains 138 Crossref-harvested NeurIPS 2024 candidates with title, authors, link, and classification tags, generated via inline Python using the same retrieval logic as `projects/multi-agent-survey/scripts/harvest_neurips_crossref.py`.

- [ ] 补全并验证 NeurIPS 2025 Multi-Agent 相关论文 [skill: orient] [zero-resource] [blocked-by: Crossref 当前快照未返回 NeurIPS 2025 proceedings records，需要更换来源或等待索引更新]
  Why: 原始任务要求覆盖 NeurIPS 2024-2025，但本次仅验证到 2024，2025 需要单独补齐
  Done when: `literature/` 下补充 NeurIPS 2025 论文列表，包含标题、作者、链接、分类标签，至少覆盖 15 篇，并注明数据源

- [x] 检索 ICML 2024-2025 Multi-Agent 相关论文 [skill: orient] [zero-resource]
  Why: ICML 侧重方法论和理论，与 NeurIPS 互补
  Completed: 2026-03-23T16:29:00Z
  Evidence: `projects/multi-agent-survey/literature/icml-2024-2025.md` lists 24 DBLP-verified ICML 2024-2025 papers with authors, PMLR links, DBLP record URLs, tags, and retrieval-query provenance.

- [ ] 全面盘点 ICLR 2024-2026 Multi-Agent 方向论文 [skill: orient] [zero-resource] [blocked-by: 仓库内无 ICLR accepted-paper 清单或缓存导出，且当前环境访问 OpenReview 返回 HTTP 403，无法验证 2024-2026 论文与 oral/spotlight/poster 标签]
  Why: 项目目标要求覆盖三大顶会 2024-2025，并额外补充最新 ICLR 2026
  Done when: literature/ 下有 ICLR 2024-2026 论文列表，标注 oral/spotlight/poster，且其中 ICLR 2026 至少覆盖 20 篇
  Evidence of current blocker: `projects/multi-agent-survey/logs/2026-03-24T040515Z-iclr-2024-2026-harvest-blocked.md`
  Supporting progress: `projects/multi-agent-survey/literature/liveresearchbench-note.md` now captures one high-value ICLR 2026 benchmark candidate from the existing 2025-2026 harvest, but does not remove the label-verification blocker.

- [x] 检索近三个月 arXiv Multi-Agent 预印本（2026-01 至 2026-03）[skill: orient] [zero-resource]
  Why: arXiv 捕捉最新趋势，顶会论文有滞后性
  Completed: 2026-03-23T16:34:00Z
  Evidence: `projects/multi-agent-survey/scripts/harvest_arxiv_recent.py` queries the arXiv Atom API and writes `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`, which groups 32 selected papers by month (2026-01/02/03), documents query sources and deduplication rules, and reports classification counts from a deduplicated pool of 396 in-window MAS-relevant records.

## Phase 2: 精读与 Literature Notes

- [ ] 精读 Phase 1 中标记为 load-bearing 的论文（Architecture 类）[skill: analyze] [zero-resource] [blocked-by: Phase 1 尚未完成，且仓库内仍无 artifact 明确标记哪些 Architecture 论文属于 load-bearing，也无标准 literature-note 模板]
  Why: 框架设计是 multi-agent 最核心的子方向
  Done when: 每篇 load-bearing 论文有标准格式的 literature note 文件
  Evidence of current blocker: `projects/multi-agent-survey/logs/2026-03-24T035631Z-architecture-load-bearing-blocked.md`

- [x] 精读 Phase 1 中标记为 load-bearing 的论文（Coordination & Communication 类）[skill: analyze] [zero-resource]
  Why: 协作与通信是区分 multi-agent 与 single-agent 的关键
  Completed: 2026-03-24T13:19:06Z
  Done when: 每篇 load-bearing 论文有 literature note
  Evidence: `projects/multi-agent-survey/literature/load-bearing-coordination-communication.md` explicitly marks 7 Coordination/Communication papers as load-bearing, and literature notes were added for each: `multi-level-communication-note.md`, `language-grounded-communication-note.md`, `teammate-generation-note.md`, `hygma-note.md`, `cut-the-crap-note.md`, `benefits-limitations-communication-note.md`, and `goagent-note.md`.

- [x] 精读 Phase 1 中标记为 load-bearing 的论文（Evaluation & Application 类）[skill: analyze] [zero-resource]
  Why: 评估方法和应用场景决定了实际价值
  Completed: 2026-03-24T04:20:00Z
  Evidence: `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md` explicitly marks 8 Evaluation/Application papers as load-bearing, and literature notes were added for each: `windows-agent-arena-note.md`, `omnibench-note.md`, `ad-hoc-human-ai-coordination-challenge-note.md`, `agent-smith-note.md`, `zsc-eval-note.md`, `mdagents-note.md`, `ai-agents-hep-note.md`, and `dig-to-heal-note.md`.

## Phase 3: 分析与综述

- [ ] 分析 Multi-Agent 研究趋势（2024 → 2026 变化）[skill: analyze] [zero-resource]
  Why: 识别方向性变化，如从 MARL 到 LLM-based MAS 的转变
  Done when: analysis/ 下有趋势分析文档，包含时间线、关键转折点、热度变化
  [blocked-by: Phase 2 精读完成]

- [x] 产出分类体系与方法对比表 [skill: record] [zero-resource]
  Why: 结构化整理是综述的核心产出
  Completed: 2026-03-24T21:18:07+08:00
  Evidence: `projects/multi-agent-survey/analysis/2026-03-24-method-taxonomy-and-comparison.md` provides a 6-category method taxonomy and comparison tables covering representative papers, strengths, weaknesses, and fit-for-use scenarios, synthesized from in-repo literature artifacts and notes.

- [x] 撰写综述初稿 [skill: record] [zero-resource]
  Why: 最终交付物
  Completed: 2026-03-24T21:18:53+08:00
  Evidence: `projects/multi-agent-survey/plans/survey-draft.md` exists and contains 引言、方法分类、关键发现、趋势分析、未来方向 sections; `wc -m projects/multi-agent-survey/plans/survey-draft.md` returned `17206`, exceeding the `≥3000 字` requirement.

- [ ] 识别研究空白并提出未来方向 [skill: analyze] [zero-resource]
  Why: 综述的最高价值在于指出"什么还没做"
  Done when: analysis/ 下有 research-gaps.md，至少 5 个具体的研究空白及可能的研究方向
  [blocked-by: 综述初稿完成]