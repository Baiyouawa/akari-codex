# MoE

Priority: high
Status: active
Mission: 在新建的 Project 下创建 MoE 工作空间，并持续推进 MoE 相关任务。
Done when: (1) MoE 项目工作空间与基础文档齐备 (2) 任务目标、执行计划与后续研究产物持续沉淀到仓库中 (3) `projects/moe/TASKS.md` 中当前未完成事项具备可执行的下一步定义。

## Context

MoE 项目当前处于早期搭建阶段。现有仓库状态已经包含 `projects/moe/README.md`、`projects/moe/TASKS.md`、`projects/moe/budget.yaml` 以及基础目录结构，因此后续工作重点应从“是否已创建工作空间”转向“如何明确目标并持续推进 MoE 相关研究任务”。

## Log

### 2026-03-24

Project created.

### 2026-03-24T03:44:17Z

Ran a conventions/quality audit for the MoE project and fixed real inconsistencies in place.

Findings:
1. `projects/moe/README.md` was missing `Done when` and `## Context`, which made it inconsistent with the active project README structure used elsewhere in `projects/`.
   - Provenance: direct comparison against `projects/akari/README.md`, `projects/multi-agent-survey/README.md`, and `examples/my-research-project/README.md` during this session.
2. `projects/moe/TASKS.md` contained a stale contradiction: it still listed “在 Project 下新建 MoE 工作空间” as open even though this README already recorded “Project created.” on `2026-03-24`.
   - Provenance: direct read of `projects/moe/README.md` and `projects/moe/TASKS.md` during this session.
3. `projects/moe/TASKS.md` formatting was inconsistent with repository task conventions because entries lacked the usual supporting fields and included a duplicate follow-on task phrased as both “继续推进 MoE 任务” and “继续执行当前Moe任务”.
   - Provenance: direct comparison against `projects/akari/TASKS.md` and `projects/multi-agent-survey/TASKS.md` during this session.
4. The stale open task and duplicate entry were corrected, and the remaining MoE tasks were normalized to the repository task format.
   - Provenance: `projects/moe/TASKS.md` updated in this session.

### 2026-03-24T03:56:30Z

Built the first-pass MoE source map and updated project next steps to depend on named sources instead of generic placeholders.

Findings:
1. `projects/moe/literature/2026-03-24-moe-source-map.md` now contains 10 source entries spanning 3 source classes: 6 papers, 3 open-source implementations, and 1 engineering reference.
   - Provenance: direct row count from the `## Source map` table in `projects/moe/literature/2026-03-24-moe-source-map.md` during this session.
2. The paper coverage now includes foundational scaling (`Sparsely-Gated MoE`, `GShard`), routing simplification (`Switch Transformers`), balancing alternatives (`BASE Layers`), stability (`ST-MoE`), and a recent open-model reference (`Mixtral of Experts`).
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`.
3. The implementation coverage now includes framework- and systems-oriented entry points via `DeepSpeed MoE`, `Megatron-LM`, and `fairseq`, which are suitable for extracting capacity factor, token dispatch, and expert parallelism configuration knobs in later sessions.
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`.
4. `projects/moe/TASKS.md` was updated so the open routing and systems tasks each point to concrete next sources rather than abstract future work.
   - Provenance: `projects/moe/TASKS.md` updated in this session.

## Open questions

1. 在当前来源地图中，哪三篇论文最适合优先抽取为 routing / load balancing 对比表？
2. `DeepSpeed MoE`、`Megatron-LM` 与 `fairseq` 三个实现入口中，哪个最适合作为首轮配置旋钮抽取的基线？
3. 训练与推理场景应先分开建模与比较；但仍需外部文献/实现证据来验证两者各自主导瓶颈是否显著不同，以及是否需要统一指标桥接二者。
