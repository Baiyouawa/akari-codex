# 2026-03-26 multi-agent 相关 10 篇综述中文综合报告

- Timestamp: 2026-03-26T00:15:25+08:00
- Session: 侑-00-1774454754-20fa0d
- 语料清单: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- 阅读依据: 各论文本地 PDF 首页摘要、目录、末尾挑战/总结段落，提取方式见元数据文件中的 `pypdf` 校验命令。

## 0. 报告结论先行

这 10 篇综述共同说明：**multi-agent 研究正在从“把多个 LLM 摆在一起”转向“把协作结构、通信协议、记忆/规划/价值约束、领域环境与评测闭环一起设计”**。如果只优化单个 agent 的 reasoning，系统性能很快会被以下瓶颈卡住：

1. **协作结构不稳定**：谁负责什么、何时交互、是否中心化，决定了系统可扩展性；
2. **通信成本不可控**：消息频率、内容粒度、带宽限制、协议安全性常被忽略；
3. **环境约束未进入设计闭环**：工业、自动驾驶、创意、人机共驾等真实场景，对时延、责任、可解释性要求高于 benchmark；
4. **评测仍以任务分数为主**：缺少对通信质量、角色分工质量、失败恢复能力、对齐与安全的系统性度量；
5. **治理层缺位**：价值对齐、安全攻防、权限边界往往作为事后补丁，而不是系统原生组件。

因此，最值得继续推进的不是再堆一个“多智能体框架”，而是做 **可观测、可控、可验证的 multi-agent operating stack**：把拓扑、协议、记忆、工具权限、评测与治理一起工程化。

---

## 1. 10 篇综述逐篇详述

## 1.1 Li et al. 2024 — 工作流/基础设施总框架综述

**论文**: *A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges*  
**来源**: Springer / Vicinagearth，见 `2026-03-26-ten-paper-metadata.md`

### 核心内容

这篇文章是较早且系统化的 LLM-MAS 总览之一。作者按工作流将系统拆为五个核心组件：

- profile
- perception
- self-action
- mutual interaction
- evolution

并把应用划分为两大类：

- **problem-solving**：把多个 agent 组织起来解复杂任务；
- **world simulation**：把 agent 作为社会/角色/环境主体进行交互模拟。

### 价值

它的最大贡献不是列举论文，而是给出一个**完整生命周期视角**。相比“多 agent = 多个角色 prompt”，这篇综述明确指出，系统必须同时考虑：个体画像、环境输入、自主行动、彼此交互和能力演化。

### 局限

- 成文时间较早，覆盖的系统仍偏 2023-2024 初期；
- “基础设施”视角很强，但在通信细节、安全治理、真实部署成本上还不够深；
- 对评测的讨论相对分散。

### 对本项目的启发

如果要做自己的 multi-agent 研究系统，这篇文章适合作为**总架构蓝图**：任何新机制都应映射到五组件中的某一层，而不只是“再加一个角色”。

---

## 1.2 Guo et al. 2024 — 早期 LLM-based Multi-Agents 进展与挑战总览

**论文**: *Large Language Model based Multi-Agents: A Survey of Progress and Challenges*

### 核心内容

这篇综述聚焦三个问题：

1. agent 被放在哪些 domain / environment 中；
2. agent 如何 profile 与 communication；
3. 哪些机制促进 agent 能力增长。

它把 LLM multi-agent 的主流用途概括为：

- 复杂问题求解
- 世界/社会模拟
- 协作决策

### 价值

它的贡献在于把“多智能体”从单纯工程框架上升为**能力增长机制**问题：为什么多个 agent 组合后，有时真的比单 agent 更强？答案常常不是“数量优势”，而是：

- 分工带来专门化；
- 对话带来错误暴露；
- 反馈循环带来反思与修正；
- 社会模拟带来更接近真实情境的博弈结构。

### 局限

- 仍属于早期 field survey，很多后来更精细的通信/协作分类还未展开；
- 对“何时 multi-agent 值得用”讨论不够严苛，容易让读者默认更多 agent 就更好。

### 启发

这篇文章适合作为“为什么需要 multi-agent”的基线综述，但后续研究必须进一步回答：**何种任务结构才配得上 multi-agent 带来的开销？**

---

## 1.3 Chen et al. 2024/2025 — LLM-MAS 应用前沿综述

**论文**: *A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application*

### 核心内容

这篇文章在 Guo/Li 的总览基础上，把重心进一步推向**应用面**。作者将 LLM-MAS 应用分成：

- solving complex tasks
- simulating specific scenarios
- evaluating generative agents

它强调，随着工作爆发式增长，单纯沿已有分类总结已不够，需要不断更新“应用前沿”。

### 价值

这篇文章的价值在于提醒读者：**multi-agent 不只是架构问题，也是应用牵引问题**。系统设计常被任务形态反向塑造：

- 代码协作需要严格角色与验证；
- 社会模拟需要人物一致性与长程记忆；
- 评估型系统需要辩论、互审与裁决机制。

### 局限

- 篇幅较短，很多分类是概括式的；
- 对方法层细节不如后来的专题综述深入。

### 启发

适合作为“应用地图”使用：帮助后续研究从任务需求出发，而不是先定死框架再找能跑的 demo。

---

## 1.4 Tran et al. 2025 — 协作机制综述

**论文**: *Multi-Agent Collaboration Mechanisms: A Survey of LLMs*

### 核心内容

这是 10 篇里最直接讨论**协作机制**的一篇。作者围绕以下维度组织文献：

- actors
- collaboration types：cooperation / competition / coopetition
- structures：peer-to-peer / centralized / distributed
- strategies：如 role-based、model-based
- coordination protocols

### 价值

它把“协作”从模糊概念变成了结构化设计空间。特别重要的是，它指出多 agent 的核心不是人数，而是：

- **关系结构**如何定义；
- **协调协议**如何维持；
- **策略差异**如何形成互补。

这对于真实系统很关键，因为同样是 4 个 agent：

- 若都是同构 peer-to-peer，可能只是重复思考；
- 若有角色异构、中心调度、冲突解决协议，则可能显著提升鲁棒性。

### 局限

- 对协作收益的因果验证仍不充分；
- 提到很多应用，但 benchmark 一致性较弱。

### 启发

未来研究应把“协作机制”作为一等研究对象，而不是默认使用 debate、planner-executor、critic-refiner 这些模板。

---

## 1.5 Yan et al. 2025 — 通信中心视角综述

**论文**: *Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems*

### 核心内容

这篇文章直接指出，很多已有综述按应用或架构分类，却忽视了**communication 才是 multi-agent 的真正核心**。作者提出双层通信框架：

- **system-level communication**：architecture、goals、protocols
- **system internal communication**：strategies、paradigms、objects、content

并系统总结通信效率、安全、benchmark、可扩展性问题。

### 价值

这是本轮最值得重点吸收的一篇之一。它的关键贡献是把“通信”从消息传递提升为系统设计学：

- 不是只看 agent 是否说话；
- 而是看谁对谁说、说什么、以什么协议说、代价是什么、风险是什么。

### 局限

- 仍偏框架级整理，对低层消息编码和可验证协议的工程实践还不够具体；
- 很多结论仍建立在异质 benchmark 上。

### 启发

任何 multi-agent 系统若不显式建模通信预算、通信内容粒度和协议安全，后续几乎必然撞上扩展性瓶颈。

---

## 1.6 Wu et al. 2025 — 自动驾驶多智能体综述

**论文**: *Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances*

### 核心内容

这篇论文讨论一个高约束、强实时、强安全场景：**自动驾驶**。作者指出单 agent ADS 面临：

- perception limited
- collaboration insufficient
- computational demand high

因此引入基于语言的多 agent 协调，并按交互模式讨论：

- cooperative
- competitive
- debate

以及结构：

- centralized
- decentralized
- hierarchical

### 价值

它的贡献在于把 multi-agent 研究拉进一个真正困难的真实场景中，迫使研究者面对：

- 通信时延
- 错误传播
- 安全责任
- 全局最优 vs 局部最优

这比很多纯 benchmark 讨论更接近未来落地问题。

### 局限

- 领域专用性较强，可迁移性有限；
- LLM 在实时系统中的工程可行性仍有距离。

### 启发

自动驾驶场景说明：**只要环境要求强实时与强安全，multi-agent 的“协作收益”就必须用时延、鲁棒性、故障隔离来重新定义**，不能只看任务正确率。

---

## 1.7 Aratchige & Ilmini 2025 — 技术要素综述

**论文**: *LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems*

### 核心内容

这篇文章聚焦四类基础技术：

- Architecture
- Memory
- Planning
- Technologies / Frameworks

其定位更像工程综述：讨论如何把多 agent 系统真正“搭起来”。

### 价值

它把注意力放回技术栈本身，提醒我们：多 agent 不是只有协作逻辑，也包括一整套执行基础设施，例如：

- 框架选型
- 记忆组织
- 规划范式
- 系统扩展性

### 局限

- 页数较短，很多内容停留在列表化比较；
- 对评测与理论问题不够深入。

### 启发

适合作为工程实现层面的 checklist：如果一个 multi-agent 系统在 memory / planning / framework 任一层欠账，再复杂的协作协议都会很脆弱。

---

## 1.8 Lin et al. 2025 — 创造力型 multi-agent 综述

**论文**: *Creativity in LLM-based Multi-Agent Systems: A Survey*

### 核心内容

这篇是较有特色的专题综述。作者认为已有 survey 多关注 infrastructure，却忽略了 **creative MAS**。文章重点讨论：

- agent proactivity 与 persona design
- 发散探索、迭代改进、协同综合等生成方式
- 文本/图像任务、数据集与评测
- 创造力评价标准不足、bias、协调冲突、统一 benchmark 缺失

### 价值

它说明 multi-agent 的优势不只在“提高正确率”，也在于：

- 扩大搜索空间；
- 激发多视角构思；
- 通过 critique / coalition / competition 产生意外新颖性。

### 局限

- 创造力本身难以客观度量；
- 该方向更容易被“好看 demo”掩盖真实方法问题。

### 启发

如果未来想研究 multi-agent 用于科研假设生成、产品创意、设计探索，这篇综述是重要入口。但必须配套更严肃的 novelty / utility / diversity 评测。

---

## 1.9 Zeng et al. 2025 — agentic AI 多层价值对齐综述

**论文**: *Multi-level Value Alignment in Agentic AI Systems: Survey and Perspectives*

### 核心内容

这篇文章把焦点放在**对齐与治理**。它把 value principles 按宏观-中观-微观层级展开，并将：

- 应用场景
- 方法
- benchmark / evaluation
- 多 agent 间价值协调

映射到这个多层框架中。

### 价值

这是本组语料中最能补足“治理盲区”的一篇。它提醒我们：对 multi-agent 来说，对齐不只是单 agent 不说脏话，而是：

- agent 与人类价值是否一致；
- agent 与 agent 之间是否出现目标漂移；
- 局部最优是否破坏系统级规范；
- 多方协作是否引入治理冲突。

### 局限

- “价值”框架较宏观，落到可执行 engineering policy 还需要二次转译；
- benchmark 仍不足以覆盖真实多方治理场景。

### 启发

未来 multi-agent 系统要想进入真实世界，必须从“任务优化”升级到“任务优化 + 规范约束 + 可追责机制”三位一体。

---

## 1.10 Chen et al. 2026 — Five Ws 通信综述

**论文**: *The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs*

### 核心内容

这篇是本轮最重磅的通信综述。作者用新闻学式的 **Five Ws** 统一三条传统：

- MARL
- Emergent Language
- LLM-based systems

具体围绕：

- who communicates with whom
- what is communicated
- when communication occurs
- why communication is beneficial

（题目中包含 five Ws，摘要明确展开了这些问题。）

### 价值

这篇文章最有价值的地方是：它让通信研究从一个个零散方法，变成**跨范式统一问题**。换句话说，MARL、EL、LLM-MAS 原本像三个社区，但在通信问题上其实共享同一组核心设计张力：

- 稀疏 vs 频繁通信
- 私有信号 vs 公共消息
- 可解释自然语言 vs 高效隐式协议
- 局部协作 vs 全局扩展

### 局限

- 篇幅极大，覆盖广，但在具体工程实现上仍需进一步抽取操作化原则；
- 对 LLM-based communication 的低成本实现路线还未收敛。

### 启发

如果只能选 1 篇作为 multi-agent communication 的总入口，这篇最值得作为主文献。它尤其适合启发“协议设计”与“跨范式混合系统”研究。

---

## 2. 横向比较

## 2.1 主题分布

这 10 篇可分为五类：

| 类别 | 论文 |
|---|---|
| 总体框架型 | Li 2024, Guo 2024, Chen 2024/2025 |
| 协作/通信型 | Tran 2025, Yan 2025, Chen 2026 |
| 技术栈型 | Aratchige 2025 |
| 应用专题型 | Wu 2025, Lin 2025 |
| 治理/对齐型 | Zeng 2025 |

### 观察

- 2024 年综述主要回答“LLM-MAS 是什么、有哪些方向”；
- 2025 年综述开始专题化，分别深挖 collaboration、communication、creativity、autonomous driving、alignment；
- 2026 年的 Five Ws 综述显示领域开始寻求**统一理论视角**，而不满足于应用堆叠。

---

## 2.2 对 multi-agent “核心问题”的定义差异

| 论文群 | 它们认为 multi-agent 的核心是什么 |
|---|---|
| Li / Guo / Chen | 复杂任务分解与应用扩展 |
| Tran | 协作机制设计 |
| Yan / Chen(2026) | 通信结构与协议 |
| Aratchige | 架构、记忆、规划等技术底座 |
| Wu | 真实高风险场景中的协调与时延 |
| Lin | 多主体共创与创意搜索 |
| Zeng | 多主体价值对齐与治理 |

### 观察

这说明领域并没有一个单一“唯一核心”。更合理的理解是：

> multi-agent = 在共享任务环境中，把多个具备部分自主性的决策单元，通过结构、协议、记忆与约束编织成一个系统。

---

## 2.3 共识点

几乎所有综述都共享以下共识：

1. **单 agent 有上限**：复杂任务、长链执行、开放环境、社会模拟、人机协作等场景容易触顶；
2. **multi-agent 的收益来自分工与交互，不是数量本身**；
3. **通信是系统表现关键变量**；
4. **memory / planning / tool use / role design 是反复出现的支柱能力**；
5. **benchmark 远落后于系统发展**；
6. **安全、对齐、扩展性会越来越成为主问题，而不是边角问题**。

---

## 2.4 分歧点

### 分歧 1：多 agent 是否普遍优于单 agent？

大部分综述默认在复杂任务上 multi-agent 有潜力，但真正严谨回答“是否值得”的证据还不够。通信成本、冲突管理、错误传播放大都可能抵消收益。

### 分歧 2：自然语言通信是不是最佳选择？

- 一部分工作偏爱自然语言，因为可解释、可迁移；
- 另一部分传统（尤其 MARL / EL）更关注效率和紧凑协议。

这意味着未来可能不是“统一自然语言”，而是**自然语言 + 结构化协议 + 隐式状态**的混合通信栈。

### 分歧 3：重点是通用系统还是垂直应用？

- 总览型论文更追求通用框架；
- 应用型综述表明，真正落地时必须高度场景化。

---

## 3. 研究空白总结

基于 10 篇综述的交叉对照，可以提炼出 7 个明显研究空白。

## 3.1 缺少“协作收益”因果识别

当前很多论文报告 multi-agent 表现更好，但常缺少以下对照：

- 同 token / 同调用预算下与单 agent 比；
- 固定角色数、仅改变通信协议；
- 固定协议、仅改变拓扑；
- 固定拓扑、仅改变记忆共享策略。

**空白本质**：我们还不知道提升到底来自 agent 数量、角色分工、反思回路、投票机制，还是仅仅来自更多采样。

## 3.2 缺少通信层可计算指标

Yan 2025 与 Chen 2026 都强调通信重要，但现有评测多数仍停在任务分数。

缺失指标包括：

- 平均消息长度 / 频率
- 有效消息率
- 冗余通信率
- 冲突恢复时延
- 通信带宽-性能曲线
- 协议鲁棒性 / 安全性

**空白本质**：没有通信层指标，就难以把 multi-agent 从经验主义推进到工程科学。

## 3.3 缺少动态组织结构研究

当前大量系统仍采用固定模板：planner-executor、debate、critic-refiner、role-playing team。真正稀缺的是：

- 根据任务难度动态扩缩 agent 数量；
- 根据失败模式重组拓扑；
- 根据上下文切换中心化 / 去中心化结构。

**空白本质**：我们研究了 agent 内部 reasoning，却较少研究**组织层自适应**。

## 3.4 缺少“记忆 × 通信 × 权限”联合设计

许多综述分别讨论 memory、communication、alignment，但真实系统中三者强耦合：

- 能记什么，决定能分享什么；
- 能分享什么，决定能协调什么；
- 能调用哪些工具，决定系统风险边界。

**空白本质**：缺少 unified control plane，把共享记忆、通信协议、工具权限放入同一治理框架。

## 3.5 缺少真实世界长期 benchmark

Wu 2025、Zeng 2025 都隐含提出：真实场景关心的是长期稳定、责任隔离、成本、时延、异常恢复，而不是一次性答题正确率。

**空白本质**：需要多轮、长时、带资源限制、带风险后果的 benchmark，而不是短平快任务。

## 3.6 缺少多主体治理与审计机制

multi-agent 一旦进入真实生产环境，就需要回答：

- 谁批准高风险动作；
- agent 之间意见冲突如何裁决；
- 错误责任如何归因；
- 安全越权如何审计与回滚。

**空白本质**：今天的大多数 multi-agent 框架更像“协作器”，还不是“可治理系统”。

## 3.7 缺少跨范式融合

Chen 2026 明显展示了 MARL、EL、LLM-MAS 的共通性，但社区仍相对割裂。

**空白本质**：未来真正有潜力的是混合范式：

- 高层用自然语言做可解释协作；
- 中层用结构化协议控成本；
- 低层用学习式通信优化效率。

---

## 4. 面向后续研究的 5 个 idea

## Idea 1：通信预算自适应的 multi-agent 调度器

### 动机
当前系统常默认“多说总比少说好”，但通信本身是成本中心。

### 核心假设
在固定 token / 延迟预算下，动态控制谁能发言、何时发言、发多长内容，能优于固定频率通信。

### 方法设计
- 将团队通信建模为 budgeted scheduling；
- 引入消息价值估计器，预测一次消息对最终结果的边际贡献；
- 在 planner / solver / critic 团队中测试静态与动态协议。

### 评测
- 任务成功率
- 单位成功所需 token
- 平均轮数
- 冗余消息率
- 失败恢复效率

## Idea 2：可审计的共享记忆总线

### 动机
多 agent 最大风险之一是共享记忆污染与无责任传播。

### 核心假设
如果共享记忆写入带 provenance、置信度、TTL、审批等级，系统会更稳健。

### 方法设计
- 为共享 memory object 增加：来源 agent、证据链接、写入时间、过期时间、信任级别；
- 区分 private / team / global memory；
- 设计 memory conflict resolver。

### 评测
- 错误信息扩散率
- 重复劳动率
- 任务成功率
- 人工审计成本

## Idea 3：组织结构自适应的 multi-agent 编排器

### 动机
固定拓扑不适合所有任务阶段。

### 核心假设
任务初期适合发散型并行结构，中后期适合层级收敛结构；动态切换优于固定模板。

### 方法设计
- 任务阶段识别器：探索 / 对齐 / 执行 / 验证；
- 不同阶段启用不同拓扑：mesh、hub-and-spoke、hierarchical；
- 使用失败信号触发重构。

### 评测
- 成功率
- 平均协调成本
- 结构切换次数
- 长任务稳定性

## Idea 4：面向真实世界的 governance benchmark

### 动机
当前 benchmark 很少测审批、冲突、权限、回滚、追责。

### 核心假设
治理能力是 multi-agent 从 demo 迈向生产的关键门槛。

### 方法设计
构建包含以下事件的任务集：
- 低风险自动执行
- 高风险需审批
- agent 间结论冲突
- 恶意消息注入
- 共享记忆污染
- 工具权限越界

### 评测
- 是否正确触发审批
- 是否拦截越权
- 冲突裁决正确率
- 审计链完整性

## Idea 5：跨范式混合通信栈

### 动机
自然语言通信解释性强但成本高；隐式协议高效但难解释。

### 核心假设
三层通信栈优于单一通信范式：
- 人类可见层：自然语言摘要
- agent 协调层：结构化 schema
- 机器高频层：压缩状态/向量信号

### 方法设计
- 设计统一 message schema；
- 高层输出自然语言 rationale；
- 中层传字段化任务状态；
- 低层在高频协调中传压缩表征。

### 评测
- 可解释性评分
- 延迟
- 带宽占用
- 成功率
- 对 prompt injection / message corruption 的鲁棒性

---

## 5. 对当前项目最实用的落地建议

结合这 10 篇综述，如果要服务本仓库中的 Agent 集群系统，最值得优先实现的不是更多“角色人设”，而是以下 4 件事：

1. **通信显式化**：记录谁向谁发送了什么结论、基于什么证据、何时发送；
2. **共享记忆分层**：区分个人笔记、团队共识、批准后事实；
3. **任务拓扑动态化**：调研、执行、复核阶段使用不同协作结构；
4. **治理内建化**：将审批、证据链、回滚、交叉 review 作为框架默认能力。

换言之，下一代 multi-agent 研究系统的差异化，不在“会不会多 agent”，而在**能不能把协作过程变成可验证对象**。

---

## 6. 报告局限

1. 本报告基于 10 篇本地 PDF 的摘要、目录、引言/总结段与部分表格信息撰写，不是逐页精读版读书笔记；
2. 10 篇语料是从当前 `literature/` 已落盘 20 个 PDF 中选出的工作子集，因而偏向当前仓库已收集语料；
3. 部分论文存在版本差异（如 arXiv v1/v2），本报告以元数据文件记录的来源页面与本地文件为准。

## 7. 一句话总评

从这 10 篇综述看，multi-agent 研究已经不缺“再造一个框架”，真正缺的是：**把协作、通信、记忆、评测与治理放进同一个可计算、可审计、可复现的系统理论与工程栈里。**
