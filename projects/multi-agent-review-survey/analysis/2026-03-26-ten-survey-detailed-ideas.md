# 2026-03-26 基于十篇 multi-agent 综述空白点与未来方向的 10 个详细 research ideas

- Timestamp: 2026-03-26T02:01:50+08:00
- Session: 理世-06-1774461669-41deb7
- Scope: 基于 canonical 10 篇综述的共同空白、作者明确提出的 future directions、以及已有中文综合报告，提出 10 个后续可做的详细 idea。
- Primary sources:
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`

## 方法说明

本文件不重新发明问题，而是把现有 10 篇综述里反复出现的缺口具体化为可执行项目。每个 idea 都强制包含：

1. 问题定义
2. 为什么值得做
3. 与现有综述的关系
4. 可行方法
5. 数据/benchmark
6. 评测指标
7. 预期难点
8. 最小可执行原型（MVP）

下文中的“与现有综述的关系”只引用仓库内已落盘的综述笔记与综合报告，不额外引入未经核验的新论文结论。

---

## Idea 1：预算感知的动态通信—工作流联合优化器

### 问题定义
在多智能体系统中，“通信要不要发生、发生几轮、由谁发给谁”和“工作流图如何组织、是否需要中间 verifier/critic 节点”通常被分开设计，导致系统要么通信过多、成本过高，要么工作流过死、遇到失败无法重组。这个 idea 要解决的问题是：**在固定 token / 时间预算下，动态联合优化 communication topology 与 workflow graph，最大化任务成功率。**

### 为什么值得做
`ten-survey-synthesis-report.md` 明确指出通信、workflow、tool-use 在真实系统里强耦合，但现有研究大多分开处理；`ten-survey-quick-overview.md` 也把“通信成为核心变量”“工程系统视角增强”列为主趋势。如果能把二者合并成统一优化问题，就能直接提升真实 agent 系统的性价比，而不是只提升离线 benchmark 分数。

### 与现有综述的关系
- **Yan 2025 / Chen 2026**：提供 communication-centric 与 5W 框架，说明“谁和谁在何时说什么”本身就是研究对象。
- **Yue 2026**：把 workflow 抽象为 agentic computation graphs（ACGs），说明结构可以被运行时编辑。
- **Guo 2024 / Aratchige 2025**：指出 orchestration efficiency、planning、memory 是系统性挑战。
- 来源：`ten-survey-structured-reading-notes.md` 对上述四篇的笔记；`ten-survey-synthesis-report.md` 第 4.3 节。

### 可行方法
1. 用图表示一个多智能体系统：节点是 planner / solver / retriever / critic / tool-agent，边是消息传递。
2. 每一步根据任务状态决定：
   - 保持原图；
   - 删除低价值通信边；
   - 插入 verifier；
   - 把串行子图改成并行子图；
   - 降级为单 agent 执行。
3. 训练或搜索一个 meta-controller，用任务成功信号、花费 token、wall-clock time 共同作为奖励。
4. 结合 rule-based 先验：高不确定度时增加复核边，低不确定度时压缩通信。
5. 输出的不只是答案，还包括最终图结构与通信轨迹，方便后验分析。

### 数据/benchmark
- `WorkflowBench`, `GAIA`, `SOP-Bench`, `MultiAgentBench`, `AgentBench`
- 证据来源：`ten-survey-structured-reading-notes.md` 中 Yue 2026、Yan 2025、Chen 2025 条目。

### 评测指标
- 任务成功率 / pass@k
- 平均 token 成本
- 平均 wall-clock latency
- 平均通信轮数
- 图编辑次数与结构稳定性
- 单位成本成功率（success per 1k tokens）

### 预期难点
- 多目标优化容易不稳定：高成功率和低成本往往冲突。
- 同一任务上不同图结构可能都成功，credit assignment 困难。
- benchmark 之间工作流复杂度差异大，泛化不一定成立。

### 最小可执行原型
先在 2~3 个任务类型上做一个 **三节点系统**：planner + worker + critic。只允许两种编辑动作：
1. 增加一次 critic 复核；
2. 关闭 worker 间互聊。
对比固定 workflow 与预算感知动态 workflow 的成本—成功率曲线。

---

## Idea 2：带权限分层与审计轨迹的多工具协作安全治理层

### 问题定义
当多个 agent 可以访问搜索、代码、终端、文件、浏览器或外部 API 时，真实风险不只来自单次错误调用，而来自**长轨迹、多工具、跨 agent 传递后的越权累积**。目标是构建一层治理机制，对 multi-agent + multi-tool 系统做权限控制、轨迹审计与高风险动作拦截。

### 为什么值得做
`ten-survey-synthesis-report.md` 与 `ten-survey-structured-reading-notes.md` 都指出：安全、治理、开放环境适应是 2026 年开始被集中讨论的空白点。尤其 **Xu 2026** 已将 safety and control、industrial-grade governance 列为核心议题，但现有综述更多是问题归纳，真正可运行的治理层仍然少。

### 与现有综述的关系
- **Xu 2026**：直接讨论 multi-tool orchestration 的安全与治理。
- **Yan 2025 / Chen 2026**：说明通信内容本身也可能成为攻击传播媒介。
- **Guo 2024 / Tran 2025**：都把风险、伦理与安全视为多智能体扩展的瓶颈。
- 来源：`ten-survey-structured-reading-notes.md`；`ten-survey-synthesis-report.md` 第 4.2、4.4 节。

### 可行方法
1. 定义三层 capability schema：agent 能做什么、tool 能做什么、memory 可写什么。
2. 对每个 tool call 打标签：读/写、低风险/高风险、可逆/不可逆。
3. 插入 governance agent：遇到高风险调用时强制二次论证或双 agent 共识。
4. 对历史轨迹做 sequence anomaly detection，发现异常工具链或越权传播。
5. 对消息做 prompt injection / malicious instruction 扫描，防止通信污染后续 agent。

### 数据/benchmark
- `MCP-Bench`, `Terminal-Bench`, `RepoBench`, `AndroidArena`, `LiveMCPBench`
- 证据来源：`ten-survey-structured-reading-notes.md` 中 Xu 2026 条目。

### 评测指标
- 正常任务成功率
- 恶意样本拦截率
- 误拦截率（false positive）
- 风险动作平均确认延迟
- 越权调用数 / 任务
- 安全治理带来的 token 开销

### 预期难点
- 安全层可能显著增加时延与交互成本。
- 很多风险不是单步可见，而是跨 5~10 步累积才显现。
- 既要防注入，又不能把正常 delegation 都视为异常。

### 最小可执行原型
做一个 **有限工具沙盒**：web_search、read_file、write_file、run_shell 四种工具；定义 3 条高风险规则（写系统文件、执行 shell 写操作、跨目录写入）。先在合成攻击任务和正常任务上比较“无治理”和“带治理层”的安全/效率差异。

---

## Idea 3：面向长时任务的共享记忆分层与冲突消解机制

### 问题定义
多智能体长期协作时，常见失败不是“不会做”，而是**记忆污染、事实漂移、不同 agent 写入互相冲突、旧结论覆盖新证据**。这个 idea 研究如何构建分层共享记忆，并让 agent 在冲突出现时自动做证据核验与版本合并。

### 为什么值得做
`ten-survey-synthesis-report.md` 把“长期、真实、可治理 benchmark 缺失”列为核心空白；`ten-survey-structured-reading-notes.md` 中 **Aratchige 2025** 和 **Wang 2026** 都把 memory 单列为关键技术。对现实仓库式 agent 系统而言，这比再多加一个 planner 更关键。

### 与现有综述的关系
- **Aratchige 2025**：memory 是高效 LLM-MAS 的四大技术基座之一。
- **Wang 2026**：角色记忆、事件记忆与长期一致性是 role-playing systems 的核心。
- **Guo 2024**：agent profiling、management 与 orchestration efficiency 暗含共享状态管理问题。
- 来源：`ten-survey-structured-reading-notes.md`；`ten-survey-synthesis-report.md` 第 5 节“对本仓库 agent 集群的启发”。

### 可行方法
1. 把记忆分成三层：
   - 个体工作记忆（private scratchpad）
   - 团队候选事实层（unverified shared memory）
   - 已复核事实层（verified memory）
2. 每条共享事实都记录 provenance：来源 agent、文件路径、时间戳、证据句。
3. 一旦检测到冲突（同一实体两个相斥结论），自动触发 verifier agent 复核。
4. 引入 memory TTL：过期事实必须重新验证。
5. 设计 memory write policy：不同角色对不同槽位拥有不同写权限。

### 数据/benchmark
- 通用任务：`GAIA`, `AgentBench`, `MultiAgentBench`
- 角色/长期一致性：`RoleBench`, `RoleEval`, `CharacterEval`
- 证据来源：`ten-survey-structured-reading-notes.md` 中 Chen 2025、Yan 2025、Wang 2026 条目。

### 评测指标
- 长任务成功率
- 事实冲突率
- 冲突恢复时延
- 错误共享记忆传播深度
- 记忆命中率 / 误命中率
- 长期一致性评分

### 预期难点
- “冲突”不总是二值的，有时只是粒度不同或时间过期。
- 过多 provenance 会让存储与检索成本上升。
- 共享记忆越强，错误一旦写入传播也越快。

### 最小可执行原型
在一个仓库问答/文档整理场景里，做 **两层记忆系统**：candidate memory + verified memory。只实现一条规则：任何将被写入 verified 的事实都要被第二个 agent 复核。先测冲突率和最终事实准确率变化。

---

## Idea 4：通信内容压缩与优先级调度的统一协议

### 问题定义
多智能体消息常常太长、太重复、太晚到，导致延迟和成本失控。研究问题是：**能否把消息压缩为结构化摘要，并根据任务状态动态分配消息优先级，从而在不明显损害效果的前提下降低通信成本？**

### 为什么值得做
`ten-survey-synthesis-report.md` 第 4.2 节指出通信层指标缺失；`ten-survey-structured-reading-notes.md` 中 **Yan 2025** 和 **Chen 2026** 都把 communication object/content/when/why 作为关键维度，**Wu 2025** 则提供了高实时、多主体场景的强需求牵引。

### 与现有综述的关系
- **Yan 2025**：system-level 与 internal communication 结构说明消息内容和协议可以被设计。
- **Chen 2026**：5W 框架非常适合做“该不该发、发给谁、发什么”的决策模板。
- **Wu 2025**：自动驾驶协作场景体现了带宽与时延约束。
- 来源：`ten-survey-structured-reading-notes.md`。

### 可行方法
1. 为消息定义四类标签：状态、计划、风险、协作请求。
2. 用 teacher-student 蒸馏：teacher 生成完整自由文本，student 压缩成结构化消息槽位。
3. 引入优先级函数：高风险、强依赖、时效性高的消息先发送。
4. 对低价值消息使用合并/跳过机制，只在状态发生显著变化时广播。
5. 为不同任务设计不同协议模板，但统一日志格式。

### 数据/benchmark
- 通用：`MultiAgentBench`, `GAIA`, `RoCoBench`
- 领域：`Waymo Open Motion Dataset` 相关多主体自动驾驶任务
- 证据来源：`ten-survey-structured-reading-notes.md` 中 Guo 2024、Yan 2025、Chen 2026、Wu 2025 条目。

### 评测指标
- 平均消息 token 长度
- 总通信 token
- 平均决策延迟
- 任务成功率
- 消息冗余率
- 高优先级消息到达及时率

### 预期难点
- 结构化压缩可能丢失隐含语义。
- 低频通信在简单任务有效，但在强耦合任务可能导致灾难性遗漏。
- 优先级调度需要可靠估计风险与依赖关系。

### 最小可执行原型
在 3-agent 协作文档问答或路线规划任务上，比对三种通信协议：
1. 原始自由文本；
2. 固定模板压缩；
3. 动态优先级压缩。
先看消息 token 节省率与成功率变化。

---

## Idea 5：面向真实工作流的多智能体 benchmark 统一日志协议

### 问题定义
当前多智能体 benchmark 分裂严重：有的只看最终答案，有的看工具调用，有的看角色一致性，有的看安全，结果导致不同系统几乎不可横向比较。这个 idea 的目标是：**设计一套可跨 benchmark 使用的统一日志协议和六维评测框架。**

### 为什么值得做
`ten-survey-synthesis-report.md` 与 `ten-survey-quick-overview.md` 都反复指出 benchmark fragmentation 是十篇综述的共识问题。若没有统一日志协议，很多所谓“multi-agent 改进”根本无法诊断是来自通信、结构、更多 token 还是更多工具。

### 与现有综述的关系
- **Guo 2024 / Chen 2025**：都系统梳理 benchmark，但覆盖范围广、口径不统一。
- **Yan 2025 / Chen 2026**：提示通信质量不能只由任务分数替代。
- **Xu 2026 / Yue 2026**：进一步要求记录 tool-use trace 与 workflow graph。
- **Wang 2026**：补充角色一致性和长期互动指标。
- 来源：`ten-survey-synthesis-report.md` 第 4.2、4.4 节；`ten-survey-structured-reading-notes.md`。

### 可行方法
1. 设计统一 schema，最少包含：
   - task result
   - communication log
   - workflow graph
   - tool-call trace
   - memory events
   - safety events
2. 设计六维评测：效果、成本、结构质量、通信质量、安全、长期一致性。
3. 为不同 benchmark 做 adapter，把原始结果映射到统一 schema。
4. 出一套 review checklist，要求论文或系统报告必须附关键统计。
5. 用 Pareto frontier 而不是单一总分比较系统。

### 数据/benchmark
- `AgentBench`, `MultiAgentBench`, `GAIA`, `WorkflowBench`, `MCP-Bench`, `RoleBench`
- 来源：`ten-survey-structured-reading-notes.md` 多篇条目中的 benchmark 列表。

### 评测指标
- 跨 benchmark 字段覆盖率
- 复现实验成功率
- 解释失败案例的时间成本
- 不同系统六维 Pareto 前沿质量
- 缺失字段率

### 预期难点
- 不同 benchmark 的原始日志粒度差异极大。
- 统一 schema 容易设计得太重，增加接入成本。
- 长期一致性和安全事件很难标准化。

### 最小可执行原型
先只支持三个 benchmark：`GAIA`、`WorkflowBench`、`MCP-Bench`。实现一个日志转换器，把三者统一输出成相同 JSON schema，并生成一张六维雷达图。

---

## Idea 6：角色—动机—关系联合建模的社会型多智能体系统

### 问题定义
目前很多 role-playing 或 social agents 仍停留在“给定角色描述 + 对话生成”，缺少长期动机、关系网络和记忆一致性。这个 idea 研究：**如何让多个角色 agent 在长期互动中保持人格一致、关系可追踪、行为有内在动机。**

### 为什么值得做
`ten-survey-structured-reading-notes.md` 中 **Wang 2026** 明确指出 role-playing agents 正从模板走向人格/记忆/行为建模；`ten-survey-synthesis-report.md` 也将 role-play/social agents 列为 2026 年独立增长主线。相比通用问答 agent，这类系统更能暴露长期一致性与社会交互问题。

### 与现有综述的关系
- **Wang 2026**：提供 personality、memory、behavior modeling 与 role-specific evaluation 的完整框架。
- **Chen 2025**：强调 world simulation / generative agents 的应用前沿。
- **Guo 2024**：把 world simulation 作为重要应用类别。
- 来源：`ten-survey-structured-reading-notes.md`。

### 可行方法
1. 每个角色持有三类状态：人格设定、长期目标、社会关系图。
2. 记忆分为事件记忆、关系记忆、价值记忆。
3. 决策时不仅看当前对话，还看“角色—关系—动机”三元组。
4. 加入 narrative critic：定期检查角色是否违背已知人格与关系历史。
5. 让系统可以在多轮后生成“社会状态摘要”，而不是只生成下一句回复。

### 数据/benchmark
- `RoleBench`, `RoleEval`, `RoleEval-Chinese`, `CharacterEval`, `RMTBench`
- 来源：`ten-survey-structured-reading-notes.md` 中 Wang 2026 条目。

### 评测指标
- 人格一致性分数
- 长期叙事连贯性
- 关系图稳定性
- 行为可解释性评分
- 人类偏好评分
- 互动幻觉率

### 预期难点
- “人格一致”很容易被模型表面风格伪装出来。
- 长期关系变化既不能僵死，也不能无缘无故漂移。
- 标注和人工评价成本高。

### 最小可执行原型
构建一个 **4 角色长对话世界**：每个角色有固定初始关系和目标，运行 20~30 轮互动；比较“仅 prompt 设定角色”与“角色+记忆+关系图”的长期一致性差异。

---

## Idea 7：面向协作收益因果拆解的 controlled multi-agent ablation suite

### 问题定义
许多工作声称 multi-agent 比 single-agent 更强，但并未控制 token 预算、工具访问、采样次数、外部信息来源，因而无法证明收益真的来自协作机制。这个 idea 的目标是建立一套**因果拆解实验框架**，严格区分“多 agent 带来的收益”和“更多计算带来的收益”。

### 为什么值得做
`ten-survey-synthesis-report.md` 第 4.1 节明确指出“协作收益缺少因果拆解”是核心空白。这个问题如果不解决，后续关于 communication、workflow、role 或 tool-use 的改进都很容易被高估。

### 与现有综述的关系
- **Tran 2025**：讨论 collaboration mechanisms，但还需要更严格的比较协议。
- **Yan 2025 / Chen 2026**：给出了通信结构维度，可作为控制变量。
- **Yue 2026 / Xu 2026**：给出了 workflow / tool-use 维度，也可作为控制变量。
- 来源：`ten-survey-synthesis-report.md` 第 4.1 节；`ten-survey-structured-reading-notes.md`。

### 可行方法
1. 为每个任务构造等预算对照：
   - 单 agent，多采样
   - 双 agent，无互聊
   - 双 agent，固定互聊
   - 双 agent，动态互聊
2. 固定工具集、固定检索结果、固定总 token budget。
3. 逐个打开变量：角色分工、通信次数、workflow 编辑、critic 节点。
4. 用 bootstrap 或 mixed-effects model 估计各因素贡献。
5. 记录失败模式，看协作是否真的减少系统性错误。

### 数据/benchmark
- `GSM8K`, `HumanEval`, `GAIA`, `AgentBench`, `MultiAgentBench`
- 来源：`ten-survey-structured-reading-notes.md` 中 Guo 2024、Chen 2025、Yue 2026 条目。

### 评测指标
- 等预算下成功率差异
- 每个机制的增益贡献
- 错误类型转移矩阵
- 成本归因图
- 结果方差

### 预期难点
- 很难做到真正“等价预算”；不同结构的 token 利用效率不同。
- 同一任务上存在较高随机性，需要多次重复试验。
- 协作收益可能高度依赖任务类型，难以得出统一结论。

### 最小可执行原型
先在 `GSM8K` 和 `HumanEval` 上做 **四条件对照**，每条件固定总 token 预算。只研究一个变量：是否允许 agent 间互聊。输出增益归因图和失败样例。

---

## Idea 8：面向开放环境的自适应工具发现与可靠调用链构建

### 问题定义
真实环境里的 agent 不可能永远只面对一个固定工具箱。研究问题是：**当系统进入开放环境时，如何发现新工具、判断是否值得使用、并把它们安全地接入已有工作流？**

### 为什么值得做
`ten-survey-structured-reading-notes.md` 里 **Xu 2026** 把 autonomous tool expansion、open environment adaptation 明确列为未来方向；`ten-survey-synthesis-report.md` 也把开放环境中的治理和可验证性视为重要空白。相比“工具调用更准”，这个问题更接近真实 agent 平台的长期演化需求。

### 与现有综述的关系
- **Xu 2026**：直接支持该方向，且给出了多工具 orchestration 与治理问题空间。
- **Yue 2026**：可把新工具接入看成 workflow graph 的结构扩展。
- **Aratchige 2025**：从 architecture / frameworks 角度说明技术基建的重要性。
- 来源：`ten-survey-structured-reading-notes.md`。

### 可行方法
1. 把工具发现拆成三步：候选发现、能力摘要、沙盒试用。
2. 为每个新工具生成 capability card：输入输出、代价、风险、适用场景。
3. 先在离线 sandbox 里执行试探性调用，记录成功率和错误模式。
4. 通过 tool graph planner 决定新工具进入现有工作流的插入点。
5. 使用回滚机制：新工具若引入异常，则自动降级回旧工作流。

### 数据/benchmark
- `MCP-Bench`, `RestBench`, `RepoBench`, `Terminal-Bench`, `Mobile-Bench`
- 来源：`ten-survey-structured-reading-notes.md` 中 Xu 2026 条目。

### 评测指标
- 新工具发现后带来的任务成功率增益
- 工具描述准确率
- 首次接入成功率
- 调用链回滚率
- 风险事件率
- 接入成本（人工/自动）

### 预期难点
- 新工具的接口文档可能不完整或不可靠。
- 工具能力评估和真实环境表现容易不一致。
- 开放工具引入后会显著扩大攻击面。

### 最小可执行原型
做一个小型开放工具库（5~10 个模拟 API），让 agent 先阅读 capability card，再通过 sandbox 测试决定是否接入。只测两件事：选对工具的比例、失败后回滚是否稳定。

---

## Idea 9：多主体自动驾驶中的风险驱动协作与异常恢复机制

### 问题定义
自动驾驶场景里的多智能体协作不只需要“正常情况下更高效”，更需要**在高风险、部分观测、通信受限条件下安全恢复**。这个 idea 聚焦：如何让多车/车路/车人系统在异常事件发生时快速重组协作结构。

### 为什么值得做
十篇综述里，**Wu 2025** 是最明确的垂直高风险场景综述；同时 `ten-survey-synthesis-report.md` 第 4.4 节指出缺少“长期、真实、可治理 benchmark”。自动驾驶刚好同时具备实时性、安全性和协作需求，是验证通信与工作流理论的强场景。

### 与现有综述的关系
- **Wu 2025**：提供多车、车路、车助理、人与 agent 协作分类。
- **Yan 2025 / Chen 2026**：提供通信设计框架，可用于高风险消息的选择与优先级调度。
- **Yue 2026**：可将异常恢复视为 runtime graph reconfiguration。
- 来源：`ten-survey-structured-reading-notes.md`。

### 可行方法
1. 定义风险状态机：正常、可疑、紧急、恢复。
2. 在不同状态下切换通信与决策模式：
   - 正常：局部低频通信
   - 可疑：提升高风险消息频率
   - 紧急：中心化协调
   - 恢复：逐步降级回分布式
3. 让异常恢复策略不仅输出动作，还输出“重新组织的协作拓扑”。
4. 用 teacher planner 生成理想协作拓扑，再蒸馏给轻量 student。

### 数据/benchmark
- `Waymo Open Motion Dataset` 与综述中提到的 multi-agent ADS benchmarks
- 来源：`ten-survey-structured-reading-notes.md` 中 Wu 2025 条目。

### 评测指标
- 碰撞率 / 违规率
- 异常事件恢复时间
- 风险消息触发及时率
- 协作重构成功率
- 通信带宽占用

### 预期难点
- 真实驾驶风险样本稀缺，长尾事件难覆盖。
- 模拟器中的协作收益不一定能迁移到现实部署。
- 安全指标高度敏感，实验设计门槛高。

### 最小可执行原型
先在仿真路口会车和并线两个场景里做 **双车 + 路侧单元** 的协作恢复实验。只测试一条机制：检测到冲突风险后是否切换到高优先级中心协调模式。

---

## Idea 10：从综述证据链到自动选题的“research gap miner”

### 问题定义
现在做综述后的 research ideation 仍很手工：人要读完大量 survey，人工归纳空白、再转成选题。这个 idea 研究：**能否让 agent 自动从综述的 future directions、limitations、benchmark 缺口中提取可操作的研究题目，并给出证据链。**

### 为什么值得做
本项目本身已经完成 10 篇综述精读、横向比较和 idea 生成，说明这是高频研究工作流。`ten-survey-synthesis-report.md` 与 `ten-survey-quick-overview.md` 已经把“空白问题、时间演化、主线趋势”结构化了，如果能进一步自动化，就能把综述阅读直接转成研究 pipeline。

### 与现有综述的关系
- **Guo 2024 / Chen 2025**：提供 broad landscape，适合作为主题空间。
- **Yan 2025 / Chen 2026 / Tran 2025**：提供 communication/collaboration 子问题模板。
- **Xu 2026 / Yue 2026**：提供 workflow、tool、governance 的具体开放问题。
- **Wang 2026 / Wu 2025**：提供垂直场景与社会型场景扩展。
- 来源：`ten-survey-structured-reading-notes.md`、`ten-survey-synthesis-report.md`、`ten-survey-quick-overview.md`。

### 可行方法
1. 从结构化综述笔记中抽取四类句子：limitations、future directions、benchmark gaps、evaluation critiques。
2. 对这些句子聚类，形成 gap taxonomy。
3. 用模板把 gap 转成 research idea：
   - 缺什么能力
   - 可在哪类 benchmark 上做
   - 最小原型是什么
4. 给每个 idea 自动生成 evidence map，列出对应综述和原始位置。
5. 增加 novelty filter：与已有 idea 高重叠时自动合并或降权。

### 数据/benchmark
- 输入数据直接来自本项目现有文档：
  - `2026-03-26-ten-survey-structured-reading-notes.md`
  - `2026-03-26-ten-survey-synthesis-report.md`
  - `2026-03-26-ten-survey-quick-overview.md`
- 若需要下游验证，可在 `GAIA`, `WorkflowBench`, `MultiAgentBench`, `RoleBench`, `MCP-Bench` 上测试自动生成 idea 的可执行性。

### 评测指标
- 自动抽取 gap 的准确率
- idea 去重率
- 人工评审的新颖性/可做性评分
- evidence completeness（每个 idea 对应综述证据数）
- 从综述到实验计划的平均时间节省

### 预期难点
- survey 里的“future work”常很泛，自动转译成具体题目不容易。
- novelty 评估需要上下文，不能只靠文本相似度。
- 需要避免生成“看起来像 idea、实际上无法做”的空洞题目。

### 最小可执行原型
只对本项目现有 10 篇笔记做一个 **gap extraction + idea templating** 脚本，输出前 20 个候选 gap 和前 5 个自动生成 idea，再由人工快速打分验证质量。

---

## 十个 idea 的去重检查

为避免只是把同一个方向换说法，按核心研究对象可分为 6 类：

1. **通信—工作流联合优化**：Idea 1
2. **治理与安全**：Idea 2、Idea 8
3. **共享记忆与长期一致性**：Idea 3、Idea 6
4. **通信协议效率**：Idea 4、Idea 9
5. **评测与因果归因**：Idea 5、Idea 7
6. **研究流程自动化**：Idea 10

其中同类 idea 的区别为：
- Idea 2 偏“已有工具的权限治理”，Idea 8 偏“开放环境中新工具接入”；
- Idea 3 偏“团队共享记忆正确性”，Idea 6 偏“角色人格与社会一致性”；
- Idea 4 偏“通用消息压缩协议”，Idea 9 偏“自动驾驶中的高风险异常恢复”；
- Idea 5 偏“统一日志与评测协议”，Idea 7 偏“协作收益的受控因果拆解”。

## 建议优先级（供后续会话参考，不视为新任务）

### 短期最适合启动
1. **Idea 1**：预算感知的动态通信—工作流联合优化器
2. **Idea 2**：带权限分层与审计轨迹的多工具协作安全治理层
3. **Idea 5**：面向真实工作流的多智能体 benchmark 统一日志协议

### 中期高价值方向
4. **Idea 3**：面向长时任务的共享记忆分层与冲突消解机制
5. **Idea 7**：面向协作收益因果拆解的 controlled ablation suite
6. **Idea 8**：开放环境中的自适应工具发现与可靠调用链构建

### 高风险高收益方向
7. **Idea 6**：角色—动机—关系联合建模的社会型多智能体系统
8. **Idea 9**：多主体自动驾驶中的风险驱动协作与异常恢复机制
9. **Idea 10**：从综述证据链到自动选题的 research gap miner
10. **Idea 4**：通信内容压缩与优先级调度的统一协议

## 结论

这 10 个 idea 并非平铺直叙地“多写 5 个”，而是把十篇综述反复出现的主线空白拆成了六个互补方向：

- communication/workflow 联合优化
- 安全治理与开放工具生态
- 共享记忆与长期一致性
- 通信压缩与高风险协作
- 统一评测与因果归因
- 综述到选题的自动化 pipeline

如果后续只做 1 个启动项目，最稳妥的是 **Idea 1**；如果更偏系统落地，优先 **Idea 2**；如果目标是给整个领域补基础设施，优先 **Idea 5**。