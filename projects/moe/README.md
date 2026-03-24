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

## Open questions

(to be filled)
