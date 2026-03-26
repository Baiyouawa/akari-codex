# 第 2 周资料调研进度摘要

## 2026-03-26T21:41:00+08:00

### 已完成内容
- 完成任务计划文件阅读，并按既有验收标准执行。
- 完成项目上下文读取：`AGENTS.md`、`projects/zero-basics-plan/README.md`、`projects/zero-basics-plan/TASKS.md`。
- 抓取并筛选多平台资料，覆盖：
  - 官方/准官方：GNU Bash Manual、GNU Coreutils、man7、Debian Handbook、Git 官方文档、GitHub Docs
  - 教程平台：DigitalOcean、Atlassian
  - 中文教程：廖雪峰
  - 互动练习：Learn Git Branching、Oh My Git!
- 产出主交付文件：`projects/zero-basics-plan/analysis/2026-03-26-week2-linux-ssh-git-resource-survey.md`

### 当前里程碑状态
- 已完成：范围确认与记录规范统一
- 已完成：资料源清单与优先级建立
- 已完成：五大主题资料搜集与初筛
- 已完成：教学映射与章节骨架整理
- 待完成：自审报告
- 待完成：最终摘要、项目日志、任务状态更新

### 关键发现
- Git 主教材最适合采用 `Pro Git 中文版`，同时用 `git-commit` 官方手册核对具体命令行为。
- 文件权限与进程管理模块应优先依赖 GNU / man7 手册，避免把社区博客中的简化说法直接写进正式教程。
- SSH 模块必须强调 host key 校验与 agent forwarding 风险，不应传播“为方便直接关闭校验”的示例。
- 第 2 周的 Git 冲突内容建议控制在 `merge conflict`，`rebase conflict` 可作为扩展阅读。

### 证据来源
- 见主调研文件中的逐条链接与版本/更新说明。
