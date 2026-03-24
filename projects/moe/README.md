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

### 2026-03-24T13:26:17Z

Reconciled project state for the routing task after verifying that the required analysis artifact had already been completed in an earlier session.

Findings:
1. `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` already satisfies the assignment acceptance bar because it compares four mechanism families — top-k token-choice routing, top-1 token-choice routing, balanced assignment routing, and stability-oriented routing refinements — exceeding the minimum requirement of three.
   - Provenance: direct read of `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` in this session.
2. The routing note is source-backed within current repo scope because its `## Sources used` section cites Shazeer et al. 2017, GShard 2020, Switch Transformers 2021, BASE Layers 2021, ST-MoE 2022, Mixtral 2024, and Hugging Face SwitchTransformers documentation, all already registered in `projects/moe/literature/2026-03-24-moe-source-map.md`.
   - Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`; `projects/moe/literature/2026-03-24-moe-source-map.md`.
3. Before this reconciliation, `projects/moe/TASKS.md` still listed the routing task as open despite the prior completion log `projects/moe/logs/2026-03-24T040504Z-routing-analysis.md` and the existing analysis artifact.
   - Provenance: direct comparison among `projects/moe/TASKS.md`, `projects/moe/logs/2026-03-24T040504Z-routing-analysis.md`, and `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`.
4. After reconciliation, project memory now reflects that both baseline Phase 2 analysis tasks are complete, so future sessions can move to finer-grained configuration extraction instead of repeating first-pass analysis work.
   - Provenance: updated `projects/moe/TASKS.md` in this session.

### 2026-03-24T13:41:05Z

Ran a self-audit for README/TASKS convention compliance and found one real stale-state issue in `projects/moe/TASKS.md`.

Findings:
1. `projects/moe/README.md` already follows the active project convention used elsewhere in `projects/`: it includes `Priority`, `Status`, `Mission`, `Done when`, `## Context`, `## Log`, and `## Open questions`.
   - Provenance: direct comparison against `projects/akari/README.md`, `projects/multi-agent-survey/README.md`, and `examples/my-research-project/README.md` during this session.
2. `projects/moe/TASKS.md` formatting for completed items is consistent with repository conventions (`Completed`, `Why`, `Evidence` fields), but it had no open task corresponding to the two unresolved items still listed under `## Open questions` in this README.
   - Provenance: direct read of `projects/moe/TASKS.md` and `projects/moe/README.md` during this session.
3. This created a real stale-state contradiction against the project’s own done condition, which requires that current unfinished items in `projects/moe/TASKS.md` have executable next steps.
   - Provenance: `Done when` line in this README; absence of matching open items in pre-fix `projects/moe/TASKS.md`; the two unresolved questions still present under `## Open questions`.
4. The fix was to add two explicit Phase 4 open tasks to `projects/moe/TASKS.md`, one for baseline implementation-entry comparison and one for training-vs-inference modeling validation, each with `Why`, `Done when`, `Priority`, and `Next step` fields grounded in existing project artifacts.
   - Provenance: updated `projects/moe/TASKS.md` in this session.

### 2026-03-24T13:43:44Z

Validated that training and inference should be modeled separately for this project, while still preserving shared bridge fields across both views.

Findings:
1. Current repo evidence is stronger for training-side systems modeling than for inference-side serving modeling because the registered implementation entries (`DeepSpeed MoE`, `Megatron-LM`, `fairseq`) are described mainly in terms of training configuration, distributed parallelism, and experiment scripts, whereas the explicit inference-facing source in the current map is primarily Hugging Face `SwitchTransformers` documentation.
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md`.
2. The current evidence base supports keeping training and inference as separate comparison axes, but does not support treating them as fully disconnected systems, because both still share MoE structure-induced costs: dispatch complexity, communication exposure, expert utilization/load skew, and capacity / overflow behavior.
   - Provenance: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`; `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md`.
3. The safest project-level evaluation frame is therefore `separate top-level metrics + shared bridge fields`, rather than either a single mixed score or two completely unrelated scorecards.
   - Provenance: `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md`, section `Decision for current project state`.
4. The current bridge-metric candidates are dispatch complexity, expert utilization/load skew, overflow or unused-capacity rate, and communication-to-compute exposure; these are candidates rather than settled standards within the present source base.
   - Provenance: `projects/moe/analysis/2026-03-24-training-vs-inference-modeling.md`, section `Bridge metric candidates`.

### 2026-03-24T13:43:47Z

Compared `DeepSpeed MoE`, `Megatron-LM`, and `fairseq` as first-pass implementation-baseline candidates and resolved the baseline recommendation in favor of `DeepSpeed MoE`.

Findings:
1. `DeepSpeed MoE` is the strongest first baseline for configuration-knob extraction because the source map already defines it as the training-framework implementation entry for extracting `capacity factor`, `auxiliary loss`, `expert parallelism`, and `token dispatch`.
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`, `DeepSpeed MoE` row; `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`.
2. `Megatron-LM` is better treated as a second-pass source because the current repo positions it primarily for studying MoE composition with tensor / pipeline / expert parallelism, which is more useful for systems expansion than for first-pass shared knob enumeration.
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`, `Megatron-LM` row; `projects/moe/plans/moe-survey-draft.md`, section `3.3 Systems source roles in the current source map`; `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`.
3. `fairseq` remains useful as a research-oriented comparison source for training scripts, `router loss` settings, and experiment configuration expression, but the current repo does not position it as the main entry for dispatch or expert-parallel knob extraction.
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`, `Fairseq examples / MoE` row; `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`.
4. The recommended extraction order is now explicit: start from `DeepSpeed MoE` for the shared configuration skeleton, then use `Megatron-LM` to add parallel-composition differences, and finally use `fairseq` to compare router-loss and script-level expression choices.
   - Provenance: `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`.

## Open questions

1. 在以 `DeepSpeed MoE` 建完首版共有配置表之后，`Megatron-LM` 的并行组合差异应追加为独立补充表，还是直接并入统一配置矩阵的 `parallel composition` 列？