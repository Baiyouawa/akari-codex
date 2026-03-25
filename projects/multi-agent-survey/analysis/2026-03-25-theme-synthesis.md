# 2026-03-25 主题归类与横向综述（基于仓库内已恢复文献清单）

## Scope

本综述只基于当前仓库中可验证的三份文献清单进行横向归类，不补充任何仓库外检索结果：

- `projects/multi-agent-survey/literature/icml-2023-2025.md`
- `projects/multi-agent-survey/literature/iclr-2025-2026.md`
- `projects/multi-agent-survey/literature/neurips-2024-2025.md`

为保证可追溯性，本页的计数均由脚本 `projects/multi-agent-survey/scripts/classify_theme_synthesis.py` 从以上三份文件直接解析并按标题/标签规则归类得到。

## Data basis

脚本统计到的总条目数为 367，来自：

- ICML: 83 篇
- ICLR: 146 篇
- NeurIPS: 138 篇
- Inline arithmetic: `83 + 146 + 138 = 367`

Provenance: `cd projects/multi-agent-survey && python3 scripts/classify_theme_synthesis.py`

## Theme counts

同一篇论文可落入多个主题，因此下表为“主题命中数”而非互斥分桶。

| 主题 | 命中数 | 观察 |
| --- | ---: | --- |
| 协作规划 | 134 | 最稳定、覆盖面最广，贯穿传统 MARL 与 LLM agent 协作系统 |
| 通信 | 59 | 从显式 message passing 扩展到 debate、discussion、KV sharing、semantic communication |
| 博弈/对齐 | 45 | 以稳健性、对抗、均衡、偏好/价值对齐为主线 |
| 工具使用 | 14 | 规模仍小，但已出现 GUI、AutoML、软件开发、Text-to-SQL 等任务化系统 |
| 多智能体LLM系统 | 167 | 是当前最突出的交叉主线，已明显从“多个 agent”走向“系统工程” |
| 训练与评测 | 42 | 从 benchmark 扩展到 distillation、curriculum、failure attribution、security benchmark |

Provenance: `projects/multi-agent-survey/scripts/classify_theme_synthesis.py` 输出中的 `theme_counts`

## Venue distribution by theme

| 主题 | ICML | ICLR | NeurIPS |
| --- | ---: | ---: | ---: |
| 协作规划 | 16 | 57 | 61 |
| 通信 | 6 | 31 | 22 |
| 博弈/对齐 | 16 | 17 | 12 |
| 工具使用 | 2 | 8 | 4 |
| 多智能体LLM系统 | 54 | 70 | 43 |
| 训练与评测 | 6 | 20 | 16 |

Provenance: `projects/multi-agent-survey/scripts/classify_theme_synthesis.py` 输出中的 `venue_theme_counts`

## 研究脉络

### 1. 协作规划：从 MARL 协调机制走向任务级分工与规划

这一主线的底层起点仍然是 cooperative MARL。ICML 2023-2025 与 NeurIPS 2024 的不少工作都在解决 credit assignment、hierarchical coordination、trajectory generation、zero-shot coordination、pathfinding、option discovery 等问题，例如：

- `Context-Aware Bayesian Network Actor-Critic Methods for Cooperative Multi-Agent Reinforcement Learning`（ICML 2023）
- `Multi-Agent Reinforcement Learning with Hierarchical Coordination for Emergency Responder Stationing`（ICML 2024）
- `Cross-environment Cooperation Enables Zero-shot Multi-agent Coordination`（ICML 2025）
- `Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments`（NeurIPS 2024）
- `N-agent Ad Hoc Teamwork`（NeurIPS 2024）

到了 ICLR 2025-2026，这条线开始与 agentic planning 合流：

- `Agent-Oriented Planning in Multi-Agent Systems`
- `CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation`
- `ATLAS: Constraints-Aware Multi-Agent Collaboration for Real-World Travel Planning`
- `CoLLMLight: Cooperative Large Language Model Agents for Network-Wide Traffic Signal Control`

横向看，协作规划已经从“学出可配合策略”升级为“显式任务分解 + 规划器/世界模型 + 角色分工”。这意味着未来综述写作时，可以把协作规划拆成两层：

1. **策略级协调**：偏 MARL、强调联合策略与收敛；
2. **任务级规划**：偏 agent system、强调子任务分配、长程计划和工具/环境交互。

### 2. 通信：从 message passing 到 debate / discussion / semantic sharing

通信主题在当前仓库样本中共有 59 次命中。早期与 MARL 更紧密绑定，典型是：

- `Cooperative Multi-Agent Reinforcement Learning: Asynchronous Communication and Linear Function Approximation`（ICML 2023）
- `Multi-Agent Best Arm Identification with Private Communications`（ICML 2023）
- `Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication`（NeurIPS 2024）
- `Multi-Agent Coordination via Multi-Level Communication`（NeurIPS 2024）

但 2024-2026 的一个明显变化是：**通信不再仅仅是压缩/传输带宽问题，而被重写为“推理交换协议”问题**。代表样本包括：

- `Improving Factuality and Reasoning in Language Models through Multiagent Debate`（ICML 2024）
- `Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs`（ICML 2024）
- `From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium`（ICML 2025）
- `Benefits and Limitations of Communication in Multi-Agent Reasoning`（ICLR 2026）
- `Context Learning for Multi-Agent Discussion`（ICLR 2026）
- `KVComm: Enabling Efficient LLM Communication through Selective KV Sharing`（ICLR 2026）
- `Cache-to-Cache: Direct Semantic Communication Between Large Language Models`（ICLR 2026）

因此通信线索可以继续拆成三代：

1. **显式低维消息通信**：经典 MARL；
2. **语言通信/辩论通信**：多 LLM 通过自然语言交换中间推理；
3. **系统层语义通信**：KV sharing、cache sharing、information bottleneck，把通信对象从“文本消息”推进到“内部状态”。

### 3. 博弈/对齐：从稳健协作到社会偏差、价值一致与攻击防御

博弈/对齐共有 45 次命中，说明它不是最大分支，但已构成高影响“约束层”。

较早的工作偏向博弈论与均衡：

- `A Game-Theoretic Framework for Managing Risk in Multi-Agent Systems`（ICML 2023）
- `Oracles & Followers: Stackelberg Equilibria in Deep Multi-Agent Reinforcement Learning`（ICML 2023）
- `Convex Markov Games: A New Frontier for Multi-Agent Reinforcement Learning`（ICML 2025）

随后逐渐转向 robustness / adversary / alignment：

- `Breaking the Curse of Multiagency in Robust Multi-Agent Reinforcement Learning`（ICML 2025）
- `M$^3$HF: Multi-agent Reinforcement Learning from Multi-phase Human Feedback of Mixed Quality`（ICML 2025）
- `Aligning Individual and Collective Objectives in Multi-Agent Cooperation`（NeurIPS 2024）
- `Secret Collusion among AI Agents: Multi-Agent Deception via Steganography`（NeurIPS 2024）
- `Measuring Bias Amplification in Multi-Agent Systems with Large Language Models`（ICLR 2026）
- `Breaking and Fixing Defenses Against Control Flow Hijacking in Multi-Agent Systems`（ICLR 2026）

横向脉络很清晰：

- **第一阶段**：研究多智能体相互作用的均衡结构；
- **第二阶段**：研究对抗、攻击与鲁棒性；
- **第三阶段**：研究 LLM society 中的价值偏移、偏见放大、集体误记忆、控制流劫持等系统安全问题。

这说明在最终综述里，“对齐”不应仅写成人类偏好对齐，而应拓展为 **multi-agent interaction alignment**：即 agent-agent、agent-human、agent-tool 三种关系同时约束。

### 4. 工具使用：从纯推理协作转向可执行 agent workflow

工具使用命中数仅 14，绝对规模不大，但信号非常强，因为它对应的是多智能体系统从“讨论问题”变成“执行工作”。代表论文包括：

- `AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML`（ICML 2025）
- `ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL`（ICLR 2025）
- `Self-Evolving Multi-Agent Collaboration Networks for Software Development`（ICLR 2025）
- `CoAct-1: Computer-using Multi-agent System with Coding Actions`（ICLR 2026）
- `M$^2$-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining`（ICLR 2026）
- `ProRe: A Proactive Reward System for GUI Agents via Reasoner–Actor Collaboration`（ICLR 2026）
- `MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution`（NeurIPS 2024）
- `Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration`（NeurIPS 2024）

研究脉络上，这是一个重要转折：系统不再把 agent 视作“并行思考者”，而是视作“有接口、有角色、有行动后果”的 workflow node。这里天然衔接本项目最终要写的系统综述，因为它最接近生产级 agent orchestration。

### 5. 多智能体 LLM 系统：当前最强主线，且正在系统工程化

在 367 条可验证样本中，`多智能体LLM系统` 命中 167 次，是六个主题中最多的。这说明当前近两年顶会中的“multi-agent”热点，已经明显被 LLM 系统范式重塑。

代表样本包括：

- `Scaling Large Language Model-based Multi-Agent Collaboration`（ICLR 2025）
- `Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration`（ICLR 2026）
- `Unlocking the Power of Multi-Agent LLM for Reasoning: From Lazy Agents to Deliberation`（ICLR 2026）
- `MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference`（ICLR 2026）
- `MAS$^2$: Self-Generative, Self-Configuring, Self-Rectifying Multi-Agent Systems`（ICLR 2026）
- `MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines`（ICML 2025）
- `MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems`（ICML 2025）
- `On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents`（ICML 2025）
- `Reflective Multi-Agent Collaboration based on Large Language Models`（NeurIPS 2024）
- `FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making`（NeurIPS 2024）

横向来看，该主线又在分化为几类子问题：

1. **拓扑/组织设计**：Graph-of-Agents, G-Designer, Multi-Agent Design；
2. **自动构造/自配置**：MetaAgent, MAS$^2$, Multi-agent Architecture Search；
3. **推理增强**：debate, reflection, deliberation, self-play；
4. **系统稳定性**：faulty agents、misinformation、Mandela effect、failure attribution；
5. **场景落地**：AutoML、科研、软件开发、医学、金融、交通、单细胞分析等。

因此最终综述结构里，`多智能体LLM系统` 应作为中心章节，而不是附属章节。

### 6. 训练与评测：从 benchmark 不足转向“能不能稳定训练、可不可以可靠评估”

训练与评测主题命中 42 次，代表工作包括：

- `FightLadder: A Benchmark for Competitive Multi-Agent Reinforcement Learning`（ICML 2024）
- `MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems`（ICML 2025）
- `Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems`（ICML 2025）
- `A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems`（ICLR 2026）
- `LiveResearchBench: Benchmarking Single- and Multi-Agent Systems for Citation-Grounded Deep Research`（ICLR 2026）
- `Benchmarking Multi-Agent Reinforcement Learning in Power Grid Operations`（ICLR 2026）
- `SocialJax: An Evaluation Suite for Multi-agent Reinforcement Learning in Sequential Social Dilemmas`（ICLR 2026）
- `ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination`（NeurIPS 2024）

这一主题的变化也很明显：

- 早期 benchmark 更偏环境/任务定义；
- 现在 benchmark 已开始测 **安全性、归因、科研能力、工具使用、社会偏差**；
- 训练方法则从常规 RL/finetuning 扩展到 curriculum、distillation、post-training preference alignment、test-time scaling。

换言之，训练与评测不再只是 supporting section，而是决定多智能体系统能否被可信部署的关键层。

## 横向总结：当前研究的六条主线如何串联

基于当前仓库样本，可以把近三年 multi-agent 研究理解为以下演进链：

1. **MARL 基础层**：先解决协作、部分可观测、信用分配、收敛与稳健性；
2. **通信扩展层**：从离散消息传递走向自然语言 debate 与语义缓存共享；
3. **博弈/对齐约束层**：讨论均衡、鲁棒性、攻击、价值冲突和社会偏差；
4. **工具执行层**：agent 开始调用 GUI、代码、检索、规划器等外部接口；
5. **LLM 系统层**：多 agent 由“多个提示”演化为“可设计、可训练、可调度的系统”；
6. **训练与评测闭环层**：需要 benchmark、failure attribution、安全基准与系统级训练机制来支撑落地。

简言之，领域主线已经不是“multi-agent RL”单线扩展，而是：

> **从协作学习问题，演进为多智能体 LLM 系统工程问题。**

## 对最终综述写作的建议结构

结合本次分类结果，KDD 风格综述主干可以组织为：

1. **Foundations: Coordination, Planning, and MARL**
2. **Communication Protocols: Message Passing, Debate, and Semantic State Sharing**
3. **Games, Alignment, Robustness, and Safety**
4. **Tool-Using Multi-Agent Workflows**
5. **LLM-based Multi-Agent Systems: Topology, Role Design, Reflection, and Self-Configuration**
6. **Training, Evaluation, and Failure Analysis**

其中第 5 节应作为全文中心，前四节提供方法和问题来源，第 6 节负责落地与可信性闭环。

## Caveats

1. 本分类基于标题关键词与现有标签，属于高层主题归类，不等于精读后的最终 taxonomy。
2. `projects/multi-agent-survey/literature/iclr-2025-2026.md` 中条目未显式记录 `Year:` 字段，因此本次脚本无法为该文件生成逐年主题统计，但不影响 venue 级统计和主题脉络总结。
3. NeurIPS 清单本身是 candidate list，且仓库内仍缺 2023 与完善的 2025 元数据，因此当前横向综述是“基于仓库现有可验证证据的阶段性研究脉络”。
