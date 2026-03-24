# MoE — Tasks

## Phase 1: 定义范围与资料入口

- [x] 在 Project 下新建 MoE 工作空间 [zero-resource]
  Completed: 2026-03-24T03:42:29Z
  Evidence: `projects/moe/README.md`, `projects/moe/TASKS.md`, `projects/moe/budget.yaml`, `projects/moe/logs/2026-03-24T034229Z-workspace-initialization.md`, plus the project subdirectories `analysis/`, `literature/`, `plans/`, and `logs/` together establish the baseline MoE workspace.

- [x] 梳理并初始化 MoE 任务目标与执行计划 [zero-resource]
  Completed: 2026-03-24T03:44:26Z
  Evidence: `projects/moe/plans/2026-03-24-initial-execution-plan.md` defines research scope, phase plan, deliverables, and non-goals; `projects/moe/analysis/2026-03-24-problem-framing.md` records prioritized research questions.

- [ ] 建立 MoE 首版来源地图 [zero-resource]
  Why: 后续任何文献或实现分析都需要统一的来源入口，避免 session 间重复从零开始找材料。
  Done when: `projects/moe/literature/2026-03-24-moe-source-map.md` 至少补充 8 个带来源与用途说明的条目，覆盖论文 / 开源实现 / 工程参考中的至少 2 类。
  Progress: 2026-03-24 repo-internal investigation confirmed the paper bucket is still empty; current project files only establish that the first-round core set must cover Transformer-era MoE architecture, routing/load-balancing, and systems/scaling questions, so external literature research is required before naming actual foundational papers.

## Phase 2: 机制分析

- [ ] 分析 MoE routing 与负载均衡机制 [zero-resource]
  Why: routing 是 MoE 与 dense Transformer 的关键差异，也是训练稳定性与专家利用率的核心问题。
  Done when: `projects/moe/analysis/` 下存在 routing 分析文档，明确比较至少 3 类机制或设计权衡，并给出来源。

- [ ] 分析 MoE 系统瓶颈与效率权衡 [zero-resource]
  Why: MoE 的价值不仅取决于参数规模，也取决于 dispatch、通信和并行策略是否真正带来吞吐收益。
  Done when: `projects/moe/analysis/` 下存在 systems 分析文档，覆盖至少 3 个系统层瓶颈或优化点，并给出来源。
  Progress: 2026-03-24 repo-internal synthesis says training and inference should be treated as separate comparison axes for now, but the claim is not yet literature-backed because `projects/moe/literature/2026-03-24-moe-source-map.md` still lacks populated external sources and no systems analysis artifact exists yet.

## Phase 3: 结构化沉淀

- [ ] 撰写 MoE 结构化综述初稿 [zero-resource]
  Why: 项目的最终价值在于把分散来源整理成可复用的结构化知识，而不是只留下零散笔记。
  Done when: `projects/moe/plans/moe-survey-draft.md` 存在，能够回链到 literature / analysis artifacts，并覆盖 architecture、routing、systems 三个主题。
