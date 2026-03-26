# 第 2 周缺口补齐进度摘要

## 2026-03-26T22:10:00+08:00

### 已完成内容
- 已读取既有计划文件，并锁定验收标准不做修改。
- 已完成项目上下文核对：`AGENTS.md`、仓库 `README.md`、`projects/zero-basics-plan/README.md`、`projects/zero-basics-plan/TASKS.md`、近期项目日志、既有第 2 周调研文档、现有 28 天教程整合稿。
- 已确认本轮不是重做“第 2 周资料调研”，而是补齐当前整合稿中偏薄的 Day 8–14 教程正文，重点补上：
  - Linux 文件系统与路径
  - 文件查看与查找
  - 权限与常见 `Permission denied`
  - 进程与服务状态查看
  - 软件安装与包管理（`apt` + `dnf/yum`）
  - SSH 基础、`known_hosts`、常见报错排查
- 已补抓外部依据，新增可用于正文事实核对的来源：
  - Filesystem Hierarchy Standard 3.0：`https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html`
  - `file-hierarchy(7)`：`https://www.man7.org/linux/man-pages/man7/file-hierarchy.7.html`
  - `apt(8)`：`https://manpages.debian.org/apt`
  - Red Hat DNF commands list：`https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/dnf-commands-list`
  - `ssh(1)`：`https://www.man7.org/linux/man-pages/man1/ssh.1.html`
- 已开始产出可直接写入教程的第 2 周增强版正文，并准备同步更新主教程、项目状态与会话日志。

### 当前里程碑状态
- 已完成：缺口盘点与现有文档比对
- 已完成：第 2 周分天结构确认（Day 8–14）
- 已完成：外部来源补抓与事实核验
- 进行中：写入可直接并入教程的 Day 8–14 增强正文
- 待完成：自审、修正、项目 README / TASKS / session log / git commit

### 关键发现
- 既有 `analysis/2026-03-26-week2-linux-ssh-git-resource-survey.md` 已覆盖第 2 周资料来源，但 `analysis/2026-03-26-28-day-markdown-tutorial.md` 中 Day 8–14 仍偏“提纲式”，尤其缺少文件系统、文件查找、SSH 报错排查和练习答案。
- 计划文件要求本轮输出必须面向零基础读者，且每个模块都要包含“是什么、为什么、怎么做、常见坑、练习题”五类内容，因此仅补链接或调研表不够，必须补教程正文。
- 当前项目 README 中已显式记录“第 2 周扩写时仍建议补充 `systemctl/service` 与 `nohup/tmux`”，本轮可在教程中纳入 `systemctl status` 基础与“长任务保活先知道问题、深入工具后学”的边界说明。

### 证据来源
- 现有主教程：`projects/zero-basics-plan/analysis/2026-03-26-28-day-markdown-tutorial.md`
- 第 2 周调研：`projects/zero-basics-plan/analysis/2026-03-26-week2-linux-ssh-git-resource-survey.md`
- 项目状态：`projects/zero-basics-plan/README.md`、`projects/zero-basics-plan/TASKS.md`
