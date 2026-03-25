# 2026-03-26 十篇 multi-agent 综述横向对比中文速览

- Timestamp: 2026-03-26T01:55:48+08:00
- Session: 智乃-02-1774461309-24c5b8
- Task: 对 10 篇综述做横向对比，整理共识、分歧、重复主题、空白问题、时间演化趋势，形成适合快速浏览的中文总览
- Canonical reading set: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- Structured notes: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- Synthesis report: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
- Cross-review evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`

> 说明：本文件不新增未经核验的论文事实，只把项目内已经 cross-review 对齐过的 canonical 10 篇综述，压缩成“适合快速浏览”的横向总览。

---

## 1. 一页看懂：这 10 篇综述到底在讲什么

如果把这 10 篇综述放在一起看，主线非常清楚：

- **2024** 先回答“LLM-based multi-agent systems 是什么”；
- **2025** 开始拆成更细的专题：协作、通信、应用场景、技术底座；
- **2026** 明显进入系统工程阶段：tool orchestration、workflow optimization、communication theory、role-playing/social agents。

换句话说，研究重心已经从“多个 agent 一起工作”转向：

1. 怎样设计**协作结构**；
2. 怎样设计**通信机制**；
3. 怎样把 **tool / workflow / memory / governance** 统一进一个运行时系统；
4. 怎样在真实约束下衡量收益，而不是只看最终任务分数。

---

## 2. 十篇综述的主题分工

| 组别 | 代表论文 | 主要回答的问题 |
|---|---|---|
| 通用总览 | Guo 2024；Chen 2025 | multi-agent 系统由哪些组件构成、应用到哪些任务 |
| 技术底座 | Aratchige 2025 | architecture、memory、planning、frameworks 哪些最关键 |
| 协作机制 | Tran 2025 | cooperation / competition / coordination 如何组织 |
| 通信机制 | Yan 2025；Chen 2026 | 谁和谁沟通、何时沟通、沟通什么、为什么沟通 |
| 工具与工作流 | Xu 2026；Yue 2026 | 多工具编排、运行时 graph、workflow 优化怎么做 |
| 垂直应用 | Wu 2025 | 自动驾驶里的多主体协作与安全/实时性约束 |
| 社会型 agents | Wang 2026 | 角色、人设、记忆、动机如何驱动长期社会互动 |

**可快速记忆的对应关系**：
- 想看“全景地图”→ Guo 2024、Chen 2025
- 想看“协作怎么组织”→ Tran 2025
- 想看“通信怎么建模”→ Yan 2025、Chen 2026
- 想看“系统怎么工程化”→ Aratchige 2025、Xu 2026、Yue 2026
- 想看“真实/特殊场景”→ Wu 2025、Wang 2026

---

## 3. 跨 10 篇的核心共识

### 共识 1：单 agent 很快遇到上限
几篇通用综述与专题综述都隐含同一个判断：复杂任务、长期轨迹、开放环境、社会交互，单 agent 容易在上下文、规划、可靠性和覆盖度上触顶。multi-agent 的价值不只是“更多调用”，而是**角色分工 + 并行探索 + 互补视角**。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Guo 2024、Chen 2025、Tran 2025 条目。

### 共识 2：收益来自结构，而不是人数
综述们普遍不把“agent 数量”当作核心变量，而把 **拓扑、角色关系、协调协议、消息内容** 当作关键变量。也就是说，多 agent 不等于多开几个实例，而是要重新设计交互结构。

- Provenance: Tran 2025、Yan 2025、Chen 2026 条目；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 2 节与第 4 节。

### 共识 3：通信已经变成主问题
Yan 2025 和 Chen 2026 最直接，但其他综述也在侧面支持：谁发消息、何时发、发什么、发给谁，会同时影响性能、成本、延迟、可解释性与安全。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Yan 2025、Chen 2026 条目。

### 共识 4：评测体系碎片化
从 Guo 2024 的通用 benchmark，到 Xu 2026 / Yue 2026 的 workflow、tool-use、长程执行 benchmark，再到 Wang 2026 的 role-play benchmarks，可以看到 benchmark 越来越多，但口径越来越碎。大家都承认：**缺少统一、可比较的 agent benchmark 协议**。

- Provenance: 同上 structured notes 各条 benchmark 列表；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 4 节。

### 共识 5：工程化与治理正在上升
2026 年的综述明显更关心资源预算、安全控制、运行时图结构、工业级治理，而不仅是“prompt 能不能 work”。

- Provenance: Xu 2026、Yue 2026、Wu 2025 条目；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 3-5 节。

---

## 4. 主要分歧：各家到底哪里看法不一样

### 分歧 1：研究主语不同
同样研究“multi-agent”，不同综述把研究主语定义得很不一样：

- Guo 2024、Chen 2025：把它看成**通用系统框架/应用体系**；
- Tran 2025：把它看成**协作结构问题**；
- Yan 2025、Chen 2026：把它看成**通信系统问题**；
- Xu 2026、Yue 2026：把它看成**运行时工作流与工具编排问题**；
- Wang 2026：把它看成**社会互动与角色建模问题**。

这不是谁对谁错，而是说明 multi-agent 已经从一个单点主题分裂成多个子学科。

### 分歧 2：自然语言通信 vs 高效协议通信
通信类综述特别明显：

- 一类工作强调自然语言的开放性、可解释性和泛化能力；
- 另一类脉络（尤其 Chen 2026 回溯 MARL / emergent language 时）更关心高效协议、时机与目标导向通信。

这意味着未来可能要在“高效压缩协议”和“自然语言可解释通信”之间做折中。

### 分歧 3：通用抽象 vs 领域约束
- 通用综述倾向于统一 taxonomy；
- Wu 2025、Wang 2026 这种专题综述则表明，一旦进入自动驾驶或社会型 agent，领域约束会压过抽象统一。

也就是说，**通用框架很重要，但落地时必须尊重场景特性**。

---

## 5. 重复主题：10 篇都在反复谈什么

以下主题在不同综述中高频重复出现，可视为当前 multi-agent 领域的“公认主战场”。

### 5.1 Memory / Planning / Role Assignment
即使不是每篇都把它们列为标题，几乎都在讨论：
- agent 如何记住过去；
- agent 如何规划长任务；
- agent 如何分工与扮演角色。

这说明多智能体问题很大程度上是**记忆、规划与角色分配的组合问题**。

### 5.2 Communication / Coordination
Tran 2025、Yan 2025、Chen 2026 是显式主线；其他综述则把它作为系统关键模块。重复出现说明：通信与协调已经不是局部技巧，而是结构核心。

### 5.3 Benchmark / Evaluation
几乎每篇都要讨论 benchmark，但讨论方式分散：有的偏任务性能，有的偏社会一致性，有的偏工具执行与长程流程。重复出现本身就说明该问题尚未被统一解决。

### 5.4 Safety / Scalability / Real-world constraints
从 Guo 2024 的 risks，到 Xu 2026 的 governance，再到 Wu 2025 的自动驾驶安全、Yue 2026 的 graph-level cost/robustness，都在提醒：工程化压力正在替代“demo-level 成功率”成为新标准。

---

## 6. 目前最清楚的空白问题

### 空白 1：协作增益缺少因果拆解
现在常见结论是“multi-agent 比 single-agent 好”，但未严格控制：
- token 预算；
- 工具权限；
- 检索条件；
- agent 数量；
- 拓扑结构。

所以还很难回答：提升究竟来自协作机制，还是来自“多采样 + 多工具 + 更多调用”。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 4 节。

### 空白 2：缺少通信层指标
当前评测更看任务正确率，较少系统衡量：
- 消息有效率；
- 冗余率；
- 冲突恢复时延；
- 通信成本-性能曲线；
- 被攻击/误导时的鲁棒性。

- Provenance: Yan 2025、Chen 2026 条目；synthesis report 第 4.2 节。

### 空白 3：workflow / communication / tool-use 仍然割裂
Xu 2026 讲工具，Yue 2026 讲 workflow，Yan 2025 / Chen 2026 讲通信；但在真实系统里，这三者是耦合的。缺少一个统一框架同时优化：
- 谁通信；
- 何时调用工具；
- workflow 如何动态调整。

- Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md` 第 4.3 节。

### 空白 4：长期、真实、可治理 benchmark 不足
真实系统不仅要完成任务，还要长期一致、安全、可回滚、可审计、可归因。这一点在自动驾驶、开放工具环境、社会型角色系统中都非常突出，但 benchmark 还没有跟上。

- Provenance: Wu 2025、Xu 2026、Yue 2026、Wang 2026 条目。

### 空白 5：社会型多智能体研究还很早期
Wang 2026 说明 role-playing/social agents 已成方向，但对 personality fidelity、memory consistency、relation stability 的评测与建模还很初级。

- Provenance: Wang 2026 条目。

---

## 7. 时间演化趋势

### 2024：先建立“总地图”
- 代表：Guo 2024
- 关键词：组件、应用、挑战、资源、benchmark
- 主要目标：定义问题空间

### 2025：从总览走向专题化
- Aratchige 2025：技术底座
- Chen 2025：应用前沿
- Tran 2025：协作机制
- Yan 2025：通信中心视角
- Wu 2025：自动驾驶垂直应用

这一年最明显的变化是：研究不再满足于“系统长什么样”，而开始追问“到底哪一层机制在发挥作用”。

### 2026：工程系统化与社会化并进
- Xu 2026：multi-tool orchestration
- Yue 2026：runtime workflow graph
- Chen 2026：5W communication
- Wang 2026：role-playing/social agents

这一阶段的多智能体研究已经明显出现两条支线：
1. **工程系统化**：工具、工作流、预算、安全、治理；
2. **社会化/交互化**：角色、动机、长期互动、叙事一致性。

---

## 8. 给快速浏览者的最终结论

如果只保留 8 个 takeaways，可以直接记下面这些：

1. **multi-agent 研究已经从“多角色协作”升级为“系统工程设计”问题。**
2. **人数不是关键，交互结构才是关键。**
3. **通信是当前最核心的统一变量之一。**
4. **workflow、tool-use、communication 未来必须联合优化。**
5. **benchmark 很多，但仍然碎片化，缺少统一协议。**
6. **真实应用正在把安全、时延、治理推到与性能同等重要的位置。**
7. **专题化正在加速：communication、workflow、tool-use、role-play 都已成为独立方向。**
8. **下一阶段最值钱的问题，不是再做一个“多 agent demo”，而是解释 multi-agent 为什么在什么条件下真正更优。**

---

## 9. 适合继续追的三个方向

### 方向 A：预算感知的通信-工作流联合优化
为什么值得做：正好落在 communication / workflow / tool-use 三个割裂主题的交叉处。
- Provenance: Xu 2026、Yue 2026、Yan 2025、Chen 2026 条目。

### 方向 B：统一的 agent benchmark 协议
为什么值得做：10 篇综述都隐含 benchmark fragmentation 问题，但没人真正统一。
- Provenance: structured notes 中多篇 benchmark 列表；synthesis report 第 4 节。

### 方向 C：带治理约束的真实多智能体系统
为什么值得做：Wu 2025、Xu 2026、Yue 2026 都显示真实部署需要安全、可审计、可回滚。
- Provenance: Wu 2025、Xu 2026、Yue 2026 条目。

---

## 10. 证据链

- 10 篇 canonical 论文清单与 PDF 路径：
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- 逐篇结构化精读：
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- 综合分析：
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
- 交叉 review 与 canonical set 对齐证据：
  `projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`

## 11. 数量核验

- canonical reading set 论文数：10 篇。
  - Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md` 表格共 10 行。
- 年份分布：2024 年 1 篇，2025 年 5 篇，2026 年 4 篇。
  - Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md` 中 `year_counts = Counter({'2025': 5, '2026': 4, '2024': 1})`。
- 总页数：340 页。
  - Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-basic-info-for-10-papers.md` 中 inline arithmetic `15 + 12 + 13 + 35 + 18 + 16 + 42 + 31 + 143 + 15 = 340`。
