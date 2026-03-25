# 2026-03-26 十篇综述统一脉络：multi-agent survey 总体框架

- Timestamp: 2026-03-26T03:12:14+08:00
- Session: 绫-07-1774465906-581fd3
- Task: 交叉比对 10 篇综述之间的重合点与差异点，整理统一的 multi-agent survey 总体脉络，包括任务分类、协作机制、通信方式、评测维度与应用方向。
- Canonical reading set: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- Primary evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- Supporting synthesis: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`; `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`

> 说明：本文不新增未在项目内交叉复核过的论文事实，只对既有 canonical 10 篇综述做统一抽象。所有“共识/差异”均回链到已落盘的结构化精读、综合报告或主文档。

---

## 1. 先给结论：十篇综述可以压成一张统一地图

这 10 篇综述虽然各自切入点不同，但可以统一压缩为一个五层框架：

1. **任务层**：multi-agent 被用于什么问题；
2. **组织层**：多个 agent 如何分工协作；
3. **通信层**：谁在何时以何种方式交换什么信息；
4. **执行层**：memory / planning / tools / workflow 如何支撑运行；
5. **评测与治理层**：怎么衡量收益、成本、安全、稳定性与真实可部署性。

换句话说，当前 multi-agent survey 领域已经不再只是“多几个 agent 一起干活”，而是在研究一套完整的**任务—协作—通信—执行—评测**系统。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 0、2、4 节；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md` 第 1、3、6、7 节。

---

## 2. 十篇综述在统一地图中的分工

| 统一层级 | 代表综述 | 主要贡献 |
|---|---|---|
| 任务层 | Guo 2024; Chen 2024; Wu 2025; Wang 2026 | 说明 multi-agent 被用来解决哪些通用任务、仿真任务、垂直场景任务与社会互动任务 |
| 组织层 | Tran 2025; Guo 2024; Aratchige 2025 | 说明角色设定、协作关系、拓扑结构、规划与记忆如何影响系统组织 |
| 通信层 | Yan 2025; Chen 2026 | 说明 communication 是主变量，并给出 system-level / internal communication 与 5W 框架 |
| 执行层 | Aratchige 2025; Xu 2026; Yue 2026 | 说明 architecture、memory、planning、tool orchestration、workflow graph 如何支撑执行 |
| 评测与治理层 | Guo 2024; Chen 2024; Xu 2026; Yue 2026; Wang 2026 | 说明 benchmark、资源预算、安全、鲁棒性、人格一致性与真实部署约束 |

这个映射解释了为什么十篇综述会看起来“主题不一样”但又能被纳入同一阅读集：它们实际上分别覆盖统一系统的不同层。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 十篇条目；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md` canonical 10 篇清单。

---

## 3. 任务分类：十篇综述合并后可归纳出的统一任务谱系

### 3.1 通用认知与问题求解任务
代表来源：Guo 2024、Chen 2024。

统一后可归纳为：
- 数学/逻辑/知识问答；
- 代码生成与编程；
- 长程复杂任务分解；
- agent-based evaluation 与对抗式讨论。

这些任务对应“为什么需要多 agent”的第一层理由：单 agent 在复杂分解、视角互补和自我纠错上容易触顶。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Guo 2024 `LLM-MA for Problem Solving`、Chen 2024 `solving complex tasks`；`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 第 1、4 节。

### 3.2 世界模拟与社会互动任务
代表来源：Guo 2024、Chen 2024、Wang 2026。

统一后可归纳为：
- world simulation；
- 社会角色扮演与长期互动；
- narrative / social agent 环境；
- 多角色博弈与文化/社会场景模拟。

这一类任务强调多 agent 的“社会性”而非单点求解能力。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Guo 2024 `World Simulation`、Chen 2024 `simulating specific scenarios`、Wang 2026 `role-playing modeling`。

### 3.3 垂直应用任务
代表来源：Wu 2025。

统一后可归纳为：
- 车-车协作；
- 车-路协作；
- 车-助手协作；
- agent-human 协作；
- cloud-edge 协同决策与部署。

这一类任务提醒我们：multi-agent 不只是抽象方法，也是一种真实约束下的系统组织方式。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Wu 2025 条目。

### 3.4 工具使用与工作流任务
代表来源：Xu 2026、Yue 2026。

统一后可归纳为：
- 单工具到多工具编排；
- 长程任务轨迹执行；
- 静态模板 workflow；
- 动态 runtime graph / ACG 优化；
- verifier-guided 执行与重规划。

这说明“任务”在 2026 年已经不只是终端目标，而是包含整个执行图和工具链。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Xu 2026、Yue 2026 条目。

### 3.5 统一任务分类结论
把十篇综述合并后，当前 multi-agent survey 的任务分类可以统一成四大类：

1. **认知求解类**：问答、代码、复杂推理；
2. **社会模拟类**：多角色互动、世界模拟、叙事生成；
3. **垂直场景类**：自动驾驶等高风险应用；
4. **系统执行类**：tool-use、workflow、runtime graph 优化。

- Provenance: 本节系对上述四个子节的合并归纳；各子节来源见对应 provenance。

---

## 4. 协作机制：重合点与差异点

### 4.1 重合点：多篇综述共享的协作共识

#### 共识 A：收益来自角色分工，不来自 agent 数量本身
- Guo 2024 强调 profiling、management、communication；
- Aratchige 2025 强调 architecture、planning、memory；
- Tran 2025 明确把 actors、relation types、structures、strategies 作为主线。

统一后可得：**角色设计 + 结构设计** 才是多 agent 价值来源。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Guo 2024、Aratchige 2025、Tran 2025 条目；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md` 第 3 节。

#### 共识 B：协作关系不止“合作”一种
Tran 2025 明确写到 cooperation / competition / coopetition；Wang 2026 的社会型 agent 也隐含多角色关系并不总是完全协同；Wu 2025 的多车与人机协作也存在约束与博弈。

统一后可得：当前综述共同承认 multi-agent 关系至少包括：
- 合作；
- 竞争；
- 协商；
- 混合博弈/竞合；
- 人机协同。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Tran 2025、Wu 2025、Wang 2026 条目。

### 4.2 差异点：不同综述关注的协作切口不同

| 切口 | 代表综述 | 差异体现 |
|---|---|---|
| 宏观系统组织 | Guo 2024; Aratchige 2025 | 更关注模块、角色、规划、记忆 |
| 协作关系 taxonomy | Tran 2025 | 更关注合作/竞争/结构/策略 |
| 通信驱动协作 | Yan 2025; Chen 2026 | 更关注协作能否成立取决于 communication design |
| 领域化协作 | Wu 2025 | 更关注车-车/车-路/人机协作的实际约束 |
| 社会型协作 | Wang 2026 | 更关注人格、记忆、动机驱动的互动质量 |

### 4.3 统一协作机制框架
十篇综述合并后，可以把协作机制统一拆成五个问题：

1. **谁参与协作**：固定角色、动态角色、社会角色；
2. **协作关系是什么**：合作、竞争、竞合、人机协同；
3. **如何组织拓扑**：点对点、中心化、分布式、图结构；
4. **如何分配职责**：静态分工、基于计划的分工、运行时重分配；
5. **如何纠错与收敛**：讨论、投票、验证器、重规划、外部工具检查。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Tran 2025、Aratchige 2025、Xu 2026、Yue 2026、Wang 2026 条目综合归纳。

---

## 5. 通信方式：重合点与差异点

### 5.1 重合点：通信已经被所有主线认可为核心变量
虽然只有 Yan 2025 与 Chen 2026 专门做通信综述，但 Guo 2024、Tran 2025、Wu 2025、Xu 2026、Yue 2026 都把 communication 或 coordination 作为系统关键环节。

统一共识是：通信同时影响
- 信息共享；
- 协作效率；
- token/时间成本；
- 错误传播；
- 安全攻击面；
- 可解释性。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 0、2、4 节；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md` 第 3、6 节。

### 5.2 差异点：通信的分类口径不同

#### 口径 1：system-level vs internal communication
- Yan 2025 将通信分为 architecture / goals / protocols 与 strategy / paradigm / object / content 两层。
- 这是“系统设计”视角。

#### 口径 2：5W communication
- Chen 2026 统一为 Who / Whom / When / What / Why。
- 这是“问题模板”视角。

#### 口径 3：协作中的通信结构
- Tran 2025 强调 communication structures 与 coordination protocols。
- 这是“协作结构”视角。

#### 口径 4：真实场景中的通信对象
- Wu 2025 以车-车、车-路、车-助手、agent-human 来划分。
- 这是“应用对象”视角。

### 5.3 统一通信框架
综合上述差异，可把 multi-agent survey 中的通信方式统一为五个维度：

1. **Who**：哪些 agent / 人 / 基础设施参与说话；
2. **Whom**：通信对象是单个 agent、群体还是外部系统；
3. **When**：固定轮次、事件触发、预算触发、冲突触发、运行时动态触发；
4. **What**：自然语言消息、计划、状态、工具结果、压缩摘要、结构化信号；
5. **Why**：信息共享、谈判协调、纠错验证、任务分解、风险规避。

这是本文认为最稳的统一通信脉络，因为它能兼容 Yan 2025 的两层结构、Chen 2026 的 5W、Tran 2025 的 coordination、Wu 2025 的场景对象划分。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Yan 2025、Chen 2026、Tran 2025、Wu 2025 条目。

### 5.4 当前通信研究的核心差异
十篇综述交叉后，通信研究内部还存在三条明显分歧：

1. **自然语言开放通信 vs 高效压缩协议**；
2. **可解释性优先 vs 成本效率优先**；
3. **通用通信框架 vs 领域特定通信规则**。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 2.2 节；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md` 第 4 节。

---

## 6. 评测维度：十篇综述合并后的统一评价表

### 6.1 重合点：都认为只看任务分数不够
Guo 2024、Chen 2024、Yan 2025、Xu 2026、Yue 2026、Wang 2026 都在不同上下文中指出：仅用 task score 评估 agent system 不足以反映真实能力。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 4 节；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md` 第 3、6、9 节。

### 6.2 差异点：不同综述强调的评测维度不同

| 维度 | 代表综述 | 重点 |
|---|---|---|
| 任务正确率/成功率 | Guo 2024; Chen 2024 | 通用任务、代码、问答、复杂问题求解 |
| 协作质量 | Tran 2025; Yan 2025; Chen 2026 | 协调效果、消息有效率、协议设计 |
| 工具执行质量 | Xu 2026 | 长轨迹、多工具、资源约束、安全控制 |
| workflow 质量 | Yue 2026 | graph quality、dynamic editing、verifier signal |
| 真实部署约束 | Wu 2025 | 实时性、安全性、云边协同 |
| 社会一致性 | Wang 2026 | personality fidelity、memory consistency、relation stability |

### 6.3 统一评测维度框架
把十篇综述的评测维度合并后，可统一为六类：

1. **任务结果**：正确率、完成率、质量分；
2. **协作效率**：分工有效性、协调收敛速度、冲突恢复；
3. **通信质量**：消息有效率、冗余率、时延、通信成本；
4. **执行质量**：工具成功率、workflow 稳定性、长程轨迹可靠性；
5. **系统成本与治理**：token/时间/算力预算、安全、鲁棒性、可审计性；
6. **场景特定质量**：自动驾驶安全、角色一致性、社会互动稳定性等。

这六类维度比任何单篇综述都更完整，且能覆盖通用、工程、通信、垂直场景与社会型 agent 研究。

- Provenance: 本节系对前述评测差异表与 `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 十篇条目的综合归纳。

### 6.4 评测层最大的共同空白
十篇综述最一致的批评之一是：**benchmark fragmented**。当前缺口主要有三类：
- 缺少统一协议，难做公平横向比较；
- 缺少通信层指标；
- 缺少长期、真实、可治理 benchmark。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 4.2、4.4 节；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md` 第 3、6、9 节。

---

## 7. 应用方向：统一后的应用版图

### 7.1 通用应用方向
- problem solving
- coding
- QA / reasoning
- dialogue generation
- generative agent evaluation

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Guo 2024、Chen 2024。

### 7.2 场景模拟与社会应用方向
- world simulation
- social and cultural settings
- role-playing agents
- collaborative narrative
- companion / immersive interaction

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Guo 2024、Tran 2025、Wang 2026。

### 7.3 工业与真实系统方向
- autonomous driving
- cloud-edge coordination
- open-environment tool use
- industrial-grade orchestration

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Wu 2025、Xu 2026。

### 7.4 平台与基础设施方向
- multi-agent frameworks
- memory/planning architectures
- workflow graphs
- agent runtime optimization
- communication protocol design

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Aratchige 2025、Yan 2025、Yue 2026、Chen 2026。

### 7.5 统一应用方向结论
十篇综述合并后，应用方向可统一成四条主线：

1. **任务求解主线**；
2. **社会模拟主线**；
3. **真实产业主线**；
4. **平台基础设施主线**。

这也解释了为什么当前“multi-agent survey”已经从一个单点领域扩展成一个跨任务、跨系统、跨应用的大方向。

- Provenance: 本节对 7.1-7.4 小节的归纳；各小节来源见对应 provenance。

---

## 8. 最终统一知识框架：一个可复用的 survey 模板

基于十篇综述的重合点与差异点，后续如果继续写 multi-agent survey，最稳定的统一模板应当是：

### 8.1 问题定义层
- 目标任务是什么？
- 为什么单 agent 不够？
- 为什么需要 multi-agent / multi-tool / workflow？

### 8.2 任务分类层
- 认知求解类
- 社会模拟类
- 垂直场景类
- 系统执行类

### 8.3 协作机制层
- 参与者
- 关系类型
- 组织拓扑
- 角色与分工
- 收敛与纠错机制

### 8.4 通信机制层
- Who / Whom / When / What / Why
- natural language vs structured protocol
- system-level vs internal communication

### 8.5 执行机制层
- architecture
- memory
- planning
- tool orchestration
- workflow graph / runtime editing

### 8.6 评测与治理层
- 任务结果
- 协作效率
- 通信质量
- 执行质量
- 成本/安全/鲁棒性
- 场景专用指标

### 8.7 应用层
- 通用任务
- 社会互动
- 垂直行业
- 平台与基础设施

这个模板基本覆盖了 canonical 10 篇综述的主要信息结构，可以作为项目后续继续扩展文献库时的统一抽取框架。

- Provenance: 全文综合归纳，基础材料来自 `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 与 `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`。

---

## 9. 对本项目的直接结论

### 9.1 本任务的交付结论
本次交叉比对后，可以把 10 篇综述之间的关系总结成一句话：

**Guo/Chen 给全景，Tran/Yan/Chen(2026) 给协作与通信主线，Aratchige/Xu/Yue 给系统执行主线，Wu/Wang 给真实场景与社会型边界。**

### 9.2 对后续研究选题的直接启发
优先值得继续做的统一问题，不是单独优化某个局部模块，而是做以下交叉点：
- communication × workflow 联合优化；
- collaboration × benchmark 统一协议；
- tool-use × governance × cost-aware control；
- social agents × memory consistency × long-horizon evaluation。

这些方向都来自本文整理出的统一框架中的“断裂处”，而不是来自单篇综述的局部热点。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 4 节；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-idea-dedup-and-priority.md`。

---

## 10. 交付核验

本文件完成后，可直接作为以下未闭环任务的证据：
- “交叉比对 10 篇综述之间的重合点与差异点，整理统一的 multi-agent survey 总体脉络，包括任务分类、协作机制、通信方式、评测维度与应用方向。”

核验方式：
- 已显式覆盖任务分类：见第 3 节；
- 已显式覆盖协作机制：见第 4 节；
- 已显式覆盖通信方式：见第 5 节；
- 已显式覆盖评测维度：见第 6 节；
- 已显式覆盖应用方向：见第 7 节；
- 已给出统一总体脉络：见第 8 节。
