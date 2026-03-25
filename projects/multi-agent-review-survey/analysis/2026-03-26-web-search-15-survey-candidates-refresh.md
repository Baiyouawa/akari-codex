# 2026-03-26 Web 检索补充：2024-2026 multi-agent / LLM agents / cooperative agents 综述候选（15 篇）

- Session: 千早-05-1774459025-ee93cb
- Timestamp: 2026-03-26T01:24:26+08:00
- Task: 使用 `web_search` / `web_fetch` 检索 2024-2026 年 multi-agent systems / LLM agents / cooperative agents 相关综述或 survey，整理不少于 15 篇候选，附标题、年份、来源 URL
- Scope: 独立于仓库内既有候选池，直接使用联网检索补充一份可追溯候选清单

## 方法

1. 先检查仓库内已有项目文档：
   - `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
   - `projects/multi-agent-review-survey/TASKS.md`
2. 使用 `web_search` 查询以下关键词组合：
   - `LLM agents survey 2025 arXiv`
   - `multi-agent systems review 2024 arXiv`
   - `2025 arXiv survey cooperative decision-making multi-agent`
   - `2024 IJCAI large language model based multi-agents survey progress challenges`
   - `2025 arXiv survey communication-centric LLM-based multi-agent systems`
   - `2025 arXiv survey agentic large language models`
   - `2025 survey evaluation benchmarking LLM agents arxiv`
   - `2025 survey spatial intelligence embodied agents large language model arxiv`
   - `2024 2025 survey software engineering LLM-based multi-agent systems arxiv`
3. 对核心候选使用 `web_fetch` 抓取 arXiv 摘要页，核验标题、作者、提交时间、摘要范围与 survey 身份。
4. 纳入规则：
   - 年份在 2024-2026；
   - 标题或摘要明确属于 survey / review / literature review / SoK；
   - 主题与 multi-agent systems、LLM agents、cooperative agents 直接相关，或属于后续 final 10 筛选时值得保留的高相关专题综述。

## 候选综述清单（15 篇）

| # | 标题 | 年份 | 方向 | 来源 URL | 来源类型 |
|---|---|---:|---|---|---|
| 1 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | LLM-based multi-agent 总综述 | https://arxiv.org/abs/2402.01680 | arXiv abs，`web_fetch` 已核验 |
| 2 | LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision and the Road Ahead | 2024 | 软件工程中的 LLM multi-agent 综述 | https://arxiv.org/abs/2404.04834 | arXiv abs，`web_fetch` 已核验 |
| 3 | A Survey on Large Language Model-based Agents for Statistics and Data Science | 2024 | 数据科学 agents 综述，含多智能体协作设计 | https://arxiv.org/abs/2412.14222 | arXiv abs，`web_fetch` 已核验 |
| 4 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2024 | LLM-MAS 应用综述 | https://arxiv.org/abs/2412.17481 | arXiv abs，`web_fetch` 已核验 |
| 5 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | LLM 多智能体协作机制综述 | https://arxiv.org/abs/2501.06322 | arXiv abs，`web_fetch` 已核验 |
| 6 | A Survey on LLM-powered Agents for Recommender Systems | 2025 | 推荐系统 agents 综述，含 multi-agent simulation 范式 | https://arxiv.org/abs/2502.10050 | arXiv abs，`web_fetch` 已核验 |
| 7 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | communication-centric LLM-MAS 综述 | https://arxiv.org/abs/2502.14321 | arXiv abs，`web_fetch` 已核验 |
| 8 | A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives | 2025 | cooperative decision-making 总综述 | https://arxiv.org/abs/2503.13415 | arXiv abs，`web_fetch` 已核验 |
| 9 | A Survey on the Optimization of Large Language Model-based Agents | 2025 | LLM agents 优化综述 | https://arxiv.org/abs/2503.12434 | arXiv abs，`web_fetch` 已核验 |
| 10 | Survey on Evaluation of LLM-based Agents | 2025 | LLM agents 评测综述 | https://arxiv.org/abs/2503.16416 | arXiv abs，`web_fetch` 已核验 |
| 11 | Large Language Model Agent: A Survey on Methodology, Applications and Challenges | 2025 | LLM agent 方法/应用/挑战总综述 | https://arxiv.org/abs/2503.21460 | arXiv abs，`web_fetch` 已核验 |
| 12 | Agentic Large Language Models, a survey | 2025 | agentic LLM 总综述 | https://arxiv.org/abs/2503.23037 | arXiv abs，`web_fetch` 已核验 |
| 13 | A Survey of Large Language Model-Powered Spatial Intelligence Across Scales: Advances in Embodied Agents, Smart Cities, and Earth Science | 2025 | embodied / spatial agents 综述 | https://arxiv.org/abs/2504.09848 | arXiv abs，`web_fetch` 已核验 |
| 14 | Creativity in LLM-based Multi-Agent Systems: A Survey | 2025 | 创意生成场景的 LLM-MAS 综述 | https://arxiv.org/abs/2505.21116 | arXiv abs，`web_fetch` 已核验 |
| 15 | Evaluation and Benchmarking of LLM Agents: A Survey | 2025 | LLM agents 评测与基准综述 | https://arxiv.org/abs/2507.21504 | arXiv abs，`web_fetch` 已核验 |

## 核验摘录

以下信息直接来自本次 `web_fetch` 的 arXiv 摘要页：

1. `2402.01680`：标题为 **Large Language Model based Multi-Agents: A Survey of Progress and Challenges**，提交时间为 `21 Jan 2024`，摘要明确写明 “we present this survey”。
2. `2412.17481`：标题为 **A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application**，提交时间为 `23 Dec 2024`，摘要明确写明 “This paper presents a comprehensive survey of these studies”。
3. `2501.06322`：标题为 **Multi-Agent Collaboration Mechanisms: A Survey of LLMs**，提交时间为 `10 Jan 2025`，摘要明确写明 “This work provides an extensive survey”。
4. `2502.14321`：标题为 **Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems**，提交时间为 `20 Feb 2025`，摘要明确写明 “this paper presents a comprehensive survey”。
5. `2503.21460`：标题为 **Large Language Model Agent: A Survey on Methodology, Applications and Challenges**，提交时间为 `27 Mar 2025`，摘要明确写明 “This survey systematically deconstructs LLM agent systems”。
6. `2503.16416`：标题为 **Survey on Evaluation of LLM-based Agents**，提交时间为 `20 Mar 2025`，摘要明确写明 “This paper provides the first comprehensive survey of evaluation methodologies”。
7. `2503.13415`：标题为 **A Comprehensive Survey on Multi-Agent Cooperative Decision-Making...**，提交时间为 `17 Mar 2025`，摘要明确写明 “This paper begins with a comprehensive survey...”。
8. `2503.23037`：标题为 **Agentic Large Language Models, a survey**，提交时间为 `29 Mar 2025`，摘要说明 “We review the growing body of work in this area”。
9. `2503.12434`：标题为 **A Survey on the Optimization of Large Language Model-based Agents**，提交时间为 `16 Mar 2025`，摘要明确写明 “In this survey, we provide a comprehensive review”。
10. `2505.21116`：标题为 **Creativity in LLM-based Multi-Agent Systems: A Survey**，提交时间为 `27 May 2025`，摘要明确写明 “This is the first survey dedicated to creativity in MAS”。
11. `2404.04834`：标题为 **LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision and the Road Ahead**，提交时间为 `7 Apr 2024`，标题直接标记 Literature Review。
12. `2412.14222`：标题为 **A Survey on Large Language Model-based Agents for Statistics and Data Science**，提交时间为 `18 Dec 2024`，摘要说明 “This survey provides an overview...”。
13. `2502.10050`：标题为 **A Survey on LLM-powered Agents for Recommender Systems**，提交时间为 `14 Feb 2025`，摘要说明 “This survey provides a systematic review...”。
14. `2504.09848`：标题为 **A Survey of Large Language Model-Powered Spatial Intelligence Across Scales...**，提交时间为 `14 Apr 2025`，摘要说明 “In this paper, we first review... Through this survey...”。
15. `2507.21504`：标题为 **Evaluation and Benchmarking of LLM Agents: A Survey**，提交时间为 `29 Jul 2025`，摘要说明 “This survey provides an in-depth overview...”。

## 快速分组

### A. 最直接的 multi-agent / LLM-MAS 候选
- #1 Large Language Model based Multi-Agents: A Survey of Progress and Challenges
- #4 A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application
- #5 Multi-Agent Collaboration Mechanisms: A Survey of LLMs
- #7 Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems
- #8 A Comprehensive Survey on Multi-Agent Cooperative Decision-Making...
- #14 Creativity in LLM-based Multi-Agent Systems: A Survey

### B. 面向 LLM agents 总体方法论的综述
- #9 A Survey on the Optimization of Large Language Model-based Agents
- #10 Survey on Evaluation of LLM-based Agents
- #11 Large Language Model Agent: A Survey on Methodology, Applications and Challenges
- #12 Agentic Large Language Models, a survey
- #15 Evaluation and Benchmarking of LLM Agents: A Survey

### C. 垂直领域专题综述，可作为补位池
- #2 软件工程
- #3 统计与数据科学
- #6 推荐系统
- #13 embodied / spatial intelligence

## 统计观察

1. 当前清单共 `15` 篇，满足“不少于 15 篇候选”的任务要求。
   - Provenance: 上表逐项编号 `1-15`。
2. 其中 `2025` 年条目有 `11` 篇，`2024` 年条目有 `4` 篇，`2026` 年条目在本轮可稳定检出的高质量结果中为 `0`。
   - Provenance: 上表年份列；内联算术 `11 + 4 + 0 = 15`。
3. 若只保留“标题直接命中 multi-agent / MAS / cooperative”候选，则至少有 `6` 篇高度直接相关候选。
   - Provenance: 上文 A 组共列出 `6` 篇。

## 与仓库既有候选池的关系

- 仓库内已有 `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`，记录了基于本地 arXiv 快照初筛出的 `19` 篇候选。
- 本文档的作用不是替代那份 19 篇清单，而是补充一份**直接基于本次 web_search/web_fetch 的独立联网检索结果**，用于验证该项目确实具备外部检索来源，而不是只依赖仓库内快照。

## 建议

如果下一轮仍要继续收敛到“最新且最直接相关的 10 篇”，可优先从以下 6 篇开始：
- #5 Multi-Agent Collaboration Mechanisms: A Survey of LLMs
- #7 Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems
- #8 A Comprehensive Survey on Multi-Agent Cooperative Decision-Making...
- #11 Large Language Model Agent: A Survey on Methodology, Applications and Challenges
- #14 Creativity in LLM-based Multi-Agent Systems: A Survey
- #4 A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application

选择依据：标题直接相关性更高，且来源均可追溯到 arXiv 摘要页。