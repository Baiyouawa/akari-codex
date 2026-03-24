# MoE 初始执行计划

- Date: 2026-03-24T03:44:26Z
- Project: `projects/moe`
- Scope: zero-resource initialization plan

## Goal

将当前仅完成工作空间搭建的 MoE 项目推进到“可连续执行”的状态：后续 session 无需重新定义范围，即可按任务列表持续补充文献、分析与结论。

## Current baseline

1. `projects/moe/` 已存在 `README.md`、`TASKS.md`、`budget.yaml` 以及 `analysis/`、`literature/`、`plans/`、`logs/` 目录。
   - Provenance: `find projects/moe -maxdepth 2 -type d | sort` 与 `find projects/moe -maxdepth 2 -type f | sort` 于本 session 输出。
2. 已有一条工作空间初始化日志，但项目任务仍缺少明确的研究阶段和可交付物。
   - Provenance: `projects/moe/logs/2026-03-24T034229Z-workspace-initialization.md`；`projects/moe/TASKS.md`。
3. 仓库内没有其他 `MoE` / `moe` 文本命中，因此当前知识主要集中在新建项目目录本身。
   - Provenance: `search_text("MoE|moe", path=".", max_results=100)` returned no matches before本次更新。

## Research scope

本项目首阶段聚焦 **LLM / Transformer 语境下的 Mixture-of-Experts**，优先关注能用仓库内零资源方式推进的研究整理工作，而非外部训练运行。

### Priority themes

1. **Architecture**
   - 稀疏激活、专家层放置位置、shared router vs per-layer router。
2. **Routing & load balancing**
   - top-k routing、capacity factor、auxiliary loss、dropless routing。
3. **Systems & efficiency**
   - expert parallelism、通信瓶颈、推理吞吐与训练稳定性。
4. **Open-source implementations / benchmarks**
   - 主流开源栈、可验证 benchmark、常见失败模式。

## Phase plan

### Phase 1 — 项目定标与问题清单

Deliverables:
- `projects/moe/analysis/2026-03-24-problem-framing.md`
- README 中补充明确 open questions

Done when:
- 至少形成 5 个可执行研究问题，并按优先级排序。

### Phase 2 — 文献与实现入口建档

Deliverables:
- `projects/moe/literature/2026-03-24-moe-source-map.md`

Done when:
- 至少记录 8 个可验证入口，覆盖论文 / 博客 / 开源实现中的至少 2 类。

### Phase 3 — 机制分析

Deliverables:
- `projects/moe/analysis/` 下形成至少 2 份专题分析：
  - routing / load balancing
  - systems / efficiency

Done when:
- 每份分析都包含明确问题、来源、结论、未决问题。

### Phase 4 — 结构化综述

Deliverables:
- `projects/moe/plans/moe-survey-draft.md`

Done when:
- 形成一份可扩展的综述草稿，能回链到前述 literature / analysis artifacts。

## Immediate next tasks

1. 产出 MoE 问题定义文档，明确首批 5 个研究问题。
2. 建立第一版 source map，收集可验证的 MoE 入口来源。
3. 将 `TASKS.md` 从占位描述改写为阶段化任务列表。

## Non-goals for this phase

- 不执行外部 API 调用。
- 不启动训练、评测或长时间算力任务。
- 不在尚无来源的情况下写结论性技术判断。
