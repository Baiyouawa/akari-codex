# 2026-03-26 十篇 multi-agent 综述结构化中文精读笔记

- Timestamp: 2026-03-26T00:16:17+08:00
- Session: 结衣-03-1774454544-65f537
- Scope: 对项目内已落盘且可溯源的 10 篇 multi-agent / LLM agents 综述进行结构化中文笔记整理。

## 方法与证据边界

本笔记只使用以下两类可追溯来源，不凭空补写未验证内容：

1. **来源页面摘要**：各论文的 arXiv / Springer 页面摘要文本。
2. **本地源码结构证据**：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中记录的 section heading、abstract 与 dataset_hits；该 JSON 由下载的 arXiv TeX 源码抽取生成，来源文件位于 `projects/multi-agent-review-survey/sources/*.tar.gz`。

因此，下文中的“分类框架”主要依据摘要与目录标题；“数据集/基准”优先来自源码中出现的 benchmark 名称；“优缺点/未来方向”只总结作者明确讨论的挑战、limitations、future directions 或可由目录结构直接支持的判断。

---

## 1. Guo et al. 2024 — Large Language Model based Multi-Agents: A Survey of Progress and Challenges

- 年份：2024
- 本地 PDF：`projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf`
- 来源页面：`https://arxiv.org/abs/2402.01680`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2402.01680`

### 研究问题
- 如何系统梳理 **LLM-based multi-agent systems** 的关键组成、典型应用与主要挑战。
- 作者在摘要中明确提出三个核心问题：这些系统模拟哪些领域/环境、agent 如何被 profile 与 communication、agent 能力如何增长。

### 分类框架
- 从源码 section 可见，作者将框架拆成：`Agents-Environment Interface`、`Agents Profiling`、`Agent Management`、`Agents Communication`、`Training Scheme`、`Multi-Agents Orchestration and Efficiency`。
- 应用层面又分为：`LLM-MA for Problem Solving`、`LLM-MA for World Simulation`、`Dialogue Dataset Generation`。
- 因此该综述本质上是 **系统组件 + 应用场景 + 挑战/资源** 的三层分类法。

### 核心方法/核心观点
- 不是提出单一算法，而是给出 LLM 多智能体系统的统一拆解视角：接口、角色设定、通信、能力获取、编排效率。
- 该文把单 agent 与 multi-agent 对比、强化学习多智能体脉络、以及实现工具与资源放在同一综述中，起到“入门总图谱”作用。

### 数据集/基准
- 源码抽取得到的 benchmark 名称包括：`GSM8K`、`HumanEval`、`MMLU`、`BIG-bench`、`ChatArena`、`RoCoBench`、`CAMEL`、`AVALONBENCH`。
- 结论：该文覆盖的问题求解、代码、博弈/对话与协作评测较广，但 benchmark 呈混合型，不局限单一任务域。

### 优点
- 覆盖面广，适合作为 LLM-based MAS 的基线综述。
- 有独立的 `Datasets and Benchmarks` 与 `Implementation Tools and Resources` 章节，对后续实验落地价值高。
- 同时讨论 problem solving 与 world simulation，使其不只停留在框架分类。

### 局限
- 2024 年时点较早，后续 2025-2026 的 workflow optimization、tool orchestration、communication-specific 综述尚未被充分纳入。
- 目录显示分类较广，意味着对某些专门议题的深度可能不如后来的垂直综述。

### 未来方向
- 作者目录中明确讨论 `Challenges and Opportunities`、`Ethicals and Risks`、`Scaling law of the Multi-Agents`。
- 可归纳的未来方向是：多模态环境、通信可靠性/幻觉控制、规模化编排规律、可复现实验基准。

---

## 2. Aratchige & Ilmini 2025 — LLMs Working in Harmony

- 年份：2025
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf`
- 来源页面：`https://arxiv.org/abs/2504.01963`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2504.01963`

### 研究问题
- 多智能体 LLM 系统在协作动态环境中，**怎样的技术栈最关键、最影响效果**？
- 作者把问题收敛到四个关键技术面：Architecture、Memory、Planning、Technologies/Frameworks。

### 分类框架
- 目录结构直接对应四个核心维度：`Architecture`、`Planning`、`Memory`、`Technologies / Frameworks`。
- 这种分类方式偏“工程搭建视角”，更适合系统构建者而不是应用分类读者。

### 核心方法/核心观点
- 摘要强调 Mixture of Agents 架构、ReAct 规划模型等代表性思路。
- 文章核心不是罗列应用，而是提炼 **构建高效 LLM-MAS 的底层技术基建**。
- 与 Guo 2024 相比，这篇更强调系统搭建技术，而不是宏观领域地图。

### 数据集/基准
- 源码抽取命中：`ALFWorld`、`HotpotQA`、`HumanEval`、`MATH`、`MT-Bench`、`AlpacaEval`、`CAMEL`、`AutoGen`。
- 可见其评测覆盖推理、代码、交互环境、对话评测四类典型任务。

### 优点
- 聚焦技术底座，适合研发者快速把握多智能体系统的关键设计位点。
- 将 memory 与 planning 单列，说明作者关注长程任务与协作效率，而非只做静态架构分类。
- `Future Directions` 单独成章，便于提炼研究空白。

### 局限
- 作者只有两位，且摘要更偏技术梳理与 recommendations，应用面覆盖可能不如大型综述全面。
- 源码目录较短，说明文章结构更凝练，但也可能意味着 benchmark 与案例覆盖相对有限。

### 未来方向
- 摘要明确点出 scalability、real-time response、agent coordination constraints。
- 对应未来方向：大规模协作扩展、实时多 agent 响应、记忆/规划一体化、框架层标准化。

---

## 3. Chen et al. 2025 — A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application

- 年份：2025
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf`
- 来源页面：`https://arxiv.org/abs/2412.17481`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2412.17481`

### 研究问题
- 随着新工作快速增长，已有综述难以完整覆盖，因而作者试图更新 **LLM-MAS 的应用前沿与新边界**。
- 重点不是单纯框架拆解，而是：多生成式 agent 系统能在哪些场景发挥作用。

### 分类框架
- 文章按应用场景组织：`solving complex tasks`、`simulating specific scenarios`、`evaluating generative agents`。
- 同时补充 `Core Components of LLM-MAS`、`Interactions in LLM-MAS`、`Challenges and Future Directions`。
- 因而这是 **应用前沿分类 + 核心组件补充** 的结构。

### 核心方法/核心观点
- 该综述把 LLM-MAS 看作多 generative agents 系统，关注交互、环境、评估三者联动。
- 与偏框架/通信的综述不同，它更强调“系统被拿来做什么”，特别是复杂任务、仿真与 agent evaluation。

### 数据集/基准
- 结构抽取中出现：`AgentBench`、`AGENTBENCH`、`AUCARENA`、`EvalPlus`、`GSM8K`、`HotpotQA`、`HumanEval`、`MATH`、`MMLU`、`MT-Bench`、`MLAgentBench`、`ToolBench`、`LLMArena`、`ChatEval`。
- 说明该文 benchmark 维度比较丰富，既含任务能力评测，也含 agent system 评测。

### 优点
- 对应用边界和评测前沿的覆盖较全面。
- 同时列出 `Comparisons with other surveys`，便于定位与同类综述的差异。
- 适合做后续“应用导向的 research idea”输入。

### 局限
- 摘要中对统一技术分类的展开不如技术向综述细。
- 以应用为主时，底层 orchestration / workflow 优化问题可能讨论不够深。

### 未来方向
- 目录直接列出 `Challenges posed by generative agents`、`Challenges posed by interactions`、`Challenges of Evaluating for LLM-MAS`。
- 可见未来重点在：交互鲁棒性、agent 评测协议、面向场景仿真的真实性与可泛化性。

---

## 4. Tran et al. 2025 — Multi-Agent Collaboration Mechanisms: A Survey of LLMs

- 年份：2025
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf`
- 来源页面：`https://arxiv.org/abs/2501.06322`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2501.06322`

### 研究问题
- 多个 LLM agent 协作时，**合作机制到底如何组织**，哪些机制决定集体智能质量。
- 目标是把 collaboration 从“现象”抽象成可扩展框架。

### 分类框架
- 摘要给出的主框架包括：`actors`、`types`（合作/竞争/竞合）、`structures`（点对点/中心化/分布式）、`strategies`、`coordination protocols`。
- 目录也包含：`Collaboration Types`、`Collaboration Strategies`、`Communication Structures`、`Coordination and Orchestration`。
- 这是一篇非常典型的 **协作机制 taxonomy** 综述。

### 核心方法/核心观点
- 文章强调多智能体协作不只是多角色分工，还包括合作关系类型、结构设计与协议层协调。
- 其价值在于把 collaborative AI 的“横向扩展”讲清楚，适合研究 collective intelligence。

### 数据集/基准
- 自动抽取命中较杂，但可确认其评估维度包含 `LLMARENA`、`CAMEL`、`AutoGen`，以及作者明确讨论的 `Comprehensive Evaluation and Benchmarking` 章节。
- 摘要还点出应用域：`5G/6G`、`Industry 5.0`、`QA/NLG`、`social and cultural settings`。

### 优点
- 对 collaboration 机制的结构化程度高。
- 将 cooperation / competition / coopetition 并列，有助于研究多 agent 非单一协同关系。
- 直接面向“人工集体智能”目标，研究愿景清晰。

### 局限
- benchmark 抽取中含较多模板噪声，表明文档工程内容较多，数据集部分需要二次人工清洗。
- 文章更强调协作机制本身，对 tool-use、workflow、memory 等纵深主题覆盖不一定充分。

### 未来方向
- 目录与摘要都明确提到：`Comprehensive Evaluation and Benchmarking`、`Ethical Risk and Safety`、`The Road to Artificial Collective Intelligence`。
- 因而未来方向集中在：统一协作评测、合作安全/伦理、从局部协同走向可扩展集体智能。

---

## 5. Wu et al. 2025 — Multi-Agent Autonomous Driving Systems with Large Language Models

- 年份：2025
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf`
- 来源页面：`https://arxiv.org/abs/2502.16804`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2502.16804`

### 研究问题
- 自动驾驶中，单 agent LLM 方案面临感知受限、协作不足、算力代价高，multi-agent LLM 是否能解决这些问题。
- 这是一个 **领域化综述**：聚焦 autonomous driving system (ADS)。

### 分类框架
- 核心分类围绕交互对象：`Multi-Vehicle Interaction`、`Vehicle-Infrastructure Interaction`、`Vehicle-Assistant Interaction`、`Agent-Human Interaction`。
- 还区分 `LLM-based Single-Agent ADS` 与 `LLM-based Multi-Agent ADS`。
- 应用再细分为：`Collaborative Perception`、`Collaborative Decision-Making`、`Collaborative Cloud-Edge Deployment`、`Collaborative Assistance-Tools`。

### 核心方法/核心观点
- 文章核心观点是：自动驾驶中的语言驱动 communication / coordination 能把多车、多基础设施、多角色协作统一起来。
- 这篇综述把通用 multi-agent 技术映射到高安全、高实时的垂直领域。

### 数据集/基准
- 结构抽取命中：`Waymo Open Motion Dataset`、`Multi-agent Autonomous Driving Dataset`，以及专门的 `Datasets and Benchmark` 章节。
- 因此它是十篇中少数 benchmark 指向非常清晰的领域综述。

### 优点
- 垂直场景强，便于把多智能体协作落到实际系统约束。
- 交互类型划分自然，对现实部署非常有解释力。
- 同时讨论 cloud-edge deployment，说明不只关注算法，还关心系统部署。

### 局限
- 领域专用性强，结论未必直接迁移到一般性 LLM-MAS。
- 摘要里已指出高计算开销与多主体感知问题，说明真实部署难度较大。

### 未来方向
- 目录中的 `Challenges and Future Directions` 指向：实时性、安全性、跨主体协同、人与 agent 共驾/协作接口。
- 研究上很适合延展到多车博弈、交通基础设施协同与现实 benchmark 标准化。

---

## 6. Yan et al. 2025 — Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems

- 年份：2025
- 本地 PDF：`projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf`
- 来源页面：`https://arxiv.org/abs/2502.14321`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2502.14321`

### 研究问题
- 现有综述偏应用或架构，但忽视了 **communication 在 LLM-MAS 中的中心地位**；作者试图从 communication 角度重构整个研究版图。

### 分类框架
- 摘要明确把 communication 分成两层：
  - `system-level communication`：architecture、goals、protocols
  - `system internal communication`：strategies、paradigms、objects、content
- 目录进一步对应为：`Communication Architecture`、`Communication Goal`、`Communication Protocol`、`Communication Strategy`、`Communication Paradigm`、`Communication Object`、`Communication Content`。

### 核心方法/核心观点
- 核心贡献是 communication-centric taxonomy。
- 这篇文章强调，多智能体能力不是简单由 agent 数量决定，而是由通信设计决定协调质量、谈判能力与 collective intelligence。

### 数据集/基准
- 自动抽取得到：`GAMA-Bench`、`MultiAgentBench`、`RealWorldBench`，并有专门的 `Benchmarks and Evaluation` 章节。
- 这意味着作者已意识到 communication benchmark 是该方向短板。

### 优点
- 视角鲜明，补上此前“以通信为中心”的综述空白。
- system-level 与 internal communication 的两层分法非常适合后续方法设计。
- 摘要中直接总结 strengths、limitations、security vulnerabilities、scalability issues，问题意识强。

### 局限
- 视角聚焦通信，因此 memory、workflow、tool-use 等非通信要素讨论可能被弱化。
- 对非语言/多模态通信虽有提及，但从目录看仍处于“机会与挑战”层面。

### 未来方向
- 目录与摘要共同支持的方向有：统一通信协议、多模态通信、安全性、效率提升、benchmark 完善。
- 对研究者尤其有价值的是“通信对象/内容/协议”的解耦设计空间。

---

## 7. Xu et al. 2026 — The Evolution of Tool Use in LLM Agents

- 年份：2026
- 本地 PDF：`projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf`
- 来源页面：`https://arxiv.org/abs/2603.22862`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2603.22862`

### 研究问题
- tool use 已从单次函数调用转向长程、多工具编排；综述要回答的是：**multi-tool orchestration 的关键问题和研究版图是什么**。
- 尽管标题不直接写 multi-agent systems，但内容显式涉及 multi-tool agents 与 orchestration，对 agent system 研究高度相关。

### 分类框架
- 摘要给出六个核心维度：`inference-time planning and execution`、`training and trajectory construction`、`safety and control`、`efficiency under resource constraints`、`capability completeness in open environments`、`benchmark design and evaluation`。
- 目录还包含：`Topological Planning`、`Long-Horizon Orchestration`、`Agent Self-Improvement`、`Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration`。

### 核心方法/核心观点
- 文章把 tool use 的问题定义从“会不会调用工具”升级为“能否在长轨迹中可靠编排多个工具并受约束地执行”。
- 这是对 agent system 从 toy task 走向真实生产环境的重要综述。

### 数据集/基准
- 自动抽取命中：`AgentLongBench`、`AndroidArena`、`CostBench`、`HammerBench`、`MCP-Bench`、`MTU-Bench`、`Mobile-Bench`、`OdysseyBench`、`RepoBench`、`RestBench` 等。
- 该综述明显比前几篇更强调 **长程、多工具、真实环境 benchmark**。

### 优点
- 对“工具编排”这一 2025-2026 热点问题总结非常系统。
- 同时纳入效率、安全、开放环境适应与治理，接近工业落地需求。
- benchmark 列举细，适合直接用于后续实验设计。

### 局限
- 重点在 tool orchestration，不是纯粹 multi-agent communication / collaboration survey。
- 若研究者关心 agent 社会模拟或 role-play，则覆盖不足。

### 未来方向
- 目录中的 `Autonomous tool expansion`、`Open environment adaptation`、`Security Risks in Parallel Execution`、`Long-Horizon Tool Chains` 直接给出下一步方向。
- 很适合继续做：开放世界工具发现、带预算约束的长程规划、安全可验证执行。

---

## 8. Yue et al. 2026 — From Static Templates to Dynamic Runtime Graphs

- 年份：2026
- 本地 PDF：`projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf`
- 来源页面：`https://arxiv.org/abs/2603.22386`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2603.22386`

### 研究问题
- LLM agents 的 workflow 不再是固定 prompt chain，关键问题变成：**工作流结构何时被决定、如何被优化、如何被评价**。

### 分类框架
- 摘要的核心 taxonomy 有三条轴：
  1. `when structure is determined`：静态 vs 动态
  2. `what part of the workflow is optimized`
  3. `which evaluation signals guide optimization`
- 目录又把动态优化分为：`selection/pruning`、`pre-execution generation`、`in-execution editing`。
- 这是十篇中最清晰的“结构优化视角”综述之一。

### 核心方法/核心观点
- 作者提出 `agentic computation graphs (ACGs)` 概念，把 workflow 看成图结构而非文本模板。
- 文章还区分 `template`、`realized graph`、`trace`，把设计、实际运行和轨迹反馈拆开。
- 这是对 agent engineering 极具启发性的抽象。

### 数据集/基准
- 自动抽取得到：`FlowBench`、`GAIA`、`GSM8K`、`HotpotQA`、`HumanEval`、`MATH`、`MCP-Bench`、`MCPEval`、`SOP-Bench`、`SWE-bench`、`Terminal-Bench`、`ToolBench`、`WorkflowBench`。
- benchmark 覆盖推理、代码、工具、流程执行，非常适合 workflow 研究。

### 优点
- taxonomy 清晰，且高度可操作。
- 把 graph-level properties、cost、robustness 纳入评价，超越只看 task score 的传统做法。
- 对静态模板、动态 runtime graph、verifier feedback 的关系讲得很系统。

### 局限
- 更偏 workflow engineering，对 social interaction / role-playing / communication 协议的细节覆盖较少。
- 由于关注 workflow 抽象，某些领域化案例可能只作为例子存在。

### 未来方向
- 目录直接给出 `Open Problems and Future Directions`，以及 `Where verifiers pay off most`、`When graph optimization matters more than prompt tuning`。
- 后续可重点研究：图级评测、动态结构编辑、带 verifier 的自优化 agent workflow。

---

## 9. Chen et al. 2026 — The Five Ws of Multi-Agent Communication

- 年份：2026
- 本地 PDF：`projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf`
- 来源页面：`https://arxiv.org/abs/2602.11583`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2602.11583`

### 研究问题
- 多智能体通信研究跨越 MARL、emergent language、LLM agents，但缺少统一视角；作者提出用 **5W（Who/Whom/When/What/Why）** 重构通信研究。

### 分类框架
- 论文按 5W 组织通信问题：谁通信、向谁通信、何时通信、传什么、为什么通信。
- 同时从历史演化角度连接三条脉络：`Communication in MARL`、`Emergent Language`、`LLM-Powered Multi-Agent Communication`。
- 目录还单列 `Search Strategy and Temporal Scope` 与 `Inclusion and Exclusion Criteria`，说明综述方法论更规范。

### 核心方法/核心观点
- 该文的最大价值是提供跨范式桥梁：把传统 MARL 通信、涌现语言、LLM agent communication 统一到同一问题框架中。
- 这使通信研究不再割裂，有助于借鉴旧范式的理论基础与新范式的开放语言能力。

### 数据集/基准
- 自动抽取命中：`AvalonBench`、`BattleAgentBench`、`ChatEval`、`GAIA`、`MultiAgentBench`、`RoCoBench`、`CAMEL` 等。
- 可见该文覆盖从协作/博弈到 agent benchmark 的多种通信场景。

### 优点
- 5W 框架高度通用，适合做后续研究设计模板。
- 同时有综述方法学章节，方便判断纳入边界。
- 把 LLM 通信放回更长历史脉络，而不是只看近两年热门工作。

### 局限
- 主题非常聚焦通信，因此对 memory、tool orchestration 等方面不是主线。
- 目录可见一些修订标记，说明文稿仍在快速演进中。

### 未来方向
- 目录中明确列出 `Perspectives on Future Directions`、`Discussions on Multi-agent Communications`。
- 未来方向可归纳为：更统一的 communication taxonomy、跨范式 benchmark、LLM-grounded MARL、开放环境中的通信可解释性与效率。

---

## 10. Wang et al. 2026 — Role-Playing Agents Driven by Large Language Models

- 年份：2026
- 本地 PDF：`projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf`
- 来源页面：`https://arxiv.org/abs/2601.10122`
- 本地结构来源：`projects/multi-agent-review-survey/analysis/2026-03-26-yui-arxiv-source-index.json` 中 `arxiv_id = 2601.10122`

### 研究问题
- role-playing language agents (RPLAs) 如何从模板驱动演化为人格、记忆、动机驱动的 agent 系统，以及该方向的技术难点是什么。
- 虽然不是最典型的通用 MAS survey，但其摘要明确提到 `multi-agent collaborative narrative`，与 social multi-agent 高相关。

### 分类框架
- 目录按研究演化与技术模块组织：
  - `Evolution of Research Paradigms`
  - `Core Technologies of Role-Playing Modeling`
  - `Construction and Annotation of Role-Specific Data`
  - `Evaluation Methods and Metrics`
  - `Future Outlook and Research Trends`
- 技术子模块包括：`Character Setting and Personality Modeling`、`Character Memory Mechanisms`、`Character Behavior and Decision-Making Modeling`。

### 核心方法/核心观点
- 文章把 role-playing agent 的关键技术归纳为人格建模、记忆增强 prompting、基于动机-情境的行为决策控制。
- 与其他综述相比，它更靠近“社会交互 agent / 角色智能体”这一分支。

### 数据集/基准
- 自动抽取得到：`CharacterEval`、`RoleBench`、`RoleEval`、`RoleEval-Chinese`、`RoleEval-Global`、`RMTBench`、`RVBench`。
- 该文在十篇中最强调角色知识、人格一致性、价值对齐与互动幻觉等评测。

### 优点
- 角色建模与记忆建模总结较系统，适合做 social simulation 或 companion agents 研究。
- 对数据构建、版权约束、结构化标注过程有明确讨论，工程落地价值高。
- 评测维度细，尤其关注 personality fidelity 与 alignment。

### 局限
- 相比通用 multi-agent collaboration 综述，它更偏角色扮演与人机交互场景。
- 对大规模任务协作、工具调用、workflow 优化等议题覆盖有限。

### 未来方向
- 摘要和目录明确支持的方向包括：personality evolution modeling、multi-agent collaborative narrative、multimodal immersive interaction、与 cognitive neuroscience 结合。
- 这为“社会型多智能体”研究提供了较清楚的前沿路线。

---

## 十篇综述的粗粒度观察

1. **总综述基线**：Guo 2024、Chen 2025 负责给出整体版图与应用前沿。
2. **协作/通信主线**：Tran 2025、Yan 2025、Chen 2026 把 collaboration 与 communication 拆得越来越细。
3. **工程系统主线**：Aratchige 2025、Xu 2026、Yue 2026 强调 architecture / memory / planning / workflow / tool orchestration。
4. **领域化延伸**：Wu 2025（自动驾驶）和 Wang 2026（角色扮演 agent）说明 multi-agent survey 已进入垂直场景深耕阶段。
5. **benchmark 演化**：从早期通用任务集（如 MMLU、HumanEval、GSM8K）逐渐转向 agent-specific benchmarks（如 AgentBench、GAIA、WorkflowBench、MultiAgentBench、RoleBench、MCP-Bench）。

## 与后续研究最相关的 5 个可复用问题模板

1. **通信协议问题**：何种通信对象/内容/频率最能提升协作收益，同时控制成本与安全风险？
2. **工作流优化问题**：何时该用静态模板，何时必须运行时生成/编辑图结构？
3. **工具编排问题**：多工具长轨迹执行如何同时保证预算、鲁棒性与可验证性？
4. **记忆与角色问题**：人格一致、长期记忆与协作叙事如何共同影响 agent 社会行为？
5. **评测问题**：agent-specific benchmark 如何同时覆盖任务效果、图结构质量、通信质量、成本与安全？

## 计数核验

本文件共覆盖 10 篇论文，分别对应以下 arXiv/source id：

`2402.01680`, `2504.01963`, `2412.17481`, `2501.06322`, `2502.16804`, `2502.14321`, `2603.22862`, `2603.22386`, `2602.11583`, `2601.10122`。
