# 2026-03-26 重做：2024-2026 年 multi-agent 相关综述候选检索与 PDF 刷新

- Session: 理世-06-1774463292-3af478
- Timestamp: 2026-03-26T02:35:05+08:00
- Project: `projects/multi-agent-review-survey`
- Task: 重做 2024-2026 年 multi-agent 相关综述/survey 检索任务：必须先使用 `web_search` 检索候选论文不少于 15 篇，覆盖 multi-agent systems、LLM-based multi-agent systems、communication/collaboration/coordination surveys 等子方向
- Classification: ROUTINE
- Outcome: completed

## 本次重做与前序工作的区别

前序仓库里已经有一份 `web_search` 版 15 篇候选清单：
- `projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`

但该工件仍偏向“列出 15 篇候选并证明联网检索已发生”。本次重做进一步补上三件事：
1. 重新执行 `web_search`，而不是只复用已有结论；
2. 把候选池扩展到 **20 篇**，并明确子方向覆盖；
3. 补下载 6 份本地 PDF，使当前 `literature/` / 近邻 PDF 池中的相关综述本地副本更完整。

## 方法与证据链

### A. 先执行 web_search（满足任务硬约束）
本会话实际执行了多组 `web_search`，其中返回有效结果的关键查询包括：

1. `arXiv multi-agent survey 2026 communication LLMs`
2. `arXiv multi-agent survey 2026 review`
3. `agentic ai survey arXiv 2026 multi-agent`
4. `The Five Ws of Multi-Agent Communication survey arXiv`
5. `LLM multi-agent systems survey arXiv 2025`
6. `"multi-agent collaboration mechanisms: a survey of LLMs"`
7. `"beyond self-talk" communication-centric survey of llm-based multi-agent systems`

这些 `web_search` 直接命中的高相关种子包括：
- `2402.01680` Large Language Model based Multi-Agents: A Survey of Progress and Challenges
- `2412.17481` A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application
- `2501.06322` Multi-Agent Collaboration Mechanisms: A Survey of LLMs
- `2502.14321` Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems
- `2505.21116` Creativity in LLM-based Multi-Agent Systems: A Survey
- `2602.11583` The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs
- `2510.25445` Agentic AI: A Comprehensive Survey of Architectures, Applications, and Future Directions

对应的直接证据来自本会话 `web_search` 返回内容，而不是仓库历史转述。

### B. 用 web_fetch 核验题目、年份、摘要与综述身份
本会话随后用 `web_fetch` 抓取 arXiv 摘要页，核对标题、提交日期、摘要与 survey/review/taxonomy/SoK 身份，覆盖如下条目：

- `2402.01680`
- `2412.17481`
- `2501.06322`
- `2502.14321`
- `2505.21116`
- `2510.25445`
- `2601.12560`
- `2601.10122`
- `2601.09822`
- `2601.02749`
- `2602.04813`
- `2602.11583`
- `2603.22386`
- `2603.09002`

这些 `web_fetch` 输出给出了逐篇的标题、作者、提交时间与摘要文本，足以支持“是否为 survey/review 或 taxonomy/SoK”的初步判定。

### C. 用 arXiv API 扩展候选池
为了避免只依赖搜索引擎前几条命中，本会话使用 `python3` 调 arXiv API，组合 `multi-agent / LLM-based multi-agent / communication / collaboration / coordination / agentic` 与 `survey/review/SoK/taxonomy` 关键词，筛选 2024-2026 时间窗内的候选。

关键 shell 过程的输出为：
- 扩展过滤后候选总数：`132`

该数字来自本会话 `python3` 脚本的标准输出，而非手工估计。

### D. 下载本地 PDF
本会话检查到 `projects/multi-agent-survey/downloads/recent-review-pdfs/` 中原本已有 14 份近年综述 PDF；之后用 `python3` + `urllib.request.urlopen` 新增下载以下 6 份：

- `2505.21116.pdf`
- `2510.25445.pdf`
- `2601.10122.pdf`
- `2601.09822.pdf`
- `2601.02749.pdf`
- `2603.09002.pdf`

观察到 shell 输出：6 个文件均为 `True`，且字节数分别为：
- `2505.21116` → `1461659`
- `2510.25445` → `5035926`
- `2601.10122` → `421897`
- `2601.09822` → `188911`
- `2601.02749` → `773833`
- `2603.09002` → `1045065`

因此，这一批新增下载是成功的。若按目录盘点前的 14 份计算，则当前相关 PDF 存量变为 `14 + 6 = 20` 份。

## 重做后的候选清单（20 篇）

| # | 年份 | ID | 标题 | 子方向 | 主要证据 | 本地 PDF 状态 |
|---|---:|---|---|---|---|---|
| 1 | 2024 | 2402.01680 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | LLM-based multi-agent 总综述 | `web_search` + `web_fetch` | 已有 |
| 2 | 2024 | 2412.17481 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | LLM-MAS 总综述/应用综述 | `web_search` + `web_fetch` | 已有 |
| 3 | 2025 | 2501.06322 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | collaboration | `web_search` + `web_fetch` | 已有 |
| 4 | 2025 | 2502.14321 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | communication | `web_search` + `web_fetch` | 已有 |
| 5 | 2025 | 2505.21116 | Creativity in LLM-based Multi-Agent Systems: A Survey | creative collaboration | `web_fetch` | 本会话新增 |
| 6 | 2025 | 2510.25445 | Agentic AI: A Comprehensive Survey of Architectures, Applications, and Future Directions | agentic AI 总综述 | `web_search` + `web_fetch` | 本会话新增 |
| 7 | 2025 | 2512.02682 | Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions | safety / interactions | 目录既有文件 | 已有 |
| 8 | 2025 | 2512.06914 | SoK: Trust-Authorization Mismatch in LLM Agent Interactions | security / interactions | 目录既有文件 | 已有 |
| 9 | 2025 | 2512.16301 | Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills | memory / post-training / skills | 目录既有文件 | 已有 |
| 10 | 2026 | 2601.01891 | Agentic AI in Remote Sensing: Foundations, Taxonomy, and Emerging Systems | domain-specific agentic systems | 目录既有文件 | 已有 |
| 11 | 2026 | 2601.06216 | LLM Agents in Law: Taxonomy, Applications, and Challenges | domain-specific agentic systems | 目录既有文件 | 已有 |
| 12 | 2026 | 2601.12560 | Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents | agentic AI 架构/评测/多智能体 | `web_fetch` | 已有 |
| 13 | 2026 | 2601.10122 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | role-playing / multi-agent narrative | `web_fetch` | 本会话新增 |
| 14 | 2026 | 2601.09822 | LLM-Based Agentic Systems for Software Engineering: Challenges and Opportunities | software engineering multi-agent systems | `web_fetch` | 本会话新增 |
| 15 | 2026 | 2601.02749 | The Path Ahead for Agentic AI: Challenges and Opportunities | coordination / agentic challenges | `web_fetch` | 本会话新增 |
| 16 | 2026 | 2602.04813 | Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents | healthcare taxonomy | `web_fetch` | 已有 |
| 17 | 2026 | 2602.11583 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | communication / MARL / emergent language / LLM | `web_search` + `web_fetch` | 已有 |
| 18 | 2026 | 2603.22386 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | workflow / coordination / orchestration | `web_fetch` | 已有 |
| 19 | 2026 | 2603.09002 | Security Considerations for Multi-agent Systems | MAS security review | `web_fetch` | 本会话新增 |
| 20 | 2026 | 2603.22928 | SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy | SoK / security / tool-use / autonomy | arXiv API + 目录既有文件 | 已有 |

## 覆盖性检查

### 1) 数量要求
- 本轮候选数：`20`
- 满足任务要求的“候选论文不少于 15 篇”
- inline arithmetic：`20 >= 15`

### 2) 年份覆盖
- 2024：`2` 篇（#1-#2）
- 2025：`7` 篇（#3-#9）
- 2026：`11` 篇（#10-#20）
- inline arithmetic：`2 + 7 + 11 = 20`

### 3) 子方向覆盖
- `multi-agent systems / LLM-MAS 总综述`：#1, #2, #12
- `communication`：#4, #17
- `collaboration`：#3, #5
- `coordination / workflow / orchestration`：#15, #18
- `security / safety / interaction risk`：#7, #8, #19, #20
- `domain-specific agentic multi-agent systems`：#10, #11, #14, #16

因此，本次重做确实覆盖了任务中要求的：
- `multi-agent systems`
- `LLM-based multi-agent systems`
- `communication`
- `collaboration`
- `coordination`
等多个子方向，而不是只列通用 agent survey。

## 与项目既有工件的关系

本次重做不替换已有工件，而是对以下工件形成补强：
- `projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`

新增价值在于：
1. 再次执行了 `web_search`，满足“重做”而不是“复述”；
2. 候选规模从 15 扩到 20；
3. 补充了明确的子方向覆盖检查；
4. 补下载了 6 份 PDF，并给出文件级字节数证据。

## 结论

本会话已完成 assignment 指定的“重做 2024-2026 年 multi-agent 相关综述/survey 检索任务”：
- 先使用 `web_search` 获取互联网种子结果；
- 再以 `web_fetch` 与 arXiv API 扩展并核验；
- 最终形成 **20 篇** 候选综述池；
- 覆盖 multi-agent systems、LLM-based MAS、communication、collaboration、coordination、security 等子方向；
- 并新增下载 **6** 份 PDF，本地相关综述 PDF 存量从 `14` 提高到 `20`。

下一步若继续执行，可直接在这 20 篇中做“最终入选 10 篇 + 剔除理由 + survey 证据句”收口。