# 《零基础计划》28 天教程草案

- 项目：`projects/zero-basics-plan`
- 草案日期：2026-03-26
- 编写会话：`智乃-02-1774524802-39277a`
- 文档状态：draft v1
- 适用人群：完全零基础，希望在 28 天内建立 Linux / Git / GitHub / Python / Cursor / VibeCoding / 基础深度学习最小能力闭环的学习者。

---

## 1. 课程说明

### 1.1 这门课要解决什么问题

很多零基础学习路线会出现三个问题：

1. **只学概念，不做产出**：看了很多文章，但没有自己的代码、仓库、项目。
2. **工具链断裂**：会一点 Python，但不会终端、不会 Git、不会配环境，导致后续 AI / 深度学习阶段频繁卡住。
3. **过早依赖 AI**：直接让 Cursor 或其他 AI 工具生成代码，却没有能力运行、验证、定位报错。

《零基础计划》的目标是用 28 天建立一条最小可用路径：

- 会在终端中完成基本操作
- 会使用 Git 和 GitHub 管理学习成果
- 会写基础 Python 程序
- 会在 VS Code / Cursor 中完成最小 AI 辅助编程练习
- 会运行最小 NumPy / PyTorch / 深度学习 demo
- 会把学习过程沉淀成仓库、文档和阶段性项目

### 1.2 学习方法

本课程采用 4 条固定规则：

1. **每天都要动手。** 每天至少完成一个可验证任务。
2. **每周都要复盘。** 第 7 / 14 / 21 / 28 天为系统课程与整合训练日。
3. **所有学习都留痕。** 每周产出统一提交到 Git 仓库。
4. **AI 只能辅助，不能替代验收。** 任何 Cursor / AI 生成的内容都必须手动运行与验证。

### 1.3 学完后的可见成果

完成 28 天后，你至少应拥有：

1. 一个自己的 GitHub 仓库，包含四周学习笔记与练习
2. 一个 Week 3 小型命令行项目
3. 一个 Week 4 最小深度学习 demo
4. 一份结营复盘文档，说明已经掌握与仍待补强的内容

### 1.4 工具建议

当前草案采用以下默认路线：

- **操作系统 / 命令行**：优先按 Linux / Ubuntu 文档路径组织概念
- **编辑器基础层**：优先使用 VS Code
- **AI 辅助编码层**：第 3 周开始引入 Cursor
- **代码管理**：Git + GitHub
- **Python 环境**：官方 `venv` + `pip`
- **深度学习入门**：NumPy + PyTorch 官方初学者文档

> 注：是否为 Windows / macOS / Linux 单独制作截图版安装教程，仍是项目开放问题，见本文末尾“开放问题”。

---

## 2. 四周总目标

| 周次 | 主题 | 周目标 | 周末系统课程产出 |
|---|---|---|---|
| Week 1 | Linux / 终端基础 | 建立命令行生存能力，理解文件系统、常用命令、权限、软件安装、Shell 最小概念 | `week1-review.md` + Linux 命令备忘单 |
| Week 2 | Git / GitHub | 理解版本控制，掌握本地 Git、分支、合并、远程仓库、Issue / PR 基础流程 | `week2-release-notes.md` + GitHub 仓库 |
| Week 3 | Python / VS Code / Cursor / VibeCoding | 掌握基础 Python，并建立“AI 辅助写代码 + 人工验证”的闭环 | `week3-mini-project/` + `week3-review.md` |
| Week 4 | NumPy / PyTorch / 基础深度学习 | 形成张量、自动求导、网络、训练、推理最小心智模型，并跑通最小 demo | 深度学习 demo 仓库 + `graduation-review.md` |

---

## 3. 28 天日程安排

## Week 1 — Linux 与终端基础

### Day 1｜认识 Linux、终端与文件系统
- **学习目标**
  - 知道 Linux 是什么、终端是做什么的
  - 理解根目录、家目录、当前目录、绝对路径、相对路径
- **今日资料**
  - Ubuntu Desktop: The Linux command line for beginners  
    https://documentation.ubuntu.com/desktop/en/latest/tutorial/the-linux-command-line-for-beginners/
  - USTC OS Docs：Linux 基础教程  
    http://home.ustc.edu.cn/~pzw2002/appendix/linux.html
- **今日任务**
  1. 打开终端
  2. 依次运行 `pwd`、`ls`、`cd ~`
  3. 创建 `zero-basics/week1/day1`
  4. 在其中新建 `hello.txt`
- **阶段性产出**
  - 一份命令记录或截图
  - 自己创建的练习目录树

### Day 2｜文件与目录操作
- **学习目标**
  - 掌握 `cp`、`mv`、`rm`、`cat`、`less`
  - 理解“复制、移动、删除、查看”的区别
- **今日资料**
  - 菜鸟教程：Linux 文件与目录管理  
    https://www.runoob.com/linux/linux-file-content-manage.html
  - LinuxCommand.org: Learning the Shell  
    https://linuxcommand.org/lc3_learning_the_shell.php
- **今日任务**
  1. 在 Day 1 目录中新增 `notes/` 与 `drafts/`
  2. 复制一个文件到 `notes/`
  3. 把它移动到 `drafts/`
  4. 用 `cat` 和 `less` 查看内容
- **阶段性产出**
  - `day2-file-ops.md`，写下你今天用过的命令及作用

### Day 3｜权限与可执行文件
- **学习目标**
  - 理解 `rwx`、owner / group / others
  - 会用 `chmod` 修改文件可执行权限
- **今日资料**
  - 菜鸟教程：Linux 文件基本属性  
    https://www.runoob.com/linux/linux-file-attr-permission.html
  - LinuxCommand.org: Learning the Shell  
    https://linuxcommand.org/lc3_learning_the_shell.php
- **今日任务**
  1. 新建 `run.sh`
  2. 写入 `echo "hello linux"`
  3. 分别观察未授权与授权后的执行差异
  4. 用 `ls -l` 记录权限变化
- **阶段性产出**
  - `permission-notes.md`

### Day 4｜查帮助、会自救
- **学习目标**
  - 会用 `man`、`--help`
  - 学会在命令行环境里自己查命令
- **今日资料**
  - OverTheWire Bandit  
    https://overthewire.org/wargames/bandit/
  - MIT Missing Semester: The Shell  
    https://missing.csail.mit.edu/2020/course-shell/
- **今日任务**
  1. 查出 `ls -la` 的含义
  2. 查出 `cp -r` 的含义
  3. 查出 `chmod +x` 的含义
  4. 写一张一页式命令备忘单
- **阶段性产出**
  - `linux-cheatsheet.md`

### Day 5｜软件安装与环境意识
- **学习目标**
  - 知道什么是包管理器、解释器、PATH
  - 知道系统软件安装和 Python 包安装不是一回事
- **今日资料**
  - 菜鸟教程：Linux apt 命令  
    https://www.runoob.com/linux/linux-comm-apt.html
  - Ubuntu apt manpage  
    https://manpages.ubuntu.com/manpages/jammy/en/man8/apt.8.html
- **今日任务**
  1. 运行 `apt search tree` 或阅读等价命令说明
  2. 记录自己机器是否已安装 Python / Git
  3. 记录当前 shell 和至少一个 PATH 中的可执行程序
- **阶段性产出**
  - `environment-audit.md`

### Day 6｜Shell 小自动化
- **学习目标**
  - 理解脚本、重定向、批量化操作的意义
  - 会写一个最小 shell 脚本
- **今日资料**
  - 菜鸟教程：Shell 教程  
    https://www.runoob.com/linux/linux-shell.html
  - MIT Missing Semester: The Shell  
    https://missing.csail.mit.edu/2020/course-shell/
- **今日任务**
  1. 写一个 5~10 行脚本 `bootstrap.sh`
  2. 自动创建 `week1/day6/output`
  3. 输出当前日期到 `today.txt`
- **阶段性产出**
  - `bootstrap.sh`

### Day 7｜Week 1 系统课程：Linux 生存能力复盘
- **系统课程目标**
  - 把文件系统、命令、权限、安装、脚本串成一套完整流程
- **系统课程资料**
  - USTC OS Docs：Linux 基础教程  
    http://home.ustc.edu.cn/~pzw2002/appendix/linux.html
  - OverTheWire Bandit  
    https://overthewire.org/wargames/bandit/
- **系统课程任务**
  1. 从空目录开始创建项目目录
  2. 新建文件并写入内容
  3. 修改权限使脚本可执行
  4. 写一页总结：最常用的 10 个命令
  5. 如果可以，尝试完成 Bandit 前 1~3 关
- **阶段性产出**
  - `week1-review.md`
  - `linux-cheatsheet.md`

---

## Week 2 — Git / GitHub 与协作基础

### Day 8｜Git 是什么，为什么需要版本控制
- **学习目标**
  - 理解版本控制、仓库、提交历史
  - 分清 Git 和 GitHub
- **今日资料**
  - Pro Git Book  
    https://git-scm.com/book/en/v2
  - GitHub Docs: About Git  
    https://docs.github.com/en/get-started/using-git/about-git
- **今日任务**
  1. 安装或确认 Git
  2. 运行 `git --version`
  3. 新建 `demo-repo`
  4. 执行 `git init`
- **阶段性产出**
  - 一个本地 Git 仓库

### Day 9｜第一次 commit
- **学习目标**
  - 理解工作区、暂存区、提交的关系
  - 会用 `git status`、`git add`、`git commit`
- **今日资料**
  - Pro Git：Getting a Git Repository  
    https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository
  - Git 官方参考  
    https://git-scm.com/docs
- **今日任务**
  1. 新建 `README.md`
  2. 运行 `git status`
  3. 执行 `git add README.md`
  4. 提交两次小修改
- **阶段性产出**
  - 至少 2 条 commit 记录

### Day 10｜查看历史与撤销基础
- **学习目标**
  - 会看历史、比较差异、恢复简单改动
- **今日资料**
  - Pro Git Book  
    https://git-scm.com/book/en/v2
  - git-commit / git-diff / git-log 参考入口  
    https://git-scm.com/docs
- **今日任务**
  1. 运行 `git log --oneline`
  2. 修改文件后看 `git diff`
  3. 撤回一次未提交改动
- **阶段性产出**
  - `git-observation-cheatsheet.md`

### Day 11｜分支、合并与冲突
- **学习目标**
  - 理解 branch 的作用
  - 知道 merge 和冲突为什么会出现
- **今日资料**
  - Pro Git Book  
    https://git-scm.com/book/en/v2
  - Learn Git Branching  
    https://learngitbranching.js.org/
- **今日任务**
  1. 创建 `feature-a` 分支
  2. 修改同一个文件
  3. 合并回主分支
  4. 手动解决一次冲突
- **阶段性产出**
  - 一次带说明的 merge 记录

### Day 12｜远程仓库与 GitHub
- **学习目标**
  - 理解本地仓库与远程仓库的差别
  - 会把本地仓库推到 GitHub
- **今日资料**
  - GitHub Docs: Hello World  
    https://docs.github.com/en/get-started/start-your-journey/hello-world
  - GitHub Docs: Quickstart for repositories  
    https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories
- **今日任务**
  1. 新建 GitHub 仓库
  2. 设置 `origin`
  3. 执行第一次 push
- **阶段性产出**
  - 你的第一个 GitHub 仓库链接

### Day 13｜Issue / PR / Review 的协作意义
- **学习目标**
  - 理解 Issue、PR、Review 在协作中的角色
- **今日资料**
  - GitHub Docs: GitHub flow  
    https://docs.github.com/en/get-started/using-github/github-flow
  - GitHub Docs: About issues  
    https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
- **今日任务**
  1. 在自己的仓库创建 1 条 Issue
  2. 新建分支修复或补充内容
  3. 提交 1 条 PR
  4. 尝试在 PR 描述中关联 Issue
- **阶段性产出**
  - 1 条 Issue + 1 条 PR

### Day 14｜Week 2 系统课程：一次完整发布流程
- **系统课程目标**
  - 把本地 Git 与 GitHub 协作流程串起来
- **系统课程资料**
  - Pro Git Book  
    https://git-scm.com/book/en/v2
  - GitHub Docs: GitHub flow  
    https://docs.github.com/en/get-started/using-github/github-flow
- **系统课程任务**
  1. 从空仓库开始完成初始化
  2. 完成至少 3 次 commit
  3. 新建 1 个分支并合并
  4. 推送到 GitHub
  5. 写一份 release note
- **阶段性产出**
  - `week2-release-notes.md`
  - 可访问的 GitHub 仓库

---

## Week 3 — Python / VS Code / Cursor / VibeCoding

### Day 15｜Python 环境与第一段程序
- **学习目标**
  - 理解解释器、脚本、REPL
  - 运行第一段 Python 程序
- **今日资料**
  - Python Tutorial  
    https://docs.python.org/3/tutorial/index.html
  - Python Tutorial: An Informal Introduction to Python  
    https://docs.python.org/3/tutorial/introduction.html
  - VS Code Python Tutorial  
    https://code.visualstudio.com/docs/python/python-tutorial
  - PY4E Lessons  
    https://www.py4e.com/lessons
- **今日任务**
  1. 安装或确认 Python
  2. 在 VS Code 中创建 `hello.py`
  3. 运行 `print("hello")`
  4. 尝试进入 Python 解释器做 2~3 个简单表达式
- **阶段性产出**
  - `hello.py`
  - 命令记录或截图

### Day 16｜变量、条件与循环
- **学习目标**
  - 掌握变量、输入输出、`if`、`for`、`while`
- **今日资料**
  - Python Tutorial: Control Flow  
    https://docs.python.org/3/tutorial/controlflow.html
  - PY4E Lessons  
    https://www.py4e.com/lessons
- **今日任务**
  1. 写一个分数等级判断器
  2. 写一个 1~100 求和程序
  3. 可选：写一个简化版猜数字游戏
- **阶段性产出**
  - `grade_checker.py`
  - `sum_100.py`

### Day 17｜列表、字典与函数
- **学习目标**
  - 理解列表、字典、函数封装
- **今日资料**
  - Python Tutorial: Data Structures  
    https://docs.python.org/3/tutorial/datastructures.html
  - Python Tutorial: Control Flow  
    https://docs.python.org/3/tutorial/controlflow.html
  - Google’s Python Class Basic Exercises  
    https://developers.google.com/edu/python/exercises/basic
- **今日任务**
  1. 写一个待办清单程序或通讯录程序
  2. 把重复逻辑改写成函数
  3. 练一个 `list1.py` 或 `string1.py` 风格练习
- **阶段性产出**
  - `todo_cli.py` 或 `contacts.py`

### Day 18｜模块、文件读写与虚拟环境
- **学习目标**
  - 理解 `import`、模块、文件读写、`.venv`
- **今日资料**
  - Python Tutorial: Modules  
    https://docs.python.org/3/tutorial/modules.html
  - Python Tutorial: Input and Output  
    https://docs.python.org/3/tutorial/inputoutput.html
  - Python Tutorial: Virtual Environments and Packages  
    https://docs.python.org/3/tutorial/venv.html
- **今日任务**
  1. 写一个脚本把任务保存到 `tasks.txt`
  2. 再把内容读取并打印
  3. 在项目目录创建 `.venv`
  4. 记录激活命令与 `pip list`
- **阶段性产出**
  - `task_store.py`
  - `tasks.txt`
  - `venv-notes.md`

### Day 19｜认识 VS Code 与 Cursor 的分工
- **学习目标**
  - 知道 VS Code 是基础编辑器工作台
  - 知道 Cursor 是 AI 强化的编程环境
- **今日资料**
  - VS Code Getting Started  
    https://code.visualstudio.com/docs/getstarted/getting-started
  - VS Code Terminal Basics  
    https://code.visualstudio.com/docs/terminal/basics
  - Cursor Docs  
    https://cursor.com/docs
  - Cursor Learn: Agents  
    https://cursor.com/learn/agents
- **今日任务**
  1. 在 VS Code 中打开项目文件夹
  2. 打开集成终端并运行 Python 文件
  3. 进入 Cursor 文档了解 Agent 基础
  4. 用 AI 帮你解释一段自己写的 Python 代码
- **阶段性产出**
  - `cursor-first-impression.md`，记录 3 个优点和 3 个风险点

### Day 20｜VibeCoding 入门：让 AI 辅助，但自己验收
- **学习目标**
  - 建立“拆需求 → 给上下文 → 运行 → 看报错 → 修复”的闭环
- **今日资料**
  - Cursor Learn: Developing Features  
    https://cursor.com/learn/creating-features
  - Cursor Learn: Customizing Agents  
    https://cursor.com/learn/customizing-agents
  - Cursor Docs: Rules  
    https://cursor.com/docs/rules
  - Cursor Docs: Terminal  
    https://cursor.com/docs/agent/tools/terminal
- **今日任务**
  1. 让 Cursor 帮你完成一个小工具，如单词统计器
  2. 给 AI 写一条简单规则：每次改动后必须给出运行命令
  3. 运行代码并记录实际输出
  4. 如果报错，让 AI 解释原因，但必须手动再次验证
- **阶段性产出**
  - 一个可运行的小工具
  - `ai-collaboration-record.md`

### Day 21｜Week 3 系统课程：Python + AI 辅助编码小项目
- **系统课程目标**
  - 把 Python 基础与 Cursor / AI 辅助编程整合为一个小交付
- **系统课程资料**
  - Python Tutorial  
    https://docs.python.org/3/tutorial/
  - Cursor Docs  
    https://cursor.com/docs
  - VS Code Python Debugging  
    https://code.visualstudio.com/docs/python/debugging
- **系统课程任务**
  1. 做一个小型命令行应用
  2. 要求包含：输入、条件判断、循环、文件读写
  3. 至少让 Cursor 参与一次重构或报错解释
  4. 自己记录验证过程
- **阶段性产出**
  - `week3-mini-project/`
  - `week3-review.md`

---

## Week 4 — NumPy / PyTorch / 基础深度学习

### Day 22｜NumPy：为什么需要数组计算
- **学习目标**
  - 理解 Python 列表与数组的差别
  - 会创建数组、查看 `shape`、做基础运算
- **今日资料**
  - NumPy Absolute Beginners  
    https://numpy.org/doc/stable/user/absolute_beginners.html
  - NumPy Learn  
    https://numpy.org/learn/
- **今日任务**
  1. 创建一维和二维数组
  2. 打印 `.shape`
  3. 做一次求和、均值、切片
- **阶段性产出**
  - `numpy_basics.py`

### Day 23｜张量与 PyTorch 基础
- **学习目标**
  - 理解 tensor 是“带形状的多维数字表”
  - 会创建张量并做基础运算
- **今日资料**
  - PyTorch Learn the Basics  
    https://docs.pytorch.org/tutorials/beginner/basics/intro.html
  - PyTorch Tensor Tutorial  
    https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html
  - PyTorch Start Locally  
    https://docs.pytorch.org/get-started/locally/
- **今日任务**
  1. 安装并导入 `torch`
  2. 创建几个张量
  3. 完成加法、矩阵乘法、reshape
- **阶段性产出**
  - `tensor_basics.py`

### Day 24｜自动求导：梯度在做什么
- **学习目标**
  - 理解参数、损失、梯度、反向传播的最小概念
- **今日资料**
  - PyTorch Autograd Tutorial  
    https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html
  - PyTorch Learn the Basics  
    https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- **今日任务**
  1. 创建 `requires_grad=True` 的张量
  2. 构造一个简单表达式
  3. 调用 `backward()`
  4. 打印 `.grad`
- **阶段性产出**
  - `autograd_demo.py`
  - `autograd_notes.md`

### Day 25｜第一个小神经网络
- **学习目标**
  - 理解输入层、隐藏层、输出层的最小结构
  - 知道 `nn.Module` 是什么
- **今日资料**
  - PyTorch Neural Networks Tutorial  
    https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
  - PyTorch Quickstart  
    https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
- **今日任务**
  1. 运行一个最小网络示例
  2. 打印模型参数与输出 shape
  3. 记录一次 loss
- **阶段性产出**
  - `first_nn.py`
  - `training-log.md`

### Day 26｜训练与推理的区别
- **学习目标**
  - 理解训练集 / 验证集 / 测试集
  - 明白训练和推理不是同一回事
- **今日资料**
  - PyTorch Quickstart  
    https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
  - PyTorch CIFAR10 Tutorial  
    https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
- **今日任务**
  1. 记录训练阶段会做什么
  2. 记录推理阶段会做什么
  3. 用一个训练后模型对新输入做预测
- **阶段性产出**
  - `train_vs_infer.md`

### Day 27｜综合项目：从命令行到 AI demo
- **学习目标**
  - 把 Linux / Git / Python / Cursor / 深度学习串成一个最小项目
- **今日资料**
  - Pro Git Book  
    https://git-scm.com/book/en/v2
  - Cursor Docs  
    https://cursor.com/docs
  - PyTorch Quickstart / 60 Minute Blitz  
    https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
    https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- **今日任务**
  1. 完成一个最小项目
  2. 至少包含 README、代码、运行命令、输出说明
  3. 使用 Git 提交并推送 GitHub
  4. 如使用 Cursor，必须记录哪些部分由 AI 协助完成
- **阶段性产出**
  - 完整项目仓库

### Day 28｜Week 4 系统课程：结营复盘与下一阶段路线
- **系统课程目标**
  - 梳理四周知识结构，形成下一阶段进阶路线图
- **系统课程资料**
  - 回看本月所有官方资料与个人产出
- **系统课程任务**
  1. 回答“我已经会了什么 / 还不会什么 / 下一步补什么”
  2. 汇总项目仓库、学习笔记、练习清单
  3. 标出最值得重复练习的 3 个任务
  4. 写出是否要继续走 AI 编程、算法、后端或深度学习方向
- **阶段性产出**
  - `graduation-review.md`
  - 最终仓库目录索引

---

## 4. 每周末系统课程统一要求

第 7 / 14 / 21 / 28 天的系统课程，统一追加以下要求：

1. 回顾本周新增概念，不超过 10 条
2. 回放本周练习，筛出 1 个最值得重做的练习
3. 把本周所有产出提交到 Git 仓库
4. 写一页“问题清单”：哪些地方还不懂、下周如何避免重复踩坑
5. 如果使用了 AI 辅助工具，必须写明：
   - 哪些内容是 AI 提供的
   - 哪些内容是自己验证过的
   - 哪些问题是 AI 没解决、最后靠自己排查的

---

## 5. 每周阶段性产出汇总

| 周次 | 最低交付要求 |
|---|---|
| Week 1 | `linux-cheatsheet.md`、`environment-audit.md`、`week1-review.md` |
| Week 2 | GitHub 仓库、至少 1 条 Issue、1 条 PR、`week2-release-notes.md` |
| Week 3 | `hello.py`、至少 3 个 Python 练习文件、1 个 AI 协作记录、`week3-mini-project/` |
| Week 4 | `numpy_basics.py`、`tensor_basics.py`、`first_nn.py`、最小深度学习 demo、`graduation-review.md` |

---

## 6. 推荐的仓库目录结构

```text
zero-basics-learning/
├── README.md
├── notes/
│   ├── week1-review.md
│   ├── week2-release-notes.md
│   ├── week3-review.md
│   └── graduation-review.md
├── week1/
│   ├── linux-cheatsheet.md
│   ├── environment-audit.md
│   └── bootstrap.sh
├── week2/
│   └── demo-repo-notes.md
├── week3/
│   ├── hello.py
│   ├── grade_checker.py
│   ├── todo_cli.py
│   └── week3-mini-project/
└── week4/
    ├── numpy_basics.py
    ├── tensor_basics.py
    ├── autograd_demo.py
    ├── first_nn.py
    └── final-demo/
```

---

## 7. 使用 AI 辅助编程时的课程约束

### 7.1 必须遵守

1. 先自己写出任务目标，再找 AI 帮忙
2. AI 每次只允许改一个小点
3. AI 给出代码后必须本地运行
4. 必须保留运行命令、报错、修复记录
5. 不允许把“AI 说可以”当成“真的可以”

### 7.2 建议给 Cursor 的固定规则模板

可在课程中给学员一份简化规则：

```md
你是我的编程助手。
每次请按以下顺序输出：
1. 先解释你准备改什么
2. 每次尽量只改一个文件
3. 给出运行命令
4. 说明预期输出
5. 如果不确定，请明确写出假设
```

---

## 8. 后续可拆分的正式文档结构

如果下一步要把本草案拆成正式教程，建议拆成：

1. `01-course-overview.md`
2. `02-week1-linux.md`
3. `03-week2-git-github.md`
4. `04-week3-python-cursor-vibecoding.md`
5. `05-week4-deep-learning.md`
6. `06-resource-audit.md`

---

## 9. Provenance

本草案基于项目内已完成调研与课程框架文件整理而成：

- 总体课程框架：
  - `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`
- Linux 资料调研：
  - `projects/zero-basics-plan/analysis/2026-03-26-linux-beginner-resource-survey.md`
- Git / GitHub 调研：
  - `projects/zero-basics-plan/analysis/git-github-beginners-research.md`
- 工具链 / Cursor / VS Code / 调试调研：
  - `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`
- Python 与编程基础调研：
  - `projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`
- 基础深度学习调研：
  - `projects/zero-basics-plan/analysis/2026-03-26-deep-learning-beginner-resource-survey.md`

本草案直接引用或沿用的外部主资料链接包括：

- Linux / Shell：
  - https://documentation.ubuntu.com/desktop/en/latest/tutorial/the-linux-command-line-for-beginners/
  - http://home.ustc.edu.cn/~pzw2002/appendix/linux.html
  - https://linuxcommand.org/lc3_learning_the_shell.php
  - https://www.runoob.com/linux/linux-file-content-manage.html
  - https://www.runoob.com/linux/linux-file-attr-permission.html
  - https://www.runoob.com/linux/linux-comm-apt.html
  - https://www.runoob.com/linux/linux-shell.html
  - https://missing.csail.mit.edu/2020/course-shell/
  - https://overthewire.org/wargames/bandit/
- Git / GitHub：
  - https://git-scm.com/book/en/v2
  - https://git-scm.com/docs
  - https://docs.github.com/en/get-started/using-git/about-git
  - https://docs.github.com/en/get-started/start-your-journey/hello-world
  - https://docs.github.com/en/get-started/using-github/github-flow
  - https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
  - https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories
  - https://learngitbranching.js.org/
- Python / Tooling / Cursor：
  - https://docs.python.org/3/tutorial/
  - https://docs.python.org/3/tutorial/controlflow.html
  - https://docs.python.org/3/tutorial/datastructures.html
  - https://docs.python.org/3/tutorial/modules.html
  - https://docs.python.org/3/tutorial/inputoutput.html
  - https://docs.python.org/3/tutorial/venv.html
  - https://www.py4e.com/lessons
  - https://developers.google.com/edu/python/exercises/basic
  - https://code.visualstudio.com/docs/getstarted/getting-started
  - https://code.visualstudio.com/docs/terminal/basics
  - https://code.visualstudio.com/docs/python/python-tutorial
  - https://code.visualstudio.com/docs/python/debugging
  - https://cursor.com/docs
  - https://cursor.com/learn/agents
  - https://cursor.com/learn/creating-features
  - https://cursor.com/learn/customizing-agents
  - https://cursor.com/docs/rules
  - https://cursor.com/docs/agent/tools/terminal
- Deep Learning：
  - https://numpy.org/doc/stable/user/absolute_beginners.html
  - https://numpy.org/learn/
  - https://docs.pytorch.org/tutorials/beginner/basics/intro.html
  - https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
  - https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html
  - https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html
  - https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
  - https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
  - https://docs.pytorch.org/get-started/locally/

---

## 10. 开放问题

1. 是否要为 Windows / macOS / Linux 分别做 3 套安装截图版教程？
2. 第 3 周是否统一使用 VS Code，还是允许 Cursor 作为升级路线？
3. 是否需要额外补充中文视频教程，以降低纯英文官方文档门槛？
4. 是否需要为 VibeCoding 单独追加一份“提示词与验收模板”附录？
