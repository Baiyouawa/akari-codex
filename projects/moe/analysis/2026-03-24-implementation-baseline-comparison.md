# MoE 实现入口对比：首轮配置旋钮抽取基线

- Timestamp: 2026-03-24T13:43:47Z
- Project: `projects/moe`
- Task: 比较 `DeepSpeed MoE`、`Megatron-LM` 与 `fairseq` 作为首轮配置旋钮抽取基线的适配性
- Scope: 仅基于仓库内现有来源地图与既有分析 artifacts，判断三类实现入口在“首轮配置旋钮抽取”场景下的适配性，并给出推荐基线。

## Sources used

1. `projects/moe/literature/2026-03-24-moe-source-map.md`
2. `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`
3. `projects/moe/plans/moe-survey-draft.md`

Provenance note: 本文所有比较结论都锚定在上述三个仓库内 artifacts 的明确文字描述，尤其是 source map 中对三个实现入口的 intended-use 描述；本文不引入新的外部检索或未登记代码细节。

## Decision target

这里的目标不是判断哪个实现“最强”或“最先进”，而是判断：**哪个入口最适合作为首轮配置旋钮抽取的基线**。因此比较标准应优先服务于首轮知识产出，而不是覆盖所有系统复杂度。

结合当前项目状态，首轮基线应优先满足三个要求：

1. **训练框架集成导向明确**：能直接看到训练期常见 MoE knobs，而不是先穿过大量并行框架组合细节。
2. **并行与 dispatch 旋钮可见**：至少能支持后续抽取 capacity factor、expert parallelism、token dispatch 这类当前项目已命名的系统变量。
3. **配置字段可发现性高**：适合在下一轮 session 里快速整理成一张实现配置地图。

Provenance:
- 这三个维度直接来自 `projects/moe/TASKS.md` 当前该任务的 `Next step`：`训练框架集成、并行策略可见性、配置字段可发现性`。
- 其中 capacity factor / expert parallelism / token dispatch 已被 `projects/moe/literature/2026-03-24-moe-source-map.md` 的 `DeepSpeed MoE` 条目标为后续要抽取的工程旋钮。

## Repo-internal role summary

### DeepSpeed MoE

Source-map role: “作为训练框架集成实现入口，用于抽取 capacity factor、auxiliary loss、expert parallelism、token dispatch 等工程配置旋钮；也可作为后续代码级 provenance 的上游入口。”

Implication for this task: 这是当前 source map 中**唯一一个已经把‘配置旋钮抽取’直接写进 intended use** 的实现入口。

### Megatron-LM

Source-map role: “作为大规模训练实现参考，适合后续查看 MoE 与 tensor / pipeline / expert parallelism 的组合方式，支撑 systems 分析。”

Implication for this task: 它更像**并行组合与系统扩展**的强入口，而不是首轮最直接的配置旋钮枚举入口。

### fairseq

Source-map role: “适合作为较早期、研究导向的 Transformer MoE 实现参考，用于比对训练脚本、router loss 设置和实验配置表达方式。”

Implication for this task: 它适合补充**研究脚本表达与 router loss 配置**视角，但 source map 并没有把它定位为并行 / dispatch 旋钮的主入口。

Provenance: 三段角色描述均直接摘自 `projects/moe/literature/2026-03-24-moe-source-map.md`。

## Comparison dimensions

| 实现入口 | 训练框架集成 | 并行策略可见性 | 配置字段可发现性 | 对首轮旋钮抽取的直接性 | Repo-internal assessment |
|---|---|---|---|---|---|
| `DeepSpeed MoE` | 强：source map 直接把它定义为“训练框架集成实现入口” | 强：明确点名 `expert parallelism` 与 `token dispatch` | 强：明确点名 `capacity factor`、`auxiliary loss` 等待抽字段 | 最强：intended use 已经是“抽取工程配置旋钮” | **首选基线** |
| `Megatron-LM` | 中：更偏大规模训练体系而非单纯 MoE 训练入口 | 很强：重点是 `tensor / pipeline / expert parallelism` 组合 | 中：当前 repo 对它的描述更偏系统组合，不是字段枚举 | 中：适合作为第二阶段补充系统复杂度 | **第二优先** |
| `fairseq` | 中：研究训练脚本入口清晰，但框架集成目标未被描述为主轴 | 弱到中：当前 repo 只明确其用于脚本与 router loss 对比 | 中到强：实验配置表达方式较易读 | 中：适合补充 loss / script 层配置，但覆盖面较窄 | **第三优先** |

Provenance:
- `DeepSpeed MoE` / `Megatron-LM` / `fairseq` 的三列判断均来自 `projects/moe/literature/2026-03-24-moe-source-map.md` 的 intended-use 描述。
- “并行策略可见性”维度同时受 `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md` 支撑：该文把 `DeepSpeed MoE` 与 `Megatron-LM` 都列为 expert parallelism / dispatch / parallel composition 的主要系统来源。

## Why `DeepSpeed MoE` is the best first baseline

### 1. 它与任务目标的语义对齐度最高

当前任务要解决的是“首轮配置旋钮抽取基线”，而 `DeepSpeed MoE` 在 source map 中已经被写成：用于抽取 `capacity factor`、`auxiliary loss`、`expert parallelism`、`token dispatch` 等工程配置旋钮。

这意味着在现有 repo 记忆里，`DeepSpeed MoE` 不是事后推断出来适合，而是**最初建 source map 时就已被明确建模为该任务的直接上游入口**。

Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md` 的 `DeepSpeed MoE` 条目。

### 2. 它同时覆盖训练侧与系统侧的首轮关键旋钮

当前项目已经把 MoE 系统层关注点收敛到至少四类：token dispatch、cross-device communication、expert parallelism、capacity-factor / overflow tuning。虽然首轮配置抽取不需要一次解决全部系统问题，但如果基线入口能够同时暴露 dispatch、capacity、expert parallelism，它就更适合作为第一张配置地图的骨架。

`DeepSpeed MoE` 正好在 source map 里同时命中 `capacity factor`、`expert parallelism`、`token dispatch` 三项；相比之下：
- `Megatron-LM` 更突出 parallelism composition；
- `fairseq` 更突出脚本 / router loss 表达。

Provenance:
- `projects/moe/literature/2026-03-24-moe-source-map.md`
- `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`, sections on token dispatch, expert parallelism, and capacity-factor tuning.

### 3. 它更适合先做“共有字段表”，再做“复杂系统补充表”

从当前 survey draft 与 systems note 看，`Megatron-LM` 的价值主要在于解释 MoE 如何与 tensor / pipeline / expert parallelism 组合，这对后续系统比较非常重要；但作为首轮 baseline，它可能过早把工作重心拉到并行组合复杂度上。相反，`DeepSpeed MoE` 更像一个先把共有旋钮表搭出来的入口。

推荐顺序因此应为：
1. 先用 `DeepSpeed MoE` 抽出首版共有旋钮骨架；
2. 再用 `Megatron-LM` 补充复杂并行组合与系统部署差异；
3. 最后用 `fairseq` 补充研究脚本、router loss 和实验配置表达差异。

Provenance:
- `projects/moe/plans/moe-survey-draft.md`, systems section `3.3 Systems source roles in the current source map`.
- `projects/moe/literature/2026-03-24-moe-source-map.md`.

## Why not choose `Megatron-LM` first

`Megatron-LM` 不是不重要，而是**更像第二阶段深化入口**：

1. source map 对它的核心定位是查看 MoE 与 `tensor / pipeline / expert parallelism` 的组合方式；
2. 这更适合回答“系统如何组合扩展”，而不是先回答“有哪些最基础且共通的配置旋钮”；
3. 如果一开始就以它为基线，首轮笔记可能被并行拓扑复杂度主导，削弱配置地图的可移植性。

Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/plans/moe-survey-draft.md`, section `3.3 Systems source roles in the current source map`.

## Why not choose `fairseq` first

`fairseq` 的优势在于研究导向与训练脚本可读性，但当前 repo 对它的定位仍然更偏：
- `router loss` 设置对比；
- 实验配置表达方式对比；
- 较早期研究实现参考。

因此它更适合在首轮基线之后，作为**对照组**去检查：
1. 哪些 knobs 是研究实现中直接暴露的；
2. 哪些 knobs 在训练脚本里表达得更清楚；
3. 哪些配置属于研究原型常见但不一定是系统扩展主轴。

Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md` 的 `fairseq` 条目。

## Recommendation

### Recommended first baseline: `DeepSpeed MoE`

推荐理由，按当前项目目标排序：

1. **任务对齐最好**：source map 已明确把它定义为配置旋钮抽取入口。
2. **字段覆盖最平衡**：同时触达 `capacity factor`、`auxiliary loss`、`expert parallelism`、`token dispatch`。
3. **适合首轮沉淀共享词表**：更容易产出后续可复用的配置地图骨架。
4. **不会过早把工作卷入并行组合复杂度**：可先建基础表，再用 `Megatron-LM` 扩展系统层差异。

### Suggested follow-on order

1. `DeepSpeed MoE` — 建首版共有配置旋钮表。
2. `Megatron-LM` — 补并行组合、系统扩展与拓扑相关旋钮。
3. `fairseq` — 补 router loss、训练脚本与研究配置表达差异。

## Implications for next session

基于这次比较，下一轮“实现配置地图”任务可直接以 `DeepSpeed MoE` 为基线，优先抽取以下四类字段：

1. `capacity factor`
2. `auxiliary loss`
3. `expert parallelism`
4. `token dispatch`

这四类字段不是本文新发明的分类，而是当前 source map 已经对 `DeepSpeed MoE` 明确点名的 intended-use 字段集合。

Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md` 的 `DeepSpeed MoE` 条目。

## Open follow-up question

1. 在以 `DeepSpeed MoE` 建完首版共有配置表之后，`Megatron-LM` 的并行组合差异应追加为独立补充表，还是直接并入统一配置矩阵的“parallel composition”列？
   - Provenance: 本文比较结果显示 `Megatron-LM` 的主要增量价值集中在 parallelism composition，而非首轮基础字段枚举。
