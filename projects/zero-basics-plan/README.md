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

- 完成 Python 与编程基础资料调研，产出 `projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`。
- 调研笔记覆盖语法、数据结构、函数、模块、文件读写、虚拟环境，并补充课程映射、练习设计、初学者误区与最小资料包建议。
- 来源组合采用“官方骨架 + 零基础补充 + 练习支撑”：Python 官方教程、PY4E、Google's Python Class Basic Exercises、CS50P；并结合项目内既有 `dev-toolchain-beginner-research.md` 与 `2026-03-26-28-day-course-framework.md` 做 Week 3 对齐。
- 关键发现：Python 官方教程覆盖完整但默认读者并非“完全无编程背景”；因此课程正文需要以官方教程为骨架，同时用 PY4E 降低入门门槛。
- 验证：`wc -l projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md` 输出文档行数；`grep -n "## 推荐资料清单\|## 按任务要求映射资料\|## 适合直接纳入课程的练习建议\|## 最小资料包建议\|## Provenance" projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md` 用于确认关键章节存在。

### 2026-03-26T19:34:13+08:00

- 完成实践项目案例调研，产出 `projects/zero-basics-plan/analysis/2026-03-26-practice-project-cases.md`。
- 调研将 28 天课程映射为 20 个由浅入深的练习 / 小项目，覆盖 Week 1 命令行与 Shell、Week 2 Git / GitHub 协作、Week 3 Python / Cursor / VibeCoding、Week 4 NumPy / PyTorch / 最小分类 demo，并给出每日练习映射表、验收物与教学落地建议。
- 关键外部来源以官方或准官方材料为主：OverTheWire Bandit、Learn Git Branching、GitHub Skills、Cursor Learn / Rules、NumPy Absolute Beginners、PyTorch Quickstart / Training a Classifier；并与项目内既有课程框架、Linux / Git / Python / 工具链调研交叉对齐。
- 验证：`wc -l projects/zero-basics-plan/analysis/2026-03-26-practice-project-cases.md` 输出 `437`；`grep -n "## Week 1：命令行与 Linux 练习案例\|## Week 2：Git / GitHub 协作练习案例\|## Week 3：Python / Cursor / VibeCoding 练习案例\|## Week 4：NumPy / PyTorch / 深度学习 demo 案例\|## 推荐的 28 天练习映射\|## Provenance" projects/zero-basics-plan/analysis/2026-03-26-practice-project-cases.md` 命中第 44 / 114 / 187 / 260 / 331 / 410 行，确认关键章节存在。

### 2026-03-26T19:38:03+08:00

- 完成基础深度学习入门资料调研，产出 `projects/zero-basics-plan/analysis/2026-03-26-deep-learning-beginner-resource-survey.md`。
- 调研笔记覆盖 Python 科学计算、NumPy、PyTorch 基础、张量、自动求导、简单神经网络、训练与推理概念，并与既有 `2026-03-26-python-programming-basics-research.md` 及 `2026-03-26-28-day-course-framework.md` 对齐 Week 4 的课程顺序。
- 关键发现：零基础主线应采用“Python 基础 → NumPy 数组 → PyTorch 张量 → autograd → `nn.Module` → 训练 / 推理”的渐进顺序；Week 4 默认采用 CPU 安装路径即可，不应把 GPU / CUDA 作为前置门槛。
- 关键来源以官方资料为主：NumPy Absolute Beginners / NumPy Learn / Scientific Python Lectures / SciPy Lecture Notes / PyTorch Learn the Basics / Start Locally / Tensor Tutorial / Autograd Tutorial / Neural Networks Tutorial / Quickstart / 60 Minute Blitz / CIFAR10 Tutorial。
- 验证：`wc -l projects/zero-basics-plan/analysis/2026-03-26-deep-learning-beginner-resource-survey.md` 输出 `588`；`grep -n "## 推荐资料清单\|## 按任务要求映射资料\|## 与 28 天课程框架的对齐建议\|## 最小资料包建议\|## Provenance" projects/zero-basics-plan/analysis/2026-03-26-deep-learning-beginner-resource-survey.md` 命中第 128 / 261 / 402 / 542 / 564 行，确认关键章节存在。

### 2026-03-26T19:47:23+08:00

- 审查 `projects/zero-basics-plan/plans/2026-03-26-course-framework.md`，重点检查结构完整性、零基础适配度、难度梯度、里程碑与审批节点，以及 Humanize 分层审批链。
- 关键发现：当前文档只有 50 行，且未出现 `Goal Description`、`Acceptance Criteria`、`Path Boundaries`、`Milestone`、`审批`、`Humanize` 等计划/审批关键字段，仍是主题纲要，不足以充当顶层执行方案或 Humanize 评审输入。
- 关键缺口：未写目标人群边界、阶段里程碑、过关标准、审批角色、失败返工路径；“每周复盘”可视为教学活动，但尚不是可执行的审批 gate。
- 依据：`projects/zero-basics-plan/TASKS.md` 要求顶层方案覆盖“28天/4周课程结构、目标人群、产出规范、阶段里程碑、审批节点”，Humanize SOP 要求 Plan 至少包含 Goal Description、Acceptance Criteria、Path Boundaries。
- 详细审查记录见 `projects/zero-basics-plan/logs/2026-03-26T19:47:23+08:00-codex-course-framework-review.md`。

### 2026-03-26T19:44:28+08:00

- 完成项目重启现状梳理，产出 `projects/zero-basics-plan/analysis/2026-03-26-restart-status.md`。
- 本次梳理确认项目已具备 28 天课程框架、6 份专题调研、1 份实践项目案例调研、1 份完整教程草案；当前阶段重点已从“补资料”转为“资料审查、执行方案、Humanize 审查、正式拆章”。
- 同步修正 `projects/zero-basics-plan/TASKS.md` 中 3 个任务状态：将已实际完成但未收口的“VibeCoding 调研”“实践项目案例调研”标记为完成，并将本次“重启现状说明”任务标记完成，避免后续重复认领。
- 验证：`wc -l projects/zero-basics-plan/analysis/*.md projects/zero-basics-plan/zero-basics-plan-course-draft.md` 输出总计 `4122` 行；其中课程草案 `751` 行、VibeCoding 调研 `648` 行、实践项目案例调研 `437` 行、课程框架 `306` 行，确认关键交付物已存在且非空。

## Open questions

1. 是否要为 Windows / macOS / Linux 分别做 3 套安装截图版教程？
2. 是否在 28 天课程中统一使用 VS Code，还是允许 Cursor 作为第 2 周升级路线？
3. 是否需要额外补充中文视频教程，以降低纯英文官方文档门槛？
4. 顶层计划的 Humanize 分层审批链应由谁负责签核：顶层计划、周计划、日计划、最终课程草案各自使用 Ask-Codex、Gen-Plan→RLCR、还是一次性 review；每个 gate 的输入/输出工件与通过标准分别是什么？
