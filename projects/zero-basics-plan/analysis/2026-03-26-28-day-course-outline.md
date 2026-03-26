# 零基础计划：28 天、4 周完整课程大纲

- 日期：2026-03-26
- 任务：基于现有调研结果设计 28 天、4 周完整课程大纲；每天包含学习目标、任务安排、详细学习资料、实践内容；每周末安排系统课程用于回顾、串联和综合练习。
- 适用对象：几乎没有 Linux、Git/GitHub、Python、AI 辅助编程、深度学习基础的学习者。
- 课程定位：以“能独立搭环境、能做基础协作、能写小脚本、能正确使用 Cursor、能跑通最小深度学习 demo”为 28 天阶段目标。

## 一、课程设计依据

### 1.1 已使用的项目内调研

1. `projects/zero-basics-plan/analysis/2026-03-26-vscode-linux-beginner-resource-survey.md`
   - 提供 VSCode 远程开发、Linux 入门、命令行、权限、SSH/Remote-SSH、常见坑等中文资料清单与课程映射。
2. `projects/zero-basics-plan/plans/调研并整理基础深度学习入门所需的前置知识-核心概念-学习路径与适合零基础的中文资料-最终汇总为28天四周课程大纲-包含每.md`
   - 提供深度学习模块的覆盖范围、前置知识边界、4 周/28 天课程组织要求。
3. `projects/zero-basics-plan/plans/最终汇总为-markdown-文档结构方案-要求内容包含每日教程正文框架-资料来源区块-每周系统课程安排-学习顺序说明与.md`
   - 提供 Markdown 教程落地约束，包括每日模板、周级安排、阶段成果目标与多 Agent 协作要求。

### 1.2 本次额外校验过的公开资料

以下资料均通过本次会话的 `web_fetch(URL)` 抓取首页或正文要点，用于校验课程顺序和资料用途：

- Python Tutorial — `https://docs.python.org/3/tutorial/`
- Pro Git Book — `https://git-scm.com/book/en/v2`
- GitHub Docs: Hello World — `https://docs.github.com/en/get-started/start-your-journey/hello-world`
- GitHub Docs: About Git — `https://docs.github.com/en/get-started/using-git/about-git`
- GitHub Docs: Set up Git — `https://docs.github.com/en/get-started/git-basics/set-up-git`
- VS Code Docs: Remote Development using SSH — `https://code.visualstudio.com/docs/remote/ssh`
- VS Code Docs: Getting Started with Python in VS Code — `https://code.visualstudio.com/docs/python/python-tutorial`
- Cursor Learn: Agents — `https://cursor.com/learn/agents`
- Cursor Learn: Working with Agents — `https://cursor.com/learn/working-with-agents`
- NumPy Absolute Beginners — `https://numpy.org/doc/stable/user/absolute_beginners.html`
- PyTorch Learn the Basics — `https://docs.pytorch.org/tutorials/beginner/basics/intro.html`
- PyTorch Start Locally — `https://docs.pytorch.org/get-started/locally/`
- Learn Git Branching — `https://learngitbranching.js.org/`
- LinuxCommand.org: Learning the Shell — `https://linuxcommand.org/lc3_learning_the_shell.php`
- OverTheWire Bandit — `https://overthewire.org/wargames/bandit/`

## 二、学习顺序说明

课程采用“环境与终端 → 版本控制与协作 → Python 与 AI 辅助编程 → 深度学习最小闭环”的递进结构，原因如下：

1. Linux/终端能力是后续使用 SSH、编辑远程文件、安装 Python 包、执行 Git 命令的前置。
2. Git/GitHub 是后续保存学习成果、管理代码、与 AI 协作时做变更确认的基础。
3. Python 必须先于 Cursor 高强度使用出现，否则学习者容易变成只会复制 AI 生成结果而不会验证。
4. 深度学习模块放在第 4 周，是因为它依赖 Python、包安装、文件管理、基础调试能力。
5. 每周第 7 天统一作为系统课程，承担三种职责：
   - 知识回顾
   - 模块串联
   - 综合练习

## 三、统一模板

### 3.1 每日模板

每一天均使用相同字段：

- 学习目标
- 任务安排
- 详细学习资料
- 实践内容
- 建议产出

### 3.2 系统课程模板

每周第 7 天统一包含：

- 本周知识地图
- 核心概念回顾
- 跨天综合练习
- 常见问题纠错
- 阶段成果检查

## 四、Week 1：Linux、终端与远程开发入门

### Week 1 目标

- 理解 Linux、终端、路径、文件系统、权限、进程、网络基础。
- 能使用 SSH 连入服务器，能在 VS Code 中理解 Remote-SSH 的基本流程。
- 完成第一个可复现的命令行工作目录。

### Day 1：认识 Linux、终端与路径

- 学习目标：理解 Linux 是什么、终端在做什么、绝对路径与相对路径的区别。
- 任务安排：
  1. 认识根目录、家目录、当前目录。
  2. 练习 `pwd`、`ls`、`cd`。
  3. 创建学习目录 `~/zero-basics/week1/day1`。
- 详细学习资料：
  - `analysis/2026-03-26-vscode-linux-beginner-resource-survey.md` 中 LI-01《新手一周入门Linux，看这篇就够了！》：适合第 1 天建立整体地图。
  - `analysis/2026-03-26-vscode-linux-beginner-resource-survey.md` 中 LI-02《Linux 初学者指令指南》：适合补“路径”和“家目录”。
  - LinuxCommand.org `https://linuxcommand.org/lc3_learning_the_shell.php`：校验 shell 学习顺序，首页目录明确包含 Navigation 与 Looking Around。
- 实践内容：
  - 进入家目录后创建 `notes`、`sandbox` 两个子目录。
  - 记录 5 条命令及其作用。
- 建议产出：`day1-terminal-notes.md`

### Day 2：文件与目录操作

- 学习目标：掌握创建、复制、移动、删除文件与目录的基本命令。
- 任务安排：
  1. 练习 `mkdir`、`touch`、`cp`、`mv`、`rm`。
  2. 区分“复制”和“移动”。
  3. 建立安全练习意识：仅在 `sandbox` 内删除文件。
- 详细学习资料：
  - Survey 中 LI-01、LC-02：适合命令入门与高频组合。
  - Survey 中 LC-01：作为查表型补充资料。
- 实践内容：
  - 创建 `draft.txt`，复制为 `draft-copy.txt`，再移动到 `notes/`。
  - 删除 `sandbox/tmp.txt`，并说明为什么不能在系统目录随便执行 `rm -rf`。
- 建议产出：`day2-file-ops.md`

### Day 3：查看文件内容与搜索

- 学习目标：掌握查看文本与快速搜索信息的最小方法。
- 任务安排：
  1. 练习 `cat`、`less`、`head`、`tail`。
  2. 练习 `grep`、`find`。
  3. 理解“日志查看”和“内容检索”的基本场景。
- 详细学习资料：
  - Survey 中 LI-01：提供搜索与文本处理的按天引导。
  - Survey 中 LC-02、LC-03：补充命令示例与参数组合。
- 实践内容：
  - 生成一个包含 20 行文本的练习文件。
  - 用 `head` 看前 5 行、`tail` 看后 5 行、`grep` 找关键词。
- 建议产出：`day3-search-practice.md`

### Day 4：权限与用户基本概念

- 学习目标：理解 `rwx` 权限、所有者、所属组的最小概念。
- 任务安排：
  1. 看懂 `ls -l` 输出。
  2. 练习 `chmod u+x`。
  3. 理解为什么不应该把所有东西设成 `777`。
- 详细学习资料：
  - Survey 中 LI-05《Linux 文件基本属性》：适合拆解 `ls -l`。
  - Survey 中 LC-04《Linux chmod 命令》：补符号模式和数字模式。
  - GNU chmod 手册 `https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html`：用于校验递归改权限的风险。
- 实践内容：
  - 编写 `hello.sh` 并从“不可执行”改成“可执行”。
  - 对比 `chmod u+x hello.sh` 与 `chmod 755 hello.sh` 的效果。
- 建议产出：`day4-permission-notes.md`

### Day 5：软件安装、进程与网络基础

- 学习目标：知道包管理、进程、SSH 是什么，以及它们分别解决什么问题。
- 任务安排：
  1. 认识 `apt install` 的使用场景。
  2. 认识 `ps`、`top`、`kill` 的基本概念。
  3. 理解 SSH 是远程登录通道。
- 详细学习资料：
  - Survey 中 LI-01、LC-01：进程与系统信息的总体介绍。
  - Survey 中 VS-C3（菜鸟 `ssh` 命令页）与 VS-05（免密登录）：适合作为 SSH 入门前置。
- 实践内容：
  - 用文字回答“apt / ssh / ps 分别解决什么问题”。
  - 在本地或服务器上执行一次 `ps`，记录看到的进程示例。
- 建议产出：`day5-system-basics.md`

### Day 6：SSH 与 VS Code Remote-SSH 入门

- 学习目标：理解 SSH 配置、Remote-SSH 插件流程、密码登录与免密登录的差别。
- 任务安排：
  1. 认识 `Host`、`HostName`、`User`、`Port`。
  2. 配置最小 `~/.ssh/config` 示例。
  3. 理解 VS Code 通过 Remote-SSH 打开远程目录的工作方式。
- 详细学习资料：
  - Survey 中 VS-01、VS-02：作为主阅读。
  - VS Code Docs `https://code.visualstudio.com/docs/remote/ssh`：校验 Remote-SSH 术语与流程。
  - OpenSSH `ssh_config` 手册：校验配置字段含义。
- 实践内容：
  - 写出一份不含真实密码的 SSH config 模板。
  - 用语言解释“别名 Host 不是服务器真实地址”。
- 建议产出：`day6-ssh-config-example`

### Day 7：系统课程 1——Linux 与远程开发总复盘

- 学习目标：把 Week 1 的命令、权限、SSH、VS Code 远程流程串起来。
- 任务安排：
  1. 画出“本地电脑 → SSH → 远程服务器 → VS Code”流程图。
  2. 总结本周 12 个高频命令。
  3. 整理 5 个常见坑及其识别方法。
- 详细学习资料：
  - Survey 中 VS-03：作为排错专题材料。
  - Survey 中 LI-01：作为一周回顾索引。
  - OverTheWire Bandit `https://overthewire.org/wargames/bandit/`：首页明确说明面向 absolute beginners，可作为轻量挑战引入。
- 实践内容：
  - 在沙盒目录完成一次“创建目录 → 创建文件 → 赋可执行权限 → 查看文件内容 → 记录命令”的综合练习。
- 建议产出：`week1-review.md`

## 五、Week 2：Git、GitHub 与协作工作流

### Week 2 目标

- 建立版本控制观念。
- 能完成本地仓库创建、提交、分支、合并、推送。
- 理解 GitHub 的 issue、pull request、README 和协作基础流程。

### Day 8：为什么需要 Git

- 学习目标：理解版本控制、仓库、提交历史的意义。
- 任务安排：
  1. 了解 Git 解决的核心问题。
  2. 安装并检查 Git。
  3. 创建第一个本地仓库。
- 详细学习资料：
  - Pro Git `https://git-scm.com/book/en/v2`：目录明确包含 Getting Started、Git Basics、Git Branching。
  - GitHub Docs: About Git `https://docs.github.com/en/get-started/using-git/about-git`
- 实践内容：
  - 建立 `git-playground/` 并执行 `git init`。
  - 写 5 句“Git 和普通文件夹的区别”。
- 建议产出：`day8-why-git.md`

### Day 9：第一次 commit

- 学习目标：掌握工作区、暂存区、提交三步走。
- 任务安排：
  1. 配置用户名与邮箱。
  2. 建立 `README.md`。
  3. 进行两次提交，观察 `git status` 的变化。
- 详细学习资料：
  - GitHub Docs: Set up Git `https://docs.github.com/en/get-started/git-basics/set-up-git`
  - Pro Git 第 2 章（通过目录校验可覆盖 Getting a Repository 与 Recording Changes）
- 实践内容：
  - 第一次提交 README。
  - 第二次补充一段学习说明并再次提交。
- 建议产出：提交历史截图或文本说明

### Day 10：查看历史与回退基础

- 学习目标：能查看历史、比较差异、理解“恢复”的基本思路。
- 任务安排：
  1. 使用 `git log`、`git diff`。
  2. 理解“提交前修改”和“提交后历史”的区别。
  3. 认识常见误操作恢复思路。
- 详细学习资料：
  - Pro Git 第 2 章目录中的 Viewing the Commit History、Undoing Things。
  - Learn Git Branching `https://learngitbranching.js.org/`：浏览器模拟仓库，适合可视化理解分支和移动。
- 实践内容：
  - 修改 README，再用 `git diff` 看变化。
  - 写一段“我什么时候该先看 status，再看 diff”。
- 建议产出：`day10-history-and-diff.md`

### Day 11：分支、合并与冲突

- 学习目标：理解 branch 的作用，以及冲突为什么会发生。
- 任务安排：
  1. 创建新分支。
  2. 在不同分支修改同一文件。
  3. 手动解决一次最小冲突。
- 详细学习资料：
  - Pro Git 目录中的 Git Branching。
  - Learn Git Branching：适合作为分支模型可视化练习。
- 实践内容：
  - 新建 `feature-intro` 分支修改 README。
  - 合并回主分支并手动处理一次冲突。
- 建议产出：`day11-merge-conflict-notes.md`

### Day 12：GitHub 仓库与远程推送

- 学习目标：理解本地仓库与远程仓库的关系。
- 任务安排：
  1. 创建 GitHub 仓库。
  2. 配置远程地址。
  3. 完成首次推送。
- 详细学习资料：
  - GitHub Docs: Hello World `https://docs.github.com/en/get-started/start-your-journey/hello-world`
  - GitHub Docs: About Git。
- 实践内容：
  - 将本地练习仓库推送到 GitHub。
  - 记录 `origin` 的含义。
- 建议产出：远程仓库链接

### Day 13：README、Issue、Pull Request 基础协作

- 学习目标：理解 GitHub 中“文档、任务、变更评审”三类对象。
- 任务安排：
  1. 完善 README。
  2. 创建一个 issue。
  3. 从 issue 出发做一个 PR 流程演示。
- 详细学习资料：
  - GitHub Docs: Hello World：正文明确写到 pull request workflow。
  - Pro Git 中 GitHub 章节目录。
- 实践内容：
  - 新建 issue，说明一个待改进点。
  - 基于分支修复后发起 PR。
- 建议产出：issue + PR 链接

### Day 14：系统课程 2——版本控制与协作闭环

- 学习目标：把 Git 本地操作与 GitHub 协作流程连成一条链。
- 任务安排：
  1. 回顾 `init/add/commit/branch/merge/push/PR`。
  2. 整理 5 个常见坑：未配置用户名、推送前未拉取、在错误分支改文件、冲突后乱删标记、README 不写清楚项目目标。
  3. 完成一次完整协作演示。
- 详细学习资料：
  - Learn Git Branching：复盘 branch/merge 模型。
  - GitHub Docs: Hello World：复盘 pull request workflow。
- 实践内容：
  - 从空仓库重新走一遍最小 GitHub Flow。
- 建议产出：`week2-review.md`

## 六、Week 3：Python 基础 + Cursor + AI 辅助编程工作流

### Week 3 目标

- 掌握 Python 最基础语法和脚本组织方式。
- 能用 VS Code 或 Cursor 运行、调试、修改基础 Python 程序。
- 建立“先拆需求，再提示 AI，再手工验证”的工作流。

### Day 15：Python 运行环境与第一个脚本

- 学习目标：理解解释器、脚本、REPL 的区别。
- 任务安排：
  1. 检查 Python 版本。
  2. 建立 `python-playground`。
  3. 运行第一个 `hello.py`。
- 详细学习资料：
  - Python Tutorial `https://docs.python.org/3/tutorial/`：正文明确写明“designed for programmers that are new to the Python language”，适合作为语言主线，但不完全适合无编程背景者，因此需配合更细的中文解释。
  - VS Code Python Tutorial `https://code.visualstudio.com/docs/python/python-tutorial`
- 实践内容：
  - 写一个打印姓名与当天日期的脚本。
- 建议产出：`hello.py`

### Day 16：变量、输入输出、条件判断

- 学习目标：掌握变量、输入、`if` 的最小使用。
- 任务安排：
  1. 学习字符串、数字、输入函数。
  2. 练习条件分支。
  3. 让程序根据输入给出简单反馈。
- 详细学习资料：
  - Python Tutorial 第 3、4 章目录可覆盖数值、文本、控制流。
  - VS Code Python Tutorial 用于运行与编辑。
- 实践内容：
  - 写一个“输入分数输出等级”的小程序。
- 建议产出：`grade_checker.py`

### Day 17：循环、列表、字典

- 学习目标：掌握最常见的数据容器和循环处理方式。
- 任务安排：
  1. 学习 `for` 循环。
  2. 使用列表管理多条数据。
  3. 用字典表示一个简单对象。
- 详细学习资料：
  - Python Tutorial：第 3 章列表、第 4 章循环。
- 实践内容：
  - 写一个待办清单程序，能遍历显示任务。
- 建议产出：`todo_list.py`

### Day 18：函数、文件读写与最小项目结构

- 学习目标：知道如何把重复逻辑封装成函数，并把数据写入文件。
- 任务安排：
  1. 定义函数。
  2. 读取与写入文本文件。
  3. 学习简单模块化组织。
- 详细学习资料：
  - Python Tutorial：函数与模块相关章节。
  - VS Code Python Tutorial：帮助理解编辑、运行、调试路径。
- 实践内容：
  - 把待办清单保存到本地文本文件，再读出来显示。
- 建议产出：`task_store.py`

### Day 19：认识 Cursor 与 Agent 工作方式

- 学习目标：理解 Cursor 不是“自动替你完成所有事情”，而是一个需要上下文和约束的协作工具。
- 任务安排：
  1. 认识 Cursor 的核心使用场景。
  2. 理解 agent 模式与普通聊天式提问的区别。
  3. 学习如何描述目标、上下文、约束。
- 详细学习资料：
  - Cursor Learn: Agents `https://cursor.com/learn/agents`
  - Cursor Learn: Working with Agents `https://cursor.com/learn/working-with-agents`
  - `projects/zero-basics-plan/plans/调研并整理-vibe-coding-cursor-使用方法-ai辅助编程工作流-提示词与常见误区的中文资料-优先选择实战.md`：用于确认后续需要覆盖误区与工作流。
- 实践内容：
  - 写出 3 条“好提示词”和 3 条“坏提示词”示例。
- 建议产出：`day19-cursor-prompt-notes.md`

### Day 20：AI 辅助编程最小闭环

- 学习目标：掌握“需求拆解 → 给提示词 → 运行代码 → 检查结果 → 修复问题”的闭环。
- 任务安排：
  1. 先自己写需求。
  2. 再让 Cursor 生成初版代码。
  3. 手工验证并记录错误。
- 详细学习资料：
  - Cursor Learn 两篇。
  - VS Code Python Tutorial：用于运行与调试。
- 实践内容：
  - 让 Cursor 帮你生成一个“统计文本行数和单词数”的脚本。
  - 手工用 2 个输入样例验证输出。
- 建议产出：`text_stats.py` + 验证记录

### Day 21：系统课程 3——Python 与 AI 协作工作流复盘

- 学习目标：把 Python 基础、编辑器、Cursor 协作习惯串起来。
- 任务安排：
  1. 总结本周学到的 Python 核心概念。
  2. 总结 5 条 AI 辅助编程误区。
  3. 完成一个小型整合项目。
- 详细学习资料：
  - Python Tutorial、VS Code Python Tutorial、Cursor Learn。
- 实践内容：
  - 完成一个“命令行待办清单”或“简单文本处理器”，要求：
    - 有输入输出
    - 有函数
    - 有文件读写
    - 至少使用一次 Cursor 帮助重构或解释错误
- 建议产出：`week3-mini-project/` + `week3-review.md`

## 七、Week 4：NumPy、PyTorch 与最小深度学习实践

### Week 4 目标

- 理解数组、张量、梯度、训练、推理的最小直觉。
- 能在 CPU 环境中安装 PyTorch 并运行官方 beginner 路线的最小例子。
- 完成一个最小分类或预测 demo。

### Day 22：为什么先学 NumPy

- 学习目标：理解数组、shape、数值计算为什么是深度学习的前置直觉。
- 任务安排：
  1. 安装或导入 NumPy。
  2. 创建数组、查看 shape。
  3. 做基础运算与 reshape。
- 详细学习资料：
  - NumPy Absolute Beginners：正文直接写明“absolute beginner’s guide to NumPy”，适合作为第一个数值计算入口。
  - 深度学习计划文件：要求先处理前置知识，再进入训练与推理。
- 实践内容：
  - 创建一维和二维数组。
  - 打印 shape、求和、求平均值。
- 建议产出：`numpy_basics.py`

### Day 23：张量与 PyTorch 安装

- 学习目标：理解 tensor 是什么，以及 PyTorch 环境如何在 CPU 路线上最小启动。
- 任务安排：
  1. 按官方 Start Locally 选择 CPU 安装。
  2. 运行随机张量测试。
  3. 对比 NumPy array 与 tensor 的共性。
- 详细学习资料：
  - PyTorch Start Locally：正文明确写有 CPU 安装路线和随机张量验证代码。
  - PyTorch Learn the Basics：作为后续章节总入口。
- 实践内容：
  - 执行 `import torch`。
  - 构造一个 `torch.rand(5, 3)` 并打印。
- 建议产出：`tensor_start.py`

### Day 24：张量操作与 shape 直觉

- 学习目标：掌握 shape、切片、矩阵乘法这些最关键的张量直觉。
- 任务安排：
  1. 创建二维张量。
  2. 做基础算术运算。
  3. 观察 shape 变化。
- 详细学习资料：
  - PyTorch Learn the Basics 入口页。
  - NumPy Absolute Beginners：辅助强化 shape 概念。
- 实践内容：
  - 写一个脚本展示 `shape`、加法、矩阵乘法、reshape。
- 建议产出：`tensor_shape_demo.py`

### Day 25：损失、梯度与自动求导直觉

- 学习目标：理解损失函数、梯度、反向传播是“让参数朝更好方向调整”的机制。
- 任务安排：
  1. 用语言解释 loss 和 gradient。
  2. 运行一个最小 autograd 例子。
  3. 打印梯度结果。
- 详细学习资料：
  - PyTorch Learn the Basics：目录中明确包含 Autograd 和 Optimization。
  - 深度学习计划文件：要求覆盖损失函数、训练与推理的零基础解释。
- 实践内容：
  - 写一个简单表达式并执行 `backward()`。
  - 记录“为什么会得到这个梯度”的人话解释。
- 建议产出：`autograd_demo.py` + `day25-gradient-notes.md`

### Day 26：第一个最小神经网络与训练流程

- 学习目标：理解输入、层、输出、参数、训练循环之间的关系。
- 任务安排：
  1. 认识 `nn.Module` 的作用。
  2. 跑通官方 beginner 网络示例的简化版。
  3. 观察 loss 的变化。
- 详细学习资料：
  - PyTorch Learn the Basics：作为总入口。
  - 深度学习计划文件：要求覆盖神经网络、训练与推理、过拟合等基础概念。
- 实践内容：
  - 写一个最小两层网络。
  - 打印训练过程中的若干 loss 值。
- 建议产出：`first_nn.py`

### Day 27：训练 vs 推理 与最小 demo 整合

- 学习目标：分清训练和推理的不同目标，并把 Week 4 内容串成一个最小 demo。
- 任务安排：
  1. 区分训练阶段和预测阶段。
  2. 用训练好的模型做一次推理。
  3. 整理 demo README。
- 详细学习资料：
  - PyTorch Learn the Basics。
  - PyTorch Start Locally：用于回查环境问题。
- 实践内容：
  - 跑一个最小分类或回归 demo。
  - 写 README 说明输入、输出和运行方法。
- 建议产出：`mini-dl-demo/`

### Day 28：系统课程 4——全课程总复盘与综合练习

- 学习目标：把 4 周内容连成一条完整技能链，并明确下一阶段路线。
- 任务安排：
  1. 画课程知识地图：Linux → Git → Python → Cursor → 深度学习。
  2. 回顾每周阶段成果。
  3. 完成最终综合练习与结营总结。
- 详细学习资料：
  - 回看本课程全部主资料。
  - 使用 Week 1~4 的回顾文档完成串联。
- 实践内容：
  - 提交一个包含以下内容的总结仓库或总结目录：
    - Linux 命令笔记
    - Git/GitHub 练习仓库
    - Python 小项目
    - Cursor 提示词与误区总结
    - NumPy / PyTorch demo
  - 用 500~1000 字说明：我现在会什么、不会什么、下一步学什么。
- 建议产出：`graduation-review.md`

## 八、每周阶段成果目标

### Week 1 成果
- 能说清路径、目录、权限、SSH、Remote-SSH 的基础概念。
- 能独立完成命令行基础操作与一份 SSH config 模板。

### Week 2 成果
- 能独立创建 Git 仓库、提交、分支、合并、推送到 GitHub。
- 能完成 issue + PR 的最小协作闭环。

### Week 3 成果
- 能写基础 Python 脚本。
- 能使用 Cursor 辅助完成一个小工具，并知道如何验证 AI 输出。

### Week 4 成果
- 能解释数组、张量、loss、gradient、训练、推理的最小直觉。
- 能跑通一个 CPU 环境下的最小 PyTorch demo。

## 九、资料选用规则

### 9.1 主资料优先级

1. 已在项目内调研中完成零基础适配说明的资料。
2. 官方 beginner / basics / tutorial 文档。
3. 可用于补坑的经验帖与教程帖。

### 9.2 每日资料区块格式

后续正式 Markdown 教程应为每一天单独维护“资料来源”区块，建议格式：

```md
## 资料来源
- 主资料：标题 + URL + 用途说明
- 补充资料：标题 + URL + 用途说明
- 校验资料：标题 + URL + 用途说明
```

### 9.3 多 Agent 并行拆分建议

- Agent A：Week 1 每日正文撰写
- Agent B：Week 2 每日正文撰写
- Agent C：Week 3 每日正文撰写
- Agent D：Week 4 每日正文撰写
- Agent E：统一资料来源区块与链接校验
- Agent F：统一系统课程、术语表、阶段成果与最终统稿

## 十、验收检查清单

- 是否完整覆盖 28 天、4 周。
- 是否第 7/14/21/28 天均为系统课程。
- 是否每天都包含：学习目标、任务安排、详细学习资料、实践内容。
- 是否符合零基础递进：Week 1 基础环境，Week 2 协作，Week 3 编程与 AI，Week 4 深度学习。
- 是否每周都有可交付的阶段成果。
- 是否资料区块可追溯到文件路径或 URL。
- 是否结构适合后续拆成 Markdown 教程正文。

## Provenance

本文件中的周主题、日安排与资料用途来自以下证据链：

1. 项目内文件：
   - `projects/zero-basics-plan/analysis/2026-03-26-vscode-linux-beginner-resource-survey.md`
   - `projects/zero-basics-plan/plans/基于上述调研结果-设计一个-28-天-4-周的完整课程大纲-每天有学习目标-任务安排-详细学习资料-实践内容-每周末安排.md`
   - `projects/zero-basics-plan/plans/调研并整理基础深度学习入门所需的前置知识-核心概念-学习路径与适合零基础的中文资料-最终汇总为28天四周课程大纲-包含每.md`
   - `projects/zero-basics-plan/plans/最终汇总为-markdown-文档结构方案-要求内容包含每日教程正文框架-资料来源区块-每周系统课程安排-学习顺序说明与.md`
2. 本次会话 `web_fetch` 校验：
   - `https://docs.python.org/3/tutorial/`
   - `https://git-scm.com/book/en/v2`
   - `https://docs.github.com/en/get-started/start-your-journey/hello-world`
   - `https://docs.github.com/en/get-started/using-git/about-git`
   - `https://docs.github.com/en/get-started/git-basics/set-up-git`
   - `https://code.visualstudio.com/docs/remote/ssh`
   - `https://code.visualstudio.com/docs/python/python-tutorial`
   - `https://cursor.com/learn/agents`
   - `https://cursor.com/learn/working-with-agents`
   - `https://numpy.org/doc/stable/user/absolute_beginners.html`
   - `https://docs.pytorch.org/tutorials/beginner/basics/intro.html`
   - `https://docs.pytorch.org/get-started/locally/`
   - `https://learngitbranching.js.org/`
   - `https://overthewire.org/wargames/bandit/`
   - `https://linuxcommand.org/lc3_learning_the_shell.php`
