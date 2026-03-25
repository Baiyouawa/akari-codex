# 10 篇 multi-agent 综述中文速读手册

- Timestamp: 2026-03-26T01:59:33+08:00
- Session: 枫-05-1774461549-e6b16c
- Purpose: 帮助人快速了解当前 canonical reading set 的 10 篇 multi-agent / agentic 综述
- Canonical reading set: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- Structured reading notes: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- Synthesis report: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
- Quick overview: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`
- Cross-review evidence: `projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`

> 说明：本文不新增未经核验的论文事实，只把项目内已经 cross-review 对齐过的 10 篇综述，整理成更适合快速浏览的中文 Markdown。年份分布、页数、PDF 路径、题目与作者均以 `analysis/2026-03-26-ten-paper-metadata.md` 与 `analysis/2026-03-26-basic-info-for-10-papers.md` 为准；逐篇判断与 benchmark/主题摘要以 `analysis/2026-03-26-ten-survey-structured-reading-notes.md` 为准。

---

## 0. 论文清单与 PDF 对应关系

| # | 简题 | 年份 | 主题 | 本地 PDF 路径 |
|---|---|---:|---|---|
| 1 | Guo 2024 | 2024 | 通用总览 | `projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` |
| 2 | Aratchige & Ilmini 2025 | 2025 | 技术底座 | `projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` |
| 3 | Chen et al. 2024 | 2024 | 应用前沿 | `projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` |
| 4 | Tran et al. 2025 | 2025 | 协作机制 | `projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` |
| 5 | Wu et al. 2025 | 2025 | 自动驾驶垂直场景 | `projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` |
| 6 | Yan et al. 2025 | 2025 | 通信中心视角 | `projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` |
| 7 | Xu et al. 2026 | 2026 | 工具编排 | `projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf` |
| 8 | Yue et al. 2026 | 2026 | workflow 优化 | `projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` |
| 9 | Chen et al. 2026 | 2026 | 5W 通信理论 | `projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` |
| 10 | Wang et al. 2026 | 2026 | role-playing / social agents | `projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf` |

---

## 1. 执行摘要

### 一句话结论
这 10 篇综述共同说明：multi-agent 研究已经从“让多个 LLM 一起回答问题”，转向“如何系统设计协作结构、通信协议、记忆机制、工具编排、运行时 workflow 与治理边界”。

### 最值得记住的 5 个判断
1. **总览型综述正在让位于专题化综述。** 2024 年以全景地图为主，2025-2026 年则拆出 communication、collaboration、tool-use、workflow、role-play 等细分方向。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`
2. **通信已变成核心研究变量。** “谁对谁说、什么时候说、说什么、为什么说”不再是 prompt 细节，而是独立设计空间。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Yan 2025、Chen 2026 条目
3. **工程系统视角明显增强。** 2026 年综述显著更关注 multi-tool orchestration、runtime graph、预算、安全与治理。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Xu 2026、Yue 2026 条目
4. **benchmark 很多，但仍然碎。** communication、workflow、tool-use、role-play 各有各的 benchmark，横向可比性不足。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
5. **最值钱的下一步不是再做一个 demo，而是解释 multi-agent 为什么在什么条件下更优。**  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`

### 数量核验
- canonical reading set：10 篇。  
  Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- 年份分布：2024 年 2 篇，2025 年 4 篇，2026 年 4 篇。  
  Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-basic-info-for-10-papers.md` 中逐行年份统计：Guo 2024、Chen 2024、Aratchige 2025、Tran 2025、Wu 2025、Yan 2025、Xu 2026、Yue 2026、Chen 2026、Wang 2026。
- 总页数：340 页。  
  Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-basic-info-for-10-papers.md` 中 inline arithmetic `15 + 12 + 13 + 35 + 18 + 16 + 42 + 31 + 143 + 15 = 340`

---

## 2. 十篇逐篇精读卡片

> 卡片字段统一来自 `analysis/2026-03-26-ten-survey-structured-reading-notes.md`，题目/年份/PDF 路径来自 `analysis/2026-03-26-ten-paper-metadata.md`。

### 卡片 1：Guo et al. 2024
- **定位**：最适合作为入门基线的通用总览。
- **核心问题**：LLM-based multi-agent systems 到底由哪些组件构成、用于哪些任务、面临哪些挑战？
- **怎么分**：interface、profiling、management、communication、training、orchestration/efficiency；应用上覆盖 problem solving、world simulation、dialogue generation。
- **你会得到什么**：一张“多智能体系统总地图”，方便后续专题化阅读定位。
- **局限**：时间较早，对 2025-2026 年 workflow、tool orchestration、communication 专题的深度不足。
- **适合谁先读**：第一次建立整个 LLM-MAS 认知框架的人。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 卡片 2：Aratchige & Ilmini 2025
- **定位**：技术底座导向综述。
- **核心问题**：构建有效 LLM-based MAS 时，architecture、memory、planning、frameworks 哪些最关键？
- **怎么分**：Architecture / Memory / Planning / Technologies & Frameworks 四大块。
- **你会得到什么**：从“怎么搭系统”而不是“系统能做什么”来理解 multi-agent。
- **局限**：应用覆盖面不如大型总览；更偏工程搭建视角。
- **适合谁先读**：想自己实现或改造 agent 系统的人。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 卡片 3：Chen et al. 2024
- **定位**：应用前沿导向综述。
- **核心问题**：LLM-MAS 目前已经扩展到哪些复杂任务、仿真场景与评测前沿？
- **怎么分**：复杂任务求解、特定场景仿真、生成式 agent 评估，并补充 core components 与 interactions。
- **你会得到什么**：从应用需求反推系统能力边界。
- **局限**：对 workflow / communication / tool-use 的细拆不如后续专题综述。
- **适合谁先读**：优先关心落地场景与应用空间的人。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 卡片 4：Tran et al. 2025
- **定位**：collaboration taxonomy 代表作。
- **核心问题**：多个 LLM agent 协作时，合作、竞争、竞合与结构拓扑该如何组织？
- **怎么分**：actors、relation types、structures、strategies、coordination protocols。
- **你会得到什么**：理解“多 agent 的收益来自结构，而不是人数”的最清晰框架之一。
- **局限**：对 tool-use、workflow、memory 讨论较少，需要与工程类综述配合。
- **适合谁先读**：研究集体智能、协作协议和角色分工的人。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 卡片 5：Wu et al. 2025
- **定位**：自动驾驶垂直应用综述。
- **核心问题**：在高风险、强实时约束下，multi-agent + LLM 如何支持车-车、车-路、车-助手、agent-人协作？
- **怎么分**：按交互对象和任务类型划分，包括协同感知、协同决策、云边部署与协同辅助工具。
- **你会得到什么**：看到 multi-agent 如何从“研究系统”进入“真实约束系统”。
- **局限**：场景专用性强，不能直接代表通用 MAS 全貌。
- **适合谁先读**：关心高风险场景、安全与实时性的研究者。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 卡片 6：Yan et al. 2025
- **定位**：communication-centric 综述。
- **核心问题**：communication 为什么是 LLM-MAS 的中心变量，而不是附属实现细节？
- **怎么分**：system-level communication 与 system-internal communication 两层；再细分 architecture、goals、protocols、strategy、paradigm、object、content。
- **你会得到什么**：把通信从“提示词设计”升级为“系统设计”的视角。
- **局限**：聚焦通信，因此 workflow、tool-use、memory 讨论相对弱。
- **适合谁先读**：打算研究消息协议、通信成本、安全与可解释性的人。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 卡片 7：Xu et al. 2026
- **定位**：tool-use / multi-tool orchestration 综述。
- **核心问题**：agent 的工具调用如何从单工具调用，演化到长程、多工具、受约束的编排问题？
- **怎么分**：planning & execution、trajectory construction、safety & control、resource efficiency、open-environment completeness、benchmark & evaluation。
- **你会得到什么**：理解为什么真实 agent 系统的难点常常是“multi-tool”而不只是“multi-agent”。
- **局限**：不是纯 communication / collaboration survey，对社会互动覆盖有限。
- **适合谁先读**：构建工业级 agent runtime 或工具链系统的人。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 卡片 8：Yue et al. 2026
- **定位**：workflow optimization 综述。
- **核心问题**：workflow 结构在何时确定、如何优化、由什么 evaluation signal 驱动？
- **怎么分**：静态 vs 动态；优化 workflow 哪一部分；由哪些信号指导优化。
- **你会得到什么**：从 template 转向 runtime graph / ACG 的系统抽象。
- **局限**：对社会性与通信协议细节覆盖不深。
- **适合谁先读**：想研究 agent graph、planner、verifier、runtime optimization 的人。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 卡片 9：Chen et al. 2026
- **定位**：5W 通信理论综述。
- **核心问题**：如何用统一框架联通 MARL、emergent language 与 LLM-based MAS 的通信研究？
- **怎么分**：Who / Whom / When / What / Why。
- **你会得到什么**：一个足够通用、可直接拿来拆解问题的通信模板。
- **局限**：聚焦通信，对 memory/tool/workflow 全景不覆盖。
- **适合谁先读**：要做“通信理论化”和跨范式比较的人。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 卡片 10：Wang et al. 2026
- **定位**：role-playing / social agents 综述。
- **核心问题**：人格、记忆、动机如何驱动 role-playing agents 的长期互动与社会行为？
- **怎么分**：研究范式演化、角色建模核心技术、数据构建、评测方法与未来趋势。
- **你会得到什么**：看到 multi-agent 不只做任务协作，还能构建社会互动与叙事系统。
- **局限**：对通用协作、tool-use、workflow 优化覆盖较少。
- **适合谁先读**：做 social simulation、角色智能体、长期记忆与叙事系统的人。
- **Provenance**：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

---

## 3. 横向对比表

| 论文 | 最强标签 | 主要贡献 | 最适合回答的问题 | 主要局限 |
|---|---|---|---|---|
| Guo 2024 | 通用总览 | 给出组件-应用-挑战总图谱 | multi-agent 全景是什么 | 对 2026 新主题覆盖不足 |
| Aratchige 2025 | 技术底座 | 把 architecture / memory / planning 提到核心位置 | 怎样搭一个有效 MAS | 应用面较窄 |
| Chen 2024 | 应用前沿 | 从复杂任务/仿真/评测看系统扩张 | 这些系统能拿来做什么 | 机制拆分不够细 |
| Tran 2025 | 协作机制 | cooperation / competition / structure taxonomy | 多 agent 怎样组织协作关系 | 工具与 workflow 讨论较弱 |
| Wu 2025 | 垂直场景 | 展示高风险真实约束下的多主体协作 | 自动驾驶等真实系统怎么落地 | 泛化到通用场景有限 |
| Yan 2025 | 通信中心视角 | communication taxonomy | communication 为什么是核心变量 | 其他系统因素覆盖较少 |
| Xu 2026 | 工具编排 | 从单工具到多工具编排的演化 | 工业级 agent 怎样管工具链 | 社会/角色互动覆盖少 |
| Yue 2026 | workflow 优化 | 提出 runtime graph / ACG 视角 | workflow 何时该动态优化 | 通信细节不是重点 |
| Chen 2026 | 5W 通信理论 | 用 5W 统一通信研究 | 如何系统拆解多智能体通信 | 非通信主题覆盖有限 |
| Wang 2026 | social agents | 角色/人格/记忆建模体系化 | role-play/social agent 如何建模 | 不主讲通用 MAS 工程 |

---

## 4. 关键趋势

### 趋势 1：从“总览”走向“专题化”
- 2024 年重点是建立问题空间；
- 2025 年开始把 collaboration、communication、应用前沿、技术底座拆开讲；
- 2026 年进一步出现 tool orchestration、workflow graph、5W communication、role-playing agents 等高密度子方向。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`

### 趋势 2：通信成为统一变量
多篇综述都隐含同一判断：通信会同时影响性能、成本、延迟、攻击面和可解释性，因此未来通信设计很难再只当作 prompt trick。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`

### 趋势 3：multi-agent 与 multi-tool / workflow 越来越耦合
2026 年的工程型综述表明，实际系统里 workflow、tool-use、communication 是联动的：谁沟通、何时调用工具、如何改写 graph，往往一起决定系统收益。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`

### 趋势 4：真实部署约束正在压过单纯分数
安全、时延、预算、可治理性、运行时可控性正在成为和 task score 同等重要的指标。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`

### 趋势 5：社会型 agent 成为新分支
Wang 2026 表明 multi-agent 的边界正在从“任务系统”扩展到“社会系统”，人格、记忆、关系稳定性成为新的核心维度。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Wang 2026 条目

---

## 5. 局限与机会

### 5.1 当前文献的共同局限
1. **协作增益缺少因果拆解。** 很多工作只证明 multi-agent 优于 single-agent，但没有严格控制 token 预算、工具权限、拓扑结构与外部检索条件。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
2. **通信层指标不足。** 现有评测更偏任务分数，较少衡量消息有效率、冗余率、恢复时延与成本-性能曲线。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`
3. **workflow / tool / communication 仍被割裂研究。** 真系统中它们强耦合，但文献常分开综述、分开优化。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
4. **长期、真实、可治理 benchmark 仍弱。** 对开放环境、长轨迹、异常恢复、责任归因的覆盖不足。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
5. **社会型多智能体评测还很早期。** 人格一致性、关系稳定性、长期记忆可靠性仍缺标准化协议。  
   Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md` 中 Wang 2026 条目

### 5.2 最值得追的机会点
1. **预算感知的 communication-workflow 联合优化**：同时回应 communication / workflow / cost 三个断裂点。  
2. **统一的 agent benchmark protocol**：解决 benchmark fragmentation。  
3. **带治理约束的 multi-tool 多智能体系统**：面向真实工业部署。  
4. **角色记忆驱动的 social multi-agent system**：连接 role-play 与 world simulation。  
5. **高风险场景下的通信压缩与优先级调度**：把自动驾驶类垂直系统做深。  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`

---

## 6. 给快速浏览者的阅读顺序建议

### 如果你只有 30 分钟
1. 先读 Guo 2024，建立总地图；
2. 再读 Yan 2025 或 Chen 2026，理解通信主线；
3. 最后读 Xu 2026 或 Yue 2026，看工程系统如何升级。

### 如果你想做系统实现
优先顺序：Aratchige 2025 → Xu 2026 → Yue 2026 → Yan 2025。

### 如果你想做理论与结构研究
优先顺序：Tran 2025 → Yan 2025 → Chen 2026。

### 如果你想做场景与应用
优先顺序：Chen 2024 → Wu 2025 → Wang 2026。

Provenance: 阅读顺序综合自 `projects/multi-agent-review-survey/analysis/2026-03-26-basic-info-for-10-papers.md` 与各篇 structured notes 的主题定位。

---

## 7. 最终 takeaway

如果把这 10 篇综述压缩成 6 句话，可以记住：

1. **multi-agent 已进入系统工程阶段。**
2. **人数不是关键，交互结构才是关键。**
3. **通信是最核心的统一变量之一。**
4. **workflow、tool-use、memory、communication 需要联合优化。**
5. **benchmark 体系仍然碎片化，是当前最大方法学瓶颈之一。**
6. **社会型 agents 可能是下一波高增长方向。**

---

## 8. 证据链

- canonical 10 篇题目、作者、年份、来源页、PDF 路径、页数：  
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- 10 篇逐篇结构化精读：  
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- 中文综合报告：  
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
- 横向速览：  
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-quick-overview.md`
- 交叉 review 记录：  
  `projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`
- research ideas：  
  `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`
