# AI Project Tasks

## Completed

- [x] 按章节并行改写正文文字，使表达更像真人学术写作：保留原意、术语、逻辑与 LaTeX 结构，仅替换措辞、句法、连接方式、段落节奏与论述展开方式 [zero-resource] [skill: record]
  Completed: 2026-03-27T00:14:18+08:00
  Evidence: `projects/AI/main.tex` 完成学术化改写；`projects/AI/plans/rewrite-main-text-human-academic-style.md`、`projects/AI/plans/rewrite-main-text-human-academic-style-progress.md`、`projects/AI/plans/rewrite-main-text-human-academic-style-self-review.md`、`projects/AI/plans/rewrite-main-text-human-academic-style-summary.md` 记录了计划、进度、自审与交付。
  Why: 使现有课程报告文本更自然、更接近人工学术写作，同时保持 UML 建模内容与文档结构稳定。

- [x] 对每个 Agent 的产出执行 PUA + Humanize 复核：若有人只做表面同义替换或未充分改写，就要求切换方案重做；必须给出证据链和修改说明 [zero-resource] [skill: govern]
  Completed: 2026-03-27T00:13:43+08:00
  Evidence: `projects/AI/plans/review-agent-outputs-pua-humanize.md`、`projects/AI/plans/review-agent-outputs-pua-humanize-findings.md`、`projects/AI/plans/review-agent-outputs-pua-humanize-self-review.md`、`projects/AI/plans/review-agent-outputs-pua-humanize-summary.md` 与 `projects/AI/logs/2026-03-27T00:13:43+08:00-agent-output-pua-humanize-review.md` 给出了逐 worker 的证据链、通过/失败判定与重做方向。
  Why: AI 改写任务已有多 Agent 产出，必须在继续验收前确认每份产出是否达到实质改写与可追溯复核标准。
