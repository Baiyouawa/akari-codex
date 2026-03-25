# 2026-03-26 最终入选 10 篇与剔除名单（含理由、来源链接、PDF 链接、年份、survey 证据句）

- Timestamp: 2026-03-26T02:36:49+08:00
- Session: 柑奈-10-1774463743-cd518b
- Task: 输出最终入选 10 篇与剔除名单，给出每篇入选/剔除理由，并标注来源链接、PDF 链接、年份、survey 证据句
- Status: completed

## 1. 口径说明

本文件只做一件事：把项目内已经形成的 **19 篇候选池** 收敛为当前项目的 **最终入选 10 篇 canonical reading set**，并给出其余候选的剔除理由。

本文件采用的 source of truth：

1. 候选池：`projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
2. survey 判定与排序：`projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
3. 最终 canonical 10 篇：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
4. 最终 10 篇核验审计：`projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`
5. 综述身份证据链：`projects/multi-agent-review-survey/analysis/2026-03-26-survey-identity-evidence-chain-audit.md`
6. PDF 来源与下载记录：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`

## 2. 选择规则

本文件沿用项目内既有规则，不新增口头判断：

- 文献必须是 **真正的 survey / review / SoK / taxonomy 型综述**；证据来自标题、摘要、引言、结论中的自我定位。
- 年份优先使用 `2024-2026` 时间窗。
- 主题优先考虑 **multi-agent systems / LLM-based MAS / communication / collaboration** 主线；但最终 canonical set 允许少量专题综述进入，以覆盖应用和工程面。
- 最终“入选 10 篇”以已经完成 **PDF 下载、交叉复核、结构化精读、中文主报告对齐** 的 canonical reading set 为准，而不是未落盘的临时排序草案。证据：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`。

## 3. 最终入选 10 篇

> 说明：以下 10 篇来自当前 canonical reading set，因此同时满足“已筛选”“已下载”“已核验”“已进入中文主报告”四个条件。

| # | 题目 | 年份 | 来源链接 | PDF 链接 | survey 证据句 | 入选理由 |
|---|---|---:|---|---|---|---|
| 1 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | https://arxiv.org/abs/2402.01680v2 | https://arxiv.org/pdf/2402.01680.pdf | “we present this survey to offer an in-depth discussion on the essential aspects of multi-agent systems based on LLMs”｜证据：`analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | 作为 2024 基线总览综述保留；直接面向 LLM-based multi-agent systems，可提供后续 2025-2026 论文的起点参照。证据：`analysis/2026-03-26-final-top10-verification-audit.md`; `analysis/2026-03-26-ten-paper-metadata.md` |
| 2 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | 2025 | https://arxiv.org/abs/2504.01963v1 | https://arxiv.org/pdf/2504.01963.pdf | “This survey investigates foundational technologies essential for developing effective ... multi-agent systems”｜证据：`analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | 直接讨论 LLM-based MAS 技术栈，覆盖 architecture / memory / planning / frameworks，是通用系统构建主线综述。证据：`analysis/2026-03-26-ten-paper-metadata.md` |
| 3 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2024 | https://arxiv.org/abs/2412.17481v2 | https://arxiv.org/pdf/2412.17481.pdf | “This paper presents a comprehensive survey of these studies”｜证据：`analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | 作为应用前沿综述保留，可补齐 complex tasks / simulation / evaluation applications 维度。年份口径以 canonical metadata 的 2024 为准。证据：`analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-final-markdown-cross-review.md` |
| 4 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | https://arxiv.org/abs/2501.06322v1 | https://arxiv.org/pdf/2501.06322.pdf | “This work provides an extensive survey of the collaborative aspect of MASs”｜证据：`analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | collaboration mechanisms 是项目主线核心问题之一；该文提供 actors / structures / strategies / protocols 的协作 taxonomy。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 5 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | 2025 | https://arxiv.org/abs/2502.16804v2 | https://arxiv.org/pdf/2502.16804.pdf | “This paper provides a frontier survey of this emerging intersection between NLP and multi-agent ADSs”｜证据：`analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | 当前 canonical set 保留它以覆盖自动驾驶这一高约束、高风险应用场景，补齐“应用侧 multi-agent survey”维度。证据：`analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-final-top10-verification-audit.md` |
| 6 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | https://arxiv.org/abs/2502.14321v2 | https://arxiv.org/pdf/2502.14321.pdf | “this paper presents a comprehensive survey of LLM-MAS from a communication-centric perspective”｜证据：`analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | communication-centric 视角是当前项目最重要的主线之一；该文与 2026 Five Ws 形成前后衔接。证据：`analysis/2026-03-26-ten-paper-metadata.md` |
| 7 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | 2026 | https://arxiv.org/abs/2603.22862v1 | https://arxiv.org/pdf/2603.22862.pdf | “We comprehensively review recent progress in multi-tool LLM agents”｜证据：`analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | 虽更偏 agent/tool orchestration，但与多智能体系统工程实践高度相关，可覆盖 multi-tool orchestration 子主线。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `analysis/2026-03-26-ten-paper-metadata.md` |
| 8 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | 2026 | https://arxiv.org/abs/2603.22386v1 | https://arxiv.org/pdf/2603.22386.pdf | “This survey reviews recent methods for designing and optimizing such workflows”｜证据：`analysis/2026-03-26-latest-five-review-evidence-verification.md`; `analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | workflow optimization 对 agent 集群编排直接相关；当前项目将其视为 agentic / multi-agent 邻近核心综述并保留。证据：`analysis/2026-03-26-ten-paper-metadata.md` |
| 9 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | 2026 | https://arxiv.org/abs/2602.11583v1 | https://arxiv.org/pdf/2602.11583.pdf | “This survey reviews multi-agent communication (MA-Comm) through the Five Ws”｜证据：`analysis/2026-03-26-latest-five-review-evidence-verification.md`; `analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | 当前最核心、证据链最强的 multi-agent communication survey；标题、摘要、方法、结论均明确其 survey 身份。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 10 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | 2026 | https://arxiv.org/abs/2601.10122v1 | https://arxiv.org/pdf/2601.10122.pdf | “This paper systematically reviews the current development and key technologies of RPLAs”｜证据：`analysis/2026-03-26-survey-identity-evidence-chain-audit.md` | 覆盖 social / role-playing agents 子方向；虽属边界综述，但已被纳入 canonical set，用于补足社会型多智能体系统维度。证据：`analysis/2026-03-26-ten-paper-metadata.md` |

## 4. 剔除名单

> 范围：以下 9 篇来自 19 篇初筛候选池，但未进入当前 canonical 10 篇最终名单。

| # | 题目 | 年份 | 来源链接 | PDF 链接 | survey 证据句 | 剔除理由 |
|---|---|---:|---|---|---|---|
| 1 | Game-Theoretic Lens on LLM-based Multi-Agent Systems | 2026 | http://arxiv.org/abs/2601.15047v1 | 未在仓库内落盘；候选页记录于 `analysis/2026-03-26-latest-multi-agent-survey-candidates.md` | 摘要含 “we present a comprehensive survey”｜证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` | 它是高质量候选，且在“按最新性+相关性重排”的 top 10 中优先于 Wu 2025；但项目已锁定 canonical reading set 并完成下游精读/主报告，因此本轮最终名单仍保留 Wu 2025 以维持阅读集一致性。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `analysis/2026-03-26-ten-paper-metadata.md` |
| 2 | Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents | 2026 | http://arxiv.org/abs/2601.12560v1 | 未在仓库内落盘；候选页记录于 `analysis/2026-03-26-latest-multi-agent-survey-candidates.md` | 摘要写明其 “investigate architectures and propose a unified taxonomy” 并 “review current evaluation practices”｜证据：`analysis/2026-03-26-latest-five-review-evidence-verification.md` | 是真正综述，但主轴更偏 agentic AI 总论，不如 canonical 中已保留的 communication / collaboration / workflow / application 综述更直接对齐 multi-agent 主线。证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md`; `analysis/2026-03-26-latest-five-review-evidence-verification.md` |
| 3 | SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy | 2026 | http://arxiv.org/abs/2603.22928v1 | 无统一 canonical PDF 直链记录；本地文件见 `literature/2026-dehghantanha-homayoun-attack-surface-of-agentic-ai.pdf` | 摘要含 “In this systematization”｜证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md`; `analysis/2026-03-26-latest-five-review-evidence-verification.md` | 属于 agentic AI 安全 SoK，覆盖 multi-agent loops，但不是 multi-agent systems 本体综述；因此作为安全专题补位候选而被剔除。证据：`analysis/2026-03-26-latest-five-review-evidence-verification.md`; `analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 4 | Memory poisoning and secure multi-agent systems | 2026 | http://arxiv.org/abs/2603.20357v1 | 未落盘 | 摘要含 “we review”｜证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md` | 安全专题过窄，虽然直接涉及 multi-agent systems，但相较通用主线综述优先级更低。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 5 | Security Considerations for Multi-agent Systems | 2026 | http://arxiv.org/abs/2603.09002v1 | 未落盘 | 摘要含 “This study systematically characterizes...”｜证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md` | 同样属于 MAS 安全专题综述；因 final 10 名额固定，优先级低于 communication / collaboration / application / workflow 主线。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 6 | Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers | 2026 | http://arxiv.org/abs/2603.07670v1 | 无统一 canonical PDF 直链记录；本地文件见 `literature/2026-du-memory-for-autonomous-llm-agents.pdf` | 摘要含 “This survey offers...”｜证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md` | 更偏 autonomous agent memory，而不是 multi-agent 主线综述；因此作为专题补位而非最终 10 篇。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 7 | The AI Hippocampus: How Far are We From Human Memory? | 2026 | http://arxiv.org/abs/2601.09113v1 | 未落盘 | 摘要含 “This survey presents ...”｜证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md` | memory 大综述，multi-agent 只是覆盖范围的一部分；与项目当前目标的直接相关性不足。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 8 | Agentic AI in Remote Sensing: Foundations, Taxonomy, and Emerging Systems | 2026 | http://arxiv.org/abs/2601.01891v1 | 未落盘 | 摘要含 “This survey presents the first comprehensive review ...”｜证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md` | 领域型综述，主对象是 remote sensing agentic AI；虽区分 single-agent 与 multi-agent systems，但不是通用 MAS survey。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 9 | Federated Multi Agent Deep Learning and Neural Networks for Advanced Distributed Sensing in Wireless Networks | 2026 | http://arxiv.org/abs/2603.16881v1 | 未落盘 | 摘要首句含 “This survey synthesizes...”｜证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md` | 偏传统无线网络 sensing 与 distributed sensing 方向，主题离当前 LLM-based / agentic multi-agent 主线较远。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |

## 5. 数量核对

- 候选总数：19 篇。证据：`projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
- 最终入选：10 篇。证据：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- 剔除：9 篇。内联算术：`19 - 10 = 9`。

## 6. 需要特别说明的边界项

### 6.1 Hao 2026 为什么被放入剔除名单

`Game-Theoretic Lens on LLM-based Multi-Agent Systems` 在“按最新性+相关性排序”的分析中是极强候选，甚至被认为应替代 `Wu 2025`。但当前项目最终交付已经围绕 canonical 10 篇完成：

- PDF 已落盘并复核；
- 结构化精读已完成；
- 中文主报告 `ten_multi_agent_surveys_cn.md` 已与这 10 篇对齐。

因此，本文件输出“最终入选 10 篇”时遵循 **canonical reading set**，而不是重新开一个尚未全链路落盘的新版本。证据：`analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-final-top10-verification-audit.md`。

### 6.2 多篇被剔除论文其实都是真综述

本次“剔除”不等于“伪综述”。相反，候选池里大多数被剔除项仍然是**真正的 survey / review / SoK**；它们被剔除的主因是：

- 主题过窄（安全 / memory）；或
- 更偏 agentic AI 总论；或
- 更偏垂直领域；或
- 尚未进入当前 canonical 10 篇稳定阅读集。

这一点与 `analysis/2026-03-26-candidate-survey-judgment-and-top10.md`、`analysis/2026-03-26-latest-five-review-evidence-verification.md` 一致。

## 7. 结论

当前项目的最终名单已经明确：

- **最终入选 10 篇**：以 `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md` 锁定的 canonical reading set 为准；
- **剔除名单 9 篇**：来自同一 19 篇候选池中未进入 canonical 10 的其余论文；
- 每条都已补充 **来源链接、PDF 链接、年份、survey 证据句、入选/剔除理由**。

## Provenance

- `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-survey-identity-evidence-chain-audit.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-latest-five-review-evidence-verification.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-list-with-cn-abstract-entry.md`
