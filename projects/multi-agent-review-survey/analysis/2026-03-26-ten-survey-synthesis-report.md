# 2026-03-26 canonical 10 篇 multi-agent / agentic 综述中文综合报告（修订版）

- Timestamp: 2026-03-26T00:40:55+08:00
- Session: 灯里-00-1774456784-9d98b8
- Scope: 基于已交叉复核并统一的 10 篇 canonical reading set，输出中文综合报告。
- Reading set: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- Structured notes: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- Research ideas: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`

## 0. 结论先行

这 10 篇综述共同显示，multi-agent 研究正在从“把多个 LLM 串起来”转向“把**协作结构、通信协议、记忆机制、工具编排、运行时工作流、角色建模与治理边界**一起设计”。

最清楚的趋势有四条：

1. **从总览走向专题深化**：Guo 2024、Chen 2025 提供全景；Yan 2025、Chen 2026 深挖通信；Xu 2026、Yue 2026 深挖 tool-use 与 workflow；Wang 2026 则进入 role-play/social agents。
2. **通信成为核心变量**：谁与谁通信、何时通信、传什么、为何通信，正从实现细节升级为研究主线。来源：`analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Yan 2025 与 Chen 2026 条目。
3. **工程系统视角增强**：memory、planning、tool orchestration、runtime graph optimization 等话题在 2026 年明显增多。来源：同上中 Aratchige 2025、Xu 2026、Yue 2026 条目。
4. **评测与治理仍然薄弱**：多数综述都指出 benchmark fragmented、成本/安全/扩展性度量不足。来源：同上中 Guo 2024、Tran 2025、Yan 2025、Xu 2026、Yue 2026 条目。

## 1. 本轮统一后的 10 篇综述

1. Guo et al. 2024 — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges*
2. Aratchige & Ilmini 2025 — *LLMs Working in Harmony*
3. Chen et al. 2025 — *A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application*
4. Tran et al. 2025 — *Multi-Agent Collaboration Mechanisms: A Survey of LLMs*
5. Wu et al. 2025 — *Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances*
6. Yan et al. 2025 — *Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems*
7. Xu et al. 2026 — *The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration*
8. Yue et al. 2026 — *From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents*
9. Chen et al. 2026 — *The Five Ws of Multi-Agent Communication*
10. Wang et al. 2026 — *Role-Playing Agents Driven by Large Language Models*

完整元数据、来源页、本地 PDF 路径与页数见：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`。

## 2. 横向比较

| 主题轴 | 代表综述 | 核心问题 |
|---|---|---|
| 总体框架 | Guo 2024, Chen 2025 | multi-agent 系统由哪些组件构成、用于哪些场景 |
| 技术底座 | Aratchige 2025 | architecture / memory / planning / frameworks 如何影响系统效果 |
| 协作机制 | Tran 2025 | cooperation / competition / coopetition、结构与协议如何组织 |
| 通信机制 | Yan 2025, Chen 2026 | who/whom/when/what/why to communicate |
| 工具与工作流 | Xu 2026, Yue 2026 | multi-tool orchestration 与 workflow graph 如何设计和优化 |
| 角色与社会性 | Wang 2026 | personality、memory、motivation 如何支撑 role-playing agents |
| 垂直应用 | Wu 2025 | 自动驾驶中多主体协作的实时性与安全性约束 |

### 2.1 共识

跨 10 篇综述反复出现的共识：

- **单 agent 上限明显**，复杂任务、开放环境、长期运行、社会交互都容易触顶。
- **多 agent 的收益来自分工与交互，不来自数量本身**。
- **通信设计是核心瓶颈**，不仅影响性能，也影响成本与安全。
- **agent-specific benchmark 缺口明显**，现有评测难覆盖长期轨迹、结构质量、消息质量与治理能力。

以上共识可分别在 `analysis/2026-03-26-ten-survey-structured-reading-notes.md` 的 Guo 2024、Tran 2025、Yan 2025、Xu 2026、Yue 2026 条目中找到直接支撑。

### 2.2 分歧

主要分歧集中在三点：

1. **研究主语不同**：有些综述把 multi-agent 看成“应用组织方式”，有些看成“通信系统”，有些看成“运行时工作流/工具编排器”。
2. **通信形式不同**：传统 MARL / emergent language 更看重高效协议，LLM-agent 综述更强调自然语言可解释性。来源：Chen 2026。
3. **通用性与场景化拉扯**：通用框架综述追求统一抽象，Wu 2025、Wang 2026 这类专题综述则表明真实落地必须拥抱领域约束。

## 3. 时间演化趋势

### 2024：建立总图谱

- Guo 2024 重点梳理 interface、profiling、communication、capabilities、applications。
- 这阶段的核心任务是回答“LLM-based multi-agent systems 到底是什么”。

### 2025：专题化深化

- Aratchige 2025 把焦点移向 architecture / memory / planning。
- Tran 2025 开始系统化讨论 collaboration mechanisms。
- Yan 2025 明确提出 communication-centric taxonomy。
- Wu 2025 与 Wang 2026 前身方向则表明专题场景正在扩张。

### 2026：系统工程化

- Xu 2026 关注 multi-tool orchestration、成本、安全与开放环境。
- Yue 2026 将 workflow 抽象为 agentic computation graphs，研究静态/动态结构优化。
- Chen 2026 把通信问题统一到 5W 框架。
- Wang 2026 反映 social / role-playing agents 已成为独立方向。

## 4. 主要研究空白

### 4.1 协作收益缺少因果拆解

目前很多工作报告 multi-agent 优于 single-agent，但常没有严格控制：

- 相同 token / 调用预算
- 相同工具条件
- 相同外部检索条件
- 仅改变拓扑/通信/角色数

因此尚难判断性能提升究竟来自“协作机制”还是“更多采样”。

### 4.2 缺少通信层指标

Yan 2025 与 Chen 2026 都提示，现有评测太依赖任务得分；更缺的是：

- 消息有效率
- 冗余率
- 冲突恢复时延
- 通信成本-性能曲线
- 安全协议鲁棒性

### 4.3 workflow / tool / communication 仍被分开研究

Xu 2026 讨论工具编排，Yue 2026 讨论 workflow graph，Yan 2025 / Chen 2026 讨论 communication，但三者在真实系统中强耦合。未来更有价值的是三者联合优化，而不是分别做局部 patch。

### 4.4 缺少长期、真实、可治理 benchmark

Wu 2025 的自动驾驶场景与 Wang 2026 的 role-play 场景都在提醒：真实世界要求长期一致性、风险控制、责任边界与异常恢复，而这些几乎不被标准 benchmark 系统覆盖。

## 5. 对本仓库 agent 集群的启发

结合本仓库“repo as memory + 多 agent 协作”实践，最直接可落地的启发有四点：

1. **把通信当作一等对象记录**：谁提交了什么结论、基于哪些文件、是否被他人复核。
2. **把共享记忆分层**：个人笔记、团队共识、经复核事实分层存放。
3. **按阶段切换拓扑**：检索期适合并行探索，撰写期适合主笔+复核，质检期适合交叉 review。
4. **把治理嵌入工作流**：高风险结论、未验证断言、文件不一致都应触发 review / 修正，而不是在最终汇报时才发现。

## 6. 与 research ideas 的关系

本综合报告支撑的后续 idea 已写入：

- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`

其中最直接由本轮空白推出的方向包括：

- 预算感知 communication-workflow 联合优化
- 多工具协作 agent 的安全治理
- 角色记忆驱动的社会型多智能体系统
- 真实世界通信压缩与优先级调度
- benchmark 统一协议

## 7. 本次修订说明

本文件已根据交叉 review 结果修正为与结构化笔记、research ideas、元数据清单一致的 10 篇 canonical reading set，避免继续出现“报告写的是一组论文、笔记读的是另一组论文”的质量问题。

交叉 review 记录见：`projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`。