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

- [x] 比较 `DeepSpeed MoE`、`Megatron-LM` 与 `fairseq` 作为首轮配置旋钮抽取基线的适配性 [zero-resource] [skill: analyze]
  Why: README 仍将“哪个实现入口最适合作为首轮配置旋钮抽取基线”列为开放问题；如果没有显式比较，后续实现配置地图任务会缺少统一起点。
  Done when: 新增一份对比笔记，至少基于 `projects/moe/literature/2026-03-24-moe-source-map.md` 中登记的三个实现入口，给出比较维度、推荐基线及理由，并把结论写回 `projects/moe/README.md`。
  Priority: high
  Completed: 2026-03-24T13:43:47Z
  Evidence: `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md` compares `DeepSpeed MoE`, `Megatron-LM`, and `fairseq` along the dimensions already named in this task’s prior next step — training-framework integration, parallel-strategy visibility, and configuration-field discoverability — and recommends `DeepSpeed MoE` as the first baseline because the source map already positions it for extracting `capacity factor`, `auxiliary loss`, `expert parallelism`, and `token dispatch`; `projects/moe/README.md` records the conclusion and follow-on ordering.

- [x] 验证训练与推理场景是否应分开建模，并确定是否需要统一指标桥接二者 [zero-resource] [skill: analyze]
  Completed: 2026-03-24T13:43:44Z
  Why: README 仍将训练/推理主导瓶颈是否显著不同列为开放问题；如果不先验证这一点，后续 systems 比较容易混淆吞吐、延迟、容量和通信成本的评价口径。
  Evidence: `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md` separates current evidence from still-open hypotheses, concludes that training and inference should be modeled as separate comparison axes, and proposes four bridge-metric candidates — dispatch complexity, expert utilization/load skew, overflow or unused-capacity rate, and communication-to-compute exposure; `projects/moe/README.md` logs the same conclusion and removes this item from `## Open questions`; `projects/moe/logs/2026-03-24T134344Z-fleet-花阳-06-1774359774-423cd9-training-vs-inference-modeling.md` records the session verification.

## Phase 5: 后续实现抽取

- [x] 以 `DeepSpeed MoE` 为首轮基线抽取共有配置旋钮，并决定 `Megatron-LM` 的并行组合差异应如何并入配置矩阵 [zero-resource] [skill: analyze]
  Why: 当前 README 的唯一剩余开放问题已经从“选谁做基线”收敛为“在选定 `DeepSpeed MoE` 之后，如何表示 `Megatron-LM` 的 parallel composition 增量”；如果不把这个下一步显式写入任务列表，README 与 TASKS 会再次失配。
  Done when: 新增一份配置抽取笔记，至少以 `DeepSpeed MoE` 为基线列出首版共有字段骨架（含 `capacity factor`、`auxiliary loss`、`expert parallelism`、`token dispatch` 四类），并明确 `Megatron-LM` 的并行组合差异应作为独立补充表还是统一矩阵列来表示；同时把结论同步到 `projects/moe/README.md`。
  Priority: high
  Completed: 2026-03-24T13:53:17Z
  Evidence: `projects/moe/analysis/2026-03-24-deepspeed-baseline-config-skeleton.md` defines a first-pass shared matrix skeleton with at least seven columns — `implementation`, `capacity factor`, `auxiliary loss`, `expert parallelism`, `token dispatch`, `parallel composition`, and `evidence source` — and concludes that `Megatron-LM` parallel-composition differences should be represented inside the unified matrix as a `parallel composition` column rather than as a separate supplementary table; `projects/moe/README.md` records the same conclusion and updates the remaining open question accordingly.

- [x] 规定 `parallel composition` 列的行内编码方式，以支持 `Megatron-LM` 与后续实现的稳定横向比较 [zero-resource] [skill: analyze]
  Why: 当前项目已经决定把 `Megatron-LM` 的并行组合差异并入统一矩阵的 `parallel composition` 列，但该列若没有明确编码方式，后续 session 仍可能用自由文本重新引入不可比的表述漂移。
  Done when: 新增一份短笔记，比较至少两种 `parallel composition` 列编码方案（如多标签短语、分层子字段、受限词表），明确推荐方案及理由，并把结论写回 `projects/moe/README.md` 与本任务文件。
  Priority: high
  Completed: 2026-03-24T14:02:11Z
  Evidence: `projects/moe/analysis/2026-03-24-parallel-composition-encoding.md` compares three candidate schemes — multi-label phrases, layered subfields, and a constrained vocabulary with canonical order — and recommends keeping one matrix column while encoding values with the constrained vocabulary `{dp, tp, pp, ep}` in fixed order `dp+tp+pp+ep`; it also standardizes the placeholders `unspecified-baseline` and `unknown` for non-free-text missingness states. `projects/moe/README.md` records the same conclusion and closes the remaining open question.
