# 2026-03-26 十篇 multi-agent 综述逐篇详读笔记

- 任务范围：对 10 篇综述逐篇提炼研究问题、分类框架、核心观点、方法谱系、评测设定、优缺点、局限、值得精读章节、关键图表。
- 说明：本文件为当前项目的结构化精读主交付，依据两类证据整理：
  1. arXiv 论文主页与元数据（各条目中的 `来源`）。
  2. 从仓库当前工作树删除差异中恢复的上一轮结构化精读内容，原路径为 `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`、`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md` 与 `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`；本次已将其中可核验内容迁移并重组到当前项目。
- 边界：本文件优先保留可由题目、摘要、章节标题、先前结构化笔记共同支撑的判断；对“值得精读章节/关键图表”采用“按章节标题或综述常见总图位置的推荐阅读位点”表述，并明确为阅读建议而非逐页 OCR 复刻。

---

## 1. Guo et al. 2024 — Large Language Model based Multi-Agents: A Survey of Progress and Challenges

- 来源：https://arxiv.org/abs/2402.01680
- 年份：2024
- 主题标签：通用总览、LLM-based multi-agent、组件框架、应用总图

### 研究问题
这篇综述试图回答：LLM-based multi-agent systems 由哪些核心组件构成、面向哪些任务/环境、相比单 Agent 的新增能力与挑战分别是什么。

### 分类框架
作者采用“系统组件 + 应用场景 + 挑战”的三层组织方式：
- 系统组件层：Agents-Environment Interface、Agents Profiling、Agent Management、Agents Communication、Training Scheme、Multi-Agents Orchestration and Efficiency。
- 应用层：Problem Solving、World Simulation、Dialogue Dataset Generation。
- 挑战层：扩展性、伦理与风险、编排效率等。

### 核心观点
- multi-agent 的价值不只是“多几个 LLM 并行回答”，而是通过角色设定、交互和管理获得更复杂的任务分解与协作能力。
- communication、management 和 orchestration 是从单 Agent 走向多 Agent 的真正增量。
- world simulation 与复杂问题求解是早期 LLM 多智能体最具代表性的两类落地方向。

### 方法谱系
可按“从系统搭建到应用落地”的谱系理解：
1. 接口与角色设定：如何定义 agent 的 persona、上下文、环境接口。
2. 管理与通信：如何分工、协商、共享中间状态。
3. 训练与增强：如何通过训练/反馈提升多 Agent 协同。
4. 编排与效率：如何控制 token、轮数、调用链和资源成本。
5. 应用映射：从任务求解扩展到仿真与数据生成。

### 评测设定
从恢复笔记可追溯到的 benchmark 包括 GSM8K、HumanEval、MMLU、BIG-bench、ChatArena、RoCoBench、CAMEL、AvalonBench。说明其评测覆盖：
- 推理/问答：GSM8K、MMLU；
- 代码：HumanEval；
- 对话/交互：ChatArena、CAMEL；
- 协作/博弈：RoCoBench、AvalonBench。
该综述的评测特征是覆盖广，但 benchmark 口径较杂，尚不是统一多智能体协议。

### 优点
- 适合作为 2024 时点的全景入门综述。
- 组件、应用、挑战三层结构清晰。
- 同时讨论 benchmark 与实现资源，对后续落地有帮助。

### 缺点
- 对后续 2025–2026 年出现的 workflow、tool orchestration、communication 专题深度不足。
- 更像全景地图，专题深挖有限。

### 局限
- 时效性局限明显。
- 分类仍偏宽口径，把多个子方向放在同一框架内，横向可比性一般。

### 值得精读章节
- `Agents Communication`：这是后续 communication-centric 综述的起点。
- `Multi-Agents Orchestration and Efficiency`：适合和 2026 年 workflow/tool-use 综述串读。
- `LLM-MA for World Simulation`：适合与 role-playing / social agents 方向衔接。

### 关键图表
- 系统总览/组件框架图：帮助快速建立 multi-agent 系统的模块化心智模型。
- 应用分类总表：适合拿来做后续十篇综述的主题对照基线。

---

## 2. Aratchige & Ilmini 2025 — LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems

- 来源：https://arxiv.org/abs/2504.01963
- 年份：2025
- 主题标签：技术底座、architecture、memory、planning

### 研究问题
该综述试图回答：构建有效的 LLM-based multi-agent systems 时，哪些技术底层最关键，尤其是 architecture、memory、planning 与 frameworks 如何协同。

### 分类框架
四大核心板块：
- Architecture
- Memory
- Planning
- Technologies / Frameworks

### 核心观点
- multi-agent 性能提升往往源于架构设计而非单纯模型替换。
- memory 与 planning 是长程任务协作的核心支柱。
- 技术框架层决定了系统是否可复用、可扩展、可工程化。

### 方法谱系
更偏工程栈谱系：
1. 体系结构：集中式、层级式、模块化多角色组合。
2. 记忆机制：短期上下文、长期记忆、共享记忆。
3. 规划机制：ReAct 类、分层规划、任务拆解与重规划。
4. 框架实现：从概念原型走向平台化搭建。

### 评测设定
恢复笔记中对应的典型任务/基准包括 ALFWorld、HotpotQA、HumanEval、MATH、MT-Bench、AlpacaEval、CAMEL、AutoGen。说明其关注：
- 交互环境任务；
- 复杂推理与代码；
- 对话质量与系统框架可用性。

### 优点
- 工程视角强，适合做系统设计参考。
- 明确把 memory / planning 拿出来单列，便于做技术拆解。
- 对后续实现者最友好。

### 缺点
- 应用侧覆盖没有通用总览类综述广。
- 对 communication 的专题化讨论不如专门通信综述深入。

### 局限
- 更偏“怎么搭系统”，不完全回答“哪些任务最需要多 Agent”。
- 对 benchmark 的统一性讨论仍有限。

### 值得精读章节
- `Architecture`：用于搭建总体系统蓝图。
- `Memory`：适合与 role-playing / social agents 的长期一致性问题联读。
- `Planning`：可与 workflow optimization 综述形成技术链条。

### 关键图表
- architecture 分类图：看清角色组织和控制流。
- memory / planning 对照表：适合后续做技术路线选择。

---

## 3. Chen et al. 2024 — A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application

- 来源：https://arxiv.org/abs/2412.17481
- 年份：2024（arXiv 时间口径；恢复稿中曾以 2025 文件名保存）
- 主题标签：应用前沿、复杂任务、仿真、评测

### 研究问题
这篇综述关注：LLM-based MAS 已经扩展到哪些新应用边界，尤其是复杂任务求解、特定场景仿真和生成式 agent 评测。

### 分类框架
- 应用侧三分：solving complex tasks、simulating specific scenarios、evaluating generative agents。
- 配套补充：core components、interactions、challenges and future directions。

### 核心观点
- 多 Agent 的价值正通过“复杂任务、仿真与评测”三条应用主线显化。
- generative agents 不只是执行器，也正在成为评测对象与评测主体。
- 应用前沿已经反过来推动系统组件与交互模式演化。

### 方法谱系
- 复杂任务求解：任务分工、协作求解、互审。
- 场景仿真：让多个 agents 在特定环境中形成行为动力学。
- agent 评测：让 agent 不只被测试，还参与评测闭环。
该谱系体现出从“执行任务”走向“模拟系统”和“评估系统”的外扩。

### 评测设定
恢复笔记列出 AgentBench、AUCArena、EvalPlus、GSM8K、HotpotQA、HumanEval、MATH、MMLU、MT-Bench、MLAgentBench、ToolBench、LLMArena、ChatEval。其特征是：
- 横跨能力评测与系统评测；
- 开始出现 agent-specific benchmarks；
- 评测对象不再只是单轮输出，而是系统行为。

### 优点
- 应用导向强，适合寻找落地研究切口。
- agent evaluation 讨论比很多通用综述更前。
- 对“新前沿”这个问题回答比较到位。

### 缺点
- 纯技术分类深度不如工程/通信专项综述。
- 方法论可能更偏应用映射，底层机制讨论略散。

### 局限
- 应用面广也意味着分类口径偏宽。
- 如果想研究通信协议或 runtime graph，这篇不是最深入口。

### 值得精读章节
- `solving complex tasks`：对应最主流的多 Agent 应用范式。
- `evaluating generative agents`：适合和 benchmark 脉络专题一起读。
- `Challenges posed by interactions`：帮助提炼后续研究空白。

### 关键图表
- 应用前沿分类图：适合给团队快速解释“现在都拿 multi-agent 做什么”。
- benchmark / evaluation 汇总表：适合做后续总览矩阵。

---

## 4. Tran et al. 2025 — Multi-Agent Collaboration Mechanisms: A Survey of LLMs

- 来源：https://arxiv.org/abs/2501.06322
- 年份：2025
- 主题标签：collaboration taxonomy、合作/竞争/竞合、结构设计

### 研究问题
作者试图系统回答：多个 LLM agents 协作时，合作关系、结构拓扑、策略与协调协议如何组织，哪些机制真正决定集体智能收益。

### 分类框架
- actors
- relation types：合作 / 竞争 / 竞合
- structures：点对点 / 中心化 / 分布式
- strategies
- coordination protocols

### 核心观点
- 多 Agent 的收益来自结构和机制设计，而非简单增加 agent 数量。
- 合作、竞争、竞合应被视为同等重要的组织关系，而非只研究合作。
- coordination protocol 是连接角色、结构和策略的关键中层抽象。

### 方法谱系
- 关系谱系：从 cooperation 到 competition/coopetition。
- 结构谱系：从 pairwise 到 centralized，再到 distributed。
- 协调谱系：从简单消息传递到协议化协作与冲突解决。
其核心不是任务类型，而是组织机制。

### 评测设定
恢复笔记提到 LLMArena、CAMEL、AutoGen 以及专门的 `Comprehensive Evaluation and Benchmarking` 章节；摘要还提及 5G/6G、Industry 5.0、QA/NLG、social/cultural settings。可见其评测更关注：
- 协作关系是否提升结果；
- 不同协作拓扑下的任务表现；
- 面向多场景的机制可迁移性。

### 优点
- collaboration taxonomy 很完整。
- 适合研究 collective intelligence。
- 把合作/竞争/竞合并列，是明显优点。

### 缺点
- tool-use、workflow、memory 等工程纵深不是重点。
- 对具体 benchmark 的协议级可复现描述可能不如工程综述详细。

### 局限
- 更适合回答“如何组织多 Agent”，不直接回答“如何落地工业 runtime”。
- 某些 benchmark/案例需要二次清洗才能严格复用。

### 值得精读章节
- `Collaboration Types`：理解关系设计。
- `Communication Structures`：与通信综述并读效果最好。
- `Coordination and Orchestration`：是 collaboration 向 workflow 过渡的桥梁。

### 关键图表
- collaboration taxonomy 图：是十篇中最适合作为协作机制底图的图之一。
- relation/structure/protocol 对照表：适合后续做横向编码表。

---

## 5. Wu et al. 2025 — Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances

- 来源：https://arxiv.org/abs/2502.16804
- 年份：2025
- 主题标签：自动驾驶、垂直应用、高风险真实系统

### 研究问题
在自动驾驶场景下，单 Agent LLM 方案面临感知受限、协作不足和成本过高等问题；该综述关注多 Agent + LLM 能否通过车-车、车-路、车-助手、agent-人协同来缓解这些问题。

### 分类框架
按交互对象与协作任务划分：
- Multi-Vehicle Interaction
- Vehicle-Infrastructure Interaction
- Vehicle-Assistant Interaction
- Agent-Human Interaction
并配套讨论：Collaborative Perception、Collaborative Decision-Making、Cloud-Edge Deployment、Collaborative Assistance Tools。

### 核心观点
- 多 Agent 对自动驾驶的价值在于分布式视角整合与协同决策。
- LLM 在该场景中更像“语义协调层”，而不是替代底层控制器。
- 真正难点来自实时性、安全性、部署约束，而不是单纯任务分数。

### 方法谱系
- 从单 Agent ADS 到多 Agent ADS。
- 从纯感知/决策模块走向协同感知、协同决策。
- 从端侧孤立系统走向 cloud-edge 协同与人机协作。

### 评测设定
恢复笔记记录 Waymo Open Motion Dataset、Multi-agent Autonomous Driving Dataset，以及专门的 `Datasets and Benchmark` 章节。说明其评测设置具有明显领域特征：
- 多车交互；
- 高实时、强安全约束；
- 感知/决策/部署联合考察。

### 优点
- 真实系统约束非常强，研究问题清晰。
- 交互对象的分类天然可解释。
- 对“多 Agent 如何进入高风险场景”很有参考价值。

### 缺点
- 通用性较弱，结论未必能直接外推到一般多 Agent 系统。
- 强依赖领域背景。

### 局限
- 垂直领域综述，不是通用 multi-agent 基础综述。
- benchmark 也更偏专用场景。

### 值得精读章节
- `Multi-Agent ADS` 总览部分：理解多 Agent 在真实系统中的功能定位。
- `Collaborative Decision-Making`：是最贴近“多 Agent 真增益”的章节。
- `Challenges and Future Directions`：适合提炼高风险系统研究缺口。

### 关键图表
- 自动驾驶多交互对象架构图：适合展示多主体协同拓扑。
- 数据集与 benchmark 总表：适合做垂直场景 benchmark 脉络归档。

---

## 6. Yan et al. 2025 — Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems

- 来源：https://arxiv.org/abs/2502.14321
- 年份：2025
- 主题标签：communication-centric、协议、内部通信

### 研究问题
作者认为以往综述偏重应用或架构，而忽视了 communication 在 LLM-MAS 中的核心地位，因此要从通信角度重构整个研究版图。

### 分类框架
两层框架：
- system-level communication：architecture、goals、protocols
- system-internal communication：strategies、paradigms、objects、content
可进一步细化为 Communication Architecture、Goal、Protocol、Strategy、Paradigm、Object、Content。

### 核心观点
- communication 不是 prompt 细节，而是系统能力变量。
- 多 Agent 收益高度依赖通信设计质量。
- scalability、security 和 communication efficiency 是同一问题的不同面。

### 方法谱系
- 从 system-level 通信结构出发：谁和谁连、为什么连。
- 进入 protocol / strategy：怎么连、何时连。
- 进一步到 content / object：传什么。
- 最后走向 benchmark 与 evaluation：如何评估通信是否有效。

### 评测设定
恢复笔记提到 GAMA-Bench、MultiAgentBench、RealWorldBench 以及单独的 `Benchmarks and Evaluation` 章节。其评测关注点不只是结果分数，还包括：
- 通信是否必要；
- 通信是否高效；
- 通信是否引入风险。

### 优点
- 视角极其鲜明，补上通信主线空白。
- 双层 taxonomy 很适合后续研究设计。
- 安全、扩展性、性能问题被统一到 communication 角度下审视。

### 缺点
- 对 memory、workflow、tool-use 关注相对弱。
- 偏重通信，可能弱化其他系统变量。

### 局限
- 若读者关注完整系统落地，需要和工程/工作流综述配套阅读。
- 多模态通信与非文本协议仍处于较早阶段。

### 值得精读章节
- `Communication Architecture`：回答“谁和谁说”。
- `Communication Protocol`：回答“按什么规则说”。
- `Benchmarks and Evaluation`：回答“通信系统怎么测”。

### 关键图表
- communication taxonomy 总图：是十篇里最值得反复看的图之一。
- benchmark 与风险/效率对照表：适合后续抽取评测维度。

---

## 7. Xu et al. 2026 — The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration

- 来源：https://arxiv.org/abs/2603.22862
- 年份：2026
- 主题标签：tool use、多工具编排、工业级 runtime

### 研究问题
该综述回答：tool use 如何从简单函数调用演化为多工具、长程、受约束的 orchestration 问题；这对 agent systems 的核心研究问题意味着什么。

### 分类框架
六大维度：
- inference-time planning and execution
- training and trajectory construction
- safety and control
- efficiency under resource constraints
- capability completeness in open environments
- benchmark design and evaluation
此外还有 Topological Planning、Long-Horizon Orchestration、Agent Self-Improvement、Industrial-Grade Governance 等专题。

### 核心观点
- 真实 agent 系统的难点常常不是“多 agent”，而是“多工具+长轨迹+受约束执行”。
- tool orchestration 把 planning、execution、safety、budget 放到同一优化问题中。
- 工业级 agent 必须把治理和工程约束放进研究问题本身。

### 方法谱系
- 从 single-tool call 到 multi-tool chain。
- 从静态调用到规划驱动执行。
- 从执行正确性到预算/安全/开放环境适应。
- 从单条轨迹走向 trajectory construction 与 self-improvement。

### 评测设定
恢复笔记包含 AgentLongBench、AndroidArena、CostBench、HammerBench、MCP-Bench、MTU-Bench、Mobile-Bench、OdysseyBench、RepoBench、RestBench。评测特点：
- 长程工具使用；
- 真实或半真实环境；
- 成本、鲁棒性和治理被纳入。

### 优点
- 与当前 agent engineering 非常贴合。
- benchmark 汇总密度高。
- 把安全与成本纳入主线，而非附录。

### 缺点
- 不是纯 multi-agent collaboration survey。
- 社会交互、role-play 类议题覆盖较弱。

### 局限
- 更偏工具编排层，对 communication/social interaction 的连接需要读者自己补。
- 可能低估了多 Agent 身份与组织结构的重要性。

### 值得精读章节
- `Long-Horizon Orchestration`：最值得和 workflow optimization 对读。
- `Safety and Control`：适合接 industrial governance 问题。
- `Benchmark design and evaluation`：适合抽取后续实验设置。

### 关键图表
- tool-use evolution 时间线/层级图：展示从简单调用到复杂编排的路径。
- benchmark 总表：是做实验设计时最有实用价值的表之一。

---

## 8. Yue et al. 2026 — From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents

- 来源：https://arxiv.org/abs/2603.22386
- 年份：2026
- 主题标签：workflow optimization、runtime graph、ACG

### 研究问题
workflow 不再只是静态 prompt chain；作者想回答的是：工作流结构何时确定、哪些部分可被优化、以及哪些信号驱动优化。

### 分类框架
三条主轴：
1. when structure is determined：静态 vs 动态
2. what part of the workflow is optimized
3. which evaluation signals guide optimization
并细分 selection/pruning、pre-execution generation、in-execution editing 等动态优化类型。

### 核心观点
- agent workflow 应被视为图结构，而非固定模板。
- template、realized graph、trace 是三个不同对象，必须区分。
- verifier / feedback 对 workflow 优化至关重要。

### 方法谱系
- 静态模板阶段。
- 动态运行时图阶段。
- 图级优化阶段：选择、生成、编辑。
- 反馈驱动阶段：verifier、cost、robustness 联合优化。

### 评测设定
恢复笔记包含 FlowBench、GAIA、GSM8K、HotpotQA、HumanEval、MATH、MCP-Bench、MCPEval、SOP-Bench、SWE-bench、Terminal-Bench、ToolBench、WorkflowBench。可见其评测不局限于单一任务，而是面向流程执行能力。

### 优点
- taxonomy 非常清晰。
- 直接提供 ACG（agentic computation graphs）这一强抽象。
- 很适合后续做 runtime 优化研究。

### 缺点
- 社会互动、通信细节不是重点。
- 对领域应用侧案例相对少。

### 局限
- 更偏 workflow engineering 视角。
- 若读者关注 role/persona/society，这篇覆盖不够。

### 值得精读章节
- `when structure is determined`：理解静态/动态边界。
- `in-execution editing`：理解运行时自适应。
- `Open Problems and Future Directions`：适合直接提 idea。

### 关键图表
- 静态模板到动态图的范式迁移图。
- workflow optimization taxonomy 表/图：适合后续研究选题编码。

---

## 9. Chen et al. 2026 — The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs

- 来源：https://arxiv.org/abs/2602.11583
- 年份：2026
- 主题标签：5W 通信理论、跨范式桥接、MARL 到 LLM

### 研究问题
多智能体通信研究跨越 MARL、涌现语言、LLM agents，但长期缺少统一框架。该综述提出用 5W 统一通信研究版图。

### 分类框架
- Who
- Whom
- When
- What
- Why
同时按历史脉络连接 MARL communication、emergent language、LLM-powered multi-agent communication。

### 核心观点
- 5W 是一种可跨范式复用的通信最小框架。
- LLM 时代的多 Agent 通信应当和 MARL / emergent language 传统对话。
- 通信问题可以被系统化拆成“主体、对象、时机、内容、动机”五个基本变量。

### 方法谱系
- 历史谱系：MARL → emergent language → LLM communication。
- 理论谱系：从单一消息机制转向完整问题分解框架。
- 方法谱系：以 5W 为坐标重组不同通信方法。

### 评测设定
恢复笔记包含 AvalonBench、BattleAgentBench、ChatEval、GAIA、MultiAgentBench、RoCoBench、CAMEL。该综述强调：
- benchmark 应支持跨范式比较；
- 通信质量而非单纯结果分数值得单列。

### 优点
- 5W 框架极具可迁移性。
- 把 LLM 多 Agent 通信放回更长理论历史中。
- 综述方法学更规范，纳排标准更清楚。

### 缺点
- 主题高度聚焦通信，非通信议题覆盖较少。
- 若要做完整系统设计，需要结合 workflow/tool/memory 综述。

### 局限
- 不是全景 multi-agent survey，而是通信专题旗舰综述。
- 工程运行时、预算与治理层面讨论不如 workflow/tool-use 文献细。

### 值得精读章节
- `Search Strategy and Temporal Scope`：看清方法学口径。
- 5W 主体章节：是全文信息密度最高的部分。
- `Perspectives on Future Directions`：适合直接提炼开放问题。

### 关键图表
- 5W 总框架图：建议作为十篇综述中最关键的图之一长期保留。
- 三大脉络对照图（MARL / emergent language / LLM）：适合做跨范式汇报。

---

## 10. Wang et al. 2026 — Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends

- 来源：https://arxiv.org/abs/2601.10122
- 年份：2026
- 主题标签：role-playing、social agents、memory、personality

### 研究问题
这篇综述要回答：role-playing language agents 如何从模板驱动演化为由人格、记忆、动机共同驱动的角色型多智能体系统，以及这一方向的主要技术难题是什么。

### 分类框架
- Evolution of Research Paradigms
- Core Technologies of Role-Playing Modeling
- Construction and Annotation of Role-Specific Data
- Evaluation Methods and Metrics
- Future Outlook and Research Trends
核心技术又分为 Character Setting and Personality Modeling、Character Memory Mechanisms、Behavior and Decision-Making Modeling。

### 核心观点
- role-playing agents 是 multi-agent 走向 social simulation 的关键分支。
- personality、memory、motivation 是角色一致性的三大技术支柱。
- 评测不能只看任务完成，还要看人格一致性、叙事连贯性和关系稳定性。

### 方法谱系
- 从 prompt-based role setup 到 personality modeling。
- 从静态角色卡到记忆增强。
- 从单角色模拟到多角色协作叙事与社会互动。
- 从生成质量评测到角色 fidelity / alignment 评测。

### 评测设定
恢复笔记提到 CharacterEval、RoleBench、RoleEval、RoleEval-Chinese、RoleEval-Global、RMTBench、RVBench。说明此方向已有较强的专门评测生态，重视：
- 人格一致性；
- 角色行为合理性；
- 跨文化/跨语言表现。

### 优点
- 对 social agents 的技术拆解很清晰。
- 数据构建、标注和评测讨论都较实。
- 很适合延展到 companion、social simulation、narrative systems。

### 缺点
- 通用多 Agent 协作/工具调用不是主线。
- 面向任务型系统的直接指导有限。

### 局限
- 领域边界更偏 social interaction，而非通用 MAS。
- 与工业级 runtime、workflow 优化的连接需要额外补充。

### 值得精读章节
- `Character Memory Mechanisms`：是理解长期角色一致性的关键。
- `Evaluation Methods and Metrics`：适合抽取 social-agent benchmark。
- `Future Outlook and Research Trends`：能直接转化为研究选题。

### 关键图表
- role-playing agent 技术栈图：适合解释角色、记忆、动机三者关系。
- evaluation taxonomy / benchmark 总表：适合后续做社会型 agent 评测设计。

---

## 横向小结

### 十篇综述共同覆盖的主线
- 通用总览：Guo 2024、Chen 2024
- 技术底座：Aratchige 2025
- 协作与通信：Tran 2025、Yan 2025、Chen 2026
- 工具与工作流：Xu 2026、Yue 2026
- 垂直/社会化场景：Wu 2025、Wang 2026

### 方法谱系总脉络
1. 通用组件式综述（2024）
2. 应用/协作专题化综述（2025）
3. 通信、工具编排、workflow、role-play 的专题纵深综述（2026）

### 评测设定总判断
- 2024：更多借用通用推理/代码/对话 benchmark。
- 2025：开始强调 agent-specific benchmarks。
- 2026：workflow、tool-use、communication、role-play 各自形成专项 benchmark 簇，但横向统一评测仍不足。
