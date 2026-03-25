# 2026-03-26 候选综述 web_fetch 元信息核验

- Timestamp: 2026-03-26T02:35:19+08:00
- Session: 沙弥香-09-1774463682-927656
- Task: 对每个候选用 `web_fetch` 抓取摘要页、arXiv页、期刊页或 PDF 首页信息，核验其是否明确自称 survey/review、年份是否在 2024-2026、主题是否与 multi-agent 直接相关
- Scope: 针对项目内当前最常用的 12 篇候选短名单做逐篇 `web_fetch` 核验；来源统一为 arXiv 摘要页，避免混入无来源断言。

## 方法

1. 读取项目内已有候选池与短名单：
   - `projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`
   - `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates-shortlist.md`
   - `projects/multi-agent-review-survey/sources/2026-03-26-arxiv-multi-agent-survey-candidates.json`
2. 选择短名单中的 12 篇候选作为本轮核验对象。
3. 对每篇候选调用 `web_fetch https://arxiv.org/abs/<id>`，记录：
   - arXiv 提交年份是否落在 `2024-2026`
   - 标题或摘要是否明确出现 `survey` / `review` / `survey reviews` / `comprehensive survey` 等综述自定位
   - 摘要主题是否直接指向 multi-agent / multi-agent systems / LLM-based MAS / multi-agent communication / collaboration，或只是 agentic/LLM agents 邻近主题
4. 按三项核验结果给出结论：`核心相关` / `边界相关` / `不建议纳入核心 multi-agent 清单`。

## 逐篇核验结果

| arXiv ID | 年份 | 标题简写 | web_fetch 综述证据 | 年份是否在 2024-2026 | 与 multi-agent 直接相关性 | 结论 |
|---|---:|---|---|---|---|---|
| 2602.11583 | 2026 | Five Ws of Multi-Agent Communication | 标题含 `A Survey`；摘要含 `This survey reviews multi-agent communication` | 是 | 直接面向 multi-agent communication | 核心相关 |
| 2601.15047 | 2026 | Game-Theoretic Lens on LLM-based Multi-Agent Systems | 摘要含 `we present a comprehensive survey of LLM-based multi-agent systems` | 是 | 直接面向 LLM-based MAS | 核心相关 |
| 2601.12560 | 2026 | Agentic AI: Architectures, Taxonomies, and Evaluation | 摘要含 `we review current evaluation practices`，并覆盖 `hierarchical multi agent systems` | 是 | 与 multi-agent 明显相关，但主题更广，偏 agentic AI 总论 | 边界相关 |
| 2603.22862 | 2026 | Evolution of Tool Use in LLM Agents | 摘要含 `We comprehensively review recent progress` | 是 | 重点是 LLM agents / multi-tool orchestration，不以 multi-agent 为中心 | 边界相关 |
| 2603.22386 | 2026 | Survey of Workflow Optimization for LLM Agents | 标题含 `A Survey`；摘要含 `This survey reviews recent methods` | 是 | 聚焦 workflow / agentic computation graphs，不限 multi-agent | 边界相关 |
| 2601.10122 | 2026 | Role-Playing Agents Driven by LLMs | 摘要含 `This paper systematically reviews` | 是 | 主要是 role-playing agents；含 `multi-agent collaborative narrative` 未来方向，但非 multi-agent 主轴 | 边界相关 |
| 2504.01963 | 2025 | LLMs Working in Harmony | 标题含 `A Survey`；摘要首句含 `This survey investigates foundational technologies ... LLM-based multi-agent systems` | 是 | 直接面向 LLM-based multi-agent systems | 核心相关 |
| 2502.14321 | 2025 | Beyond Self-Talk | 标题含 `Survey`；摘要含 `this paper presents a comprehensive survey of LLM-MAS` | 是 | 直接面向 communication-centric LLM-MAS | 核心相关 |
| 2501.06322 | 2025 | Multi-Agent Collaboration Mechanisms | 标题含 `A Survey`；摘要含 `This work provides an extensive survey` | 是 | 直接面向 LLM-based MAS collaboration | 核心相关 |
| 2412.17481 | 2024 | Survey on LLM-based Multi-Agent System | 标题含 `A Survey`；摘要含 `This paper presents a comprehensive survey of these studies` | 是 | 直接面向 LLM-MAS | 核心相关 |
| 2402.01680 | 2024 | LLM based Multi-Agents: Survey of Progress and Challenges | 标题含 `A Survey`；摘要含 `we present this survey` | 是 | 直接面向 LLM-based multi-agent systems | 核心相关 |
| 2502.16804 | 2025 | Multi-Agent Autonomous Driving Systems with LLMs | 标题含 `A Survey`；摘要含 `This paper provides a frontier survey` | 是 | 与 multi-agent 直接相关，但属于自动驾驶垂直领域 | 边界相关 |

## 逐篇证据摘录

### 1. `2602.11583` — The Five Ws of Multi-Agent Communication
- URL: https://arxiv.org/abs/2602.11583
- `web_fetch` 结果显示：`[Submitted on 12 Feb 2026]`
- 标题证据：`... A Survey from MARL to Emergent Language and LLMs`
- 摘要证据：`This survey reviews multi-agent communication (MA-Comm) through the Five Ws ...`
- 相关性判断：摘要主语就是 `multi-agent communication`，且覆盖 `MARL`、`LLM-based systems`、`multi-agent collaboration`。
- 结论：**核心相关**。

### 2. `2601.15047` — Game-Theoretic Lens on LLM-based Multi-Agent Systems
- URL: https://arxiv.org/abs/2601.15047
- `web_fetch` 结果显示：`[Submitted on 21 Jan 2026]`
- 摘要证据：`we present a comprehensive survey of LLM-based multi-agent systems through a game-theoretic lens`
- 相关性判断：标题与摘要都直接出现 `LLM-based Multi-Agent Systems`。
- 结论：**核心相关**。

### 3. `2601.12560` — Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents
- URL: https://arxiv.org/abs/2601.12560
- `web_fetch` 结果显示：`[Submitted on 18 Jan 2026]`
- 摘要证据：`we review current evaluation practices`
- 主题证据：摘要含 `from simple single loop agents to hierarchical multi agent systems`
- 相关性判断：属于综述/综述近邻，但中心是 agentic AI / LLM agents 总览，而非纯 multi-agent 主线。
- 结论：**边界相关**。

### 4. `2603.22862` — The Evolution of Tool Use in LLM Agents
- URL: https://arxiv.org/abs/2603.22862
- `web_fetch` 结果显示：`[Submitted on 24 Mar 2026]`
- 摘要证据：`We comprehensively review recent progress in multi-tool LLM agents`
- 相关性判断：是综述，但对象是 tool use / multi-tool orchestration；不等于 multi-agent systems。
- 结论：**边界相关**。

### 5. `2603.22386` — From Static Templates to Dynamic Runtime Graphs
- URL: https://arxiv.org/abs/2603.22386
- `web_fetch` 结果显示：`[Submitted on 23 Mar 2026]`
- 标题证据：`A Survey of Workflow Optimization for LLM Agents`
- 摘要证据：`This survey reviews recent methods for designing and optimizing such workflows`
- 相关性判断：主题是 workflow optimization / ACGs；可支撑多代理编排，但非 multi-agent 专题本体。
- 结论：**边界相关**。

### 6. `2601.10122` — Role-Playing Agents Driven by Large Language Models
- URL: https://arxiv.org/abs/2601.10122
- `web_fetch` 结果显示：`[Submitted on 15 Jan 2026]`
- 摘要证据：`This paper systematically reviews the current development and key technologies of RPLAs`
- 相关性判断：属综述，但主要对象是 role-playing agents；摘要只在未来方向里提到 `multi-agent collaborative narrative`。
- 结论：**边界相关**。

### 7. `2504.01963` — LLMs Working in Harmony
- URL: https://arxiv.org/abs/2504.01963
- `web_fetch` 结果显示：`[Submitted on 13 Mar 2025]`
- 标题证据：`A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems`
- 摘要证据：`This survey investigates foundational technologies essential for developing effective ... multi-agent systems`
- 相关性判断：直接面向 LLM-based multi-agent systems。
- 结论：**核心相关**。

### 8. `2502.14321` — Beyond Self-Talk
- URL: https://arxiv.org/abs/2502.14321
- `web_fetch` 结果显示：`[Submitted on 20 Feb 2025]`
- 标题证据：`A Communication-Centric Survey of LLM-Based Multi-Agent Systems`
- 摘要证据：`this paper presents a comprehensive survey of LLM-MAS from a communication-centric perspective`
- 相关性判断：直接面向 LLM-MAS 通信机制。
- 结论：**核心相关**。

### 9. `2501.06322` — Multi-Agent Collaboration Mechanisms: A Survey of LLMs
- URL: https://arxiv.org/abs/2501.06322
- `web_fetch` 结果显示：`[Submitted on 10 Jan 2025]`
- 标题证据：`A Survey of LLMs`
- 摘要证据：`This work provides an extensive survey of the collaborative aspect of MASs`
- 相关性判断：直接讨论 collaboration mechanisms 与 LLM-based MASs。
- 结论：**核心相关**。

### 10. `2412.17481` — A Survey on LLM-based Multi-Agent System
- URL: https://arxiv.org/abs/2412.17481
- `web_fetch` 结果显示：`[Submitted on 23 Dec 2024]`
- 标题证据：`A Survey on LLM-based Multi-Agent System`
- 摘要证据：`This paper presents a comprehensive survey of these studies`
- 相关性判断：直接面向 LLM-MAS 的总览型综述。
- 结论：**核心相关**。

### 11. `2402.01680` — Large Language Model based Multi-Agents
- URL: https://arxiv.org/abs/2402.01680
- `web_fetch` 结果显示：`[Submitted on 21 Jan 2024]`
- 标题证据：`A Survey of Progress and Challenges`
- 摘要证据：`we present this survey to offer an in-depth discussion on the essential aspects of multi-agent systems based on LLMs`
- 相关性判断：直接面向 LLM-based multi-agent systems，是 2024 基线综述。
- 结论：**核心相关**。

### 12. `2502.16804` — Multi-Agent Autonomous Driving Systems with Large Language Models
- URL: https://arxiv.org/abs/2502.16804
- `web_fetch` 结果显示：`[Submitted on 24 Feb 2025]`
- 标题证据：`A Survey of Recent Advances`
- 摘要证据：`This paper provides a frontier survey of this emerging intersection between NLP and multi-agent ADSs`
- 相关性判断：确实是 multi-agent survey，但更偏自动驾驶垂直领域，而非通用 multi-agent 主线。
- 结论：**边界相关**。

## 汇总判断

### A. 可直接作为“multi-agent 核心综述”保留的候选（7 篇）
1. `2602.11583`
2. `2601.15047`
3. `2504.01963`
4. `2502.14321`
5. `2501.06322`
6. `2412.17481`
7. `2402.01680`

这些条目都同时满足：
- `web_fetch` 可见年份在 `2024-2026`；
- 标题或摘要明确自称 `survey` / `comprehensive survey` / `this survey`；
- 标题或摘要直接出现 `multi-agent` / `multi-agent systems` / `LLM-MAS` / `multi-agent communication` / `collaboration mechanisms`。

### B. 综述身份成立，但更适合作为边界或补位候选（5 篇）
1. `2601.12560` — agentic AI 总论，含 multi-agent 但外延更广
2. `2603.22862` — tool-use / orchestration 综述，不以 multi-agent 为中心
3. `2603.22386` — workflow optimization 综述，不限 multi-agent
4. `2601.10122` — role-playing agents 综述，multi-agent 只属邻近主题
5. `2502.16804` — multi-agent 自动驾驶综述，属垂直应用领域

## 本轮发现

1. 本轮核验的 12 篇候选里，`12/12` 都满足“年份在 2024-2026”这一条件。
   - Provenance: 各 arXiv `Submitted on ...` 字段；内联算术 `12 = 12`。
2. 本轮核验的 12 篇候选里，`12/12` 都有明确综述信号，但只有 `7/12` 可视为通用 multi-agent 核心综述，另外 `5/12` 更适合作为边界补位文献。
   - Provenance: 上表“结论”列；内联算术 `7 + 5 = 12`。
3. 当前最稳的核心主线包括 communication、collaboration、general LLM-MAS overview 三类；workflow、tool-use、role-playing、agentic-AI 总论更像外围支撑层。
   - Provenance: `2602.11583`, `2502.14321`, `2501.06322`, `2412.17481`, `2402.01680`, `2504.01963`, `2601.15047` 的标题与摘要字段。

## 建议

- 若下一轮要输出“最终入选 10 篇与剔除名单”，可直接以本文件的 `7` 篇核心相关候选作为骨架，再从边界相关池中按任务口径选择是否纳入 `2601.12560`、`2603.22386`、`2603.22862` 等 agentic 邻近综述。
- 若口径严格限定为“multi-agent 本体综述”，则应优先剔除 `2603.22862`、`2603.22386`、`2601.10122`，并谨慎对待 `2601.12560`。

## Provenance

- `web_fetch https://arxiv.org/abs/2602.11583`
- `web_fetch https://arxiv.org/abs/2601.15047`
- `web_fetch https://arxiv.org/abs/2601.12560`
- `web_fetch https://arxiv.org/abs/2603.22862`
- `web_fetch https://arxiv.org/abs/2603.22386`
- `web_fetch https://arxiv.org/abs/2601.10122`
- `web_fetch https://arxiv.org/abs/2504.01963`
- `web_fetch https://arxiv.org/abs/2502.14321`
- `web_fetch https://arxiv.org/abs/2501.06322`
- `web_fetch https://arxiv.org/abs/2412.17481`
- `web_fetch https://arxiv.org/abs/2402.01680`
- `web_fetch https://arxiv.org/abs/2502.16804`
- `projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates-shortlist.md`
- `projects/multi-agent-review-survey/sources/2026-03-26-arxiv-multi-agent-survey-candidates.json`
