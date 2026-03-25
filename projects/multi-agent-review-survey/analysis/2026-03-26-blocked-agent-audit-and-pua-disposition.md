# 2026-03-26 blocked agent audit and PUA disposition

- Session: 文乃-04-1774462781-971acb
- Timestamp: 2026-03-26T02:20:47+08:00
- Task: 审查已报 blocked 的 Agent 是否先穷尽 `web_search` / `web_fetch` / 本地文件核验等手段；未穷尽者按伪阻塞处理并要求切换方案

## 审查范围

本次优先审查 `projects/multi-agent-review-survey/` 中 2026-03-25 晚间第一批与 2026-03-26 已完成补救之间形成对照的 blocked 记录，重点覆盖：

1. 早期仅依赖 repo-local 检查就报 blocked 的会话；
2. 后续已用 `web_search` / `web_fetch` / arXiv API / `curl` 下载完成同类任务的会话；
3. 已使用多种外部与本地核验手段后形成的收口会话。

## 审查标准

按任务中给定 PUA 标准，本次用以下规则判定：

- **伪阻塞**：报 blocked 前未见 `web_search`、`web_fetch`、联网来源核验、或本地文件核验的充分尝试；且后续已有其他 Agent 用这些方法完成同类任务。
- **真实阻塞（历史时点）**：已使用多种本质不同的方法，或阻塞发生在上游事实尚未落盘、但后续并无反证表明其存在主观偷懒。
- **已被后续会话解除**：虽然当时报 blocked，但后续已有联网检索、下载、核验和精读闭环工件，因此该 blocker 不应再作为现行状态继续沿用。

## 逐项审查结论

| Agent / Session | 原 blocked 任务 | 当时报告中已尝试的方法 | 审查结论 | 依据 |
|---|---|---|---|---|
| 日向-03-1774451763-82a7be | 第 1 篇综述详读 | 读 README/TASKS；列目录；项目内和仓库内 `search_text` | **伪阻塞，打回重做** | 仅做 repo-local 搜索即停止；后续已有 `web_search` / `web_fetch` / 下载 / 精读闭环，证明“仓库初始为空”不是 blocker。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:17:04+08:00-fleet-日向-03-1774451763-82a7be-first-survey-reading-blocked.md`；`projects/multi-agent-review-survey/logs/2026-03-26T00:09:06+08:00-fleet-沙弥香-01-1774454514-a894bc-pdf-downloads-completed.md`；`projects/multi-agent-review-survey/logs/2026-03-26T00:16:17+08:00-fleet-结衣-03-1774454544-65f537-ten-survey-deep-reading.md` |
| 文乃-04-1774451763-e37b1e | 第 2 篇综述详读 | 读 README/TASKS；列目录；项目内 `search_text` | **伪阻塞，打回重做** | 与上同，只做本地盘点，没有切换到 web 路径。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:17:05+08:00-fleet-文乃-04-1774451763-e37b1e-second-survey-reading-blocked.md`；后续完成链同上。 |
| 沙弥香-01-1774452423-4754bc | 最新 5 篇综述检索 | 读项目文件；`list_files`；`search_text`；重读 blocker assessment | **伪阻塞，打回重做** | 任务文本明确允许外部检索，但该会话未使用 `web_search` / `web_fetch`；后续千早-05 与沙弥香-01 已用联网手段完成候选池与下载。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:27:42+08:00-fleet-沙弥香-01-1774452423-4754bc-latest-five-surveys-blocked.md`；`projects/multi-agent-review-survey/logs/2026-03-26T01:24:26+08:00-fleet-千早-05-1774459025-ee93cb-web-search-15-survey-candidates.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md` |
| 柑奈-02-1774452423-dad5ad | 下载确认后的 5 篇综述 | 读已有 blocker；仓库搜索；更新 TASKS | **伪阻塞，打回重做** | 未先自己补齐候选与来源页，也未尝试 `web_search` / `web_fetch` / `curl` 下载；后续同类任务已被联网检索 + 下载完成。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:27:50+08:00-fleet-柑奈-02-1774452423-dad5ad-download-confirmed-five-surveys-blocked.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md` |
| 结衣-03-1774452423-785487 | 逐篇精读 5 篇综述 | 读 README/TASKS；列目录；复读 blocker 文件 | **伪阻塞，打回重做** | 精读会话本身未尝试先联网补齐可读材料，也未基于后续可获取 PDF 转入阅读；后续该类工作已完成。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:29:31+08:00-fleet-结衣-03-1774452423-785487-five-survey-deep-reading-blocked.md`；`projects/multi-agent-review-survey/logs/2026-03-26T00:16:17+08:00-fleet-结衣-03-1774454544-65f537-ten-survey-deep-reading.md` |
| 日向-03-1774452723-ecc7b8 | 新增 5 篇来源核验与下载 | 读项目文件；列目录；检查是否已有确认清单 | **伪阻塞，打回重做** | 没有使用 web 路线主动核验来源。后续已有 `web_search` / `web_fetch` / 来源页与 PDF 直链确认工件。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:33:25+08:00-fleet-日向-03-1774452723-ecc7b8-review-source-verification-blocked.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md` |
| 沙弥香-01-1774453054-cdbef9 | 最新 10 篇综述检索 | 读项目文件；重读 blocker；列目录 | **伪阻塞，打回重做** | 仍然是 repo-only 检查；后续同主题检索任务已通过 `web_search` / `web_fetch` / arXiv API 完成。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:38:17+08:00-fleet-沙弥香-01-1774453054-cdbef9-ten-survey-search-blocked.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md` |
| 智乃-02-1774453535-5ccc8a | 为入选综述确认主页与 PDF 直链 | 读项目文件；列目录；`search_text` | **伪阻塞，打回重做** | 未执行外部抓取；后续绫-07、沙弥香-01 等已完成主页/PDF 直链确认。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:46:59+08:00-fleet-智乃-02-1774453535-5ccc8a-survey-homepage-pdf-links-blocked.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-top10-survey-selection-closeout.md` |
| 日向-03-1774453535-a492b2 | 下载 10 篇 PDF 到 literature | 读 blocker；本地 `find` / `list_files` | **伪阻塞，打回重做** | 仅证明目录为空，没有切换到联网下载；后续同任务已由 `curl` 下载完成。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:46:25+08:00-fleet-日向-03-1774453535-a492b2-literature-download-blocked.md`；`projects/multi-agent-review-survey/logs/2026-03-26T00:09:06+08:00-fleet-沙弥香-01-1774454514-a894bc-pdf-downloads-completed.md` |
| 灯里-00-1774453535-02b046 | 核验 literature 中 10 个 PDF | 本地 `find` / `wc -l` | **非伪阻塞，属阶段性真实阻塞** | 该任务前提是“目标文件已落盘”；在当时目录内确实 `pdf_count = 0`，且这是一项依赖上游下载结果的下游核验任务。其阻塞点虽随后被解除，但不属于“不用工具就报 blocked”。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:46:22+08:00-fleet-灯里-00-1774453535-02b046-literature-pdf-verification-blocked.md`；后续解阻证据：`projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-verification.md` |
| 沙弥香-01-1774453535-252bca | 2024-2026 最新 10 篇综述筛选 | 读 blocker；列目录；写 blocker assessment | **伪阻塞，打回重做** | 和同 Agent 先前 blocked 一样，未先走外部检索；而同一主题后来就是该组通过联网完成。证据：`projects/multi-agent-review-survey/logs/2026-03-25T23:46:27+08:00-fleet-沙弥香-01-1774453535-252bca-2024-2026-ten-survey-selection-blocked.md`；`projects/multi-agent-review-survey/logs/2026-03-26T00:09:06+08:00-fleet-沙弥香-01-1774454514-a894bc-pdf-downloads-completed.md`；`projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md` |

## 归纳判断

### 1. 哪些 blocked 属于伪阻塞

上述审查中，以下会话应按 **PUA 标准打回重做**：

- 日向-03-1774451763-82a7be
- 文乃-04-1774451763-e37b1e
- 沙弥香-01-1774452423-4754bc
- 柑奈-02-1774452423-dad5ad
- 结衣-03-1774452423-785487
- 日向-03-1774452723-ecc7b8
- 沙弥香-01-1774453054-cdbef9
- 智乃-02-1774453535-5ccc8a
- 日向-03-1774453535-a492b2
- 沙弥香-01-1774453535-252bca

共同问题：

1. 主要只做了 repo-local 检查；
2. 没有先切换到 `web_search` / `web_fetch` / arXiv API / `curl` 下载等本质不同的方法；
3. 其后续同类任务已被其他 Agent 用外部检索和本地核验成功完成，形成反证。

### 2. 哪些 blocked 不应算伪阻塞

- 灯里-00-1774453535-02b046 的 “literature PDF verification blocked” 属于 **依赖上游产物缺失** 的阶段性真实阻塞：它已经完成了本地计数与目录核验，且该任务性质就是对既有文件做验证；在上游下载未完成前，确实无对象可验。

### 3. 后续成功会话证明了什么

后续会话已经证明该项目并非“repo 为空所以只能 blocked”，而是可以通过如下路径解阻：

1. `web_search` / `web_fetch` 形成候选池与网页证据；
2. arXiv API / Springer 来源页补齐题录与 PDF 直链；
3. `curl -L --fail` 下载 PDF 到本地；
4. `python3` + `pypdf.PdfReader` 做文件可读性、页数、首页标题校验；
5. 在此基础上完成结构化精读、中文主报告和 10 个 ideas。

对应完成证据：

- `projects/multi-agent-review-survey/analysis/2026-03-26-web-search-15-survey-candidates-refresh.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-verification.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-detailed-ideas.md`

## PUA disposition / 打回建议

对被判定为伪阻塞的历史会话，统一建议如下：

> 结论：伪阻塞。未穷尽方法即停止，未满足“先做后问”“至少切换到 3 种本质不同方法”的要求。应打回重做。  
> 重做要求：
> 1. 先用 `web_search` 检索候选；
> 2. 再用 `web_fetch` 或 arXiv / 出版社页面核验 survey 身份与年份；
> 3. 必要时用 `curl` / `wget` 下载 PDF；
> 4. 用本地 `python3` / `pypdf` 核验文件与标题；
> 5. 只有三类路径都尝试后仍失败，才允许再次报 blocked。

## 结论

本次审查表明：`projects/multi-agent-review-survey/` 在 2026-03-25 晚间出现的大多数 blocked 记录，按当前任务标准应视为 **伪阻塞**，因为它们主要停留在“仓库内没有”这一层，没有继续使用已明确允许的外部检索与抓取工具。后续 2026-03-26 的成功会话已经形成完整反证链，说明这些任务多数都可以通过切换方案完成，而不是必须阻塞。
