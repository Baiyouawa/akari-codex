# MoE 配置矩阵笔记：`parallel composition` 列的行内编码方式

- Timestamp: 2026-03-24T13:59:06Z
- Project: `projects/moe`
- Task: 规定 `parallel composition` 列的行内编码方式，以支持 `Megatron-LM` 与后续实现的稳定横向比较
- Scope: 仅基于仓库内既有配置矩阵决策与实现入口定位，比较候选编码方案，并为统一矩阵中的单列编码给出推荐。

## Sources used

1. `projects/moe/analysis/2026-03-24-deepspeed-baseline-config-skeleton.md`
2. `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`
3. `projects/moe/literature/2026-03-24-moe-source-map.md`
4. `projects/moe/README.md`
5. `projects/moe/TASKS.md`

Provenance note: 本文不引入新的外部实现检索；所有比较标准都锚定在 repo 已确认的前提：`DeepSpeed MoE` 先提供共享字段骨架，`Megatron-LM` 的主要增量价值集中在并行组合差异，并且这些差异已经决定放入统一矩阵的 `parallel composition` 列。

## Decision target

已知前提有两点：

1. 统一配置矩阵至少包含 `parallel composition` 这一列。
   - Provenance: `projects/moe/analysis/2026-03-24-deepspeed-baseline-config-skeleton.md`.
2. `Megatron-LM` 在当前项目中的主要增量角色是观察 MoE 与 `tensor / pipeline / expert parallelism` 的组合方式。
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`, `Megatron-LM` row; `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`.

因此这里真正要决定的是：**同一单元格里如何编码并行组合，既保持横向可比，又不把矩阵重新拆成多张表。**

## Evaluation criteria

候选方案按三个 repo-internal 目标比较：

1. **可比性**：未来 session 能否用同一表达直接对比 `DeepSpeed MoE`、`Megatron-LM` 与后续实现。
2. **抗漂移性**：是否能抑制自由文本造成的别名、顺序不一致和描述粒度漂移。
3. **抽取成本**：下一轮做实现级抽取时，是否能低成本落地到现有统一矩阵，而不需要额外 schema 改造。

Provenance: 这三个标准直接服务于当前任务文本中“稳定横向比较”“避免自由文本漂移”与“统一矩阵列”的要求；见 `projects/moe/TASKS.md` 当前任务描述，以及 `projects/moe/README.md` 的唯一开放问题表述。

## Candidate schemes

### Option A — 多标签短语

示例：
- `expert parallelism only`
- `tensor + expert parallelism`
- `pipeline + tensor + expert parallelism`

#### Strengths

1. 人类可读性最好。
2. 不需要额外字段定义，写起来最快。

#### Weaknesses

1. 容易出现同义改写漂移，如 `tensor + expert`、`TP+EP`、`tensor/expert hybrid` 可能都在表达同一件事。
2. 排序和连接词不稳定，后续做过滤或统计时需要再归一化。
3. 难以区分“未观察到某维度”与“作者只是没写出来”。

#### Assessment

适合作为草稿速记，不适合作为项目级稳定编码。

## Option B — 分层子字段

示例：把单列拆成结构化子字段：
- `dp: yes/no`
- `tp: yes/no`
- `pp: yes/no`
- `ep: yes/no`

或在单元格中写成伪结构：
- `dp=0,tp=1,pp=1,ep=1`

#### Strengths

1. 机器可解析性最强。
2. 是否启用某种并行维度一目了然。
3. 对后续排序、筛选和透视表最友好。

#### Weaknesses

1. 它实际把单列重新扩展成了隐式 schema，偏离当前任务想保留的“统一矩阵中的单列”表达。
2. 会提高抽取负担：未来 session 需要维护字段名、布尔值、缺失值约定。
3. 对当前 repo 阶段而言过早结构化；现有 artifacts 只要求先稳定表示组合差异，并未要求单列内承载完整机器 schema。

#### Assessment

如果未来矩阵升级为真正的结构化数据表，这会是强候选；但对当前单列场景来说，复杂度偏高。

## Option C — 受限词表 + 规范顺序的单元格编码

示例词表：
- `none`
- `ep`
- `tp`
- `pp`
- `dp`

组合规则：
- 使用固定缩写词表 `{dp, tp, pp, ep}`。
- 组合时按固定顺序 `dp+tp+pp+ep` 书写，只写已确认出现的维度。
- 若当前 artifact 只证明 MoE 专家并行而未见其他并行组合，则写 `ep`。
- 若明确未结合额外并行维度，可写 `none` 或 `unspecified-baseline`；当前项目更适合用 `unspecified-baseline` 表示“此实现在当前骨架里不是以并行组合作为主抽取目标”。

示例：
- `unspecified-baseline`
- `ep`
- `tp+ep`
- `pp+tp+ep`

#### Strengths

1. 保留单列表达，符合已确定的统一矩阵方案。
2. 通过受限词表和固定顺序抑制自由文本漂移。
3. 对人和机器都足够友好：人能读，后续脚本也能按 `+` 分割。
4. 抽取成本低，不需要把当前矩阵升级成多子字段 schema。

#### Weaknesses

1. 细节表达力弱于分层子字段，不能直接编码“主次关系”“拓扑位置”等更细信息。
2. 仍需要一个缺失值约定，以区分 `unknown`、`not emphasized`、`not applicable`。

#### Assessment

这是当前项目阶段最平衡的方案：约束足够强，又不会破坏单列设计。

## Recommendation

**推荐方案：Option C — 受限词表 + 规范顺序的单元格编码。**

### Why this is the best fit now

1. 它直接服务于当前 repo 已做出的矩阵决策：`parallel composition` 应保留为统一矩阵中的一列，而不是拆表。
   - Provenance: `projects/moe/analysis/2026-03-24-deepspeed-baseline-config-skeleton.md`.
2. 它最贴合 `Megatron-LM` 的当前项目角色：重点不是记录任意解释性 prose，而是稳定表示 `tensor / pipeline / expert parallelism` 的组合差异。
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`.
3. 它比多标签短语更抗漂移，又比分层子字段更低成本，适合“先完成实现级抽取，再视需要升级 schema”的当前阶段。
   - Provenance: 本文上文对三个候选方案的对比。

## Canonical encoding rule for next sessions

后续在统一矩阵中填写 `parallel composition` 列时，采用以下规则：

1. **只允许使用受限词表**：`dp`、`tp`、`pp`、`ep`。
2. **多维组合按固定顺序编码**：`dp+tp+pp+ep`。
   - 例如同时出现 tensor 与 expert parallelism，写 `tp+ep`，不要写 `ep+tp`。
3. **单维情况直接写单 token**：如 `ep`。
4. **当前 artifact 未把该实现的并行组合作为明确差异点时**，写 `unspecified-baseline`，不要用自由文本说明句。
5. **若证据不足以确认是否存在某并行维度**，写 `unknown`，不要推断补全。

## Minimal examples

| implementation | parallel composition | Why this form is allowed |
|---|---|---|
| `DeepSpeed MoE` | `unspecified-baseline` | 当前 repo 将其首先定位为共享 MoE 旋钮骨架来源，而不是并行组合主入口。 Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/analysis/2026-03-24-implementation-baseline-comparison.md`. |
| `Megatron-LM` | `tp+pp+ep` | 合法，因为只使用受限词表且顺序规范；具体值仍需在下一轮实现抽取时由证据确认。 Provenance: 编码规则来自本文；`Megatron-LM` 关注并行组合来自 `projects/moe/literature/2026-03-24-moe-source-map.md`. |
| future implementation | `ep` | 合法，因为单维并行可直接用受限词表单 token 表示。 Provenance: 本文编码规则. |

Provenance note: 上表第二行展示的是**编码形式示例**，不是对 `Megatron-LM` 已完成抽取的事实断言；具体值仍需在后续实现级抽取中由证据填写。

## Compact conclusion

为保证 `parallel composition` 列能稳定支持 `Megatron-LM` 与后续实现的横向比较，当前项目应采用：

- **单列保留**；
- **受限词表 `{dp, tp, pp, ep}`**；
- **固定顺序 `dp+tp+pp+ep`**；
- **缺失值约定 `unspecified-baseline` / `unknown`**。

这样既避免自由文本漂移，也不必把当前统一矩阵过早升级成多子字段 schema。
