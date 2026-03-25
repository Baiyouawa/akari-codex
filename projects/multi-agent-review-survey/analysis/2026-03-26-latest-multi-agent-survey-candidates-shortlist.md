# 2026-03-26 近年最新 multi-agent 相关综述/survey 候选短名单

- Timestamp: 2026-03-26T01:39:54+08:00
- Session: 理世-06-1774460347-c498ca
- Task: 检索近年最新的 multi-agent 相关综述/survey 候选论文，优先 2024-2026，给出题目、年份、链接与入选理由
- Status: completed

## 方法与证据范围

本次不重复发散检索，而是复用项目内已经落盘并经前序会话核验的候选池与联网检索结果，整理一份直接可用的候选短名单：

1. 本地 arXiv 候选池：`projects/multi-agent-review-survey/sources/2026-03-26-arxiv-multi-agent-survey-candidates.json`
2. 本地初筛结果（19 篇）：`projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
3. 联网补充结果（15 篇）：`projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`
4. 逐篇综述属性核验与 top 10 排序：`projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`

入选理由统一按以下口径整理：
- 年份优先：2026 > 2025 > 2024
- 主题优先：直接面向 multi-agent systems / LLM-based MAS / communication / collaboration / workflow / role-playing
- 文献类型：标题或摘要明确是 survey / review / SoK / taxonomy

## 候选短名单（按新近程度与相关性排序）

| # | 题目 | 年份 | 链接 | 入选理由 |
|---|---|---:|---|---|
| 1 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | 2026 | https://arxiv.org/abs/2602.11583 | 直接研究 multi-agent communication，标题显式为 survey，且覆盖 MARL、emergent language 与 LLM agents，是当前最核心的 multi-agent 主线综述之一。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 2 | Game-Theoretic Lens on LLM-based Multi-Agent Systems | 2026 | https://arxiv.org/abs/2601.15047 | 直接面向 LLM-based multi-agent systems，摘要明确为 comprehensive survey，并提供 game-theoretic 统一框架，兼具新近性与通用性。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 3 | Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents | 2026 | https://arxiv.org/abs/2601.12560 | 覆盖从单 agent 到 hierarchical multi-agent systems 的架构、taxonomy 与 evaluation，属于通用 agentic/multi-agent 总览。证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md` |
| 4 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | 2026 | https://arxiv.org/abs/2603.22862 | 虽聚焦 tool use，但主题直接连接 multi-tool orchestration 与 agent 系统协作，是 2026 年最贴近工程实践的 agent 综述之一。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 5 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | 2026 | https://arxiv.org/abs/2603.22386 | 直接讨论 workflow optimization，可支撑多 agent runtime graph 与编排问题，和仓库内 agent 集群任务高度相关。证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md` |
| 6 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | 2026 | https://arxiv.org/abs/2601.10122 | 属于 2026 年升温很快的 social / role-playing multi-agent 子方向，摘要明确是系统性综述。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 7 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi-Agent Systems | 2025 | https://arxiv.org/abs/2504.01963 | 直接讨论 LLM-based MAS 技术栈，主题非常聚焦且标题显式为 survey，适合作为通用 multi-agent engineering 代表综述。证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md`；`analysis/2026-03-26-web-search-15-survey-candidates-refresh.md` |
| 8 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | https://arxiv.org/abs/2502.14321 | 2025 年 communication-centric 代表综述，与 2026 Five Ws 形成前后衔接，适合作为通信主线的重要候选。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 9 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | https://arxiv.org/abs/2501.06322 | 直接讨论 collaboration mechanisms，是 LLM multi-agent systems 的核心问题之一，标题显式为 survey。证据：`analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`；`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 10 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2024 | https://arxiv.org/abs/2412.17481 | 尽管 arXiv 发布时间为 2024-12，但仍处于近年窗口内，且是通用 LLM-MAS 总览类综述，适合作为 2024→2026 演化链条中的基线。证据：`analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`；`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` |
| 11 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | https://arxiv.org/abs/2402.01680 | 是当前项目内最早但仍高相关的基线总览综述，适合补充“发展起点”视角。若更强调最新性，可降为备选。证据：`analysis/2026-03-26-web-search-15-survey-candidates-refresh.md` |
| 12 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | 2025 | https://arxiv.org/abs/2502.16804 | 垂直领域型综述，但仍是明确的 LLM-based multi-agent survey；若需要应用侧代表，可以作为候选补位。证据：`analysis/2026-03-26-latest-multi-agent-survey-candidates.md` |

## 结论

若目标是“先给出近年最新、最值得继续精读的 multi-agent 综述候选”，则优先推荐前 10 篇；其中前 6 篇全部来自 2026 年，代表当前最靠近前沿的通用主线综述。若需要保留一篇更早但奠基性的基线综述，则可额外关注 `2402.01680`。

## Provenance

- `projects/multi-agent-review-survey/sources/2026-03-26-arxiv-multi-agent-survey-candidates.json`
- `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`
