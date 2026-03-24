# MoE 配置抽取笔记：以 `DeepSpeed MoE` 为基线的共有字段骨架

- Timestamp: 2026-03-24T13:53:17Z
- Project: `projects/moe`
- Task: 以 `DeepSpeed MoE` 为首轮基线抽取共有配置旋钮，并决定 `Megatron-LM` 的并行组合差异应如何并入配置矩阵
- Scope: 仅基于仓库内已登记的 source map、systems 分析、survey draft 与 baseline comparison 结论，先定义首版共有字段骨架，并决定 `Megatron-LM` 的 parallel composition 增量应如何表示。

## Sources used

1. `projects/moe/literature/2026-03-24-moe-source-map.md`
2. `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`
3. `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`
4. `projects/moe/plans/moe-survey-draft.md`
5. `projects/moe/TASKS.md`

Provenance note: 本文不引入新的外部代码检索或实现细节；所有字段类别与表示决策都锚定在上述仓库内 artifacts 已明确写出的 intended-use、系统主题与后续任务定义。

## Decision target

当前已解决的问题是：`DeepSpeed MoE` 应作为首轮配置旋钮抽取基线。
本笔记要继续解决两个更具体的问题：

1. 首版“共有配置表”至少应有哪些字段骨架？
2. `Megatron-LM` 的 parallel composition 差异，应该作为独立补充表，还是作为统一矩阵中的一列？

## Why `DeepSpeed MoE` is the right skeleton source

当前 repo 对 `DeepSpeed MoE` 的定位最直接：source map 明确说它用于抽取 `capacity factor`、`auxiliary loss`、`expert parallelism`、`token dispatch` 等工程配置旋钮；前一份 baseline comparison 也已经据此将它定为首轮基线。

Provenance:
- `projects/moe/literature/2026-03-24-moe-source-map.md`, `DeepSpeed MoE` row.
- `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`, sections `Why DeepSpeed MoE is the best first baseline` and `Recommendation`.

## First-pass shared field skeleton

这里的目标不是提前发明所有实现的最终 schema，而是先产出一张能够容纳当前 repo 已明确命名变量的“共有字段骨架”。

### Skeleton principles

1. 首版字段必须直接覆盖当前 source map 已点名的 `DeepSpeed MoE` 抽取目标。
2. 字段应能和现有 systems 分析里的主要 bottleneck 对应起来，而不是只罗列名称。
3. 字段应允许后续把 `Megatron-LM` 的并行组合增量加进来，而不必重做表结构。

Provenance:
- `projects/moe/literature/2026-03-24-moe-source-map.md`
- `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`
- `projects/moe/TASKS.md`, Phase 5 task text.

### Proposed first-pass matrix columns

| 字段类 | 首版列名 | 为什么必须在骨架里 | Repo-internal provenance |
|---|---|---|---|
| Baseline identity | `implementation` | 需要区分 `DeepSpeed MoE`、`Megatron-LM`、后续 `fairseq` 等实现入口。 | `projects/moe/literature/2026-03-24-moe-source-map.md` implementation rows |
| Capacity control | `capacity factor` | 已被 source map 直接点名，也是 systems note 中 capacity / overflow tuning 的核心旋钮。 | `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md` |
| Router regularization | `auxiliary loss` | 已被 source map 直接点名，且与 routing/balancing 分析中的负载均衡机制相连。 | `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` as referenced by the baseline comparison |
| Distributed layout | `expert parallelism` | 已被 source map 直接点名，也是 systems note 的中心扩展轴。 | `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md` |
| Dispatch path | `token dispatch` | 已被 source map 直接点名，并直接对应 systems note 的 dispatch bottleneck。 | `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md` |
| Parallel-composition extension | `parallel composition` | 这是当前 README 剩余开放问题的目标字段，用于承接 `Megatron-LM` 相对 `DeepSpeed MoE` 的主要增量。 | `projects/moe/README.md`; `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/plans/moe-survey-draft.md` |
| Provenance | `evidence source` | 后续行级抽取必须可追溯到具体 artifact 或实现入口，避免无来源字段表。 | `AGENTS.md` provenance rule as already applied in project artifacts; operationalized here via in-repo artifact citation |

### Minimal row skeleton

首版共有配置表可先按下列骨架表达：

| implementation | capacity factor | auxiliary loss | expert parallelism | token dispatch | parallel composition | evidence source |
|---|---|---|---|---|---|---|
| `DeepSpeed MoE` | 待从实现/文档抽取 | 待从实现/文档抽取 | 待从实现/文档抽取 | 待从实现/文档抽取 | 基线行先记录为“shared skeleton baseline；并行组合细节未作为首轮主轴” | source map + 后续实现级抽取 artifact |
| `Megatron-LM` | 若有对应暴露则补充 | 若有对应暴露则补充 | 待补充 | 待补充 | 重点填写其与 `tensor / pipeline / expert parallelism` 的组合方式 | source map + 后续实现级抽取 artifact |

注意：上表不是在声称这些实现已经具备某个具体参数名；这里只定义比较矩阵需要承载的列结构。

## Should `Megatron-LM` be a supplementary table or a unified matrix column?

## Decision

**应并入统一配置矩阵的 `parallel composition` 列，而不是单独再开一张补充表。**

## Why unified column is better

### 1. `Megatron-LM` 的增量是“同一比较对象上的一个额外维度”，不是完全不同的对象

当前 repo 对 `Megatron-LM` 的角色定义是：查看 MoE 与 `tensor / pipeline / expert parallelism` 的组合方式，支撑 systems 分析。也就是说，它的主要增量是并行组合复杂度，而不是一整套与 `capacity factor`、`auxiliary loss`、`token dispatch` 完全无关的新主题。

既然它仍然属于“实现配置抽取”的同一问题空间，那么最稳定的表达方式就是把增量放进同一矩阵的 `parallel composition` 列。

Provenance:
- `projects/moe/literature/2026-03-24-moe-source-map.md`, `Megatron-LM` row.
- `projects/moe/plans/moe-survey-draft.md`, section `3.3 Systems source roles in the current source map`.
- `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`, finding that `Megatron-LM` is better treated as a second-pass source focused on parallel composition.

### 2. 单独补充表会打断“共有字段骨架”的比较连续性

本任务的目标之一是先建立 `DeepSpeed MoE` 的共有字段骨架。如果把 `Megatron-LM` 另开一张表，那么 future session 在横向比较时会重新面对两个问题：

1. 哪些字段是共享列，哪些是实现专属列？
2. `Megatron-LM` 的并行组合到底是 systems 附录，还是配置表主体的一部分？

这会让 README 当前已收敛的问题重新发散。相反，把 `parallel composition` 作为统一矩阵列，可以明确：
- 前四类字段是当前已确认的 shared baseline；
- `parallel composition` 是为 `Megatron-LM` 预留的增量列，但仍留在同一比较框架内。

Provenance:
- `projects/moe/TASKS.md`, this task’s `Done when` and `Next step` require one coherent first-pass skeleton plus a decision on how to represent `Megatron-LM` delta.
- `projects/moe/README.md`, the only remaining open question is exactly about representation inside the configuration matrix.

### 3. 统一矩阵更符合当前项目的“shared skeleton → systems extension”推进顺序

前一份 baseline comparison 已明确推荐顺序：
1. 先用 `DeepSpeed MoE` 建共享配置骨架；
2. 再用 `Megatron-LM` 增加 parallel-composition 差异；
3. 最后再用 `fairseq` 看 script / router-loss 表达。

这个顺序天然更适合“一张主表逐步加列/加注释”，而不是“每加入一个实现就新开一张表”。

Provenance:
- `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`, `Suggested follow-on order`.

## Practical implication for the next extraction pass

下一轮如果做实现级抽取，推荐按以下顺序填表：

1. 先完成 `DeepSpeed MoE` 行，至少填 `capacity factor`、`auxiliary loss`、`expert parallelism`、`token dispatch` 四类字段。
2. 再新增 `Megatron-LM` 行，并重点填 `parallel composition` 列，记录其与 `tensor / pipeline / expert parallelism` 的组合方式。
3. 如某实现在某列当前没有明确 evidence，则写为“待抽取 / 未在当前 artifact 中确认”，而不是推断填写。

## Compact conclusion

首版共有配置骨架应至少包含 7 列：
1. `implementation`
2. `capacity factor`
3. `auxiliary loss`
4. `expert parallelism`
5. `token dispatch`
6. `parallel composition`
7. `evidence source`

其中，前四类 MoE 关键字段来自当前 repo 对 `DeepSpeed MoE` 的直接定位；`parallel composition` 列用于把 `Megatron-LM` 的主要系统增量保留在同一张矩阵里，而不是拆成独立补充表。

## Open follow-up question

1. 下一轮实现级抽取时，`parallel composition` 列应采用多标签短语、分层子字段，还是受限词表，以保证 `Megatron-LM` 与后续其他实现之间仍可横向比较？
   - Provenance: 本文已决定该差异进入统一矩阵列，但尚未决定列内编码方式。