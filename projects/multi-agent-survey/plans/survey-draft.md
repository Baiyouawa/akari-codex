# Multi-Agent 研究综述初稿（2024-2026）

- Timestamp: 2026-03-24T21:18:53+08:00
- Project: `projects/multi-agent-survey`
- Status: draft
- Provenance scope: 本稿仅基于仓库内已沉淀的文献清单、literature notes 与 session logs 组装，不引入新的外部检索结果。核心来源包括：
  - `projects/multi-agent-survey/literature/neurips-2024-2025.md`
  - `projects/multi-agent-survey/literature/icml-2024-2025.md`
  - `projects/multi-agent-survey/literature/iclr-2025-2026.md`
  - `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`
  - `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md`
  - `projects/multi-agent-survey/literature/*-note.md` 中已完成的 load-bearing literature notes
  - `projects/multi-agent-survey/logs/2026-03-23T16:40:00Z-arxiv-subdirection-synthesis.md`
  - `projects/multi-agent-survey/logs/2026-03-23T170500Z-single-vs-multi-agent-boundary-synthesis.md`

## 1. 引言

2024-2026 的 Multi-Agent 研究出现了非常清晰的结构性变化：如果说更早阶段的多智能体研究主要由 MARL、合作博弈、分布式决策和 emergent communication 驱动，那么 2024 之后，随着大模型 agent 框架的普及，Multi-Agent 不再只是“多个策略体在环境里互动”的问题，而逐渐变成“多个具备语言、工具使用、记忆、规划与角色分工能力的 agent，如何在复杂任务上形成稳定、可控、可评估协作”的问题。这个变化在仓库现有文献资产中已经能看得很明显。

首先，从顶会覆盖看，当前仓库内已经沉淀了三类互补证据。NeurIPS 2024 候选池中保留了 138 篇相关论文，包含传统 MARL、零样本协作、通信与一批 LLM-based collaboration/application 论文；但 NeurIPS 2025 仍因索引来源问题暂未补齐，因此本稿不会对 NeurIPS 2025 做完备性断言，相关限制见 `projects/multi-agent-survey/literature/neurips-2024-2025.md`。ICML 2024-2025 当前已整理 24 篇 venue-verified 论文，呈现出“2024 偏 MARL/theory，2025 增加 LLM-agent benchmark 与系统论文”的转向，见 `projects/multi-agent-survey/literature/icml-2024-2025.md`。ICLR 2025-2026 已通过官方 schedule 页构建了 146 篇去重论文清单，其中 2025 年 54 篇、2026 年 92 篇，且已验证 Oral/Poster 标签，见 `projects/multi-agent-survey/literature/iclr-2025-2026.md`。单看数量，ICLR 2026 比 ICLR 2025 多出 38 篇（内联算术：92 - 54 = 38），说明 multi-agent 相关工作在最新一届 ICLR 的可见度显著上升。

其次，从 arXiv 最新趋势看，仓库当前可复现的 2026-01-01 到 2026-03-23 抓取结果包含 396 篇去重后的相关记录，其中 1 月 55 篇、2 月 89 篇、3 月 252 篇（内联算术：55 + 89 + 252 = 396），见 `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`。这组数字非常重要，因为它说明研究热度不仅没有放缓，反而在 2026 年 3 月明显加速。更关键的是，这批论文的主方向不是单一的 MARL 或单一的通信优化，而是以 architecture/orchestration 为最强主线，evaluation-heavy systems 为第二主线，MARL-backed coordination 作为仍然强势但正在与 agent systems 融合的第三主线。这一判断在 `projects/multi-agent-survey/logs/2026-03-23T16:40:00Z-arxiv-subdirection-synthesis.md` 中已经形成明确结论。

因此，本综述初稿的目标，不是做一个“论文罗列式”的大全，而是回答五个更有结构的问题：

1. 2024-2026 的 Multi-Agent 研究到底在研究什么？
2. 方法分类上，当前主流路线有哪些，彼此有什么关系？
3. 从顶会到最新 arXiv，哪些方向是真正变热的，哪些只是老问题的新包装？
4. Multi-Agent 相比 Single-Agent + tools 的边界在哪里？
5. 下一阶段最值得关注的研究空白是什么？

为了回答这些问题，下面按方法分类、关键发现、趋势分析与未来方向展开。

## 2. 方法分类

基于项目 README 中预先定义的分类框架，以及当前已整理文献的实际分布，Multi-Agent 研究在 2024-2026 至少可以分成六个核心类别：Architecture、Coordination、Communication、Evaluation、Application、Theory。这个分类并不是互斥标签，而更像是一个“主问题”维度。大量论文同时跨越多个维度，例如既是 architecture paper，又带 evaluation；既涉及 communication，又把 coordination 当作主要难点。

### 2.1 Architecture：从静态角色编排走向动态协作结构

Architecture 是当前样本中最强的主轴。尤其在 ICLR 2026 与 2026 年初 arXiv 中，最常见的问题不是“有没有多个 agent”，而是“这些 agent 该如何组织”。这类工作关心的对象包括：角色分工、层级结构、共享记忆、工作流编排、图结构协作、运行时 token/compute 控制，以及 agent 网络如何自配置、自修复、自演化。

从 ICLR 2025-2026 文献看，代表性题目已经能勾勒出这条线索：`Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration`、`MAS^2: Self-Generative, Self-Configuring, Self-Rectifying Multi-Agent Systems`、`MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference`、`Agentic Collaboration as an Information Bottleneck Problem`、`Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems`、`TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture` 等，见 `projects/multi-agent-survey/literature/iclr-2025-2026.md`。

从 arXiv 近三个月结果看，这条线又向“结构可学习”推进。例如 `GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems` 被单独记为 horizon-scan note，明确提出通信拓扑本身是生成对象，而不只是设计者手工选择的模板，见 `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md`。这意味着 Architecture 已经不再只是“manager-worker vs debate vs shared memory”的模板比较，而开始进入 topology design / structure search 阶段。

综合仓库现有证据，Architecture 子方向内部又可细分为四类：

1. **固定工作流型**：预定义角色和顺序，强调稳定性与可控性。
2. **图/层级组织型**：通过图结构、树结构或层级控制提高扩展性。
3. **记忆与上下文型**：通过共享记忆、局部记忆、状态压缩缓解协作退化。
4. **动态结构型**：按任务或运行状态自适应改变 topology、角色关系或消息路由。

这条主线的重要含义是：Multi-Agent 的差异化优势，越来越不在于“人数更多”，而在于“结构更可设计”。

### 2.2 Coordination：从合作控制到任务分解与异质伙伴协同

Coordination 是传统 multi-agent 的核心命题，在 2024-2026 中并没有消失，而是分裂成两条路线。一条仍延续 MARL、Dec-POMDP、合作控制、路径规划、交通/机器人/资源分配等经典问题；另一条则进入 LLM-agent 任务分解、动态任务分配、零样本协作和人机协同。

ICML 2024-2025 的证据最能体现这个分裂。2024 部分出现 `Locally Interdependent Multi-Agent MDP`、`Sequential Asynchronous Action Coordination in Multi-Agent Systems`、`Open Ad Hoc Teamwork with Cooperative Game Theory` 等偏理论/控制的工作；2025 则出现 `Cross-environment Cooperation Enables Zero-shot Multi-agent Coordination`、`LLM-Assisted Semantically Diverse Teammate Generation for Efficient Multi-agent Coordination`、`Ad-Hoc Human-AI Coordination Challenge` 等更贴近开放环境与 agentic 协作的题目，见 `projects/multi-agent-survey/literature/icml-2024-2025.md`。

ICLR 2026 中，Coordination 又进一步与现实任务耦合，如 `ATLAS` 面向真实旅行规划，`CoLLMLight` 面向交通信号控制，`Multi-agent Coordination via Flow Matching`、`When Is Diversity Rewarded in Cooperative Multi-Agent Learning?` 等则延续方法论探索，见 `projects/multi-agent-survey/literature/iclr-2025-2026.md`。

当前证据表明，Coordination 至少可分成三种问题设定：

1. **封闭环境协作**：如 cooperative MARL、路径规划、交通控制。
2. **开放伙伴协作**：如 zero-shot coordination、ad hoc teamwork、human-AI teaming。
3. **复杂任务分解协作**：如 general-purpose LLM agents 在复杂任务中的任务拆解与协调执行。

其中第二类和第三类是近两年最值得关注的变化，因为它们直接触碰“什么时候值得用多智能体”的核心问题：只有当环境不封闭、伙伴不固定、任务可拆解且需要互补视角时，coordination 的难点才真正显性化。

### 2.3 Communication：从消息传递走向共享记忆、稀疏路由与拓扑设计

Communication 在老一代多智能体研究中常表现为 emergent communication 或带宽/消息机制设计；在当前样本里，它的形态明显丰富了。仓库中现有论文表明，communication 已经至少包含四类机制：

1. **显式消息传递**：如 debate、轮次对话、多级通信。
2. **共享记忆/外部状态**：如 shared memory、memory masking、dual latent memory。
3. **语义压缩与高效通信**：如 token 压缩、KV sharing、economical communication pipeline。
4. **拓扑与路由设计**：如 GoAgent、指数拓扑、图结构协作。

NeurIPS 2024 候选池中已有 `Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication`、`Multi-Agent Coordination via Multi-Level Communication`、`Bridging semantics and pragmatics in information-theoretic emergent communication` 等工作，说明 communication 仍有扎实的传统理论根基，见 `projects/multi-agent-survey/literature/neurips-2024-2025.md`。但到了 ICLR 2025-2026，通信问题越来越像系统设计问题：`Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems`、`Cache-to-Cache: Direct Semantic Communication Between Large Language Models`、`KVComm: Enabling Efficient LLM Communication through Selective KV Sharing`、`Benefits and Limitations of Communication in Multi-Agent Reasoning` 等题目直接把通信效率与 reasoning quality 绑定起来，见 `projects/multi-agent-survey/literature/iclr-2025-2026.md`。

值得强调的是，当前仓库 synthesis 已经指出：在最近三个月的 arXiv 样本中，Communication 并不是最独立、最主导的论文簇，而更多嵌在 Architecture 和 Coordination 里，见 `projects/multi-agent-survey/logs/2026-03-23T16:40:00Z-arxiv-subdirection-synthesis.md`。这说明通信不再被视为单独模块，而被当作系统结构的一部分来共同优化。

### 2.4 Evaluation：从单一成功率走向多维 benchmark、human-AI coordination 与系统性失败分析

Evaluation 是当前仓库里最成熟、也最能支撑综述结论的类别之一，因为已经完成了 load-bearing 论文筛选与 literature notes。`projects/multi-agent-survey/literature/load-bearing-evaluation-application.md` 明确列出了 8 篇当前仓库认定的 Evaluation/Application 类 load-bearing papers，其中 5 篇评价导向、3 篇应用导向。

基于已完成的 literature notes，当前 evaluation 方向至少出现四种新的评估范式：

1. **真实环境 benchmark**：如 `Windows Agent Arena`，强调真实 OS 任务、planning + perception + tool use 的联合测评。其 literature note 记录：150+ 任务，全量评估可并行到 20 分钟，最佳模型成功率 19.5%，人类 74.5%，见 `projects/multi-agent-survey/literature/windows-agent-arena-note.md`。
2. **多维能力 benchmark**：如 `OmniBench`，强调 controllable complexity、graph-structured task synthesis 与多维指标；该 note 记录其包含 36k 任务、20 个场景、91% human acceptance，见 `projects/multi-agent-survey/literature/omnibench-note.md`。
3. **人机协同 benchmark**：如 `Ad-Hoc Human-AI Coordination Challenge`，用 proxy agents 替代昂贵且不可复现的人类评估，其 note 记录公开了 3,079 局游戏数据，见 `projects/multi-agent-survey/literature/ad-hoc-human-ai-coordination-challenge-note.md`。
4. **系统性失败/安全 stress test**：如 `Agent Smith`，指出单个 agent 被 jailbreak 后， harmful behavior 可以在最多一百万个 multimodal agents 中指数传播，见 `projects/multi-agent-survey/literature/agent-smith-note.md`。

此外，ICLR 2026 文献列表中已经出现多篇明确 benchmark/evaluation 指向论文，如 `A2ASecBench`、`Benchmarking Multi-Agent Reinforcement Learning in Power Grid Operations`、`LiveResearchBench`、`Measuring Bias Amplification in Multi-Agent Systems with Large Language Models` 等，见 `projects/multi-agent-survey/literature/iclr-2025-2026.md`。这意味着项目 README 里关于“ICLR 2026 是否有新的 multi-agent evaluation benchmark 工作”的开放问题，至少在仓库内部已经可以给出更强的 provisional answer：**有，而且不止一篇，问题已经从“是否存在”转移到“哪些属于真正 load-bearing”**。

### 2.5 Application：从 demo 场景扩展到高风险决策、科学工作流与真实系统控制

Application 类研究在当前样本中的变化也很明显：2024 年时它更多像“LLM multi-agent 能否做某事”的 demonstration；到 2026 年初，已经出现更强的 domain-specific workflow claims。

仓库中已完成 note 的代表论文包括：

- `MDAgents`：面向医疗决策，强调高风险场景中的 adaptive collaboration，见 `projects/multi-agent-survey/literature/mdagents-note.md`。
- `AI Agents Can Already Autonomously Perform Experimental High Energy Physics`：声称 agent 系统已能在较少专家干预下执行 HEP 分析流程的重要部分，见 `projects/multi-agent-survey/literature/ai-agents-hep-note.md`。
- `DIG to Heal`：面向一般用途 agent collaboration 的可解释动态决策路径，其 survey 价值在于连接系统扩展性与真实可用性，见 `projects/multi-agent-survey/literature/dig-to-heal-note.md`。

与此同时，ICLR 2026 列表还出现了旅行规划、单细胞分析、GUI 数据挖掘、化学反应条件推理、教育可视化、抗菌肽设计等领域应用，说明 application frontier 正从“单一 demo 任务”升级为“复杂工作流自动化”。

### 2.6 Theory：理论工作没有消失，而是在重新定义多智能体的可解释边界

Theory 在当前仓库里相对不如 Architecture/Evaluation 显眼，但并不弱。尤其在 NeurIPS 2024 与 ICML 2024-2025 中，仍能看到大量 cooperative MARL、causal effect propagation、social welfare、robustness、distribution shift、fairness、game-theoretic coordination 的工作，见 `projects/multi-agent-survey/literature/neurips-2024-2025.md` 与 `projects/multi-agent-survey/literature/icml-2024-2025.md`。

不过，理论工作的角色已经发生变化：它不再是整个 Multi-Agent 领域的唯一主轴，而是成为三个问题的支撑层：

1. 为什么某些 coordination/communication 机制有效？
2. 多智能体是否真的带来能力增益，而非只是额外 compute 和 prompt engineering？
3. 在 robustness、安全性、偏差传播与协作失效方面，能否建立更一般的解释框架？

例如 `Agentic Collaboration as an Information Bottleneck Problem`、`Benefits and Limitations of Communication in Multi-Agent Reasoning`、`MARS`、`SPIRAL` 等 ICLR 2026 题目，就表明理论问题正在向 agentic reasoning 的上层机制迁移。

## 3. 关键发现

结合当前仓库证据，本综述初稿提出六条关键发现。

### 3.1 关键发现一：2024-2026 的研究重心已经从“多智能体是否可行”转向“多智能体如何组织才有用”

这几乎是当前样本最稳的结论。顶会与 arXiv 中大量题目把焦点放在 framework、graph、topology、memory、runtime efficiency、token budgeting、dynamic decision path，而不是单纯宣称“多个 agents 比一个更强”。这一结论的核心证据来自 ICLR 2025-2026 论文题目分布与 arXiv subdirection synthesis，见 `projects/multi-agent-survey/literature/iclr-2025-2026.md` 与 `projects/multi-agent-survey/logs/2026-03-23T16:40:00Z-arxiv-subdirection-synthesis.md`。

换句话说，Multi-Agent 已从“人数扩增”问题进入“组织设计”问题。

### 3.2 关键发现二：Evaluation 正在变成决定领域成熟度的关键瓶颈

当前最有分量的 load-bearing notes 多数落在 Evaluation/Application 侧，这本身就是一个信号：相比继续提出更多协作框架，社区越来越需要证明这些框架在什么任务上真的有效、何时失效、成本是否可接受、风险是否被放大。

`Windows Agent Arena` 给出的 19.5% vs 74.5% 人机差距，`OmniBench` 的多维任务图评估，`AH2AC2` 的人机协作替身评估，`Agent Smith` 的系统性失败传播分析，都说明 evaluation 已经从 leaderboard 扩展成 deployment science。相关证据见各自 literature notes。

### 3.3 关键发现三：Multi-Agent 相对 Single-Agent + tools 的优势不是默认存在，而是高度条件化

仓库现有 synthesis 已明确指出，当前没有直接 head-to-head benchmark 在完全匹配工具、记忆、token budget 条件下比较两者，但已有证据支持一个保守规则：**默认优先 single-agent + tools；只有当任务的难点是角色分工、分布式视角、零样本协作、故障隔离、共享记忆或通信拓扑时，multi-agent 才更可能值得使用**，见 `projects/multi-agent-survey/logs/2026-03-23T170500Z-single-vs-multi-agent-boundary-synthesis.md`。

这一结论之所以重要，是因为它反驳了 2024 年大量 agent 框架工作中隐含的“多 agent 总是更强”的叙事。仓库中的反例证据包括：`Dual Latent Memory for Visual Multi-agent System` 报告增加 agent turn 可能造成 scaling wall；而支持多智能体必要性的证据则来自 `ZSC-Eval`、`Ad-Hoc Human-AI Coordination Challenge`、`GoAgent` 等，说明当 coordination/topology 本身是任务难点时，多智能体确实有独立价值。

### 3.4 关键发现四：2026 年的前沿变化之一是 communication topology 成为显式设计对象

`GoAgent` 是当前仓库中最鲜明的信号，它提示 2026 年的一个新趋势：通信结构本身不再是背景变量，而是方法对象，见 `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md`。这使得 communication 从“消息协议”升级为“信息路由架构”，也使 architecture 与 communication 更难分离。

这条趋势如果继续发展，会使 Multi-Agent 的真正增益更接近“信息流结构优化”，而不是“多个 agent 并行投票”。

### 3.5 关键发现五：MARL 没有被 LLM-agent 取代，而是在与 agent systems 融合

一个常见误解是：LLM-based multi-agent 爆发后，MARL 已经边缘化。当前仓库证据并不支持这个说法。相反，在 ICML、ICLR 与 arXiv 2026 样本里，MARL 仍然是大体量来源，但它正在向两个方向融合：

1. 与 LLM collaboration 融合，如 actor-critic fine-tuning、多 agent reasoning、self-play 驱动的 reasoning。
2. 与 evaluation/application 融合，如交通、机器人、资源系统、科学流程等现实控制场景。

也就是说，MARL 不再独立主导叙事，但仍构成 multi-agent 方法论的重要基础层。

### 3.6 关键发现六：风险、偏差与失败传播正在成为 multi-agent 的一等问题

`Agent Smith` 是最典型证据，但 ICLR 2026 列表中还出现了 rapport bias、bias amplification、misinformation rectification、control-flow hijacking、security benchmark 等题目。这说明随着 multi-agent 系统从 academic toy setup 走向真实部署，研究问题已经从“能力提升多少”扩展到“风险会不会同步放大”。

这也是为什么 future survey 不应再把安全与评估放在附录里，而应作为主线之一。

## 4. 趋势分析：2024 → 2026 的变化

### 4.1 从 MARL/theory-heavy 到 agentic systems-heavy

ICML 2024-2025 的 quick takeaways 已明确指出：2024 更偏 MARL theory 与 coordination structure，2025 则明显增加 LLM-agent system 与 benchmark work，见 `projects/multi-agent-survey/literature/icml-2024-2025.md`。NeurIPS 2024 候选池同样呈现“传统 MARL + 新兴 LLM agent/application”混合态。到 ICLR 2026 与最近 arXiv，architecture/orchestration 已成为最强子方向。

因此，2024 → 2026 的主变化不是简单的主题替换，而是研究层级上移：从底层策略学习，逐步上移到协作结构、运行时组织、任务分解、评估基准与系统安全。

### 4.2 从固定角色设计到动态协作路径

早期 LLM multi-agent 系统常依赖固定角色分工：planner、critic、executor、reviewer。当前样本则出现明显升级：不仅角色可动态变化，连通信路径、拓扑结构和 memory usage 都在被优化。`DIG to Heal` 的 dynamic decision paths 与 `GoAgent` 的 topology generation 是最明显信号。

这意味着 2026 年前沿开始回答一个更困难的问题：不是“给定工作流能否做任务”，而是“系统能否自己找到更好的工作流”。

### 4.3 从平均成功率到多维能力与失效模式评估

Benchmark 的转向也非常清晰。以前常见评估是单任务成功率或 reward；现在越来越多 benchmark 明确追踪：

- 环境真实性：OS、真实工作流、真实应用域；
- 能力维度：planning、screen understanding、tool use、subtask graph execution；
- 伙伴泛化：zero-shot coordination、human proxy partner；
- 失败传播：jailbreak contagion、bias amplification、misremembering collectively。

这反映出 community 已经认识到，多智能体系统的真实问题不是单点性能，而是系统行为。

### 4.4 从“多 agent 提升能力”到“多 agent 是否值得其额外开销”

最近的论文标题中频繁出现 efficiency、runtime、compression、token、economical communication、selective KV sharing 等词。说明研究重心不再只关心上界性能，而开始关心 coordination overhead 是否值得。这个趋势与仓库的边界 synthesis 一致：multi-agent 不该是默认配置，而应在明确收益场景下使用。

### 4.5 2026 arXiv 的增量主要来自 architecture + evaluation，而非纯 communication

根据 arXiv harvest summary，32 篇选中论文中 Architecture = 28、Evaluation = 21、Coordination = 14、Communication = 8，见 `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`。这说明近期新增工作更多是在“系统结构 + 评估/应用”方向上堆积，而非只做通信协议细化。换句话说，领域正在朝“完整 agent system engineering”而不是“单点协作模块优化”演进。

## 5. 未来方向

基于当前仓库证据，未来最值得关注的方向至少有五条。

### 5.1 边界研究：何时 multi-agent 真正优于 single-agent + tools

这是当前项目 README 中最重要的开放问题之一。现有证据足以支持 operational heuristic，但不足以支持严格经验定律。未来最需要的是：

1. 在相同工具、相同上下文窗口、相同 token/latency 预算下做 head-to-head 比较；
2. 对 multi-agent 系统做 collapse ablation：把多角色压缩成单 agent 看性能变化；
3. 把任务分成可分解/不可分解、单视角/多视角、稳定环境/开放环境等类型，找到 multi-agent 的收益边界。

如果没有这类研究，许多 multi-agent 系统论文仍然难以判断其“必要性”而非“可行性”。

### 5.2 结构学习：从 workflow engineering 到 topology learning

`GoAgent` 所指向的 topology generation 很可能只是开始。下一阶段真正有价值的工作，不会停留在手工画 graph，而会学习：

- 哪些角色需要通信；
- 哪些通信是冗余的；
- 何时共享 memory、何时局部保留；
- 何时应当退化回单 agent；
- 何时需要引入审计者、裁决者或安全监控 agent。

这将让 multi-agent 研究更接近自适应分布式系统，而不仅是 prompt workflow。

### 5.3 Evaluation 2.0：从 benchmark 走向 deployment-grade evaluation

当前 benchmark 虽已明显进步，但仍有缺口。未来 evaluation 应更多覆盖：

1. 成本维度：token、latency、并行资源、人工监督量；
2. 稳定性维度：不同运行随机种子、不同伙伴、不同环境扰动下的方差；
3. 安全维度：失败传播、偏差放大、误记忆、control flow hijacking；
4. 人机协作维度：人是否理解、信任、纠正 multi-agent 的行为；
5. 生命周期维度：系统是否会随着长期使用而 drift 或自我污染。

换句话说，未来 benchmark 不应只问“能不能完成任务”，而应问“能否可负担、可解释、可治理地完成任务”。

### 5.4 领域应用：科学研究、医疗、工业控制等高价值工作流

`MDAgents` 与 `AI Agents Can Already Autonomously Perform Experimental High Energy Physics` 都提示：真正能证明 multi-agent 价值的，往往不是聊天对话 benchmark，而是高价值工作流。未来值得重点跟踪的领域包括：

- 科学研究自动化；
- 医疗决策支持；
- 复杂软件工程与 computer-use；
- 交通/电网/机器人等多主体控制；
- 安全与风险管理。

这些场景共同特征是：任务复杂、环节异质、工具密集、需要可审计的分工。这正是 multi-agent 可能产生真实增益的区域。

### 5.5 安全与治理：多智能体系统的风险不会线性增长，而可能级联放大

`Agent Smith` 已经说明风险传播是级联的，不是线性的。未来治理研究需要回答：

- 什么拓扑最易传播错误和攻击？
- 如何把安全隔离做进协作结构？
- 共享记忆与消息传递谁更容易造成系统性污染？
- 是否可以设计可验证的 fail-stop / quarantine 机制？
- 多 agent 的监督责任如何分配给人类？

如果这条线缺位，multi-agent 在现实世界的扩张会明显受限。

## 6. 结论

综合当前仓库中的顶会清单、arXiv 趋势、load-bearing literature notes 与 session syntheses，可以给出一个相对稳健的阶段性结论：

2024-2026 的 Multi-Agent 研究，正在从传统 MARL 与静态多角色协作框架，转向以 **系统组织、动态结构、真实评估、复杂工作流应用与系统性风险控制** 为核心的新阶段。Architecture/orchestration 已成为最强主轴；Evaluation 不再是配角，而成为决定工作是否真正“站得住”的关键；Application 则开始进入高价值、高风险领域。与此同时，Single-Agent + tools 仍应是多数任务的默认基线，多智能体只有在任务本身具有可分解性、异质信息源、协作不确定性、故障隔离需求或信息流结构优化空间时，才更可能展示独立价值。

因此，下一阶段最值得做的，不是继续堆叠更多 workflow 花样，而是建立更严格的 comparative evaluation：到底什么任务需要多智能体、什么任务不需要；什么结构真的减少了 coordination overhead，什么结构只是增加了 token 消耗；什么 benchmark 能真正解释系统行为，而不只是给出新的排行榜。这些问题一旦被更系统地回答，Multi-Agent 才会从一个“很热的方向”变成一个“有清晰边界和成熟方法论的方向”。

## 7. 局限性说明

本稿是综述初稿，不是最终版，限制主要有三点：

1. NeurIPS 2025 当前仍未在仓库内补齐，见 `projects/multi-agent-survey/TASKS.md` 与 `projects/multi-agent-survey/literature/neurips-2024-2025.md`。
2. ICLR 2024-2026 的正式“全面盘点”任务在 `TASKS.md` 仍标记为 blocked，但仓库内已经有 2025-2026 的大规模可验证清单，因此本稿对 ICLR 2026 的趋势判断是强的，对 ICLR 2024 的覆盖判断是弱的。
3. Architecture、Coordination & Communication 两个 bucket 的 load-bearing 深读尚未完成，因此本稿在这些部分更多依赖 title-screened inventory 与已有 synthesis，而不是逐篇深入 literature note。

尽管如此，基于仓库内现有证据，本稿已足以作为最终综述的第一版结构骨架。