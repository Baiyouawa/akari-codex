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

### 2026-03-26T19:25:37+08:00

- 完成开发工具链零基础资料调研，产出 `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`。
- 调研范围覆盖 Cursor、VS Code、终端、包管理、Python 虚拟环境、基础调试、VibeCoding 入门实践，并给出适合零基础课程的教学顺序、资料清单、课程落地建议与常见误区。
- 来源以官方文档为主：Cursor Docs / Cursor Learn、VS Code Docs、Python Docs、Microsoft Learn、Homebrew、Ubuntu Tutorial、Ubuntu apt manpage；其中 Cursor 具体页面路径通过抓取 `https://cursor.com/docs` 后解析站点内 `filePath` 得到。
- 验证：`wc -l projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md` 输出 `373`；`grep -n "## 1. Cursor\|## 2. VS Code\|## 3. 终端与命令行\|## 4. 包管理\|## 5. 环境配置\|## 6. 基本调试方法\|## 7. VibeCoding 入门实践建议" projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md` 命中第 47 / 121 / 155 / 177 / 210 / 226 / 242 行，确认关键章节存在。

### 2026-03-26T19:29:10+08:00

- 验证并接收 28 天整体课程框架草案 `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md` 作为当前任务交付物。
- 课程总表已按 4 周共 28 天展开，覆盖每日学习目标、实操任务、配套资料与每周末系统复盘；主题顺序为 Linux / 终端 → Git / GitHub → Python / Cursor / VibeCoding → NumPy / PyTorch / 深度学习。
- 验证：`python3` 统计 `### Day ` 标题得到 `day_count 28`，且 `## Week 1`、`## Week 2`、`## Week 3`、`## Week 4`、`## Provenance` 全部存在；`wc -l` 输出 `306 projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`。
- 已同步更新 `projects/zero-basics-plan/TASKS.md`，将“设计整体课程框架”标记为完成，并把交付物路径写入 Done when。

## Open questions

1. 是否要为 Windows / macOS / Linux 分别做 3 套安装截图版教程？
2. 是否在 28 天课程中统一使用 VS Code，还是允许 Cursor 作为第 2 周升级路线？
3. 是否需要额外补充中文视频教程，以降低纯英文官方文档门槛？
