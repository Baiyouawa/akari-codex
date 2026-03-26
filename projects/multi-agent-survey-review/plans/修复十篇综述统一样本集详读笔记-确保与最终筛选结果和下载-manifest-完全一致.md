# 修复十篇综述统一样本集详读笔记-确保与最终筛选结果和下载 manifest 完全一致

## Goal Description
修复 `projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-detailed-reading-notes.md`，使其只覆盖 `projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json` 锁定的 10 篇综述，并与 `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`、`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-cross-comparison.md` 的样本口径保持一致。

## Acceptance Criteria
- AC-1: 计划执行前完成样本基线核对。
  - 正向验证：计划文件中明确列出唯一可信样本基线文件为 selection + manifest，并确认共有 10 篇论文。
  - 负向验证：不得以旧版 `2026-03-26-ten-survey-detailed-reading-notes.md` 作为样本真值来源。
- AC-2: 主详读笔记文件只包含 manifest 中 10 篇论文，且标题/年份/来源与 manifest 对齐。
  - 正向验证：详读笔记逐篇覆盖 10.1007/s44336-024-00009-2、2402.01680、10.1007/s10458-023-09633-6、2412.17481、2501.06322、2502.14321、2502.16804、2503.13415、2505.21116、2602.11583。
  - 负向验证：不得出现 Aratchige 2025、Zeng 2025、Xu 2026、Yue 2026、Wang 2026 等非锁定样本。
- AC-3: 每篇详读笔记保留统一结构，至少包含研究问题、分类框架、核心观点、方法谱系、评测设定、局限性、值得精读章节、关键图表、证据来源/边界。
  - 正向验证：10 篇均具备统一小节结构。
  - 负向验证：不得只给列表名录或缺少证据边界说明。
- AC-4: 修复过程需留下 RLCR 过程文件。
  - 正向验证：在 `plans/` 下新增本任务的 progress、自审、summary 文件，自审无 P0/P1。
  - 负向验证：不得只改主文件而缺少过程记录。
- AC-5: 项目状态需闭环更新。
  - 正向验证：更新 `projects/multi-agent-survey-review/TASKS.md` 对应任务状态，更新项目 README 日志，新增本次 session log。
  - 负向验证：不得完成内容后不更新任务状态与日志。

## Path Boundaries
### Upper Bound
基于 selection、manifest、cross-comparison、background-notes 与本地 PDF 元数据，重写整份详读笔记，逐篇校正样本、结构与证据边界，并完成 RLCR 闭环、README/TASKS/log/commit 全链路更新。

### Lower Bound
在不新增外部检索的前提下，使用仓库内已有可信文件重写主详读笔记，确保样本集完全正确、非锁定样本完全移除，并补齐最基本的 RLCR 记录与项目状态更新。

## Milestones
1. 核对 selection 与 manifest，锁定 10 篇论文清单与文件路径。
2. 重写统一样本集详读笔记，仅保留 10 篇锁定样本。
3. 编写 progress 与 self-review，修复 P0/P1 问题。
4. 更新 README、TASKS、session log、summary，并提交 git commit。

## Plan Evolution Log
- 2026-03-26T23:44:51+08:00: 初始计划创建；当前判断仓库内已有足够证据，无需额外联网检索。