# 28 天零基础开发与 AI 学习教程

- 更新日期：2026-03-26
- 适用对象：能正常使用电脑、但对 Linux、Git、GitHub、AI 编程工具、深度学习仍处于入门阶段的学习者
- 建议节奏：工作日每天 60–120 分钟；周末系统课 120–180 分钟
- 交付定位：可直接学习的 Markdown 教程初稿，可继续扩写为正式课程讲义

## 教程使用说明

1. **先完成每天的操作步骤，再看补充资料。** 每天都按“做完最小任务”优先，而不是先囤一堆链接。
2. **坚持留下输出物。** 每天建议至少留下 1 份笔记、1 个脚本、1 次提交或 1 份复盘。
3. **优先使用主资料。** 每天只列 1–3 条主资料，避免信息过载。
4. **周末系统课必须完成。** Day 7 / 14 / 21 / 28 负责把前面分散的知识串成体系。
5. **默认学习环境。** 本教程默认你有一台本地电脑、一个可 SSH 登录的 Linux 环境，以及一个 GitHub 账号。

## 28 天学习目标

28 天后，你应至少达到以下闭环能力：

1. 能使用 VS Code Remote SSH 连接并操作 Linux 主机。
2. 能完成 Linux 常见目录、文件、权限、进程、SSH 与基础排障操作。
3. 能使用 Git 与 GitHub 完成本地版本管理、远程同步、分支开发与 Pull Request。
4. 能理解并实践 AI 辅助编程的最小工作流：拆任务、给上下文、看 diff、做验证。
5. 能理解深度学习中的张量、模型、训练、推理等基础概念，并跑通一个最小 PyTorch 实验。
6. 能完成一个带仓库记录的结课小项目。

## 资料选择原则

- 主线优先采用官方文档、长期维护教程、官方仓库 README / CONTRIBUTING。
- 中文资料优先补充新手理解、案例和操作感。
- 社区资料只在能补足“实操截图、案例、避坑点”时纳入，不作为唯一依据。
- AI 工具类资料变化快，正文以“原则 + 当前入口页”为主，不写死易变界面细节。

## 四周总览

| 周次 | 阶段目标 | 主题范围 | 周末产出 |
|---|---|---|---|
| 第 1 周 | 打通环境与基础命令 | 开发环境、VS Code Remote SSH、Linux 基础命令 | 完成远程开发最小闭环与命令基础复盘 |
| 第 2 周 | 建立服务器操作与版本管理基础 | 权限、进程、SSH、Git 基础与远程仓库 | 完成终端到 GitHub 的完整工作流 |
| 第 3 周 | 建立协作与 AI 编程工作流 | GitHub 协作、分支/PR、项目阅读、工程实践、Cursor | 完成一次 AI 辅助的仓库改动与 PR |
| 第 4 周 | 建立深度学习最小认知并完成综合输出 | PyTorch 入门、训练/推理、AI 辅助学习、结课项目 | 完成最小深度学习实验与结课复盘 |

---

# 第 1 周：环境连通与 Linux 入门

## Day 1｜认识路线、准备环境、建立学习记录

### 学习目标
- 明确 28 天要学什么、产出什么。
- 准备一台可 SSH 登录的 Linux 主机或虚拟机。
- 建立课程笔记目录与每日记录习惯。

### 任务安排
- 阅读本教程总说明。
- 准备 Linux 环境与 GitHub 账号。
- 创建本地课程文件夹与笔记模板。

### 操作步骤
1. 在本地创建 `zero-basics-28days/` 文件夹。
2. 在其中建立 `notes/`、`screenshots/`、`projects/` 三个子目录。
3. 准备一个可 SSH 登录的 Linux 环境，记录 IP、用户名、认证方式。
4. 新建 `notes/day1-environment-notes.md`，记录你的设备、系统、学习目标。
5. 写下 28 天后你希望完成的一个小项目。

### 推荐资料
- **必读｜学习路径**：编程学习全指南：从零基础到职业发展的实用路径  
  来源链接：https://developer.cloud.tencent.com/article/2571989
- **必读｜路线图**：计算机学习路线大全（2025版）  
  来源链接：https://csguide.cn/roadmap/
- **选读｜官方教程入口**：VS Code Remote SSH 文档  
  来源链接：https://code.visualstudio.com/docs/remote/ssh

### 当日产出
- `notes/day1-environment-notes.md`
- 一份环境信息清单

---

## Day 2｜安装 VS Code、Python 与基础开发环境

### 学习目标
- 完成 VS Code、Python 或 Miniconda 的最小安装。
- 理解编辑器、解释器、终端三者的区别。
- 跑通一个最简单的 Python 脚本。

### 任务安排
- 安装 VS Code。
- 安装 Python 或 Miniconda。
- 在 VS Code 中选择解释器并运行 `hello.py`。

### 操作步骤
1. 安装 VS Code，并确认能正常打开本地文件夹。
2. 安装 Python 3 或 Miniconda。
3. 新建 `hello.py`，写入 `print("hello, 28 days")`。
4. 在终端运行 `python hello.py` 或 `python3 hello.py`。
5. 在笔记里记录安装时遇到的 PATH、权限或解释器选择问题。

### 推荐资料
- **必读｜中文实操**：安装 Conda + VSCode 配置 Python 开发环境  
  来源链接：https://zeeklog.com/xiao-bai-ling-ji-chu-jiao-cheng-an-zhuang-conda-vscode-pei-zhi-python-kai-fa-huan-jing-9/
- **必读｜官方基线**：Getting Started with Python in VS Code  
  来源链接：https://code.visualstudio.com/docs/python/python-tutorial
- **选读｜中文补充**：VS Code Python 配置完全指南  
  来源链接：https://cloud.tencent.com/developer/article/2562202

### 当日产出
- `projects/hello.py`
- `notes/day2-setup.md`

---

## Day 3｜第一次连接 Linux：SSH 与 VS Code Remote SSH

### 学习目标
- 理解“本地 VS Code + 远程 Linux”工作模式。
- 会配置一条 SSH Host。
- 在 VS Code 中成功打开远程目录。

### 任务安排
- 本地终端测试 SSH。
- 安装 Remote - SSH 扩展。
- 通过 VS Code 连到远程主机。

### 操作步骤
1. 在本地终端执行 `ssh 用户名@IP`，验证 SSH 可连通。
2. 安装 VS Code 的 Remote - SSH 扩展。
3. 打开 SSH config，新增一条 Host 配置。
4. 在 VS Code 中选择 `Connect to Host` 并连接。
5. 成功后打开远程 Home 目录，新建一个 `README.md` 测试文件。

### 推荐资料
- **必读｜官方中文**：使用 SSH 进行远程开发  
  来源链接：https://vscode.js.cn/docs/remote/ssh
- **必读｜新手操作文**：vscode 使用 ssh 进行远程开发（remote-ssh）  
  来源链接：https://cloud.tencent.com/developer/article/2600946
- **选读｜SSH 基础**：SSH Essentials  
  来源链接：https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys

### 当日产出
- 可用的 `~/.ssh/config` 条目
- `notes/day3-remote-ssh.md`

---

## Day 4｜命令行起步：pwd、ls、cd、mkdir、touch

### 学习目标
- 会在终端中切换目录、查看文件、创建目录与文件。
- 理解绝对路径、相对路径、当前目录。
- 建立远程终端操作的最小熟悉感。

### 任务安排
- 在远程终端中练习 5 个基础命令。
- 建立课程练习目录。
- 记录你已经会用的命令。

### 操作步骤
1. 登录远程主机并执行 `pwd`。
2. 执行 `ls` 与 `ls -la`，观察普通文件与隐藏文件。
3. 用 `mkdir zero-basics` 创建练习目录。
4. 进入目录后用 `touch notes.txt` 创建文件。
5. 用 `cd ~`、`cd /tmp`、`cd -` 来回切换目录。

### 推荐资料
- **必读｜中文七天路径**：新手一周入门 Linux，看这篇就够了！  
  来源链接：https://www.cnblogs.com/jche/p/18900912/study_linux
- **必读｜长期维护教程**：The Linux command line for beginners  
  来源链接：https://ubuntu.com/tutorials/command-line-for-beginners
- **选读｜命令索引**：Linux Journey  
  来源链接：https://linuxjourney.com/

### 当日产出
- `notes/day4-basic-commands.md`

---

## Day 5｜文件操作与文本查看：cat、less、cp、mv、rm

### 学习目标
- 掌握常用文件查看、复制、移动、删除命令。
- 理解命令行删除的风险。
- 能在终端里快速查看文本内容。

### 任务安排
- 新建并编辑几个测试文件。
- 完成复制、移动、重命名、删除操作。
- 记录危险命令注意事项。

### 操作步骤
1. 在练习目录里创建 `a.txt`、`b.txt`。
2. 用 `echo` 写入两三行文本。
3. 用 `cat`、`less` 查看文件内容。
4. 用 `cp a.txt a-copy.txt`、`mv b.txt b-renamed.txt`。
5. 删除测试文件，记录“删除前先 `ls` 再确认”的习惯。

### 推荐资料
- **必读｜中文命令索引**：Linux 常用基础命令（2024 年最新篇）  
  来源链接：https://cloud.tencent.com/developer/article/2424112
- **必读｜长期维护教程**：Linux Journey  
  来源链接：https://linuxjourney.com/
- **选读｜视频导入**：【2026最新版】Linux 操作系统从基础入门到精通必学教程  
  来源链接：https://www.bilibili.com/video/BV1bxAjznEyq/

### 当日产出
- `notes/day5-file-ops.md`

---

## Day 6｜管道、重定向、grep 与 history

### 学习目标
- 理解命令可以组合使用。
- 会使用 `|`、`>`、`>>`、`grep`、`history`。
- 能把输出保存到文件并从中筛选信息。

### 任务安排
- 保存终端输出到文件。
- 搜索文本中的关键词。
- 复盘本周已使用的命令。

### 操作步骤
1. 执行 `history | tail` 查看最近命令。
2. 用 `ls -la > filelist.txt` 保存输出。
3. 用 `grep ssh filelist.txt` 搜索关键词。
4. 用 `echo "today learned" >> notes.txt` 追加内容。
5. 在笔记中总结“管道适合串联命令，重定向适合保存结果”。

### 推荐资料
- **必读｜官方语义**：Bash Manual: Redirections  
  来源链接：https://www.gnu.org/software/bash/manual/html_node/Redirections.html
- **必读｜官方语义**：Bash Manual: Pipelines  
  来源链接：https://www.gnu.org/software/bash/manual/html_node/Pipelines.html
- **选读｜入门教程**：Ubuntu command line for beginners  
  来源链接：https://ubuntu.com/tutorials/command-line-for-beginners

### 当日产出
- `notes/day6-pipe-and-redirection.md`

---

## Day 7｜系统课程 1：远程开发环境与 Linux 基础复盘

### 学习目标
- 把“SSH 登录 → VS Code Remote SSH → 命令行基础操作”串起来。
- 检查自己是否具备进入第 2 周的环境前提。

### 系统课程内容
- 梳理本地电脑、远程 Linux、VS Code、终端之间的关系。
- 回顾路径、文件、命令、重定向、文本查看。
- 演示一次完整流程：连接远程主机 → 创建目录 → 写 README → 在终端查看结果。
- 归纳常见错误：SSH 连不上、Host key 提示、解释器找不到、路径混乱。

### 操作步骤
1. 通过 VS Code Remote SSH 连接远程主机。
2. 创建 `week1-demo/README.md`。
3. 在文件中写 5 行自我介绍与本周收获。
4. 用终端执行 `cat README.md` 和 `ls -la` 验证。
5. 整理一份《第 1 周我已经会做的事》清单。

### 推荐资料
- **必读｜官方中文**：使用 SSH 进行远程开发  
  来源链接：https://vscode.js.cn/docs/remote/ssh
- **必读｜Linux 路径与命令**：Linux Journey  
  来源链接：https://linuxjourney.com/
- **选读｜SSH 补充**：SSH Essentials  
  来源链接：https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys

### 复盘作业
- 写一份《我已经会的 Linux / 远程开发操作清单》。
- 给自己在三个维度打分：环境连通、目录操作、文本处理。
- 如果仍有卡点，写出“问题、出现条件、已尝试解决方法”。

### 当日产出
- `notes/week1-review.md`

---

# 第 2 周：Linux 实战深化与 Git 入门

## Day 8｜Linux 文件系统、路径与目录导航

### 学习目标
- 理解 Linux 文件系统是“从 `/` 开始的一棵树”。
- 认识 `/home`、`/etc`、`/var`、`/tmp`、`/usr` 等常见目录用途。
- 掌握 `pwd`、`ls`、`cd`、`mkdir`、`touch` 的最小导航与建文件流程。

### 先理解：今天到底在学什么
Linux 不像 Windows 那样按“C 盘、D 盘”作为主要入口。对新手来说，先把它想成一棵从根目录 `/` 长出来的目录树更容易。

常见目录可以先这样理解：
- `/`：整棵文件树的起点。
- `/home`：普通用户的家目录，自己的练习文件通常放这里。
- `/etc`：系统配置文件常见位置，例如网络、服务配置。
- `/var`：经常变化的数据，例如日志、缓存、队列。
- `/tmp`：临时文件目录，通常重启后可能被清理。
- `/usr`：大量应用程序、库和共享资源所在位置。

### 核心概念
- **绝对路径**：从 `/` 开始写的完整路径，例如 `/home/akari/notes/todo.txt`。
- **相对路径**：相对于“当前所在目录”写的路径，例如 `notes/todo.txt`。
- **当前目录**：你现在所在的位置，可用 `pwd` 查看。

### 任务安排
- 看清当前所在目录。
- 建一个安全练习区。
- 在练习区里创建目录和文件。
- 练习绝对路径与相对路径切换。

### 操作步骤
> 默认环境：任意 Debian/Ubuntu、CentOS、Rocky、Fedora、WSL 或虚拟机 Linux。
> 为了安全，今天的练习尽量都放在自己的家目录下，不要在 `/etc`、`/usr`、`/var` 里乱改文件。

1. 查看当前目录：
   ```bash
   pwd
   ```
   预期现象：会输出类似 `/home/你的用户名`。

2. 看看当前目录里有什么：
   ```bash
   ls
   ls -la
   ```
   预期现象：`ls -la` 会显示隐藏文件，例如 `.bashrc`、`.ssh`。

3. 在家目录创建本周练习区：
   ```bash
   mkdir -p ~/week2-lab/day8
   cd ~/week2-lab/day8
   pwd
   ```
   预期现象：最后一条命令应输出类似 `/home/你的用户名/week2-lab/day8`。

4. 创建两个测试文件：
   ```bash
   touch notes.txt todo.txt
   ls -l
   ```
   预期现象：目录中会出现两个空文件。

5. 练习目录跳转：
   ```bash
   cd ..
   pwd
   cd day8
   pwd
   cd ~
   pwd
   ```
   说明：`..` 表示上一级目录，`~` 表示当前用户家目录。

6. 用绝对路径与相对路径分别进入同一个目录：
   ```bash
   cd /home/$USER/week2-lab/day8
   pwd
   cd ~/week2-lab
   cd day8
   pwd
   ```

### 常见坑与提醒
- `cd /tmp` 不是进入“桌面”，而是进入临时目录。
- 不要因为看到系统目录就随便 `cd /etc` 后乱编辑文件。
- 在删除或移动文件前，先用 `pwd` 和 `ls` 确认自己在哪。

### 练习
1. **基础练习**：在 `~/week2-lab/day8` 下再创建一个 `images/` 目录和一个 `readme.md` 文件。  
   验证方式：执行 `ls -la ~/week2-lab/day8`，应能看到 `images` 和 `readme.md`。
2. **路径练习**：先回到家目录，再只用相对路径进入 `~/week2-lab/day8/images`。  
   参考验证：如果最后 `pwd` 输出以 `/week2-lab/day8/images` 结尾，说明成功。

### 推荐资料
- **必读｜文件系统标准**：Filesystem Hierarchy Standard 3.0  
  来源链接：https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html
- **必读｜目录层级手册**：file-hierarchy(7)  
  来源链接：https://www.man7.org/linux/man-pages/man7/file-hierarchy.7.html
- **选读｜命令行入门**：The Linux command line for beginners  
  来源链接：https://ubuntu.com/tutorials/command-line-for-beginners

### 当日产出
- `notes/day8-filesystem.md`

---

## Day 9｜文件查看、复制移动、查找与安全删除

### 学习目标
- 掌握 `cat`、`less`、`cp`、`mv`、`rm`、`find` 的基础使用。
- 理解“查看文件”和“查找文件”是两个不同动作。
- 建立删除前先确认路径的习惯。

### 先理解：为什么这一课重要
很多初学者会把“找文件”“看内容”“移动文件”“删文件”混在一起。今天的目标就是把这些动作拆清楚：
- **看内容**：`cat`、`less`
- **复制/移动**：`cp`、`mv`
- **查找位置**：`find`
- **删除**：`rm`

### 任务安排
- 在练习目录里写入几行文本。
- 练习查看、复制、重命名。
- 学会按名字查找文件。
- 理解为什么 `rm -rf` 不能乱用。

### 操作步骤
1. 进入昨天的练习目录：
   ```bash
   cd ~/week2-lab/day8
   ```

2. 写入测试内容：
   ```bash
   echo 'hello linux' > notes.txt
   echo 'line 2' >> notes.txt
   cat notes.txt
   ```
   预期现象：`cat` 应打印两行文本。

3. 用 `less` 查看文件：
   ```bash
   less notes.txt
   ```
   说明：按 `q` 退出。`less` 适合看长文本，`cat` 更适合看短文件。

4. 复制与重命名文件：
   ```bash
   cp notes.txt notes-copy.txt
   mv todo.txt todo-old.txt
   ls -l
   ```

5. 建一个子目录并移动文件进去：
   ```bash
   mkdir -p archive
   mv notes-copy.txt archive/
   ls -l archive
   ```

6. 用 `find` 查找文件：
   ```bash
   find ~/week2-lab -name 'notes.txt'
   find ~/week2-lab -name '*.txt'
   ```
   预期现象：第一条会找到具体文件，第二条会列出所有 `.txt` 文件。

7. 删除一个明确知道用途的测试文件：
   ```bash
   rm todo-old.txt
   ls -l
   ```

### 常见坑与提醒
- `rm` 删除后默认不会进回收站。
- `rm -rf` 破坏性非常强，不要在教程练习里把它当默认手段。
- `mv` 既可以“移动”，也可以“重命名”，看目标写法而定。
- `find` 是查位置，不是查看内容。

### 练习
1. **基础练习**：把 `notes.txt` 复制到 `archive/notes-backup.txt`。  
   验证方式：执行 `ls -l archive`，应能看到 `notes-backup.txt`。
2. **进阶练习**：在 `~/week2-lab` 下创建 `day9/logs/app.log`，再用 `find` 找到它。  
   参考答案：
   ```bash
   mkdir -p ~/week2-lab/day9/logs
   touch ~/week2-lab/day9/logs/app.log
   find ~/week2-lab -name 'app.log'
   ```

### 推荐资料
- **必读｜命令行入门**：Linux Journey  
  来源链接：https://linuxjourney.com/
- **必读｜官方教程**：The Linux command line for beginners  
  来源链接：https://ubuntu.com/tutorials/command-line-for-beginners
- **选读｜中文命令整理**：Linux 常用基础命令（2024 年最新篇）  
  来源链接：https://cloud.tencent.com/developer/article/2424112

### 当日产出
- `notes/day9-file-ops-and-find.md`

---

## Day 10｜权限、用户组与 Permission denied

### 学习目标
- 看懂 `ls -l` 输出中的权限位。
- 理解文件与目录的 `rwx` 含义不同。
- 会使用 `chmod`、`chown`、`chgrp` 的基础形式。
- 能排查最常见的 `Permission denied`。

### 先理解：权限到底在控制什么
Linux 会从“谁在操作”和“操作什么对象”两个方向判断权限。

最常见的三类身份：
- **owner**：文件所有者
- **group**：所属用户组
- **others**：其他用户

最常见的三类权限：
- `r`：读
- `w`：写
- `x`：执行

### `ls -l` 怎么看
例如：
```bash
-rwxr-xr-- 1 akari dev 25 Mar 26 10:00 script.sh
```
可以先只拆成四块：
- 第一位 `-`：普通文件；如果是 `d` 表示目录。
- `rwx`：owner 权限。
- `r-x`：group 权限。
- `r--`：others 权限。

### 文件和目录权限的区别
- 对**文件**来说：
  - `r`：可读内容
  - `w`：可改内容
  - `x`：可执行
- 对**目录**来说：
  - `r`：可列出目录内容
  - `w`：可在目录内创建、删除、改名
  - `x`：可进入目录

这就是为什么“目录没有 `x`，你可能连 `cd` 进去都不行”。

### 任务安排
- 创建一个脚本并赋执行权限。
- 分别体验数字法和符号法。
- 学会读懂 `Permission denied` 的最小排查顺序。

### 操作步骤
1. 进入练习区并创建脚本：
   ```bash
   cd ~/week2-lab
   mkdir -p day10
   cd day10
   printf '#!/bin/bash\necho hello permission\n' > script.sh
   ls -l script.sh
   ```
   预期现象：刚创建时通常还没有执行权限。

2. 尝试直接执行：
   ```bash
   ./script.sh
   ```
   可能现象：会看到 `Permission denied`。

3. 赋执行权限后再运行：
   ```bash
   chmod u+x script.sh
   ls -l script.sh
   ./script.sh
   ```
   预期现象：能输出 `hello permission`。

4. 用数字法设置普通文本文件权限：
   ```bash
   touch notes.txt
   chmod 644 notes.txt
   ls -l notes.txt
   ```
   说明：`644` 常见含义是 owner 可读写，group 和 others 只读。

5. 认识组权限修改：
   ```bash
   chgrp $(id -gn) notes.txt
   ls -l notes.txt
   ```
   说明：这里把文件组改成你当前用户所在的主组，适合安全演示。

6. 只读理解 `chown` 语法，不强求在普通用户环境执行：
   ```bash
   chown user:group file
   ```
   说明：通常需要 root 或 `sudo`。如果你不是管理员，知道语法和使用边界就够了。

### `Permission denied` 最小排查顺序
1. 我是不是在操作一个需要更高权限的位置？
2. 我是读失败、写失败，还是执行失败？
3. `ls -l` 看看文件或目录权限是什么？
4. 我是不是用错了用户，或者本来就不该改这个文件？
5. 只有在明确知道原因时才考虑 `sudo`。

### 常见坑与提醒
- 不要把 `chmod -R 777` 当成万能修复。
- `sudo` 不是“遇错就加”的魔法按钮。
- 修改目录权限要比修改单个文件更谨慎。
- `chown` 可能需要管理员权限，不要在系统目录里盲改所有权。

### 练习
1. **基础练习**：新建 `runme.sh`，写一行 `echo run ok`，让它从不能执行变成能执行。  
   验证方式：执行前报错，`chmod u+x runme.sh` 后可以正常输出。
2. **进阶练习**：创建目录 `private-dir`，设置为只有自己可访问。  
   参考答案：
   ```bash
   mkdir private-dir
   chmod 700 private-dir
   ls -ld private-dir
   ```
   自检：权限应类似 `drwx------`。

### 推荐资料
- **必读｜官方文档**：GNU Coreutils: chmod invocation  
  来源链接：https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html
- **必读｜官方文档**：GNU Coreutils: chown invocation  
  来源链接：https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html
- **选读｜新手解释**：An Introduction to Linux Permissions  
  来源链接：https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-permissions

### 当日产出
- `notes/day10-permissions.md`

---

## Day 11｜进程、前后台任务与服务状态查看

### 学习目标
- 理解进程、PID、前台任务、后台任务、服务的区别。
- 会使用 `ps`、`top`、`grep`、`kill`、`jobs`、`bg`、`fg`、`&`。
- 知道 `systemctl status` 是看服务状态，不是看所有普通进程。

### 先理解：进程和服务不是一回事
- **进程**：正在运行中的程序实例，每个进程有自己的 PID。
- **前台任务**：当前终端正在直接占用的任务。
- **后台任务**：任务仍在跑，但终端暂时能做别的事。
- **服务**：通常由系统统一管理的长期运行程序，例如 `sshd`、`nginx`。

### 任务安排
- 先学会看进程，再学会结束进程。
- 练习前后台切换。
- 认识系统服务状态查看命令。

### 操作步骤
1. 查看系统进程快照：
   ```bash
   ps -ef | head
   ```
   说明：`ps` 更像“拍一张快照”。

2. 查找某个进程：
   ```bash
   ps -ef | grep ssh
   ```
   说明：通常会连 `grep ssh` 自己也显示出来，这是正常现象。

3. 实时观察系统状态：
   ```bash
   top
   ```
   说明：按 `q` 退出。`top` 更像“实时监控画面”。

4. 启动一个后台任务：
   ```bash
   sleep 300 &
   jobs
   ```
   预期现象：`jobs` 会显示一个后台任务。

5. 找到这个任务对应的 PID：
   ```bash
   ps -ef | grep sleep
   ```

6. 优先用正常方式结束：
   ```bash
   kill PID
   ```
   说明：默认发送的是 `TERM`，表示“请正常退出”。

7. 体验前后台切换：
   ```bash
   sleep 300
   ```
   运行后按 `Ctrl+Z` 暂停，再执行：
   ```bash
   jobs
   bg %1
   jobs
   fg %1
   ```

8. 看一个系统服务状态：
   ```bash
   systemctl status ssh
   ```
   或者在部分系统里：
   ```bash
   systemctl status sshd
   ```
   说明：不同发行版服务名可能不同；Ubuntu 常见 `ssh`，RHEL 系常见 `sshd`。

### 安全提醒
- `kill -9` 是最后手段，不是默认手段。
- 不要随便 `kill` 掉看不懂的系统进程。
- 后台任务不等于“永远不会断”；关闭终端后，许多任务仍可能结束。后续若要学长任务保活，再补 `nohup` / `tmux`。

### 练习
1. **基础练习**：启动一个 `sleep 120 &`，再用 `jobs` 和 `kill` 把它结束。  
   验证方式：结束后再执行 `jobs`，该任务应消失。
2. **进阶练习**：尝试查看 SSH 服务状态。  
   验证方式：`systemctl status ssh` 或 `systemctl status sshd` 至少有一个能返回服务状态信息；若提示服务名不存在，记录你所在系统的正确服务名即可。

### 推荐资料
- **必读｜手册页**：ps(1)  
  来源链接：https://www.man7.org/linux/man-pages/man1/ps.1.html
- **必读｜手册页**：kill(1)  
  来源链接：https://www.man7.org/linux/man-pages/man1/kill.1.html
- **必读｜作业控制**：Job Control Basics  
  来源链接：https://www.gnu.org/software/bash/manual/html_node/Job-Control-Basics.html
- **选读｜流程化教程**：How To Use ps, kill, and nice to Manage Processes in Linux  
  来源链接：https://www.digitalocean.com/community/tutorials/how-to-use-ps-kill-and-nice-to-manage-processes-in-linux

### 当日产出
- `notes/day11-process-and-service.md`

---

## Day 12｜软件安装与包管理：apt、dnf、yum

### 学习目标
- 理解包管理器是“安装、升级、删除软件”的标准入口。
- 至少认识 Debian/Ubuntu 常见的 `apt`，以及 RHEL/Fedora 系常见的 `dnf` / `yum`。
- 会做更新、搜索、安装、卸载和安装后验证。

### 先理解：为什么不能到处手动下载二进制
Linux 里很多软件都可以通过包管理器安装。好处是：
- 依赖关系更容易处理。
- 升级和卸载更统一。
- 更容易复现别人给你的教程步骤。

### 发行版差异先记住
- **Debian / Ubuntu 常用**：`apt`
- **Fedora / RHEL 8+ / Rocky / AlmaLinux 常用**：`dnf`
- **较老的 CentOS / RHEL 7 资料中常见**：`yum`

### 任务安排
- 确认自己是哪类系统。
- 学会更新索引、搜索包、安装包、删除包。
- 安装后用 `--version` 或运行命令验证。

### 操作步骤
1. 先看系统大概属于哪一类：
   ```bash
   cat /etc/os-release
   ```

2. 如果你是 Debian / Ubuntu：
   ```bash
   sudo apt update
   apt search tree
   sudo apt install tree
   tree --version
   sudo apt remove tree
   ```
   说明：`apt(8)` 说明 `apt` 是更偏交互式的高层命令接口，适合终端手工操作。

3. 如果你是 Fedora / RHEL / Rocky / AlmaLinux：
   ```bash
   sudo dnf search tree
   sudo dnf install tree
   tree --version
   sudo dnf remove tree
   ```
   如果系统较旧，也可能看到：
   ```bash
   sudo yum install tree
   ```

4. 安装 `curl` 或 `git` 时也可以用同样思路：
   ```bash
   curl --version
   git --version
   ```
   说明：安装后一定要做版本检查或实际运行，不能只看“安装命令没报错”。

### 常见坑与提醒
- `update` 往往是更新软件包索引，不等于“系统已经升级完”。
- 没有 `sudo` 权限时，很多安装命令会失败，这不是命令错了，而是权限不够。
- 网络源不可达时，可能会出现下载失败或超时。
- 不同系统命令不同，不要把 `apt install` 硬套到 RHEL 系发行版上。

### 练习
1. **基础练习**：确认你的系统应该用 `apt` 还是 `dnf/yum`。  
   验证方式：查看 `cat /etc/os-release` 输出中的 `ID` 或 `ID_LIKE`。
2. **实操练习**：安装一个小工具（如 `tree` 或 `curl`），再验证版本。  
   参考验证：如果 `tree --version` 或 `curl --version` 有输出，说明安装成功。

### 推荐资料
- **必读｜Debian 手册页**：apt(8)  
  来源链接：https://manpages.debian.org/apt
- **必读｜Debian Handbook**：The APT Tools  
  来源链接：https://debian-handbook.info/browse/stable/apt.html
- **必读｜Red Hat 文档**：DNF commands list  
  来源链接：https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/dnf-commands-list
- **选读｜Fedora Docs**：Using the DNF software package manager  
  来源链接：https://docs.fedoraproject.org/en-US/quick-docs/dnf/

### 当日产出
- `notes/day12-package-manager.md`

---

## Day 13｜SSH 基础：连接、端口、密钥与 known_hosts

### 学习目标
- 会读懂 `ssh user@host` 这类连接命令。
- 理解密码登录与密钥登录的差异。
- 认识 `~/.ssh`、公钥、私钥、`known_hosts` 的作用。
- 会用 `-p` 指定端口、用 `-i` 指定私钥。

### 先理解：SSH 命令长什么样
最常见形式：
```bash
ssh user@host
```
可以拆成两部分：
- `user`：远程主机上的用户名
- `host`：远程主机地址，可以是 IP 或域名

如果不是默认 22 端口，可以写：
```bash
ssh -p 2222 user@host
```
如果想显式指定私钥：
```bash
ssh -i ~/.ssh/id_ed25519 user@host
```

### 密码登录 vs 密钥登录
- **密码登录**：输入远程账户密码。
- **密钥登录**：本地保存私钥，远程保存对应公钥。通常更方便，也更适合长期使用。

推荐密钥登录的原因：
- 不用每次手输密码。
- 可以配合更严格的服务端策略。
- 更适合和 GitHub 等平台集成。

### `~/.ssh` 里常见的文件
- `id_ed25519`：私钥，**不能泄露**。
- `id_ed25519.pub`：公钥，可以发给服务器或平台。
- `known_hosts`：你连接过的主机指纹记录。
- `config`：SSH 客户端配置文件。

### 任务安排
- 生成一对 SSH 密钥。
- 学会首次连接时的确认逻辑。
- 认识 host key 校验为什么重要。

### 操作步骤
1. 查看本地 SSH 目录：
   ```bash
   ls -la ~/.ssh
   ```
   如果目录不存在可先创建：
   ```bash
   mkdir -p ~/.ssh
   chmod 700 ~/.ssh
   ```

2. 生成一对新密钥：
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   预期现象：会提示保存路径，默认通常是 `~/.ssh/id_ed25519`。

3. 查看公钥内容：
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
   说明：复制的是 `.pub`，不是私钥文件本体。

4. 首次连接远程主机：
   ```bash
   ssh user@host
   ```
   可能会看到：
   ```text
   The authenticity of host 'host (x.x.x.x)' can't be established.
   Are you sure you want to continue connecting (yes/no/[fingerprint])?
   ```
   说明：这不是报错，而是在让你确认主机指纹。

5. 指定端口连接：
   ```bash
   ssh -p 2222 user@host
   ```

6. 连接 GitHub 测试 SSH：
   ```bash
   ssh -T git@github.com
   ```
   预期现象：首次也会有 host key 确认；成功后通常会看到认证提示信息。

### 安全提醒
- 私钥文件不要发给别人，也不要提交到 Git 仓库。
- 不要把“关闭 host key 校验”写成默认方案。
- `ssh -A` 是 agent forwarding，官方手册明确提示要谨慎使用。

### 练习
1. **基础练习**：确认你的 `~/.ssh` 目录权限是安全的。  
   验证方式：执行 `ls -ld ~/.ssh`，推荐看到 `drwx------` 或等价的 700 权限。
2. **实操练习**：如果你有 GitHub 账号，尝试执行 `ssh -T git@github.com`。  
   验证方式：看到主机指纹确认或认证反馈即可；如果失败，把完整报错抄到笔记中，第二天继续排查。

### 推荐资料
- **必读｜手册页**：ssh(1)  
  来源链接：https://www.man7.org/linux/man-pages/man1/ssh.1.html
- **必读｜GitHub 官方**：Connecting to GitHub with SSH  
  来源链接：https://docs.github.com/en/authentication/connecting-to-github-with-ssh
- **选读｜SSH 入门**：SSH Essentials  
  来源链接：https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys

### 当日产出
- `notes/day13-ssh-basic.md`

---

## Day 14｜系统课程 2：SSH 常见报错排查与第 2 周综合练习

### 学习目标
- 按固定顺序排查 SSH 常见错误，而不是乱试命令。
- 识别 `Connection timed out`、`Connection refused`、`Permission denied`、`REMOTE HOST IDENTIFICATION HAS CHANGED` 等常见报错。
- 用一套综合练习把“文件系统、权限、进程、包管理、SSH”串起来。

### 先记住这套排查顺序
遇到 SSH 问题时，先按顺序查，不要一上来就删配置：
1. 网络是否通？主机地址是否写对？
2. 端口是否对？
3. SSH 服务是否在运行？
4. 用户名是否对？
5. 认证方式是否对？是密码、密钥，还是私钥路径错了？
6. 私钥与 `~/.ssh` 权限是否合理？
7. 是不是主机指纹变化了？

### 常见报错速查表

#### 1. `Connection timed out`
**现象**：长时间无响应，最后超时。  
**常见原因**：
- IP 或域名写错
- 网络不通
- 目标端口被防火墙拦住
- 目标主机没开机或不在网

**怎么确认**：
- 先检查地址和端口是不是填错
- 如果你有服务器控制台权限，确认机器在线
- 如可登录另一台跳板机，可从那边再测网络

**怎么修复**：
- 改正主机地址
- 确认安全组/防火墙开放了 SSH 端口
- 确认正确使用 `-p 端口`

**修复后如何验证**：
```bash
ssh -p 端口 user@host
```
能进入密码提示、指纹确认或认证阶段，通常就比“超时”更前进了一步。

#### 2. `Connection refused`
**现象**：很快返回拒绝连接。  
**常见原因**：
- 主机在线，但该端口没有 SSH 服务监听
- SSH 服务未启动
- 端口写错，例如服务实际跑在 2222，你却连 22

**怎么确认**：
- 在服务器本机执行：
  ```bash
  systemctl status ssh
  ```
  或：
  ```bash
  systemctl status sshd
  ```
- 核对 SSH 端口配置

**怎么修复**：
- 启动 SSH 服务
- 用正确端口重连

**修复后如何验证**：
再次执行 `ssh -p 端口 user@host`，若不再出现 refused，说明服务或端口问题已改善。

#### 3. `Permission denied` / `Permission denied (publickey)`
**现象**：连得上，但认证失败。  
**常见原因**：
- 用户名写错
- 私钥路径不对
- 远程没放对应公钥
- 本地 `~/.ssh` 或私钥权限太宽松
- 服务器只允许密钥登录，而你还在尝试密码

**怎么确认**：
- 检查用户名是不是远程真实存在的账户
- 检查本地有没有对应私钥：
  ```bash
  ls -la ~/.ssh
  ```
- 必要时显式指定私钥：
  ```bash
  ssh -i ~/.ssh/id_ed25519 user@host
  ```

**怎么修复**：
- 改正用户名
- 重新上传公钥到远程主机或 GitHub
- 修正权限：
  ```bash
  chmod 700 ~/.ssh
  chmod 600 ~/.ssh/id_ed25519
  chmod 644 ~/.ssh/id_ed25519.pub
  ```

**修复后如何验证**：
重新连接，若进入 shell 或得到平台认证成功提示，说明问题已解决。

#### 4. `REMOTE HOST IDENTIFICATION HAS CHANGED`
**现象**：SSH 明确警告远程主机指纹变化。  
**这意味着什么**：
- 目标机器可能重装过系统
- 你连到的主机不是之前那台
- 也可能存在中间人风险，所以不能无脑忽略

**怎么确认**：
- 先确认服务器是否真的重建、换机、换 IP
- 与可信渠道提供的主机指纹核对

**怎么修复**：
在确认主机变化是可信且正常之后，再删除旧记录，例如：
```bash
ssh-keygen -R host
```
如果你用的是 IP，也可写 IP：
```bash
ssh-keygen -R x.x.x.x
```
然后重新连接，让 SSH 记录新的主机指纹。

**不要这么做**：
- 不要没确认来源就随便删除 `known_hosts` 全文件
- 不要把“关闭 host key 校验”当成教程默认答案

### 第 2 周综合练习

#### 练习 A：本地 Linux 基础闭环
1. 在 `~/week2-lab/final` 下创建 `docs/`、`scripts/`、`logs/` 三个目录。
2. 创建 `docs/README.md` 并写 3 行文字。
3. 创建 `scripts/check.sh`，内容为：
   ```bash
   #!/bin/bash
   echo week2 check ok
   ```
4. 给脚本执行权限并运行。
5. 用 `find` 找到所有 `.sh` 文件。
6. 安装一个小工具（如 `tree`）并验证版本。

**自检答案**：
- `ls -l scripts/check.sh` 应显示可执行位。
- `./scripts/check.sh` 应输出 `week2 check ok`。
- `find ~/week2-lab/final -name '*.sh'` 应至少找到 `check.sh`。

#### 练习 B：SSH 排障记录练习
1. 尝试执行一次 `ssh user@host` 或 `ssh -T git@github.com`。
2. 如果成功，记录成功前出现了什么提示。
3. 如果失败，把完整报错原文抄到笔记里。
4. 按“网络 → 端口 → 服务 → 用户名 → 认证方式 → 密钥权限 → 主机指纹”的顺序写排查笔记。

**验证方式**：
- 笔记里必须出现完整报错原文，而不是只写“连不上”。
- 笔记里必须出现至少 3 个你已经检查过的点。

### 推荐资料
- **必读｜手册页**：ssh(1)  
  来源链接：https://www.man7.org/linux/man-pages/man1/ssh.1.html
- **必读｜GitHub 官方**：Connecting to GitHub with SSH  
  来源链接：https://docs.github.com/en/authentication/connecting-to-github-with-ssh
- **选读｜SSH 入门与排障补充**：SSH Essentials  
  来源链接：https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys

### 复盘作业
- 用自己的话解释：绝对路径、`chmod 755`、PID、包管理器、公钥/私钥、`known_hosts` 分别是什么。
- 列出你本周最常用的 8 条命令，并为每条命令写一个场景。
- 如果本周出现过 `Permission denied` 或 SSH 报错，记录原文、原因、修复方法、修复后验证方法。

### 当日产出
- `notes/week2-review.md`

---

# 第 3 周：GitHub 协作与 AI 编程工作流

## Day 15｜GitHub 协作全景：Issue、分支、PR

### 学习目标
- 理解 GitHub 协作不是“直接改主分支”。
- 知道 Issue、Branch、Pull Request 的关系。
- 能描述共享仓库模型与 fork 模型的差异。

### 任务安排
- 阅读 GitHub 协作文档。
- 画出 Issue → Branch → PR → Merge 的流程图。
- 打开一个开源仓库，观察它的 Issue 和 PR 页面。

### 操作步骤
1. 阅读 GitHub 协作模型文档。
2. 打开一个熟悉项目的 Pull Requests 页面。
3. 观察 PR 中的 Conversation、Commits、Checks 三个区域。
4. 在笔记中写下“为什么协作要先开分支”。
5. 为自己的练习仓库创建一个待办 issue。

### 推荐资料
- **必读｜官方协作模型**：About collaborative development models  
  来源链接：https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models
- **必读｜官方 PR 说明**：About pull requests  
  来源链接：https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- **选读｜开源贡献入口**：Contributing to open source  
  来源链接：https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source

### 当日产出
- `notes/day15-github-collaboration.md`

---

## Day 16｜Feature Branch 与第一个 Pull Request

### 学习目标
- 会基于小任务创建功能分支。
- 会提交一个最小 PR。
- 理解“小 PR 更容易 review”的原因。

### 任务安排
- 在练习仓库中创建 feature branch。
- 修改 README 或新增一个小文件。
- 提交 PR 并填写说明。

### 操作步骤
1. 执行 `git switch -c feature/update-readme`。
2. 做一个尽量小的改动，例如补充 README 的一段说明。
3. 提交并推送该分支。
4. 在 GitHub 上发起 PR。
5. 按“改了什么、为什么改、怎么验证”的格式写 PR 描述。

### 推荐资料
- **必读｜实践工作流**：Git Feature Branch Workflow  
  来源链接：https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow
- **必读｜官方 PR 说明**：About pull requests  
  来源链接：https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- **选读｜如何让 PR 更易 review**：Helping others review your changes  
  来源链接：https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes

### 当日产出
- 第一个 PR 链接
- `notes/day16-first-pr.md`

---

## Day 17｜读懂一个开源项目：README、CONTRIBUTING、目录结构

### 学习目标
- 学会从陌生仓库提取关键信息。
- 知道 README 和 CONTRIBUTING 是两个高回报入口。
- 能写出一页项目阅读笔记。

### 任务安排
- 选择一个中小型开源仓库。
- 阅读 README、CONTRIBUTING、根目录结构。
- 写出项目定位、入口和协作方式。

### 操作步骤
1. 先看 README：项目做什么、怎么运行、面向谁。
2. 再看 CONTRIBUTING：怎样提 issue、提 PR、遵守什么规范。
3. 浏览根目录，记录 `src/`、`docs/`、`tests/`、配置文件。
4. 看最近 5–10 条提交与 3 个 issue/PR 标题。
5. 输出一页项目阅读总结。

### 推荐资料
- **必读｜项目导向方法**：How to Contribute to Open Source  
  来源链接：https://opensource.guide/how-to-contribute/
- **必读｜真实案例**：Visual Studio Code README  
  来源链接：https://raw.githubusercontent.com/microsoft/vscode/main/README.md
- **选读｜真实案例**：Visual Studio Code CONTRIBUTING  
  来源链接：https://raw.githubusercontent.com/microsoft/vscode/main/CONTRIBUTING.md

### 当日产出
- `notes/day17-project-reading.md`

---

## Day 18｜基础工程实践：格式化、Lint、最小验证

### 学习目标
- 理解 formatter 与 linter 的分工。
- 建立“提交前最小验证”的习惯。
- 明白工程实践不是复杂流程，而是降低出错成本。

### 任务安排
- 了解 Prettier 与 ESLint 的角色。
- 为一个示例项目写出最小自检清单。
- 在笔记中定义“提交前必须做的三件事”。

### 操作步骤
1. 阅读 Prettier 文档首页，理解“格式交给工具”。
2. 阅读 ESLint 入门页，理解“静态检查发现问题”。
3. 写下 formatter 与 linter 的区别。
4. 为你的练习仓库补一段 README：如何运行、如何验证。
5. 定义自己的提交前清单：运行、看 diff、写说明。

### 推荐资料
- **必读｜格式化工具**：Prettier Docs  
  来源链接：https://prettier.io/docs/
- **必读｜静态检查**：Getting Started with ESLint  
  来源链接：https://eslint.org/docs/latest/use/getting-started
- **选读｜协作规范**：Open Source Guides CONTRIBUTING  
  来源链接：https://raw.githubusercontent.com/github/opensource.guide/main/CONTRIBUTING.md

### 当日产出
- `notes/day18-engineering-basics.md`

---

## Day 19｜日志与排错：不要只靠 print

### 学习目标
- 理解 logging 与 print 的区别。
- 知道最小排错过程：重现、观察、记录、修复、验证。
- 为后续 AI 辅助调试建立基本表达方式。

### 任务安排
- 阅读 Python Logging HOWTO。
- 写一个带日志输出的小脚本。
- 记录一次“故意制造错误 → 定位 → 修复”的过程。

### 操作步骤
1. 写一个简单 Python 脚本，包含输入、输出与异常分支。
2. 用 `logging.info()`、`logging.error()` 代替纯 `print()`。
3. 故意制造一个错误输入。
4. 观察日志输出并写下定位思路。
5. 修复后重新运行并确认结果正确。

### 推荐资料
- **必读｜官方文档**：Python Logging HOWTO  
  来源链接：https://docs.python.org/3/howto/logging.html
- **必读｜工程习惯补充**：Visual Studio Code CONTRIBUTING  
  来源链接：https://raw.githubusercontent.com/microsoft/vscode/main/CONTRIBUTING.md
- **选读｜新手协作意识**：How to Contribute to Open Source  
  来源链接：https://opensource.guide/how-to-contribute/

### 当日产出
- `projects/logging-demo.py`
- `notes/day19-logging-and-debugging.md`

---

## Day 20｜Cursor 入门：Ask、Edit、Agent 的区别

### 学习目标
- 理解 Cursor 是“编辑器里的 AI 工作台”。
- 会区分 Ask、Edit、Agent 三种模式。
- 知道自动上下文、应用更改、检查点分别解决什么问题。

### 任务安排
- 阅读 Cursor Chat 概述。
- 列出三种模式各适合什么场景。
- 让 AI 帮你解释一段代码，并观察它给出的变更方式。

### 操作步骤
1. 打开 Cursor 文档中的聊天概述页面。
2. 记录 Ask、Edit、Agent 的定义。
3. 理解 `@` 上下文、自动上下文、Apply、检查点的作用。
4. 用一段自己的代码测试 Ask 模式，让它解释功能。
5. 在笔记中写明：为什么“先看 diff 再接受”很重要。

### 推荐资料
- **必读｜中文官方**：Cursor 聊天概述  
  来源链接：https://docs.cursor.ac.cn/chat/overview
- **必读｜总入口**：Cursor Docs  
  来源链接：https://cursor.com/docs
- **选读｜官方规则入口**：Cursor AI 规则  
  来源链接：https://docs.cursor.ac.cn/context/rules-for-ai

### 当日产出
- `notes/day20-cursor-overview.md`

---

## Day 21｜系统课程 3：AI 编程工作流与仓库协作实践

### 学习目标
- 形成“读仓库 → 开分支 → AI 辅助改动 → 看 diff → 验证 → 提 PR”的闭环。
- 理解 Agent 强大但必须受规则与验证约束。

### 系统课程内容
- 回顾 GitHub Flow、PR、项目阅读、基础工程实践。
- 讲解 Cursor Agent 能做什么：读写代码、搜索代码库、运行终端、自动网页搜索。
- 讲解风险边界：Yolo 模式、自动运行命令、防护栏、规则文件。
- 演示一个小改动流程：解释需求 → AI 生成 → 人工核验 → 提交 PR。

### 操作步骤
1. 为练习仓库创建一个小任务，如“补充 README 的运行步骤”或“增加一个简单脚本”。
2. 在 Cursor 中使用 Ask 或 Agent 辅助完成其中 1 个环节。
3. 检查 diff，并做一次最小运行验证。
4. 把改动提交到分支并发起 PR。
5. 写一份《我当前的 AI 编程工作流》。

### 推荐资料
- **必读｜中文官方**：Cursor Agent  
  来源链接：https://docs.cursor.ac.cn/chat/agent
- **必读｜中文官方**：Cursor AI 规则  
  来源链接：https://docs.cursor.ac.cn/context/rules-for-ai
- **选读｜PR 协作规范**：Helping others review your changes  
  来源链接：https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes

### 复盘作业
- 用自己的话写出 AI 编程最小闭环：任务、上下文、生成、验证、提交。
- 列出 3 个适合交给 AI 的任务，和 3 个不能盲交给 AI 的任务。
- 附上本周 PR 链接。

### 当日产出
- `notes/week3-review.md`
- 一个带 PR 的仓库改动

---

# 第 4 周：深度学习入门与综合结课

## Day 22｜深度学习到底在做什么

### 学习目标
- 建立数据、张量、模型、训练、推理的最小概念框架。
- 理解深度学习不是“神秘黑箱”，而是“数据 + 参数 + 优化”的过程。
- 能用自己的话解释训练和推理的区别。

### 任务安排
- 阅读 PyTorch 60 分钟入门概览。
- 记录 10 个关键词。
- 用生活化例子解释分类任务。

### 操作步骤
1. 阅读 PyTorch 中文“60 分钟闪电入门”首页。
2. 在笔记中解释：tensor、dataset、model、epoch、loss、optimizer、inference。
3. 用“猫狗分类”或“手写数字识别”写一个训练/推理例子。
4. 画一张“数据 → 模型 → 损失 → 更新参数 → 推理”的流程图。
5. 写出你目前最不懂的 3 个术语。

### 推荐资料
- **必读｜中文官方**：PyTorch 深度学习：60 分钟闪电入门  
  来源链接：https://docs.pytorch.ac.cn/tutorials/beginner/deep_learning_60min_blitz.html
- **必读｜官方英文入口**：Deep Learning with PyTorch: A 60 Minute Blitz  
  来源链接：https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- **选读｜中文系统教程**：深入浅出 PyTorch  
  来源链接：https://github.com/datawhalechina/thorough-pytorch

### 当日产出
- `notes/day22-dl-concepts.md`

---

## Day 23｜张量与 PyTorch 环境

### 学习目标
- 准备最小 PyTorch 运行环境。
- 理解张量是多维数组及其基本属性。
- 能执行几个最基础的张量操作。

### 任务安排
- 安装或进入可用的 PyTorch 环境。
- 运行张量创建、加法、变形示例。
- 记录 `shape`、`dtype`、`device`。

### 操作步骤
1. 按 PyTorch 官方说明安装 `torch`。
2. 新建一个脚本或 notebook。
3. 创建两个简单张量并做相加操作。
4. 试试 `reshape/view` 或打印形状。
5. 记录张量与 Python 列表的差异。

### 推荐资料
- **必读｜中文官方**：PyTorch 深度学习：60 分钟闪电入门  
  来源链接：https://docs.pytorch.ac.cn/tutorials/beginner/deep_learning_60min_blitz.html
- **必读｜中文系统教程**：深入浅出 PyTorch 在线文档  
  来源链接：https://datawhalechina.github.io/thorough-pytorch/
- **选读｜配套仓库**：thorough-pytorch README  
  来源链接：https://github.com/datawhalechina/thorough-pytorch

### 当日产出
- `projects/day23-tensor-practice.py` 或 `.ipynb`
- `notes/day23-tensors.md`

---

## Day 24｜神经网络最小直觉：输入、层、输出、损失

### 学习目标
- 理解模型是一组可学习参数。
- 知道前向传播、损失计算、反向传播的基本位置。
- 能读懂一个最小神经网络示例。

### 任务安排
- 阅读 PyTorch 神经网络教程。
- 摘录一个最小网络结构。
- 用自己的话解释 loss 为什么会影响参数更新。

### 操作步骤
1. 打开 PyTorch 中文“神经网络”教程。
2. 阅读 `nn.Module`、`forward()`、卷积层/线性层的基本示例。
3. 记录训练的基本步骤：定义模型 → 前向 → 计算损失 → 反向传播 → 更新参数。
4. 把示例代码中的模块名称写成自然语言解释。
5. 在笔记里写一段“训练其实是在调参数”的直觉说明。

### 推荐资料
- **必读｜中文官方**：神经网络 — PyTorch 教程  
  来源链接：https://docs.pytorch.ac.cn/tutorials/beginner/blitz/neural_networks_tutorial.html
- **必读｜中文官方总入口**：PyTorch 深度学习：60 分钟闪电入门  
  来源链接：https://docs.pytorch.ac.cn/tutorials/beginner/deep_learning_60min_blitz.html
- **选读｜中文系统教程**：深入浅出 PyTorch  
  来源链接：https://github.com/datawhalechina/thorough-pytorch

### 当日产出
- `notes/day24-network-intuition.md`

---

## Day 25｜训练与推理：跑一个最小分类实验

### 学习目标
- 跑通一次最小训练与推理流程。
- 知道训练输出中至少要看 loss 或关键指标变化。
- 能记录实验环境、输入和结果。

### 任务安排
- 跑一个最小图像分类或示例训练脚本。
- 保存训练日志或截图。
- 对一条样本做推理并记录输出。

### 操作步骤
1. 选择 PyTorch 60 分钟入门中的训练示例或跟随 Datawhale 教程做一个最小实验。
2. 运行训练脚本，记录 epoch 和 loss 变化。
3. 取一条测试样本做推理。
4. 把运行环境、命令和输出写进报告。
5. 总结：模型“跑起来”和“结果可解释”之间有什么差别。

### 推荐资料
- **必读｜中文官方**：PyTorch 深度学习：60 分钟闪电入门  
  来源链接：https://docs.pytorch.ac.cn/tutorials/beginner/deep_learning_60min_blitz.html
- **必读｜中文系统教程**：深入浅出 PyTorch  
  来源链接：https://github.com/datawhalechina/thorough-pytorch
- **选读｜配套视频**：深入浅出 PyTorch 配套视频教程  
  来源链接：https://www.bilibili.com/video/BV1L44y1472Z

### 当日产出
- `notes/day25-mini-training-report.md`

---

## Day 26｜用 AI 工具辅助理解训练脚本

### 学习目标
- 会让 AI 帮你解释 PyTorch 代码、补注释、做小范围重构。
- 理解 AI 适合辅助学习，但不能替代实验验证。
- 形成“让 AI 解释 → 自己验证”的学习习惯。

### 任务安排
- 把训练脚本交给 AI 解释。
- 让 AI 帮你优化注释或命名。
- 重新运行脚本验证未被改坏。

### 操作步骤
1. 选择 Day 25 的训练脚本。
2. 在 Cursor 中要求 AI 按模块解释代码功能。
3. 再要求它增加注释或拆分一个小函数。
4. 比较修改前后的 diff。
5. 重新运行脚本，确认结果仍可复现。

### 推荐资料
- **必读｜中文官方**：Cursor 聊天概述  
  来源链接：https://docs.cursor.ac.cn/chat/overview
- **必读｜中文官方**：Cursor Agent  
  来源链接：https://docs.cursor.ac.cn/chat/agent
- **选读｜规则系统**：Cursor AI 规则  
  来源链接：https://docs.cursor.ac.cn/context/rules-for-ai

### 当日产出
- `notes/day26-ai-for-dl.md`

---

## Day 27｜结课项目日：把前 26 天串起来

### 学习目标
- 通过一个最小项目把环境、Git、GitHub、AI 工具、深度学习体验串起来。
- 完成一个可提交、可说明、可复盘的结课输出。

### 任务安排
- 选择一个结课项目方向。
- 建仓库、写 README、完成一次提交与一次推送。
- 用 AI 参与至少一个环节。

### 项目建议
1. **开发流程型项目**：
   - 在远程 Linux 上建立一个小 Python 项目
   - 用 Git 管理版本
   - 用 GitHub 发起 PR
   - 用 AI 辅助写 README、注释或小功能
2. **深度学习体验型项目**：
   - 跑通一个最小 PyTorch 分类示例
   - 用 AI 帮你解释代码和修小问题
   - 用 GitHub 记录实验过程

### 操作步骤
1. 明确项目目标、输入输出、目录结构。
2. 初始化仓库并写 README。
3. 完成一个最小可运行版本。
4. 让 AI 辅助一个具体环节并保留记录。
5. 推送到 GitHub，并写 `final-project-report.md`。

### 推荐资料
- **必读｜配套仓库**：深入浅出 PyTorch  
  来源链接：https://github.com/datawhalechina/thorough-pytorch
- **必读｜官方协作流程**：Hello World  
  来源链接：https://docs.github.com/en/get-started/start-your-journey/hello-world
- **选读｜Cursor 总入口**：Cursor Docs  
  来源链接：https://cursor.com/docs

### 当日产出
- 一个结课仓库
- `final-project-report.md`

---

## Day 28｜系统课程 4：结课复盘、知识地图与后续 30 天计划

### 学习目标
- 对 28 天学习内容做体系化收束。
- 形成自己的知识地图与下一阶段计划。
- 用一份复盘证明自己已经从“零基础”进入“可持续学习”。

### 系统课程内容
- 回顾四条主线：
  1. 远程连接与开发环境
  2. Linux 基础与服务器操作
  3. Git / GitHub 协作
  4. AI 编程与深度学习入门
- 用知识图整理依赖关系：环境 → 终端 → 版本管理 → 协作 → AI 工具 → 模型实验。
- 总结每一块最重要的“一个概念 + 一个动作 + 一个坑”。
- 说明后续进阶方向：Linux 进阶运维、团队 Git 规范、更完整的软件工程、更系统的机器学习数学基础。

### 操作步骤
1. 回看前 27 天所有笔记与输出物。
2. 写一篇《28 天后我已经具备的能力》。
3. 列出一个你最熟练、一个你最薄弱、一个你接下来最想补的模块。
4. 制定未来 30 天进阶计划。
5. 把最终仓库、实验记录、复盘文章汇总到一个索引页。

### 推荐资料
- **必读｜中文官方入口**：PyTorch 教程首页  
  来源链接：https://docs.pytorch.ac.cn/tutorials/index.html
- **必读｜GitHub 学习入口**：GitHub Learning resources / Hello World  
  来源链接：https://docs.github.com/en/get-started/start-your-journey/hello-world
- **选读｜课程总入口**：本教程前 27 天所有主资料回看

### 复盘作业
- 提交你的最终仓库链接或实验记录。
- 写一篇《28 天后我已经具备的能力》。
- 列出接下来 30 天的进阶计划，并按“继续练 Linux / 继续练 GitHub 协作 / 深入 AI 编程 / 系统学深度学习”四类归档。

### 当日产出
- `notes/week4-final-review.md`
- `notes/next-30-days-plan.md`

---

# 周末系统课程总表

| Day | 系统课程主题 | 必做输出 |
|---|---|---|
| Day 7 | 远程开发环境与 Linux 基础复盘 | `week1-review.md` |
| Day 14 | 从终端到 GitHub 的完整工作流 | `week2-review.md` |
| Day 21 | AI 编程工作流与仓库协作实践 | `week3-review.md` + PR |
| Day 28 | 结课复盘、知识地图与后续计划 | `week4-final-review.md` + `next-30-days-plan.md` |

# 参考资料总表

## 第 1 周：环境与 Linux 入门
- 编程学习全指南：从零基础到职业发展的实用路径  
  https://developer.cloud.tencent.com/article/2571989
- 计算机学习路线大全（2025版）  
  https://csguide.cn/roadmap/
- 使用 SSH 进行远程开发  
  https://vscode.js.cn/docs/remote/ssh
- Remote Development using SSH  
  https://code.visualstudio.com/docs/remote/ssh
- The Linux command line for beginners  
  https://ubuntu.com/tutorials/command-line-for-beginners
- Linux Journey  
  https://linuxjourney.com/

## 第 2 周：Linux 进阶与 Git
- Bash Manual: Environment  
  https://www.gnu.org/software/bash/manual/html_node/Environment.html
- Bash Manual: Redirections  
  https://www.gnu.org/software/bash/manual/html_node/Redirections.html
- GNU Coreutils: chmod invocation  
  https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html
- GNU Coreutils: chown invocation  
  https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html
- ssh(1) / scp(1) / rsync(1)  
  https://www.man7.org/linux/man-pages/man1/ssh.1.html  
  https://www.man7.org/linux/man-pages/man1/scp.1.html  
  https://www.man7.org/linux/man-pages/man1/rsync.1.html
- gittutorial / Pro Git  
  https://git-scm.com/docs/gittutorial  
  https://git-scm.com/book/zh/v2

## 第 3 周：GitHub 协作与 AI 编程
- About collaborative development models  
  https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models
- About pull requests  
  https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- Hello World  
  https://docs.github.com/en/get-started/start-your-journey/hello-world
- Cursor Docs / Chat / Agent / Rules  
  https://cursor.com/docs  
  https://docs.cursor.ac.cn/chat/overview  
  https://docs.cursor.ac.cn/chat/agent  
  https://docs.cursor.ac.cn/context/rules-for-ai
- Prettier / ESLint / Python Logging HOWTO  
  https://prettier.io/docs/  
  https://eslint.org/docs/latest/use/getting-started  
  https://docs.python.org/3/howto/logging.html

## 第 4 周：PyTorch 与结课实践
- PyTorch 深度学习：60 分钟闪电入门（中文）  
  https://docs.pytorch.ac.cn/tutorials/beginner/deep_learning_60min_blitz.html
- 神经网络（中文）  
  https://docs.pytorch.ac.cn/tutorials/beginner/blitz/neural_networks_tutorial.html
- PyTorch Tutorials（英文首页）  
  https://docs.pytorch.org/tutorials/index.html
- 深入浅出 PyTorch（Datawhale）  
  https://github.com/datawhalechina/thorough-pytorch
- 深入浅出 PyTorch 配套视频  
  https://www.bilibili.com/video/BV1L44y1472Z

# 来源与整合说明

本教程综合以下仓库内调研与外部核验结果整理而成：
- 第 1 周资料调研：`projects/zero-basics-plan/analysis/2026-03-26-week1-resource-survey-zero-basics-env-vscode-remote-ssh-linux.md`
- 第 2 周资料调研：`projects/zero-basics-plan/analysis/2026-03-26-week2-linux-ssh-git-resource-survey.md`
- 第 3 周资料调研：`projects/zero-basics-plan/analysis/2026-03-26-week3-github-collaboration-cursor-ai-workflow-research.md`
- 总路线初稿：`projects/zero-basics-plan/analysis/2026-03-26-28-day-course-outline.md`
- 第 4 周补充核验来源：PyTorch 中文教程、Datawhale 仓库 README、Cursor 中文文档

# 后续扩写建议

1. 第 1 周可继续补强知乎 / 小红书 / B 站中文案例，但正文主线已可用。
2. 第 2 周若正式扩写，可补 `systemctl/service` 与 `nohup/tmux` 的教学实验。
3. 第 4 周如需更强 AI 提示词证据，可另行补抓 OpenAI Prompt Engineering 正文或 PDF。
4. 若做正式课程版，可为每天补充“常见错误”“预计耗时”“完成打卡清单”。
