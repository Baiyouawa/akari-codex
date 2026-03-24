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

### 2026-03-24T04:05:00Z

Investigated the open question “在训练与推理两个场景下，MoE 的系统瓶颈是否需要分开建模与比较？” using only existing in-repo MoE artifacts.

Findings:
1. Current in-repo MoE knowledge already separates the question operationally: `projects/moe/analysis/2026-03-24-problem-framing.md` lists “MoE 的系统瓶颈主要出现在哪些环节” as a P0 systems question and separately lists “训练阶段与推理阶段的 MoE 关注点有何不同？” as a P1 comparison question.
   - Provenance: `projects/moe/analysis/2026-03-24-problem-framing.md`.
2. The initial execution plan also distinguishes training stability from inference efficiency in the project scope: it names “训练稳定性” and “推理效率” as separate research objects and postpones any unified benchmark design until after Phase 1-2 scoping.
   - Provenance: `projects/moe/plans/2026-03-24-moe-execution-plan.md`.
3. The current repository does not yet contain any source-backed MoE systems analysis artifact or populated source map entries that would let us verify a detailed bottleneck taxonomy for training vs inference.
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md` is still an unfilled skeleton, `projects/moe/TASKS.md` still lists “分析 MoE 系统瓶颈与效率权衡” as open, and `search_text("训练|推理|bottleneck|routing|capacity factor|expert parallelism|system bottleneck|MoE", path="projects/moe", max_results=200)` returned no source-bearing matches beyond project setup files during this session.
4. Useful working answer from current repo state: yes, training and inference should be treated as separate comparison axes in this project’s planning, because the repo already frames them as different objectives; however, this is still a planning hypothesis rather than a literature-backed conclusion.
   - Provenance: synthesis of Items 1-3 above.
5. More research is specifically needed on externally sourced evidence for which bottlenecks dominate in each scenario — e.g. whether dispatch/all-to-all communication, load imbalance, memory pressure, latency tails, or expert parallelism limits are reported differently for training and for serving.
   - Provenance: gap between the open systems-analysis task in `projects/moe/TASKS.md` and the empty source buckets in `projects/moe/literature/2026-03-24-moe-source-map.md`.

## Open questions

1. 哪些 foundational MoE 论文最适合作为本项目首轮 source map 的核心入口？
2. 当前开源 MoE 实现中，哪些项目最适合用来抽取 routing、capacity factor、expert parallelism 等关键配置旋钮？
3. 训练与推理场景应先分开建模与比较；但仍需外部文献/实现证据来验证两者各自主导瓶颈是否显著不同，以及是否需要统一指标桥接二者。
