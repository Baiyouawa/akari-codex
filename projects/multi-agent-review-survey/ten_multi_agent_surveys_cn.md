# 2026-03-26 十篇 multi-agent 相关综述中文总报告

- Timestamp: 2026-03-26T00:52:23+08:00
- Session: 结衣-03-1774457492-789106
- 任务: 综合 10 篇综述撰写中文 Markdown 报告，包含横向比较与研究空白总结
- Canonical reading set: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- 逐篇精读来源: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- 综合修订来源: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
- 交叉 review: `projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`
- research ideas: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`

> 说明：本报告不重新发明一套未验证结论，而是把项目内已经完成交叉复核的 10 篇 canonical 论文集合、结构化笔记、综合分析与 ideas 统一整理成一份可直接阅读的中文主报告。所有具体论文信息、页数、PDF 路径、来源页面均可回溯到上列文件。

---

## 1. 执行摘要

这 10 篇综述共同说明，multi-agent 研究的重心已经从“让多个 LLM 一起工作”升级为“如何系统设计协作结构、通信协议、记忆机制、工具编排、运行时工作流、角色建模与治理边界”。

### 1.1 最主要的四个趋势

1. **总览型综述正在让位于专题化综述**
   - 2024 年的 Guo 2024 更像全景地图；
   - 2025 年开始出现 communication、collaboration、垂直应用等专题化综述；
   - 2026 年进一步出现 workflow optimization、tool orchestration、role-playing agents 等工程/社会化子方向。

2. **通信已经从实现细节升级为一等研究对象**
   - Yan 2025 与 Chen 2026 都把 communication 放到中心位置；
   - “谁对谁说、什么时候说、说什么、为什么说”已成为独立 taxonomy。

3. **agent engineering 进入系统工程阶段**
   - Aratchige 2025、Xu 2026、Yue 2026 明显强调 architecture、memory、planning、tool-use、workflow graph；
   - 研究对象不再只是 prompt，而是完整运行时系统。

4. **评测与治理仍然是最大短板之一**
   - 多篇综述都指出 benchmark fragmented、成本与安全缺少统一度量、长期运行和真实世界评测薄弱；
   - 这也是本轮综述综合后最清晰的研究空白之一。

### 1.2 一句话结论

如果说 2024 年的主问题是“multi-agent systems 是什么”，那么 2025-2026 年的主问题已经变成“如何在成本、安全、可解释性和真实约束下，把 multi-agent systems 做成可复用、可优化、可治理的工程系统”。

---

## 2. 本轮最终采用的 10 篇综述

以下清单与 `analysis/2026-03-26-ten-paper-metadata.md` 保持一致。

| # | 论文 | 年份 | 主题定位 | 本地 PDF |
|---|---|---:|---|---|
| 1 | Guo et al. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* | 2024 | 通用总览 | `projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` |
| 2 | Aratchige & Ilmini — *LLMs Working in Harmony* | 2025 | architecture / memory / planning / frameworks | `projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` |
| 3 | Chen et al. — *A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application* | 2025 | 应用前沿与组件 | `projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` |
| 4 | Tran et al. — *Multi-Agent Collaboration Mechanisms: A Survey of LLMs* | 2025 | collaboration taxonomy | `projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` |
| 5 | Wu et al. — *Multi-Agent Autonomous Driving Systems with Large Language Models* | 2025 | 自动驾驶垂直应用 | `projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` |
| 6 | Yan et al. — *Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems* | 2025 | communication-centric survey | `projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` |
| 7 | Xu et al. — *The Evolution of Tool Use in LLM Agents* | 2026 | tool orchestration | `projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf` |
| 8 | Yue et al. — *From Static Templates to Dynamic Runtime Graphs* | 2026 | workflow optimization | `projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` |
| 9 | Chen et al. — *The Five Ws of Multi-Agent Communication* | 2026 | 5W communication framework | `projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` |
| 10 | Wang et al. — *Role-Playing Agents Driven by Large Language Models* | 2026 | 角色扮演/社会型 agent | `projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf` |

---

## 3. 十篇逐篇详述

以下逐篇内容基于结构化笔记文件 `analysis/2026-03-26-ten-survey-structured-reading-notes.md` 汇总改写，保留原有证据边界：优先依据来源页摘要、源码 section heading、以及源码中抽取到的 benchmark/dataset 命中信息。

### 3.1 Guo et al. 2024

**研究问题**
- 系统梳理 LLM-based multi-agent systems 的核心组成、应用类型与挑战。

**分类框架**
- 组件层：interface、profiling、management、communication、training、orchestration/efficiency；
- 应用层：problem solving、world simulation、dialogue data generation。

**核心贡献**
- 提供了早期最完整的通用框架地图之一；
- 适合作为后续专题综述的共同起点。

**涉及 benchmark / 数据集**
- `GSM8K`、`HumanEval`、`MMLU`、`BIG-bench`、`ChatArena`、`RoCoBench`、`CAMEL`、`AVALONBENCH`。

**优点**
- 覆盖面最广；
- 同时讨论 benchmark 与实现资源；
- 能快速建立对 LLM-MAS 的总体认识。

**局限**
- 时间较早；
- 对 2025-2026 年兴起的 workflow、tool orchestration、通信专题深度不足。

**启发**
- 适合作为“总览基线”，不适合作为最新专题问题的唯一依据。

### 3.2 Aratchige & Ilmini 2025

**研究问题**
- 构建高效 LLM-based MAS 时，哪些技术要素最关键？

**分类框架**
- `Architecture`、`Memory`、`Planning`、`Technologies/Frameworks` 四大块。

**核心贡献**
- 把研究重点从“系统长什么样”转向“系统为什么有效”；
- 更偏工程搭建视角。

**涉及 benchmark / 数据集**
- `ALFWorld`、`HotpotQA`、`HumanEval`、`MATH`、`MT-Bench`、`AlpacaEval`、`CAMEL`、`AutoGen`。

**优点**
- 对 architecture / memory / planning 的工程意义总结清晰；
- 对研发者比应用导向综述更直接。

**局限**
- 应用覆盖不如大型总览广；
- 更偏技术基建，总体地图感稍弱。

**启发**
- 对搭建真实系统最有帮助的是把 memory、planning 视作一等模块，而非附属功能。

### 3.3 Chen et al. 2025

**研究问题**
- 随着工作快速增长，LLM-MAS 在应用前沿上扩展到了哪些新边界？

**分类框架**
- 按应用场景组织：复杂任务求解、特定场景仿真、生成式 agent 评估；
- 同时补充 core components 与 interactions。

**核心贡献**
- 更强调“多生成式 agent 系统拿来做什么”；
- 把应用前沿与评测边界并列起来看。

**涉及 benchmark / 数据集**
- `AgentBench`、`AUCARENA`、`EvalPlus`、`GSM8K`、`HumanEval`、`MATH`、`MMLU`、`MT-Bench`、`MLAgentBench`、`ToolBench`、`LLMArena`、`ChatEval`。

**优点**
- 应用与评测覆盖面较强；
- 有助于从“场景需求”反推系统设计。

**局限**
- 对 workflow/tool/通信机制的深入程度不如后续专题综述。

**启发**
- 如果目标是找落地场景，这篇比纯 taxonomy 综述更实用。

### 3.4 Tran et al. 2025

**研究问题**
- 多个 LLM agent 的 collaboration mechanism 应该如何抽象、组织和比较？

**分类框架**
- actor、relation type（合作/竞争/竞合）、structure（点对点/中心化/分布式）、strategy、coordination protocol。

**核心贡献**
- 把 collaboration 从“多个 agent 一起做事”提升为有明确定义的结构问题；
- 对集体智能研究非常关键。

**涉及 benchmark / 应用域**
- 文中强调 benchmark 与应用域包括 QA/NLG、5G/6G、Industry 5.0、social/cultural settings。

**优点**
- taxonomy 很强；
- 合作/竞争/竞合三分法很有研究价值；
- 能帮助设计更丰富的多主体关系。

**局限**
- 对 workflow、工具、长程记忆不是重点；
- 需要与工程类综述配合使用。

**启发**
- “多 agent”不是简单加人数，而是重新定义交互结构与激励关系。

### 3.5 Wu et al. 2025

**研究问题**
- 在自动驾驶中，multi-agent + LLM 能否解决单 agent ADS 的感知、协作与决策瓶颈？

**分类框架**
- 按交互对象分：车-车、车-路、车-助手、agent-人类；
- 按任务分：协同感知、协同决策、云边部署、协同辅助工具。

**核心贡献**
- 证明 multi-agent 研究已从通用框架进入真实高风险行业场景；
- 把语言驱动通信映射到自动驾驶协同系统。

**涉及 benchmark / 数据集**
- `Waymo Open Motion Dataset`、multi-agent autonomous driving datasets 等。

**优点**
- 现实约束强；
- 对实时性、安全性、部署问题更敏感；
- 给了垂直场景下的具体需求。

**局限**
- 领域专用性强；
- 一些结论未必可无损迁移到通用 MAS。

**启发**
- 真正高价值的 multi-agent 系统不只是提高任务分数，还必须在时延、安全和部署约束下成立。

### 3.6 Yan et al. 2025

**研究问题**
- communication 在 LLM-MAS 中并非附属因素，而是核心决定变量；如何据此重构研究版图？

**分类框架**
- system-level：architecture、goals、protocols；
- internal communication：strategy、paradigm、object、content。

**核心贡献**
- 给出了 communication-centric taxonomy；
- 强调 communication design 决定协作质量、成本、安全与扩展性。

**涉及 benchmark / 数据集**
- `GAMA-Bench`、`MultiAgentBench`、`RealWorldBench`。

**优点**
- 视角鲜明，补上此前通用综述忽略的中心问题；
- system-level / internal 两层切分很适合做方法设计。

**局限**
- 过于聚焦通信，可能弱化 workflow、tool-use、memory 等其他因素。

**启发**
- 今后做多智能体实验，通信协议不应只当 prompt engineering 细节，而应当单独建模和评测。

### 3.7 Xu et al. 2026

**研究问题**
- LLM agent 的 tool use 如何从单工具调用演化到长程、多工具编排？

**分类框架**
- inference-time planning/execution、training/trajectory construction、safety/control、resource efficiency、open-environment completeness、benchmark/evaluation。

**核心贡献**
- 把工具调用问题升级为 multi-tool orchestration 问题；
- 更接近真实工业系统。

**涉及 benchmark / 数据集**
- `AgentLongBench`、`AndroidArena`、`CostBench`、`HammerBench`、`MCP-Bench`、`MTU-Bench`、`Mobile-Bench`、`OdysseyBench`、`RepoBench`、`RestBench`。

**优点**
- 长程、多工具、成本、安全四个维度总结完整；
- 对工业级 agent 系统非常有价值。

**局限**
- 不是纯 communication / collaboration survey；
- 对社会互动、角色建模覆盖有限。

**启发**
- 未来许多“multi-agent”提升，很可能和“multi-tool”能力边界纠缠在一起，不能分开看。

### 3.8 Yue et al. 2026

**研究问题**
- LLM agents 的 workflow 结构在何时确定、如何优化、用什么信号指导优化？

**分类框架**
- 三条主轴：
  1. 结构何时决定：静态 vs 动态；
  2. 优化 workflow 的哪一部分；
  3. 由何种 evaluation signal 驱动。

**核心贡献**
- 提出 `agentic computation graphs (ACGs)` 抽象；
- 把 workflow 从“固定模板链”升级为“运行时图结构”。

**涉及 benchmark / 数据集**
- `FlowBench`、`GAIA`、`GSM8K`、`HotpotQA`、`HumanEval`、`MATH`、`MCP-Bench`、`MCPEval`、`SOP-Bench`、`SWE-bench`、`Terminal-Bench`、`ToolBench`、`WorkflowBench`。

**优点**
- taxonomy 清晰且工程上可执行；
- 引入 graph-level properties、cost、robustness，超越单一 task score。

**局限**
- 对角色社会性、通信协议细节不是主线。

**启发**
- 未来 agent 系统优化，不会只靠 prompt 微调，而会越来越依赖 runtime graph 级别优化。

### 3.9 Chen et al. 2026

**研究问题**
- 如何用统一框架联通 MARL、emergent language、LLM-based MAS 中的通信研究？

**分类框架**
- 5W：Who / Whom / When / What / Why。

**核心贡献**
- 给出跨范式桥梁，把传统多智能体通信与 LLM 通信放进统一问题模板；
- 同时包含纳入/排除标准，综述方法更规范。

**涉及 benchmark / 数据集**
- `AvalonBench`、`BattleAgentBench`、`ChatEval`、`GAIA`、`MultiAgentBench`、`RoCoBench`、`CAMEL` 等。

**优点**
- 5W 框架普适性很强；
- 有助于后续研究直接按 5W 拆问题；
- 为 communication 子方向提供“标准问法”。

**局限**
- 强聚焦通信，不覆盖 workflow/tool/memory 全景。

**启发**
- 对任何多智能体系统，都可以先问：谁通信、面向谁、何时触发、消息内容是什么、通信目标为何。

### 3.10 Wang et al. 2026

**研究问题**
- role-playing agents 如何从模板角色生成，演化为人格、记忆、动机驱动的社会型 agent 系统？

**分类框架**
- paradigm evolution、角色建模核心技术、角色专属数据构建、评测方法与指标、未来趋势。

**核心贡献**
- 把 social/role-playing agents 作为独立且系统化的研究支线；
- 强调 personality、memory、motivation 对长期互动与叙事一致性的作用。

**涉及 benchmark / 数据集**
- `CharacterEval`、`RoleBench`、`RoleEval`、`RoleEval-Chinese`、`RoleEval-Global`、`RMTBench`、`RVBench`。

**优点**
- 对人格一致性、长期记忆、价值对齐等问题讨论细；
- 对 social simulation、companion agents 研究特别有价值。

**局限**
- 对通用协作、工具调用、workflow 优化覆盖较少；
- 更偏社会型场景。

**启发**
- 多智能体不只用于做任务，也可能用于构建社会互动、叙事生成与角色生态。

---

## 4. 横向比较

### 4.1 按研究主题分组

| 组别 | 论文 | 关心的问题 |
|---|---|---|
| 通用总览 | Guo 2024、Chen 2025 | multi-agent 系统有哪些组件、应用和挑战 |
| 技术底座 | Aratchige 2025 | architecture / memory / planning / frameworks 如何影响系统效果 |
| 协作机制 | Tran 2025 | cooperation / competition / coordination 如何组织 |
| 通信机制 | Yan 2025、Chen 2026 | 谁在何时对谁说什么、为什么说 |
| 工具与工作流 | Xu 2026、Yue 2026 | multi-tool orchestration 与 workflow graph 如何设计与优化 |
| 垂直应用 | Wu 2025 | 自动驾驶中的多主体协同与安全约束 |
| 社会型 agents | Wang 2026 | 角色、人格、记忆、社会叙事如何建模 |

### 4.2 共识

跨 10 篇综述反复出现的共识如下：

1. **单 agent 在复杂长期任务中会触顶**
   - 多角色分工、互补视角和并行探索仍然是 multi-agent 的核心吸引力。

2. **真正决定收益的不是 agent 数量，而是交互结构**
   - 这一点在 Tran 2025、Yan 2025、Chen 2026 中尤为明显。

3. **通信是性能、成本与安全的共同瓶颈**
   - 通信不足会导致协作失效；
   - 通信过量又会抬高 token 成本、延迟和攻击面。

4. **agent benchmark 体系不统一**
   - 不同论文使用不同的 benchmark 家族，导致横向比较困难。

5. **现实部署要求开始压过纯方法分数**
   - Xu 2026、Yue 2026、Wu 2025 都在强调效率、治理、时延、鲁棒性、运行时优化。

### 4.3 分歧

1. **研究主语不同**
   - 有的把 multi-agent 看成应用系统；
   - 有的看成通信网络；
   - 有的看成 workflow graph；
   - 有的看成社会角色生态。

2. **自然语言通信 vs 高效协议通信**
   - Chen 2026 连接了 MARL、emergent language 与 LLM communication，显示这两类传统并未统一。

3. **通用性 vs 领域约束**
   - 通用综述追求统一框架；
   - Wu 2025、Wang 2026 则显示垂直领域必须接纳真实约束，而不能只靠抽象统一。

---

## 5. 时间演化脉络

### 5.1 2024：先回答“是什么”

- 代表：Guo 2024。
- 核心任务：建立 LLM-based MAS 的总地图。
- 关键词：组件、应用、挑战、资源、benchmark。

### 5.2 2025：进入专题化分化

- architecture / memory / planning：Aratchige 2025；
- 应用前沿：Chen 2025；
- collaboration：Tran 2025；
- communication：Yan 2025；
- 垂直场景：Wu 2025。

这一阶段的标志是：研究者不再满足于“多 agent 有用”，而开始问“究竟是哪一层机制在起作用”。

### 5.3 2026：工程系统化与社会化并进

- tool orchestration：Xu 2026；
- runtime workflow graph：Yue 2026；
- unified communication theory：Chen 2026；
- role-playing/social agents：Wang 2026。

这说明 multi-agent 已经明显分裂成多个高密度子方向，并开始争夺统一方法学与统一评测协议。

---

## 6. 研究空白总结

以下空白是根据 `analysis/2026-03-26-ten-survey-synthesis-report.md` 与各逐篇笔记共同归纳得出。

### 6.1 协作收益缺少因果拆解

很多工作只报告 multi-agent 优于 single-agent，但未严格控制：
- token 预算；
- 工具使用权限；
- 外部检索条件；
- 拓扑与角色数。

因此现在往往只能知道“多 agent 变好了”，却不知道到底是：
- 多了一次采样；
- 多了外部工具；
- 多了角色分工；
- 还是通信结构真的更优。

### 6.2 缺少通信层专属指标

Yan 2025 与 Chen 2026 都间接说明，当前评测过度依赖任务得分，缺失以下关键指标：
- 消息有效率；
- 冗余率；
- 冲突恢复时延；
- 通信成本-性能曲线；
- 安全/攻击鲁棒性。

### 6.3 workflow / communication / tool-use 仍被割裂研究

- Xu 2026 研究工具编排；
- Yue 2026 研究 workflow graph；
- Yan 2025 / Chen 2026 研究 communication。

但真实系统中，这三者是强耦合的：
- workflow 决定谁有机会通信；
- 通信决定是否触发工具；
- 工具结果反过来改变 workflow。

目前缺少把三者一起优化的统一框架。

### 6.4 缺少长期、真实、可治理 benchmark

- 自动驾驶、开放环境工具调用、社会型角色交互都提示：
  - 长轨迹；
  - 失败恢复；
  - 安全边界；
  - 权限治理；
  - 责任归因；
  还远未被现有 benchmark 系统覆盖。

### 6.5 角色与社会型多智能体研究仍处早期

Wang 2026 提醒我们：
- personality fidelity；
- memory consistency；
- social relation stability；
- narrative coherence；
目前仍缺少统一而强的评测与建模标准。

### 6.6 真实工业系统的治理仍弱

Xu 2026、Wu 2025 都在强调：
- 开放环境下的越权调用；
- 多工具并发带来的安全问题；
- 高风险行业中的通信失真；
- runtime graph 的不可控增长；
这些仍是研究与落地之间最大的缝隙之一。

---

## 7. 对本项目与 agent 集群的直接启发

结合本仓库的 `repo as memory + multi-agent` 工作方式，10 篇综述带来的可执行启发包括：

### 7.1 把通信当成一等对象记录

不仅要记录最终结论，还要记录：
- 谁提出；
- 基于哪些文件；
- 是否被复核；
- 是否与他人结论冲突。

这与 Yan 2025、Chen 2026 的通信中心视角高度一致。

### 7.2 共享记忆要分层

可分为：
- 个体工作笔记；
- 团队共享中间结论；
- 经交叉 review 锁定的 canonical facts。

这与 Aratchige 2025、Wang 2026 对 memory 重要性的强调一致。

### 7.3 不同阶段应使用不同协作拓扑

- 检索期：并行探索更有效；
- 写作期：主笔 + 复核更有效；
- 质检期：交叉审查更有效。

这与 Tran 2025、Yue 2026 对结构与 workflow 的认识一致。

### 7.4 将治理嵌入工作流

- 高风险写操作触发 review；
- 文档间 canonical set 不一致时强制修正；
- 未验证断言不允许升格为最终结论。

这与 Xu 2026 对 governance 的强调一致。

---

## 8. 可继续推进的研究方向

本项目已另行产出 5 个 research ideas：
`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`

其中最值得优先推进的方向包括：

1. **预算感知的通信-工作流联合优化器**
   - 直接对应 communication 与 workflow 断裂这一空白。

2. **agent benchmark 统一协议**
   - 直接回应 benchmark fragmentation 问题。

3. **开放环境中的多工具协作 agent 安全治理**
   - 直接回应 industrial-grade deployment 的治理缺口。

4. **角色记忆驱动的社会型多智能体叙事系统**
   - 对 social agents / role-playing agents 有较强新意。

5. **面向自动驾驶的多主体通信压缩与优先级调度**
   - 适合作为高风险高收益方向。

---

## 9. 快速结论版

如果要把这 10 篇综述压缩成一页 takeaway，可以记住下面六句话：

1. **multi-agent 研究已经从“多人协作”进入“系统工程”阶段。**
2. **通信是核心变量，不是实现细节。**
3. **workflow、tool-use、memory、communication 需要联合优化。**
4. **benchmark 体系仍然碎片化，是当前最大方法学瓶颈之一。**
5. **真实应用场景正在把安全、延迟、治理拉到和性能同等重要的位置。**
6. **社会型 agent 与角色建模可能成为下一波新的增长点。**

---

## 10. 证据链与对应关系

- canonical 10 篇清单、作者、年份、来源、页数、PDF 路径：
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- 逐篇结构化精读：
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- 综合分析修订稿：
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
- 交叉 review 证据：
  `projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`
- 研究 idea：
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`

本报告本身不新增未经验证的论文事实，只对以上已核验材料做统一编排与中文总结。