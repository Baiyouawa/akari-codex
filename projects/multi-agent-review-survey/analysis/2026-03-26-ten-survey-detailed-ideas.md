# 2026-03-26 基于 10 篇 multi-agent 综述共同空白与差异的 10 个详细 research ideas（按最终字段重写）

- Timestamp: 2026-03-26T02:19:21+08:00
- Session: 柑奈-02-1774462721-f2ece3
- Scope: 将项目内 canonical 10 篇综述的共同空白与差异，重写为满足最终任务字段要求的 10 个详细 research ideas。
- Required fields: 题目、背景动机、核心问题、创新点、方法设计、实验方案、数据/benchmark、评价指标、风险点、最小可行原型
- Primary sources:
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
  - `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`

## 方法说明

本文件不新增未经项目内证据链核验的新论文结论，只把已落盘的十篇综述中的共同空白与主要差异具体化为可执行研究方向。所有方向都可回链到以下已落盘结论：

1. `ten-survey-synthesis-report.md` 已明确指出四类主空白：协作收益缺少因果拆解、通信层指标不足、workflow/tool/communication 割裂、长期真实可治理 benchmark 缺失。
2. `ten-survey-quick-overview.md` 已明确指出五类主趋势：专题化深化、通信成为核心变量、工程系统视角增强、benchmark 碎片化、社会型 agents 兴起。
3. `ten-survey-structured-reading-notes.md` 已逐篇记录 communication、collaboration、tool-use、workflow、role-playing、autonomous driving、memory/planning 等差异化重点。

---

## Idea 1：预算感知的通信—工作流联合优化器

### 题目
预算感知的通信—工作流联合优化器：在固定成本下动态重组多智能体协作图

### 背景动机
项目内综合报告指出，Yan 2025 / Chen 2026 聚焦 communication，Yue 2026 聚焦 workflow graph，Xu 2026 聚焦 tool orchestration，但现实系统里三者是强耦合的；当前文献仍常把它们分开讨论。来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`。

### 核心问题
在固定 token、时间与工具调用预算下，系统应如何同时决定：谁与谁通信、何时通信、是否插入 verifier/critic、工作流图是否需要串并转换，才能最大化任务成功率？

### 创新点
1. 把 communication edge 与 workflow edge 放进同一个 runtime graph 中统一优化。
2. 用“单位成本成功率”而非单纯 accuracy 作为主优化目标。
3. 将是否通信、是否复核、是否重组工作流看成同一类图编辑动作。

### 方法设计
1. 用有向图表示 agent workflow；节点为 planner / worker / tool-agent / critic，边为消息或依赖关系。
2. 定义运行时动作集合：增删通信边、插入 verifier、并行化子图、降级为单 agent、切换工具调用路径。
3. 设计 meta-controller，输入任务状态、不确定度、已消耗预算，输出图编辑动作。
4. 奖励函数同时考虑成功率、token 成本、wall-clock time、结构稳定性。
5. 使用 rule-based warm start：高不确定度时增加复核，低不确定度时压缩通信。

### 实验方案
- 对比四类系统：
  1. 固定 workflow + 固定通信；
  2. 固定 workflow + 动态通信；
  3. 动态 workflow + 固定通信；
  4. 联合动态优化。
- 在相同 token 预算下画 success-cost 曲线。
- 对失败案例做归因：失败是因为信息不足、通信冗余还是结构错误。

### 数据/benchmark
`WorkflowBench`, `GAIA`, `SOP-Bench`, `MultiAgentBench`, `AgentBench`。
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Yue 2026、Yan 2025、Chen 2024 条目。

### 评价指标
- 任务成功率 / pass@k
- 总 token 成本
- wall-clock latency
- 平均通信轮数
- 图编辑次数
- 单位成本成功率（success per 1k tokens）

### 风险点
- 多目标优化不稳定；
- 不同任务最优拓扑不同，泛化难；
- controller 可能学到“省成本但不解决问题”的退化策略。

### 最小可行原型
做一个 3 节点系统（planner + worker + critic），只允许两种图编辑：
1. 增加一次 critic 复核；
2. 关闭一条 worker 间通信边。
在 `GAIA` 子集与 `WorkflowBench` 子集上比较固定图与动态图。

---

## Idea 2：带权限分层与审计轨迹的多工具协作安全治理层

### 题目
多工具协作 agent 的权限—审计双层治理：面向开放环境越权与长轨迹风险

### 背景动机
综合报告明确指出，安全、治理、开放环境适应是 2026 年系统综述集中暴露的空白；Xu 2026 尤其强调 multi-tool orchestration 的 safety and control。来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`。

### 核心问题
多智能体共享搜索、文件、终端、浏览器、API 等工具时，如何在不显著压垮效率的前提下，控制越权、注入传播、危险调用链和跨 agent 风险累积？

### 创新点
1. 把权限控制从“单 agent 单工具”升级到“多 agent 多工具 长轨迹”级别。
2. 将 capability schema、轨迹异常检测、二次确认机制合并成统一治理层。
3. 把通信内容视为攻击面的一部分，而不是只检查 tool call。

### 方法设计
1. 为 agent、tool、memory 三层定义 capability schema。
2. 将工具调用标注为读/写、低/高风险、可逆/不可逆。
3. 引入 governance agent，对高风险操作强制二次论证或双 agent 共识。
4. 对消息流和工具流做 sequence anomaly detection，识别异常链路。
5. 在通信侧加入 prompt injection / malicious instruction 扫描。

### 实验方案
- 构造三类任务：正常任务、显式恶意任务、正常任务中夹带注入片段。
- 对比：无治理、静态白名单治理、动态治理层。
- 测量安全提升与正常任务性能损失。

### 数据/benchmark
`MCP-Bench`, `Terminal-Bench`, `RepoBench`, `AndroidArena`, `LiveMCPBench`。
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Xu 2026 条目。

### 评价指标
- 正常任务成功率
- 恶意样本拦截率
- 误拦截率
- 平均审批延迟
- 越权调用数 / task
- 治理额外 token 开销

### 风险点
- 安全层可能过重，显著增加时延；
- 风险检测规则过于保守会误杀正常 delegation；
- 长轨迹风险常在后段显现，早期信号弱。

### 最小可行原型
在一个仅含 `web_search`、`read_file`、`write_file`、`run_shell` 的受限工具沙盒里，先实现三条高风险规则和一个二次确认 agent，比对有无治理层的安全/效率差异。

---

## Idea 3：面向长时任务的共享记忆分层与冲突消解机制

### 题目
多智能体共享记忆的分层写入与冲突消解：从候选事实到已验证事实

### 背景动机
Aratchige 2025 把 memory 列为关键技术底座，Wang 2026 把角色记忆与长期一致性列为核心问题；综合报告也强调长期真实任务中的共享记忆与事实漂移问题。来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`。

### 核心问题
多个 agent 长时间协作时，如何防止错误事实进入共享记忆、不同 agent 的结论互相冲突、旧信息覆盖新证据、以及错误信息被快速传播？

### 创新点
1. 把共享记忆拆成 candidate layer 与 verified layer。
2. 让 provenance 成为写入条件，而非附加说明。
3. 把“冲突检测—复核—升级/淘汰”做成自动闭环。

### 方法设计
1. 记忆分三层：private scratchpad、shared candidate memory、verified memory。
2. 每条共享事实都带来源 agent、文件路径、时间戳、证据句。
3. 检测同实体/同结论的相斥项并触发 verifier agent。
4. 引入 TTL 与 refresh policy，过期事实必须重验。
5. 定义角色化写权限：检索 agent 负责 candidate，复核 agent 负责 verified。

### 实验方案
- 在仓库研究任务或文档整理任务上构造长链协作。
- 对比：无共享记忆、统一共享记忆、分层共享记忆。
- 插入冲突证据和过时证据，比较系统恢复能力。

### 数据/benchmark
`GAIA`, `AgentBench`, `MultiAgentBench`, `RoleBench`, `RoleEval`。
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Chen 2024、Yan 2025、Wang 2026 条目。

### 评价指标
- 长任务成功率
- 事实冲突率
- 冲突恢复时延
- 错误传播深度
- 记忆命中率 / 误命中率
- 长期一致性评分

### 风险点
- provenance 记录会增加存储与检索成本；
- 冲突并非总是二元真/假；
- 分层机制可能拖慢正常写入。

### 最小可行原型
在一个仓库问答场景里只实现两层共享记忆：candidate + verified。规定“写入 verified 的事实必须被第二个 agent 复核”，先测事实准确率与冲突率变化。

---

## Idea 4：通信内容压缩与优先级调度的统一协议

### 题目
面向多智能体协作的结构化消息压缩与风险优先级调度协议

### 背景动机
Yan 2025 与 Chen 2026 把 communication object/content/when/why 明确化，Wu 2025 显示在高实时场景下通信成本与时延非常关键。来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`。

### 核心问题
多智能体消息常常过长、重复、低价值；如何在不明显损伤效果的前提下，把自由文本通信压缩成结构化消息，并根据风险与依赖动态调度发送顺序？

### 创新点
1. 把消息分为状态、计划、风险、协作请求四类并分别压缩。
2. 统一设计“压缩格式 + 发送优先级”而不是只做摘要。
3. 把风险感知调度用于通用任务与高实时任务的共享协议。

### 方法设计
1. 定义统一消息 schema：type、receiver、urgency、payload、confidence。
2. 用 teacher-student 蒸馏把完整对话压成结构化槽位。
3. 基于任务不确定度和依赖强度计算消息优先级。
4. 对低价值消息做合并与跳过，对高风险消息强制广播或确认。
5. 记录压缩前后消息，便于误差分析。

### 实验方案
- 比较三种协议：原始自由文本、固定模板压缩、动态优先级压缩。
- 在文档协作、路线规划、高风险冲突协调三类任务上测试。
- 额外做 ablation：只压缩不调度、只调度不压缩。

### 数据/benchmark
`MultiAgentBench`, `GAIA`, `RoCoBench`；若做垂直场景扩展，可接 `Waymo Open Motion Dataset` 相关任务。
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Guo 2024、Wu 2025、Yan 2025、Chen 2026 条目。

### 评价指标
- 平均消息长度
- 总通信 token
- 平均决策延迟
- 任务成功率
- 消息冗余率
- 高优先级消息及时送达率

### 风险点
- 压缩可能丢失隐含约束；
- 优先级估计错误会导致关键信息迟到；
- 不同任务的最优 schema 不一致。

### 最小可行原型
在 3-agent 协作文档问答任务上，先将自由文本通信替换为四槽位消息格式，再加入简单的“高风险优先”队列，测 token 降幅与成功率变化。

---

## Idea 5：面向真实工作流的多智能体 benchmark 统一日志协议

### 题目
AgentBench 之后：面向 communication、workflow、tool-use、memory 与 safety 的统一日志协议

### 背景动机
综合报告与横向速览反复指出 benchmark fragmentation：communication 看一套、workflow 看一套、role-play 看一套、tool-use 看一套，导致系统横向比较困难。来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`。

### 核心问题
如何设计一个可跨多类 agent benchmark 使用的统一日志协议，使研究者能同时记录结果、成本、结构、通信、安全与长期一致性，而不是只报最终得分？

### 创新点
1. 统一 communication / workflow / tool / memory / safety 五类轨迹字段。
2. 从“单一总分”转为“六维 Pareto 评价”。
3. 为不同 benchmark 设计 adapter 而不是强推单一评测任务。

### 方法设计
1. 设计统一 schema：task result、workflow graph、communication log、tool-call trace、memory events、safety events。
2. 抽象六维指标：效果、成本、结构质量、通信质量、安全、长期一致性。
3. 为 `GAIA`、`WorkflowBench`、`MCP-Bench` 等实现日志转换器。
4. 提供自动生成雷达图与 Pareto frontier 的分析脚本。
5. 附带 review checklist，约束论文报告字段完整性。

### 实验方案
- 先接三类 benchmark：通用任务、workflow 任务、tool-use 任务。
- 评估 schema 覆盖率、接入成本、复现实验的便利性。
- 用统一协议重跑两个已有系统，比较是否能更好解释胜负来源。

### 数据/benchmark
`AgentBench`, `MultiAgentBench`, `GAIA`, `WorkflowBench`, `MCP-Bench`, `RoleBench`。
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 多篇条目。

### 评价指标
- 跨 benchmark 字段覆盖率
- 日志缺失率
- 复现实验成功率
- 失败归因时间成本
- 六维报告完整性

### 风险点
- schema 设计过重，导致接入门槛高；
- 某些维度很难标准化；
- 不同 benchmark 的原始粒度差异很大。

### 最小可行原型
仅支持 `GAIA`、`WorkflowBench`、`MCP-Bench` 三个 benchmark，输出统一 JSON schema 与一个六维可视化面板。

---

## Idea 6：角色—动机—关系联合建模的社会型多智能体系统

### 题目
角色—动机—关系联合建模：面向长期叙事一致性的社会型 multi-agent 系统

### 背景动机
Wang 2026 表明 role-playing agents 已从模板式人设转向人格、记忆、行为与关系建模；综合报告指出社会型 agents 正在成为独立方向。来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Wang 2026 条目；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`。

### 核心问题
如何让多个角色 agent 在长期互动中保持人格一致、动机可解释、关系可追踪，而不是只在局部对话里“像某个角色”？

### 创新点
1. 将人格、长期目标、社会关系图统一纳入决策状态。
2. 区分事件记忆、关系记忆、价值记忆三类社会型记忆。
3. 用 narrative critic 检查长期角色漂移，而不是只测单轮风格相似度。

### 方法设计
1. 为每个角色维护人格向量、长期目标、关系 embedding。
2. 记忆按事件/关系/价值分槽存储。
3. 通过动机—情境—关系三元组驱动下一步行动选择。
4. 让 critic 定期比较当前行为与历史设定是否冲突。
5. 生成社会状态摘要，作为长期上下文压缩形式。

### 实验方案
- 构造 4 角色长对话世界，运行 20–30 轮互动。
- 对比：仅 prompt 角色设定、角色+长期记忆、角色+记忆+关系图。
- 让人工与自动指标共同评价人格一致性和关系稳定性。

### 数据/benchmark
`RoleBench`, `RoleEval`, `RoleEval-Chinese`, `CharacterEval`, `RMTBench`。
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Wang 2026 条目。

### 评价指标
- 人格一致性
- 长期叙事连贯性
- 关系图稳定性
- 行为可解释性
- 人类偏好评分
- 互动幻觉率

### 风险点
- 人格一致可能被表面语言风格伪装；
- 长期标注成本高；
- 社会关系既不能僵死，也不能无故漂移。

### 最小可行原型
做一个 4 角色小型世界，给每个角色固定初始关系和目标，只比较“有无关系图记忆”对长期一致性的提升。

---

## Idea 7：面向协作收益因果拆解的 controlled ablation suite

### 题目
多智能体真的更强吗：面向协作收益因果拆解的受控实验框架

### 背景动机
综合报告明确指出，现有文献很难严格证明 multi-agent 的提升究竟来自协作机制，还是来自更多 token、更多工具、更多采样。来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`。

### 核心问题
如何在固定预算、固定工具、固定检索条件下，严格拆解角色分工、通信次数、workflow 结构、critic 机制各自带来的真实增益？

### 创新点
1. 把协作机制作为受控变量逐个打开，而不是直接比“单 agent vs 多 agent”。
2. 在等预算前提下做多条件实验，减少“更多计算”混淆。
3. 同时输出错误类型迁移，而非只看平均得分。

### 方法设计
1. 为每类任务构造等预算对照：单 agent、多采样；双 agent、无互聊；双 agent、固定互聊；双 agent、动态互聊。
2. 固定工具集、固定检索结果、固定总 token budget。
3. 用 bootstrap / mixed-effects model 估计各因素贡献。
4. 记录失败类型：信息缺失、重复推理、协调失败、工具误用。

### 实验方案
- 先在数学推理、代码、长任务三类 benchmark 上运行四条件对照。
- 再做 ablation：只加角色，不加通信；只加通信，不加 critic；只加 critic，不改角色。
- 输出归因图和失败案例矩阵。

### 数据/benchmark
`GSM8K`, `HumanEval`, `GAIA`, `AgentBench`, `MultiAgentBench`。
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Guo 2024、Chen 2024、Yue 2026 条目。

### 评价指标
- 等预算成功率差异
- 各机制边际增益
- 错误类型转移矩阵
- 结果方差
- 成本归因图

### 风险点
- “等预算”定义并不总是公平；
- 随机性较大，需要多次重复；
- 结论可能高度依赖任务类别。

### 最小可行原型
先在 `GSM8K` 与 `HumanEval` 上做四条件实验，只研究“是否允许互聊”一个变量，固定总 token 预算并输出增益归因图。

---

## Idea 8：面向开放环境的自适应工具发现与可靠调用链构建

### 题目
从封闭工具箱到开放工具生态：agent 的自适应工具发现与安全接入

### 背景动机
Xu 2026 把 autonomous tool expansion 与 open environment adaptation 明确列为未来方向；这与现有大多数固定工具箱假设形成明显差异。来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Xu 2026 条目。

### 核心问题
在开放环境中，agent 如何发现新工具、判断其能力与风险、决定是否接入当前 workflow，并在失败时稳定回滚？

### 创新点
1. 将“工具发现—能力摘要—沙盒试用—正式接入”做成完整流水线。
2. 为每个新工具生成 capability card 与风险标签。
3. 将工具接入视为 workflow graph 的结构扩展问题。

### 方法设计
1. 从工具描述页/API 文档生成 capability card。
2. 在 sandbox 中执行试探性调用，收集成功率与错误模式。
3. 由 planner 决定新工具在现有 workflow 中的插入位置。
4. 用回滚模块在异常率过高时退回旧工作流。
5. 记录工具选择与失败原因，便于持续更新 capability card。

### 实验方案
- 构建 5–10 个模拟 API 的开放工具库。
- 对比：固定工具箱、开放发现无回滚、开放发现有回滚。
- 测量首接入成功率与回滚稳定性。

### 数据/benchmark
`MCP-Bench`, `RestBench`, `RepoBench`, `Terminal-Bench`, `Mobile-Bench`。
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Xu 2026 条目。

### 评价指标
- 发现后任务增益
- capability card 准确率
- 首次接入成功率
- 回滚率
- 风险事件率
- 自动接入成本

### 风险点
- 文档可能不完整；
- 工具离线评估与真实表现可能不一致；
- 新工具会放大攻击面。

### 最小可行原型
搭一个 5 个模拟 API 的小型开放工具库，只做两件事：自动生成 capability card、sandbox 试用后决定是否接入。

---

## Idea 9：多主体自动驾驶中的风险驱动协作与异常恢复机制

### 题目
高风险场景下的协作重构：多主体自动驾驶中的风险驱动通信与异常恢复

### 背景动机
Wu 2025 展示了自动驾驶中的多车、车路、车助手、人与 agent 协作；该方向与通用综述形成明显差异，因为它把实时性与安全性置于首位。来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Wu 2025 条目。

### 核心问题
面对部分观测、通信受限与突发风险事件，多主体自动驾驶系统如何快速切换协作结构并完成异常恢复？

### 创新点
1. 将异常恢复视为 runtime collaboration topology reconfiguration。
2. 用风险状态机驱动通信频率与协调模式切换。
3. 把高优先级中心化协调只留给高风险窗口，以控制带宽。

### 方法设计
1. 定义四种风险状态：正常、可疑、紧急、恢复。
2. 在不同状态下切换消息频率和决策结构：分布式—增强通信—中心协调—恢复降级。
3. 用 teacher planner 生成理想协作拓扑，再蒸馏到轻量 student。
4. 记录每次拓扑切换与恢复效果。

### 实验方案
- 在仿真路口会车、并线、遮挡冲突三类场景测试。
- 对比：固定分布式、固定中心化、风险驱动切换。
- 评估高风险触发阈值与误报率对系统的影响。

### 数据/benchmark
`Waymo Open Motion Dataset` 与 Wu 2025 综述提到的 multi-agent ADS benchmarks。
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Wu 2025 条目。

### 评价指标
- 碰撞率 / 违规率
- 异常恢复时间
- 高风险消息及时率
- 协作重构成功率
- 通信带宽占用

### 风险点
- 长尾风险事件样本少；
- 仿真到真实迁移困难；
- 安全指标高度敏感，实验门槛高。

### 最小可行原型
先在双车+路侧单元的路口会车仿真中，只测试“检测到冲突风险后是否切换到中心协调模式”这一机制。

---

## Idea 10：从综述证据链到自动选题的 research gap miner

### 题目
综述到选题的自动化闭环：基于证据链的 research gap miner

### 背景动机
本项目本身已经完成 10 篇综述精读、横向比较与 idea 生成，说明“从综述到研究问题”的流程是高频研究工作；而现有文献仍主要停留在人工归纳阶段。来源：`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`。

### 核心问题
能否让 agent 自动从综述的 limitations、future directions、benchmark gaps 与评测批评中抽取研究空白，并生成带证据链、可执行性和去重机制的研究 idea？

### 创新点
1. 直接把综述笔记作为结构化输入，而不是从原始 PDF 端到端生造 idea。
2. 每个自动生成 idea 都附 evidence map，明确来源综述与证据段落。
3. 将 gap clustering、idea templating、novelty filter 串成 pipeline。

### 方法设计
1. 从结构化精读笔记中抽取四类句子：limitations、future directions、benchmark gaps、evaluation critiques。
2. 聚类形成 gap taxonomy。
3. 用模板生成候选 idea：缺什么能力、在哪类 benchmark 上验证、最小原型是什么。
4. 计算与已有 idea 的重合度，做去重与降权。
5. 输出 evidence map 与可行性评分。

### 实验方案
- 先只使用本项目的 10 篇综述笔记作为输入。
- 输出前 20 个 gap 和前 10 个自动生成 idea。
- 由人工快速打分：新颖性、可做性、证据完整性。
- 与本项目人工生成的 10 个 idea 做 overlap 对比。

### 数据/benchmark
直接输入本项目现有文档：
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`
下游验证可接 `GAIA`, `WorkflowBench`, `MultiAgentBench`, `RoleBench`, `MCP-Bench`。

### 评价指标
- gap 抽取准确率
- idea 去重率
- 人工新颖性/可做性评分
- evidence completeness
- 从综述到实验计划的时间节省

### 风险点
- future work 表述常过泛，难直接转成课题；
- novelty 评估不能只靠文本相似度；
- 容易生成“听起来合理但做不出来”的空洞 idea。

### 最小可行原型
写一个脚本，仅对本项目 10 篇结构化笔记执行 gap extraction + idea templating，输出前 5 个带 evidence map 的自动选题建议，再由人工快速复核。

---

## 去重与差异说明

这 10 个 idea 覆盖的是 6 条相对独立主线，而不是同一方向的重复改写：

1. communication-workflow 联合优化：Idea 1
2. 安全治理与开放工具生态：Idea 2、Idea 8
3. 长时共享记忆与社会一致性：Idea 3、Idea 6
4. 通信效率与高风险协作：Idea 4、Idea 9
5. 统一评测与因果归因：Idea 5、Idea 7
6. 综述到选题的自动化 pipeline：Idea 10

差异依据可回链到：
- communication 主线：Yan 2025、Chen 2026
- workflow/tool 主线：Xu 2026、Yue 2026
- memory/role 主线：Aratchige 2025、Wang 2026
- collaboration 主线：Tran 2025
- high-risk vertical 主线：Wu 2025
来源：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

## 推荐优先级

### 短期最适合启动
1. Idea 1：预算感知的通信—工作流联合优化器
2. Idea 2：多工具协作安全治理层
3. Idea 5：统一日志协议与六维评测

### 中期高价值方向
4. Idea 3：共享记忆分层与冲突消解
5. Idea 7：协作收益因果拆解实验框架
6. Idea 8：开放工具发现与可靠接入

### 高风险高收益方向
7. Idea 6：社会型多智能体系统
8. Idea 9：自动驾驶异常恢复协作
9. Idea 10：research gap miner
10. Idea 4：通信压缩与优先级调度

## 结论

本次重写已把原先的 10 个 detailed ideas 对齐到最终任务要求字段，并将每个 idea 显式绑定到项目内已落盘的共同空白与差异：
- 共同空白来自 `ten-survey-synthesis-report.md`
- 主趋势与分歧来自 `ten-survey-quick-overview.md`
- 逐篇专题差异来自 `ten-survey-structured-reading-notes.md`

因此，这 10 个 idea 既不是凭空脑补，也不是旧 5 个 idea 的简单扩写，而是对 canonical 10 篇综述共识与差异的结构化再表达。