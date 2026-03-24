# MoE — Tasks

## Phase 1: 定义范围与资料入口

- [x] 在 Project 下新建 MoE 工作空间 [zero-resource]
  Completed: 2026-03-24T03:42:29Z
  Evidence: `projects/moe/README.md`, `projects/moe/TASKS.md`, `projects/moe/budget.yaml`, `projects/moe/logs/2026-03-24T034229Z-workspace-initialization.md`, plus the project subdirectories `analysis/`, `literature/`, `plans/`, and `logs/` together establish the baseline MoE workspace.

- [x] 梳理并初始化 MoE 任务目标与执行计划 [zero-resource]
  Completed: 2026-03-24T03:44:26Z
  Evidence: `projects/moe/plans/2026-03-24-initial-execution-plan.md` defines research scope, phase plan, deliverables, and non-goals; `projects/moe/analysis/2026-03-24-problem-framing.md` records prioritized research questions.

- [x] 建立 MoE 首版来源地图 [zero-resource]
  Completed: 2026-03-24T03:56:30Z
  Why: 后续任何文献或实现分析都需要统一的来源入口，避免 session 间重复从零开始找材料。
  Evidence: `projects/moe/literature/2026-03-24-moe-source-map.md` now contains 10 source-map entries spanning 6 papers, 3 open-source implementations, and 1 engineering reference; count derived by direct row count in the file's `## Source map` table during this session.

## Phase 2: 机制分析

- [x] 分析 MoE routing 与负载均衡机制 [zero-resource]
  Completed: 2026-03-24T04:05:04Z
  Why: routing 是 MoE 与 dense Transformer 的关键差异，也是训练稳定性与专家利用率的核心问题。
  Evidence: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` compares four source-backed mechanism families — top-k token-choice routing, top-1 token-choice routing, balanced assignment routing, and stability-oriented routing refinements — and cites Shazeer et al. 2017, GShard 2020, Switch Transformers 2021, BASE Layers 2021, ST-MoE 2022, Mixtral 2024, and Hugging Face SwitchTransformers docs; `projects/moe/logs/2026-03-24T040504Z-routing-analysis.md` records the original completion and verification.

- [x] 分析 MoE 系统瓶颈与效率权衡 [zero-resource]
  Completed: 2026-03-24T04:08:52Z
  Why: MoE 的价值不仅取决于参数规模，也取决于 dispatch、通信和并行策略是否真正带来吞吐收益。
  Evidence: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md` covers four source-backed system-layer bottlenecks / optimization points — token dispatch and gather overhead, cross-device communication from expert parallelism, expert placement / utilization efficiency, and capacity-factor / overflow tuning — citing `GShard`, `DeepSpeed MoE`, `Megatron-LM`, `Switch Transformers`, and Hugging Face SwitchTransformers docs; `projects/moe/logs/2026-03-24T040852Z-systems-analysis.md` records the original completion and verification.

## Phase 3: 结构化沉淀

- [x] 撰写 MoE 结构化综述初稿 [zero-resource]
  Why: 项目的最终价值在于把分散来源整理成可复用的结构化知识，而不是只留下零散笔记。
  Completed: 2026-03-24T04:08:21Z
  Evidence: `projects/moe/plans/moe-survey-draft.md` links back to `projects/moe/literature/2026-03-24-moe-source-map.md`, `projects/moe/analysis/2026-03-24-problem-framing.md`, `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`, and `projects/moe/analysis/2026-03-24-workspace-audit.md`, and contains `Architecture`, `Routing`, and `Systems` sections.

## Phase 4: 未决问题收敛

- [ ] 比较 `DeepSpeed MoE`、`Megatron-LM` 与 `fairseq` 作为首轮配置旋钮抽取基线的适配性 [zero-resource] [skill: analyze]
  Why: README 仍将“哪个实现入口最适合作为首轮配置旋钮抽取基线”列为开放问题；如果没有显式比较，后续实现配置地图任务会缺少统一起点。
  Done when: 新增一份对比笔记，至少基于 `projects/moe/literature/2026-03-24-moe-source-map.md` 中登记的三个实现入口，给出比较维度、推荐基线及理由，并把结论写回 `projects/moe/README.md`。
  Priority: high
  Next step: 先从 `projects/moe/literature/2026-03-24-moe-source-map.md` 中已有的 intended-use 描述抽取比较维度（训练框架集成、并行策略可见性、配置字段可发现性），再形成首版 baseline recommendation。

- [x] 验证训练与推理场景是否应分开建模，并确定是否需要统一指标桥接二者 [zero-resource] [skill: analyze]
  Completed: 2026-03-24T13:43:44Z
  Why: README 仍将训练/推理主导瓶颈是否显著不同列为开放问题；如果不先验证这一点，后续 systems 比较容易混淆吞吐、延迟、容量和通信成本的评价口径。
  Evidence: `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md` separates current evidence from still-open hypotheses, concludes that training and inference should be modeled as separate comparison axes, and proposes four bridge-metric candidates — dispatch complexity, expert utilization/load skew, overflow or unused-capacity rate, and communication-to-compute exposure; `projects/moe/README.md` logs the same conclusion and removes this item from `## Open questions`; `projects/moe/logs/2026-03-24T134344Z-fleet-花阳-06-1774359774-423cd9-training-vs-inference-modeling.md` records the session verification.
