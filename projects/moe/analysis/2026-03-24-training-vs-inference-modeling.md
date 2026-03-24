# MoE 训练与推理是否应分开建模：当前证据与桥接指标候选

- Timestamp: 2026-03-24T13:43:44Z
- Project: `projects/moe`
- Task: 验证训练与推理场景是否应分开建模，并确定是否需要统一指标桥接二者
- Scope: 仅基于当前仓库已登记来源与既有分析笔记，整理 training-vs-inference 的证据边界，不引入新的外部检索。

## Sources used

1. `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`
2. `projects/moe/literature/2026-03-24-moe-source-map.md`
3. `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`
4. `projects/moe/plans/moe-survey-draft.md`

Provenance note: 本文中的“来源证据”均指上述仓库内 artifact 已经登记或已写明的来源用途。例如 source map 明确把 `DeepSpeed MoE` 标为训练框架集成 / capacity factor / token dispatch / expert parallelism 的配置入口，把 `Megatron-LM` 标为训练期并行组合入口，把 Hugging Face `SwitchTransformers` 文档标为面向配置字段与推理侧调用约束的工程参考。

## Question

要回答的不是“训练和推理是否完全无关”，而是两个更具体的问题：

1. **是否应先分开建模？** 也就是后续 systems 比较时，训练与推理是否需要不同的主指标与瓶颈假设。
2. **是否仍需要统一指标桥接？** 也就是在分开建模之后，是否还需要一组可跨两类场景复用的中间指标，避免项目内比较口径彻底断裂。

## Current evidence inventory

### A. 支持“训练与推理应先分开建模”的当前证据

#### Evidence A1: 当前仓库中训练侧证据明显更强，且其主语是吞吐、并行与容量

`projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md` 已把 MoE 系统问题组织为四类：token dispatch / gather、expert parallelism 带来的跨设备通信、expert placement / utilization、capacity-factor / overflow tuning。该文件对这些问题的 framing 明确围绕“step time / throughput / sharding / distributed execution”展开，而不是围绕单请求延迟。

- Provenance: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`, sections `Bottleneck 1` through `Bottleneck 4`.

这说明：**当前已沉淀的系统证据主要是训练式或批处理式视角**，其核心对象是并行训练中的移动、同步、利用率与容量调优。

#### Evidence A2: source map 中训练实现入口比推理入口更具体

source map 对三个实现入口的 intended use 写得很清楚：

- `DeepSpeed MoE`：用于抽取 `capacity factor`、`auxiliary loss`、`expert parallelism`、`token dispatch` 等工程配置旋钮；
- `Megatron-LM`：用于查看 MoE 与 `tensor / pipeline / expert parallelism` 的组合方式；
- `fairseq`：用于比对训练脚本、router loss 设置和实验配置表达方式。

这些都是**训练配置与训练系统组织**的描述。

相对地，source map 中与推理更直接相关的条目主要是 Hugging Face `SwitchTransformers` 文档，其 intended use 是“快速定位实现层参数名、配置字段与推理侧调用约束”。这表明当前仓库对推理侧的证据入口还较薄，且偏接口 / 配置，而非 serving systems benchmark。

- Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`, rows for `DeepSpeed MoE`, `Megatron-LM`, `Fairseq examples / MoE`, and `Hugging Face Transformers — SwitchTransformers documentation`.

因此，**训练与推理在当前 repo evidence base 中并不是同样成熟的比较对象**；若强行共用一个系统模型，容易把训练吞吐问题与推理延迟问题混写。

#### Evidence A3: 既有系统分析已经把 training-vs-inference separation 标成未决假设

现有 systems note 的 `Implications for projects/moe` 明确写道：训练与推理“should still be kept as separate comparison axes in future work”，但把它视为“awaiting finer-grained implementation or literature evidence rather than as a settled conclusion”。

- Provenance: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`, section `Implications for projects/moe`, item 3.

这条很关键：它没有宣称仓库已经证明“训练与推理完全不同”，但已经证明**把二者暂时合并讨论会超出当前证据分辨率**。

### B. 支持“即使分开建模，也需要桥接指标”的当前证据

#### Evidence B1: 训练与推理共享同一组结构性成本来源

尽管训练与推理关注的外层目标不同，现有 systems note 中四类瓶颈本身是结构性的：

1. token dispatch / gather；
2. expert parallelism 导致的跨设备通信；
3. expert placement / utilization；
4. capacity-factor / overflow。

这些成本来源不是训练专属概念，而是由 MoE 稀疏激活和 expert placement 机制本身引入的执行成本。因此，**它们可以作为训练 / 推理之间的桥接层**：上层目标函数不同，但底层结构性代价相同。

- Provenance: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`, compact comparison table and bottleneck sections.

#### Evidence B2: 路由分析已经显示“模型行为”和“系统开销”存在耦合，而不是可完全拆开

routing note 指出，routing 选择既影响负载均衡，也影响系统复杂度；systems note 则进一步指出 simpler routing 也是减少 distributed execution complexity 的手段。换言之，**同一个 routing / capacity 设计会同时影响训练稳定性、吞吐与潜在推理开销**。

- Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`; `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`, section `Cross-cutting synthesis`, item 2.

这说明项目不能把训练与推理做成两套完全断开的评价系统；至少要保留若干共同的中层变量，才能解释“同一个配置为什么在训练和推理上都变差或都变好”。

## What the current evidence does and does not prove

### What is supported now

1. **当前项目工作流中，训练与推理应先分开建模。**
   - Supported meaning: 在后续对比表、系统笔记和配置抽取中，不应把训练吞吐 / step-time 问题与推理延迟 / serving constraint 问题混成单一结论。
   - Provenance: source-map intended-use differences plus the systems note’s explicit “separate comparison axes” statement.

2. **即使分开建模，仍需要一层统一桥接指标。**
   - Supported meaning: 需要保留共享的结构性执行成本字段，作为训练与推理比较之间的中介层。
   - Provenance: the four bottlenecks in the systems note are mechanism-level costs introduced by MoE structure itself, not by only one workload type.

3. **当前证据强度在训练侧明显高于推理侧。**
   - Supported meaning: 当前仓库已登记的实现入口主要描述训练配置、并行策略和训练脚本；推理侧更像配置 / 接口入口，而不是完整 serving evidence base。
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md` intended-use text for `DeepSpeed MoE`, `Megatron-LM`, `Fairseq`, and Hugging Face `SwitchTransformers` docs.

### What remains hypothesis

1. **“训练主导瓶颈 = 通信 / 吞吐，推理主导瓶颈 = 延迟 / 小 batch inefficiency”** 目前仍是合理假设，不是被当前仓库严格证明的结论。
   - Why still hypothesis: 当前 source map 尚未登记专门的 serving benchmark、online inference kernel analysis 或 production latency study。
   - Provenance: absence of such sources in `projects/moe/literature/2026-03-24-moe-source-map.md`; open follow-up question 3 in `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`.

2. **“训练和推理需要完全不同的一套指标体系”** 也未被证明。
   - Why still hypothesis: 现有四类系统瓶颈显示二者至少共享 dispatch、communication、utilization、capacity 这些结构性变量。
   - Provenance: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`.

3. **“一个单一总指标可以充分覆盖训练与推理”** 也未被证明。
   - Why still hypothesis: 当前证据只足以提出桥接候选，还不足以证明某个单一数值可以同时保真地代表吞吐、延迟、容量和通信成本。
   - Provenance: same systems note plus the task rationale in `projects/moe/TASKS.md`, which explicitly warns against conflating throughput, latency, capacity, and communication cost.

## Recommended modeling split for this project

### Training track

优先建模对象：
- throughput / step time；
- communication exposure from expert parallelism；
- utilization balance；
- capacity overflow / drop pressure。

Why: 这些维度与当前 repo 中最强的实现入口 (`DeepSpeed MoE`, `Megatron-LM`, `fairseq`) 以及既有 systems note 的 framing 一致。

- Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`; `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`.

### Inference track

优先建模对象：
- latency sensitivity to token dispatch path；
- routing simplicity vs serving complexity；
- active-parameter path length / per-token work；
- whether capacity / placement constraints create tail-latency or batching constraints。

Why: 当前 repo 对推理的直接证据较少，因此这里应先作为“轻量 hypothesis frame”而非强结论；但 Hugging Face `SwitchTransformers` 文档与 `Switch Transformers` / `Mixtral` 这类实现/模型入口足以支撑首版问题框架。

- Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md`, rows for `Switch Transformers`, `Mixtral of Experts`, and Hugging Face `SwitchTransformers` documentation.

## Bridge metric candidates

以下指标在当前仓库中只能称为 **candidate bridge metrics**，不是已被当前 sources 共同验证的标准答案。

### Candidate 1: 每 token 的 expert fan-out / dispatch complexity

含义：每个 token 需要被送往多少 expert，以及因此引入多少 dispatch / gather 复杂度。

为什么可桥接：
- 对训练，它影响通信量、packing 复杂度和 step throughput；
- 对推理，它影响单 token 执行路径长度和潜在延迟放大。

Current source support:
- routing note 区分了 top-k、top-1 与其他 routing family；
- systems note 明确把 token dispatch / gather 当作第一类系统瓶颈。

- Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`; `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`.

### Candidate 2: expert utilization / load skew

含义：token 负载是否集中到少数 hot experts，或能否较均匀地占用已分配专家容量。

为什么可桥接：
- 对训练，它影响吞吐、设备利用率与 overflow；
- 对推理，它可能影响某些 expert 的热点排队、batching 不稳定性或 tail-latency 风险。

Current source support:
- routing note 把负载均衡列为核心问题；
- systems note 把 expert placement / utilization 视为第三类瓶颈。

- Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`; `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`.

### Candidate 3: overflow / unused-capacity rate

含义：容量设置下有多少 token 溢出、被丢弃、被重分配，或有多少保留容量未被使用。

为什么可桥接：
- 对训练，它连接稳定性、吞吐与硬件利用率；
- 对推理，它连接容量预留、请求路径稳定性与是否需要为 tail cases 付出额外资源。

Current source support:
- systems note 把 `capacity-factor and overflow choices` 列为第四类瓶颈；
- source map 明确将 `capacity factor` 作为 `DeepSpeed MoE` 的抽取目标。

- Provenance: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`, `Bottleneck 4`; `projects/moe/literature/2026-03-24-moe-source-map.md`, row for `DeepSpeed MoE`.

### Candidate 4: communication-to-compute exposure

含义：不是追求单一标准公式，而是记录某个配置中 dispatch / communication 开销相对于 active expert compute 的暴露程度。

为什么可桥接：
- 对训练，它决定 sparse FLOPs 是否真正转化为 throughput；
- 对推理，它决定省下的计算是否又被跨设备或 gather 路径吃回去。

Current source support:
- systems note 的核心综合判断就是“sparse FLOPs are not the same as end-to-end speedup”；
- `GShard` 与 `Megatron-LM` 在 source map 中都被登记为并行 / sharding / communication 路径入口。

- Provenance: `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`, section `Cross-cutting synthesis`, item 1; `projects/moe/literature/2026-03-24-moe-source-map.md`, rows for `GShard` and `Megatron-LM`.

## Decision for current project state

### Conclusion

**当前项目应把训练与推理先分开建模，但不能完全分家。**

更具体地说：

1. 训练与推理的顶层评价对象应分开：训练优先看 throughput / distributed efficiency，推理优先看 latency / serving path constraints。
2. 同时保留一层共享的结构性桥接指标：dispatch complexity、expert utilization、overflow / unused capacity、communication-to-compute exposure。
3. 在当前证据条件下，不应宣称某一个统一总指标已经足够覆盖训练与推理；更安全的做法是使用“分场景顶层指标 + 共享中层桥接字段”的两层模型。

## Implications for next sessions

1. 后续 systems 对比应默认拆成 `training` 与 `inference` 两个子表，而不是一个混合表。
2. 配置旋钮抽取任务应优先看哪些字段能映射到上面的四个 bridge candidates。
3. 如果后续新增 serving-specific literature 或实现 benchmark，应重点验证的是：推理是否真的出现与训练显著不同的主导瓶颈排序，而不是重复证明 dispatch / utilization / capacity 这些结构成本的存在。
