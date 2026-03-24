# Multi-Agent 方法分类体系与方法对比表

- Timestamp: 2026-03-24T21:18:07+08:00
- Project: `projects/multi-agent-survey`
- Purpose: 为综述提供可复用的 Multi-Agent 方法分类体系、代表论文、优缺点与适用场景对比表。
- Provenance boundary: 本文仅综合仓库内已有文献清单与 literature notes，不引入新的外部检索。

## Sources used

1. `projects/multi-agent-survey/literature/icml-2024-2025.md`
2. `projects/multi-agent-survey/literature/neurips-2024-2025.md`
3. `projects/multi-agent-survey/literature/iclr-2025-2026.md`
4. `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`
5. `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md`
6. `projects/multi-agent-survey/literature/omnibench-note.md`
7. `projects/multi-agent-survey/literature/agent-smith-note.md`
8. `projects/multi-agent-survey/literature/mdagents-note.md`
9. `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md`
10. `projects/multi-agent-survey/logs/2026-03-23T170500Z-single-vs-multi-agent-boundary-synthesis.md`

## Classification principle

本分类体系按“**多智能体系统究竟把哪一部分变成显式设计变量**”来组织，而不是只按会议或应用领域分组。这样更适合回答综述中的核心问题：什么时候多智能体真的有必要，什么时候 single-agent + tools 已经足够。

这里把当前仓库证据归纳为 6 类：

1. **角色/拓扑驱动架构**：系统优势来自 agent role、层级、图结构或拓扑设计。
2. **任务分解与协调优化**：系统优势来自显式分工、计划分配、联合决策或协同学习。
3. **通信与共享记忆机制**：系统优势来自消息压缩、选择性通信、共享记忆、辩论协议等。
4. **训练/自改进型多智能体**：系统优势来自 RL/self-play/post-training，让多个 agent 在训练时互相塑造。
5. **评测/基准/诊断型工作**：系统价值不在“提出更强系统”，而在回答怎样评测多智能体、在哪些维度会失效。
6. **高价值应用型系统**：系统价值在真实任务落地，检验 multi-agent 是否带来超出单体系统的实际收益。

## 方法分类总表

| 类别 | 核心机制 | 代表论文 | 主要优点 | 主要缺点 | 更适用场景 |
|---|---|---|---|---|---|
| 角色/拓扑驱动架构 | 通过 manager-worker、graph-of-agents、动态拓扑把信息流显式结构化 | `Graph-of-Agents` (`iclr-2025-2026.md`, entry 95); `GoAgent` (`2026-03-23-goagent-communication-topology.md`); `Multi-Agent Design` (`iclr-2025-2026.md`, entry 117) | 能把复杂任务拆成结构化子问题；可控制信息路由；更容易扩展到多角色协作 | 设计空间大、调参重；错误会沿拓扑传播；收益常依赖任务可分解性 | 长链路推理、复杂 research/workflow、需要控制通信结构的任务 |
| 任务分解与协调优化 | 通过 task allocation、joint planning、coordination policy 优化协作过程 | `CaPo` (`iclr-2025-2026.md`, entry 8); `MiTa` (`arxiv-2026-01-to-2026-03.md`, 2026-01 entry 5); `Cross-environment Cooperation Enables Zero-shot Multi-agent Coordination` (`icml-2024-2025.md`, entry 23) | 当任务天然可分工时效果最好；可并行；能提升鲁棒性和覆盖面 | 协调开销高；分工不当会抵消收益；对任务边界和接口定义敏感 | embodied cooperation、复杂流程任务、多人/多体系统协调 |
| 通信与共享记忆机制 | 将消息传递、共享记忆、KV sharing、memory masking、压缩通信作为关键变量 | `Cut the Crap` (`iclr-2025-2026.md`, entry 13); `KVComm` (`iclr-2025-2026.md`, entry 100); `Agent Reviewers` (`icml-2024-2025.md`, entry 16) | 可降低 token/带宽成本；保留必要协作；能提升可解释性与长期一致性 | 通信不足会损害协作质量；共享记忆可能引入污染/级联错误；协议设计复杂 | token 成本敏感场景、长任务上下文共享、多 agent 共写共审 |
| 训练/自改进型多智能体 | 用 self-play、actor-critic、post-training、preference optimization 直接训练协作行为 | `ACC-Collab` (`iclr-2025-2026.md`, entry 3); `AgentPO` (`iclr-2025-2026.md`, entry 60); `Learning Decentralized LLM Collaboration with Multi-Agent Actor Critic` (`arxiv-2026-01-to-2026-03.md`, 2026-01 entry 9) | 能把“合作本身”学出来，而非手写协议；在固定 benchmark 上可显著提升协作质量 | 训练成本高；泛化与稳定性不一定好；很难与 single-agent + tools 公平对比 | 有可重复环境、可在线/离线训练、希望优化协作策略而非仅 orchestration 的任务 |
| 评测/基准/诊断型工作 | 把 benchmark、failure attribution、安全压力测试、能力维度建模做成核心贡献 | `Windows Agent Arena` (`windows-agent-arena-note.md`); `OmniBench` (`omnibench-note.md`); `A2ASecBench` (`iclr-2025-2026.md`, entry 55); `LiveResearchBench` (`iclr-2025-2026.md`, entry 103); `Agent Smith` (`agent-smith-note.md`) | 能回答“什么时候值得用多智能体”；揭示系统级失败模式；为 head-to-head 比较打基础 | 不直接提升系统能力； benchmark 往往带有任务偏置；指标设计可能落后于真实使用需求 | survey、系统评估、产品选型、安全评测、研究复现 |
| 高价值应用型系统 | 面向医学、科学发现、GUI/OS、交通、网络等具体高价值场景设计 agent society | `MDAgents` (`mdagents-note.md`); `AI Agents Can Already Autonomously Perform Experimental High Energy Physics` (`ai-agents-hep-note.md`); `CellAgent` (`iclr-2025-2026.md`, entry 69); `ATLAS` (`iclr-2025-2026.md`, entry 62) | 最能检验真实价值；容易体现角色互补和专家分工；对综述“未来方向”最有承载力 | 容易受领域工程和专有流程影响；跨任务迁移性弱； often 缺少强 single-agent baseline | 高风险决策支持、科研 workflow、跨工具复杂工作流、需要多视角审查的任务 |

## Per-category comparison notes

### 1. 角色/拓扑驱动架构

**定义**
- 不把 multi-agent 视为“多开几个模型实例”，而是把**结构**当作一等公民：谁和谁通信、通信层级如何组织、拓扑是否静态或动态。

**Representative papers**
- `Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration` — `projects/multi-agent-survey/literature/iclr-2025-2026.md`, entry 95.
- `GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems` — `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md`.
- `Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies` — `projects/multi-agent-survey/literature/iclr-2025-2026.md`, entry 117.
- `CARD: Towards Conditional Design of Multi-agent Topological Structures` — `projects/multi-agent-survey/literature/iclr-2025-2026.md`, entry 68.

**Strengths**
- 对“信息该流向哪里”进行显式控制，而不是默认 all-to-all chat。
- 更适合复杂任务的层级化分解。
- 与仓库内 open question “communication-topology generation 是否会成为独立方法类”直接相关。

**Weaknesses**
- 拓扑搜索空间大，调参复杂。
- 如果上层路由错误，会导致系统级瓶颈或传播错误。
- 当前仓库证据仍不足以证明这类方法在所有任务上优于单体 agent + tools。

**Best-fit scenarios**
- 复杂 research、软件工程、长链 reasoning、需要不同专家角色交互的任务。
- 通信成本高、必须做稀疏信息路由的任务。

### 2. 任务分解与协调优化

**定义**
- 核心不是网络拓扑，而是**谁做什么、何时交接、怎样联合行动**。

**Representative papers**
- `CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation` — `iclr-2025-2026.md`, entry 8.
- `MiTa: A Hierarchical Multi-Agent Collaboration Framework with Memory-integrated and Task Allocation` — `arxiv-2026-01-to-2026-03.md`, 2026-01 entry 5.
- `Cross-environment Cooperation Enables Zero-shot Multi-agent Coordination` — `icml-2024-2025.md`, entry 23.
- `LLM-Assisted Semantically Diverse Teammate Generation for Efficient Multi-agent Coordination` — `icml-2024-2025.md`, entry 24.

**Strengths**
- 在任务天然可拆解时，多智能体最容易兑现收益。
- 允许并行和专业化，减少单个 agent 上下文过载。
- 对 embodied、MARL、human-AI coordination 问题尤其关键。

**Weaknesses**
- 协调成本可能高于分工收益。
- 对接口定义、子任务边界、回滚机制非常敏感。
- 当任务实际是单线程、低分叉流程时，可能不如 single-agent + tools 简洁有效。

**Best-fit scenarios**
- 多步骤工作流、robotics/embodied cooperation、需要并行探索与汇总的任务。

### 3. 通信与共享记忆机制

**定义**
- 将 communication protocol 视作主创新点，包括 message pruning、compressed communication、shared memory、selective KV sharing、辩论协议等。

**Representative papers**
- `Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems` — `iclr-2025-2026.md`, entry 13.
- `KVComm: Enabling Efficient LLM Communication through Selective KV Sharing` — `iclr-2025-2026.md`, entry 100.
- `Agent Reviewers: Domain-specific Multimodal Agents with Shared Memory for Paper Review` — `icml-2025-2025.md` typo? see note below.
- `Multi-Agent Debate with Memory Masking` — `iclr-2025-2026.md`, entry 116.
- `Benefits and Limitations of Communication in Multi-Agent Reasoning` — `iclr-2025-2026.md`, entry 65.

**Strengths**
- 直接回应多智能体最现实的系统问题：token 开销和上下文冗余。
- 共享记忆能提高长期任务一致性。
- 选择性通信可以把 multi-agent 从“昂贵群聊”推进到“稀疏协作系统”。

**Weaknesses**
- 通信设计常带来额外工程复杂度。
- 共享记忆会扩大错误污染面；与 `Agent Smith` 的系统级传播风险相呼应。
- 在简单任务上，复杂通信机制通常不值得。

**Best-fit scenarios**
- 上下文很长、多个 agent 必须共享中间产物、token 成本敏感的任务。

**Note**
- `Agent Reviewers` 的准确出处为 `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 16。

### 4. 训练/自改进型多智能体

**定义**
- 与 orchestration-only 方法不同，这类工作试图通过 RL、self-play、preference optimization 或 post-training 学到更好的协作策略。

**Representative papers**
- `ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration` — `iclr-2025-2026.md`, entry 3.
- `AgentPO: Enhancing Multi-Agent Collaboration via Reinforcement Learning` — `iclr-2025-2026.md`, entry 60.
- `MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference` — `iclr-2025-2026.md`, entry 107.
- `Learning Decentralized LLM Collaboration with Multi-Agent Actor Critic` — `arxiv-2026-01-to-2026-03.md`, 2026-01 entry 9.
- `Coevolving with the Other You: Fine-Tuning LLM with Sequential Cooperative Multi-Agent Reinforcement Learning` — `neurips-2024-2025.md`, entry 1.

**Strengths**
- 如果任务环境明确，可把“合作”本身变成可优化目标。
- 比手工 prompt/role 编排更有潜力跨任务泛化。
- 对 benchmark 上的协作质量、效率、协调稳定性可能有较大收益。

**Weaknesses**
- 训练成本高，且容易受 reward design 和环境偏置影响。
- 对现实开放世界任务，离线训练得到的协作策略未必稳定迁移。
- 当前仓库没有足够 head-to-head 证据证明它稳健优于更简单的 orchestration 方法。

**Best-fit scenarios**
- 有标准环境、可反复采样、可以清晰定义 reward/feedback 的任务。
- 希望把合作协议长期固化到模型行为中的系统。

### 5. 评测/基准/诊断型工作

**定义**
- 目标不是再造一个 agent framework，而是回答：**怎样公平评估 multi-agent，哪些 failure mode 是多智能体特有的，哪些 benchmark 真正能区分方法优劣**。

**Representative papers**
- `Windows Agent Arena` — `projects/multi-agent-survey/literature/windows-agent-arena-note.md`.
- `OmniBench` — `projects/multi-agent-survey/literature/omnibench-note.md`.
- `Ad-Hoc Human-AI Coordination Challenge` — `projects/multi-agent-survey/literature/ad-hoc-human-ai-coordination-challenge-note.md`.
- `A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems` — `iclr-2025-2026.md`, entry 55.
- `LiveResearchBench: Benchmarking Single- and Multi-Agent Systems for Citation-Grounded Deep Research` — `iclr-2025-2026.md`, entry 103.
- `Agent Smith` — `projects/multi-agent-survey/literature/agent-smith-note.md`.

**Strengths**
- 这是回答“什么时候值得用多智能体”的必要工具层。
- 能把任务成功率之外的维度纳入评估，如安全、传播性失效、能力覆盖、人与 agent 协作质量。
- `LiveResearchBench` 在标题层面已直接覆盖 single- vs multi-agent 对比，是后续综述的关键锚点之一。

**Weaknesses**
- benchmark 设计很容易绑定特定任务分布。
- 评价指标是否覆盖真实部署需求仍是开放问题。
- 有些 benchmark 更像“能力展示平台”，不一定提供强因果归因。

**Best-fit scenarios**
- survey synthesis、系统选型、安全验证、比较不同 agent 范式。

### 6. 高价值应用型系统

**定义**
- 在具体垂直领域中部署多智能体，观察它是否真的带来比单体 agent 更好的实用结果。

**Representative papers**
- `MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making` — `projects/multi-agent-survey/literature/mdagents-note.md`.
- `AI Agents Can Already Autonomously Perform Experimental High Energy Physics` — `projects/multi-agent-survey/literature/ai-agents-hep-note.md`.
- `ATLAS: Constraints-Aware Multi-Agent Collaboration for Real-World Travel Planning` — `iclr-2025-2026.md`, entry 62.
- `CellAgent: LLM-Driven Multi-Agent Framework for Natural Language-Based Single-Cell Analysis` — `iclr-2025-2026.md`, entry 69.
- `CoLLMLight` — `iclr-2025-2026.md`, entry 71.

**Strengths**
- 最接近“业务价值”与“科学价值”的真实检验。
- 角色分工、专家互补、交叉检查更容易在高价值领域体现。
- 对未来方向章节最有帮助，因为它暴露真实部署瓶颈。

**Weaknesses**
- 领域工程影响很大，难以迁移到一般任务。
- 如果没有强 single-agent baseline，很难证明 multi-agent 是必要的，而不是“更多工程”。
- 数据、工具、流程通常高度定制，复现门槛高。

**Best-fit scenarios**
- 医疗、科研、复杂 GUI/操作系统、交通控制、网络系统等高 stakes 工作流。

## Cross-category comparison table

| 维度 | 角色/拓扑驱动 | 协调优化 | 通信/共享记忆 | 训练/自改进 | 评测/基准/诊断 | 高价值应用 |
|---|---|---|---|---|---|---|
| 主要回答的问题 | agent 应该如何组织 | 子任务如何协同 | 信息如何流动 | 协作行为如何学出来 | 怎么知道系统真的更好 | 在真实场景是否有价值 |
| 典型收益来源 | 结构化路由 | 分工与并行 | 降低冗余、增强一致性 | 学习协作策略 | 暴露真实能力/风险 | 领域专家化、流程闭环 |
| 典型成本 | 设计复杂度 | 协调开销 | 协议与内存管理复杂度 | 训练成本 | benchmark 构建成本 | 领域工程与复现成本 |
| 最容易失效的地方 | 路由错误、拓扑僵化 | 分工错误、交接失败 | 信息污染、上下文丢失 | reward 偏差、泛化差 | 指标偏置 | 缺少可迁移性 |
| 相比 single-agent + tools 更可能胜出的条件 | 任务需要多视角路由 | 任务天然可分解 | 上下文/带宽是瓶颈 | 协作可在环境中反复优化 | 需要严谨比较与安全评估 | 真实任务存在专家分工 |

## Practical synthesis for the survey

### When multi-agent is more justified

基于仓库内现有证据，multi-agent 更值得优先考虑的情形是：

1. **任务天然可分解且需要角色互补**。
   - Provenance: `CaPo`, `MiTa`, `ATLAS`, `MDAgents`。
2. **信息路由本身是难点，而不是附属问题**。
   - Provenance: `GoAgent`, `Graph-of-Agents`, `Cut the Crap`, `KVComm`。
3. **需要显式处理协调、辩论、共享记忆或故障传播**。
   - Provenance: `Agent Smith`, `Benefits and Limitations of Communication in Multi-Agent Reasoning`, `Agent Reviewers`。
4. **需要系统级 benchmark / safety / robustness 评估，而不是只看单题正确率**。
   - Provenance: `Windows Agent Arena`, `OmniBench`, `A2ASecBench`, `LiveResearchBench`。

### When single-agent + tools is still the better default

1. 任务基本是单线程规划 + 工具调用。
2. 协调收益不明显，但 token/延迟开销会线性上升。
3. 没有强证据表明角色分工优于一个强模型的长上下文/工具使用。
4. 缺乏 benchmark 来证明多智能体增加的复杂性是值得的。

This remains consistent with `projects/multi-agent-survey/logs/2026-03-23T170500Z-single-vs-multi-agent-boundary-synthesis.md`, which records the current repo-level provisional rule: **single-agent + tools first, unless coordination/communication/topology is itself the hard part**.

## Key takeaways

1. 当前仓库证据最强的方法主线，不是“越多 agent 越强”，而是**把结构、协调、通信、评测逐步显式化**。
2. 2026 年的一个明显趋势是：**拓扑设计与通信效率**正从实现细节上升为独立研究问题。
   - Provenance: `GoAgent`, `Multi-Agent Design`, `Cut the Crap`, `KVComm`。
3. 评测层正在快速补课，尤其是 realistic benchmark、security benchmark、single-vs-multi head-to-head benchmark。
   - Provenance: `Windows Agent Arena`, `OmniBench`, `A2ASecBench`, `LiveResearchBench`。
4. 对综述而言，最有解释力的结构不是按会议划分，而是按“**结构设计 / 协调机制 / 通信机制 / 训练方式 / 评测工具 / 应用落地**”六类组织。

## Open follow-up items

1. `LiveResearchBench` 是否应纳入后续 load-bearing evaluation 子集，作为 single-vs-multi-agent 边界问题的关键证据？
2. `A2ASecBench`、`DoVer`、`Measuring Bias Amplification in Multi-Agent Systems with Large Language Models` 中，哪些最适合代表 2026 evaluation 章节？
3. 拓扑生成类工作（如 `GoAgent`、`CARD`、`Multi-Agent Design`）是否应在最终综述中单列为“Topology Optimization”而非并入 Architecture？
