# 2026-03-26 最新 multi-agent 十篇综述筛选结果

## 任务范围
- 目标：检索并筛选与 multi-agent 相关的最新十篇综述论文，优先覆盖 2024-2026。
- 输出要求：每篇记录题目、年份、链接、来源与入选理由，并保留检索与筛选证据，便于后续下载与精读。
- 本轮时间策略：优先 2026 > 2025 > 2024；由于当前可稳定核实的 2026 年直接相关综述较少，最终以 2025/2024 补足。

## 检索时间
- 检索执行时间：2026-03-26（北京时间，见 `functions.get_current_time` 返回 `2026年03月26日 周四 22:50:01`）

## 检索来源与方法
### 来源类别
1. arXiv 论文页 / arXiv API
2. Springer Nature 正式出版页
3. DBLP 记录页（含 DOI 与年份）
4. OpenReview 作为补充核查来源（本次命中 1 篇医学向候选，但页面抓取受限，未进入最终清单）

### 检索关键词
- `"survey on LLM-based multi-agent systems"`
- `"A Survey" "multi-agent systems" "large language models"`
- `ti:"survey" AND abs:"multi-agent"`（arXiv API）
- `ti:"survey" AND all:"LLM-based multi-agent"`（arXiv API）
- `ti:"overview" AND all:"multi-agent"`（arXiv API）
- `multi-agent survey`（DBLP API）

### 筛选规则
**纳入标准**
- 与 multi-agent / multi-agent systems / LLM-based multi-agent / multi-agent communication / multi-agent decision-making 高相关；
- 标题、摘要或来源中可明确识别为 survey / review / overview / taxonomy；
- 2024-2026 优先；
- 链接可稳定落到 arXiv、出版社页面或 DOI/DBLP 入口；
- 最终 10 篇需尽量覆盖不同子方向，避免完全同质化。

**排除标准**
- 普通方法论文、系统论文、benchmark 论文；
- 更宽泛的 agentic AI 综述，但 multi-agent 不是核心主体；
- 来源可访问但权威性或相关性明显弱于已有候选；
- 与已入选条目高度重复且覆盖增益有限。

## 候选池与筛选结论
| 序号 | 候选论文 | 年份 | 初筛结论 | 说明 |
|---|---|---:|---|---|
| 1 | A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | 2024 | 入选 | Springer 正式出版，通用框架综述 |
| 2 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | 入选 | 早期代表性总览，含 benchmark 与挑战 |
| 3 | A survey of multi-agent deep reinforcement learning with communication | 2024 | 入选 | 非 LLM 方向的重要补位，覆盖 MARL 通信 |
| 4 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2024 | 入选 | 侧重应用版图与定义整理 |
| 5 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | 入选 | 协作机制专题，结构化框架清晰 |
| 6 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | 入选 | 以 communication 为主线，和通用综述互补 |
| 7 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | 2025 | 入选 | 代表应用综述，覆盖自动驾驶场景 |
| 8 | A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives | 2025 | 入选 | 覆盖 cooperative decision-making、仿真平台与方法谱系 |
| 9 | Creativity in LLM-based Multi-Agent Systems: A Survey | 2025 | 入选 | 代表新兴创意生成子方向 |
| 10 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | 2026 | 入选 | 2026 新作，连接 MARL / EL / LLM 三条线 |
| 11 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | 2025 | 淘汰 | 与 1/2/4 在“通用 LLM-MAS 技术总览”上高度重叠，主题增益低于 creativity/ADS |
| 12 | A Taxonomy of Hierarchical Multi-Agent Systems: Design Patterns, Coordination Mechanisms, and Industrial Applications | 2025 | 淘汰 | 更像结构 taxonomy 与工业设计讨论，缺少更广领域代表性 |
| 13 | LLM-based Agentic Reasoning Frameworks: A Survey from Methods to Scenarios | 2025 | 淘汰 | 多 agent 只是其分类的一部分，主题中心不是 multi-agent |
| 14 | A Survey of LLM-based Multi-agent Systems in Medicine | 2025 | 淘汰 | OpenReview 页面抓取受限，且领域过窄；本轮优先保留更通用或更高影响应用面 |
| 15 | Large Language Model Applied in Multi-agent System—A Survey | 2024 | 淘汰 | 可访问，但来源权威性与综述深度弱于 Springer/arXiv/期刊候选 |

## 最终入选 10 篇
| 序号 | 题目 | 年份 | 链接 | 来源 | 入选理由 |
|---|---|---:|---|---|---|
| 1 | A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | 2024 | https://link.springer.com/article/10.1007/s44336-024-00009-2 | Springer / Vicinagearth | 正式出版的开放获取综述；按 workflow 拆成 profile、perception、self-action、mutual interaction、evolution 五部分，是后续搭建统一分析框架的最好起点之一。 |
| 2 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | https://arxiv.org/abs/2402.01680 | arXiv | 2024 年较早系统综述，摘要明确总结多智能体模拟环境、通信、能力增长机制和常用 benchmark，适合作为时间线起点。 |
| 3 | A survey of multi-agent deep reinforcement learning with communication | 2024 | https://dblp.org/rec/journals/aamas/ZhuDW24 | DBLP / Autonomous Agents and Multi-Agent Systems / DOI 10.1007/S10458-023-09633-6 | 不是 LLM-only，而是补齐 multi-agent 通信的经典 MARL 视角；能为后续比较“LLM 通信 vs 学习式通信协议”提供必要背景。 |
| 4 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2024 | https://arxiv.org/abs/2412.17481 | arXiv | 明确聚焦“Recent Advances + Application Frontiers”，比通用框架综述更强调应用分类，适合后续做场景分工与下载优先级安排。 |
| 5 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | https://arxiv.org/abs/2501.06322 | arXiv | 将协作机制分为 actors、types、structures、strategies、protocols 等维度，适合抽取 multi-agent 协作设计空间。 |
| 6 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | https://arxiv.org/abs/2502.14321 | arXiv | 与 5 的“协作机制”互补，专门从 communication-centric 角度讨论 goals、protocols、strategies、objects、content，并显式讨论安全、benchmark、scalability。 |
| 7 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | 2025 | https://arxiv.org/abs/2502.16804 | arXiv | 代表高价值应用方向；把 LLM-based multi-agent 带入 autonomous driving，可帮助后续 idea 设计落到可验证场景。 |
| 8 | A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives | 2025 | https://arxiv.org/abs/2503.13415 | arXiv | 覆盖仿真环境、任务形式、奖励分配、规则/博弈/进化算法/MARL/LLM 推理等方法谱系，横跨传统 MAS 与新型 LLM-MAS。 |
| 9 | Creativity in LLM-based Multi-Agent Systems: A Survey | 2025 | https://arxiv.org/abs/2505.21116 | arXiv | 代表“创意生成”这一正在升温的新方向；覆盖 persona design、divergent exploration、iterative refinement、evaluation metrics，能为后续 idea 设计提供非传统任务面。 |
| 10 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | 2026 | https://arxiv.org/abs/2602.11583 | arXiv / TMLR accepted | 本轮可稳定核实的 2026 代表作；把 MARL、Emergent Language、LLM 三阶段通信研究串联到统一“五个 W”框架，覆盖面和解释力都很强。 |

## 覆盖结构说明
### 时间覆盖
- 2026：1 篇
- 2025：5 篇
- 2024：4 篇

说明：本轮检索中，2026 年可稳定核实且明确属于 multi-agent 综述的条目较少，因此以 2025 和 2024 的高质量综述补足，满足“优先覆盖 2024-2026”的要求，同时不放宽文献类型标准。

### 主题覆盖
- 通用 LLM-based multi-agent 框架综述：1, 2, 4
- 协作/通信机制：3, 5, 6, 10
- 决策与传统 MAS / MARL 连接：3, 8, 10
- 应用综述：7（自动驾驶）、9（创造力任务）
- 评测/挑战/开放问题：1, 4, 6, 8, 9, 10

## 后续下载与精读建议
### 第一优先级
1. `10` Five Ws of Multi-Agent Communication
2. `1` Springer workflow/infrastructure/challenges survey
3. `5` Collaboration Mechanisms
4. `6` Communication-Centric Survey

原因：这四篇最适合搭主线框架，能最快形成“系统结构—协作—通信—挑战”的中文综述骨架。

### 第二优先级
5. `8` Cooperative Decision-Making
6. `3` MARL with Communication
7. `2` Progress and Challenges
8. `4` Recent Advances and Application

原因：补齐传统 MAS、MARL 与 broader application landscape。

### 第三优先级
9. `7` Autonomous Driving
10. `9` Creativity in LLM-based MAS

原因：提供高价值应用与新兴方向样例，适合后续研究 idea 发散。

## 证据摘录（用于判定综述属性）
- `1` Springer 页面明确标注 `Review`，摘要写明 `we present a comprehensive survey`。
- `2` arXiv 标题含 `A Survey`，摘要写明 `we present this survey`。
- `3` DBLP 题名为 `A survey of ...`，期刊条目标注 2024 年正式发表。
- `4` arXiv 标题含 `A Survey`，摘要写明 `This paper presents a comprehensive survey`。
- `5` arXiv 标题含 `A Survey`，摘要写明 `This work provides an extensive survey`。
- `6` arXiv 标题含 `Survey`，摘要写明 `this paper presents a comprehensive survey`。
- `7` arXiv 标题含 `A Survey`，摘要写明 `This paper provides a frontier survey`。
- `8` arXiv 标题含 `A Comprehensive Survey`，摘要写明 `This paper begins with a comprehensive survey`。
- `9` arXiv 标题含 `A Survey`，摘要写明 `This is the first survey dedicated to creativity in MAS`。
- `10` arXiv 标题含 `A Survey`，摘要写明 `This survey reviews multi-agent communication ...`。

## 本轮局限
- OpenReview 对部分候选页返回 403，导致医学向综述仅能作为候选线索，未纳入最终清单。
- arXiv API 在连续高频检索下出现 429，因此候选池以“多次低频查询 + 页面核实”方式完成，而非一次性批量抓取。
- 本轮任务只做“检索与筛选”，尚未下载 PDF；下载动作应由后续任务继续执行。
