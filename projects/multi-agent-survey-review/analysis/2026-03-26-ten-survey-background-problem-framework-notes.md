# 2026-03-26 十篇 multi-agent 综述详读提炼（研究背景 / 问题定义 / 分类框架 / 核心观点 / 方法脉络 / 数据集与 benchmark / 局限性 / 未来方向）

## 说明
- 本文件对应任务：`对 10 篇综述分别进行详读，提炼每篇的研究背景、问题定义、分类框架、核心观点、方法脉络、数据集/benchmark、局限性与未来方向`。
- 样本范围以 `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md` 的最终入选 10 篇为准。
- 证据来源包括：
  1. 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/*.pdf`
  2. 本地路径与页数校验：`projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-local-paths.md`
  3. 既有结构化精读：`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-detailed-reading-notes.md`
  4. 既有交叉比较：`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-cross-comparison.md`
- 为避免无依据扩写，本文件中的每条结论尽量绑定到可见的章节标题、摘要原句或既有已落库笔记；若仅能达到摘要级证据，会明确写明。

---

## 1. Li et al. 2024
### 论文
- 标题：*A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges*
- 来源：Springer / DOI `10.1007/s44336-024-00009-2`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf`
- 证据定位：摘要；`3 LLM-based multi-agent work`；`3.1 Agent profile`；`3.2 Perception`；`3.3 Self-action`；后续挑战章节（由摘要与标题可见）

### 研究背景
作者把目标放在“更智能、更可信、类人社会式自治系统”的长期追求上，认为 LLM 的推理与规划能力让 agent 从传统 RL 式窄能力主体升级为可在复杂环境中感知、决策、行动的通用主体，因此需要系统梳理 LLM-based MAS 的工作流与基础设施。

### 问题定义
论文要回答的核心问题是：LLM-based multi-agent systems 到底由哪些工作流组件组成，它们如何支持 problem-solving 与 world simulation 两类主应用，以及当前系统在工程与能力层面面临哪些挑战。

### 分类框架
作者采用严格的工作流式五段框架：
1. profile
2. perception
3. self-action
4. mutual interaction
5. evolution
这比按应用分类更偏系统设计视角，强调 agent 生命周期与系统运行链条。

### 核心观点
- 多智能体系统的核心增益不在“多个 LLM 同时输出”，而在 profile、interaction 与 evolution 形成的协作闭环。
- workflow 是统一已有 LLM-MAS 文献的最好主轴，因为不同系统虽然任务不同，但都落在相似的感知—行动—交互—演化管线中。
- 应用上，problem-solving 与 world simulation 是最典型的两大落点。

### 方法脉络
方法主线从单 agent 能力扩展到多 agent 协作工作流：
- 先定义角色与 profile；
- 再处理 perception 的消息来源与类型；
- 进入 self-action，如 memory、knowledge utilization；
- 再到 mutual interaction 的通信与协作；
- 最后以 evolution 讨论训练、反馈与系统持续改进。
这是一条明显的“系统流水线演化线”，不是按算法家族分的谱系。

### 数据集 / benchmark
从既有落库笔记与文中评测表述可追溯到，本综述覆盖的软件开发、具身环境、社会模拟等任务中，常见评测与资源包括 ChatDev、MetaGPT 一类系统案例，以及通用任务环境与数据集汇总表；文件中还显式存在 `Evaluation` 表格与 benchmark 汇总段落。该综述的特点是“案例与系统表较强、统一 benchmark 协议较弱”。

### 局限性
- 2024 年时点较早，对后续 communication protocol、workflow optimization、tool orchestration 的专题演化覆盖不足。
- 工作流框架虽统一，但不同步骤下的方法粒度差异较大，横向比较时仍需二次抽象。
- benchmark 仍偏案例汇编，尚未形成统一的 multi-agent 评测语言。

### 未来方向
结合摘要中的 challenges/future 表述，可归纳为：
- 更强的 agent evolution / feedback 学习机制；
- 更可靠的互操作基础设施；
- 更系统的 world simulation 与 problem-solving 评测；
- 对复杂协作、可扩展性与可信性的持续改进。

---

## 2. Guo et al. 2024
### 论文
- 标题：*Large Language Model based Multi-Agents: A Survey of Progress and Challenges*
- 来源：arXiv `2402.01680`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf`
- 证据定位：摘要；`3 Dissecting LLM-MA Systems`；`4 Applications`；`5 Implementation Tools and Resources`

### 研究背景
作者把 LLM-based multi-agent 放在单 LLM agent 成功之后的下一阶段：单 agent 已展现规划与决策能力，但复杂问题求解与世界模拟需要多主体分工、交流和专长互补，因此需要一个面向社区的系统综述。

### 问题定义
论文围绕三个问题组织：
- LLM-based multi-agents 在哪些环境和领域中被使用？
- agents 如何被 profile、如何 communication？
- 什么机制推动 agents capability growth？

### 分类框架
核心结构是“三层展开”：
1. 系统剖析：Agents-Environment Interface、Agents Profiling、Agents Communication、Agents Capabilities Acquisition
2. 应用：Problem Solving 与 World Simulation
3. 实现工具与资源：framework、dataset、benchmark

### 核心观点
- 多智能体的真实增量来自 specialization + interaction，而不是简单投票。
- communication 与 capability acquisition 是从单 agent 走向多 agent 的关键差异项。
- LLM-MA 的主应用已从任务求解扩展到社会、游戏、经济、心理等 world simulation。

### 方法脉络
其方法脉络是“从系统模块到应用扩张”：
- 先构造 interface 与 profiling；
- 再设计 communication；
- 再讨论能力增长与训练；
- 最后进入 problem-solving/world-simulation 应用。
因此这篇更像“总图式演化脉络”。

### 数据集 / benchmark
文中明确声称总结常见 datasets/benchmarks；既有精读记录列出 GSM8K、HumanEval、MMLU、BIG-bench、ChatArena、RoCoBench、CAMEL、AvalonBench 等。特点是覆盖推理、代码、对话、博弈与协作，但口径较杂，说明 2024 年阶段很多工作仍借用通用 benchmark。

### 局限性
- 时间较早，后续 2025-2026 的 communication-centric、workflow-centric 细分方向尚未展开。
- 虽有 benchmark 汇总，但多为资源罗列，尚难直接支持统一实验设计。
- world simulation 覆盖很广，分类深度不如后来的专题综述。

### 未来方向
从摘要与“Progress and Challenges”定位可归纳为：
- 更完善的 communication 设计；
- 更可控的 capability growth；
- 更系统的 benchmark 与资源维护；
- 向更复杂真实环境和模拟系统扩展。

---

## 3. Zhu et al. 2024
### 论文
- 标题：*A survey of multi-agent deep reinforcement learning with communication*
- 来源：Autonomous Agents and Multi-Agent Systems / DOI `10.1007/s10458-023-09633-6`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2024-zhu-et-al-a-survey-of-multi-agent-deep-reinforcement-learning-with-communication-doi-10.1007-s10458-023-09633-6.pdf`
- 证据定位：摘要；`2 Background`；`3 Learning tasks with communication in MADRL`

### 研究背景
这篇不是 LLM 专题，而是为了补齐 multi-agent communication 的传统 MADRL 根基。作者指出，多主体场景广泛存在于自动驾驶、传感网络、机器人和博弈中，而部分可观测与非平稳性使 communication 成为 MARL 中的关键机制。

### 问题定义
论文要解决的是：已有 Comm-MADRL 工作越来越多，但缺少系统化分类与比较框架，因此需要提出一个多维分析空间，让研究者能区分不同 communication 设计。

### 分类框架
摘要明确给出 9 个维度；从章节可见的维度至少包括：
- controlled goal
- communication constraints
- communicatee type
- communication policy
- communicated messages
- message combination
以及训练/评估相关维度
该框架的特点是“多维坐标系”，不是树状 taxonomy。

### 核心观点
- communication 是处理 partial observability 与 non-stationarity 的有效手段。
- Comm-MADRL 的关键差异在于“传给谁、传什么、何时传、怎样学”。
- 把方法投射到多维空间比单轴分类更能发现研究趋势和组合空白。

### 方法脉络
方法脉络体现为：
- 早期把 communication 视为预定义机制；
- 后续转向可学习 communication policy；
- 再细分出通信对象、消息内容、约束、消息组合与训练方案；
- 最后用多维框架总结趋势并提出未来设计组合。

### 数据集 / benchmark
文中讨论的 benchmark 多来自 MARL 环境，而非文本 agent benchmark。通过 PDF 提取可见 MPE、predator-prey、StarCraft II 等环境被反复提及；既有交叉比较也把它定位为“传统通信基线补位综述”。因此其 benchmark 价值在于提供可控多主体决策环境，而不是 LLM 社会交互基准。

### 局限性
- 不直接覆盖 LLM-based natural language agents，因此对语言协商、角色扮演、tool-use 帮助有限。
- 评测生态更偏强化学习环境，对开放式生成任务的迁移性有限。
- 9 维框架很强，但对工业级工程约束着墨较少。

### 未来方向
摘要明确提到通过不同维度组合探索 future Comm-MADRL systems，可归纳为：
- 在真实约束下学习何时通信；
- 探索更丰富的消息形式与目标对象设计；
- 将维度组合系统化，而非单点改进；
- 强化可扩展性与现实通信限制建模。

---

## 4. Chen et al. 2024/2025
### 论文
- 标题：*A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application*
- 来源：arXiv `2412.17481`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf`
- 证据定位：摘要；`2 Core Components of LLM-MAS`；`3/4/5` 应用三分；`6 Challenges and Future Directions`

### 研究背景
作者认为已有综述难以持续覆盖快速增长的新论文，尤其是新应用前沿不断超出既有通用框架，因此需要用“recent advances + application frontiers”的角度重构综述版图。

### 问题定义
论文试图重新定义与扩展 LLM-MAS 的应用边界：除了复杂任务求解，还要系统讨论特定场景模拟与 generative agent evaluation，并整理相关资源和评测。

### 分类框架
最核心的分类是三大应用目的：
1. solving complex tasks
2. simulating specific scenarios
3. evaluating generative agents
此外再辅以 core components 与 challenges/future。

### 核心观点
- 应用目的比单纯系统模块更能解释 2024 年后 LLM-MAS 的扩张方向。
- generative agents 不只执行任务，也逐渐成为动态评测对象和评测主体。
- 新前沿应用正在反向推动 framework 与 evaluation 的更新。

### 方法脉络
方法脉络是“从系统组件走向应用用途”：
- 先定义 generative agents 与 environment；
- 再沿 task-solving、simulation、evaluation 三条应用线展开；
- 最后把 challenges 分解到 agent、interaction 与 evaluation 三层。

### 数据集 / benchmark
章节标题已明确包含 `Resources` 与 `Evaluation`；既有笔记提到 AgentBench、AUCArena、EvalPlus、GSM8K、HotpotQA、HumanEval、MATH、MMLU、MT-Bench、MLAgentBench、ToolBench、ChatEval 等。其特点是比 2024 年通用总览更靠近“agent-specific benchmark”过渡阶段。

### 局限性
- 自身在 `8 Limitations` 中承认，由于篇幅限制，对单个方法的技术细节只能概述。
- 样本集中于 2023-2024 顶会与部分 arXiv，时间覆盖仍有限。
- 用“应用目的”分类虽清晰，但在协议、通信、workflow 等底层机制上的深挖不如专题综述。

### 未来方向
根据 `6 Challenges and Future Directions` 可归纳为：
- generative agents 本体能力与稳定性的提升；
- interaction 机制优化；
- 更强的 LLM-MAS evaluation；
- 让应用、资源与评测协同发展而非分离演进。

---

## 5. Tran et al. 2025
### 论文
- 标题：*Multi-Agent Collaboration Mechanisms: A Survey of LLMs*
- 来源：arXiv `2501.06322`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf`
- 证据定位：摘要；`3 Multi-Agent Collaboration Concept`；`4 Methodology`；`4.2 Collaboration Types`

### 研究背景
作者看到 Agentic AI 正从单体 LLM 走向 collaboration-centric approaches，但对于“协作机制本身”缺少统一框架，因此希望围绕 collaboration 构建一个可扩展综述。

### 问题定义
核心问题是：LLM-based MAS 的 collaboration 由哪些关键维度组成，不同协作机制如何支持复杂真实任务，并能否借此走向 artificial collective intelligence。

### 分类框架
摘要给出完整框架：
- actors
- types（cooperation / competition / coopetition）
- structures（peer-to-peer / centralized / distributed）
- strategies
- coordination protocols
这是十篇里最清晰的协作机制 taxonomy 之一。

### 核心观点
- 多智能体系统研究重心应从 isolated models 转向 collaboration-centric designs。
- 协作不应只等于 cooperation，competition 和 coopetition 同样关键。
- coordination protocol 是把 actor、structure 与 strategy 串起来的中层机制。

### 方法脉络
作者给出的主脉络不是按任务，而是按组织机制：
- 先定义 collaboration concept 与 problem definition；
- 再按 collaboration types 区分合作/竞争/竞合；
- 再讨论策略与结构；
- 最后再连接应用、挑战和 lessons learned。

### 数据集 / benchmark
从正文片段可见 LLMARENA 明确出现；既有笔记还记录 CAMEL、AutoGen 等系统案例。该综述更偏“协作机制在不同场景中的表现”而非单一 benchmark 表，因此 benchmark 信息是服务于协作比较的，而不是完整数据集目录。

### 局限性
- 对 memory、tool-use、workflow optimization 等工程细节讨论不够深。
- benchmark 更像场景举例而非统一评测协议。
- 协作分类非常好用，但对底层 agent 内部能力假设较强。

### 未来方向
结合摘要与 open challenges，可归纳为：
- 提升复杂协作的可解释性与鲁棒性；
- 面向真实场景完善 coordination protocols；
- 将合作、竞争、竞合机制统一纳入 collective intelligence 研究；
- 更系统地连接应用落地与协作理论。

---

## 6. Yan et al. 2025
### 论文
- 标题：*Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems*
- 来源：arXiv `2502.14321`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf`
- 证据定位：摘要；`3.1 Communication Architecture`；`3.2 Communication Goal`；`3.3 Communication Protocol`；`4.1 Communication Strategy`；`5.5 Benchmarks & Evaluation`

### 研究背景
作者指出，既有综述通常按应用领域或系统架构分类，却忽略 communication 在协调 agent 行为与交互中的中心作用。因此需要专门的 communication-centric 综述。

### 问题定义
论文要回答：在 LLM-MAS 中，communication 到底由哪些层面组成，system-level 与 system-internal communication 如何共同决定 collective intelligence，同时现有系统在哪些通信挑战上仍不足。

### 分类框架
作者明确提出双层结构化框架：
- system-level communication：architecture、goals、protocols
- system-internal communication：strategies、paradigms、objects、content
并进一步细分 flat / hierarchical / team / society / hybrid 等架构。

### 核心观点
- communication 是系统能力变量，而不是局部 prompt 技巧。
- 要理解多智能体协作，必须同时看“谁和谁说、为什么说、怎么说、说什么”。
- communication efficiency、security、benchmarking、scalability 是同一个中心问题的不同表现。

### 方法脉络
方法主线是：
- 先交代 LLM agents、传统 MAS 与 LLM-MAS 背景；
- 再从 architecture / goal / protocol 建立外层框架；
- 再深入 strategy / paradigm / object / content 的内层通信机制；
- 最后进入 benchmark、安全、多模态与未来方向。

### 数据集 / benchmark
文中 `5.5 Benchmarks & Evaluation` 明确讨论评测；抽取文本中点名 MultiAgentBench、RealWorldBench，既有笔记补充 GAMA-Bench。作者批评现有数据集覆盖场景少、异构域不足、agent population scale 不够，因此 benchmark 章节既是资源总结，也是批判性诊断。

### 局限性
- 为突出通信，弱化了 memory、tool-use、workflow graph 等其他关键变量。
- 仍以文本通信为主，多模态通信部分相对早期。
- 面向部署的工业执行层约束还需与其他综述合读。

### 未来方向
摘要与目录可直接支持以下方向：
- communication efficiency
- security vulnerabilities 防护
- unified communication protocol
- multimodal communication
- 更完备的 benchmarks & evaluation
- 可扩展通信系统设计

---

## 7. Wu et al. 2025
### 论文
- 标题：*Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances*
- 来源：arXiv `2502.16804`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf`
- 证据定位：摘要；`3 LLM-based Multi-Agent Interaction`；`5 Applications`；`6 Datasets and Benchmark`；`7 Challenges and Future Directions`

### 研究背景
论文起点很现实：单 agent LLM-based ADS 面临 limited perception、insufficient collaboration、high computational demands 三大问题，因此自动驾驶需要走向语言驱动的多 agent 协作。

### 问题定义
作者想系统梳理 LLM-based multi-agent ADS 的交互模式、agent-human interaction、应用、数据集与挑战，明确多智能体在自动驾驶中的独特价值和难题。

### 分类框架
最核心的分类方式是交互对象与协作任务：
- multi-vehicle interaction
- vehicle-infrastructure interaction
- vehicle-assistant interaction
- agent-human interaction
并在应用层展开到 collaborative perception、collaborative decision-making、cloud-edge deployment、assistance-tools。

### 核心观点
- 在自动驾驶中，多智能体的优势首先体现在多视角协同和语义协调，而不是替代底层控制器。
- 单 agent ADS 的三大瓶颈，正好对应 multi-agent ADS 的三个增益点：视野、协作、任务分担。
- 自动驾驶是检验 multi-agent 是否能进入高风险真实系统的重要场景。

### 方法脉络
其方法脉络是明显的垂直场景演化线：
- 先回顾 single-agent ADS；
- 再转向 multi-agent ADS 架构与交互；
- 再按多车、车路、车助理、人机等关系展开；
- 再进入应用、数据集与挑战。

### 数据集 / benchmark
目录中明确有 `6 Datasets and Benchmark`；抽取文本可见 INTERACTION dataset 被点名，既有笔记补充 Waymo Open Motion Dataset 与 multi-agent ADS 数据。该综述的 benchmark 特点是高实时、高安全约束、真实道路交互强，不同于通用文本 agent benchmark。

### 局限性
- 通用性较弱，许多结论强依赖自动驾驶环境。
- LLM 部分更多是高层决策与协调，不等于端到端自动驾驶能力。
- 高风险场景使评测成本和可复现实验门槛更高。

### 未来方向
`7 Challenges and Future Directions` 支持的方向包括：
- 更强的协同感知与协同决策；
- 更可靠的 cloud-edge 部署；
- 更成熟的人机协作模式；
- 更完备的自动驾驶多 agent benchmark 与安全保障。

---

## 8. Jin et al. 2025
### 论文
- 标题：*A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives*
- 来源：arXiv `2503.13415`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-misc-a-comprehensive-survey-on-multi-agent-cooperative-decision-making-scenarios-approaches-challenges-and-perspectives-arxiv-2503.13415.pdf`
- 证据定位：摘要；引言；方法总览与挑战部分（由摘要与抽取片段可见）

### 研究背景
作者将 multi-agent cooperative decision-making 放在复杂协作任务中的核心技术位置，强调其已广泛应用于自动驾驶、无人机导航、灾害救援和模拟军事对抗等现实场景，因此需要统一梳理环境、方法和挑战。

### 问题定义
论文聚焦两个问题：
1. 多 agent 协同决策通常在哪些 simulation environments / platforms 中展开？
2. 主流决策方法体系如何分类，尤其是传统规则/博弈/进化方法与 MARL、LLM 推理方法之间如何比较？

### 分类框架
摘要明确给出两层分类：
- 场景/环境维度：task formats、reward allocation、underlying technologies
- 方法维度：
  1. rule-based
  2. game theory-based
  3. evolutionary algorithms-based
  4. deep MARL-based
  5. LLM reasoning-based

### 核心观点
- simulation environments 不是辅助工具，而是多 agent 决策研究的组成部分。
- 传统规则/博弈/进化方法仍有价值，但 MARL 与 LLM-based decision-making 是当前最值得重点讨论的主线。
- cooperative decision-making 的关键不只在算法，还在任务格式与奖励结构设计。

### 方法脉络
作者把方法脉络放在“传统到现代”的谱系里：
- 从 rule-based 和 fuzzy logic 起步；
- 发展到 game-theoretic 与 evolutionary methods；
- 再进入 deep MARL；
- 最后纳入 LLM reasoning-based cooperative decision-making。
这条谱系适合做传统 MAS 到 LLM-MAS 的桥接。

### 数据集 / benchmark
这篇最强调 environment / platform。抽取文本明确提到 MPE、predator-prey、StarCraft II；摘要也强调会系统分析 simulation environments、task formats、reward allocation。其 benchmark 价值在于“协同决策环境和协议设计”，不是单一问答基准。

### 局限性
- 覆盖面大，单个子类方法的技术深度有限。
- LLM-based decision-making 由于新，细化程度可能不如 MARL 部分。
- 更多是从 cooperative decision-making 视角切入，不覆盖完整 LLM agent engineering。

### 未来方向
摘要直接提到 challenges and perspectives，可归纳为：
- 更复杂真实环境的协同决策建模；
- MARL 与 LLM 的深度结合；
- 更合理的 reward allocation 与 environment design；
- 面向多领域应用的可迁移协作策略。

---

## 9. Lin et al. 2025
### 论文
- 标题：*Creativity in LLM-based Multi-Agent Systems: A Survey*
- 来源：arXiv `2505.21116`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf`
- 证据定位：摘要；`2 MAS Workflow and Proactivity`；`3 MAS Techniques for Creativity`；`5 Evaluation`；`6 Datasets`；`7 Challenges and Future Work`

### 研究背景
作者认为既有 MAS 综述主要关注 infrastructure，却忽略 creativity：即新颖输出如何生成、如何评估、persona 如何影响创意、creative workflow 如何协调。因此需要第一篇专门面向 creativity in MAS 的综述。

### 问题定义
论文关注的是：在文本与图像生成任务中，creative MAS 如何组织 agent proactivity、persona、generation techniques、datasets 与 evaluation，从而系统提升创造力。

### 分类框架
摘要与目录支持以下核心分类：
- workflow 与 proactivity 谱系
- creativity techniques：divergent exploration、iterative refinement、collaborative synthesis
- persona and agent profile
- evaluation：objective / subjective / user study
- datasets：psychological test datasets、task-specific datasets

### 核心观点
- creativity 是 MAS 中独立的重要维度，而不是 infrastructure 的副产品。
- persona、proactivity 与 workflow integration 会实质影响创意输出质量。
- creative MAS 当前最大短板不在生成本身，而在 evaluation inconsistency、bias mitigation、coordination conflict 与缺少 unified benchmarks。

### 方法脉络
其方法主线很清楚：
- 从 workflow 与 agent 主动性出发；
- 到三类创造性生成技术；
- 再到 persona/profile；
- 再到 evaluation 与 dataset；
- 最后总结 creative MAS 的挑战与 future work。

### 数据集 / benchmark
目录显式包含 `5 Evaluation` 和 `6 Datasets`。作者区分 psychological test datasets 与 task-specific datasets，并强调现阶段 benchmark 缺乏统一标准。与通用 multi-agent benchmark 相比，这一方向更依赖多维主客观评价。

### 局限性
- 强调 creativity，会弱化通用协作、通信、tool-use 问题。
- 评价高度依赖主观性和用户研究，横向可比性弱。
- 当前许多 creative debate / synthesis 方法难以扩展到大规模 agent 群体。

### 未来方向
根据 `7 Challenges and Future Work` 与摘要可归纳为：
- 建立 unified creative benchmarks；
- 更稳健的 bias mitigation；
- 更好地解决 coordination conflicts；
- 让 proactivity 自适应任务与用户偏好；
- 拓展到更大规模、更异质的 creative MAS。

---

## 10. Chen et al. 2026
### 论文
- 标题：*The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs*
- 来源：arXiv `2602.11583`
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf`
- 证据定位：摘要；`4 Methodology and Scope of the Survey`；`5/6/7` 三大范式章节；`8 Discussion, Open Problems, and Future Directions`

### 研究背景
作者认为 multi-agent communication 已横跨 MARL、emergent language、LLM-based systems，但缺少统一框架来解释这些不同范式中的共性与权衡，因此需要 dedicated survey 来统一三条传统。

### 问题定义
核心问题是：如何用 Who / Whom / When / What / Why 这五个基本问题，统一刻画 multi-agent communication，并解释 MARL、EL、LLM 三种范式如何分别处理这些问题。

### 分类框架
全文最核心就是 Five Ws：
1. who communicates
2. with whom
3. when
4. what
5. why
同时按范式组织主体内容：
- MARL communication
- emergent language
- LLM-based communication

### 核心观点
- Five Ws 是跨范式最小统一语言，可把通信问题分解成稳定维度。
- MARL、EL、LLM 三类方法不是替代关系，而是应对不同局限的连续演化。
- 真正重要的不只是会不会通信，而是通信在任务、规模、可解释性与协调收益上的 trade-off。

### 方法脉络
这篇的方法脉络是典型“历史演化 + 统一框架”双线：
- 先讲 communication as action 的理论基础；
- 再综述已有三类 survey；
- 再在 `Methodology and Scope` 中界定范围；
- 接着对 MARL、EL、LLM 三大范式分别按 Five Ws 重组；
- 最后进入 open problems 与 future directions。

### 数据集 / benchmark
既有笔记记录 AvalonBench、BattleAgentBench、ChatEval、GAIA、MultiAgentBench、RoCoBench、CAMEL 等；目录还明确有 `Evaluation Settings for Communication` 和 `Future Works on Benchmarking`。其 benchmark 讨论重点是“跨范式 communication evaluation”，不是只列数据集名。

### 局限性
- 高度聚焦通信，不是通用 multi-agent 全景综述。
- 尽管统一了 5W 框架，但工程运行时与成本治理仍需和 workflow/tool 综述互补。
- 跨范式统一很强，但具体到某些专题场景时仍需额外细读原始文献。

### 未来方向
`8 Discussion, Open Problems, and Future Directions` 以及目录中的 `Future Works on Benchmarking`、`Human-Centric Multi-Agent Communication` 明确支持：
- 新 communication algorithms；
- 更统一的 benchmarking；
- human-centric multi-agent communication；
- 混合系统，把 learning、language、control 结合起来；
- 兼顾 task、scalability 与 interpretability 的通信设计。

---

## 横向总览

### 共同研究背景
十篇综述都把 multi-agent 放在“单体模型已不足以应对复杂、分布式、动态任务”的背景下，但切入点分为三类：
1. 通用系统扩张：Li 2024、Guo 2024、Chen 2024/2025
2. 通信/协作/决策机制：Zhu 2024、Tran 2025、Yan 2025、Chen 2026、Jin 2025
3. 垂直与新兴场景：Wu 2025、Lin 2025

### 共性的分类框架演化
- 2024 通用综述多按 workflow / component / application 分类。
- 2025 开始出现 collaboration、communication、cooperative decision-making、creativity 等专题 taxonomy。
- 2026 则尝试用 Five Ws 这种更抽象的统一框架连接多个研究传统。

### 共性的 benchmark 判断
- 2024：大量借用 GSM8K、HumanEval、MMLU 等通用基准。
- 2025：更强调 MultiAgentBench、LLMArena、INTERACTION、creative task datasets 等专题基准。
- 2026：进一步强调 communication-specific evaluation 的统一问题。

### 共性的局限
- 统一 benchmark 缺乏；
- 子方向间 taxonomy 不兼容；
- communication、workflow、memory、tool-use、safety 往往分开讨论；
- 垂直场景与通用框架之间可迁移性不足。

### 共性的未来方向
- 统一评测协议；
- 提升 communication / coordination 的效率与安全；
- 打通传统 MARL 与 LLM-based MAS；
- 面向真实高风险环境强化部署与治理；
- 在 creative/social/human-centric 场景中建立更成熟的评价标准。

## 与既有产出的关系
- 单篇更细的“优缺点、值得精读章节、关键图表”见：`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-detailed-reading-notes.md`
- 十篇交叉比较与研究空白见：`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-cross-comparison.md`
- 本文件补齐的是该任务明确要求的 8 个字段口径，尤其是“研究背景、问题定义、未来方向”三项。