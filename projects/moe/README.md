# MoE

Priority: high
Status: active
Mission: 在新建的 Project 下创建 MoE 工作空间，并持续推进 MoE 相关任务。
Done when: MoE 项目具备可持续推进所需的基础工作空间（README、TASKS、budget、logs/、analysis/、literature/、plans/）且已形成可执行的阶段计划、来源地图入口与后续分析任务。

## Context

本项目用于承载 Mixture-of-Experts（MoE）相关研究与执行工作。当前阶段的目标是先建立符合仓库约定的项目工作空间，确保后续 MoE 任务可以在统一的 README / TASKS / logs / artifact 结构下持续推进。

## Log

### 2026-03-24

Project created.

### 2026-03-24T03:42:29Z

Completed the initial MoE workspace scaffold verification and normalization.

Findings:
1. `projects/moe/` currently contains `README.md`, `TASKS.md`, `budget.yaml`, `analysis/`, `literature/`, and `plans/`.
   - Provenance: `list_files("projects/moe", recursive=false)` during this session.
2. The standard per-project log directory used by active projects was not present under `projects/moe/` before this update, while comparable active projects already use an in-project `logs/` directory.
   - Provenance: `list_files("projects/moe", recursive=false)` showed no `logs/`; `list_files("projects/akari", recursive=false)` showed `projects/akari/logs`.
3. This session added `projects/moe/logs/2026-03-24T034229Z-workspace-initialization.md` and updated project metadata so the MoE workspace now records its baseline state in-repo.
   - Provenance: files written in this session.

### 2026-03-24T03:44:26Z

Advanced the MoE project from workspace bootstrap to executable research planning.

Findings:
1. The workspace now contains project-local planning, analysis, literature, and log artifacts under `projects/moe/`.
   - Provenance: `find projects/moe -maxdepth 2 -type d | sort` and `find projects/moe -maxdepth 2 -type f | sort` during this session.
2. The previous highest-value gap was execution specificity rather than missing structure: the task list still contained a generic continuation task and the README only had high-level direction-setting questions.
   - Provenance: direct read of `projects/moe/TASKS.md` and `projects/moe/README.md` before overwrite in this session.
3. This session added an initial execution plan, a prioritized problem-framing note, and a source-map skeleton so future sessions can advance MoE research without redoing basic project framing.
   - Provenance: `projects/moe/plans/2026-03-24-initial-execution-plan.md`, `projects/moe/analysis/2026-03-24-problem-framing.md`, `projects/moe/literature/2026-03-24-moe-source-map.md`, and `projects/moe/logs/2026-03-24T034426Z-initial-planning.md`.

## Open questions

- 哪些 foundational MoE 论文最适合作为本项目首轮 source map 的核心入口？
- 当前开源 MoE 实现中，哪些项目最适合用来抽取 routing、capacity factor、expert parallelism 等关键配置旋钮？
- 在训练与推理两个场景下，MoE 的系统瓶颈是否需要分开建模与比较？
