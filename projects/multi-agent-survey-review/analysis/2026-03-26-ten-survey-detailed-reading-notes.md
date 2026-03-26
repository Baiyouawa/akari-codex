# 2026-03-26 十篇 multi-agent 综述逐篇详读笔记（统一锁定样本集）

## 样本集声明
本文件**只**覆盖以下两份基线文件共同锁定的 10 篇论文：
1. `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`
2. `projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json`

为避免继承旧版污染输入，本文不纳入任何未出现在上述 manifest 中的论文。每篇条目的标题、年份、来源链接与本地 PDF 路径均以 manifest 为准；内容提炼主要来自以下仓库内证据：
- `projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-cross-comparison.md`
- `projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-background-problem-framework-notes.md`
- `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`
- `projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json`

证据边界说明：本文件以摘要级、章节级与既有结构化笔记级证据为主；未强行给出逐页页码断言。凡不能稳定追溯到上述文件的细节，均不写入。

---

## 1. Li et al. 2024
- Paper ID：`10.1007/s44336-024-00009-2`
- 标题：*A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges*
- 年份：2024
- 来源：https://link.springer.com/article/10.1007/s44336-024-00009-2
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf`

### 研究问题
LLM-based multi-agent systems 的标准工作流由哪些环节组成，这些环节如何支撑 problem-solving 与 world simulation，并在基础设施与挑战层面提出了哪些共性问题。

### 分类框架
以 workflow 为主轴，分为 profile、perception、self-action、mutual interaction、evolution 五段。

### 核心观点
- multi-agent 的关键增益在于角色设定、交互和演化形成闭环。
- workflow 比单纯按应用分类更适合做统一系统抽象。
- problem-solving 与 world simulation 是最典型的两大应用落点。

### 方法谱系
从角色/profile 定义，到 perception、self-action、mutual interaction，再到 evolution，体现出从单 agent 能力到多 agent 系统流水线的组织方式。

### 评测设定
以系统案例和 benchmark 汇总为主，偏向通用任务质量与系统组件完整性比较；统一多智能体评测协议仍较弱。

### 局限性
- 时间较早，尚未覆盖后续 communication-centric、workflow optimization 等专题化进展。
- workflow 抽象很强，但组件内部方法粒度不完全统一。

### 值得精读章节
- workflow 五段主框架章节
- 挑战与基础设施相关章节
- problem-solving / world simulation 对照部分

### 关键图表
- LLM-MAS 工作流总览图
- 应用与挑战汇总表

### 证据来源与边界
主要依据 selection 文件对入选理由的描述、cross-comparison 中 S1 条目、background-notes 中 Li 2024 的八字段提炼，以及 manifest 中题目/年份/路径校验。

---

## 2. Guo et al. 2024
- Paper ID：`2402.01680`
- 标题：*Large Language Model based Multi-Agents: A Survey of Progress and Challenges*
- 年份：2024
- 来源：https://arxiv.org/abs/2402.01680
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf`

### 研究问题
LLM-based multi-agents 已在何种环境与任务中使用，agent 的 profiling、communication 与 capability growth 机制如何组织，以及这些系统面临哪些共性挑战。

### 分类框架
按系统剖析、应用、实现工具与资源三层组织：interface / profiling / communication / capability acquisition → problem solving / world simulation → tools/resources。

### 核心观点
- 多智能体收益来自 specialization + interaction，而不是简单投票。
- communication 与 capability acquisition 是从单 agent 走向多 agent 的关键差异。
- world simulation 是 2024 时点的重要应用方向。

### 方法谱系
从系统模块拆解切入，再延伸至应用和资源，形成“组件—应用—资源”式总览谱系。

### 评测设定
既有仓库笔记记录其覆盖 GSM8K、HumanEval、MMLU、BIG-bench、ChatArena、RoCoBench、CAMEL、AvalonBench 等，说明其评测横跨推理、代码、对话与交互。

### 局限性
- benchmark 口径杂糅，更多是汇总而非统一评测协议。
- 对后续专题化方向的纵深讨论不足。

### 值得精读章节
- `Dissecting LLM-MA Systems`
- `Applications`
- `Implementation Tools and Resources`

### 关键图表
- 系统组件总图
- 应用版图/资源汇总表

### 证据来源与边界
主要依据 selection 文件、cross-comparison 中 S2、background-notes 中 Guo 2024 条目；benchmark 名录来自仓库既有笔记，不额外扩大到仓库外来源。

---

## 3. Zhu et al. 2024
- Paper ID：`10.1007/s10458-023-09633-6`
- 标题：*A survey of multi-agent deep reinforcement learning with communication*
- 年份：2024
- 来源：https://dblp.org/rec/journals/aamas/ZhuDW24
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2024-zhu-et-al-a-survey-of-multi-agent-deep-reinforcement-learning-with-communication-doi-10.1007-s10458-023-09633-6.pdf`

### 研究问题
在 MARL 中，communication 如何缓解 partial observability 与 non-stationarity；已有 Comm-MADRL 方法应如何被系统分类与比较。

### 分类框架
以 communication 的多维分析空间为核心，摘要明确给出 9 个维度；仓库内已有对其主要维度的概括包括 communication constraints、communicatee type、communication policy、communicated messages、message combination 等。

### 核心观点
- communication 是 MADRL 中的关键机制，而非边缘增强项。
- 最重要的不只是“能不能通信”，而是“传给谁、传什么、在何种约束下学”。
- 多维分类比单轴 taxonomy 更适合发现组合空白。

### 方法谱系
从预定义通信机制，发展到可学习 communication policy，再细分通信对象、消息内容、约束和训练方式，形成传统多智能体通信的基础谱系。

### 评测设定
以 MARL 环境和协同决策任务为主；仓库内 cross-comparison 明确将其归到 communication 与 decision-method 双重基线，常见环境包括 MPE、predator-prey、StarCraft II 一类可控多主体环境。

### 局限性
- 不直接面向 LLM-based natural language agents。
- 对开放式文本协作、角色交互和工具调用的覆盖有限。

### 值得精读章节
- 背景与通信问题定义部分
- 9 维通信分类框架部分
- future Comm-MADRL system 展望部分

### 关键图表
- Comm-MADRL 多维分类图
- 方法维度组合总结表

### 证据来源与边界
主要依据 selection 文件对其“传统 MARL 通信补位”定位、cross-comparison 中 S3、background-notes 中 Zhu 2024 条目；环境举例保持在仓库内已出现的名称范围内。

---

## 4. Chen et al. 2025
- Paper ID：`2412.17481`
- 标题：*A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application*
- 年份：2025
- 来源：https://arxiv.org/abs/2412.17481
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf`

### 研究问题
LLM-MAS 的最新扩张主要体现在哪些应用前沿，尤其是复杂任务求解、特定场景模拟与 generative agent evaluation 这三条主线如何共同重构领域版图。

### 分类框架
以三类应用目的为主轴：solving complex tasks、simulating specific scenarios、evaluating generative agents；并辅以 core components 与 challenges/future。

### 核心观点
- 应用目的比单纯系统模块更能解释新论文的增长方向。
- generative agents 正从执行者变成评测对象与评测主体。
- 新应用前沿正在反向塑造框架和评测方式。

### 方法谱系
从 core components 出发，沿三类应用主线展开，再汇总 challenges 与 future directions，体现“组件—应用—评测”式组织。

### 评测设定
仓库内已有笔记记录其涉及 AgentBench、AUCArena、EvalPlus、GSM8K、HotpotQA、HumanEval、MATH、MMLU、MT-Bench、MLAgentBench、ToolBench、ChatEval 等，反映出其正处于通用 benchmark 向 agent-specific benchmark 过渡的阶段。

### 局限性
- 对 communication、workflow 等底层专题不如专项综述深入。
- 篇幅限制导致细粒度技术讨论有限。

### 值得精读章节
- 三类应用前沿主章节
- evaluation / resources 相关章节
- challenges and future directions

### 关键图表
- 应用三分法总图
- benchmark / resources 汇总表

### 证据来源与边界
主要依据 selection 文件、cross-comparison 中 S4、background-notes 中 Chen 2412.17481 条目；benchmark 名录不超出仓库既有记录。

---

## 5. Tran et al. 2025
- Paper ID：`2501.06322`
- 标题：*Multi-Agent Collaboration Mechanisms: A Survey of LLMs*
- 年份：2025
- 来源：https://arxiv.org/abs/2501.06322
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf`

### 研究问题
LLM-based multi-agent collaboration 到底由哪些关键维度组成，不同协作关系、结构与协调协议如何影响 collective intelligence。

### 分类框架
按 actors、types（cooperation / competition / coopetition）、structures、strategies、coordination protocols 组织，是当前样本集中协作 taxonomy 最完整的论文之一。

### 核心观点
- 多智能体研究应从 isolated models 转向 collaboration-centric designs。
- cooperation、competition、coopetition 都是重要组织关系。
- protocol 是把 actor、structure 和 strategy 串联起来的关键抽象层。

### 方法谱系
先定义 collaboration concept，再按协作类型、组织结构、策略与协议逐层展开，属于典型“组织机制”视角的谱系。

### 评测设定
更强调协作效果和结构差异在真实任务中的表现；仓库内已有记录点名 LLMArena、CAMEL、AutoGen 等系统与场景线索，但该文重点在协作机制比较，不是单独构建 benchmark 目录。

### 局限性
- memory、tool-use、workflow engineering 不是主轴。
- benchmark 更像协作案例的比较背景，而不是统一实验协议。

### 值得精读章节
- collaboration concept / problem definition
- collaboration types
- coordination and orchestration 相关部分

### 关键图表
- collaboration taxonomy 总图
- relation / structure / protocol 对照表

### 证据来源与边界
主要依据 selection 文件对其入选理由、cross-comparison 中 S5、background-notes 中 Tran 2025 条目；未超出仓库内已落库的案例名。

---

## 6. Yan et al. 2025
- Paper ID：`2502.14321`
- 标题：*Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems*
- 年份：2025
- 来源：https://arxiv.org/abs/2502.14321
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf`

### 研究问题
在 LLM-MAS 中，communication 由哪些层面组成，system-level 与 system-internal communication 如何共同决定系统能力，并在哪些效率、安全与扩展性问题上暴露短板。

### 分类框架
双层框架：
- system-level communication：architecture、goals、protocols
- system-internal communication：strategies、paradigms、objects、content

### 核心观点
- communication 是系统能力变量，不是 prompt 小技巧。
- 研究 communication 时必须同时看“为什么说、怎么说、说什么”。
- efficiency、security、benchmarking、scalability 需要一起审视。

### 方法谱系
从外层 architecture / goal / protocol 出发，再进入 strategy / paradigm / object / content 的内层通信机制，最后落到 benchmark 和风险。

### 评测设定
仓库内已有记录显示其讨论 GAMA-Bench、MultiAgentBench、RealWorldBench 等通信相关评测；更重要的是它强调现有 benchmarks 在覆盖场景、异构域与 agent population scale 上仍有不足。

### 局限性
- 为突出通信，弱化了 memory、tool-use、workflow graph 等其他变量。
- 多模态通信和工业部署仍处于较早阶段。

### 值得精读章节
- Communication Architecture
- Communication Protocol
- Benchmarks & Evaluation

### 关键图表
- communication taxonomy 总图
- benchmark 与效率/风险对照表

### 证据来源与边界
主要依据 selection 文件、cross-comparison 中 S6、background-notes 中 Yan 2025 条目；benchmark 仅使用仓库已出现的名字与族群判断。

---

## 7. Wu et al. 2025
- Paper ID：`2502.16804`
- 标题：*Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances*
- 年份：2025
- 来源：https://arxiv.org/abs/2502.16804
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf`

### 研究问题
单 agent 自动驾驶系统在感知、协作和计算代价上存在明显瓶颈；多 agent + LLM 能否通过车-车、车-路、车-助手与 agent-human 协作缓解这些问题。

### 分类框架
以交互对象与协作任务为核心：multi-vehicle、vehicle-infrastructure、vehicle-assistant、agent-human；并延伸到 collaborative perception、collaborative decision-making、cloud-edge deployment、assistance tools。

### 核心观点
- 多智能体在自动驾驶中的价值首先体现在分布式视角整合与语义协调。
- LLM 更像高层协调与决策层，不是简单替代底层控制器。
- 自动驾驶是高风险真实场景中检验 multi-agent 价值的重要方向。

### 方法谱系
从 single-agent ADS 回顾切入，再转向 multi-agent ADS 架构与交互模式，最后连接应用、数据集与挑战。

### 评测设定
以自动驾驶专用 datasets / benchmarks 为主；仓库内已有记录点名 INTERACTION、Waymo Open Motion Dataset 等，突出实时性、安全性与多车协同约束。

### 局限性
- 垂直领域特性强，结论不一定可直接迁移到通用 MAS。
- 高风险场景使复现实验与评测门槛高。

### 值得精读章节
- LLM-based Multi-Agent Interaction
- Applications
- Datasets and Benchmark
- Challenges and Future Directions

### 关键图表
- 多交互对象自动驾驶架构图
- 自动驾驶数据集/benchmark 汇总表

### 证据来源与边界
主要依据 selection 文件、cross-comparison 中 S7、background-notes 中 Wu 2025 条目；数据集名称保持在仓库已有提及范围内。

---

## 8. Jin et al. 2025
- Paper ID：`2503.13415`
- 标题：*A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives*
- 年份：2025
- 来源：https://arxiv.org/abs/2503.13415
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-misc-a-comprehensive-survey-on-multi-agent-cooperative-decision-making-scenarios-approaches-challenges-and-perspectives-arxiv-2503.13415.pdf`

### 研究问题
多 agent cooperative decision-making 在不同场景、任务形式、奖励机制和底层技术下如何被系统化梳理；传统方法与 MARL、LLM reasoning 方法如何比较。

### 分类框架
按场景/环境与方法双轴组织：
- 场景轴：simulation environments、task formats、reward allocation、underlying technologies
- 方法轴：rule-based、game theory-based、evolutionary algorithms-based、deep MARL-based、LLM reasoning-based

### 核心观点
- cooperative decision-making 不只是算法问题，也强依赖 environment 与 reward design。
- 传统 MAS 决策方法与新型 MARL/LLM 方法需要放在同一张谱系图里看。
- 真实复杂场景推动方法分类从单纯算法比较转向“算法 + 环境 + 协议”联合分析。

### 方法谱系
从规则和博弈方法，发展到进化算法，再到 deep MARL，最后纳入 LLM reasoning-based cooperative decision-making，形成一条传统 MAS 到 LLM-MAS 的桥接线。

### 评测设定
重点不在通用问答 benchmark，而在 simulation environments 与 cooperative tasks；仓库内已有记录提到 MPE、predator-prey、StarCraft II 等环境，体现其环境导向的评测风格。

### 局限性
- 覆盖面广，单个方法簇的纵深有限。
- LLM reasoning 部分因时间较新，细化程度可能弱于 MARL 部分。

### 值得精读章节
- 场景与 environment 总览部分
- 五类方法总述部分
- challenges and perspectives

### 关键图表
- cooperative decision-making 方法谱系图
- 场景 / 任务形式 / 奖励分配总结表

### 证据来源与边界
主要依据 selection 文件、cross-comparison 中 S8、background-notes 中 Jin 2025 条目；环境名仅沿用仓库内已出现的例子。

---

## 9. Lin et al. 2025
- Paper ID：`2505.21116`
- 标题：*Creativity in LLM-based Multi-Agent Systems: A Survey*
- 年份：2025
- 来源：https://arxiv.org/abs/2505.21116
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf`

### 研究问题
creative MAS 如何组织 agent proactivity、persona、generation techniques、datasets 与 evaluation，以系统提升文本和图像生成任务中的创造力。

### 分类框架
围绕 workflow and proactivity、creative techniques（divergent exploration、iterative refinement、collaborative synthesis）、persona/profile、evaluation、datasets 展开。

### 核心观点
- creativity 是 MAS 的独立能力维度，不只是 infrastructure 的副产物。
- persona、proactivity 与 workflow integration 会直接影响创意结果。
- 当前最大短板在 evaluation inconsistency、bias mitigation、coordination conflict 和 lack of unified benchmarks。

### 方法谱系
从 workflow 与主动作业模式切入，扩展到多种创造性生成技术，再进入 persona/profile 设计，最后讨论 evaluation 与 dataset。

### 评测设定
以 creative task datasets 和多维评价为主；仓库内已有记录区分 psychological test datasets 与 task-specific datasets，并强调 objective、subjective、user study 混合评测。

### 局限性
- 与通用协作、通信、tool-use 问题的连接较弱。
- 主观评价比例高，横向可比性不足。

### 值得精读章节
- MAS Workflow and Proactivity
- MAS Techniques for Creativity
- Evaluation / Datasets
- Challenges and Future Work

### 关键图表
- creative MAS 工作流图
- evaluation taxonomy / datasets 汇总表

### 证据来源与边界
主要依据 selection 文件、cross-comparison 中 S9、background-notes 中 Lin 2025 条目；数据集与评价类别保持在仓库已落库的分类层级。

---

## 10. Chen et al. 2026
- Paper ID：`2602.11583`
- 标题：*The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs*
- 年份：2026
- 来源：https://arxiv.org/abs/2602.11583
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf`

### 研究问题
如何用 Who / Whom / When / What / Why 五个问题统一刻画 multi-agent communication，并把 MARL、emergent language、LLM-based communication 三条研究传统连接到同一框架中。

### 分类框架
Five Ws 是全文核心 taxonomy：
- Who
- Whom
- When
- What
- Why
同时按 MARL、emergent language、LLM-based communication 三大范式组织正文。

### 核心观点
- Five Ws 提供了跨范式的最小统一语言。
- MARL、EL、LLM 三条路线不是割裂的，而是连续演化的通信研究谱系。
- communication 的关键不只是是否存在，而是主体、对象、时机、内容与动机的联合设计。

### 方法谱系
采用“历史演化 + 统一框架”双线：先回顾 communication as action 的理论基础，再按三大范式重组，最终落到 Five Ws 统一分析和 future directions。

### 评测设定
仓库内已有记录显示其涉及 AvalonBench、BattleAgentBench、ChatEval、GAIA、MultiAgentBench、RoCoBench、CAMEL 等；其重点是 communication evaluation 的跨范式可比性，而非单一任务分数。

### 局限性
- 主题高度聚焦通信，不是通用 multi-agent 全景综述。
- 工程运行时、成本治理等维度需要和其他综述互补阅读。

### 值得精读章节
- Methodology and Scope
- Five Ws 主体章节
- Discussion, Open Problems, and Future Directions

### 关键图表
- Five Ws 总框架图
- MARL / EL / LLM 三范式对照图

### 证据来源与边界
主要依据 selection 文件、cross-comparison 中 S10、background-notes 中 Chen 2026 条目；benchmark 仅采用仓库已出现的名称与分类。

---

## 横向小结

### 当前统一样本集覆盖面
- 通用 LLM-MAS 总览：Li 2024、Guo 2024、Chen 2025
- 通信/协作/决策：Zhu 2024、Tran 2025、Yan 2025、Jin 2025、Chen 2026
- 垂直与新兴应用：Wu 2025、Lin 2025

### 共性判断
- communication 是 10 篇样本中最强的交叉主题。
- 2024 年样本更偏通用框架，2025 年样本快速专题化，2026 年样本开始尝试统一理论。
- benchmark 仍明显碎片化：通用能力基准、协作交互基准、通信专项基准、垂直场景基准彼此尚未统一。

### 本文件与其他产物的分工
- 本文件：统一样本集下的逐篇详读笔记。
- `analysis/2026-03-26-ten-survey-background-problem-framework-notes.md`：突出研究背景/问题定义/未来方向八字段。
- `analysis/2026-03-26-ten-survey-cross-comparison.md`：横向比较、研究空白与统一分析框架。

### 一致性声明
经对照 `projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json`，本文覆盖的 10 篇论文分别为：
`10.1007/s44336-024-00009-2`、`2402.01680`、`10.1007/s10458-023-09633-6`、`2412.17481`、`2501.06322`、`2502.14321`、`2502.16804`、`2503.13415`、`2505.21116`、`2602.11583`。
未包含任何非锁定样本。