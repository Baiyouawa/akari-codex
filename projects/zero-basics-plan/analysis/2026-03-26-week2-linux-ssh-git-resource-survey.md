# 第 2 周资料调研：Linux 进阶、文件权限、进程管理、SSH/服务器常用操作、Git 基础与实战

- 调研时间：2026-03-26
- 适用项目：`projects/zero-basics-plan`
- 任务范围：Linux 进阶、文件权限、进程管理、SSH/服务器常用操作、Git 基础与实战
- 记录规范：`标题 | 主题 | 子主题 | 来源平台 | 作者/机构 | 链接 | 语言 | 发布时间/版本 | 难度 | 内容类型 | 使用级别 | 教学用途 | 教学摘要 | 备注`
- 使用级别说明：
  - **可直接引用**：来源权威、结构完整、示例稳定，适合直接进入教程正文或课堂演示
  - **需改写整理**：内容有价值但偏英文、偏长、或页面噪声较多，适合二次整理后进入教程
  - **仅供参考**：适合补充背景、练习或互动，不宜作为主教材

## 筛选口径

1. **准确性优先**：命令语义优先采用 GNU / man7 / Git 官方 / GitHub Docs / OpenSSH / Debian Handbook 等原始或准原始来源。
2. **教学友好优先**：对初学者更友好的内容优先采用廖雪峰、DigitalOcean、Atlassian 等教程型来源作为辅助层。
3. **时效性优先**：
   - `git-commit` 官方手册页显示最近更新到 `2.53.0 / 2026-02-02`，来源：`https://git-scm.com/docs/git-commit`
   - GNU Coreutils 页面显示 `9.10`，来源：`https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html`
   - GitHub Docs / man7 / Bash Manual / Debian Handbook 均为持续维护页面，抓取时间为 2026-03-26。
4. **安全性约束**：不采用鼓励弱密码、关闭 host key 校验、无差别 `chmod -R 777`、直接 `kill -9` 作为默认方案的材料。
5. **课程映射导向**：每条资料都要能落到第 2 周某个教学环节，而不是纯收藏链接。

## 多平台筛选结论总览

| 平台类型 | 代表来源 | 结论 | 适用角色 | 备注 |
|---|---|---|---|---|
| 官方文档 / 手册 | git-scm.com, GitHub Docs, GNU Coreutils, Bash Manual, man7, Debian Handbook | 入选为主资料 | 讲师、教材编写者 | 准确性最高，但部分内容需中文化整理 |
| 教程网站 | DigitalOcean, Atlassian | 入选为辅助资料 | 学生、助教 | 实操感强，但需去除站点噪声并提炼重点 |
| 中文系统教程 | 廖雪峰 Git 教程 | 入选为中文友好辅助资料 | 零基础学习者 | 适合 Git 入门解释与操作路径 |
| 互动仓库 / 游戏 | Learn Git Branching, Oh My Git! | 入选为练习 / 拓展 | 学生课后练习 | 不适合作为唯一主教材 |
| 低质量候选类型 | 转载页、无来源帖子、碎片化问答 | 淘汰 | 无 | 不满足可追溯性与结构完整性 |

## 统一资料总表

| 标题 | 主题 | 子主题 | 来源平台 | 作者/机构 | 链接 | 语言 | 发布时间/版本 | 难度 | 内容类型 | 使用级别 | 教学用途 | 教学摘要 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bash Reference Manual: Redirections | Linux 进阶 | 重定向 | GNU Bash Manual | GNU Project | https://www.gnu.org/software/bash/manual/html_node/Redirections.html | 英文 | Bash Reference Manual（持续维护） | 初中级 | 官方文档 | 可直接引用 | 概念讲解、命令演示 | 明确 `>`, `>>`, `2>`, `2>&1`、重定向顺序、文件描述符处理规则，可直接支撑“为什么 `ls >a 2>&1` 与 `ls 2>&1 >a` 不同”的讲解。 | 适合配中文示例讲解 |
| Bash Reference Manual: Pipelines | Linux 进阶 | 管道 | GNU Bash Manual | GNU Project | https://www.gnu.org/software/bash/manual/html_node/Pipelines.html | 英文 | Bash Reference Manual（持续维护） | 初中级 | 官方文档 | 可直接引用 | 概念讲解、课堂实验 | 清楚解释 `|` 与 `|&`、`pipefail`、pipeline 返回值，适合搭配 `grep`/`wc` 演示。 | 需补充中文课堂案例 |
| Bash Reference Manual: Environment | Linux 进阶 | 环境变量 | GNU Bash Manual | GNU Project | https://www.gnu.org/software/bash/manual/html_node/Environment.html | 英文 | Bash Reference Manual（持续维护） | 初中级 | 官方文档 | 可直接引用 | 概念讲解 | 解释 shell 如何导出环境变量、子进程如何继承环境，适合讲 `export PATH=...` 与临时变量。 | 可与 `environ(7)` 联读 |
| environ(7) | Linux 进阶 | 环境变量 | man7 | Linux man-pages project | https://www.man7.org/linux/man-pages/man7/environ.7.html | 英文 | man7 持续维护 | 中级 | 手册页 | 需改写整理 | 讲师备课 | 从进程角度解释环境变量与 `execve`/`fork` 继承，适合帮助讲师避免把 shell 变量与进程环境混讲。 | 偏底层，不建议直接给新手通读 |
| Debian Handbook: aptitude, apt-get, and apt Commands | Linux 进阶 | 包管理 | Debian Handbook | Debian 社区 | https://www.debian.org/doc/manuals/debian-handbook/sect.apt-get.el.html | 英文 | Handbook 在线版（持续维护） | 初中级 | 官方/准官方教程 | 可直接引用 | 概念讲解、演示命令 | 明确 `apt` 适合交互式使用，`apt-get` 接口更稳定、适合脚本，适合解释“为什么教程里会看到两套命令”。 | 适合 Debian/Ubuntu 通用场景 |
| chmod invocation (GNU Coreutils 9.10) | 文件权限 | chmod | GNU Coreutils Manual | GNU Project | https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html | 英文 | Coreutils 9.10 | 中级 | 官方文档 | 可直接引用 | 概念讲解、误区说明 | 明确 `chmod` 对符号链接、递归、`--dereference` 的行为，以及递归处理符号链接的安全风险。 | 是讲“别乱 `chmod -R`”的重要依据 |
| chown invocation (GNU Coreutils 9.10) | 文件权限 | chown | GNU Coreutils Manual | GNU Project | https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html | 英文 | Coreutils 9.10 | 中级 | 官方文档 | 可直接引用 | 概念讲解、风险提示 | 明确 owner/group 写法、`:` 语法、setuid/setgid 位可能受影响，适合讲 `chown user:group file`。 | 讲授时应补中文示例 |
| chgrp invocation (GNU Coreutils 9.10) | 文件权限 | chgrp | GNU Coreutils Manual | GNU Project | https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html | 英文 | Coreutils 9.10 | 初中级 | 官方文档 | 需改写整理 | 课堂补充 | 适合说明“只改组”与 `chown :group` 的关系，也包含递归与符号链接风险。 | 不必单独成主教材 |
| An Introduction to Linux Permissions | 文件权限 | rwx 入门 | DigitalOcean Community | Justin Ellingwood / DigitalOcean 社区 | https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-permissions | 英文 | 在线教程（抓取于 2026-03-26） | 初级 | 教程文章 | 需改写整理 | 学生预习、课后阅读 | 面向入门者，对 rwx、owner/group/others、目录权限的解释更直观，适合转化为中文图文教程。 | 站点导航噪声较多，需二次清洗 |
| ps(1) | 进程管理 | ps | man7 | procps / man-pages | https://www.man7.org/linux/man-pages/man1/ps.1.html | 英文 | man7 持续维护 | 初中级 | 手册页 | 可直接引用 | 命令演示 | 精确定义 `ps -e`, `ps -ef`, `ps axu` 等常见用法及默认选择行为，适合作为课堂示例依据。 | 适合搭配真实终端输出 |
| top(1) | 进程管理 | top | man7 | procps / man-pages | https://www.man7.org/linux/man-pages/man1/top.1.html | 英文 | man7 持续维护 | 初中级 | 手册页 | 需改写整理 | 演示、练习 | 说明 top 的实时视图与交互按键，适合讲 CPU/内存观察。 | 对新手需截取最常用按键 |
| kill(1) | 进程管理 | 信号与 kill | man7 | procps / util-linux 生态 | https://www.man7.org/linux/man-pages/man1/kill.1.html | 英文 | man7 持续维护 | 初中级 | 手册页 | 可直接引用 | 风险讲解、演示 | 明确默认发送 `TERM`，应优先用 TERM 而不是 `KILL(9)`；这是教学中纠正常见误区的核心依据。 | 可直接写入“误区”板块 |
| Job Control Basics | 进程管理 | jobs/bg/fg | GNU Bash Manual | GNU Project | https://www.gnu.org/software/bash/manual/html_node/Job-Control-Basics.html | 英文 | Bash Manual（持续维护） | 中级 | 官方文档 | 可直接引用 | 讲解前后台任务 | 从 shell job 抽象解释 `Ctrl+Z`、`bg`、`fg`、前后台进程组，很适合解释“为什么终端关了任务会没”。 | 建议配 `nohup`/`tmux` 延伸自编内容 |
| How To Use ps, kill, and nice to Manage Processes in Linux | 进程管理 | 综合流程 | DigitalOcean Community | DigitalOcean 社区 | https://www.digitalocean.com/community/tutorials/how-to-use-ps-kill-and-nice-to-manage-processes-in-linux | 英文 | 在线教程（抓取于 2026-03-26） | 初级 | 教程文章 | 需改写整理 | 学生预习、课后练习 | 把 `ps`、`kill`、`nice` 串成一条操作链，适合做新手友好的流程化练习。 | 可作为“从观察到处理”的实战材料 |
| ssh(1) | SSH/服务器操作 | ssh 登录 | man7 | OpenSSH / man-pages | https://www.man7.org/linux/man-pages/man1/ssh.1.html | 英文 | man7 持续维护 | 初中级 | 手册页 | 可直接引用 | 命令讲解、安全讲解 | 明确 `ssh [user@]host`、`-i`、`-J`、端口转发、agent forwarding 风险，适合作为主讲义依据。 | 可直接引用 agent forwarding 风险说明 |
| scp(1) | SSH/服务器操作 | scp | man7 | OpenSSH / man-pages | https://www.man7.org/linux/man-pages/man1/scp.1.html | 英文 | man7 持续维护 | 初级 | 手册页 | 可直接引用 | 演示、练习 | 说明 scp 基于 SFTP over SSH，适合本地与远程文件传输入门。 | 可与 rsync 对比讲授 |
| rsync(1) | SSH/服务器操作 | rsync | man7 | Samba / rsync 项目 | https://www.man7.org/linux/man-pages/man1/rsync.1.html | 英文 | rsync 手册页在线版 | 中级 | 手册页 | 可直接引用 | 实战、练习 | 解释增量同步、保留权限、通过 ssh 远程同步，是“比 scp 更适合目录同步”的权威依据。 | 适合周末系统课实战 |
| Connecting to GitHub with SSH | SSH/服务器操作 | GitHub SSH 认证 | GitHub Docs | GitHub | https://docs.github.com/en/authentication/connecting-to-github-with-ssh | 英文 | GitHub Docs（持续维护） | 初级 | 官方文档 | 可直接引用 | 课堂操作、故障排查 | 提供 GitHub SSH 使用入口与一组相关文章，可直接支撑“检查现有 key / 生成新 key / 添加 key / 测试连接”的教学链路。 | GitHub 官方、可信度高 |
| How To Use Rsync to Sync Local and Remote Directories | SSH/服务器操作 | rsync 实战 | DigitalOcean Community | DigitalOcean 社区 | https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories | 英文 | 在线教程（抓取于 2026-03-26） | 初中级 | 教程文章 | 需改写整理 | 课后练习、案例实战 | 有助于把 rsync 从“命令存在”转成“备份/同步场景”理解。 | 需抽取命令模板 |
| About Git | Git 基础与实战 | Git 基础概念 | GitHub Docs | GitHub | https://docs.github.com/en/get-started/using-git/about-git | 英文 | GitHub Docs（持续维护） | 初级 | 官方文档 | 可直接引用 | 概念讲解 | 适合解释 Git 与 GitHub 的关系、版本控制基本概念。 | 可用于教程开篇 |
| Git basics | Git 基础与实战 | Git 起步 | GitHub Docs | GitHub | https://docs.github.com/en/get-started/git-basics | 英文 | GitHub Docs（持续维护） | 初级 | 官方文档 | 可直接引用 | 起步引导 | 汇总设置 Git、远程仓库、rebase 冲突等基础入口，适合作为 Git 模块索引。 | 适合做资料导航 |
| Pro Git 中文版（第二版） | Git 基础与实战 | Git 全景 | git-scm.com | Scott Chacon、Ben Straub | https://git-scm.com/book/zh/v2 | 中文 | 第二版（站点注明 2014 基础版本，页面持续修订） | 初中级 | 官方书籍 | 可直接引用 | 主教材、章节参考 | 覆盖 Git 基础、分支、远程仓库、服务器、GitHub、工具等，结构完整，最适合做 Git 主线讲义。 | 需注意个别平台截图偏旧，但核心命令稳定 |
| git-commit manual | Git 基础与实战 | commit 语义 | git-scm.com | Git 项目 | https://git-scm.com/docs/git-commit | 中文/英文可切换 | 手册页显示 last updated in 2.53.0 / 2026-02-02 | 中级 | 官方手册 | 可直接引用 | 教师备课、命令核对 | 用于核对 `git commit` 参数与行为，保证教程里的命令解释不过时。 | 适合作为事实核验，不适合新手直接通读 |
| Git是什么 | Git 基础与实战 | 版本控制入门 | 廖雪峰 | 廖雪峰 | https://www.liaoxuefeng.com/wiki/896043488029600/896067008724000 | 中文 | 在线教程（抓取于 2026-03-26） | 初级 | 中文教程 | 可直接引用 | 入门解释 | 用通俗示例解释版本控制、集中式 vs 分布式，适合零基础学习者建立心智模型。 | 中文友好度高 |
| 从远程库克隆 | Git 基础与实战 | clone / 远程仓库 | 廖雪峰 | 廖雪峰 | https://www.liaoxuefeng.com/wiki/896043488029600/898732792973664 | 中文 | 在线教程（抓取于 2026-03-26） | 初级 | 中文教程 | 可直接引用 | 课堂演示、课后练习 | 用 GitHub 仓库实例讲 `git clone`、SSH vs HTTPS 的差别，适合第一次远程协作课。 | 可直接转成课堂步骤 |
| Git init: Set Up Your Git Repo | Git 基础与实战 | init | Atlassian | Atlassian | https://www.atlassian.com/git/tutorials/setting-up-a-repository | 英文 | 在线教程（抓取于 2026-03-26） | 初级 | 教程文章 | 需改写整理 | 课堂补充 | 适合补充 `git init` 建仓流程。 | 抓取噪声大，需自行提炼 |
| Git Commit | Git 基础与实战 | commit | Atlassian | Atlassian | https://www.atlassian.com/git/tutorials/saving-changes/git-commit | 英文 | 在线教程（抓取于 2026-03-26） | 初级 | 教程文章 | 需改写整理 | 课堂补充 | 有助于补充 commit 工作流与 staged changes 讲解。 | 作为辅助，不作主教材 |
| How to Resolve Merge Conflicts in Git? | Git 基础与实战 | merge conflict | Atlassian | Atlassian | https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts | 英文 | 在线教程（抓取于 2026-03-26） | 初中级 | 教程文章 | 需改写整理 | 冲突实战 | 可作为“冲突是什么、怎么处理”的案例化补充。 | 建议转成中文实验步骤 |
| Resolving merge conflicts after a Git rebase | Git 基础与实战 | rebase 冲突 | GitHub Docs | GitHub | https://docs.github.com/en/get-started/using-git/resolving-merge-conflicts-after-a-git-rebase | 英文 | GitHub Docs（持续维护） | 中级 | 官方文档 | 需改写整理 | 进阶补充 | 适合给学有余力的学生补充 rebase 冲突处理。 | 不建议第 2 周作为核心内容 |
| Learn Git Branching | Git 基础与实战 | 分支可视化练习 | GitHub 仓库 | pcottle | https://github.com/pcottle/learnGitBranching | 英文 | 仓库首页抓取于 2026-03-26 | 初中级 | 互动仓库/练习 | 仅供参考 | 课后练习 | 交互式可视化分支学习资源，适合学生练习 `branch` / `merge` / `rebase` 心智模型。 | 不适合替代系统讲解 |
| Oh My Git! | Git 基础与实战 | 游戏化练习 | ohmygit.org | bleeptrack / blinry | https://ohmygit.org/ | 英文 | 官网抓取于 2026-03-26 | 初中级 | 游戏化资源 | 仅供参考 | 兴趣扩展 | 通过可视化游戏展示 Git 内部结构，适合增强兴趣。 | 不是主线教学材料 |

## 分主题教学建议

### Linux 进阶

**推荐讲授顺序**
1. 环境变量与 shell 执行环境
2. 重定向
3. 管道
4. 包管理
5. 组合实战

**关键知识点**
- shell 变量与环境变量的区别
- `export VAR=value` 与 `VAR=value command` 的作用域差异
- `>`, `>>`, `2>`, `2>&1`, `/dev/null`
- `|` 与 `|&` 的差异
- `apt update`、`apt install` 的交互式使用；`apt-get` 更适合脚本

**建议演示命令 / 案例**
```bash
export DEMO=hello
echo "$DEMO"
DEMO=world env | grep '^DEMO='
ls > out.txt 2>&1
ls no-such-file > out.txt 2>&1
printf 'a\nb\n' | wc -l
sudo apt update
sudo apt install tree
```

**推荐主资料**
- GNU Bash Manual: Redirections
- GNU Bash Manual: Pipelines
- GNU Bash Manual: Environment
- Debian Handbook: aptitude, apt-get, and apt Commands

**教学提醒**
- `apt` 与 `apt-get` 都常见，不要把其中一个说成“错误命令”。
- 讲重定向必须演示“顺序会改变结果”。

### 文件权限

**推荐讲授顺序**
1. 用户 / 组 / others
2. 文件与目录的 rwx 含义差异
3. `chmod` 数字法与符号法
4. `chown` / `chgrp`
5. 递归修改权限的风险

**关键知识点**
- 文件的 `rwx` 与目录的 `rwx` 含义不同
- `chmod 755`、`chmod u+x`
- `chown user:group file`
- 符号链接与递归权限修改的风险
- 不要把 `777` 当万能修复方案

**建议演示命令 / 案例**
```bash
ls -l
chmod 644 notes.txt
chmod u+x script.sh
chmod -R u+rwX project/
chown alice:dev app.log
chgrp dev shared/
```

**推荐主资料**
- GNU Coreutils: chmod invocation
- GNU Coreutils: chown invocation
- DigitalOcean: An Introduction to Linux Permissions

**教学提醒**
- 课堂上必须解释为什么目录权限不能简单按文件权限理解。
- 需要明确示警：不要对项目目录默认执行 `chmod -R 777`。

### 进程管理

**推荐讲授顺序**
1. `ps` 看什么
2. `top` 如何实时观察
3. 信号与 `kill`
4. `jobs` / `bg` / `fg`
5. 案例：找到并优雅终止异常进程

**关键知识点**
- `ps -ef` / `ps axu`
- `top` 适合实时观察，`ps` 适合快照
- 默认 `kill` 发送 `TERM`
- `Ctrl+Z`、`bg`、`fg` 与前后台任务
- 优先优雅终止，最后才考虑 `kill -9`

**建议演示命令 / 案例**
```bash
ps -ef | grep python
top
sleep 300
jobs
bg %1
fg %1
kill 12345
kill -9 12345
```

**推荐主资料**
- man7: ps(1)
- man7: top(1)
- man7: kill(1)
- Bash Manual: Job Control Basics
- DigitalOcean: How To Use ps, kill, and nice to Manage Processes in Linux

**教学提醒**
- 要把 `kill -9` 放在“最后手段”位置讲，而不是第一反应。
- 可自编 `nohup` / `tmux` 补充内容，本次资料中暂无单条主资料覆盖得足够教学友好。

### SSH / 服务器常用操作

**推荐讲授顺序**
1. `ssh` 远程登录
2. `scp` 单文件传输
3. `rsync` 目录同步
4. SSH key 与 GitHub 连接
5. 常见报错：host key / 权限 / key 未生效

**关键知识点**
- `ssh user@host`
- `-i` 指定私钥、`-p` 指定端口、`-J` 跳板机
- `scp` 与 `rsync` 的适用差异
- host key 验证的重要性
- agent forwarding 需要谨慎

**建议演示命令 / 案例**
```bash
ssh user@example.com
ssh -i ~/.ssh/id_ed25519 -p 2222 user@example.com
scp local.txt user@example.com:/tmp/
rsync -avz ./site/ user@example.com:/var/www/site/
ssh -T git@github.com
```

**推荐主资料**
- man7: ssh(1)
- man7: scp(1)
- man7: rsync(1)
- GitHub Docs: Connecting to GitHub with SSH
- DigitalOcean: How To Use Rsync to Sync Local and Remote Directories

**教学提醒**
- 不要把关闭 host key 校验当作默认解决方案。
- `scp` 够简单，`rsync` 更适合目录同步和部署演示。

### Git 基础与实战

**推荐讲授顺序**
1. Git 是什么、为什么需要版本控制
2. `init` / `clone`
3. `add` / `commit`
4. `branch` / `merge`
5. 冲突处理
6. 与远程仓库协作

**关键知识点**
- 工作区 / 暂存区 / 提交历史
- `git clone` 与远程地址
- commit 是“保存历史节点”，不是简单“同步到 GitHub”
- 分支用于隔离修改
- merge conflict 是多人协作正常现象

**建议演示命令 / 案例**
```bash
git init
git clone git@github.com:USER/REPO.git
git status
git add README.md
git commit -m "init"
git switch -c feature/demo
git merge feature/demo
```

**推荐主资料**
- Pro Git 中文版
- GitHub Docs: About Git
- GitHub Docs: Git basics
- 廖雪峰：Git是什么
- 廖雪峰：从远程库克隆
- Atlassian merge conflict 教程（辅助）

**教学提醒**
- 第 2 周以 merge 冲突为上界即可，`rebase` 冲突可放扩展阅读。
- 互动练习资源可选 Learn Git Branching，不宜直接代替系统教程。

## 第 2 周课程映射建议

| 建议天数 | 主题 | 重点内容 | 推荐主资料 | 建议练习 |
|---|---|---|---|---|
| Day 8 | Linux 进阶 1 | 环境变量、重定向 | Bash Environment / Redirections | 配置临时环境变量并把输出重定向到文件 |
| Day 9 | Linux 进阶 2 | 管道、包管理 | Bash Pipelines / Debian Handbook | 用管道统计日志行数；用 apt 安装一个工具 |
| Day 10 | 文件权限 | rwx、chmod、chown | GNU Coreutils / DigitalOcean Permissions | 修改脚本执行权限，给共享目录设组权限 |
| Day 11 | 进程管理 | ps、top、kill、jobs | man7 + Bash Job Control | 启动一个后台任务并用 jobs / kill 管理 |
| Day 12 | SSH / 服务器操作 | ssh、scp、rsync、SSH key | man7 + GitHub Docs SSH | 登录远程主机并传一个文件，再做一次 rsync |
| Day 13 | Git 基础 | Git 概念、init、clone、commit | Pro Git / GitHub Docs / 廖雪峰 | 初始化仓库并提交一次变更 |
| Day 14 | Git 实战系统课 | branch、merge、冲突、远程协作综合演练 | Pro Git / Atlassian / GitHub Docs | 两人或双目录模拟分支协作与冲突解决 |

## 入选 / 备选 / 淘汰规则

### 入选为主资料
- 官方或持续维护文档
- 结构清晰，能支撑概念 + 命令 + 注意事项
- 可以直接转写为 Markdown 教程段落

### 备选资料
- 教程型站点内容好，但页面噪声大，需要手工提炼
- 互动资源有教学价值，但不适合作为唯一讲义

### 淘汰资料类型
- 无作者、无更新时间、仅转载
- 只给命令不解释风险与上下文
- 推荐危险默认实践，如关闭 SSH 校验或默认 `777`

## 待补空白点

1. `systemctl` / `service` 作为现代 Linux 服务管理内容，本轮未抓到足够干净、适合新手直接引用的官方页；建议后续补充一条 systemd 官方文档或发行版官方文档，并自编最小示例。
2. `nohup` / `screen` / `tmux` 作为长期任务保活内容，本轮现成资料里没有同时兼顾权威性与教学友好度的主资料，建议在写第 2 周教程时自编一个“SSH 断开后任务为何中断”的补充实验。
3. `umask`、setuid、setgid、sticky bit 可在文件权限模块作为扩展阅读加入，但不建议第 2 周主线讲太深。

## 直接可用于 Markdown 教程的章节骨架

```markdown
## 第 2 周：Linux 实战深化与 Git 入门

### Day 8：环境变量、重定向与日志输出
### Day 9：管道与包管理
### Day 10：文件权限与所有权
### Day 11：进程观察、前后台任务与安全终止
### Day 12：SSH 登录、文件传输与远程同步
### Day 13：Git 入门：仓库、提交与远程克隆
### Day 14：系统课：Git 分支、冲突与协作演练
```

## 来源说明

本文件中的结论均来自 2026-03-26 对下列原始页面的抓取与整理：
- GNU Bash Manual
- GNU Coreutils Manual
- man7 Linux manual pages
- Debian Handbook
- Git 官方书籍与命令手册（git-scm.com）
- GitHub Docs
- DigitalOcean Community Tutorials
- Atlassian Git Tutorials
- 廖雪峰 Git 教程
- Learn Git Branching 仓库首页
- Oh My Git! 官网
