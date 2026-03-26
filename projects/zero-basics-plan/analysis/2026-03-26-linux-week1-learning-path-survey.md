# 2026-03-26 Linux 零基础入门学习路径调研（第 1 周资料筛选）

- 日期: 2026-03-26
- 任务: 调研 Linux 零基础入门学习路径，整理文件系统、常用命令、权限、软件安装、进程、网络基础等内容，筛选适合第 1 周学习的资料并记录来源
- 适用项目: `projects/zero-basics-plan`
- 访问时间: 2026-03-26T20:21:37+08:00（来源：`get_current_time`）
- 前置内部材料:
  - `projects/zero-basics-plan/analysis/2026-03-26-vscode-linux-beginner-resource-survey.md`
  - `projects/zero-basics-plan/README.md`
- 外部来源获取方式:
  - 直接页面抓取：`web_fetch(URL)`
  - 本轮 `web_search` 多次返回 403 / 无结果，故转为直接验证已知高质量来源，并在文中逐项记录 URL

## 结论先看

适合零基础学习者的 Linux 第 1 周路线，不应该从“背命令大全”开始，而应该按下面顺序建立认知：

1. **先建立地图**：Linux 是什么、终端是什么、路径与目录如何理解。
2. **再学高频操作**：`pwd`、`ls`、`cd`、`mkdir`、`touch`、`cp`、`mv`、`rm`、`cat`、`less`。
3. **再引入最小系统观**：文件权限、软件安装、进程、网络分别先学“是什么、为什么要看、最小命令是什么”。
4. **把高阶内容延后**：复杂网络配置、systemd 深入、源码编译、内核、企业级运维不适合第 1 周。

本次调研认为，第 1 周主线应以 **Ubuntu / Debian 命令习惯作为主讲路径**，同时在软件安装处简要标注 `apt` 与 `yum`/`dnf` 的发行版差异。原因是 Ubuntu 初学者资料更多、命令示例更统一、教程迁移成本更低；这一点来自 Ubuntu 官方入门材料和菜鸟教程的 Debian/CentOS 双线资料对照，而不是主观偏好。

---

## 一、零基础 Linux 学习路径框架

> 目标：满足“文件系统、常用命令、权限、软件安装、进程、网络基础”六大模块，并按零基础认知递进排序。

### 模块 1：终端、路径与文件系统认知

- 学习目标:
  - 知道 Linux 是什么、终端是什么
  - 理解根目录 `/`、家目录 `~`、绝对路径、相对路径
  - 建立对 `/home`、`/etc`、`/var`、`/tmp`、`/usr` 的最小认知
- 为什么放第一位:
  - 不先理解“我现在在哪、系统目录是什么”，后面所有命令都容易变成机械复制
- 适合第 1 周:
  - 是

### 模块 2：常用命令与文件操作

- 学习目标:
  - 会查看当前位置与目录内容：`pwd`、`ls`
  - 会切换目录：`cd`
  - 会创建、复制、移动、删除文件：`mkdir`、`touch`、`cp`、`mv`、`rm`
  - 会查看文件内容：`cat`、`less`、`head`、`tail`
- 为什么放第二位:
  - 这些命令构成后续所有练习的最小操作闭环
- 适合第 1 周:
  - 是

### 模块 3：权限基础

- 学习目标:
  - 读懂 `ls -l` 输出
  - 理解 owner/group/others 与 `rwx`
  - 会做最小权限修改：`chmod u+x file`、理解 `755/644`
  - 知道 `chmod 777` 不是默认解法
- 为什么放第三位:
  - 新手经常在“脚本不能执行”“文件不能修改”处卡住，但不需要第一天就学复杂权限
- 适合第 1 周:
  - 是

### 模块 4：软件安装基础

- 学习目标:
  - 知道 Linux 软件通常通过包管理器安装
  - Ubuntu / Debian 主线理解 `apt-get update`、`apt-get install`
  - 知道 CentOS / RHEL 体系常见 `yum install`
  - 理解“安装前更新索引”和“依赖关系”这两个概念
- 为什么放第四位:
  - 学会文件与权限后，再理解“系统如何安装软件”最自然
- 适合第 1 周:
  - 是，但只学最小必需，不学软件源深挖和复杂仓库配置

### 模块 5：进程基础

- 学习目标:
  - 知道进程是“正在运行的程序”
  - 会用 `ps`、`top` 查看进程
  - 知道 `kill` 默认是发送 TERM，`kill -9` 是强制手段
- 为什么放第五位:
  - 第 1 周先建立“程序在运行”这件事的观察能力，不追求服务治理
- 适合第 1 周:
  - 是，但只做观察级入门

### 模块 6：网络与远程操作基础

- 学习目标:
  - 知道 IP、端口、远程连接的最小概念
  - 会用 `ssh` 远程登录
  - 对 `ifconfig`/`ip addr`、`netstat`/`ss` 保持“看得懂一点”的程度
  - 能理解“网络检查”和“文件下载”最小工具：`ping`、`wget`、`curl`
- 为什么放第六位:
  - 对零基础来说，网络应以“能连接、能下载、能远程登录”为边界，不应提前深入复杂配置
- 适合第 1 周:
  - 是，但控制在“最小必要理解”

---

## 二、资料筛选原则

### 2.1 选材规则

- **官方/机构资料优先作为校验底座**：Ubuntu、GNU、LinuxCommand.org
- **教程站与社区文章优先作为中文主教材候选**：菜鸟教程、博客园、阿里云开发者社区
- **第 1 周资料必须满足**：
  - 对零基础术语有解释
  - 有最小示例
  - 没有把高阶主题当默认前提
  - 页面可访问、来源可记录

### 2.2 不纳入第 1 周核心的内容

- 编译安装、源码构建
- systemd/service 深入
- SELinux 深入
- 复杂网络路由与防火墙
- 容器、Kubernetes、内核编译
- 批量自动化脚本工程化

---

## 三、多平台资料池（按主题整理）

> 说明：每个主题至少给出 2 条候选；平台覆盖官方文档、教程网站、社区博客/开发者社区三类以上来源。

### 3.1 文件系统

| ID | 类型 | 标题 | 平台 | 链接 | 适合阶段 | 备注 |
|---|---|---|---|---|---|---|
| FS-01 | 主资料候选 | Linux 系统目录结构 | 菜鸟教程 | https://www.runoob.com/linux/linux-system-contents.html | 第 1 周 | 中文、表格化、适合建立目录地图 |
| FS-02 | 主资料候选 | 新手一周入门Linux，看这篇就够了！ | 博客园 | https://www.cnblogs.com/jche/p/18900912/study_linux | 第 1 周 | 按 Day1-Day7 分解，适合课程映射 |
| FS-03 | 主资料候选 | 【零基础友好】Linux 初学者指令指南 | 阿里云开发者社区 | https://developer.aliyun.com/article/1680064 | 第 1 周 | 有 Windows 与 Linux 路径对比 |
| FS-04 | 校验资料 | The Linux command line for beginners | Ubuntu | https://ubuntu.com/tutorials/command-line-for-beginners | 第 1 周 | 官方入门材料，讲 terminal 与文件操作 |
| FS-05 | 校验资料 | Learning the shell | LinuxCommand.org | https://linuxcommand.org/lc3_learning_the_shell.php | 后续阶段参考 | 英文、体系化，适合补足 shell 认知 |

#### 文件系统主题判断

- 第 1 周推荐: FS-01、FS-02、FS-03、FS-04
- 后续参考: FS-05
- 原因:
  - FS-01/02/03 中文可直接上手，FS-04 负责术语与顺序校验
  - FS-05 更适合英语可读用户作为延伸阅读，不应成为唯一核心材料

### 3.2 常用命令

| ID | 类型 | 标题 | 平台 | 链接 | 适合阶段 | 备注 |
|---|---|---|---|---|---|---|
| CMD-01 | 主资料候选 | 新手一周入门Linux，看这篇就够了！ | 博客园 | https://www.cnblogs.com/jche/p/18900912/study_linux | 第 1 周 | 命令按天拆分 |
| CMD-02 | 主资料候选 | 【零基础友好】Linux 初学者指令指南 | 阿里云开发者社区 | https://developer.aliyun.com/article/1680064 | 第 1 周 | 对 `pwd`、`cd`、家目录、隐藏文件解释细 |
| CMD-03 | 补充资料 | Linux 教程 | 菜鸟教程 | https://www.runoob.com/linux/linux-tutorial.html | 第 1 周 | 目录化索引强，适合查漏补缺 |
| CMD-04 | 校验资料 | The Linux command line for beginners | Ubuntu | https://ubuntu.com/tutorials/command-line-for-beginners | 第 1 周 | 官方从 terminal 到文件操作的练习路线 |
| CMD-05 | 校验资料 | Learning the shell | LinuxCommand.org | https://linuxcommand.org/lc3_learning_the_shell.php | 后续阶段参考 | 偏英文体系化学习 |

#### 常用命令主题判断

- 第 1 周推荐: CMD-01、CMD-02、CMD-04
- 补充索引: CMD-03
- 后续参考: CMD-05
- 原因:
  - 第 1 周更需要“场景 + 少量命令”的材料，CMD-01/02/04 都符合
  - CMD-03 更像词典，不建议作为第一读物

### 3.3 权限

| ID | 类型 | 标题 | 平台 | 链接 | 适合阶段 | 备注 |
|---|---|---|---|---|---|---|
| PERM-01 | 主资料候选 | Linux 文件基本属性 | 菜鸟教程 | https://www.runoob.com/linux/linux-file-attr-permission.html | 第 1 周 | 能把 `ls -l` 拆开解释 |
| PERM-02 | 主资料候选 | Linux chmod 命令 | 菜鸟教程 | https://www.runoob.com/linux/linux-comm-chmod.html | 第 1 周 | 覆盖符号模式与数字模式 |
| PERM-03 | 补充资料 | 新手一周入门Linux，看这篇就够了！ | 博客园 | https://www.cnblogs.com/jche/p/18900912/study_linux | 第 1 周 | 把权限放在 Day5，顺序友好 |
| PERM-04 | 校验资料 | chmod invocation | GNU Coreutils | https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html | 第 1 周 | 校验 `chmod` 行为与递归风险 |

#### 权限主题判断

- 第 1 周推荐: PERM-01、PERM-02、PERM-03
- 校验底座: PERM-04
- 原因:
  - 中文资料已足够满足入门；GNU 手册用于避免误讲，尤其是递归与符号链接风险

### 3.4 软件安装

| ID | 类型 | 标题 | 平台 | 链接 | 适合阶段 | 备注 |
|---|---|---|---|---|---|---|
| PKG-01 | 主资料候选 | Linux apt-get 命令完全指南 | 菜鸟教程 | https://www.runoob.com/linux/linux-comm-apt-get.html | 第 1 周 | 对 Ubuntu/Debian 主线很直接 |
| PKG-02 | 主资料候选 | linux yum 命令 | 菜鸟教程 | https://www.runoob.com/linux/linux-yum.html | 第 1 周 | 用于简要说明 RedHat/CentOS 体系 |
| PKG-03 | 补充资料 | Linux 教程 | 菜鸟教程 | https://www.runoob.com/linux/linux-tutorial.html | 第 1 周 | 作为包管理导航索引 |
| PKG-04 | 校验资料 | Ubuntu package management | Ubuntu Server Docs | https://ubuntu.com/server/docs/package-management | 后续阶段参考 | 抓取发生跳转，但可作为官方路径线索 |

#### 软件安装主题判断

- 第 1 周推荐: PKG-01、PKG-02
- 补充索引: PKG-03
- 后续参考: PKG-04
- 原因:
  - 第 1 周只要理解“包管理器是什么、如何安装软件”，不需要展开复杂源配置
  - 以 `apt-get` 为主，`yum` 为发行版差异补注即可

### 3.5 进程

| ID | 类型 | 标题 | 平台 | 链接 | 适合阶段 | 备注 |
|---|---|---|---|---|---|---|
| PROC-01 | 主资料候选 | Linux ps 命令 | 菜鸟教程 | https://www.runoob.com/linux/linux-comm-ps.html | 第 1 周 | 解释“查看进程状态” |
| PROC-02 | 主资料候选 | Linux top 命令 | 菜鸟教程 | https://www.runoob.com/linux/linux-comm-top.html | 第 1 周 | 实时查看进程，利于建立“程序在运行”概念 |
| PROC-03 | 主资料候选 | Linux kill 命令 | 菜鸟教程 | https://www.runoob.com/linux/linux-comm-kill.html | 第 1 周 | 解释 TERM 与 KILL 的区别 |
| PROC-04 | 补充资料 | 新手一周入门Linux，看这篇就够了！ | 博客园 | https://www.cnblogs.com/jche/p/18900912/study_linux | 第 1 周 | Day4 放系统监控与进程管理 |

#### 进程主题判断

- 第 1 周推荐: PROC-01、PROC-02、PROC-03、PROC-04
- 原因:
  - 这些资料只要求“会看、会区分、知道慎用 kill -9”，强度适中

### 3.6 网络基础

| ID | 类型 | 标题 | 平台 | 链接 | 适合阶段 | 备注 |
|---|---|---|---|---|---|---|
| NET-01 | 主资料候选 | Linux ssh 命令 | 菜鸟教程 | https://www.runoob.com/linux/linux-comm-ssh.html | 第 1 周 | 最适合讲远程登录最小闭环 |
| NET-02 | 主资料候选 | Linux ifconfig命令 | 菜鸟教程 | https://www.runoob.com/linux/linux-comm-ifconfig.html | 第 1 周 | 用于认识网卡与 IP；注意命令偏传统 |
| NET-03 | 主资料候选 | Linux netstat命令 | 菜鸟教程 | https://www.runoob.com/linux/linux-comm-netstat.html | 第 1 周 | 用于认识“监听/连接”概念 |
| NET-04 | 补充资料 | 新手一周入门Linux，看这篇就够了！ | 博客园 | https://www.cnblogs.com/jche/p/18900912/study_linux | 第 1 周 | Day6 涵盖网络与远程连接 |
| NET-05 | 补充资料 | 【零基础友好】Linux 初学者指令指南 | 阿里云开发者社区 | https://developer.aliyun.com/article/1680064 | 后续阶段参考 | 更偏基础终端与文件，不是网络主资料 |

#### 网络主题判断

- 第 1 周推荐: NET-01、NET-02、NET-03、NET-04
- 风险提示:
  - `ifconfig` 与 `netstat` 在现代系统中常常被 `ip`、`ss` 替代；第 1 周可以保留传统命令作为“看得懂旧教程”的桥梁，但课程正文应补一行“现代系统常见替代命令”。

---

## 四、第 1 周推荐清单

> 标准：只保留“零基础友好 + 覆盖核心概念 + 可直接落地到 7 天学习顺序”的资料。

### 4.1 第 1 周主资料

| 顺位 | 资料 ID | 标题 | 作用 | 推荐理由 |
|---|---|---|---|---|
| 1 | FS-04 / CMD-04 | The Linux command line for beginners | 建立终端与命令行心理模型 | 官方、从零假设、强调 practical exercises |
| 2 | FS-03 / CMD-02 | 【零基础友好】Linux 初学者指令指南 | 用中文讲路径、账号、隐藏文件、家目录 | 对 Windows 用户迁移非常友好 |
| 3 | FS-01 | Linux 系统目录结构 | 建立 `/home`、`/etc`、`/var` 等目录地图 | 表格化，适合改写成课程卡片 |
| 4 | CMD-01 / PROC-04 / NET-04 | 新手一周入门Linux，看这篇就够了！ | 课程节奏参照物 | 已按天拆分，利于映射第 1 周结构 |
| 5 | PERM-01 | Linux 文件基本属性 | 第一次讲权限的主材料 | 能拆解 `ls -l` |
| 6 | PERM-02 | Linux chmod 命令 | 第一次讲 chmod 的主材料 | 同时给出符号法与数字法 |
| 7 | PKG-01 | Linux apt-get 命令完全指南 | 软件安装的 Ubuntu 主线 | 容易转写成“update → install”最小闭环 |
| 8 | PROC-01 / PROC-02 / PROC-03 | Linux ps/top/kill 命令 | 进程最小认知 | 够用、不需要拔高 |
| 9 | NET-01 | Linux ssh 命令 | 远程登录最小闭环 | 可和 VSCode 远程学习线衔接 |

### 4.2 第 1 周只做补充、不做主线的资料

| 资料 ID | 原因 |
|---|---|
| FS-05 / CMD-05 | 英文体系化很好，但不应成为零基础中文课程唯一主材料 |
| PKG-02 | `yum` 适合做发行版差异补注，不宜压过 Ubuntu 主线 |
| NET-02 / NET-03 | 只需达到“见过、会看一点”的程度，不适合深讲参数 |
| PERM-04 | GNU 手册是校验底座，不适合作为新手第一读物 |

---

## 五、第 1 周学习顺序设计（可直接映射 7 天）

### Day 1：Linux、终端、路径

- 学习目标:
  - 知道终端是做什么的
  - 理解当前目录、家目录、绝对路径、相对路径
- 推荐资料:
  - FS-04 / CMD-04
  - FS-03 / CMD-02
- 练习建议:
  - 打开终端，执行 `pwd`、`whoami`、`ls`
  - 用 `cd ~`、`cd /`、`cd ..` 感受路径变化

### Day 2：目录与文件操作

- 学习目标:
  - 会创建目录和文件，复制、移动、删除
- 推荐资料:
  - CMD-01
  - CMD-02
- 练习建议:
  - 在 `~/sandbox` 下练 `mkdir`、`touch`、`cp`、`mv`
  - 只允许在沙盒目录里使用 `rm`

### Day 3：查看文件内容与帮助

- 学习目标:
  - 会用 `cat`、`less`、`head`、`tail`
  - 知道可以用 `man` / `--help` 查帮助
- 推荐资料:
  - CMD-01
  - FS-04 / CMD-04
- 练习建议:
  - 自己创建一个文本文件，用不同命令查看

### Day 4：文件系统地图

- 学习目标:
  - 初步理解 `/home`、`/etc`、`/var`、`/tmp`、`/usr`
- 推荐资料:
  - FS-01
  - FS-03
- 练习建议:
  - `ls /` 后逐个口述这些目录“像什么房间”

### Day 5：权限基础

- 学习目标:
  - 能读 `ls -l`
  - 理解 `rwx`、owner/group/others
  - 会给脚本加执行权限
- 推荐资料:
  - PERM-01
  - PERM-02
  - PERM-03
- 练习建议:
  - 创建 `hello.sh`，执行 `chmod u+x hello.sh`
  - 只讲 `u+x`、`644`、`755`，不讲特殊权限

### Day 6：软件安装与进程基础

- 学习目标:
  - 理解包管理器与依赖
  - 会看进程、知道如何温和结束进程
- 推荐资料:
  - PKG-01
  - PROC-01 / PROC-02 / PROC-03
- 练习建议:
  - 只讲 `apt-get update` 与 `apt-get install <package>`
  - 用 `ps` 与 `top` 观察进程，不要求掌握全部字段

### Day 7：网络与远程最小闭环

- 学习目标:
  - 知道 SSH 是什么
  - 会做一次最简单的远程登录或理解远程登录流程
  - 认识“端口/监听/网络接口”这些词
- 推荐资料:
  - NET-01
  - NET-04
  - NET-02 / NET-03（只选读）
- 练习建议:
  - 如果有测试主机，执行一次 `ssh user@host`
  - 没有远程主机则至少理解命令格式与参数 `-p`、`-i`

---

## 六、为什么这些内容适合第 1 周

### 6.1 第 1 周的边界

第 1 周应该解决的是“新手第一次面对 Linux 时会不会慌”，而不是“让人一周内变成运维”。因此应聚焦：

- 能认路
- 能操作文件
- 能读简单权限
- 能安装一个包
- 能看进程
- 能理解远程登录

### 6.2 明确延后的内容

以下内容本次明确归为“后续阶段参考”，不进入第 1 周主线：

- `find` / `grep` 的复杂组合
- `sed` / `awk` 正文讲解
- 大规模文件权限递归修改
- `apt sources` / 软件源镜像深挖
- `systemctl` 服务管理体系
- 网络路由、防火墙、桥接、端口映射
- shell 脚本自动化

---

## 七、与 28 天 Markdown 教程的映射

### 7.1 课程结构映射

- 第 1 周: Linux 基础认知 + 高频命令 + 最小系统观
- 第 2 周: 搜索过滤、文本处理、压缩归档、远程开发体验
- 第 3 周: Git/GitHub、编辑器、项目实践
- 第 4 周: AI 辅助编程、深度学习前置、综合练习

### 7.2 第 1 周产出可直接转写为教程章节

1. Linux 和终端是什么
2. 路径、目录与文件系统地图
3. 常用命令最小闭环
4. 查看文件内容与帮助
5. 权限是什么、如何看懂 `ls -l`
6. 包管理器是什么
7. 进程与网络最小概念

---

## 八、Multi-Agent 拆分建议

> 满足“适合 Multi-Agent 分工执行，任务拆分清晰”。

### 子任务 A：资料继续补充与去重

- 输入: 本文已有资料池
- 输出: 去重后的标准化资料表（标题、平台、URL、语言、主题、适合阶段）
- 依赖: 无

### 子任务 B：来源校验

- 输入: 资料表 + URL
- 输出: 可访问性状态、抓取摘录、是否存在明显过时/失效问题
- 依赖: A 可并行开始

### 子任务 C：课程映射细化

- 输入: 第 1 周推荐资料
- 输出: 7 天课程草案，每天 2~3 条资料与练习建议
- 依赖: A、B

### 子任务 D：术语改写

- 输入: 英文/偏技术化资料
- 输出: 零基础人话解释模板（“是什么 / 为什么 / 类比 / 最小示例 / 常见错误”）
- 依赖: C

### 子任务 E：风险与误用清单

- 输入: 权限、删除、kill、包管理资料
- 输出: 初学者警示框素材库
- 依赖: A、B

### 子任务 F：最终汇总成 Markdown 教程底稿

- 输入: C、D、E
- 输出: 可并入 28 天教程的第 1 周正文结构
- 依赖: C、D、E

---

## 九、关键发现与风险

### 9.1 关键发现

1. **Ubuntu 官方教程非常适合做第 1 周“主线校验资料”**，因为它明确写出“assume no prior knowledge”，并把内容组织为 practical exercises。来源：`web_fetch(https://ubuntu.com/tutorials/command-line-for-beginners)`。
2. **LinuxCommand.org 很适合做后续 shell 体系化延伸**，但英语门槛决定它不应单独承担第 1 周主教材角色。来源：`web_fetch(https://linuxcommand.org/lc3_learning_the_shell.php)`。
3. **中文社区资料里，博客园 + 阿里云开发者社区 + 菜鸟教程的组合，足够覆盖零基础第 1 周**，同时又能用 Ubuntu/GNU 资料做底层校验。
4. **权限与网络主题最容易被社区文章带偏到“命令大全”或“危险参数”**，因此课程正文必须主动降复杂度。

### 9.2 风险与处理

- 风险 1：`chmod -R` 与符号链接递归存在安全风险。
  - 依据：GNU Coreutils `chmod invocation`
  - 处理：第 1 周不教递归权限修改。

- 风险 2：很多资料示例包含 `rm -rf`。
  - 依据：`https://www.cnblogs.com/jche/p/18900912/study_linux`
  - 处理：所有删除命令仅在 `~/sandbox` 示例目录演示。

- 风险 3：`ifconfig`、`netstat` 在现代系统中不是唯一推荐命令。
  - 依据：本次资料池多来自传统教程站；因此课程中需标注“现代替代常见为 `ip` / `ss`”。
  - 处理：第 1 周只要求识别，不把其当唯一标准答案。

- 风险 4：软件安装资料容易默认 root 或 sudo 全程无解释。
  - 依据：菜鸟教程 apt/yum 页面常见示例
  - 处理：教程正文需补“sudo 是临时以管理员权限执行命令”的概念说明。

---

## 十、最终推荐组合

### 第 1 周最小主资料组合

- Ubuntu：
  - https://ubuntu.com/tutorials/command-line-for-beginners
- 阿里云开发者社区：
  - https://developer.aliyun.com/article/1680064
- 博客园：
  - https://www.cnblogs.com/jche/p/18900912/study_linux
- 菜鸟教程：
  - https://www.runoob.com/linux/linux-system-contents.html
  - https://www.runoob.com/linux/linux-file-attr-permission.html
  - https://www.runoob.com/linux/linux-comm-chmod.html
  - https://www.runoob.com/linux/linux-comm-apt-get.html
  - https://www.runoob.com/linux/linux-comm-ps.html
  - https://www.runoob.com/linux/linux-comm-top.html
  - https://www.runoob.com/linux/linux-comm-kill.html
  - https://www.runoob.com/linux/linux-comm-ssh.html

### 作为校验与延伸

- GNU Coreutils：
  - https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html
- LinuxCommand.org：
  - https://linuxcommand.org/lc3_learning_the_shell.php
- 菜鸟教程补充页：
  - https://www.runoob.com/linux/linux-yum.html
  - https://www.runoob.com/linux/linux-comm-ifconfig.html
  - https://www.runoob.com/linux/linux-comm-netstat.html

---

## Provenance Notes

- 本文所有结论均绑定到以下证据之一：
  1. 仓库内前置调研文件：`projects/zero-basics-plan/analysis/2026-03-26-vscode-linux-beginner-resource-survey.md`
  2. 本轮页面抓取：`web_fetch(URL)`，URL 已逐项写入正文
- 本文未使用无来源数值统计；关于“第 1 周优先 Ubuntu 主线”“延后高阶内容”“权限与网络需降复杂度”等判断，均来自对已抓取资料内容范围、解释粒度与术语负载的比较，而非无依据断言。
