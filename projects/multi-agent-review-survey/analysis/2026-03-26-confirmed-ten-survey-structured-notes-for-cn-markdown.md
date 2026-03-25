# 2026-03-26 已确认 10 篇综述的结构化笔记（供后续中文 Markdown 精读复用）

- Timestamp: 2026-03-26T02:56:37+08:00
- Session: 智乃-10-1774464944-212caf
- Purpose: 针对当前 canonical reading set 的 10 篇已确认综述，统一抽取 `摘要`、`研究问题`、`分类框架`、`核心结论`、`局限性`、`可延展方向` 六类字段，作为后续中文 Markdown 精读与汇报的直接输入。
- Canonical source of truth: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- Primary provenance:
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
  - `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-list-with-cn-abstract-entry.md`

> 说明：本文件不重新发明新的论文事实；所有字段均从项目内既有 cross-review 工件归纳、重组并压缩为统一模板。所谓“摘要”在此按后续中文写作需要，采用**中文摘要提要**而非逐字转录原文摘要；若后续需要逐字英文 abstract，应回到对应来源页面（见 `ten-paper-metadata.md` 中 source URL）。

---

## 统一模板

每篇综述统一记录：
1. 摘要（中文提要）
2. 研究问题
3. 分类框架
4. 核心结论
5. 局限性
6. 可延展方向

---

## 1) Guo et al. 2024 — Large Language Model based Multi-Agents: A Survey of Progress and Challenges

- 年份：2024
- 来源页面：`https://arxiv.org/abs/2402.01680v2`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf`

### 摘要
该综述系统梳理了 LLM-based multi-agent systems 的研究进展，重点讨论这些系统模拟了哪些环境与任务、agent 如何进行角色设定与通信、以及 agent 能力如何被训练和增强。文章同时汇总典型应用、数据集/benchmark、工具链与主要挑战，试图给出该方向的总图谱。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 1 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 1。

### 研究问题
- LLM-based multi-agent systems 的核心组成模块是什么？
- 这些系统主要被用于哪些任务与场景？
- 多 agent 的通信、管理与能力增长面临哪些共性挑战？

### 分类框架
- 系统组件：interface、profiling、management、communication、training、orchestration/efficiency
- 应用场景：problem solving、world simulation、dialogue dataset generation
- 支撑层：datasets & benchmarks、implementation tools & resources、challenges & opportunities

### 核心结论
- LLM-MAS 已形成相对稳定的系统拆解方式，通信、角色设定与编排效率是主轴变量。
- 该方向已从简单多角色问答扩展到复杂任务求解、世界模拟与对话数据生成。
- benchmark 与工具生态开始成形，但系统化评测与规模化规律仍不充分。

### 局限性
- 发表时点较早，对 2025-2026 年 workflow、tool orchestration、5W communication 等专题进展覆盖不足。
- 分类广而全，但对某些垂直议题的深挖不如后续专题综述。

### 可延展方向
- 多模态与复杂环境中的多 agent 协作
- 通信可靠性、幻觉控制与安全治理
- multi-agent scaling law 与编排效率规律
- 可复现 benchmark 与统一评测协议

---

## 2) Aratchige & Ilmini 2025 — LLMs Working in Harmony

- 年份：2025
- 来源页面：`https://arxiv.org/abs/2504.01963v1`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf`

### 摘要
该文从系统构建视角总结了高效 LLM-based multi-agent systems 的关键技术面，重点聚焦 architecture、memory、planning 与 frameworks/technologies。文章强调 Mixture-of-Agents、ReAct 类规划、记忆增强与系统框架是构建有效多智能体系统的底层支柱。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 2 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 2。

### 研究问题
- 构建有效的 LLM-MAS 时，哪些技术维度最关键？
- architecture / memory / planning / framework 之间如何共同决定系统表现？
- 当前系统在 scalability、real-time response、coordination 上的主要瓶颈是什么？

### 分类框架
- Architecture
- Memory
- Planning
- Technologies / Frameworks
- Future Directions

### 核心结论
- 多智能体系统性能并不只由模型能力决定，系统架构、记忆机制和规划设计同样是决定性因素。
- 工程上“怎么搭”比“堆多少 agent”更重要。
- LLM-MAS 已从概念验证走向需要考虑实时性、协调约束与工程可维护性的阶段。

### 局限性
- 偏技术搭建视角，应用图谱不如总览型综述全面。
- benchmark 与领域案例覆盖相对凝练，适合工程提纲，不一定适合做全景式调研唯一入口。

### 可延展方向
- 大规模 agent 的协同扩展机制
- 低延迟 / 实时多 agent runtime
- 长程任务中的 memory-planning 一体化
- 统一框架层标准与复现实验接口

---

## 3) Chen et al. 2024 — A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application

- 年份：2024（项目统一口径）
- 来源页面：`https://arxiv.org/abs/2412.17481v2`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf`

### 摘要
该综述聚焦 LLM-based multi-agent systems 的最新应用前沿，围绕复杂任务求解、特定场景仿真、生成式 agent 评测等方向，重新梳理多 agent 系统的能力边界。文章在应用导向之外，也回顾 core components、interactions 与未来挑战。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 3 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 3；年份修正见 `projects/multi-agent-review-survey/analysis/2026-03-26-final-markdown-cross-review.md`。

### 研究问题
- LLM-MAS 已经扩展到哪些代表性应用前沿？
- 复杂任务、情景仿真与 agent evaluation 分别需要怎样的系统能力？
- 交互机制和评测协议如何限制应用外推？

### 分类框架
- 应用：complex task solving、scenario simulation、generative agent evaluation
- 系统：core components、interactions in LLM-MAS
- 方法学：comparisons with other surveys、challenges and future directions

### 核心结论
- 应用扩张速度很快，multi-agent 已不止是“协作问答”，而是逐步进入复杂任务执行与场景仿真。
- evaluation 正在成为与方法设计同等重要的研究主题。
- 应用前沿越多，越需要统一的 component / interaction 抽象与更可比的 benchmark。

### 局限性
- 侧重应用扩展，对 workflow、tool-use、communication 机制的细粒度拆分不如专题综述深入。
- 更适合回答“能做什么”，对“为什么这样设计最优”解释较弱。

### 可延展方向
- 统一 agent evaluation protocol
- 复杂任务环境中的交互鲁棒性研究
- 生成式 agent 在高真实度场景仿真中的可泛化性
- 应用驱动的 benchmark 体系重构

---

## 4) Tran et al. 2025 — Multi-Agent Collaboration Mechanisms: A Survey of LLMs

- 年份：2025
- 来源页面：`https://arxiv.org/abs/2501.06322v1`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf`

### 摘要
该综述专门讨论多个 LLM agent 如何协作，试图把 collaboration 从经验性设计提升为系统化 taxonomy。文章围绕 actor、合作/竞争/竞合关系、通信结构、协作策略与协调协议，提出人工集体智能视角下的多 agent 协作框架。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 4 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 4。

### 研究问题
- 多 LLM agent 的协作机制可以如何被系统分类？
- cooperation / competition / coopetition 与结构拓扑如何影响协作效果？
- 多 agent 系统怎样迈向人工集体智能？

### 分类框架
- actors
- relation types：合作 / 竞争 / 竞合
- communication structures：点对点 / 中心化 / 分布式
- collaboration strategies
- coordination and orchestration protocols
- evaluation / benchmarking / ethics

### 核心结论
- 多智能体收益主要来自关系设计、结构设计与协议设计，而不是简单增加 agent 数量。
- 协作机制需要被当成独立研究对象，而非 prompt engineering 的副产品。
- 如果缺少统一 benchmarking 与安全/伦理约束，协作系统很难稳定走向可扩展集体智能。

### 局限性
- 重点在 collaboration taxonomy，对 tool-use、workflow、memory 等工程议题讨论较少。
- 数据集/benchmark 部分需要与其他综述联合看，单篇不足以覆盖系统工程全栈。

### 可延展方向
- 协作结构与收益的因果分析
- 通信协议与协作质量的联合建模
- 集体智能 benchmark 标准化
- 面向安全/伦理的协作治理机制

---

## 5) Wu et al. 2025 — Multi-Agent Autonomous Driving Systems with Large Language Models

- 年份：2025
- 来源页面：`https://arxiv.org/abs/2502.16804v2`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf`

### 摘要
该综述将 multi-agent + LLM 技术放入自动驾驶场景，讨论多车、多基础设施、多助手与人机交互如何构成协同驾驶系统。文章从交互对象、协同感知/决策/部署等视角总结 recent advances，并强调该领域面临高实时性与高安全性约束。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 5 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 5。

### 研究问题
- 在自动驾驶中，多 agent LLM 系统相较单 agent 能解决哪些限制？
- 多车、车路、车助理、人与 agent 之间的交互如何组织？
- 高风险实时场景对多智能体系统提出了哪些特殊要求？

### 分类框架
- 交互对象：vehicle-vehicle、vehicle-infrastructure、vehicle-assistant、agent-human
- 功能任务：collaborative perception、decision-making、cloud-edge deployment、assistance-tools
- 对比视角：single-agent ADS vs multi-agent ADS

### 核心结论
- 自动驾驶提供了 multi-agent 技术进入真实高约束系统的典型试验场。
- 语言驱动通信和协调可统一多车/多主体协作，但前提是满足时延、安全与可靠性要求。
- 垂直场景中的部署、感知与协同问题，会反向推动通用 multi-agent 研究关注现实约束。

### 局限性
- 领域专用性强，不能直接代表通用 multi-agent 系统的全貌。
- 系统落地难度高，许多结论受特定感知、硬件、法规条件限制。

### 可延展方向
- 高风险场景下的通信压缩与优先级调度
- 车路协同中的可解释决策与责任归因
- cloud-edge 多 agent 实时编排
- 面向真实交通场景的统一 benchmark 与安全协议

---

## 6) Yan et al. 2025 — Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems

- 年份：2025
- 来源页面：`https://arxiv.org/abs/2502.14321v2`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf`

### 摘要
该文提出 communication-centric 视角，认为 communication 不是 LLM-MAS 的附属细节，而是决定系统协同质量的中心变量。作者把通信拆成 system-level communication 与 system-internal communication 两层，并进一步整理 architecture、goal、protocol、strategy、object、content 等子维度。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 6 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 6。

### 研究问题
- communication 为什么应被提升为 LLM-MAS 的核心研究对象？
- system-level 与 internal communication 如何共同影响系统能力？
- 当前 communication design 面临哪些安全、效率与可扩展性问题？

### 分类框架
- system-level communication：architecture、goals、protocols
- system-internal communication：strategies、paradigms、objects、content
- evaluation：benchmarks and evaluation
- outlook：opportunities and challenges

### 核心结论
- 多智能体性能不只由 individual agent quality 决定，通信设计是关键杠杆。
- 通信问题可被拆解为稳定的设计空间，而不再只是 ad hoc 提示词技巧。
- benchmark、协议、安全与效率，构成 communication research 的四个长期瓶颈。

### 局限性
- 视角聚焦通信，对 workflow、tool-use、memory 等其他变量展开不足。
- 更适合作为 communication 方向主综述，而不是全景总入口。

### 可延展方向
- 多模态通信协议
- 消息有效率、冗余率与恢复时延的量化评测
- 通信安全与攻击面治理
- communication cost-aware optimization

---

## 7) Xu et al. 2026 — The Evolution of Tool Use in LLM Agents

- 年份：2026
- 来源页面：`https://arxiv.org/abs/2603.22862v1`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf`

### 摘要
该综述讨论 LLM agent 的 tool use 如何从单次函数调用演化为多工具、长轨迹、受约束的 orchestration 问题。文章从 planning & execution、trajectory construction、safety & control、resource efficiency、open-environment completeness 与 benchmark design 等角度，对 multi-tool agent 系统的核心挑战进行系统总结。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 7 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 7；survey 身份证据见 `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-list-with-cn-abstract-entry.md`。

### 研究问题
- tool use 的研究重点为何从“会不会调用”转向“能否可靠编排多个工具”？
- 长程、多工具 agent 的主要失败模式是什么？
- 工业级 runtime 如何同时保证性能、预算、安全与治理？

### 分类框架
- inference-time planning and execution
- training and trajectory construction
- safety and control
- efficiency under resource constraints
- capability completeness in open environments
- benchmark design and evaluation

### 核心结论
- 真正困难的问题不是单工具调用，而是多工具长轨迹编排的稳定性与治理性。
- tool-use 已成为 agent system 工程化的核心议题之一。
- benchmark 正在从通用问答/代码任务，转向更接近真实环境与长任务链的 agent benchmarks。

### 局限性
- 重点在 tool orchestration，不是纯 communication / collaboration survey。
- 社会性互动、role-play、多 agent 关系建模不是其主线。

### 可延展方向
- 开放环境中的自动工具发现与扩展
- 预算感知的长程规划与执行控制
- 并行执行下的安全与责任归因
- 多工具 agent 的统一评测协议

---

## 8) Yue et al. 2026 — From Static Templates to Dynamic Runtime Graphs

- 年份：2026
- 来源页面：`https://arxiv.org/abs/2603.22386v1`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf`

### 摘要
该文把 LLM agents 的 workflow 研究抽象为从静态模板走向动态 runtime graph 的演化过程，提出 agentic computation graphs 的视角，并系统梳理 workflow 结构何时确定、优化哪个部分、由哪些 evaluation signal 驱动。它将 selection/pruning、pre-execution generation、in-execution editing 等策略纳入统一框架。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 8 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 8；survey 身份证据见 `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-list-with-cn-abstract-entry.md`。

### 研究问题
- workflow 的结构是在设计时静态给定，还是运行时动态生成/编辑更优？
- workflow optimization 到底在优化什么对象？
- verifier、cost、robustness 等信号如何进入优化闭环？

### 分类框架
- 结构确定时机：static vs dynamic
- 优化对象：workflow 的哪一部分被优化
- 评价信号：哪些 signals guide optimization
- 动态策略：selection/pruning、pre-execution generation、in-execution editing
- 抽象：agentic computation graphs (ACGs)

### 核心结论
- agent workflow 不应只被看作 prompt template，而应被视为可优化、可编辑的计算图。
- runtime graph 的设计与反馈闭环，是提升 agent 系统稳定性与效率的关键。
- graph-level evaluation 可能比单点任务分数更能解释系统优劣。

### 局限性
- 更偏 workflow engineering，对通信协议与社会性互动讨论较少。
- 抽象层较高，需结合具体系统论文才能直接落地实现细节。

### 可延展方向
- 图级质量评测与 verifier 设计
- 动态工作流编辑与自优化 runtime
- communication / tool-use / workflow 联合优化
- 在真实长任务环境中验证 ACG 抽象的外部有效性

---

## 9) Chen et al. 2026 — The Five Ws of Multi-Agent Communication

- 年份：2026
- 来源页面：`https://arxiv.org/abs/2602.11583v1`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf`

### 摘要
该综述尝试用 5W（Who、Whom、When、What、Why）统一多智能体通信研究，把传统 MARL、emergent language 与 LLM-powered multi-agent communication 放在同一分析框架内。文章同时强调综述方法学、纳排标准与时间范围，是一篇兼具理论与综述规范性的 communication 主线论文。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 9 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 9。

### 研究问题
- 如何以统一框架连接不同范式下的多智能体通信研究？
- “谁对谁说、什么时候说、说什么、为什么说”能否成为稳定的通信分析模板？
- 旧范式（MARL、emergent language）与新范式（LLM agents）之间有哪些可迁移知识？

### 分类框架
- 5W：Who / Whom / When / What / Why
- 历史脉络：MARL communication、emergent language、LLM-powered communication
- 方法学：search strategy、temporal scope、inclusion / exclusion criteria

### 核心结论
- 5W 框架足以覆盖跨范式通信研究的核心问题，是非常强的统一模板。
- 多智能体通信研究不应被割裂在不同社群里，旧理论与新系统可以相互借鉴。
- communication 研究需要更强的跨范式 benchmark 与更明确的方法学标准。

### 局限性
- 主要聚焦 communication，对 memory、tool orchestration、workflow 并不做全景覆盖。
- 理论整合价值很高，但若要直接指导工程落地，仍需搭配系统综述阅读。

### 可延展方向
- 5W 驱动的统一 benchmark 设计
- LLM-grounded MARL / emergent communication 融合研究
- 开放环境下 communication 的可解释性与效率权衡
- communication 与 workflow / planning 的耦合建模

---

## 10) Wang et al. 2026 — Role-Playing Agents Driven by Large Language Models

- 年份：2026
- 来源页面：`https://arxiv.org/abs/2601.10122v1`
- 本地 PDF：`projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf`

### 摘要
该综述关注 role-playing language agents 的现状、挑战与未来趋势，系统整理了人格设定、角色记忆、行为决策建模、角色数据构建与评测方法等技术模块。它把 social / narrative multi-agent 系统作为一个独立分支，强调人格一致性、长期互动与沉浸式交互的重要性。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 第 10 节；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 卡片 10；survey 身份证据见 `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-list-with-cn-abstract-entry.md`。

### 研究问题
- role-playing agents 的关键技术模块是什么？
- 人格、记忆与动机如何共同决定长期互动与社会行为？
- social agent 的评测体系应如何设计？

### 分类框架
- research paradigm evolution
- core technologies of role-playing modeling
- role-specific data construction and annotation
- evaluation methods and metrics
- future outlook and trends

### 核心结论
- role-playing agent 已从简单角色模板，演化为人格、记忆、行为决策联合建模的问题。
- social multi-agent systems 需要专门的数据构建与评测协议，不能完全沿用任务型 agent 评测。
- personality fidelity、alignment 与长期一致性是该分支的核心指标。

### 局限性
- 对通用任务协作、tool-use、workflow 优化覆盖有限。
- 更适合 social / simulation / companion agents 场景，不宜直接外推到所有 MAS。

### 可延展方向
- 人格演化建模与长期记忆稳定性
- 多 agent collaborative narrative
- 多模态沉浸式交互
- 与认知科学 / 神经科学结合的 social agent 建模

---

## 横向总结：供后续中文 Markdown 直接复用的 6 个共识

1. **从总览到专题化**：2024 更偏全景地图；2025-2026 则快速细化到 communication、collaboration、tool-use、workflow、role-play。  
   Provenance: `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 第 4 节；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`。
2. **通信是主轴变量**：Yan 2025 与 Chen 2026 都表明 communication 已从实现细节升级为系统设计中心。  
   Provenance: 同上。
3. **工程系统化增强**：Aratchige 2025、Xu 2026、Yue 2026 共同说明，多智能体研究正快速靠近 runtime、workflow、tool orchestration 与治理。  
   Provenance: 同上。
4. **benchmark 碎片化明显**：不同专题各有 benchmark，横向可比性不足。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 各篇 benchmark 条目；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 第 5 节。
5. **真实约束正在压过单纯分数**：安全、预算、时延、可治理性成为共同关键词。  
   Provenance: Xu 2026、Yue 2026、Wu 2025 条目。
6. **social agents 是新分支**：Wang 2026 说明 multi-agent 已从任务协作扩展到社会交互与叙事系统。  
   Provenance: Wang 2026 条目。

## 直接用途

本文件可以直接作为后续两个交付的输入：

1. `ten_multi_agent_surveys_cn.md` 的逐篇精读卡片补强版
2. 后续新的中文汇报/答辩稿中的“逐篇结构化摘要”附录

若后续要继续扩展字段，建议优先补：
- 逐篇 benchmark 明细表
- 逐篇 survey evidence sentence 原文摘录
- 逐篇与本仓库 multi-agent 系统的映射启发
