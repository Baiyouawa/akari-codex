# 2026-03-26 多智能体综述中文最终报告（统一锁定样本集修正版）

## 0. 报告说明与样本集声明
本报告只覆盖以下两份文件共同锁定的 10 篇综述，不使用任何超出该样本集的论文作为逐篇详述对象：
1. `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`
2. `projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json`

本报告的跨篇判断与研究 idea 主要建立在以下仓库内证据之上：
- 样本筛选：`projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`
- 下载与本地 PDF 校验：`projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json`
- 交叉比较：`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-cross-comparison.md`
- 八字段背景笔记：`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-background-problem-framework-notes.md`
- 统一样本详读笔记：`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-detailed-reading-notes.md`

证据边界：本报告优先使用以上文件中已经落库的摘要级、章节级、结构化笔记级结论；不额外伪造页码级断言。凡无法稳定回链到这些文件的主张，不纳入正文。

### 0.1 本报告采用的 10 篇综述
| 序号 | Paper ID | 论文 | 年份 | 来源链接 |
|---|---|---|---:|---|
| 1 | `10.1007/s44336-024-00009-2` | Li et al. — *A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges* | 2024 | https://link.springer.com/article/10.1007/s44336-024-00009-2 |
| 2 | `2402.01680` | Guo et al. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* | 2024 | https://arxiv.org/abs/2402.01680 |
| 3 | `10.1007/s10458-023-09633-6` | Zhu et al. — *A survey of multi-agent deep reinforcement learning with communication* | 2024 | https://dblp.org/rec/journals/aamas/ZhuDW24 |
| 4 | `2412.17481` | Chen et al. — *A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application* | 2025 | https://arxiv.org/abs/2412.17481 |
| 5 | `2501.06322` | Tran et al. — *Multi-Agent Collaboration Mechanisms: A Survey of LLMs* | 2025 | https://arxiv.org/abs/2501.06322 |
| 6 | `2502.14321` | Yan et al. — *Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems* | 2025 | https://arxiv.org/abs/2502.14321 |
| 7 | `2502.16804` | Wu et al. — *Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances* | 2025 | https://arxiv.org/abs/2502.16804 |
| 8 | `2503.13415` | Jin et al. — *A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives* | 2025 | https://arxiv.org/abs/2503.13415 |
| 9 | `2505.21116` | Lin et al. — *Creativity in LLM-based Multi-Agent Systems: A Survey* | 2025 | https://arxiv.org/abs/2505.21116 |
| 10 | `2602.11583` | Chen et al. — *The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs* | 2026 | https://arxiv.org/abs/2602.11583 |

### 0.2 样本时间分布
按 `analysis/2026-03-26-latest-10-multi-agent-survey-selection.md` 与 manifest 可直接统计：2024 年 3 篇、2025 年 6 篇、2026 年 1 篇，总计 10 篇。

### 0.3 为什么这 10 篇值得一起读
这 10 篇不是随机拼盘，而是形成了一条清晰的研究主线：
- 通用系统框架：Li 2024、Guo 2024、Chen 2025
- 协作/通信/决策机制：Zhu 2024、Tran 2025、Yan 2025、Jin 2025、Chen 2026
- 垂直与新兴场景：Wu 2025、Lin 2025

这一组合同时覆盖 workflow、collaboration、communication、decision-making、benchmark、vertical application 与 creativity，能够支撑“逐篇详述—横向比较—后续 idea”三部分使用同一证据边界。

---

## 1. 十篇综述逐篇详述

## 1.1 Li et al. 2024
- 来源路径：selection 第 10 篇清单；manifest 对应 `paper_id=10.1007/s44336-024-00009-2`；background-notes 第 1 节；detailed-reading 第 1 节。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf`

Li 2024 是当前样本集中最适合作为总框架入口的一篇。它不按零碎方法名堆砌，而是把 LLM-based multi-agent systems 组织为一条五段工作流：profile、perception、self-action、mutual interaction、evolution。这个视角的价值在于，它天然回答“系统如何从角色定义走向感知、行动、交互与持续改进”，比单纯的应用分类更贴近系统设计逻辑。

这篇综述的核心贡献有三点。第一，它把多智能体的能力增量解释为角色化、交互化与演化闭环，而不是“多开几个 LLM 实例”。第二，它把 problem-solving 与 world simulation 确立为早期 LLM-MAS 的两大代表性应用。第三，它说明 workflow 才是整合早期多智能体文献的最好语言，这为后续 communication、benchmark、safety 等专题综述提供了母框架。

它的不足也很明显。由于时间点在 2024 年，后续 2025–2026 年出现的 communication-centric、Five Ws、creative MAS、cooperative decision-making 深化议题尚未被系统覆盖。因此，Li 2024 适合作为总图，而不应单独承担最新方向判断。若想快速把握“多智能体系统一般长什么样”，它仍然是优先级最高的起点之一。

## 1.2 Guo et al. 2024
- 来源路径：selection 第 2 篇；manifest `paper_id=2402.01680`；background-notes 第 2 节；detailed-reading 第 2 节。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf`

Guo 2024 的定位是“进展与挑战总览”。它试图回答：多智能体系统究竟在何种环境与任务中出现，agent 如何被 profile、communication 如何发生、capability growth 如何实现，以及这一切最终落到哪些应用场景与 benchmark 上。

与 Li 2024 相比，Guo 2024 的长处是把系统剖析、应用场景和实现资源连接起来。它一方面整理 interface、profiling、communication、capability acquisition，另一方面又系统汇总了 problem solving 与 world simulation，并延伸到 benchmark 和工具资源。这使它成为 2024 年阶段“从系统模块走向任务与资源”的代表性综述。

从本项目已有笔记可追溯到，这篇综述覆盖的 benchmark 面很广，包括 GSM8K、HumanEval、MMLU、BIG-bench、ChatArena、RoCoBench、CAMEL、AvalonBench 等。这恰好说明了当时社区还处在“混用通用基准与多智能体基准”的阶段。它的局限也在这里：覆盖广，但尚未形成统一实验协议。因此，它最适合用来理解“早期社区都在看哪些任务与资源”，不适合直接拿来定义今天的系统级 benchmark 标准。

## 1.3 Zhu et al. 2024
- 来源路径：selection 第 3 篇；manifest `paper_id=10.1007/s10458-023-09633-6`；background-notes 第 3 节；detailed-reading 第 3 节；cross-comparison 中 S3。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2024-zhu-et-al-a-survey-of-multi-agent-deep-reinforcement-learning-with-communication-doi-10.1007-s10458-023-09633-6.pdf`

Zhu 2024 不是 LLM 专题综述，但它是本样本集中补齐“传统多智能体通信理论根基”的关键一篇。它关注的是 MARL with communication：在 partial observability 和 non-stationarity 普遍存在的多主体决策环境中，communication 如何成为核心机制，而已有 Comm-MADRL 工作又该如何系统分类。

这篇综述最大的价值是提出了 communication 的多维分析框架，而不是简单把方法切成几类。仓库内已有笔记显示，它至少围绕 communication constraints、communicatee type、communication policy、communicated messages、message combination 等维度展开，并强调“传给谁、传什么、在什么约束下、如何学习”才是通信研究的真正问题。相比后来的 LLM 通信综述，它提供的是更底层、更可学习、更环境约束化的视角。

它的局限也很明确：不直接面向语言 agent，不覆盖角色扮演、开放式协作、工具调用等主题。因此，这篇论文在本报告中的角色不是提供 LLM-MAS 全景，而是充当后续 Yan 2025 与 Chen 2026 的理论前史，让我们看到“communication 作为研究对象”并不是 LLM 时代才突然出现的。

## 1.4 Chen et al. 2025
- 来源路径：selection 第 4 篇；manifest `paper_id=2412.17481`；background-notes 第 4 节；detailed-reading 第 4 节。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf`

Chen 2025 的切入点不是“系统怎么搭”，而是“系统已经被带到了哪些新应用前沿”。它把 LLM-MAS 组织成 solving complex tasks、simulating specific scenarios、evaluating generative agents 三大方向，由此重新画出 2025 年前后的应用版图。

它的重要性在于把 generative agents evaluation 单独拉出来。也就是说，multi-agent 不再只是问题求解器，还逐渐成为系统行为评测对象与评测主体。这是一个研究范式转换：评测开始从静态答案走向动态系统行为。从已有仓库笔记看，这篇综述还整理了 AgentBench、AUCArena、EvalPlus、MLAgentBench、ToolBench、ChatEval 等资源，代表 benchmark 已经从“借用单模型任务”过渡到“agent-specific benchmark”。

它的局限是底层专题深度不如通信或协作综述，因此如果读者更关心 protocol、memory、runtime，它需要与 Yan 2025、Tran 2025、Li 2024 合读。但若研究目标是找应用方向、理解评测对象如何从模型扩展到系统，这篇综述非常关键。

## 1.5 Tran et al. 2025
- 来源路径：selection 第 5 篇；manifest `paper_id=2501.06322`；background-notes 第 5 节；detailed-reading 第 5 节；cross-comparison 中 S5。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf`

Tran 2025 关注“协作机制”本身。它的核心问题是：多智能体的性能差异究竟多少来自模型能力，多少来自组织结构、关系类型、策略和协议设计。与很多总览型综述不同，它把 actors、types、structures、strategies、coordination protocols 作为核心 taxonomy。

这篇综述最重要的贡献，是明确把 cooperation、competition、coopetition 都纳入 multi-agent 协作的正统讨论。这意味着“协作”不再被狭义理解为大家和谐分工，而是包含竞争、竞合、博弈和协调在内的整体组织机制。对研究者而言，这一点非常重要，因为它把系统增益从“多副本投票”转移到“结构与协议设计”上。

它的短板在于对 memory、tool-use、workflow engineering 着墨不足，benchmark 更多作为场景比较背景，而不是统一实验协议。但若研究目标是理解“多 agent 为什么强、结构该如何选、协议该如何设计”，Tran 2025 是十篇里最强的协作机制论文之一。

## 1.6 Yan et al. 2025
- 来源路径：selection 第 6 篇；manifest `paper_id=2502.14321`；background-notes 第 6 节；detailed-reading 第 6 节；cross-comparison 中 S6。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf`

Yan 2025 的核心判断很鲜明：过去很多综述把 communication 当作模块，而它主张 communication 是系统级中心变量。为此，它建立了 system-level communication 与 system-internal communication 的双层框架，把 architecture、goals、protocols 与 strategies、paradigms、objects、content 统一到一个通信视角中。

这篇综述的最大价值，是把 communication efficiency、security、benchmarking、scalability 看成同一类根问题的不同表面。也就是说，消息该怎么发、发给谁、发多少、是否安全、能否扩展，并不是分散的工程问题，而是同一通信设计空间中的联动变量。从本项目已有交叉比较可见，它与 Chen 2026 一起构成了当前样本集中最强的 communication 主线。

它的局限则是：为了强调 communication，会弱化 memory、tool-use、workflow graph 等其他系统变量。因此它不是完整工程手册，但对任何涉及辩论、互评、协商、共享上下文和多角色互动的研究来说，这篇综述都应被优先阅读。

## 1.7 Wu et al. 2025
- 来源路径：selection 第 7 篇；manifest `paper_id=2502.16804`；background-notes 第 7 节；detailed-reading 第 7 节；cross-comparison 中 S7。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf`

Wu 2025 把 multi-agent 带入自动驾驶这个高风险、强实时、强约束场景。它指出单 agent 自动驾驶在 perception、collaboration、computational demands 上存在明显瓶颈，而多 agent + LLM 的组合可能通过车-车、车-路、车-助手、agent-human 的协作缓解这些问题。

这篇综述的独特价值，不只是“自动驾驶是个应用”，而是它迫使研究者正视真实世界部署约束。与很多通用 benchmark 不同，自动驾驶需要同时考虑安全性、实时性、责任边界和云边协同。仓库内已有笔记也表明，这篇综述关注 collaborative perception、collaborative decision-making、cloud-edge deployment 与对应数据集/benchmark，如 INTERACTION、Waymo Open Motion Dataset 等。

它的不足是通用性较弱，很多结论强依赖自动驾驶背景；但也正因为如此，它成为观察 multi-agent 能否从 demo 走向真实部署的关键样本。对未来高风险场景研究，它提供了非常实用的问题模板。

## 1.8 Jin et al. 2025
- 来源路径：selection 第 8 篇；manifest `paper_id=2503.13415`；background-notes 第 8 节；detailed-reading 第 8 节；cross-comparison 中 S8。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-misc-a-comprehensive-survey-on-multi-agent-cooperative-decision-making-scenarios-approaches-challenges-and-perspectives-arxiv-2503.13415.pdf`

Jin 2025 把多智能体 cooperative decision-making 放到一条更长的谱系里看。它不仅讨论 LLM reasoning-based methods，也系统整理 rule-based、game theory-based、evolutionary algorithms-based、deep MARL-based 方法，并把 task formats、reward allocation、simulation environments 一起纳入框架。

这篇综述的重要性，在于它把“环境、奖励、任务格式、算法方法”视为不可分割的联合设计问题，而不是单独优化某个算法。对理解传统 MAS、MARL 与 LLM-MAS 的连续性尤其关键。从本项目交叉比较文件可见，它正是连接传统决策范式与新型 agentic methods 的桥梁样本。

局限在于覆盖过广，单个方法簇的纵深有限，尤其 LLM reasoning 部分因时间较新而展开不如 MARL 深。但它为后续研究提供了很强的谱系感：今天的 LLM-MAS 决策问题，并不是凭空出现的，而是长期 cooperative decision-making 研究的延续。

## 1.9 Lin et al. 2025
- 来源路径：selection 第 9 篇；manifest `paper_id=2505.21116`；background-notes 第 9 节；detailed-reading 第 9 节；cross-comparison 中 S9。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf`

Lin 2025 的特别之处在于，它不再追问多 agent 是否能“做对”，而是追问多 agent 是否能“做新”“做得有风格”“做得更有创造力”。它围绕 workflow and proactivity、creative techniques、persona/profile、evaluation 与 datasets 构建了第一篇 creativity in MAS 的专题综述。

这篇综述的核心贡献，是把 divergent exploration、iterative refinement、collaborative synthesis 等技术与 persona、proactivity 放在一起讨论，说明创意系统的性能来源不仅是生成模型强不强，更是角色设定和协作过程如何组织。与此同时，它也非常清楚地指出 creative MAS 的真正难点在 evaluation inconsistency、bias mitigation、coordination conflict 和缺少 unified benchmarks。

因此，Lin 2025 对本项目的意义不只是补充一个“有趣应用”，而是在方法论上提醒我们：开放式任务不能再沿用封闭任务的单一分数逻辑。未来教育、陪伴、角色扮演、协同设计等任务，都可以从这篇综述获得重要启发。

## 1.10 Chen et al. 2026
- 来源路径：selection 第 10 篇；manifest `paper_id=2602.11583`；background-notes 第 10 节；detailed-reading 第 10 节；cross-comparison 中 S10。
- 本地 PDF：`projects/multi-agent-survey-review/literature/pdf/2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf`

Chen 2026 是当前样本集中最强的统一理论论文之一。它意识到 multi-agent communication 研究分散在 MARL、emergent language、LLM-based communication 三条传统中，术语和评测口径都不统一，因此提出用 Who、Whom、When、What、Why 这五个问题重构整个领域。

Five Ws 的价值在于，它既足够抽象，可以横跨三条范式；又足够具体，可以直接转化为系统问题拆解：谁在通信、与谁通信、何时通信、通信内容是什么、为什么通信。它让 communication 不再只是一个“加消息”的工程技巧，而成为可系统研究、可跨范式比较的对象。仓库内交叉比较文件也明确把它定位为“跨范式统一理论 + 通信机制”的代表作。

它的局限是高度聚焦通信，不覆盖完整系统工程。但若目标是设计统一的 communication benchmark、连接传统 MARL 与 LLM-MAS、解释协议设计的核心维度，Chen 2026 是最关键的读物之一。

---

## 2. 跨综述对比分析

## 2.1 一个清晰的时间演化：从“系统是什么”到“系统为什么有效”再到“系统如何可信落地”
基于 `ten-survey-cross-comparison.md` 第 7 节与 background-notes 的逐篇总结，可以把这 10 篇综述的演化分成三段。

第一段是 2024 年的通用框架阶段，以 Li 2024 和 Guo 2024 为代表。核心问题是：LLM-based MAS 是什么、由哪些模块组成、有哪些应用和挑战。这个阶段的关键特征是建立基本词汇表与总框架。

第二段是 2025 年的专题深化阶段，以 Tran 2025、Yan 2025、Jin 2025、Wu 2025、Lin 2025 为代表。这里的重点不再是泛泛描述系统，而是开始问：协作为什么有效、通信为什么关键、决策如何组织、垂直场景怎么落地、创造性任务如何评测。

第三段是 2026 年初出现的统一理论阶段，以 Chen 2026 为代表。此时研究开始试图打通 MARL、emergent language 与 LLM-MAS 三条传统，寻找跨范式最小公共语言。换言之，领域开始从“多样化探索”转向“统一理解与可比性建设”。

## 2.2 当前最强共识：通信、组织设计与系统级评测的重要性
从 `ten-survey-cross-comparison.md` 第 3、5、7 节可直接读出三条强共识。

第一，communication 是十篇样本中最强的交叉主题。高强度覆盖它的至少包括 Zhu 2024、Tran 2025、Yan 2025、Wu 2025、Chen 2026，Guo 2024 和 Li 2024 也有重要涉及。也就是说，通信早已不是附属变量，而是系统能力与代价的决定性因素。

第二，多 agent 的价值不再被解释为“数量堆叠”，而被解释为组织结构、角色分工、协议设计与反馈闭环。Li 2024 的 workflow、Tran 2025 的 collaboration taxonomy、Yan 2025 的 communication taxonomy、Chen 2026 的 Five Ws，都指向同一个结论：真正有用的是组织设计，而非实例数。

第三，benchmark 已经明显从静态任务分数转向系统行为评测。Chen 2025、Yan 2025、Wu 2025、Lin 2025 都强调评测对象不再只是最后答案，而是交互轨迹、通信效率、场景真实性、创造性与风险约束。这意味着“系统级评测”正在替代“单题分数”。

## 2.3 当前最主要分歧：multi-agent 到底该按什么方式分类
这 10 篇综述并没有给出统一 taxonomy，反而凸显了多个强竞争视角。

- Li 2024 用 workflow 划分。
- Guo 2024 用组件—应用—资源三层总览。
- Chen 2025 用应用前沿三分法。
- Tran 2025 用协作结构与协议划分。
- Yan 2025 和 Chen 2026 用 communication 视角重组。
- Jin 2025 用决策方法与环境双轴分类。
- Lin 2025 则按 creativity workflow 与 evaluation 组织。

这并不意味着谁错了，而是说明领域仍处在“多轴并存”的阶段。换句话说，今天做综述或做系统时，如果不先声明自己的分类轴，很容易在讨论中发生口径漂移。本项目此前出现的样本集漂移，本质上也提醒我们：分类轴和样本边界必须先锁定。

## 2.4 benchmark 脉络：从通用基准借用，走向专项系统 benchmark
结合 `ten-survey-cross-comparison.md` 第 5 节与各篇详细笔记，可以把 benchmark 发展看成三步。

第一步，2024 年阶段大量借用单模型或通用任务 benchmark，例如 GSM8K、HumanEval、MMLU 等，用于粗略说明多 agent 是否优于单 agent。这在 Guo 2024 中最明显。

第二步，开始出现交互与协作导向 benchmark，如 ChatArena、RoCoBench、CAMEL、MultiAgentBench 等，用于测试讨论、博弈、合作、对抗和社会交互。这一阶段对应 Chen 2025、Yan 2025 等。

第三步，垂直与开放式任务进入主舞台，例如 Wu 2025 的自动驾驶数据集/benchmark、Lin 2025 的 creative task datasets，以及 Chen 2026 所强调的跨范式 communication evaluation。到这一步，benchmark 已经不只是“测结果”，而是“测系统在特定约束下怎样完成过程”。

## 2.5 当前最值得重视的真实研究空白
根据 `ten-survey-cross-comparison.md` 第 6 节，可明确区分几类真实空白，而不是把单篇没写到的内容误判为空白。

第一，缺统一系统级 benchmark。S4、S6、S9、S10 都以不同方式指向这个问题：质量、成本、通信效率、安全、对齐与创造性尚未被一个统一协议整合起来。

第二，communication 研究与 workflow / engineering 研究仍然割裂。Li 2024、Guo 2024、Chen 2025 更偏 workflow 与应用；Yan 2025、Chen 2026 更偏 communication；两类工作之间还缺统一 runtime 语言。

第三，高风险场景部署与治理不足。Wu 2025 强调自动驾驶部署约束，Yan 2025 强调 security/scalability，Jin 2025 强调现实协同挑战。这表明真实世界落地仍是系统性短板。

第四，creative/open-ended task 的评测标准不稳定。Lin 2025 对此给出了最清晰的批评，这个问题未来不仅属于创造性任务，也会影响教育、陪伴、社会模拟等开放问题。

---

## 3. 五个后续可做的 research idea

## 3.1 Idea 1：统一 multi-agent 系统级评测协议
### Motivation
根据 cross-comparison 第 5、6 节，当前 benchmark 碎片化是跨样本最稳定的共识性问题：通用能力、交互、通信、垂直场景、创造性与安全治理彼此割裂。

### 问题定义
能否构建一个统一评测协议，同时衡量任务完成质量、通信效率、协作稳定性、成本、风险与对齐表现，使不同 multi-agent 结构可以在同一框架下比较。

### 方法设计
1. 以 `ten-survey-cross-comparison.md` 第 5 节的 benchmark 族群为基础，构建统一指标层：quality / cost / communication / coordination / safety / alignment。
2. 选取典型结构：中心化、分布式、层级式、讨论式，映射自 Tran 2025 与 Yan 2025 的 taxonomy。
3. 使用标准事件日志格式记录消息数、token 消耗、工具调用、失败模式与升级路径。
4. 在通用任务、通信任务、自动驾驶仿真任务、创意任务上做统一比较。

### 预期贡献
- 把多篇综述反复提到的“benchmark 缺失”问题转化为可执行协议。
- 提供跨论文、跨框架、跨任务的基线比较方式。
- 为后续治理和部署研究提供统一测量接口。

### 潜在风险
- 指标太多会增加评测成本。
- 不同任务对指标权重差异大，统一性与灵活性难平衡。
- 需要较强工程基础设施支持日志采集与分析。

## 3.2 Idea 2：通信感知的动态工作流优化
### Motivation
Li 2024 提供 workflow 主轴，Yan 2025 与 Chen 2026 提供 communication 主轴，但二者在现有研究中仍割裂。cross-comparison 第 6 节也把这一点列为真实研究空白。

### 问题定义
在多 agent 长程任务中，能否把 communication 的 5W 维度显式写入 workflow/runtime，使“谁在何时、与谁、传什么、为何传”成为动态优化对象，而不是固定 prompt 设计。

### 方法设计
1. 把 multi-agent 执行过程建模成动态图：节点是 agent/tool/subtask，边是消息或控制流。
2. 用 Chen 2026 的 Five Ws 作为边属性，用 Li 2024 的 workflow 段作为阶段约束。
3. 在每轮执行后利用 verifier 或成本约束调整通信边，减少冗余信息传输。
4. 对比静态工作流与动态工作流在复杂任务和工具任务上的表现差异。

### 预期贡献
- 打通 communication 研究与 workflow engineering。
- 降低冗余通信和 token 浪费。
- 提高长轨迹任务的稳定性和可解释性。

### 潜在风险
- 图优化本身可能引入额外系统开销。
- 如果 verifier 不可靠，可能误删必要通信。
- 开放式任务下最优通信结构高度依赖上下文，泛化难度高。

## 3.3 Idea 3：把对齐约束写入协作协议而非外部守卫
### Motivation
虽然当前 10 篇锁定样本中没有单独的 alignment 专题综述，但 Wu 2025、Yan 2025、Jin 2025 都在各自场景中暴露出安全、约束和部署风险；cross-comparison 第 6 节也把治理不足列为真实空白。

### 问题定义
能否把权限、责任边界、安全约束、风险升级机制直接写入多 agent 协作协议与任务分解流程，而不是只在输出后做 guardrail。

### 方法设计
1. 在 Tran 2025 的 protocol 层增加角色权限与升级规则。
2. 在 Yan 2025 的 communication architecture 中加入敏感信息门控与异常中断策略。
3. 在 Wu 2025 式高风险场景中设计仿真测试：通信受限、角色冲突、越权指令、协作失败等。
4. 统一记录协议级失败模式，如死循环、越权、信息遗漏、错误升级路径。

### 预期贡献
- 让安全与治理从“事后审查”前移到“系统协议设计”。
- 提升多 agent 在高风险任务中的部署可信度。
- 为责任追踪和系统审计提供结构化接口。

### 潜在风险
- 约束形式化难度高。
- 过强约束可能伤害系统灵活性与性能。
- 不同场景的治理规则差异大，迁移性不一定强。

## 3.4 Idea 4：面向 cooperative decision-making 的 MARL–LLM 混合协议
### Motivation
Zhu 2024、Jin 2025、Chen 2026 共同表明：传统 MARL 通信理论、协同决策方法和 LLM 通信研究之间仍存在断层，但也存在明显可桥接空间。

### 问题定义
能否构建一套混合协议：在低层决策与通信调度中使用可学习或规则化 MARL 机制，在高层任务拆解、解释与异常处理上使用 LLM agents，从而兼顾可控性与灵活性。

### 方法设计
1. 以 Jin 2025 的五类决策方法为谱系基线，明确 MARL 与 LLM 分别负责哪些层次。
2. 用 Zhu 2024 的通信维度定义低层通信限制和对象选择。
3. 用 Chen 2026 的 Five Ws 统一高层协议表达。
4. 在自动驾驶或多无人机协同等场景中对比纯 MARL、纯 LLM、多层混合协议三种范式。

### 预期贡献
- 连接传统多智能体决策理论与当前 LLM-MAS 研究。
- 为高风险、强约束环境提供更可解释的混合架构。
- 帮助形成跨范式可比的研究语言。

### 潜在风险
- 系统架构复杂，调试难度高。
- 低层和高层协议接口设计不当会导致信息损失。
- 混合系统可能带来额外时延。

## 3.5 Idea 5：面向 creative/open-ended tasks 的多样性—一致性联合优化
### Motivation
Lin 2025 清楚表明 creative MAS 的关键难题是：多样性提升往往会伤害一致性、可控性和评价稳定性，而这类矛盾未来会扩展到教育、陪伴、角色扮演和社会模拟。

### 问题定义
如何在开放式任务中同时优化 idea diversity、artifact coherence、persona consistency 与 user controllability，而不是只追求更多观点或更高 novelty。

### 方法设计
1. 采用多角色结构，如 explorer、critic、synthesizer、user-proxy，对应 Lin 2025 中的 collaborative synthesis 与 proactivity 设计思路。
2. 把 Tran 2025 的不同协作结构映射到 creative workflow，比较中心化与对等讨论的差异。
3. 设计双重评价：自动评价负责结构和一致性，人类评价负责新颖性与价值感。
4. 在文本创意、协同设计、教育内容生成等任务上比较不同协议表现。

### 预期贡献
- 给 creative MAS 提供更可操作的系统设计范式。
- 推动开放任务从“会生成”走向“会共创”。
- 为多样性与一致性之间的权衡提供更稳定的实验框架。

### 潜在风险
- 创造性评价主观性高，实验复现难。
- 人工评价成本较高。
- 过度追求一致性可能抑制真正的创造性发散。

---

## 4. 结论
基于当前锁定的 10 篇综述，可以给出一个清晰判断：multi-agent 研究已经从“多模型协作 demo”阶段，进入“组织结构、通信机制、决策范式、系统评测与真实部署”共同塑形的阶段。

如果必须用一句话概括这组样本的共同信息，那就是：**multi-agent 的核心不再是模型数量，而是组织设计。** Li 2024 和 Guo 2024 给出了系统总图，Tran 2025、Yan 2025、Chen 2026 说明协作与通信是关键变量，Jin 2025 把它接回长期 cooperative decision-making 研究，Wu 2025 与 Lin 2025 则把它推进到高风险场景和开放式创造性任务。

因此，未来最值得做的不是继续重复“多 agent 比单 agent 强”的案例，而是三类更硬的工作：
1. 建立统一系统级 benchmark；
2. 打通 communication 与 workflow/runtime 理论；
3. 在高风险与开放任务中，把治理、评测和部署约束前置到协议设计层。

这也是本项目后续继续扩展 multi-agent 研究图谱时，最应该坚持的主线。

---

## 5. 参考路径
### 样本锁定与下载
- `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`
- `projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json`

### 逐篇分析与横向比较
- `projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-detailed-reading-notes.md`
- `projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-background-problem-framework-notes.md`
- `projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-cross-comparison.md`

### 直接来源链接
- Li et al. 2024: https://link.springer.com/article/10.1007/s44336-024-00009-2
- Guo et al. 2024: https://arxiv.org/abs/2402.01680
- Zhu et al. 2024: https://dblp.org/rec/journals/aamas/ZhuDW24
- Chen et al. 2025: https://arxiv.org/abs/2412.17481
- Tran et al. 2025: https://arxiv.org/abs/2501.06322
- Yan et al. 2025: https://arxiv.org/abs/2502.14321
- Wu et al. 2025: https://arxiv.org/abs/2502.16804
- Jin et al. 2025: https://arxiv.org/abs/2503.13415
- Lin et al. 2025: https://arxiv.org/abs/2505.21116
- Chen et al. 2026: https://arxiv.org/abs/2602.11583
