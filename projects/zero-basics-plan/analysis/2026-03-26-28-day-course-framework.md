# 《零基础计划》28 天四周课程框架（课程总表）

- Date: 2026-03-26
- Session: `岛村-01-1774523931-34903a`
- Task: 设计整体课程框架：将教程拆分为 4 周共 28 天，每天有明确学习目标、实操任务、配套资料；每周末安排一次系统课程复盘与整合训练
- Status: completed draft

## 适用人群

- 完全零基础，尚未形成稳定的命令行、版本控制、编程与 AI 工具使用习惯的学习者。
- 目标是在 28 天内建立一条最小可用路径：会用 Linux/终端、会用 Git/GitHub、能写基础 Python、能借助 Cursor 完成简单任务、能看懂并运行最小深度学习 demo。

## 设计原则

1. **先环境，后协作，再编程，最后深度学习。** Linux/终端是 Git、Python、包管理与调试的前置能力。
2. **每天必须有手。** 每天至少安排一个可验证的实操输出，避免只读不练。
3. **每周必须回环。** 第 7/14/21/28 天固定做系统复盘与整合训练。
4. **工具不是替代思考。** Cursor / AI 辅助编程被安排在 Python 基础同步阶段，强调“先拆任务、再提示、后验收”。
5. **课程总量受控。** 4 周共 `4 × 7 = 28` 天；其中复盘日 `4` 天，主题学习日 `24` 天。计算为内联算术。

---

## Week 1 — Linux 与终端基础

**周目标**：建立最小命令行生存能力，理解文件系统、常用命令、权限、软件安装与 Shell 基本工作方式。

### Day 1 — 认识 Linux、终端与文件系统
- 学习目标：知道 Linux 是什么、终端是做什么的、目录/路径/家目录的基本概念。
- 实操任务：打开终端，完成 `pwd`、`ls`、`cd`、`mkdir`、`touch`，创建 `zero-basics/week1/day1` 目录并放入一个 `hello.txt`。
- 配套资料：
  - Linux Journey — https://linuxjourney.org/
  - Linux Journey Tutorials — https://linuxjourney.org/tutorials
- 阶段产出：一份你自己创建的练习目录树截图或命令记录。

### Day 2 — 文件与目录操作
- 学习目标：掌握复制、移动、删除、查看文件内容的最常见命令。
- 实操任务：练习 `cp`、`mv`、`rm`、`cat`、`less`，把 Day 1 的目录重组为 `notes/` 与 `drafts/` 两个子目录。
- 配套资料：
  - Linux Journey Tutorials — https://linuxjourney.org/tutorials
- 阶段产出：整理后的目录结构与一份命令清单。

### Day 3 — 权限与用户概念
- 学习目标：理解可读/可写/可执行权限，认识 `chmod` 与基本用户/组概念。
- 实操任务：新建一个脚本文件 `run.sh`，分别观察不可执行与可执行时的差异。
- 配套资料：
  - Linux Journey Tutorials — https://linuxjourney.org/tutorials
- 阶段产出：一份“权限修改前后”记录。

### Day 4 — 搜索、帮助与命令自救
- 学习目标：会用 `man`、`--help`、基础搜索命令解决问题。
- 实操任务：独立查出 `ls -la`、`cp -r`、`chmod +x` 的含义，并写成一页备忘单。
- 配套资料：
  - Linux Journey Tutorials — https://linuxjourney.org/tutorials
- 阶段产出：`linux-cheatsheet.md`。

### Day 5 — 软件安装与环境意识
- 学习目标：知道“包管理器/解释器/可执行文件/环境变量”这些词大概是什么意思。
- 实操任务：记录自己机器的系统信息、Shell 类型、Python 是否已安装，以及 PATH 中至少一个可执行程序。
- 配套资料：
  - Linux Journey Tutorials — https://linuxjourney.org/tutorials
  - VS Code Docs（工具环境视角）— https://code.visualstudio.com/docs/python/python-tutorial
- 阶段产出：`environment-audit.md`。

### Day 6 — Shell 小自动化
- 学习目标：理解命令串联、重定向、最小脚本化思维。
- 实操任务：写一个 5~10 行的 Shell 脚本，自动创建练习目录并生成日期文件。
- 配套资料：
  - Linux Journey Tutorials — https://linuxjourney.org/tutorials
- 阶段产出：`bootstrap.sh`。

### Day 7 — Week 1 复盘与整合训练
- 学习目标：把本周零散命令合成一个完整流程。
- 实操任务：从空目录开始，完成“创建项目目录 → 生成文件 → 修改权限 → 查看内容 → 写一页总结”。
- 配套资料：
  - Linux Journey — https://linuxjourney.org/
- 阶段产出：`week1-review.md`，内容包括你最常用的 10 个命令与踩坑总结。

---

## Week 2 — Git / GitHub 与协作基础

**周目标**：理解版本控制，掌握本地 Git 基础、分支与合并、远程仓库、GitHub 基本协作流程。

### Day 8 — Git 是什么，为什么需要版本控制
- 学习目标：理解版本控制、仓库、提交、历史记录的基本意义。
- 实操任务：安装/确认 Git，运行 `git --version`，初始化一个练习仓库。
- 配套资料：
  - Pro Git Book — https://git-scm.com/book/en/v2
  - GitHub Docs: About Git — https://docs.github.com/en/get-started/using-git/about-git
- 阶段产出：本地 `demo-repo` 仓库。

### Day 9 — 第一次 commit
- 学习目标：理解工作区、暂存区、提交的基本流程。
- 实操任务：在仓库里创建 `README.md`，完成 `git status`、`git add`、`git commit`。
- 配套资料：
  - Pro Git Book — https://git-scm.com/book/en/v2
- 阶段产出：至少 2 次 commit 记录。

### Day 10 — 查看历史与撤销基础
- 学习目标：知道如何看历史、比较差异、撤销简单改动。
- 实操任务：练习 `git log`、`git diff`、修改文件后回退到上一个稳定状态。
- 配套资料：
  - Pro Git Book — https://git-scm.com/book/en/v2
- 阶段产出：一张“常用 Git 观察命令”备忘卡。

### Day 11 — 分支、合并与冲突
- 学习目标：理解 branch 的作用，知道 merge 是什么、冲突为什么会出现。
- 实操任务：创建 `feature-a` 分支修改同一文件，再与主分支合并并手动解决一次冲突。
- 配套资料：
  - Pro Git Book — https://git-scm.com/book/en/v2
- 阶段产出：一次带冲突解决说明的合并记录。

### Day 12 — GitHub 仓库与远程协作
- 学习目标：知道本地仓库和远程仓库的区别，会把本地项目推到 GitHub。
- 实操任务：注册/登录 GitHub，新建远程仓库，把本地仓库连接为 `origin` 并推送。
- 配套资料：
  - GitHub Docs: Hello World — https://docs.github.com/en/get-started/start-your-journey/hello-world
  - GitHub Docs: About Git — https://docs.github.com/en/get-started/using-git/about-git
- 阶段产出：你的第一个 GitHub 公开或私有仓库链接。

### Day 13 — GitHub 基本协作元素：Issue / PR / Review
- 学习目标：理解 issue、pull request、review、merge 的协作意义。
- 实操任务：在自己的仓库里模拟一次“提 issue → 新建分支修改 → 发起 PR → 合并”。
- 配套资料：
  - GitHub Docs: Hello World — https://docs.github.com/en/get-started/start-your-journey/hello-world
- 阶段产出：一条 issue 与一条 PR。

### Day 14 — Week 2 复盘与整合训练
- 学习目标：把本地 Git 与 GitHub 远程流程串成一次完整发布过程。
- 实操任务：从空仓库开始完成“初始化 → 3 次 commit → 1 个分支 → 1 次合并 → 推送 GitHub → 写 Release Notes”。
- 配套资料：
  - Pro Git Book — https://git-scm.com/book/en/v2
  - GitHub Docs: Hello World — https://docs.github.com/en/get-started/start-your-journey/hello-world
- 阶段产出：`week2-release-notes.md`。

---

## Week 3 — Python + Cursor + VibeCoding 基础实践

**周目标**：掌握 Python 最基础语法，并开始在 Cursor / VS Code 中做 AI 辅助编码练习，形成“提出需求—生成代码—运行验证—修改修复”的闭环。

### Day 15 — Python 运行环境与第一段程序
- 学习目标：理解解释器、脚本、REPL 的区别，运行第一个 Python 程序。
- 实操任务：安装/确认 Python，运行 `print("hello")`，建立 `python-playground/`。
- 配套资料：
  - Python Tutorial — https://docs.python.org/3/tutorial/
  - VS Code Python Tutorial — https://code.visualstudio.com/docs/python/python-tutorial
- 阶段产出：`hello.py` 与运行截图/命令记录。

### Day 16 — 变量、条件、循环
- 学习目标：掌握变量、输入输出、`if`、`for`、`while` 的最小用法。
- 实操任务：写一个命令行小程序：输入分数，输出等级；再写一个 1~100 求和程序。
- 配套资料：
  - Python Tutorial — https://docs.python.org/3/tutorial/
- 阶段产出：`grade_checker.py`、`sum_100.py`。

### Day 17 — 列表、字典、函数
- 学习目标：理解常见数据结构与函数封装。
- 实操任务：把通讯录或待办清单写成 Python 程序，用列表/字典管理数据。
- 配套资料：
  - Python Tutorial — https://docs.python.org/3/tutorial/
- 阶段产出：`todo_cli.py` 或 `contacts.py`。

### Day 18 — 文件读写、模块与虚拟环境意识
- 学习目标：理解 `.py` 文件、导入模块、文本文件读写，知道虚拟环境存在的意义。
- 实操任务：写一个脚本，把一组任务保存到本地文本文件并重新读取显示。
- 配套资料：
  - Python Tutorial — https://docs.python.org/3/tutorial/
  - VS Code Python Tutorial — https://code.visualstudio.com/docs/python/python-tutorial
- 阶段产出：`task_store.py` 与 `tasks.txt`。

### Day 19 — 认识 Cursor / AI 编程工作台
- 学习目标：知道 Cursor 是什么、它与普通编辑器相比多了什么、什么叫 agentic development。
- 实操任务：安装 Cursor 或进入文档了解界面，完成一次“让 AI 帮你解释一段 Python 代码”的练习。
- 配套资料：
  - Cursor Docs — https://cursor.com/docs
  - Cursor Learn: Agents — https://cursor.com/learn/agents
  - Cursor Homepage — https://cursor.com
- 阶段产出：一份 `cursor-first-impression.md`，记录 3 个有用点和 3 个风险点。

### Day 20 — VibeCoding / AI 辅助编程入门
- 学习目标：建立正确的 AI 编程工作流：拆需求、给上下文、让 AI 生成、自己运行、自己验收。
- 实操任务：用 Cursor 或其他 AI 助手完成一个小工具，例如“统计单词数”或“批量重命名文件”，并手工验证结果。
- 配套资料：
  - Cursor Learn: Agents — https://cursor.com/learn/agents
  - Cursor Learn: Working with Agents — https://cursor.com/learn/working-with-agents
  - Andrej Karpathy 个人站（其站点集中整理了 AI 教育视频与 Zero to Hero 学习路径）— https://karpathy.ai/
- 阶段产出：一个能运行的小工具 + 一份“我给了 AI 什么提示、最后如何验证”的记录。

### Day 21 — Week 3 复盘与整合训练
- 学习目标：把 Python 基础与 AI 辅助编码合成一次完整小交付。
- 实操任务：做一个“小型命令行应用”，要求包含：输入、条件判断、循环、文件读写，且至少让 Cursor 参与一次重构或报错解释。
- 配套资料：
  - Python Tutorial — https://docs.python.org/3/tutorial/
  - Cursor Docs — https://cursor.com/docs
  - VS Code Python Tutorial — https://code.visualstudio.com/docs/python/python-tutorial
- 阶段产出：`week3-mini-project/` + `week3-review.md`。

---

## Week 4 — NumPy / PyTorch / 深度学习入门与综合项目

**周目标**：形成“数组/张量 → 自动求导 → 简单网络 → 训练与推理”的最小心智模型，并完成一个初学者可运行的 demo。

### Day 22 — 数值计算入门：NumPy
- 学习目标：理解数组与 Python 列表的区别，知道为什么数值计算常用 NumPy。
- 实操任务：创建数组，做加减乘除、切片、求均值与形状查看。
- 配套资料：
  - NumPy Absolute Beginners — https://numpy.org/doc/stable/user/absolute_beginners.html
- 阶段产出：`numpy_basics.py`。

### Day 23 — 张量与 PyTorch 基础
- 学习目标：理解张量和数组的关系，学会创建 tensor、查看 shape、做基础运算。
- 实操任务：用 PyTorch 创建几个张量，完成加法、矩阵乘法、reshape。
- 配套资料：
  - PyTorch Learn the Basics — https://docs.pytorch.org/tutorials/beginner/basics/intro.html
  - PyTorch 60 Minute Blitz — https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- 阶段产出：`tensor_basics.py`。

### Day 24 — 自动求导与训练直觉
- 学习目标：知道参数、损失、梯度、反向传播分别是什么意思。
- 实操任务：照着教程跑一个最简单的 autograd 示例，并用自己的话解释梯度在做什么。
- 配套资料：
  - PyTorch Learn the Basics — https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- 阶段产出：`autograd_notes.md` + 示例代码。

### Day 25 — 第一个小神经网络
- 学习目标：理解“输入层—隐藏层—输出层”的最小网络结构。
- 实操任务：运行一个官方入门网络示例，观察损失变化。
- 配套资料：
  - PyTorch 60 Minute Blitz — https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- 阶段产出：`first_nn.py` 与训练日志。

### Day 26 — 训练 vs 推理，数据与评估
- 学习目标：知道训练集/验证集/测试集、epoch、batch、推理这些词的基本含义。
- 实操任务：在现有 demo 上区分“训练阶段”与“预测阶段”，并记录模型输入输出。
- 配套资料：
  - PyTorch Learn the Basics — https://docs.pytorch.org/tutorials/beginner/basics/intro.html
  - PyTorch 60 Minute Blitz — https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- 阶段产出：`train_vs_infer.md`。

### Day 27 — 综合小项目：从命令行到 AI demo
- 学习目标：完成一次跨主题整合，把 Linux / Git / Python / Cursor / PyTorch 串到一个最小项目中。
- 实操任务：完成一个“可运行、可提交到 GitHub、可由 Cursor 协助改进”的小项目，例如：
  - 命令行数字分类演示器
  - 简单文本统计工具 + NumPy 可视化
  - PyTorch 最小分类 demo + README
- 配套资料：
  - Pro Git Book — https://git-scm.com/book/en/v2
  - Cursor Docs — https://cursor.com/docs
  - PyTorch 60 Minute Blitz — https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- 阶段产出：完整项目仓库。

### Day 28 — Week 4 总复盘与结营整合训练
- 学习目标：总结四周知识结构，明确下一阶段进阶路线。
- 实操任务：输出一份结营文档，至少回答：
  1. 我已经会了什么？
  2. 我还不会什么？
  3. 下一步要继续补什么？
  4. 我的项目仓库、学习笔记、练习清单分别在哪里？
- 配套资料：
  - 回看本月所有官方资料链接与个人产出
- 阶段产出：`graduation-review.md` + 最终仓库目录索引。

---

## 每周复盘日统一要求

第 7 / 14 / 21 / 28 天统一追加以下动作：

1. 回顾本周新增概念，不超过 10 条。
2. 回放本周所有练习，筛出 1 个最值得重做的练习。
3. 把本周产出提交到 Git 仓库。
4. 写一页“问题清单”：我哪里还不懂、卡点在哪里、下周如何避免。
5. 如果用了 AI 辅助工具，必须写明：哪些地方是 AI 给的，哪些地方是自己验证过的。

## 后续文档拆分建议

接下来可以把最终 Markdown 教程拆成以下文件：

1. `01-course-overview.md`：课程说明、学习方式、环境要求。
2. `02-week1-linux.md`：Week 1 的 7 天详细讲义。
3. `03-week2-git-github.md`：Week 2 的 7 天详细讲义。
4. `04-week3-python-cursor-vibecoding.md`：Week 3 的 7 天详细讲义。
5. `05-week4-deep-learning.md`：Week 4 的 7 天详细讲义。
6. `06-resource-audit.md`：资料质量、访问性、适合初学者理由。

## Provenance

本课程框架中的“资料来源”全部来自本次会话实际检索与抓取到的公开文档：

- Linux Journey — https://linuxjourney.org/
- Linux Journey Tutorials — https://linuxjourney.org/tutorials
- Pro Git Book — https://git-scm.com/book/en/v2
- GitHub Docs: About Git — https://docs.github.com/en/get-started/using-git/about-git
- GitHub Docs: Hello World — https://docs.github.com/en/get-started/start-your-journey/hello-world
- Cursor Docs — https://cursor.com/docs
- Cursor Learn: Agents — https://cursor.com/learn/agents
- Cursor Learn: Working with Agents — https://cursor.com/learn/working-with-agents
- Cursor Homepage — https://cursor.com
- VS Code Python Tutorial — https://code.visualstudio.com/docs/python/python-tutorial
- Python Tutorial — https://docs.python.org/3/tutorial/
- NumPy Absolute Beginners — https://numpy.org/doc/stable/user/absolute_beginners.html
- PyTorch Learn the Basics — https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- PyTorch 60 Minute Blitz — https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- Andrej Karpathy — https://karpathy.ai/
