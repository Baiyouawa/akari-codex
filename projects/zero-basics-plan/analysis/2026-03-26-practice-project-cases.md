# 28 天课程实践项目案例调研

- 项目：`projects/zero-basics-plan`
- 任务：调研实践项目案例：为 28 天课程匹配由浅入深的小练习或小项目，如命令行练习、Git 协作练习、Cursor 辅助编码、小型深度学习 demo
- 产出人：Fleet Worker `岛村-01-1774524772-3cf537`
- 日期：2026-03-26

## 调研目标

为《零基础计划》现有 28 天课程框架补齐一条“从会做单步练习，到能完成最小项目”的实践主线。要求：

1. 练习难度随周次递进，而不是随机堆砌。
2. 每个练习都能映射到现有课程日程与已有资料调研。
3. 优先选择能直接验证成果的案例：文件、命令输出、Git 提交记录、PR、脚本运行结果、模型推理结果。
4. 尽量复用官方或准官方材料中的练习形式，降低课程设计风险。

## 结论摘要

1. **Week 1 最适合采用“命令序列练习 + 小脚本 + Bandit 闯关”三层结构。** 其中 OverTheWire Bandit 官方页明确说明它“aimed at absolute beginners”，适合做周末挑战。来源：`https://overthewire.org/wargames/bandit/`。
2. **Week 2 最适合采用“本地 Git 仓库演练 → Learn Git Branching 交互练习 → GitHub Skills 协作练习”三层结构。** Learn Git Branching 官方站点是浏览器内模拟仓库；GitHub Skills 提供官方模板仓库，适合做 Issue / PR / Actions 练习。来源：`https://learngitbranching.js.org/`、`https://github.com/skills/hello-github-actions`、`https://github.com/skills/review-pull-requests`、`https://github.com/skills/test-with-actions`。
3. **Week 3 最适合采用“纯手写 Python 小程序 → Cursor 辅助重构 / 修 bug → 有规则的 AI 协作小项目”三层结构。** 这样能避免学生一开始把 AI 当黑箱。来源：`projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`、`projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`、`https://cursor.com/learn/creating-features`。
4. **Week 4 最适合采用“NumPy 计算练习 → PyTorch 张量与 quickstart → 最小分类 demo”三层结构。** NumPy 官方绝对初学者指南和 PyTorch Quickstart / Training a Classifier 已经提供了从数组到分类器的自然阶梯。来源：`https://numpy.org/doc/stable/user/absolute_beginners.html`、`https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html`、`https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html`。
5. **整个 28 天课程最稳妥的项目主线不是一个大项目，而是 4 个逐步升级的小项目。** 原因是零基础学习者在 28 天内更需要可闭环的小成功，而不是长期大工程。此判断基于项目内课程框架“每天必须有手、每周必须回环”的原则。来源：`projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`。

## 选型标准

为保证练习真正适合零基础，本次筛选按以下标准进行：

1. **可验证**：能通过命令、文件、仓库记录、网页链接、截图或日志判断是否完成。
2. **低前置**：不要求学习者提前掌握复杂框架。
3. **可拆步**：可以在 20~90 分钟内完成一个子练习。
4. **可衔接**：能自然衔接到下一周主题。
5. **有官方支撑**：优先使用官方文档、官方教程或项目内已有官方资料调研。

## 课程实践设计总表

| 周次 | 实践主线 | 练习类型 | 最终产出 | 主要来源 |
|---|---|---|---|---|
| Week 1 | Linux / 命令行生存 | 命令操作、目录整理、权限、Shell 小脚本、Bandit | `week1-lab/` + `bootstrap.sh` + `week1-review.md` | Ubuntu / Linux Journey / Bandit / 既有 Linux 调研 |
| Week 2 | Git / GitHub 协作 | 本地仓库、分支合并、冲突解决、Issue / PR / Actions | GitHub 仓库 + 1 个 PR + 1 个 workflow | Pro Git / Learn Git Branching / GitHub Skills |
| Week 3 | Python + Cursor + VibeCoding | CLI 小程序、文件读写、AI 重构、带规则协作 | `week3-mini-project/` + AI 协作记录 | Python 官方教程 / Cursor Learn / 既有 Python & 工具链调研 |
| Week 4 | NumPy / PyTorch / 深度学习入门 | 数组练习、张量练习、quickstart、分类 demo | `week4-dl-demo/` + 推理截图/日志 | NumPy / PyTorch 官方教程 |

## Week 1：命令行与 Linux 练习案例

### 案例 1：个人练习目录搭建
- 对应日程：Day 1~2
- 学习目标：理解路径、目录、文件、复制、移动、删除。
- 任务说明：
  1. 新建 `zero-basics/week1/day1`。
  2. 在其中创建 `notes/`、`drafts/`、`assets/` 三个子目录。
  3. 创建 `todo.txt`、`hello.txt`。
  4. 把 `hello.txt` 移动到 `notes/`，复制到 `drafts/`。
- 验收标准：
  - 能用 `pwd`、`ls`、`tree` 或 `find` 展示目录结构。
  - 最终目录中至少有 2 个文本文件、3 个子目录。
- 对应来源：
  - `projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`
  - `https://documentation.ubuntu.com/desktop/en/latest/tutorial/the-linux-command-line-for-beginners/`

### 案例 2：权限实验
- 对应日程：Day 3
- 学习目标：理解可读、可写、可执行。
- 任务说明：
  1. 新建 `run.sh`，内容为输出当天日期。
  2. 在不可执行时尝试运行，观察报错。
  3. 用 `chmod +x run.sh` 后再次运行。
- 验收标准：
  - 记录“修改前后”的现象差异。
  - `run.sh` 成功输出日期或固定文本。
- 对应来源：
  - `projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`

### 案例 3：Linux 备忘单项目
- 对应日程：Day 4~5
- 学习目标：形成“查帮助 → 摘要整理”的自救能力。
- 任务说明：
  1. 选择 10 个常用命令，如 `pwd`、`ls`、`cd`、`cp`、`mv`、`rm`、`cat`、`chmod`、`man`、`grep`。
  2. 每个命令写 1 句用途 + 1 个示例。
  3. 整理成 `linux-cheatsheet.md`。
- 验收标准：
  - 文档至少包含 10 条命令。
  - 至少 5 条带示例命令。
- 对应来源：
  - `projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`
  - `https://overthewire.org/wargames/bandit/` 中对 `man` / `help` / 搜索的建议。

### 案例 4：Shell 自动化脚本
- 对应日程：Day 6
- 学习目标：理解“把重复命令写进脚本”。
- 任务说明：
  1. 编写 `bootstrap.sh`。
  2. 自动创建 `logs/`、`notes/`、`src/`、`data/`。
  3. 自动生成当天日期文件 `logs/YYYY-MM-DD.txt`。
- 验收标准：
  - 运行一次脚本后自动出现目录树。
  - 第二次运行不应把已有文件破坏掉，或要在说明中写明覆盖行为。
- 对应来源：
  - `projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`

### 案例 5：Bandit 周末挑战
- 对应日程：Day 7
- 学习目标：把本周命令行能力投入真实闯关情境。
- 任务说明：
  1. 完成 OverTheWire Bandit Level 0 → 3 或 0 → 5。
  2. 对每一关记录“用了什么命令、为什么想到这个命令”。
- 验收标准：
  - 提交 `bandit-notes.md`。
  - 每关至少写 2 句：命令 + 思路。
- 适配理由：Bandit 官方页明确写明“aimed at absolute beginners”。
- 对应来源：
  - `https://overthewire.org/wargames/bandit/`

## Week 2：Git / GitHub 协作练习案例

### 案例 6：从零初始化本地仓库
- 对应日程：Day 8~9
- 学习目标：理解工作区、暂存区、提交记录。
- 任务说明：
  1. 建立 `demo-repo/`。
  2. 新建 `README.md`、`notes.md`。
  3. 完成至少 3 次 commit，主题分别为“初始化 / 增加内容 / 修正文案”。
- 验收标准：
  - `git log --oneline` 至少出现 3 条记录。
  - `README.md` 中写明项目用途。
- 对应来源：
  - `projects/zero-basics-plan/analysis/git-github-beginners-research.md`
  - `https://git-scm.com/book/en/v2`

### 案例 7：Learn Git Branching 交互闯关
- 对应日程：Day 10~11
- 学习目标：理解 branch、merge、rebase 的动态图景。
- 任务说明：
  1. 完成 Learn Git Branching 的基础分支 / 合并 / rebase 练习若干关。
  2. 将每关对应的命令抄回本地仓库中手动执行一遍。
- 验收标准：
  - 记录至少 3 个操作：`branch`、`merge`、`rebase`。
  - 提交 `git-branching-notes.md`，解释每个操作解决什么问题。
- 适配理由：官方站点就是浏览器中模拟仓库，特别适合新手先理解再实操。
- 对应来源：
  - `https://learngitbranching.js.org/`
  - `projects/zero-basics-plan/analysis/git-github-beginners-research.md`

### 案例 8：手动制造并解决一次冲突
- 对应日程：Day 11
- 学习目标：认识冲突不是灾难，而是协作中的普通现象。
- 任务说明：
  1. 在 `main` 和 `feature-a` 分支修改同一行。
  2. 合并时触发冲突。
  3. 手工编辑冲突标记并完成 commit。
- 验收标准：
  - 截图或记录冲突标记 `<<<<<<<` `=======` `>>>>>>>`。
  - 最终成功合并并留下解释说明。
- 对应来源：
  - `projects/zero-basics-plan/analysis/git-github-beginners-research.md`

### 案例 9：GitHub 个人发布练习
- 对应日程：Day 12~13
- 学习目标：把本地仓库连接到远程并体验最小协作流程。
- 任务说明：
  1. 创建 GitHub 仓库。
  2. 推送本地项目。
  3. 自己给自己提一个 issue，例如“补充安装说明”。
  4. 新建分支修复后发起 PR 并合并。
- 验收标准：
  - 仓库在线可访问。
  - 至少 1 个 issue、1 个 PR。
- 对应来源：
  - `https://docs.github.com/en/get-started/start-your-journey/hello-world`
  - `projects/zero-basics-plan/analysis/git-github-beginners-research.md`

### 案例 10：GitHub Skills 自动化入门
- 对应日程：Day 14 或 Week 2 加餐
- 学习目标：感受“仓库不仅存代码，还能自动跑流程”。
- 任务说明：
  1. 参考 `skills/hello-github-actions` 完成一个最简单 workflow。
  2. 若时间允许，再参考 `skills/test-with-actions` 或 `skills/review-pull-requests` 做扩展。
- 验收标准：
  - 仓库 `Actions` 页出现一次成功运行。
  - 写一段话说明 Actions 在做什么。
- 适配理由：GitHub Skills 仓库本身就是教学模板，门槛低于从零配置复杂 CI。
- 对应来源：
  - `https://github.com/skills/hello-github-actions`
  - `https://github.com/skills/test-with-actions`
  - `https://github.com/skills/review-pull-requests`

## Week 3：Python / Cursor / VibeCoding 练习案例

### 案例 11：命令行成绩判断器
- 对应日程：Day 15~16
- 学习目标：练习输入、变量、条件判断。
- 任务说明：
  1. 用户输入一个分数。
  2. 程序输出等级 A/B/C/D。
  3. 处理非法输入可作为加分项。
- 验收标准：
  - `grade_checker.py` 可运行。
  - 至少测试 3 组输入。
- 对应来源：
  - `projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`

### 案例 12：待办清单 CLI
- 对应日程：Day 17~18
- 学习目标：练习列表、字典、函数、文件读写。
- 任务说明：
  1. 实现“查看任务 / 添加任务 / 标记完成 / 保存到文本文件”。
  2. 初版可只支持命令行菜单。
- 验收标准：
  - 至少包含 3 个函数。
  - 能读写 `tasks.txt` 或 `tasks.json`。
- 对应来源：
  - `projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`

### 案例 13：Cursor 解释与重构练习
- 对应日程：Day 19
- 学习目标：先让 AI 做“解释者”和“重构建议者”，而不是直接代写全部程序。
- 任务说明：
  1. 将自己写好的 `grade_checker.py` 或 `todo_cli.py` 打开到 Cursor。
  2. 让 Cursor 解释代码结构。
  3. 再让 Cursor 做一次“小范围重构”，例如提取函数、改变量名、增加注释。
- 验收标准：
  - 保留一份 `before.py` 和 `after.py` 对比，或用 Git commit 展示差异。
  - 学员能写下“我接受了哪些建议、拒绝了哪些建议”。
- 对应来源：
  - `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`
  - `https://cursor.com/learn/creating-features`

### 案例 14：有规则的 AI 协作小项目
- 对应日程：Day 20
- 学习目标：学会给 AI 设护栏，而不是只下模糊指令。
- 任务说明：
  1. 新建一个简单规则文件，内容示例：
     - 每次只改一个文件；
     - 先解释思路，再给代码；
     - 必须给运行命令；
     - 如果不确定，要写明假设。
  2. 让 Cursor 帮你做一个“单词计数器”或“批量重命名文件”小工具。
- 验收标准：
  - 提交规则文件。
  - 提交 AI 协作记录：提示词、运行命令、实际输出、发现的问题。
- 对应来源：
  - `https://cursor.com/docs/rules`
  - `https://cursor.com/learn/creating-features`
  - `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`

### 案例 15：Week 3 迷你项目
- 对应日程：Day 21
- 学习目标：完成一个“有输入、有逻辑、有文件读写、经过 AI 协作和人工验证”的闭环项目。
- 可选项目：
  1. 命令行记账本
  2. 待办事项管理器
  3. 学习时间记录器
- 验收标准：
  - 项目目录至少包含 `README.md`、主程序、数据文件或示例数据。
  - README 必须写“如何运行”“AI 参与了什么”“我是怎么验证的”。
- 对应来源：
  - `projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`
  - `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`

## Week 4：NumPy / PyTorch / 深度学习 demo 案例

### 案例 16：NumPy 数组计算练习
- 对应日程：Day 22
- 学习目标：理解数组、shape、切片、统计量。
- 任务说明：
  1. 创建一个 2×3 数组。
  2. 计算和、均值、最大值。
  3. 做一组切片操作。
- 验收标准：
  - `numpy_basics.py` 成功运行。
  - 输出至少包含 `shape`、`mean`、`max`。
- 对应来源：
  - `https://numpy.org/doc/stable/user/absolute_beginners.html`

### 案例 17：PyTorch 张量速写
- 对应日程：Day 23~24
- 学习目标：理解 tensor、shape、自动求导前置概念。
- 任务说明：
  1. 创建几个张量。
  2. 执行加法、矩阵乘法、reshape。
  3. 记录 NumPy 数组和 tensor 在写法上的相似之处。
- 验收标准：
  - `tensor_basics.py` 可运行。
  - 写一段“tensor 和数组哪里像、哪里不同”。
- 对应来源：
  - `https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html`
  - `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`

### 案例 18：FashionMNIST Quickstart
- 对应日程：Day 24~26
- 学习目标：理解 dataset、dataloader、train、test、predict 的最小闭环。
- 任务说明：
  1. 运行 PyTorch Quickstart。
  2. 观察训练输出。
  3. 对 1 张样本做预测。
  4. 用自己的话解释：模型输入是什么，输出是什么。
- 验收标准：
  - 至少保存一次训练日志或终端输出。
  - 写 `quickstart-notes.md`，解释 `train` 和 `predict`。
- 对应来源：
  - `https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html`

### 案例 19：最小分类器观察实验
- 对应日程：Day 25~27
- 学习目标：把“网络、训练、损失、预测”串起来。
- 任务说明：
  1. 运行 PyTorch `Training a Classifier` 教程的最小版本或教师预裁剪版。
  2. 不要求从头理解全部 CNN 细节，但要记录：输入是什么、标签是什么、模型最后输出什么。
  3. 如果完整版过重，可只保留前几步：下载数据、看 batch、跑一次前向、看输出维度。
- 验收标准：
  - 至少记录 1 次 batch shape。
  - 至少记录 1 次模型输出 shape 或预测结果。
- 对应来源：
  - `https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html`

### 案例 20：结营综合项目
- 对应日程：Day 27~28
- 学习目标：把 Linux / Git / Python / Cursor / 深度学习 demo 串成一个能展示的仓库。
- 推荐项目模板：
  1. **学习数据统计器**：命令行读取学习记录文件，用 NumPy 统计平均学习时长，再把结果提交到 GitHub。
  2. **最小图像分类演示仓库**：保留官方 quickstart / classifier 的运行脚本、结果说明和自己的理解笔记。
  3. **AI 协作增强版 CLI 工具**：Week 3 的 CLI 工具 + Week 4 的简单数据分析模块。
- 验收标准：
  - GitHub 仓库中包含 README、运行说明、至少 5 次 commit。
  - README 明确标注：哪些部分来自官方教程，哪些部分是自己改的，哪些部分由 Cursor 辅助。
- 对应来源：
  - `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`
  - `https://numpy.org/doc/stable/user/absolute_beginners.html`
  - `https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html`

## 推荐的 28 天练习映射

| Day | 推荐练习 / 项目 | 预计时长 | 验收物 |
|---|---|---:|---|
| 1 | 个人练习目录搭建 | 20-30 分钟 | 目录树 |
| 2 | 文件整理与复制移动 | 20-30 分钟 | 命令记录 |
| 3 | 权限实验 | 20 分钟 | `run.sh` |
| 4 | Linux 备忘单 | 30-45 分钟 | `linux-cheatsheet.md` |
| 5 | 环境审计清单 | 20-30 分钟 | `environment-audit.md` |
| 6 | Shell 自动化脚本 | 30-60 分钟 | `bootstrap.sh` |
| 7 | Bandit 闯关 | 30-60 分钟 | `bandit-notes.md` |
| 8 | 初始化 Git 仓库 | 20-30 分钟 | 仓库 + 1 次 commit |
| 9 | 3 次 commit 练习 | 20-30 分钟 | `git log --oneline` |
| 10 | Learn Git Branching 基础关 | 20-40 分钟 | `git-branching-notes.md` |
| 11 | 冲突制造与解决 | 30-45 分钟 | 冲突说明 |
| 12 | 推送 GitHub | 20-30 分钟 | 仓库链接 |
| 13 | Issue + PR 模拟协作 | 30-45 分钟 | 1 个 issue + 1 个 PR |
| 14 | GitHub Actions 初体验 | 30-60 分钟 | 成功 workflow |
| 15 | `hello.py` + 环境准备 | 20-30 分钟 | `hello.py` |
| 16 | 成绩判断器 | 20-40 分钟 | `grade_checker.py` |
| 17 | 列表 / 字典小程序 | 30-45 分钟 | `todo_cli.py` |
| 18 | 文件读写版待办清单 | 30-45 分钟 | `tasks.txt` + 程序 |
| 19 | Cursor 解释与重构 | 20-40 分钟 | before/after 对比 |
| 20 | 有规则的 AI 协作工具 | 30-60 分钟 | 规则文件 + 小工具 |
| 21 | Week 3 迷你项目 | 45-90 分钟 | `week3-mini-project/` |
| 22 | NumPy 数组练习 | 20-40 分钟 | `numpy_basics.py` |
| 23 | PyTorch 张量练习 | 20-40 分钟 | `tensor_basics.py` |
| 24 | Quickstart 阅读 + 运行 | 30-60 分钟 | 训练输出 |
| 25 | autograd / 网络结构观察 | 30-60 分钟 | `autograd_notes.md` |
| 26 | train vs infer 记录 | 30-45 分钟 | `train_vs_infer.md` |
| 27 | 最小分类 demo / 综合项目 | 45-90 分钟 | `week4-dl-demo/` |
| 28 | 结营整理与仓库封装 | 45-60 分钟 | `graduation-review.md` |

## 教学落地建议

### 1. 优先做“小练习串联”，不要一上来做“大项目”
零基础用户在 28 天内更需要连续反馈。建议按照“命令小练习 → 小项目 → 综合项目”的顺序推进，而不是第一周就开长期项目。

### 2. 每周只保留 1 个主项目，其他都做支撑练习
- Week 1 主项目：`bootstrap.sh` + Linux 练习目录
- Week 2 主项目：GitHub 协作仓库
- Week 3 主项目：CLI 工具
- Week 4 主项目：最小深度学习 demo 仓库

### 3. AI 辅助编程必须带验证模板
建议课程统一要求学员每次 AI 协作都填写 4 项：
1. 我给了什么提示
2. AI 改了什么
3. 我如何运行验证
4. 我发现了什么问题

### 4. 深度学习阶段要允许“观察型成功”
对零基础而言，Week 4 不必把重点放在从零写神经网络，而应允许以下层次的成功：
- 能运行官方 demo
- 能解释输入输出
- 能识别训练与推理区别
- 能在 README 中写清楚自己看懂了什么

## 与现有课程框架的衔接建议

本次调研建议对 `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md` 做如下增强：

1. 在每个 Day 下新增一栏“最小练习”。
2. 在每个 Week 复盘日新增一栏“本周主项目验收”。
3. 在最终教程中单独整理 `practice-roadmap.md`，把所有练习与项目集中列出，便于学员按产出推进。

## 最小可直接采用的项目清单

如果现在就要从本调研中抽取最稳妥的 8 个实践项目，建议选这 8 个：

1. 个人练习目录搭建
2. 权限实验 + `run.sh`
3. `bootstrap.sh` 自动建项目骨架
4. Learn Git Branching 基础闯关
5. GitHub 仓库 + issue + PR 模拟协作
6. 文件读写版待办清单 CLI
7. Cursor 规则驱动的小工具协作
8. PyTorch Quickstart / 最小分类 demo

## Provenance

### 项目内既有材料
- `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`
- `projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`
- `projects/zero-basics-plan/analysis/git-github-beginners-research.md`
- `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`
- `projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`

### 本次会话额外核验的外部来源
- OverTheWire Bandit — `https://overthewire.org/wargames/bandit/`
  - 关键句：`The Bandit wargame is aimed at absolute beginners.`
- Learn Git Branching — `https://learngitbranching.js.org/`
  - 关键点：浏览器内模拟 Git 仓库，适合新手交互式练习。
- GitHub Skills: Hello GitHub Actions — `https://github.com/skills/hello-github-actions`
- GitHub Skills: Review Pull Requests — `https://github.com/skills/review-pull-requests`
- GitHub Skills: Test with Actions — `https://github.com/skills/test-with-actions`
- Cursor Learn: Developing Features — `https://cursor.com/learn/creating-features`
- Cursor Docs: Rules — `https://cursor.com/docs/rules`
- NumPy Absolute Beginners — `https://numpy.org/doc/stable/user/absolute_beginners.html`
- PyTorch Quickstart — `https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html`
- PyTorch Training a Classifier — `https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html`

## Open questions

1. Week 4 的深度学习 demo 是否应统一提供“教师预裁剪版”，以避免下载数据和训练时间过长？
2. GitHub 协作练习是否要强制要求找同学互评 PR，还是允许“自己给自己发 PR”作为保底方案？
3. Cursor 练习是否要提供统一规则模板，避免新手提示词质量差导致挫败感？
