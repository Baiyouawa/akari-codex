# Git + GitHub + 基础协作工作流调研笔记（零基础课程向）

- 日期：2026-03-26
- 项目：`projects/zero-basics-plan`
- 任务：调研主题：Git + GitHub + 基础协作工作流
- 说明：本笔记先执行 `web_search`，但 3 组中文关键词均返回 `HTTP Error 403: Forbidden`；随后改用 `web_fetch` 抓取中文官方文档与高质量中文教程正文，形成可追溯资料清单。

## 调研范围

本轮必须覆盖：

- `git add`
- `git commit`
- `git push`
- `git pull`
- `branch`
- `merge`
- SSH 配置
- GitHub 仓库创建
- 常见报错与解决

## 搜索关键词记录

### 第 1 组：Git 基础命令与工作流
- 查询：`Git GitHub 零基础 教程 中文 add commit push pull branch merge`
- 目标：寻找面向新手的 Git 基础命令说明、提交与同步工作流资料
- 结果：`web_search` 返回 `HTTP Error 403: Forbidden`

### 第 2 组：GitHub 仓库创建与 SSH 配置
- 查询：`GitHub SSH 配置 仓库创建 中文 教程 新手`
- 目标：寻找 GitHub 账号、仓库创建、SSH 连接与密钥配置资料
- 结果：`web_search` 返回 `HTTP Error 403: Forbidden`

### 第 3 组：常见报错与协作冲突
- 查询：`Git push pull merge 常见报错 解决 中文 GitHub`
- 目标：寻找 `Permission denied (publickey)`、`non-fast-forward`、合并冲突等常见问题解释
- 结果：`web_search` 返回 `HTTP Error 403: Forbidden`

## 筛选与去重原则

1. **优先中文正文可抓取来源**：优先保留 `web_fetch` 可直接读取正文的中文页面。
2. **优先官方中文文档与体系化教程**：GitHub Docs、Pro Git 中文版、廖雪峰、菜鸟教程优先于零散转载页。
3. **优先零基础友好**：保留讲清“命令在工作流中为什么要这样用”的资料，而不是只给命令表。
4. **优先覆盖缺口**：对 SSH、仓库创建、push/pull 报错、merge 冲突等专项单独补源。
5. **避免重复收录**：同类主题只保留最清晰、最权威或最适合课程改写的一篇作为主参考。

## 资料清单（13 条）

| 编号 | 标题 | URL | 来源类型 | 覆盖主题 | 摘要 | 适合插入第几天课程 |
|---|---|---|---|---|---|---|
| 1 | Pro Git（简体中文版） | https://git-scm.com/book/zh/v2 | 官方书籍 | add/commit/push/pull/branch/merge/SSH/GitHub | Git 官方维护的系统化中文教材，目录直接覆盖 Git 基础、远程仓库、分支、SSH、公钥、GitHub 协作，适合做“概念校准”和术语基准。 | 第 2-4 天、第 7-8 天 |
| 2 | 廖雪峰 Git 教程 | https://www.liaoxuefeng.com/wiki/896043488029600 | 中文教程 | 创建版本库、工作区/暂存区、add/commit、远程仓库、分支、冲突 | 明确面向初学者，强调“工作区-暂存区-版本库”三层结构，对 `git add` 和 `git commit` 的顺序解释友好，适合做主线入门材料。 | 第 2-3 天、第 6-7 天 |
| 3 | 菜鸟教程 Git 教程 | https://www.runoob.com/git/git-tutorial.html | 中文教程 | Git 安装、工作流程、创建仓库、基本操作、分支、GitHub | 内容覆盖面广，适合补齐命令速查和快速上手练习，适合作为课程中的“查漏补缺”和命令字典。 | 第 1-8 天全程参考 |
| 4 | 在 GitHub 上创建帐户 | https://docs.github.com/zh/get-started/start-your-journey/creating-an-account-on-github | GitHub 官方文档 | GitHub 账号创建 | 说明注册 GitHub 个人账户、验证邮箱、后续入门步骤；适合在真正创建仓库前做平台准备说明。 | 第 1 天 |
| 5 | 关于 Git | https://docs.github.com/zh/get-started/using-git/about-git | GitHub 官方文档 | Git 概念、仓库、clone/add/commit/merge 协作背景 | 用较少篇幅解释版本控制、仓库、命令行与 GitHub 协作模型，适合作为“为什么要学 Git 和 GitHub”的概念导入。 | 第 1 天 |
| 6 | 仓库快速入门 | https://docs.github.com/zh/repositories/creating-and-managing-repositories/quickstart-for-repositories | GitHub 官方文档 | 仓库创建、README、首次提交 | 直接演示创建仓库、初始化 README、编辑并提交第一个变更，适合课程设计中的第一份 GitHub 实操。 | 第 2 天 |
| 7 | 使用 SSH 连接到 GitHub | https://docs.github.com/zh/authentication/connecting-to-github-with-ssh | GitHub 官方文档 | SSH 连接总览 | 给出 SSH 连接 GitHub 的总入口，串起“检查现有密钥—生成密钥—添加到账户—测试连接—排错”的完整路径。 | 第 4 天 |
| 8 | 生成新的 SSH 密钥并将其添加到 ssh-agent | https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent | GitHub 官方文档 | SSH 密钥生成、ssh-agent | 说明如何生成新 SSH key、为什么需要 passphrase、如何把密钥加入 agent；适合手把手配置 SSH 登录。 | 第 4 天 |
| 9 | 推送提交到远程仓库 | https://docs.github.com/zh/get-started/using-git/pushing-commits-to-a-remote-repository | GitHub 官方文档 | `git push`、远程分支、推送失败提示 | 解释 `git push REMOTE BRANCH` 的基本形态，以及重命名分支、非快进错误、推送标签等操作，是理解 push 的核心材料。 | 第 5 天 |
| 10 | 从远程仓库获取更改 | https://docs.github.com/zh/get-started/using-git/getting-changes-from-a-remote-repository | GitHub 官方文档 | `git clone`、`fetch`、`merge`、`pull` | 清晰区分 `clone`、`fetch`、`merge` 和 `pull` 的关系，并明确 `pull = fetch + merge`，适合帮助新手理解“拉取”到底做了什么。 | 第 5 天 |
| 11 | 处理非快进错误 | https://docs.github.com/zh/get-started/using-git/dealing-with-non-fast-forward-errors | GitHub 官方文档 | `git push` 报错 | 直接给出 `non-fast-forward` 的典型报错和 `fetch + merge` / `pull` 的修复思路，适合做课程中的第一个远程同步报错案例。 | 第 5 天或第 8 天 |
| 12 | GitHub Flow | https://docs.github.com/zh/get-started/using-github/github-flow | GitHub 官方文档 | branch、commit、push、PR、协作流程 | 以 GitHub 官方协作流程说明“创建分支—提交并推送—发起 PR—讨论—合并”的轻量工作流，适合从命令转到协作实践。 | 第 6-7 天 |
| 13 | 关于拉取请求 | https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests | GitHub 官方文档 | Pull Request、审查、讨论 | 说明 PR 是“提议、评审、合并代码”的协作中枢，适合解释 GitHub 为什么不只是代码托管，而是协作平台。 | 第 7 天 |
| 14 | 关于合并冲突 | https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts | GitHub 官方文档 | merge 冲突与解决 | 解释冲突出现的典型情形、GitHub 上与本地解决的边界，以及 `git merge` 冲突提示示例。 | 第 8 天 |
| 15 | 错误：权限被拒绝（公钥） | https://docs.github.com/zh/authentication/troubleshooting-ssh/error-permission-denied-publickey | GitHub 官方文档 | SSH 报错排查 | 逐项说明 `Permission denied (publickey)` 的高频原因：错误域名、错误用户名、未加载密钥、账户未绑定公钥等，适合作为 SSH 排障清单。 | 第 4 天或第 8 天 |

## 覆盖映射

| 知识点 | 对应来源 |
|---|---|
| `git add` | 1, 2, 3, 5 |
| `git commit` | 1, 2, 3, 5, 6 |
| `git push` | 1, 2, 3, 9, 11, 12 |
| `git pull` | 1, 2, 3, 10, 11 |
| `branch` | 1, 2, 3, 12, 13 |
| `merge` | 1, 2, 3, 10, 12, 14 |
| SSH 配置 | 1, 7, 8, 15 |
| 仓库创建 | 2, 3, 4, 6 |
| 常见报错与解决 | 11, 14, 15 |

结论：指定知识点均已覆盖，且每类至少有 1-2 条主参考资料。

## 适合零基础者的课程化整理

### 第 1 天：先搞清 Git、GitHub、仓库、版本控制在解决什么问题
- 核心问题：为什么不是直接改文件发压缩包？
- 建议主资料：5《关于 Git》、4《在 GitHub 上创建帐户》
- 课程提示：
  - 先区分 Git（版本控制工具）与 GitHub（托管与协作平台）
  - 先让学习者注册账号、验证邮箱
  - 不急着背命令，先建立“快照、历史、协作”的心智模型

### 第 2 天：创建本地仓库与 GitHub 仓库，完成第一次提交
- 核心操作：创建仓库、初始化 README、第一次提交
- 建议主资料：6《仓库快速入门》、2《廖雪峰 Git 教程》
- 应讲命令：`git init`、`git status`、`git add`、`git commit`
- 教学重点：
  - `git add` 是“放进暂存区”
  - `git commit` 是“形成一张历史快照”
  - 一次提交最好只做一类改动

### 第 3 天：理解工作区、暂存区、版本库，避免“为什么改了却没提交上去”
- 建议主资料：2《廖雪峰 Git 教程》、1《Pro Git》
- 应讲命令：`git add`、`git commit -m`、`git status`、`git log`
- 典型误区：
  - 只修改文件但没 `add`
  - `add` 之后又改文件，不知道哪些内容进了提交
  - 提交信息太模糊，如 `update`、`fix`、`1`

### 第 4 天：配置 SSH，解决“每次推送都认证失败”问题
- 建议主资料：7《使用 SSH 连接到 GitHub》、8《生成新的 SSH 密钥并将其添加到 ssh-agent》、15《错误：权限被拒绝（公钥）》
- 实操顺序：
  1. 检查是否已有 SSH key
  2. 生成新密钥
  3. 加入 `ssh-agent`
  4. 将公钥加到 GitHub 账户
  5. 测试 `ssh -T git@github.com`
- 高风险坑点：
  - 用了错误用户名，如 `用户名@github.com` 而不是 `git@github.com`
  - 公钥没有加到 GitHub 账户
  - 用 `sudo git push` 导致读到另一套密钥

### 第 5 天：学会 `push` / `pull` / `fetch` / `clone`
- 建议主资料：10《从远程仓库获取更改》、9《推送提交到远程仓库》、11《处理非快进错误》
- 核心理解：
  - `clone`：第一次把远程仓库完整拉到本地
  - `fetch`：只更新远程信息，不自动合并
  - `merge`：把别人的更新合到当前分支
  - `pull`：`fetch + merge`
  - `push`：把本地提交发到远程仓库
- 高风险坑点：
  - 远程已有新提交时直接 `push`，触发 `non-fast-forward`
  - 误把 `pull` 当“下载按钮”，忽略其包含合并动作

### 第 6 天：开始使用分支，避免多人直接改主分支
- 建议主资料：12《GitHub Flow》、2《廖雪峰 Git 教程》、1《Pro Git》
- 应讲命令：`git branch`、`git switch -c` / `git checkout -b`、`git merge`
- 课程重点：
  - 一项功能一个分支
  - 分支名要描述性强
  - 先在分支上改，再合并回主分支

### 第 7 天：理解 GitHub 协作流程，而不只是“会用命令”
- 建议主资料：12《GitHub Flow》、13《关于拉取请求》
- 协作顺序：
  1. 创建分支
  2. 本地修改并提交
  3. 推送分支到 GitHub
  4. 发起 Pull Request
  5. 讨论与修改
  6. 合并 PR
- 对零基础者的重要性：
  - 让学习者知道“代码协作”不是靠口头说，而是靠提交历史与评审记录

### 第 8 天：集中讲报错与冲突处理
- 建议主资料：11《处理非快进错误》、14《关于合并冲突》、15《错误：权限被拒绝（公钥）》
- 必讲报错：
  - `Permission denied (publickey)`
  - `non-fast-forward`
  - merge conflict / `CONFLICT (content)`
- 建议教学方式：
  - 用一个最小示例仓库主动制造冲突
  - 让学习者亲手经历“报错—定位—修复—重新提交”闭环

## 推荐优先级

### 第一优先级：可直接作为课程主干
1. 廖雪峰 Git 教程
2. GitHub 官方《仓库快速入门》
3. GitHub 官方《从远程仓库获取更改》
4. GitHub 官方《GitHub Flow》
5. GitHub 官方 SSH 与报错排查文档

### 第二优先级：作为术语校验与延伸阅读
1. Pro Git（简体中文版）
2. 菜鸟教程 Git 教程
3. GitHub 官方《关于拉取请求》
4. GitHub 官方《关于合并冲突》

## 给 28 天课程的插入建议

如果后续扩展到完整 28 天课程，本主题建议集中放在第 1 周后半段：

- 第 1 天：Git/GitHub 是什么、账号创建
- 第 2 天：创建仓库、第一次提交
- 第 3 天：工作区/暂存区/提交历史
- 第 4 天：SSH 配置与远程连接
- 第 5 天：push / pull / fetch / clone
- 第 6 天：branch / merge
- 第 7 天：GitHub Flow、Pull Request、协作习惯
- 第 8 天：常见报错、冲突处理、复盘练习

## 可直接用于课程写作的命令清单

```bash
git init
git status
git add README.md
git commit -m "docs: add README"
git clone <repo-url>
git pull origin main
git push origin main
git branch
git switch -c feature/demo
git merge feature/demo
ssh -T git@github.com
```

## 本轮调研结论

1. 对零基础学习者，最重要的不是一次性记住很多命令，而是理解“本地修改 → 暂存 → 提交 → 推送 → 协作合并”的顺序。
2. SSH 配置和远程同步报错是新手最容易卡住的环节，课程中必须单独拆一天并配排障清单。
3. 分支与 PR 应尽早引入，否则学习者容易把 Git 理解为“本地备份工具”，而不是协作工具。
4. 适合作为课程主线的材料应以 GitHub 中文官方文档 + 廖雪峰教程为主，Pro Git 用于校准概念边界，菜鸟教程用于命令补查。

## 参考链接汇总

1. https://git-scm.com/book/zh/v2
2. https://www.liaoxuefeng.com/wiki/896043488029600
3. https://www.runoob.com/git/git-tutorial.html
4. https://docs.github.com/zh/get-started/start-your-journey/creating-an-account-on-github
5. https://docs.github.com/zh/get-started/using-git/about-git
6. https://docs.github.com/zh/repositories/creating-and-managing-repositories/quickstart-for-repositories
7. https://docs.github.com/zh/authentication/connecting-to-github-with-ssh
8. https://docs.github.com/zh/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
9. https://docs.github.com/zh/get-started/using-git/pushing-commits-to-a-remote-repository
10. https://docs.github.com/zh/get-started/using-git/getting-changes-from-a-remote-repository
11. https://docs.github.com/zh/get-started/using-git/dealing-with-non-fast-forward-errors
12. https://docs.github.com/zh/get-started/using-github/github-flow
13. https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
14. https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts
15. https://docs.github.com/zh/authentication/troubleshooting-ssh/error-permission-denied-publickey
