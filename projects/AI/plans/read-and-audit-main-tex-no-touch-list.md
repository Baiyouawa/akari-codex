# 审查 `projects/AI/main.tex` 并建立禁止改动清单

## Goal Description
读取并审查 `projects/AI/main.tex`，精确识别其中可改写的纯文字区域，并建立一份可执行的“禁止改动清单”。本任务不改写正文，只定义后续改写时的可动区与不可动区，确保表格、图题、图片引用、公式、标签、引用键、章节结构、环境命令全部保持不变。

## Acceptance Criteria
- AC-1: 形成一份基于 `projects/AI/main.tex` 当前内容的审查记录，明确列出可改写的纯文字区域，并给出可追溯到源码的行号证据。
  - Positive check: 审查文件中列出具体行号范围与对应内容类型。
  - Negative check: 不得仅用“正文大部分可改”这类模糊描述替代精确定位。
- AC-2: 建立“禁止改动清单”，覆盖表格、图题、图片引用、公式、标签、引用键、章节结构、环境命令等约束，并注明当前文件中哪些项存在、哪些项不存在。
  - Positive check: 清单同时区分“当前文件中已出现的不可改项”和“当前文件中未出现但若后续操作涉及仍禁止改动的项”。
  - Negative check: 不得遗漏用户明确指定的禁止项。
- AC-3: 审查结论不修改 `projects/AI/main.tex` 内容本身，仅新增 RLCR 记录文件、任务状态与会话日志。
  - Positive check: `main.tex` 保持未改动。
  - Negative check: 不得在本任务中直接重写正文。
- AC-4: 产出完整 RLCR 痕迹：计划、进度、自审、总结均写入 `projects/AI/plans/`。
  - Positive check: `projects/AI/plans/` 下存在本任务对应的 plan / progress / self-review / summary 文件。
  - Negative check: 不得只在聊天中口头说明完成。
- AC-5: 任务状态与会话记录持久化到仓库。
  - Positive check: `projects/AI/TASKS.md` 记录该专项检查结果，`logs/sessions/` 新增会话日志。
  - Negative check: 不得仅凭对话声明完成。

## Path Boundaries
### Upper Bound (most complete)
给出逐段、逐块的行号级审查：覆盖标题页、主体正文、图表前后说明、结论、附录反思，并单独列出所有不可改的 LaTeX 结构元素与命令类别。

### Lower Bound (minimum viable)
给出足以指导后续安全改写的可改写区域列表与禁止改动清单，并完成 RLCR 记录、任务状态和会话日志。

## Milestones
1. 读取现有任务、计划与 `main.tex`，确认本次任务边界。
2. 形成可改写纯文字区域清单与禁止改动清单。
3. 写入进度记录、自审报告、最终总结，并更新任务状态与会话日志。

## Plan Evolution Log
- 2026-03-27: 因 `projects/AI/plans/` 中不存在本专项任务计划文件，新建本计划文件并锁定 AC。