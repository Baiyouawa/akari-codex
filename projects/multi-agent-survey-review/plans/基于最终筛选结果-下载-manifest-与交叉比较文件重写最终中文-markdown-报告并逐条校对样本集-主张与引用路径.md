# 基于最终筛选结果、下载 manifest 与交叉比较文件重写最终中文 Markdown 报告，并逐条校对样本集、主张与引用路径

## Goal Description
重写 `projects/multi-agent-survey-review/analysis/2026-03-26-final-chinese-multi-agent-survey-report.md`，使其只覆盖 `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md` 与 `projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json` 锁定的 10 篇综述，并与 `projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-cross-comparison.md`、`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-background-problem-framework-notes.md` 保持主张与引用路径一致。

## Acceptance Criteria
- AC-1: 开工前完成样本基线核对，并在报告头部显式声明样本集来源。
  - 正向验证：报告开头明确写出唯一可信样本基线为 selection + manifest，并列出交叉比较与背景笔记为分析输入。
  - 负向验证：不得把旧版最终报告或旧污染详读笔记当作样本真值来源。
- AC-2: 新报告只覆盖 manifest 锁定的 10 篇综述，标题、年份、来源链接、本地路径与主样本清单一致。
  - 正向验证：报告逐篇详述只出现 paper_id `10.1007/s44336-024-00009-2`、`2402.01680`、`10.1007/s10458-023-09633-6`、`2412.17481`、`2501.06322`、`2502.14321`、`2502.16804`、`2503.13415`、`2505.21116`、`2602.11583`。
  - 负向验证：不得出现 Aratchige 2025、Zeng 2025、Xu 2026、Yue 2026、Wang 2026 等非锁定样本。
- AC-3: 报告中的逐篇主张、跨篇比较与研究 idea 均可追溯到仓库内证据文件。
  - 正向验证：每个小节明确引用 selection、manifest、cross-comparison、background-notes 或统一样本详读笔记中的至少一种来源路径。
  - 负向验证：不得出现无法回链到仓库内文件的“悬空结论”。
- AC-4: 报告保留完整交付结构：样本声明、十篇逐篇详述、跨综述对比分析、5 个后续研究 idea、结论与参考路径。
  - 正向验证：主报告完整覆盖上述五部分，且五个 idea 逐项包含 motivation、问题定义、方法设计、预期贡献、潜在风险。
  - 负向验证：不得只修头部样本声明而保留错误正文，或删减掉五个 idea 以逃避修复。
- AC-5: 完成 RLCR 过程文件与项目状态闭环。
  - 正向验证：新增本任务对应 progress/self-review/summary 文件，更新 `projects/multi-agent-survey-review/TASKS.md`、`projects/multi-agent-survey-review/README.md`，新增 session log，并保证自审无 P0/P1。
  - 负向验证：不得只改主报告而不更新任务状态、日志与过程文件。

## Path Boundaries
### Upper Bound
在不新增样本的前提下，全面重写最终报告正文，逐条校对样本列表、逐篇章节、对比结论、idea 论据和引用路径，并同步完成 RLCR 闭环、README/TASKS/session log/git commit。

### Lower Bound
基于 selection、manifest、cross-comparison、background-notes 和统一样本详读笔记，修复最终报告的样本漂移与证据链问题，确保报告头部声明、10 篇样本、正文主张和项目状态闭环全部正确。

## Milestones
1. 核对 selection、manifest、cross-comparison、background-notes 与当前最终报告，锁定应保留的 10 篇样本与可复用论据。
2. 重写最终中文 Markdown 报告，修正样本集、逐篇详述、横向比较与 5 个 research ideas 的证据路径。
3. 写 progress 与 self-review，修复 P0/P1 问题。
4. 更新 README、TASKS、session log、summary，并完成 git commit。

## Plan Evolution Log
- 2026-03-26T23:48:50+08:00: 初始计划创建；预计不需要联网检索，仓库内已有 selection、manifest、cross-comparison、background-notes 与统一样本详读笔记足以支撑重写。