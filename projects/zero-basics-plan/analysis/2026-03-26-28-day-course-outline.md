# 28 天零基础课程总路线（Markdown 教程初稿）

更新日期：2026-03-26
适用对象：能正常使用电脑、但对 Linux / Git / GitHub / AI 编程工具 / 深度学习仍处于入门阶段的学习者
建议节奏：每天 60–120 分钟；周末系统课 120–180 分钟

## 课程目标

28 天后，学习者应完成以下最小闭环：

1. 能用 VS Code Remote SSH 连接 Linux 主机并完成基础远程开发。
2. 能独立完成 Linux 常见文件、权限、进程、网络与 SSH 操作。
3. 能使用 Git 与 GitHub 完成本地版本管理、远程同步、分支开发与 Pull Request。
4. 能理解 Vibe Coding 的适用边界，知道如何把 AI 工具用于需求拆解、代码生成、验证与修正。
5. 能使用 Cursor / Claude Code 类 AI 编程工作流做小型功能开发与代码阅读。
6. 能理解深度学习最基础的概念：数据、张量、模型、训练、推理，并跑通一个最小实验。

## 产出边界

本路线聚焦：课程路线设计、学习任务安排、练习路径、资料映射与 Markdown 教程结构。

本路线**不包含**：录播视频制作、题库平台开发、完整在线实验平台、大规模模型训练部署、复杂数学推导课程。

## 学习前准备

- 本地电脑：Windows / macOS / Linux 均可
- 建议准备一个可 SSH 登录的 Linux 环境：云主机、家里闲置设备、虚拟机均可
- 安装 VS Code
- 准备 GitHub 账号
- 第 4 周建议有 Python 3 环境

## 并行调研汇总方法

本总路线依赖以下资料类别交叉整理：

- 官方文档：VS Code Docs、Git docs、GitHub Docs、Cursor Docs、PyTorch Tutorials
- 长期维护教程：Linux Journey、Ubuntu Tutorials、DigitalOcean Tutorials
- AI 编程工作流文档：Claude Code Docs、Cursor Docs
- 社区补充：用于理解术语传播与案例，但不作为唯一依据

筛选标准：权威性、时效性、初学者可执行性、可复现性、与本路线主题的贴合度。

## 四周总览

| 周次 | 阶段目标 | 主要主题 | 周末系统课产出 |
|---|---|---|---|
| 第 1 周 | 打通环境与基础命令 | VS Code Remote SSH、Linux 入门、文件与目录 | 完成远程开发环境连通与命令基础复盘 |
| 第 2 周 | 建立服务器操作与版本管理基础 | Linux 权限/进程/SSH、Git 基础、远程仓库 | 完成个人仓库同步与命令实践清单 |
| 第 3 周 | 建立协作与 AI 编程工作流 | GitHub 协作、PR、项目阅读、Cursor、Claude Code 类工作流 | 完成一次 AI 辅助的小功能开发或代码阅读报告 |
| 第 4 周 | 完成深度学习入门与综合实战 | 深度学习基础、训练/推理、Vibe Coding 综合应用 | 完成最小深度学习实验与结课作品说明 |

---

# 第 1 周：环境搭建 + Linux 入门

## Day 1｜认识课程、安装工具、准备 Linux 环境

### 学习目标
- 明确 28 天路线和最终产出。
- 安装 VS Code，并准备一个可 SSH 登录的 Linux 环境。
- 理解“本地电脑 + 远程 Linux + 编辑器”的基本关系。

### 任务安排
- 阅读本教程总览。
- 安装 VS Code。
- 准备 Linux 主机：云服务器、虚拟机或局域网机器。
- 记录主机 IP、用户名、认证方式。

### 操作步骤
1. 安装 VS Code。
2. 确认 Linux 主机能联网并开启 SSH 服务。
3. 在本地终端测试 `ssh 用户名@IP` 是否可连通。
4. 建立自己的课程笔记文件夹，记录环境信息。

### 建议输出物
- `day1-environment-notes.md`
- 一份环境信息清单（主机、系统版本、登录方式）

### 推荐资料
- VS Code 文档：Remote Development using SSH  
  https://code.visualstudio.com/docs/remote/ssh
- Ubuntu 教程：The Linux command line for beginners  
  https://ubuntu.com/tutorials/command-line-for-beginners

---

## Day 2｜配置 VS Code Remote SSH

### 学习目标
- 会安装 Remote SSH 扩展。
- 能从 VS Code 远程连接 Linux 主机。
- 理解 SSH config 的基本写法。

### 任务安排
- 安装 Remote SSH 扩展。
- 在 VS Code 中添加一条 SSH Host 配置。
- 用图形界面连上远程主机并打开远程目录。

### 操作步骤
1. 在 VS Code 扩展市场安装 Remote - SSH。
2. 打开 SSH config，填写 Host、HostName、User、Port。
3. 在 VS Code 中选择“Connect to Host”。
4. 成功后打开远程 Home 目录。
5. 记录首次连接遇到的问题，如 host key、权限、密码登录。

### 建议输出物
- `~/.ssh/config` 中新增一条可用配置
- 截图或笔记证明 VS Code 已连接远程主机

### 推荐资料
- VS Code 文档：Remote Development using SSH  
  https://code.visualstudio.com/docs/remote/ssh
- DigitalOcean：SSH Essentials  
  https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys

---

## Day 3｜命令行入门：pwd、ls、cd、mkdir、touch

### 学习目标
- 会打开终端并在目录间移动。
- 理解绝对路径、相对路径、当前目录。
- 能创建目录和文件。

### 任务安排
- 在远程 Linux 终端中练习基础命令。
- 新建课程练习目录。
- 整理一份“我已经会的命令”清单。

### 操作步骤
1. 打开远程终端，执行 `pwd` 查看当前位置。
2. 用 `ls` / `ls -la` 查看目录内容。
3. 用 `cd` 在 `~`、`/tmp`、课程目录之间切换。
4. 用 `mkdir zero-basics`、`touch notes.txt` 建立练习空间。
5. 删除测试文件并再次创建，形成肌肉记忆。

### 建议输出物
- `linux-basic-commands-day3.md`

### 推荐资料
- Ubuntu：The Linux command line for beginners  
  https://ubuntu.com/tutorials/command-line-for-beginners
- Linux Journey：Command Line  
  https://linuxjourney.com/

---

## Day 4｜查看文件与编辑文本：cat、less、cp、mv、rm、nano/vim

### 学习目标
- 能查看文本内容并完成基础编辑。
- 理解复制、移动、删除的区别。
- 知道命令行删除不可轻易撤销。

### 任务安排
- 新建多个文本文件并练习查看、复制、重命名。
- 选择一个命令行编辑器完成 5 行笔记。
- 记录“危险命令”注意事项。

### 操作步骤
1. 用 `cat`、`less` 查看文件。
2. 用 `cp` 复制笔记，用 `mv` 改名。
3. 用 `rm` 删除测试文件，确认删除效果。
4. 用 `nano` 或 `vim` 修改文件内容。
5. 总结：什么时候该用 VS Code，什么时候直接用终端编辑器。

### 建议输出物
- `day4-file-operations.txt`

### 推荐资料
- Linux Journey：Command Line / Text-Fu  
  https://linuxjourney.com/
- Ubuntu：The Linux command line for beginners  
  https://ubuntu.com/tutorials/command-line-for-beginners

---

## Day 5｜理解 Linux 文件系统与隐藏文件

### 学习目标
- 知道 `/`、`/home`、`/etc`、`/var`、`/tmp` 等常见目录用途。
- 理解隐藏文件与配置文件的意义。
- 初步接触 `.ssh`、`.bashrc` 这类用户配置。

### 任务安排
- 浏览关键系统目录。
- 查看家目录中的隐藏文件。
- 记录 10 个常见目录或配置项用途。

### 操作步骤
1. `cd /` 后查看顶层目录。
2. 进入 `/home`、`/etc`、`/var/log`，只读浏览。
3. 回到用户目录，执行 `ls -la` 查看隐藏文件。
4. 用 `cat ~/.bashrc | head` 浏览配置。
5. 建立“目录用途表”。

### 建议输出物
- `day5-filesystem-map.md`

### 推荐资料
- Linux Journey：The Filesystem  
  https://linuxjourney.com/
- Ubuntu 教程同上

---

## Day 6｜命令组合：管道、重定向、grep、history

### 学习目标
- 理解把命令串起来的思路。
- 会使用 `|`、`>`、`>>`、`grep`、`history`。
- 能从命令输出中过滤信息。

### 任务安排
- 在日志或文本里搜索关键词。
- 把命令输出重定向到文件。
- 复盘本周已使用命令。

### 操作步骤
1. 执行 `history` 查看历史命令。
2. 用 `ls -la > filelist.txt` 保存输出。
3. 用 `cat filelist.txt | grep ssh` 过滤结果。
4. 用 `echo "today learned" >> notes.txt` 追加内容。
5. 归纳：为什么命令行适合批量操作。

### 建议输出物
- `day6-command-pipeline.md`

### 推荐资料
- Ubuntu：The Linux command line for beginners  
  https://ubuntu.com/tutorials/command-line-for-beginners
- Linux Journey：Text-Fu  
  https://linuxjourney.com/

---

## Day 7｜系统课程 1：远程开发环境与 Linux 基础复盘

### 系统课程目标
- 串起“SSH 登录 → VS Code Remote SSH → 终端基础操作”。
- 检查学习者是否已具备后续 Git 和 AI 编程的环境前提。

### 系统课程内容
- 复盘 SSH、VS Code Remote SSH、路径、文件、终端、基础命令。
- 演示一次完整流程：本地打开 VS Code → 远程登录 → 新建项目目录 → 写一份 README。
- 总结常见报错：SSH 连不上、权限问题、host key 提示、路径混乱。

### 练习任务
- 在远程主机创建 `week1-demo/README.md`。
- 用 VS Code 编辑并保存。
- 在终端中查看、复制、移动该文件。

### 复盘作业
- 写一份《我已经会的 Linux/远程开发操作清单》。
- 给自己打分：环境连通、目录操作、文本处理三个维度各 1–5 分。

### 建议输出物
- `week1-review.md`

---

# 第 2 周：Linux 进阶 + Git / GitHub 基础

## Day 8｜用户、权限与 chmod/chown 基础

### 学习目标
- 理解用户、用户组、rwx 权限。
- 能看懂 `-rw-r--r--` 这类权限表示。
- 会使用 `chmod` 与 `chown` 的基础形式。

### 任务安排
- 查看文件权限。
- 修改测试文件权限。
- 理解为什么不应该滥用 `777`。

### 操作步骤
1. 用 `ls -l` 查看权限位。
2. 创建测试文件并执行 `chmod 644 test.txt`。
3. 观察可读可写可执行变化。
4. 了解 `chown` 的作用，只在测试范围内使用。
5. 记录权限误用风险。

### 建议输出物
- `day8-permissions.md`

### 推荐资料
- Linux Journey：Permissions  
  https://linuxjourney.com/

---

## Day 9｜进程与任务管理：ps、top、kill、jobs

### 学习目标
- 知道“进程”是什么。
- 能查看正在运行的程序。
- 理解前台/后台任务和结束进程的基本方法。

### 任务安排
- 使用 `ps`、`top` 查看系统状态。
- 运行一个后台任务并结束它。
- 记录 PID 的含义。

### 操作步骤
1. 执行 `ps aux | head`。
2. 执行 `top` 或可选 `htop` 观察资源使用。
3. 用 `sleep 300 &` 建立后台任务。
4. 用 `jobs` 查任务，用 `kill` 结束。
5. 记录不要随意 kill 系统进程。

### 建议输出物
- `day9-processes.md`

### 推荐资料
- Linux Journey：Processes / Process Utilization  
  https://linuxjourney.com/

---

## Day 10｜SSH 常用操作：密钥登录、scp、rsync 思维

### 学习目标
- 知道密码登录和密钥登录的区别。
- 会使用 `scp` 传文件。
- 理解 `rsync` 适合做同步而不是简单复制。

### 任务安排
- 生成一对 SSH key。
- 把公钥写入目标主机。
- 用 `scp` 在本地与远程之间传一个文件。

### 操作步骤
1. 执行 `ssh-keygen` 生成密钥。
2. 配置公钥登录。
3. 用 `scp` 上传一份文本文件。
4. 理解 `known_hosts` 的作用。
5. 记录：为什么生产环境更推荐密钥认证。

### 建议输出物
- `day10-ssh-practice.md`

### 推荐资料
- DigitalOcean：SSH Essentials  
  https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys
- VS Code Remote SSH 文档  
  https://code.visualstudio.com/docs/remote/ssh

---

## Day 11｜Git 是什么：仓库、提交、历史

### 学习目标
- 理解 Git 是版本控制系统。
- 认识工作区、暂存区、提交的关系。
- 会初始化仓库并完成第一次提交。

### 任务安排
- 建一个练习仓库。
- 添加 README。
- 完成 `init → add → commit`。

### 操作步骤
1. 进入课程目录，执行 `git init`。
2. 新建 `README.md`。
3. 用 `git status` 看变化。
4. 用 `git add .` 暂存。
5. 用 `git commit -m "first commit"` 提交。

### 建议输出物
- 本地 Git 仓库 1 个

### 推荐资料
- Git Tutorial  
  https://git-scm.com/docs/gittutorial
- GitHub Docs：About GitHub and Git  
  https://docs.github.com/en/get-started/start-your-journey/about-github-and-git
- GitHub Docs：Set up Git  
  https://docs.github.com/en/get-started/git-basics/set-up-git

---

## Day 12｜Git 常见操作：status、diff、log、restore

### 学习目标
- 能看懂仓库当前状态。
- 会比较修改前后差异。
- 会查看提交历史并撤销工作区修改。

### 任务安排
- 修改已有文件并观察状态变化。
- 用 `git diff` 看差异。
- 尝试恢复未提交修改。

### 操作步骤
1. 修改 `README.md`。
2. 用 `git status` 和 `git diff` 查看变化。
3. 再提交一次变更。
4. 用 `git log --oneline` 查看历史。
5. 对测试文件练习 `git restore`。

### 建议输出物
- `day12-git-basics.md`

### 推荐资料
- Git Tutorial  
  https://git-scm.com/docs/gittutorial

---

## Day 13｜连接 GitHub：创建远程仓库并 push

### 学习目标
- 理解本地仓库与远程仓库的关系。
- 能把本地提交推送到 GitHub。
- 知道 remote、origin、main 的含义。

### 任务安排
- 在 GitHub 新建仓库。
- 给本地仓库添加 remote。
- 完成第一次 `push`。

### 操作步骤
1. 在 GitHub 创建一个新仓库。
2. 执行 `git remote add origin <url>`。
3. 执行 `git branch -M main`。
4. 执行 `git push -u origin main`。
5. 在网页确认仓库内容已同步。

### 建议输出物
- 一个公开或私有的课程练习仓库

### 推荐资料
- GitHub Docs：About remote repositories  
  https://docs.github.com/en/get-started/git-basics/about-remote-repositories
- GitHub Docs：Pushing commits to a remote repository  
  https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository

---

## Day 14｜系统课程 2：Linux 实战 + Git 基础串联

### 系统课程目标
- 把 Linux 操作与 Git 使用打通，形成最小开发工作流。

### 系统课程内容
- 复盘权限、进程、SSH 文件传输、Git 初始化、提交、推送。
- 演示完整闭环：在远程 Linux 上改文件 → 本地或远程提交 → 推送到 GitHub。
- 讲解常见错误：未配置用户名邮箱、push 被拒、权限不足、分支混乱。

### 练习任务
- 重新创建一个小仓库，加入 2 个文件并完成两次提交。
- 把仓库推送到 GitHub。

### 复盘作业
- 写一篇《从终端到 GitHub 的一条完整工作流》。

### 建议输出物
- `week2-review.md`

---

# 第 3 周：GitHub 协作 + Cursor / AI 编程工作流

## Day 15｜GitHub Flow：分支、提交、Pull Request 的全貌

### 学习目标
- 理解为什么协作要用分支。
- 知道 Pull Request 是什么。
- 建立“提改动—审查—合并”的基本心智模型。

### 任务安排
- 阅读 GitHub Hello World。
- 在现有仓库创建 feature branch。
- 准备一次小改动。

### 操作步骤
1. 阅读 GitHub Hello World 流程。
2. 用 `git switch -c feature/update-readme` 创建分支。
3. 修改 README。
4. 提交并推送分支。
5. 在 GitHub 界面发起 PR。

### 建议输出物
- 第一个 Pull Request 链接

### 推荐资料
- GitHub Docs：Hello World  
  https://docs.github.com/en/get-started/start-your-journey/hello-world
- GitHub Docs：Pull requests documentation  
  https://docs.github.com/en/pull-requests

---

## Day 16｜分支合并、冲突与代码评审基础

### 学习目标
- 了解 merge conflict 为何出现。
- 会在简单场景下解决冲突。
- 理解 Review 的关注点：正确性、可读性、风险。

### 任务安排
- 模拟两个分支修改同一段文本。
- 人工解决一次冲突。
- 给自己的 PR 写一段自我说明。

### 操作步骤
1. 在 main 与 feature 上分别修改同一行文本。
2. 执行 merge 或在 GitHub 上触发冲突。
3. 根据冲突标记手动修正。
4. 再次提交并完成合并。
5. 写下“冲突解决 3 步法”。

### 建议输出物
- `day16-merge-conflict.md`

### 推荐资料
- GitHub Docs：Resolve merge conflicts  
  https://docs.github.com/en/pull-requests

---

## Day 17｜阅读项目：README、目录结构、Issue、Commit 历史

### 学习目标
- 学会从陌生仓库提取关键信息。
- 能描述一个项目的目标、结构与入口。
- 为后续 AI 辅助理解代码库做准备。

### 任务安排
- 随机选择一个中小型开源仓库。
- 阅读 README、目录结构、最近提交。
- 输出一页项目阅读笔记。

### 操作步骤
1. 浏览 README、安装说明、使用说明。
2. 看根目录有哪些文件夹。
3. 看最近 10 条 commit 标题。
4. 看 3 个 issue 或 PR 标题。
5. 总结项目功能、入口文件、依赖、协作方式。

### 建议输出物
- `day17-project-reading.md`

### 推荐资料
- GitHub Docs：About branches / About pull requests / collaborative docs  
  https://docs.github.com/en/pull-requests

---

## Day 18｜Cursor 入门：它是什么、适合做什么

### 学习目标
- 理解 Cursor 是 AI 优先的代码编辑器环境。
- 了解其文档结构、主要功能入口与典型使用场景。
- 明确它不是“自动替你负责正确性”的工具。

### 任务安排
- 浏览 Cursor Docs。
- 列出 5 个你最可能用到的能力。
- 与 VS Code 的基础使用方式做对比。

### 操作步骤
1. 阅读 Cursor Docs 首页与学习导航。
2. 记录 Chat / Agent / 编辑 / 项目上下文等概念。
3. 写下适合新手的 3 个用法：解释代码、生成脚手架、修改小功能。
4. 写下不应盲用的场景：安全、关键逻辑、大范围重构不验证。

### 建议输出物
- `day18-cursor-overview.md`

### 推荐资料
- Cursor Docs  
  https://cursor.com/docs

---

## Day 19｜AI 编程工作流入门：探索、计划、实现、验证

### 学习目标
- 理解 AI 辅助编程的基本闭环。
- 学会把需求拆成可交给 AI 的小问题。
- 知道“先读代码，再计划，再改，再验证”的顺序。

### 任务安排
- 阅读 Claude Code 的 common workflows / best practices。
- 总结一份 AI 编程四步流程。
- 设计一个小功能任务给 AI 处理。

### 操作步骤
1. 阅读 Common workflows 中的 codebase overview、bug fix、refactor 部分。
2. 阅读 Best practices 中的 explore first, then plan, then code。
3. 把“加一个命令行参数”之类小需求拆成步骤。
4. 写出适合发给 AI 的 prompt 模板。
5. 列出验证方式：运行、测试、阅读 diff、回归检查。

### 建议输出物
- `day19-ai-workflow.md`

### 推荐资料
- Claude Code Docs：Common workflows  
  https://code.claude.com/docs/en/common-workflows
- Claude Code Docs：Best practices  
  https://code.claude.com/docs/en/best-practices

---

## Day 20｜Vibe Coding：何时适用，何时必须收紧

### 学习目标
- 理解 Vibe Coding 更接近“快速原型和高频试错”，不是放弃工程纪律。
- 能区分原型、练习、小工具与生产级项目的不同要求。
- 建立“AI 生成 ≠ 已验证”的底线。

### 任务安排
- 总结 Vibe Coding 的收益与风险。
- 选择一个小需求，让 AI 帮你生成初版。
- 自己执行验证与修正。

### 操作步骤
1. 先写清楚目标、输入、输出、限制条件。
2. 让 AI 生成最小版本。
3. 手动运行并记录报错。
4. 让 AI 基于错误修复。
5. 最后自己检查可读性、边界条件与命名。

### 建议输出物
- `day20-vibe-coding-notes.md`

### 推荐资料
- Claude Code Docs：Best practices  
  https://code.claude.com/docs/en/best-practices
- Cursor Docs  
  https://cursor.com/docs
- Vibe Coding 传播线索搜索记录（社区材料只作补充，不作唯一依据）

---

## Day 21｜系统课程 3：GitHub 协作与 AI 编程工作流综合实践

### 系统课程目标
- 形成“读仓库 → 建分支 → AI 辅助修改 → 自测 → PR”的可重复流程。

### 系统课程内容
- 复盘 GitHub Flow、PR、项目阅读、Cursor / Claude Code 工作流。
- 演示一个小功能开发：需求说明 → AI 产出初稿 → 人工验证 → 提交 PR。
- 总结常见失误：上下文不足、提示过宽、没验证直接提交、PR 描述含糊。

### 练习任务
- 在你的练习仓库中增加一个小功能或一段文档增强。
- 使用 AI 至少参与 1 个环节：解释、生成、重构或审查。

### 复盘作业
- 写一篇《我当前的 AI 编程工作流》并附 PR 链接。

### 建议输出物
- `week3-review.md`

---

# 第 4 周：基础深度学习 + 综合结课

## Day 22｜深度学习到底在做什么：数据、特征、模型、训练、推理

### 学习目标
- 建立深度学习最小概念框架。
- 区分训练与推理。
- 了解为什么需要数据、损失函数和优化。

### 任务安排
- 阅读 PyTorch 60 Minute Blitz 概览。
- 自己写出 10 个关键词解释。
- 用生活例子理解分类任务。

### 操作步骤
1. 阅读深度学习入门部分。
2. 记录关键词：dataset、tensor、model、epoch、loss、optimizer、inference 等。
3. 用“猫狗分类”或“手写数字识别”解释训练与预测。
4. 把概念整理成一页图。

### 建议输出物
- `day22-dl-concepts.md`

### 推荐资料
- PyTorch Tutorials：Deep Learning with PyTorch: A 60 Minute Blitz  
  https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

---

## Day 23｜Python / PyTorch 环境与张量入门

### 学习目标
- 准备最小 Python 深度学习环境。
- 理解张量是多维数组。
- 能在交互环境里创建简单 tensor。

### 任务安排
- 安装 PyTorch 或进入可用环境。
- 执行几个张量操作。
- 记录 shape、dtype、device 等概念。

### 操作步骤
1. 准备 Python 环境。
2. 按 PyTorch 官方教程安装依赖。
3. 运行创建张量、加法、reshape 的示例。
4. 观察输出形状。
5. 总结：张量和普通列表的差异。

### 建议输出物
- `day23-tensor-practice.ipynb` 或 `.py`

### 推荐资料
- PyTorch 60 Minute Blitz  
  https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

---

## Day 24｜最小神经网络直觉：输入、层、输出、损失

### 学习目标
- 理解“模型 = 一组可学习参数”。
- 初步认识前向传播与损失计算。
- 能从直觉上理解训练在“调参数”。

### 任务安排
- 阅读最小网络示意。
- 跑通一个官方示例。
- 记录你对 loss 的直觉理解。

### 操作步骤
1. 阅读 PyTorch 教程中的网络与训练示例。
2. 看一遍模型定义、前向计算、loss 输出。
3. 观察训练前后损失变化。
4. 用自己的话解释“为什么训练后会更好”。

### 建议输出物
- `day24-network-intuition.md`

### 推荐资料
- PyTorch 60 Minute Blitz  
  https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

---

## Day 25｜训练与推理：一次最小实验

### 学习目标
- 亲手跑完一次最小训练与推理流程。
- 知道评估不是只看“跑没跑起来”。
- 能记录实验输入、输出与结果。

### 任务安排
- 跑一个最小分类示例。
- 保存训练日志或截图。
- 对一条样本做推理。

### 操作步骤
1. 运行教程中的训练代码。
2. 记录 epoch、loss 变化。
3. 对一条测试样本执行推理。
4. 观察输出类别或概率。
5. 写明实验环境、依赖和运行结果。

### 建议输出物
- `day25-mini-training-report.md`

### 推荐资料
- PyTorch 60 Minute Blitz  
  https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

---

## Day 26｜把 AI 编程工具用于深度学习小实验

### 学习目标
- 学会让 AI 帮你解释训练脚本、排查错误、补充注释。
- 理解 AI 适合辅助学习，但不能替代实验核验。

### 任务安排
- 让 AI 解释一段 PyTorch 代码。
- 让 AI 帮你把训练脚本改得更易读。
- 自己验证改动是否仍可运行。

### 操作步骤
1. 把训练脚本交给 AI，要求逐段解释。
2. 要求 AI 增加注释或拆函数。
3. 再次运行脚本。
4. 比较修改前后差异。
5. 总结哪些地方 AI 真正帮到了你。

### 建议输出物
- `day26-ai-for-dl.md`

### 推荐资料
- Cursor Docs  
  https://cursor.com/docs
- Claude Code Docs：Common workflows / Best practices  
  https://code.claude.com/docs/en/common-workflows  
  https://code.claude.com/docs/en/best-practices

---

## Day 27｜结课项目日：综合小项目

### 学习目标
- 串联前 27 天内容，完成一个最小结课项目。
- 同时体现环境、版本管理、AI 辅助与深度学习入门认知。

### 项目建议（二选一）
1. **开发流程型项目**：
   - 在远程 Linux 上建立一个小型 Python 项目
   - 用 Git 管理版本
   - 用 GitHub 发起 PR
   - 用 AI 辅助补全 README、注释和小功能
2. **深度学习体验型项目**：
   - 跑通一个最小 PyTorch 分类示例
   - 用 AI 帮你解释代码和错误
   - 用 GitHub 记录实验过程

### 操作步骤
1. 明确项目目标。
2. 列出输入、输出与目录结构。
3. 建仓库并分支开发。
4. AI 辅助完成一部分实现或解释。
5. 提交结果并写项目说明。

### 建议输出物
- 一个课程结课仓库
- `final-project-report.md`

### 推荐资料
- 前 3 周所有核心资料按需回看

---

## Day 28｜系统课程 4：结课复盘、知识地图与后续进阶路线

### 系统课程目标
- 对 28 天全部内容做体系化收束。
- 帮学习者形成自己的后续学习路径。

### 系统课程内容
- 回顾四条主线：
  1. 远程连接与开发环境
  2. Linux 基础与服务器操作
  3. Git / GitHub 协作
  4. AI 编程与深度学习入门
- 展示一个完整知识地图：环境 → 操作系统 → 版本管理 → 协作 → AI 工具 → 模型实验。
- 说明后续进阶方向：
  - Linux 进阶管理
  - Git 团队协作规范
  - 更系统的软件工程实践
  - 更完整的深度学习课程

### 结课作业
- 提交你的最终仓库或实验记录。
- 写一篇《28 天后我已经具备的能力》。
- 列出接下来 30 天的进阶计划。

### 建议输出物
- `week4-final-review.md`
- `next-30-days-plan.md`

---

# 参考资料总表

## 环境与远程连接
- VS Code Docs: Remote Development using SSH  
  https://code.visualstudio.com/docs/remote/ssh
- DigitalOcean: SSH Essentials: Working with SSH Servers, Clients, and Keys  
  https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys

## Linux 基础
- Ubuntu Tutorials: The Linux command line for beginners  
  https://ubuntu.com/tutorials/command-line-for-beginners
- Linux Journey  
  https://linuxjourney.com/

## Git / GitHub
- Git Tutorial  
  https://git-scm.com/docs/gittutorial
- GitHub Docs: About GitHub and Git  
  https://docs.github.com/en/get-started/start-your-journey/about-github-and-git
- GitHub Docs: Hello World  
  https://docs.github.com/en/get-started/start-your-journey/hello-world
- GitHub Docs: Pull requests documentation  
  https://docs.github.com/en/pull-requests
- GitHub Docs: Set up Git  
  https://docs.github.com/en/get-started/git-basics/set-up-git
- GitHub Docs: About remote repositories  
  https://docs.github.com/en/get-started/git-basics/about-remote-repositories
- GitHub Docs: Pushing commits to a remote repository  
  https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository

## Cursor / AI 编程工作流
- Cursor Docs  
  https://cursor.com/docs
- Claude Code Docs: Common workflows  
  https://code.claude.com/docs/en/common-workflows
- Claude Code Docs: Best practices  
  https://code.claude.com/docs/en/best-practices

## 深度学习入门
- PyTorch Tutorials: Deep Learning with PyTorch: A 60 Minute Blitz  
  https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

## 使用建议
- 官方文档优先作为主线资料。
- 社区文章可用于补充案例，但不替代官方路径。
- AI 工具相关内容变化较快，后续扩写正式教程时需再次检查版本与界面。