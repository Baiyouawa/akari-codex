# zero-basics-plan

Priority: high
Status: active
Mission: 小侑要创建“零基础计划”，需要并行调研 Linux、Git、GitHub、VibeCoding、Cursor、基础深度学习等资料，并整理成 28 天四周课程的 Markdown 教程。任务跨度大、资料量多，适合启动 Multi-Agent 系统并行完成。

## Log

### 2026-03-26

项目创建。

### 2026-03-26T19:19:37+08:00

- 完成 Git / GitHub 零基础资料调研，产出 `projects/zero-basics-plan/analysis/git-github-beginners-research.md`。
- 调研笔记覆盖版本控制概念、`git init`、commit、branch、merge、rebase、remote、Issue、PR、协作流程，并给出新手友好教程骨架与 5 组练习。
- 资料来源以官方文档为主：Git Book / Git Reference / GitHub Docs，并补充 `Learn Git Branching` 作为交互式练习来源。
- 验证：`wc -l projects/zero-basics-plan/analysis/git-github-beginners-research.md` 输出 `459`，确认文档已落盘且内容非空。

### 2026-03-26T19:22:16+08:00

- 完成 Linux 零基础入门资料调研，产出 `projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`。
- 调研笔记覆盖文件系统、常用命令、权限、软件安装、Shell 基础、实战练习，并按课程设计需要整理出主线教材组合、主题映射、4 周拆分建议与练习清单。
- 已筛出适合零基础的主资料：USTC OS Docs、Ubuntu Desktop documentation、LinuxCommand.org、菜鸟教程相关页面、MIT Missing Semester、OverTheWire Bandit。
- 验证：`wc -l projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md` 输出 `264`；`grep -n "## 推荐资料清单\|## 按任务要求映射资料\|## 可直接放入课程的练习建议" projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md` 命中第 32 / 134 / 198 行，确认关键章节存在。
