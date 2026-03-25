# 2026-03-26 基于十篇 multi-agent 综述的研究 ideas

- Timestamp: 2026-03-26T00:16:17+08:00
- Session: 结衣-03-1774454544-65f537
- Upstream notes: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

## Idea 1：预算感知的通信-工作流联合优化器

### 问题动机
Yan 2025 与 Chen 2026 强调 communication 设计，Yue 2026 强调 workflow graph 优化，但这两条线还没有真正统一：现实系统里，通信频率和工作流结构共同决定成本、延迟和成功率。

### 核心假设
如果把“谁在何时对谁说什么”看成 workflow graph 上的边编辑问题，则可以学习出**预算感知的动态 communication/workflow 联合策略**，在成本受限下优于固定多 agent 模板。

### 方法设计
- 用 ACG（Yue 2026）表示 agent workflow。
- 将 communication event 建模为图边的添加、删除、重加权。
- 用 verifier / critic 信号作为结构更新奖励。
- 目标函数同时优化任务质量、token 成本、响应时延、结构稳定性。

### 可用数据/benchmark
- `WorkflowBench`, `GAIA`, `MultiAgentBench`, `SOP-Bench`。

### 评测方案
- 成功率 / pass@k
- token 与 wall-clock 成本
- 平均通信轮数
- 图结构编辑次数
- 失败案例类型分布

---

## Idea 2：开放环境中的多工具协作 agent 安全治理

### 问题动机
Xu 2026 明确指出 multi-tool orchestration 存在长程安全风险；通信类综述又提示协议与内容可能成为攻击面。

### 核心假设
为 multi-agent + multi-tool 系统引入**层级权限、轨迹审计与高风险动作二次验证**，能显著降低开放环境中的越权与工具滥用。

### 方法设计
- 为 agent、tool、memory 三层都定义 capability schema。
- 在工作流图上增加 governance 节点，负责高风险工具调用审批。
- 用 trajectory verifier 检查 tool call sequence 是否越权或偏离任务。
- 结合 prompt-injection / memory poisoning 检测器做在线拦截。

### 可用数据/benchmark
- `MCP-Bench`, `LiveMCPBench`, `Terminal-Bench`, `RepoBench`, `AndroidArena`。

### 评测方案
- 任务成功率
- 恶意样本拦截率
- 误杀率
- 审批额外时延
- 风险事件平均损失

---

## Idea 3：角色记忆驱动的社会型多智能体叙事系统

### 问题动机
Wang 2026 指出 role-playing agents 正从模板生成转向人格/记忆/动机建模；Guo 2024、Chen 2025 则显示 world simulation 是多智能体重要应用。

### 核心假设
如果把人格、长期记忆、社会关系图联合建模，则 role-playing agents 在长期叙事一致性、多主体互动质量与社会仿真可信度上会显著提高。

### 方法设计
- 角色层：人格向量 + 价值偏好 + 社会关系 embedding。
- 记忆层：事件记忆 / 关系记忆 / 价值记忆分槽存储。
- 决策层：动机-情境-关系三因素驱动行动选择。
- 多 agent 互动时引入 narrative consistency critic。

### 可用数据/benchmark
- `RoleBench`, `RoleEval`, `RoleEval-Chinese`, `CharacterEval`。

### 评测方案
- 人格一致性
- 长期叙事连贯性
- 社会关系稳定性
- 交互幻觉率
- 人类偏好评分

---

## Idea 4：面向自动驾驶的多主体通信压缩与优先级调度

### 问题动机
Wu 2025 说明自动驾驶中的多车/车路/车人协作对通信依赖很强，但高实时场景下通信成本与延迟极敏感；Yan 2025/Chen 2026 提供了通信设计框架。

### 核心假设
把 communication content 做结构化压缩，并学习通信优先级调度，可在几乎不损失安全性的情况下显著降低多车协作带宽与延迟。

### 方法设计
- 先验地将 communication object 分为状态、意图、风险、协作请求四类。
- 对不同对象采用不同压缩模板与置信度门控。
- 在路口会车、并线等高交互场景中动态提升高风险消息优先级。
- 用 teacher-student 方式，把完整对话蒸馏为短结构化消息。

### 可用数据/benchmark
- `Waymo Open Motion Dataset` 以及文中提到的 multi-agent ADS benchmark。

### 评测方案
- 碰撞率 / 违规率
- 带宽消耗
- 通信延迟
- 协作决策成功率
- 压缩后性能下降幅度

---

## Idea 5：面向综述与系统设计的 agent benchmark 统一协议

### 问题动机
多篇综述都反复指出 benchmark fragmentation：通信看一套、workflow 看一套、tool-use 看一套、role-play 又看一套，导致横向比较困难。

### 核心假设
若构建一个统一 benchmark protocol，把任务效果、结构质量、通信质量、成本、安全、长期记忆维度共同纳入，则能显著提升 multi-agent 研究的可比性和复现性。

### 方法设计
- 设计统一评测 schema：task / communication / workflow / safety / cost / memory 六维指标。
- 为不同场景定义 adapter：tool-use、role-play、autonomous driving、general problem solving。
- 产出标准化日志格式，要求保留 trace、graph、message、tool calls。
- 建立 review checklist，防止只报 task score。

### 可用数据/benchmark
- `AgentBench`, `MultiAgentBench`, `GAIA`, `WorkflowBench`, `RoleBench`, `MCP-Bench`。

### 评测方案
- 跨 benchmark 可比较性
- 报告完整性提升幅度
- 复现实验成功率
- 不同系统在六维指标上的 Pareto 前沿质量

## 推荐优先级

### 短期最适合启动
1. Idea 1：预算感知的通信-工作流联合优化器
2. Idea 5：agent benchmark 统一协议
3. Idea 2：开放环境中的多工具协作 agent 安全治理

### 中期方向
4. Idea 3：角色记忆驱动的社会型多智能体叙事系统

### 高风险高收益
5. Idea 4：面向自动驾驶的多主体通信压缩与优先级调度
