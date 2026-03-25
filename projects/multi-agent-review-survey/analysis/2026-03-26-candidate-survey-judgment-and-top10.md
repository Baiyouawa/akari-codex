# 2026-03-26 候选论文逐篇核验：是否属于真正综述/survey，并按新近程度与相关性筛到 10 篇

- Timestamp: 2026-03-26T01:00:51+08:00
- Session: 理世-06-1774458003-4ca462
- Task: 对候选论文逐篇判断是否属于真正的综述/survey，并按新近程度与相关性筛到 10 篇
- Status: completed

## 1. 证据来源与判定规则

### 1.1 证据来源

本轮不重新发散检索，而是基于仓库内已落盘且可追溯的候选池做逐篇核验：

1. 候选池与摘要：`projects/multi-agent-review-survey/sources/2026-03-26-arxiv-multi-agent-survey-candidates.json`
2. 初筛候选文档（19 篇）：`projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
3. 当前本地 PDF 库存：`projects/multi-agent-review-survey/analysis/2026-03-26-literature-metadata-inventory.md`
4. 当前 canonical reading set：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`

### 1.2 判定规则

对每篇候选按两步处理：

**Step A：先判断是否属于“真正的综述/survey”**

满足以下任一强证据，即判为 `是`：

- 标题显式包含 `survey` / `review` / `SoK` / `taxonomy`
- 摘要显式出现 `this survey` / `we survey` / `we review` / `systematization`
- 摘要明确说明其工作是对已有研究进行结构化归纳、分类、比较、开放问题总结

若标题或摘要主要在报告一个新系统/benchmark/framework/case study，而不是系统综述既有文献，则判为 `否`。

**Step B：对判为综述的候选按“新近程度 + 相关性”排序**

- 新近程度优先：`2026 > 2025 > 2024`
- 同年份内按相关性排序：
  - `高`：直接面向 multi-agent systems / LLM-based MAS / agentic multi-agent communication/collaboration
  - `中`：agentic/LLM agents 的关键子问题综述，能直接支撑 multi-agent 研究（如 workflow、tool use、role-playing）
  - `低`：更偏专题外围、安全、memory、特定垂直领域，虽是综述但不适合作为本轮 top 10 主集合

## 2. 逐篇核验结果（19 篇）

| # | 候选 | 年份 | 是否真正综述 | 证据 | multi-agent 相关性 | 结论 |
|---|---|---:|---|---|---|---|
| 1 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | 2026 | 是 | 标题含 `A Survey`；摘要首句含 `This survey reviews recent methods`，见候选 JSON 与候选初筛文档 | 中 | 入选 top 10 |
| 2 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | 2026 | 是 | 摘要含 `We comprehensively review`，见候选 JSON | 中 | 入选 top 10 |
| 3 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | 2026 | 是 | 标题显式含 `A Survey`；摘要首句含 `This survey reviews multi-agent communication`，见候选 JSON | 高 | 入选 top 10 |
| 4 | Game-Theoretic Lens on LLM-based Multi-Agent Systems | 2026 | 是 | 摘要含 `we present a comprehensive survey`，见候选 JSON | 高 | 入选 top 10 |
| 5 | Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents | 2026 | 是 | 标题含 `Taxonomies`；摘要写明 `we investigate architectures and propose a unified taxonomy`，并覆盖 hierarchical multi agent systems，见候选 JSON | 高 | 入选 top 10 |
| 6 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | 2026 | 是 | 标题为 `Current Status, Challenges, and Future Trends`；摘要写明 `systematically reviews`，见候选 JSON | 中 | 入选 top 10 |
| 7 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi-Agent Systems | 2025 | 是 | 标题显式含 `A Survey`，见候选初筛文档 | 高 | 入选 top 10 |
| 8 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2024 | 是 | 标题显式含 `A Survey`，见候选初筛文档 | 高 | 入选 top 10 |
| 9 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | 是 | 标题显式含 `A Survey`，见候选初筛文档 | 高 | 入选 top 10 |
| 10 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | 是 | 标题显式含 `Survey`，见候选初筛文档 | 高 | 入选 top 10 |
| 11 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | 2025 | 是 | 标题显式含 `A Survey`，见候选初筛文档 | 中 | 备选 1 |
| 12 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | 是 | 标题显式含 `A Survey`，见候选初筛文档 | 高 | 备选 2 |
| 13 | SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy | 2026 | 是 | 标题含 `SoK`；摘要首句含 `In this systematization`，见候选 JSON | 低 | 剔除：更偏 agentic 安全综述 |
| 14 | Memory poisoning and secure multi-agent systems | 2026 | 是 | 摘要含 `we review the already existing security solutions`，见候选 JSON | 低 | 剔除：安全专题过窄 |
| 15 | Security Considerations for Multi-agent Systems | 2026 | 是 | 摘要含 `This study systematically characterizes` 与 cross-framework survey，见候选 JSON | 低 | 剔除：安全专题过窄 |
| 16 | Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers | 2026 | 是 | 摘要首句含 `This survey offers`，见候选 JSON | 低 | 剔除：memory 主体不是 multi-agent 主线 |
| 17 | The AI Hippocampus: How Far are We From Human Memory? | 2026 | 是 | 摘要含 `This survey presents`，见候选 JSON | 低 | 剔除：memory 大综述，multi-agent 仅为一部分 |
| 18 | Agentic AI in Remote Sensing: Foundations, Taxonomy, and Emerging Systems | 2026 | 是 | 摘要含 `This survey presents the first comprehensive review`，见候选 JSON | 低 | 剔除：垂直领域专题 |
| 19 | Federated Multi Agent Deep Learning and Neural Networks for Advanced Distributed Sensing in Wireless Networks | 2026 | 是 | 摘要首句含 `This survey synthesizes`，见候选 JSON | 低 | 剔除：传统无线网络 sensing 方向，偏离本项目主线 |

## 3. 为什么这些论文算“真正综述”，而不是普通方法论文

本轮 19 篇候选里，**19/19 都可判为综述型文献**，原因是每篇都具备至少一个强证据：

- 标题显式含 `survey` / `review` / `SoK` / `taxonomy`；或
- 摘要明确声明本工作在回顾、归纳、分类已有研究，而不是只报告一个新模型/新系统。

因此，本轮筛选的关键不是“有没有伪综述混入 19 篇”，而是：

1. 哪些综述最贴近 **multi-agent 主线**；
2. 哪些虽然是综述，但属于 **安全 / memory / 垂直行业** 等外围专题；
3. 在必须收敛到 10 篇时，如何兼顾 **新近程度** 与 **主题相关性**。

## 4. 最终 top 10（按“新近程度优先，相关性次之”排序）

| 排名 | 论文 | 年份 | 入选理由 |
|---|---|---:|---|
| 1 | The Five Ws of Multi-Agent Communication | 2026 | 2026 年且直接研究 multi-agent communication，本轮最贴近“multi-agent 主线中的通信核心问题” |
| 2 | Game-Theoretic Lens on LLM-based Multi-Agent Systems | 2026 | 2026 年且直接面向 LLM-based MAS，总结框架统一性强 |
| 3 | Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents | 2026 | 2026 年，覆盖从单 agent 到 hierarchical multi-agent systems 的统一 taxonomy |
| 4 | The Evolution of Tool Use in LLM Agents | 2026 | 2026 年，虽然是子问题综述，但与 multi-agent tool orchestration 直接相连 |
| 5 | From Static Templates to Dynamic Runtime Graphs | 2026 | 2026 年，workflow optimization 是 agent 集群工程化的关键支点 |
| 6 | Role-Playing Agents Driven by Large Language Models | 2026 | 2026 年，社会性/角色化 multi-agent 是快速升温子方向 |
| 7 | LLMs Working in Harmony | 2025 | 2025 年且直接讨论 LLM-based MAS 技术栈，相关性高 |
| 8 | Beyond Self-Talk | 2025 | 2025 年且 communication-centric，和 2026 Five Ws 形成自然递进 |
| 9 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | 2025 年且直接讨论 collaboration mechanisms，是主线核心综述 |
| 10 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2024 | 虽发表于 2024-12，但仍属最近一轮 general MAS survey，且比领域型综述更适合作为 top 10 通用主集合 |

## 5. 备选与剔除理由

### 5.1 高质量但未进入 top 10 的备选

1. **Wu et al. 2025 — Autonomous Driving Survey**
   - 未入选原因：是高质量 survey，但更偏自动驾驶垂直场景；在 top 10 名额固定时，通用型 multi-agent survey 优先级更高。
2. **Guo et al. 2024 — Progress and Challenges**
   - 未入选原因：是很强的基线总览，但时间上早于 2024-12/2025/2026 候选；若任务更强调“奠基性基线”，它应优先作为补充阅读。

### 5.2 被剔除的专题综述

- **安全方向**：Dehghantanha 2026、Torra 2026、Nguyen 2026
- **memory 方向**：Du 2026、Jia 2026
- **垂直领域方向**：Talemi 2026、Muller 2026

共同原因：这些论文本身是综述，但主题更像 **agentic AI 的专题分支**，而不是本项目当前要优先沉淀的通用 multi-agent survey 主线。

## 6. 与现有 canonical reading set 的关系

当前仓库已有 canonical reading set 见：
`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`

与本轮 top 10 对比：

- **重合 9 篇**：Aratchige 2025、Chen 2412/2024、Tran 2025、Yan 2025、Xu 2026、Yue 2026、Chen 2026、Wang 2026，加上 multi-agent general/core 相关集合中的多数主线论文
- **差异 1 篇**：
  - 现有 canonical reading set 保留了 **Wu 2025（自动驾驶综述）**
  - 本轮 top 10 改为保留 **Hao 2026（Game-Theoretic Lens）**

差异原因：本轮任务强调“按新近程度与相关性筛到 10 篇”，因此更倾向保留 **2026 年、且更通用的 LLM-based MAS 理论综述**，而不是 2025 年的垂直场景综述。

## 7. 结论

本轮已完成对候选论文的逐篇 survey 属性核验，并在 19 篇均为真实综述型文献的前提下，按“**2026 优先、通用 multi-agent 主线优先于专题外围、通用型优先于垂直领域型**”的规则收敛出最终 top 10。

推荐后续会话若要继续统一全项目 reading set，应优先处理一件事：

- 决定是否用 **Hao 2026** 替换现有 canonical reading set 中的 **Wu 2025**。

在未替换前，可把本文件视为“**面向最新性与主题相关性的 top 10 重排结果**”；而 `analysis/2026-03-26-ten-paper-metadata.md` 仍是当前已下载、已精读、已交叉复核过的稳定 reading set。
