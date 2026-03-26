# 2026-03-26 Git 与 GitHub 零基础中文资料调研

- 日期: 2026-03-26
- 任务: 调研 Git 与 GitHub 零基础学习资料，覆盖仓库创建、clone、commit、branch、merge、pull request、README、issue、协作流程与常见坑，优先收集通俗易懂的中文资料并记录来源
- 适用项目: `projects/zero-basics-plan`
- 访问时间: 2026-03-26 20:25:55（北京时间，来源：`get_current_time`）

## 检索说明

### 实际检索路径

本轮先按任务要求尝试了 `web_search`，但 3 组关键词均返回 `HTTP 403: Forbidden`，因此改用 `run_shell + curl DuckDuckGo HTML` 抓取搜索结果页，并用 `web_fetch` 抓取目标页面正文。

### 已尝试的 3 组关键词

1. `Git GitHub 零基础 中文 教程 仓库创建 clone commit branch merge pull request README issue`
2. `GitHub 新手 中文 教程 pull request issue README SSH 配置 常见报错`
3. `Git 零基础 中文 commit push pull branch merge SSH 教程 博客`

### 筛选标准

- **中文优先**：优先中文官方文档、中文教程站、中文社区高质量文章
- **零基础友好**：有步骤、解释术语、最好带图或带操作顺序
- **覆盖完整**：需要能映射到仓库创建、clone、commit、branch、merge、pull request、README、issue、SSH、常见报错
- **课程可落地**：可以明确放入某一天课程，而不是只能做背景知识
- **交叉校验**：关键流程与报错优先用 GitHub Docs 校验，社区文章负责“人话解释”和踩坑案例

---

## 结论先看

适合零基础教程的资料组合可以分成两层：

1. **主教学资料**：菜鸟教程、博客园完整教程、腾讯云 GitHub 指南、CSDN 新手教程、阿里云分支合并教程。
2. **校验与排错资料**：GitHub 官方中文文档（仓库、README、Issue、PR、SSH、clone 报错、non-fast-forward、rebase 冲突）。

对于零基础学习者，最顺的学习顺序不是“先学所有命令”，而是：

- 先理解 **Git 是版本控制工具，GitHub 是托管与协作平台**
- 再做 **创建仓库 → clone/初始化 → add/commit → push/pull**
- 然后进入 **branch/merge**
- 最后进入 **Issue / PR / README / 协作流程 / 常见冲突**

必须单独强调的高频坑：

- SSH `Permission denied (publickey)`
- `git push` 非快进拒绝（non-fast-forward）
- clone 地址拼错或仓库权限不足
- 在默认分支上直接乱改，导致后续 PR 与协作成本变高
- 把 README 当成“可有可无”，导致协作对象不知道项目做什么、怎么运行

---

## 资料清单

| ID | 级别 | 标题 | 来源类型 | 平台 | 链接 |
|---|---|---|---|---|---|
| GG-01 | 优先采用 | 仓库快速入门 | 官方中文文档 | GitHub Docs | https://docs.github.com/zh/repositories/creating-and-managing-repositories/quickstart-for-repositories |
| GG-02 | 优先采用 | 关于拉取请求 | 官方中文文档 | GitHub Docs | https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests |
| GG-03 | 优先采用 | 关于问题 | 官方中文文档 | GitHub Docs | https://docs.github.com/zh/issues/tracking-your-work-with-issues/about-issues |
| GG-04 | 优先采用 | 关于仓库 README 文件 | 官方中文文档 | GitHub Docs | https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes |
| GG-05 | 优先采用 | 使用 SSH 连接到GitHub | 官方中文文档 | GitHub Docs | https://docs.github.com/zh/authentication/connecting-to-github-with-ssh |
| GG-06 | 优先采用 | 错误：权限被拒绝（公钥） | 官方中文文档 | GitHub Docs | https://docs.github.com/zh/authentication/troubleshooting-ssh/error-permission-denied-publickey |
| GG-07 | 优先采用 | 排查克隆错误 | 官方中文文档 | GitHub Docs | https://docs.github.com/zh/repositories/creating-and-managing-repositories/troubleshooting-cloning-errors |
| GG-08 | 优先采用 | 处理非快进错误 | 官方中文文档 | GitHub Docs | https://docs.github.com/zh/get-started/using-git/dealing-with-non-fast-forward-errors |
| GG-09 | 可补充 | Git 基本操作 | 教程站 | 菜鸟教程 | https://www.runoob.com/git/git-basic-operations.html |
| GG-10 | 可补充 | Git 分支管理 | 教程站 | 菜鸟教程 | https://www.runoob.com/git/git-branch.html |
| GG-11 | 可补充 | Git 教程 | 教程站 | 菜鸟教程 | https://www.runoob.com/git/git-tutorial.html |
| GG-12 | 优先采用 | GitHub完全指南：从零入门到高效代码管理 | 社区教程 | 腾讯云开发者社区 | https://cloud.tencent.com/developer/article/2586845 |
| GG-13 | 优先采用 | 完整教程：从零开始，学会上传，更新，维护github仓库 | 博客 | 博客园 | https://www.cnblogs.com/ljbguanli/p/18916988 |
| GG-14 | 可补充 | 怎样在GitHub上建立仓库、以及怎样实现分支代码的合并。保姆级别的教程 | 社区教程 | 阿里云开发者社区 | https://developer.aliyun.com/article/1584777 |
| GG-15 | 可补充 | Github入门教程，适合新手学习（非常详细） | 社区教程 | CSDN | https://blog.csdn.net/black_sneak/article/details/139600633 |
| GG-16 | 可补充 | Git 初学者指南：从配置到创建仓库 | 社区教程 | 掘金 | https://juejin.cn/post/7506832918317531199 |

> 注：DuckDuckGo 搜索中还出现了知乎与其他候选条目，但知乎正文抓取受限（403）或页面抽取不完整，因此本轮不将其作为核心证据来源。

---

## 每条资料的用途、亮点与适用课程

### GG-01 仓库快速入门

- 来源证明: `web_fetch(https://docs.github.com/zh/repositories/creating-and-managing-repositories/quickstart-for-repositories)`
- 覆盖主题:
  - 创建仓库
  - 初始化 README
  - 第一次修改 README 并提交
  - 用 GitHub CLI 或网页建立第一个仓库
- 适合零基础原因:
  - 直接按照“5 分钟创建第一个仓库并提交第一次更改”组织
  - 用仓库与 README 作为最小闭环，适合第一次接触 GitHub 的人
- 适合插入课程:
  - **第 1 天**：创建第一个仓库、认识 README、完成第一个 commit
- 风险与备注:
  - 更偏 GitHub Web 与仓库概念，需要搭配本地 Git 命令资料补齐 `clone / add / commit / push`

### GG-02 关于拉取请求

- 来源证明: `web_fetch(https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)`
- 覆盖主题:
  - pull request 是什么
  - Conversation / Commits / Checks / Files changed 四个视角
  - draft pull request
- 适合零基础原因:
  - 直接解释 PR 是“先讨论和审查，再合并”的协作核心机制
  - 能帮助新手把“PR 不等于直接提交代码”这件事讲明白
- 适合插入课程:
  - **第 4 天**：协作流程、PR、评审与合并
- 风险与备注:
  - 偏概念与页面介绍，需搭配社区文章做“真实操作路径”讲解

### GG-03 关于问题

- 来源证明: `web_fetch(https://docs.github.com/zh/issues/tracking-your-work-with-issues/about-issues)`
- 覆盖主题:
  - issue 的用途
  - 标签、里程碑、子任务、分配、通知
  - issue 与 PR 的联动
- 适合零基础原因:
  - 很适合把 issue 讲成“任务单 / bug 单 / 想法卡片”
  - 解释了为什么 issue 不只是提 bug，也能做计划与跟踪
- 适合插入课程:
  - **第 4 天**：Issue 管理、任务协作、PR 关联 issue
- 风险与备注:
  - 如果学习者完全没做过项目管理，需要用更生活化语言改写

### GG-04 关于仓库 README 文件

- 来源证明: `web_fetch(https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)`
- 覆盖主题:
  - README 的作用
  - 推荐包含的核心信息
  - `.github/`、根目录、`docs/` 中 README 的展示优先级
- 适合零基础原因:
  - 明确告诉新手 README 是项目首页说明书，而不是“装饰文件”
- 适合插入课程:
  - **第 1 天**：仓库创建时一起写 README
  - **第 5 天**：项目说明写作练习
- 风险与备注:
  - 课程中建议只讲“项目是什么、怎么开始、怎么求助、谁维护”四个最低必要块

### GG-05 使用 SSH 连接到GitHub

- 来源证明: `web_fetch(https://docs.github.com/zh/authentication/connecting-to-github-with-ssh)`
- 覆盖主题:
  - SSH 连接总入口
  - 检查密钥、生成密钥、添加密钥、测试连接
- 适合零基础原因:
  - 官方路径清晰，适合用来校验社区文章中的命令是否正确
- 适合插入课程:
  - **第 2 天**：连接远程仓库，配置 SSH
- 风险与备注:
  - 仍需搭配更口语化教程讲“公钥/私钥/ssh-agent”是什么

### GG-06 错误：权限被拒绝（公钥）

- 来源证明: `web_fetch(https://docs.github.com/zh/authentication/troubleshooting-ssh/error-permission-denied-publickey)`
- 覆盖主题:
  - `Permission denied (publickey)` 的常见原因
  - 必须使用 `git@github.com`
  - 不要混用 `sudo`
  - 检查当前实际使用的 key
- 适合零基础原因:
  - 直接对应新手最容易卡住的 SSH 报错
- 适合插入课程:
  - **第 2 天附录** 或 **第 5 天排错课**
- 风险与备注:
  - 课程里要把“别用你的 GitHub 用户名替代 SSH 用户 git”做成醒目提示

### GG-07 排查克隆错误

- 来源证明: `web_fetch(https://docs.github.com/zh/repositories/creating-and-managing-repositories/troubleshooting-cloning-errors)`
- 覆盖主题:
  - 401/403/404 类 HTTPS clone 错误
  - 仓库找不到
  - remote HEAD 指向问题
  - 检查 `git remote -v`
- 适合零基础原因:
  - clone 是早期高频动作，出错后很容易怀疑自己“什么都不会”
  - 官方文档能帮新手把错误归因到“地址 / 权限 / token / 协议”
- 适合插入课程:
  - **第 2 天**：clone 与 remote 基础
  - **第 5 天**：常见报错排查
- 风险与备注:
  - 课程中要明确 HTTPS 现在通常要用 token，不再直接用密码

### GG-08 处理非快进错误

- 来源证明: `web_fetch(https://docs.github.com/zh/get-started/using-git/dealing-with-non-fast-forward-errors)`
- 覆盖主题:
  - push 被拒绝的非快进错误
  - `git fetch` + `git merge`
  - `git pull`
- 适合零基础原因:
  - 这是多人协作或多端提交时最常见的 push 报错之一
- 适合插入课程:
  - **第 4 天**：push/pull 与协作冲突
- 风险与备注:
  - 课程里要讲清楚：不是 Git 坏了，而是远程比你本地更新，先同步再推送

### GG-09 Git 基本操作

- 来源证明: `web_fetch(https://www.runoob.com/git/git-basic-operations.html)`
- 覆盖主题:
  - `git init`、`git clone`、`git add`、`git commit`、`git pull`、`git push`
  - 工作区、暂存区、本地仓库、远程仓库
- 适合零基础原因:
  - 把最常用 6 个命令放在一起，适合做第一轮记忆地图
  - 对工作区/暂存区/本地仓库的解释比较适合初学者建立模型
- 适合插入课程:
  - **第 1-2 天**：本地 Git 与远程仓库基本命令
- 风险与备注:
  - 更像知识索引，需要讲师或教程文本做步骤串联

### GG-10 Git 分支管理

- 来源证明: `web_fetch(https://www.runoob.com/git/git-branch.html)`
- 覆盖主题:
  - `git branch`
  - `git checkout -b`
  - `git merge`
  - 冲突解决与删除分支
- 适合零基础原因:
  - 有完整示例，能帮助学习者理解“不同分支像不同开发线”
- 适合插入课程:
  - **第 3 天**：branch / merge 基础
- 风险与备注:
  - 课程里可补充 `git switch` 作为新命令，但不必第一天就讲

### GG-11 Git 教程

- 来源证明: `web_fetch(https://www.runoob.com/git/git-tutorial.html)`
- 覆盖主题:
  - Git 基本概念总入口
  - 与 SVN 的差异
  - Git 系列章节索引
- 适合零基础原因:
  - 适合做整套教程的目录导航页
- 适合插入课程:
  - **全课程参考索引**
- 风险与备注:
  - 不建议单独作为主阅读，因为信息范围较大、节奏较散

### GG-12 GitHub完全指南：从零入门到高效代码管理

- 来源证明: `web_fetch(https://cloud.tencent.com/developer/article/2586845)`
- 覆盖主题:
  - GitHub 账号、仓库、clone、commit、push、pull、branch、PR
  - 仓库页面模块、Issue、Actions 等
  - 本地 Git 配置
- 适合零基础原因:
  - 用“为什么这么做”解释功能，而不只是罗列命令
  - 把 GitHub 页面与 Git 本地操作连了起来
- 适合插入课程:
  - **第 1-4 天** 均可拆分使用
- 风险与备注:
  - 篇幅较长，课程里应拆成模块阅读，不建议一口气全读

### GG-13 完整教程：从零开始，学会上传，更新，维护github仓库

- 来源证明: `web_fetch(https://www.cnblogs.com/ljbguanli/p/18916988)`
- 覆盖主题:
  - 注册 GitHub
  - 安装 Git
  - 全局配置
  - 生成 SSH key
  - 建仓、关联远程、上传项目、维护更新
- 适合零基础原因:
  - 从“账号、安装、配置、安全验证、首次上传”全流程串起来了
  - 非常适合作为第一次完整实操主线
- 适合插入课程:
  - **第 1-2 天主资料**
- 风险与备注:
  - 个别命令在网页抽取中格式较挤，课程改写时要重新排版命令块

### GG-14 怎样在GitHub上建立仓库、以及怎样实现分支代码的合并。保姆级别的教程

- 来源证明: `web_fetch(https://developer.aliyun.com/article/1584777)`
- 覆盖主题:
  - 建仓
  - 建分支
  - 编辑并发布更改
  - 拉取请求
  - 合并分支
- 适合零基础原因:
  - 结构简短，适合作为“网页端理解 branch → PR → merge”演示材料
- 适合插入课程:
  - **第 3-4 天**：分支协作与 PR
- 风险与备注:
  - 偏 GitHub 网页端演示，命令行配套不足

### GG-15 Github入门教程，适合新手学习（非常详细）

- 来源证明: `web_fetch(https://blog.csdn.net/black_sneak/article/details/139600633)`
- 覆盖主题:
  - Git 与 GitHub 的关系
  - GitHub 注册与仓库创建
  - Git Bash 安装
  - 基础使用路径
- 适合零基础原因:
  - 对“Git 和 GitHub 不是一回事”解释得更通俗
  - 很适合给完全没接触过版本控制的人建立第一印象
- 适合插入课程:
  - **第 1 天预习**
- 风险与备注:
  - 篇幅很长，部分背景介绍多于核心操作，需拆读

### GG-16 Git 初学者指南：从配置到创建仓库

- 来源证明: `web_fetch(https://juejin.cn/post/7506832918317531199)`
- 覆盖主题:
  - Git 基本概念
  - `git config`
  - `git init`
  - `git add`
  - `git commit`
  - 连接远程仓库与首次推送
- 适合零基础原因:
  - 篇幅短，适合做“最小闭环”阅读
- 适合插入课程:
  - **第 1 天**：本地仓库初始化与第一次提交
- 风险与备注:
  - 不覆盖 GitHub 的 Issue / PR / README 等协作层能力，需要搭配其他来源

---

## 主题覆盖映射

| 主题 | 对应资料 |
|---|---|
| 仓库创建 | GG-01, GG-12, GG-13, GG-14, GG-15 |
| clone | GG-07, GG-09, GG-12 |
| add / commit | GG-01, GG-09, GG-12, GG-13, GG-16 |
| push / pull | GG-08, GG-09, GG-12, GG-13, GG-16 |
| branch | GG-10, GG-12, GG-14 |
| merge | GG-10, GG-14, GG-08 |
| pull request | GG-02, GG-12, GG-14 |
| README | GG-01, GG-04 |
| issue | GG-03, GG-12 |
| SSH 配置 | GG-05, GG-06, GG-13 |
| clone/push 常见报错 | GG-06, GG-07, GG-08 |
| 协作流程 | GG-02, GG-03, GG-12, GG-14 |

结论：本轮已覆盖任务要求中的全部核心主题，没有明显缺口。

---

## 推荐阅读顺序

### 阶段 1：先建立基本认识

1. GG-15（Git 和 GitHub 的区别、平台概念）
2. GG-11（Git 全貌索引）
3. GG-01（创建第一个仓库）

### 阶段 2：完成第一次本地到远程闭环

1. GG-16（本地配置与初始化）
2. GG-13（完整上传与维护路径）
3. GG-09（补齐命令含义）
4. GG-05（SSH 连接）

### 阶段 3：开始分支与协作

1. GG-10（branch / merge）
2. GG-14（网页端分支、PR、merge）
3. GG-02（PR 官方解释）
4. GG-03（Issue 官方解释）
5. GG-04（README 应该写什么）

### 阶段 4：常见问题排查

1. GG-06（SSH 公钥权限拒绝）
2. GG-07（clone 报错）
3. GG-08（push 非快进）

---

## 可直接映射到课程的建议安排

### 第 1 天：Git / GitHub 是什么，创建第一个仓库

- 主资料:
  - GG-15
  - GG-01
  - GG-16
- 实践:
  - 注册 GitHub
  - 创建第一个公开仓库
  - 初始化 README
  - 本地 `git init`、`git add`、`git commit`
- 当天成果:
  - 能解释 Git 与 GitHub 的区别
  - 能完成第一次本地提交

### 第 2 天：clone、push、pull、SSH 连接

- 主资料:
  - GG-13
  - GG-05
  - GG-09
- 排错资料:
  - GG-06
  - GG-07
- 实践:
  - clone 一个仓库
  - 配置 SSH key
  - push 本地更改
  - pull 远程更新
- 当天成果:
  - 能把本地代码同步到 GitHub
  - 遇到 SSH/clone 报错知道先看哪里

### 第 3 天：branch 与 merge

- 主资料:
  - GG-10
  - GG-14
- 实践:
  - 建新分支
  - 在分支上改 README
  - merge 回 main
- 当天成果:
  - 理解为什么多人协作不应都在主分支上直接改

### 第 4 天：Issue、PR 与基础协作流程

- 主资料:
  - GG-02
  - GG-03
  - GG-12
- 实践:
  - 新建一个 issue
  - 从 issue 派生任务描述
  - 创建 pull request
  - 模拟代码评审与合并
- 当天成果:
  - 理解“issue 管任务，PR 管代码变更”的协作分工

### 第 5 天：README 与常见坑复盘

- 主资料:
  - GG-04
  - GG-06
  - GG-07
  - GG-08
- 实践:
  - 重写仓库 README
  - 模拟一个 non-fast-forward 场景并修复
  - 总结常见坑
- 当天成果:
  - 能写出一个最低可用 README
  - 认识 clone/push/SSH 三类高频报错

---

## 面向零基础的解释模板

### Git
- 这是什么：版本控制工具。
- 解决什么问题：帮你记录代码历史、回滚错误、多人协作。
- 类比：像“带时间轴的存档系统”。

### GitHub
- 这是什么：托管 Git 仓库的平台。
- 解决什么问题：帮你把代码放到网上，并与别人协作。
- 类比：像“代码云盘 + 协作平台”。

### commit
- 这是什么：一次保存的版本快照。
- 类比：像游戏存档点。
- 易错点：不要所有改动都塞进一个“update”提交里。

### branch
- 这是什么：独立开发线。
- 类比：主线剧情外开一条支线，不影响主线稳定。
- 易错点：新功能直接在主分支上改，后续难审查也难回退。

### pull request
- 这是什么：请求把一条分支的改动合并到另一条分支。
- 类比：把作业交上去，请老师/同学先审一遍再收录。
- 易错点：把 PR 当成“上传代码按钮”，忽略评审与讨论意义。

### issue
- 这是什么：任务、问题、bug、想法的记录单。
- 类比：项目待办卡片。
- 易错点：只在聊天里说问题，不在 issue 留痕，后面没人能追踪。

---

## 常见坑与教学提醒

### 1. SSH 报错：`Permission denied (publickey)`

- 依据: GG-05, GG-06
- 常见原因:
  - 没把公钥加到 GitHub
  - 远程地址写错
  - 用了 `用户名@github.com` 而不是 `git@github.com`
  - 混用了 `sudo`
- 教学提醒:
  - 在课程中固定给出 `ssh -T git@github.com` 作为测试命令

### 2. clone 失败

- 依据: GG-07
- 常见原因:
  - 仓库名拼错
  - 没有权限
  - HTTPS 凭证过期或没用 token
- 教学提醒:
  - 先检查仓库 URL，再检查权限，再检查协议与认证方式

### 3. push 被拒绝（non-fast-forward）

- 依据: GG-08
- 常见原因:
  - 远程分支已经有你本地没有的提交
- 教学提醒:
  - 先 `pull`/`fetch + merge`，再推送
  - 不要把这个错误理解成“GitHub 出故障了”

### 4. merge / rebase 冲突

- 依据: GG-10, `web_fetch(https://docs.github.com/zh/get-started/using-git/resolving-merge-conflicts-after-a-git-rebase)`
- 教学提醒:
  - 零基础课只需先教会“冲突是两边改了同一处，Git 不知道听谁的”
  - 先学 merge 冲突，rebase 放进补充材料

### 5. README 写得像空壳

- 依据: GG-01, GG-04
- 教学提醒:
  - 最少包含：项目做什么、怎么开始、如何求助、谁维护

---

## 最终推荐组合

### 作为主资料的最小组合

- GG-01 仓库快速入门
- GG-09 Git 基本操作
- GG-10 Git 分支管理
- GG-12 GitHub完全指南：从零入门到高效代码管理
- GG-13 完整教程：从零开始，学会上传，更新，维护github仓库

### 作为协作模块核心资料

- GG-02 关于拉取请求
- GG-03 关于问题
- GG-04 关于仓库 README 文件
- GG-14 怎样在GitHub上建立仓库、以及怎样实现分支代码的合并

### 作为排错模块核心资料

- GG-05 使用 SSH 连接到GitHub
- GG-06 错误：权限被拒绝（公钥）
- GG-07 排查克隆错误
- GG-08 处理非快进错误

---

## Provenance Notes

本文件中的结论来自两类证据：

1. **搜索记录证据**：3 组关键词先尝试 `web_search`，因 403 失败后改用 `run_shell + curl DuckDuckGo HTML` 抓取搜索结果
2. **正文抓取证据**：每条核心资料均通过对应 `web_fetch(URL)` 抓取正文并据此归纳

没有使用无来源断言；关于仓库、README、Issue、PR、SSH、clone 报错、non-fast-forward 的关键表述，均绑定了 GitHub Docs 或对应中文教程来源。
