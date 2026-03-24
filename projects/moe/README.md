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

### 2026-03-24T04:08:21Z

Assembled the first structured MoE survey draft from existing project artifacts.

Findings:
1. `projects/moe/plans/moe-survey-draft.md` now exists and organizes the current evidence base into `Architecture`, `Routing`, and `Systems` sections with explicit artifact back-links.
   - Provenance: `projects/moe/plans/moe-survey-draft.md` written in this session.
2. The draft’s routing section is the strongest-supported portion because it reuses the existing source-backed comparison in `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`.
   - Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`; `projects/moe/plans/moe-survey-draft.md`.
3. The draft includes systems as a structured outline rather than a closed conclusion because the project still lacked a dedicated systems analysis artifact under `projects/moe/analysis/` at the time of drafting.
   - Provenance: `projects/moe/TASKS.md` state at draft time; directory contents of `projects/moe/analysis/` observed in that session; `projects/moe/plans/moe-survey-draft.md`.
4. The survey draft now gives future sessions a reusable synthesis layer above the source map and analysis notes, reducing the need to reassemble architecture / routing / systems context from scratch.
   - Provenance: `projects/moe/plans/moe-survey-draft.md` and its `Artifact map`, section structure, and `Recommended next increments` section.

### 2026-03-24T13:17:45Z

Resolved the first open routing question using only repo-internal evidence and tightened the next extraction target accordingly.

Findings:
1. The strongest first trio for a routing / load-balancing comparison table is `Switch Transformers`, `BASE Layers`, and `ST-MoE`.
   - Provenance: `projects/moe/TASKS.md` already names these three as the routing task’s next-step extraction set; `projects/moe/literature/2026-03-24-moe-source-map.md` assigns them three complementary roles: routing simplification (`Switch Transformers`), balancing alternative (`BASE Layers`), and stability-focused refinement (`ST-MoE`).
2. This trio is preferable to alternatives in the current source map because it spans three distinct comparison axes with minimal overlap: single-expert simplified routing, balancing-by-assignment, and stability intervention layered onto sparse routing.
   - Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` sections `Token-choice routing simplified to top-1: Switch Transformer style`, `Balanced assignment routing: BASE Layers style`, and `Stability-oriented routing refinements: ST-MoE style`.
3. Repo-internal synthesis had already converged on the same answer before this session: the survey draft states that these three are the strongest immediate trio for a first routing table because they produce the cleanest contrast set for `experts-per-token / balancing method / stability intervention` style columns.
   - Provenance: `projects/moe/plans/moe-survey-draft.md`, section `2.3 Routing implications for this project`; `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`, `Implications for projects/moe`.
4. What still remains undone is the actual row-level extraction into a compact matrix; the answer here resolves source prioritization, not the full table build.
   - Provenance: `projects/moe/TASKS.md` keeps the routing task open and defines extraction as the next step.

### 2026-03-24T13:17:44Z

Reconciled project state for the systems task after verifying that the required artifact had already been completed in an earlier session.

Findings:
1. `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md` already satisfies the assignment acceptance bar because it covers four system-layer bottlenecks / optimization points — token dispatch and gather overhead, cross-device communication from expert parallelism, expert placement / utilization efficiency, and capacity-factor / overflow tuning — exceeding the minimum requirement of three.
   - Provenance: direct read of `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md` in the reconciliation session.
2. The systems note is source-backed within current repo scope because it cites `GShard`, `DeepSpeed MoE`, `Megatron-LM`, `Switch Transformers`, and Hugging Face SwitchTransformers docs, all of which are also registered in `projects/moe/literature/2026-03-24-moe-source-map.md`.
   - Provenance: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`; `projects/moe/literature/2026-03-24-moe-source-map.md`.
3. Before reconciliation, `projects/moe/TASKS.md` still listed the systems task as open despite the prior completion log `projects/moe/logs/2026-03-24T040852Z-systems-analysis.md` and the existing analysis artifact.
   - Provenance: direct comparison among `projects/moe/TASKS.md`, `projects/moe/logs/2026-03-24T040852Z-systems-analysis.md`, and `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`.
4. After reconciliation, project memory now reflects that the systems baseline artifact exists, so future sessions can move to configuration extraction and finer-grained evidence rather than redoing the first-pass note.
   - Provenance: updated `projects/moe/TASKS.md`; `projects/moe/logs/2026-03-24T131744Z-fleet-智乃-02-1774358212-4f942d-systems-task-closeout.md`.

## Open questions

1. `DeepSpeed MoE`、`Megatron-LM` 与 `fairseq` 三个实现入口中，哪个最适合作为首轮配置旋钮抽取的基线？
2. 训练与推理场景应先分开建模与比较；但仍需外部文献/实现证据来验证两者各自主导瓶颈是否显著不同，以及是否需要统一指标桥接二者。
