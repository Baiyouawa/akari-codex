# Linux 零基础入门资料调研（文件系统 / 常用命令 / 权限 / 软件安装 / Shell / 实战练习）

日期：2026-03-26
项目：`projects/zero-basics-plan`
任务：调研 Linux 零基础入门资料：覆盖文件系统、常用命令、权限、软件安装、Shell 基础、实战练习，筛选适合初学者的高质量中文或英文资料并记录来源。

## 调研范围与筛选标准

本次只纳入满足以下至少一项的资料：

1. **面向新手**：页面标题或正文明确说明是 beginner / basics / 基础教程 / 入门。
2. **覆盖任务要求主题**：文件系统、常用命令、权限、软件安装、Shell 基础、实战练习。
3. **可直接访问**：可通过 `web_fetch` 获取正文，或至少可通过搜索结果确认页面定位。
4. **适合作为 28 天课程材料**：教程结构清晰、概念和命令例子足够基础。

## 结论摘要

适合本项目的 Linux 入门资料可以分成 4 类：

1. **主线入门教程**：Ubuntu Desktop 文档、USTC OS Docs Linux 基础教程、LinuxCommand.org。
2. **中文查缺补漏资料**：菜鸟教程的目录管理、权限、apt、Shell、命令大全页面。
3. **进阶但仍适合早期引入的 Shell 思维资料**：MIT Missing Semester 第 1 讲。
4. **实战练习资料**：OverTheWire Bandit。

如果只选最小可用教材组合，建议采用：

- **中文主线**：USTC OS Docs + 菜鸟教程
- **英文主线**：Ubuntu Desktop doc + LinuxCommand.org
- **Shell 提升**：MIT Missing Semester
- **练习主线**：OverTheWire Bandit

## 推荐资料清单

### 1. Ubuntu Desktop documentation: The Linux command line for beginners
- 类型：英文官方入门教程
- URL：https://documentation.ubuntu.com/desktop/en/latest/tutorial/the-linux-command-line-for-beginners/
- 适合程度：**高**
- 难度：**低**
- 覆盖主题：常用命令、终端基本使用、入门路径理解
- 适合原因：标题明确是 “for beginners”，属于 Ubuntu 官方文档，适合作为零基础第一篇英文材料。
- 局限：更偏“终端入门”，对 Shell 脚本和系统化练习覆盖不够深。
- 证据摘录：`web_fetch` 返回标题为 “The Linux command line for beginners - Ubuntu Desktop documentation”。

### 2. USTC OS Docs：Linux 基础教程
- 类型：中文基础教程
- URL：http://home.ustc.edu.cn/~pzw2002/appendix/linux.html
- 适合程度：**高**
- 难度：**低**
- 覆盖主题：路径与文件系统、常用命令、apt、wget、grep、tar、编辑器
- 适合原因：明确写明“面向 Linux 零基础同学”，并给出“预计用时 20~30 分钟”；内容从路径、工作目录、绝对/相对路径讲起，教学顺序很适合 0 基础。
- 局限：是实验配套文档，Shell 脚本部分较弱。
- 证据摘录：`web_fetch` 返回 “本节面向 Linux 零基础同学… 预计用时 20~30 分钟”，目录中含 `ls`/`cd`/`pwd`/`rm`/`mv`/`cp`/`mkdir`/`wget`/`tar`/`apt`/`grep` 等。

### 3. LinuxCommand.org: Learning the Shell
- 类型：英文系统化入门教程
- URL：https://linuxcommand.org/lc3_learning_the_shell.php
- 适合程度：**高**
- 难度：**低-中**
- 覆盖主题：导航、文件操作、命令、I/O 重定向、Expansion、Permissions、Job Control
- 适合原因：站点目录天然就是课程顺序，覆盖从 shell 是什么到 permissions / redirection / expansion，特别适合做第 2 周 Shell 主线教材。
- 局限：英文为主，中文零基础用户需要配套术语解释。
- 证据摘录：`web_fetch` 返回目录包括 “Navigation / Looking Around / Manipulating Files / Working with Commands / I/O Redirection / Expansion / Permissions / Job Control”。

### 4. 菜鸟教程：Linux 文件与目录管理
- 类型：中文命令入门 / 查阅型资料
- URL：https://www.runoob.com/linux/linux-file-content-manage.html
- 适合程度：**高**
- 难度：**低**
- 覆盖主题：文件系统、路径、目录操作、文件复制移动删除
- 适合原因：直接列出 `ls` / `cd` / `pwd` / `mkdir` / `rmdir` / `cp` / `rm` / `mv`，对中文初学者非常友好，适合配合 USTC 文档做命令练习单。
- 局限：解释偏“命令手册化”，需要配套情境化任务。
- 证据摘录：`web_fetch` 返回“Linux 的目录结构为树状结构，最顶级的目录为根目录 /”，并列出处理目录常用命令。

### 5. 菜鸟教程：Linux 文件基本属性
- 类型：中文权限入门资料
- URL：https://www.runoob.com/linux/linux-file-attr-permission.html
- 适合程度：**高**
- 难度：**低**
- 覆盖主题：权限、用户/组、`chmod`、`chown`
- 适合原因：从 `rwx`、owner/group/others 讲起，适合拿来解释权限字符串与最常见的 `chmod/chown`。
- 局限：ACL、sticky bit 等高级主题不是重点，适合基础课，不适合深挖权限模型。
- 证据摘录：`web_fetch` 返回“Linux 系统是一种典型的多用户系统…通常使用 chown 修改所属用户与组，chmod 修改用户的权限”，并解释 `rwx` 与 owner/group/others。

### 6. 菜鸟教程：Linux apt 命令
- 类型：中文软件安装入门资料
- URL：https://www.runoob.com/linux/linux-comm-apt.html
- 适合程度：**高**
- 难度：**低**
- 覆盖主题：软件安装、更新、删除、查询
- 适合原因：把 `apt update` / `apt upgrade` / `apt install` / `apt remove` / `apt search` / `apt show` / `apt autoremove` 串成了最常见的新手工作流，适合第 1 周或第 2 周上手。
- 局限：只覆盖 Debian / Ubuntu 系生态，不适合泛化为所有 Linux 发行版。
- 证据摘录：`web_fetch` 返回“apt（Advanced Packaging Tool）是一个在 Debian 和 Ubuntu 中的 Shell 前端软件包管理器”，并列出常用命令。

### 7. 菜鸟教程：Shell 教程
- 类型：中文 Shell 脚本入门资料
- URL：https://www.runoob.com/linux/linux-shell.html
- 适合程度：**中-高**
- 难度：**低**
- 覆盖主题：Shell 概念、脚本执行、变量、参数、流程控制、函数、重定向
- 适合原因：内容结构完整，适合作为“Shell 脚本最小入门手册”；对 Bash 脚本的第一段代码、执行方式解释很直接。
- 局限：更偏语法手册，不如 Missing Semester 那样强调 shell 思维和命令行工作流。
- 证据摘录：`web_fetch` 返回“Shell 是一个用 C 语言编写的程序… Bash 也是大多数 Linux 系统默认的 Shell”，并给出 `#!/bin/bash` 与 `chmod +x ./test.sh` 示例。

### 8. 菜鸟教程：Linux 命令大全
- 类型：中文命令索引
- URL：https://www.runoob.com/linux/linux-command-manual.html
- 适合程度：**中**
- 难度：**低**
- 覆盖主题：命令检索
- 适合原因：适合做课程附录和查漏补缺，不适合独立作为主教材。
- 局限：偏索引，不适合作为零基础第一手教程。
- 证据摘录：`web_fetch` 返回页面标题为 “Linux 命令大全 | 菜鸟教程”。

### 9. MIT Missing Semester：Course Overview + The Shell
- 类型：英文高质量课程
- URL：https://missing.csail.mit.edu/2020/course-shell/
- 适合程度：**中-高**
- 难度：**中**
- 覆盖主题：shell 思维、命令行生产力、课程练习
- 适合原因：适合在学生已会 `cd/ls/cp/mv` 后引入，帮助理解“为什么要学 shell”和“如何更高效地使用计算机工具”。文中明确说明每讲都有 exercises。
- 局限：密度较高，不适合第一天直接上。
- 证据摘录：`web_fetch` 返回课程介绍中写明 “each lecture includes a set of exercises”，并说明 Topic 1 是 “The Shell”。

### 10. OverTheWire: Bandit
- 类型：英文实战练习 / 闯关式训练
- URL：https://overthewire.org/wargames/bandit/
- 适合程度：**高**
- 难度：**低-中**
- 覆盖主题：命令行练习、查手册、基本文件操作、逐关实践
- 适合原因：站点明确说明 “aimed at absolute beginners”；非常适合作为周末闯关练习，能把命令学习转为任务驱动。
- 局限：是英文环境，且风格偏 CTF / wargame，不适合完全没有英语阅读能力的用户单独使用。
- 证据摘录：`web_fetch` 返回 “The Bandit wargame is aimed at absolute beginners. It will teach the basics…”，并建议使用 `man` 与 `help`。

## 按任务要求映射资料

| 主题 | 首选资料 | 备选资料 | 说明 |
|---|---|---|---|
| 文件系统 / 路径 | USTC OS Docs；菜鸟教程《文件与目录管理》 | Ubuntu command line tutorial | USTC 更适合中文 0 基础；菜鸟适合补命令细节。 |
| 常用命令 | USTC OS Docs；菜鸟教程《文件与目录管理》 | LinuxCommand.org | 中文先建立概念，再用英文教程补 redirection / expansion。 |
| 权限 | 菜鸟教程《文件基本属性》 | LinuxCommand.org；linuxconfig 权限文 | 菜鸟对 `rwx/chmod/chown` 最直观。 |
| 软件安装 | 菜鸟教程《apt 命令》 | USTC OS Docs | 二者都以 Ubuntu/Debian 系为主，适合零基础主流场景。 |
| Shell 基础 | 菜鸟教程《Shell 教程》 | LinuxCommand.org；MIT Missing Semester | 菜鸟适合语法第一步，后两者适合提高。 |
| 实战练习 | OverTheWire Bandit | Missing Semester exercises | Bandit 更像“闯关练手”；Missing Semester 更像“课程作业”。 |

## 最终筛选建议（适合 28 天教程的教材组合）

### A. 中文优先组合
1. USTC OS Docs：Linux 基础教程
2. 菜鸟教程：文件与目录管理
3. 菜鸟教程：文件基本属性
4. 菜鸟教程：apt 命令
5. 菜鸟教程：Shell 教程
6. OverTheWire Bandit（作为实战）

适用人群：完全零基础、中文为主、需要快速建立基础操作能力。

### B. 中英结合组合
1. Ubuntu Desktop: The Linux command line for beginners
2. LinuxCommand.org: Learning the Shell
3. MIT Missing Semester: The Shell
4. 菜鸟教程若干中文补充页
5. OverTheWire Bandit

适用人群：想逐步阅读英文文档，后续要进入开发 / AI / 服务器方向的学习者。

## 对 28 天课程编排的启发

基于本次调研，Linux 部分适合拆成以下结构：

### 第 1 周：认识 Linux 与文件系统
- 路径、根目录、家目录、绝对路径、相对路径
- 常用文件 / 目录命令：`pwd` `ls` `cd` `mkdir` `cp` `mv` `rm`
- 软件安装入门：`apt update` `apt install`

推荐教材：USTC OS Docs + 菜鸟教程《文件与目录管理》《apt 命令》

### 第 2 周：权限与 Shell 入门
- 用户、组、权限字符串
- `chmod` `chown`
- Shell 是什么、如何运行脚本、变量与参数

推荐教材：菜鸟教程《文件基本属性》《Shell 教程》

### 第 3 周：命令行进阶工作流
- I/O 重定向
- expansion
- 通过 `man` / `help` 自助查命令
- shell 作为生产力工具

推荐教材：LinuxCommand.org + MIT Missing Semester

### 第 4 周：综合练习
- 结合真实任务进行文件整理、权限修改、安装工具、执行脚本
- 进行 3~5 关 Bandit 练习

推荐教材：OverTheWire Bandit + 自建练习清单

## 可直接放入课程的练习建议

### 基础练习
1. 在家目录创建 `linux-day1`，其中建立 `notes`、`projects`、`trash` 三个子目录。
2. 用绝对路径和相对路径各进入一次 `notes`。
3. 复制一个文件到 `projects`，再改名。
4. 删除一个空目录与一个非空目录，理解报错差异。

### 权限练习
1. 新建 `hello.sh` 并写入 `echo "hello linux"`。
2. 观察未授权时能否直接执行。
3. 使用 `chmod +x hello.sh` 后再次执行。
4. 用 `ls -l` 解释权限字符串变化。

### 安装练习
1. 执行 `sudo apt update`
2. 搜索一个常见工具：`apt search tree`
3. 查看说明：`apt show tree`
4. 安装并使用：`sudo apt install tree`

### Shell 练习
1. 写一个脚本输出当前目录和当前用户。
2. 用位置参数让脚本打印 “Hello, <name>”。
3. 使用重定向把结果保存到 `output.txt`。

### 闯关练习
1. 注册 / 连接 OverTheWire Bandit。
2. 完成 Level 0→3。
3. 每一关记录“用了什么命令、查了什么文档、踩了什么坑”。

## 不建议单独作为主教材的资料

1. **Linux 命令大全类索引页**：适合作为字典，不适合作为 0 基础主线学习材料。
2. **高密度英文博客**：虽然内容可能正确，但对零基础学习者的术语负担偏高。
3. **仅命令罗列、不讲场景的速查表**：更适合复习，不适合第一轮学习。

## 资料来源与证据链

以下条目均来自本次会话的 `web_search` / `web_fetch`：

1. Ubuntu Desktop documentation — The Linux command line for beginners  
   URL: https://documentation.ubuntu.com/desktop/en/latest/tutorial/the-linux-command-line-for-beginners/
2. USTC OS Docs — Linux 基础教程  
   URL: http://home.ustc.edu.cn/~pzw2002/appendix/linux.html
3. LinuxCommand.org — Learning the Shell  
   URL: https://linuxcommand.org/lc3_learning_the_shell.php
4. 菜鸟教程 — Linux 文件与目录管理  
   URL: https://www.runoob.com/linux/linux-file-content-manage.html
5. 菜鸟教程 — Linux 文件基本属性  
   URL: https://www.runoob.com/linux/linux-file-attr-permission.html
6. 菜鸟教程 — Linux apt 命令  
   URL: https://www.runoob.com/linux/linux-comm-apt.html
7. 菜鸟教程 — Shell 教程  
   URL: https://www.runoob.com/linux/linux-shell.html
8. 菜鸟教程 — Linux 命令大全  
   URL: https://www.runoob.com/linux/linux-command-manual.html
9. MIT Missing Semester — Course Overview + The Shell  
   URL: https://missing.csail.mit.edu/2020/course-shell/
10. OverTheWire — Bandit  
    URL: https://overthewire.org/wargames/bandit/

## 本次产出可供后续任务直接复用的内容

1. 已筛出可做 Linux 模块主线教材的中英文资料。
2. 已按“文件系统 / 命令 / 权限 / 安装 / Shell / 练习”完成主题映射。
3. 已给出适合 28 天课程的 Linux 模块拆分建议。
4. 已给出可直接纳入教程的练习清单。
