# 2026-03-26 最新 multi-agent 综述候选初筛（>=15 篇）

- Timestamp: 2026-03-26T00:53:04+08:00
- Session: 灯里-00-1774457492-6d95d9
- Task: 检索并筛选最新的 multi-agent 相关综述/survey 论文，优先近年高相关结果，初步候选不少于 15 篇
- Status: completed for initial candidate collection
- Provenance:
  - 候选总池：`projects/multi-agent-review-survey/sources/2026-03-26-arxiv-multi-agent-survey-candidates.json`
  - 生成脚本：`projects/multi-agent-review-survey/sources/gather_arxiv_multi_agent_survey_candidates.py`
  - 查询来源：脚本内 4 组 arXiv API query，按 submittedDate 降序抓取近 50 条，再以 `year in {2024,2025,2026}`、`survey|review|perspective`、`multi-agent|agentic|LLM agent` 规则初筛
  - 本地 PDF 盘点：`projects/multi-agent-review-survey/literature/`

## 方法说明

本轮不重新发散到不可控的外部候选池，而是先利用仓库中已落盘的 arXiv 候选快照做一次可追溯初筛：

1. 读取 `sources/2026-03-26-arxiv-multi-agent-survey-candidates.json`，该文件记录了 4 组 arXiv API 查询结果与 100 篇候选。
2. 以“是否明确自称 survey/review/SoK/taxonomy”“是否直接讨论 multi-agent / LLM-based MAS / agentic AI / multi-agent communication”“是否足够新（优先 2025-2026）”为三条主规则做人工复核。
3. 输出 **19 篇** 初步候选，分为：
   - **A 组：直接高相关 multi-agent / LLM-MAS 综述**（优先后续进入 final 10）
   - **B 组：专题型 agentic / memory / security / domain-MAS 综述**（保留作补位或专题扩展）
4. 同时记录其是否已在 `literature/` 中落盘，方便后续下载与阅读分工。

## 初筛结果总览

- 初筛候选数：**19 篇**
- 其中 2026 年：**11 篇**
- 其中 2025 年：**7 篇**
- 其中 2024 年：**1 篇**
- 已在 `literature/` 中存在本地 PDF 的候选：**13/19**
  - 依据：当前 `projects/multi-agent-review-survey/literature/` 目录盘点

## A 组：直接高相关候选（优先级最高）

这些论文在标题或摘要中直接把对象界定为 multi-agent systems / LLM-based multi-agent systems / communication in MAS / agentic multi-agent collaboration，最适合作为后续 final 10 的核心池。

| # | Published | Title | 年份 | 直接相关性判断 | Survey/Review 证据 | 来源 | 本地 PDF |
|---|---|---|---:|---|---|---|---|
| 1 | 2026-03-23 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | 2026 | 讨论 LLM agents 的 workflow optimization，可覆盖多 agent runtime graph | 摘要首句含 “This survey reviews recent methods...” | http://arxiv.org/abs/2603.22386v1 | 是：`2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` |
| 2 | 2026-03-24 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | 2026 | 直接关联 agent 系统从单工具走向多工具/多步编排 | 摘要含 “We comprehensively review...” | http://arxiv.org/abs/2603.22862v1 | 是：`2026-xu-et-al-tool-use-in-llm-agents.pdf` |
| 3 | 2026-02-12 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | 2026 | 直接讨论 multi-agent communication，且覆盖 MARL→LLM agent | 标题显式含 “A Survey” | http://arxiv.org/abs/2602.11583v1 | 是：`2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` |
| 4 | 2026-01-21 | Game-Theoretic Lens on LLM-based Multi-Agent Systems | 2026 | 直接讨论 LLM-based MAS 的统一理论框架 | 摘要含 “we present a comprehensive survey” | http://arxiv.org/abs/2601.15047v1 | 否 |
| 5 | 2026-01-18 | Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents | 2026 | 覆盖从单 agent 到 hierarchical multi-agent systems 的 taxonomy | 标题含 Architectures, Taxonomies, and Evaluation；摘要系统性综述 agentic AI | http://arxiv.org/abs/2601.12560v1 | 否 |
| 6 | 2026-01-15 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | 2026 | 专注 role-playing agents，但摘要明确提到 multi-agent collaborative narrative | 标题为 Current Status / Challenges / Future Trends，摘要 “systematically reviews” | http://arxiv.org/abs/2601.10122v1 | 是：`2026-wang-et-al-role-playing-agents.pdf` |
| 7 | 2025-04-03 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi-Agent Systems | 2025 | 直接面向 LLM-based MAS 技术栈 | 标题显式含 “A Survey” | http://arxiv.org/abs/2504.01963v1 | 是：`2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` |
| 8 | 2024-12-23 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2025* | 虽 arXiv 发布时间在 2024-12，但当前项目文件按 2025 归档，主题直接命中 | 标题显式含 “A Survey” | http://arxiv.org/abs/2412.17481v1 | 是：`2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` |
| 9 | 2025-01-11 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | 直接讨论 collaboration mechanisms、structures、strategies | 标题显式含 “A Survey” | http://arxiv.org/abs/2501.06322v1 | 是：`2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` |
| 10 | 2025-02-20 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | 直接面向 communication-centric LLM-MAS | 标题显式含 “Survey” | http://arxiv.org/abs/2502.14321v2 | 是：`2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` |
| 11 | 2025-02-24 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | 2025 | 领域型但直接是 LLM-based multi-agent ADS survey | 标题显式含 “A Survey” | http://arxiv.org/abs/2502.16804v2 | 是：`2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` |
| 12 | 2024-02-02 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | 当前仓库里最早的核心总览基线之一 | 标题显式含 “A Survey” | http://arxiv.org/abs/2402.01680v1 | 是：`2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` |

> 注：第 8 篇在 arXiv 数据中的 `published` 为 2024-12-23，因此若后续严格限定 2025-2026，需要决定是否将其视作 2024 候选；当前先保留，因为它在现有项目阅读集里已被使用且主题高度相关。

## B 组：专题型高相关候选（补位池）

这些论文不一定是“通用 multi-agent survey”，但与 agentic / multi-agent 研究主线高度相关，适合在 final 10 需要补充专题维度时纳入比较。

| # | Published | Title | 年份 | 保留理由 | Survey/Review 证据 | 来源 | 本地 PDF |
|---|---|---|---:|---|---|---|---|
| 13 | 2026-03-24 | SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy | 2026 | 安全专题；摘要明确提到 autonomous multi-agent decision loops | 标题含 SoK；摘要 “In this systematization...” | http://arxiv.org/abs/2603.22928v1 | 是：`2026-dehghantanha-homayoun-attack-surface-of-agentic-ai.pdf` |
| 14 | 2026-03-20 | Memory poisoning and secure multi-agent systems | 2026 | multi-agent memory security 专题；直接讨论 agent 间 memory poisoning | 摘要含 “we first present... we review...” | http://arxiv.org/abs/2603.20357v1 | 否 |
| 15 | 2026-03-09 | Security Considerations for Multi-agent Systems | 2026 | 直接面向 MAS 安全威胁与框架覆盖率 | 摘要含 “This study systematically characterizes...” | http://arxiv.org/abs/2603.09002v1 | 否 |
| 16 | 2026-03-08 | Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers | 2026 | agent memory 专题；摘要点名 multi-agent teamwork | 标题为机制/评测/frontiers 综述；摘要 “This survey offers...” | http://arxiv.org/abs/2603.07670v1 | 是：`2026-du-memory-for-autonomous-llm-agents.pdf` |
| 17 | 2026-01-14 | The AI Hippocampus: How Far are We From Human Memory? | 2026 | memory taxonomy 专题；摘要点名 agentic memory 与 multi-agent systems | 标题与摘要均为 survey 结构 | http://arxiv.org/abs/2601.09113v1 | 否 |
| 18 | 2026-01-05 | Agentic AI in Remote Sensing: Foundations, Taxonomy, and Emerging Systems | 2026 | 领域型专题，明确区分 single-agent copilots 与 multi-agent systems | 摘要 “This survey presents the first comprehensive review...” | http://arxiv.org/abs/2601.01891v1 | 否 |
| 19 | 2026-02-24 | Federated Multi Agent Deep Learning and Neural Networks for Advanced Distributed Sensing in Wireless Networks | 2026 | 更偏传统 multi-agent deep learning，但属于 multi-agent survey 扩展边界 | 摘要首句含 “This survey synthesizes...” | http://arxiv.org/abs/2603.16881v1 | 否 |

## 当前建议的后续筛选顺序

如果下一轮要把候选进一步收敛到 10 篇，建议按以下顺序优先核验：

### 第一优先级：最可能进入 final 10 的核心池

1. Xu 2026 — Tool Use in LLM Agents
2. Yue 2026 — Workflow Optimization for LLM Agents
3. Chen et al. 2026 — Five Ws of Multi-Agent Communication
4. Hao et al. 2026 — Game-Theoretic Lens on LLM-based Multi-Agent Systems
5. Arunkumar et al. 2026 — Agentic AI: Architectures, Taxonomies, and Evaluation
6. Wang et al. 2026 — Role-Playing Agents
7. Aratchige & Ilmini 2025 — LLMs Working in Harmony
8. Chen et al. 2025/2412.17481 — Recent Advances and New Frontiers in Application
9. Tran et al. 2025 — Collaboration Mechanisms
10. Yan et al. 2025 — Communication-Centric Survey
11. Wu et al. 2025 — Autonomous Driving Survey
12. Guo et al. 2024 — Progress and Challenges（作为基线）

### 第二优先级：如果需要补专题维度

13. Dehghantanha & Homayoun 2026 — Agentic AI attack surface
14. Torra & Bras-Amorós 2026 — Memory poisoning and secure MAS
15. Nguyen et al. 2026 — Security Considerations for Multi-agent Systems
16. Du 2026 — Memory for Autonomous LLM Agents
17. Jia et al. 2026 — The AI Hippocampus
18. Talemi et al. 2026 — Agentic AI in Remote Sensing
19. Muller et al. 2026 — Federated Multi Agent Deep Learning...

## 初步观察

1. **2026 年候选显著增加了“agentic”与“专题化综述”比例。** 这说明“通用 LLM-MAS survey”之外，安全、memory、workflow、tool orchestration、role-playing 等子问题正在快速独立成综述方向。
2. **最直接的 multi-agent 主线仍集中在 communication / collaboration / architecture / workflow。** 这四条线同时得到 A 组多篇论文支撑，适合作为后续 final 10 的骨架。
3. **仓库现有 `literature/` 已经覆盖了 A 组中的多数核心候选。** 这意味着后续工作重点可以从“找论文”切换到“核验 survey 身份与统一 final 10”。
4. **候选池里存在不少伪相关项。** 例如部分标题虽含 multi-agent 或 agentic，但本质是系统论文、benchmark、position paper 或应用论文；因此下一轮必须逐篇做 survey 属性核验，不能只依赖关键词命中。

## 待下一轮回答的问题

1. final 10 是否严格限定 **2025-2026**，还是允许保留 2024 的基线总览（如 Guo 2024）？
2. 是否把“agentic AI general survey”视为 multi-agent 直接候选，还是仅作为补位池？
3. 对于领域型综述（自动驾驶、遥感、无线网络），是否计入 final 10，还是优先保留更通用的 MAS survey？

## 结论

本轮已基于仓库中可追溯的 arXiv 候选快照完成初筛，得到 **19 篇** 最新 multi-agent / agentic 相关综述候选，满足“初步候选不少于 15 篇”的任务要求。后续应在此清单基础上继续完成：

- 逐篇核验其是否属于真正的 survey / review / SoK；
- 按“新近程度 + multi-agent 直接相关性”收敛到 final 10；
- 对未落盘候选补抓 PDF 并统一命名。
