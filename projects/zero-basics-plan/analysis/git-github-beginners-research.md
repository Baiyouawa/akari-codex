# Git 与 GitHub 零基础调研笔记

## 任务范围

覆盖以下主题，并整理成适合零基础学习者的教程骨架与练习：

- 版本控制概念
- 仓库初始化
- commit
- branch
- merge
- rebase
- remote
- Pull Request
- Issue
- 协作流程

## 资料筛选标准

- **优先官方文档**：降低二手误解风险。
- **优先可循序渐进的材料**：适合第一次接触命令行与代码托管平台的学习者。
- **练习必须可独立完成**：不依赖复杂环境。
- **概念和命令同时给出**：避免“只会抄命令，不理解为什么”。

## 结论摘要

1. **Git 与 GitHub 应拆开讲**：Git 是本地版本控制工具，GitHub 是远程托管与协作平台；初学者常把两者混为一谈。来源：Pro Git 第 1 章与 GitHub Docs「Using Git」总览。  
   - Pro Git: https://git-scm.com/book/en/v2  
   - GitHub Docs: https://docs.github.com/get-started/using-git
2. **初学顺序应为“本地 Git → 分支协作 → 远程仓库 → GitHub PR/Issue”**，而不是一开始就讲复杂团队流程。来源：Pro Git 目录顺序、Git 官方 Reference 分类、GitHub flow 文档。  
   - https://git-scm.com/book/en/v2  
   - https://git-scm.com/docs  
   - https://docs.github.com/en/get-started/using-github/github-flow
3. **branch / merge 应先于 rebase**：rebase 虽常见，但会改写提交历史；对零基础学习者应先建立“分支合并”的安全心智模型，再引入 rebase。来源：Pro Git 第 3 章先讲 basic branching and merging，再讲 rebasing。  
   - https://git-scm.com/book/en/v2
4. **交互式练习需要额外补充**：官方文档适合查阅与系统学习，但分支/历史变换的直观理解，`Learn Git Branching` 更适合作为练习平台。来源：网站说明其在浏览器中模拟 Git 仓库。  
   - https://learngitbranching.js.org/
5. **GitHub 协作流程最适合用 GitHub flow 讲解**：创建分支、提交修改、开 PR、讨论、合并，结构清晰，适合作为新手第一套协作工作流。来源：GitHub Docs「GitHub flow」。  
   - https://docs.github.com/en/get-started/using-github/github-flow

## 新手常见误区

### 1. 把 GitHub 当成 Git

纠正方式：
- Git 负责记录历史。
- GitHub 负责托管仓库、讨论问题、提交流程和协作。

### 2. 只会复制命令，不知道命令作用在哪一层

建议把命令分成 3 层：
- **工作区**：你正在编辑的文件
- **暂存区**：准备进入下一次提交的变更
- **仓库历史**：已经提交保存的版本

### 3. 太早使用 rebase 处理冲突

对新手应先建立规则：
- 自己本地整理提交，可以学 `rebase`
- 公共分支历史，先不要随便改写

### 4. 认为 PR 只是“提交代码”

PR 本质上也是：
- 让别人看差异
- 讨论设计与实现
- 连接 Issue
- 记录为什么要改

## 推荐资料清单

### A. Git 核心入门

#### 1. Pro Git（Book）
- 链接：https://git-scm.com/book/en/v2
- 类型：系统教程 / 参考书
- 难度：入门到中级
- 推荐理由：内容覆盖完整，从版本控制基础到分支、远程、GitHub 协作都有系统说明。
- 适合使用方式：作为主线阅读材料，不要求一次读完；新手优先读 1、2、3、6 章中的基础部分。

#### 2. Git Reference
- 链接：https://git-scm.com/docs
- 类型：官方命令参考
- 难度：入门查表 / 中级深入
- 推荐理由：可以确认 `git init`、`git commit`、`git branch`、`git merge`、`git rebase`、`git remote` 等命令的正式说明。
- 适合使用方式：在做练习时对照查询，不适合完全从头顺序读完。

#### 3. Git 仓库入门章节（Pro Git 2.1）
- 链接：https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository
- 类型：入门章节
- 难度：入门
- 推荐理由：明确讲解“如何得到一个 Git 仓库”，对应 `git init` 和 `git clone` 的新手起点。

### B. GitHub 协作入门

#### 4. GitHub Docs — Using Git
- 链接：https://docs.github.com/get-started/using-git
- 类型：GitHub 官方入口页
- 难度：入门
- 推荐理由：把 Git 与 GitHub 关联起来，适合作为 GitHub 生态入口。

#### 5. GitHub flow
- 链接：https://docs.github.com/en/get-started/using-github/github-flow
- 类型：协作流程指南
- 难度：入门
- 推荐理由：用最小流程说明“建分支 → 修改 → PR → 讨论 → 合并”，适合零基础第一次理解团队协作。

#### 6. About issues
- 链接：https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
- 类型：功能说明
- 难度：入门
- 推荐理由：解释 Issue 可用于跟踪 bug、功能、想法和任务，有助于让新手理解 GitHub 不只是“代码网盘”。

#### 7. Quickstart for repositories
- 链接：https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories
- 类型：仓库快速开始
- 难度：入门
- 推荐理由：适合第一次创建 GitHub 仓库、理解 README、分支、协作设置等基本仓库概念。

#### 8. Contributing to open source
- 链接：https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source
- 类型：贡献流程介绍
- 难度：入门到初级
- 推荐理由：帮助学习者把 Fork、Issue、PR、Review 放到真实开源协作场景中理解。

### C. 交互式练习

#### 9. Learn Git Branching
- 链接：https://learngitbranching.js.org/
- 类型：浏览器交互练习
- 难度：入门到初级
- 推荐理由：适合练 branch、merge、rebase 的可视化路径；对新手理解“提交历史怎么移动”很有效。

## 面向零基础的教程结构建议

## 1. 先讲清楚 Git 与 GitHub 的区别

可直接用下面的解释：

- **Git**：保存文件历史，支持回退、对比、分支开发。
- **GitHub**：把 Git 仓库放到云端，并提供协作能力，如仓库页面、Issue、PR、Review。

## 2. 命令教学顺序

建议顺序：

1. `git init`
2. `git status`
3. `git add`
4. `git commit`
5. `git log`
6. `git branch`
7. `git switch`
8. `git merge`
9. `git remote add`
10. `git push`
11. `git pull`
12. `git rebase`（最后再讲）

原因：前 1-5 步先建立本地心智模型；6-8 理解多人并行开发；9-11 才连接 GitHub；12 用于整理历史与同步上游。

## 3. 每个知识点都给“一句话理解 + 最小命令 + 可见结果”

示例：

### commit
- 一句话理解：一次 commit 就是“给当前已暂存的变更拍一张可回溯快照”。
- 最小命令：`git add . && git commit -m "初始化项目"`
- 可见结果：`git log --oneline` 能看到新提交。

### branch
- 一句话理解：branch 是一条独立开发线，不会立刻污染主线。
- 最小命令：`git switch -c feature/readme`
- 可见结果：`git branch` 中当前分支前面有 `*`。

### merge
- 一句话理解：把另一条分支的成果合进当前分支。
- 最小命令：`git merge feature/readme`
- 可见结果：主分支出现对应修改，可能产生 merge commit。

### rebase
- 一句话理解：把“我的提交”改挂到新的基础提交后面，历史更直，但可能改写提交 ID。
- 最小命令：`git rebase main`
- 可见结果：提交顺序改变；如果有冲突，要逐个解决后继续 `git rebase --continue`。

## 新手友好教程草案

## 第 1 节：为什么需要版本控制

- 没有版本控制时，常见文件名会变成：`final.docx`、`final2.docx`、`final_真的最终版.docx`
- 版本控制解决的问题：
  - 记录每次修改
  - 比较差异
  - 回到旧版本
  - 多人同时改

建议配套操作：
- 建一个 `notes/` 目录
- 新建 `todo.txt`
- 连续修改三次，观察 Git 如何记录变化

## 第 2 节：初始化本地仓库

推荐命令：

```bash
git init
git status
```

新手解释：
- `git init`：让当前文件夹开始被 Git 管理
- `git status`：查看 Git 眼里的当前状态

练习：
1. 新建 `hello.txt`
2. 写入一行内容
3. 运行 `git status`
4. 观察 untracked files 提示

## 第 3 节：add 与 commit

推荐命令：

```bash
git add hello.txt
git commit -m "添加 hello.txt"
```

新手解释：
- `add`：把改动放进“待提交清单”
- `commit`：正式记录到历史中

练习：
1. 修改 `hello.txt`
2. 再次 `git status`
3. `git add` 后再看一次 `git status`
4. 提交并用 `git log --oneline` 查看结果

## 第 4 节：branch 与并行开发

推荐命令：

```bash
git switch -c feature-title
```

新手解释：
- 主分支保持稳定
- 新功能放到新分支上做

练习：
1. 在新分支修改 `hello.txt`
2. 回到主分支
3. 对比文件内容变化
4. 再切回功能分支确认改动仍在

## 第 5 节：merge

推荐命令：

```bash
git switch main
git merge feature-title
```

新手解释：
- merge 是把分支成果合并回来
- 如果两边改了同一位置，可能冲突

练习：
1. 建两个分支分别改同一行
2. 尝试合并
3. 观察冲突标记
4. 手动解决并完成 commit

## 第 6 节：rebase

推荐讲法：
- 先讲用途：保持历史更直
- 再讲风险：会重写提交历史
- 最后给规则：**只在自己可控的分支上练**

基础命令：

```bash
git switch feature-title
git rebase main
```

练习：
1. main 新增一个提交
2. feature 分支也新增一个提交
3. 在 feature 上执行 `git rebase main`
4. 用 `git log --oneline --graph --all` 观察历史变化

## 第 7 节：remote 与连接 GitHub

推荐命令：

```bash
git remote add origin <仓库URL>
git remote -v
git push -u origin main
```

新手解释：
- remote 就是“给远程仓库起一个本地别名”
- `origin` 只是惯例，不是强制名字

练习：
1. 在 GitHub 创建空仓库
2. 本地仓库执行 `remote add`
3. 推送到 GitHub
4. 刷新网页确认文件已出现

## 第 8 节：Issue、PR 与协作流程

建议流程：
1. 用 Issue 记录要做什么
2. 从 Issue 创建或关联一个分支
3. 本地修改并 push
4. 提交 Pull Request
5. 在 PR 中说明变更、截图、验证方式
6. Review 后合并

新手解释：
- **Issue**：讨论问题和任务
- **PR**：讨论具体代码改动

练习：
1. 新建一个 Issue：例如“补充 README 安装步骤”
2. 新建分支修复
3. push 到 GitHub
4. 开一个 PR，并在描述中写 `Closes #1`（其中 `#1` 替换成实际 Issue 编号）

## 推荐协作工作流

最适合零基础的流程：

1. `main` 保持稳定
2. 每个任务开一个分支
3. 小步提交，commit message 讲清意图
4. push 到远程
5. 开 PR
6. 讨论与修改
7. 合并回 `main`

可配套一句提醒：
- **merge 更适合先学会协作**
- **rebase 更适合后面学会整理历史**

## 练习设计

## 练习 1：个人仓库最小闭环

目标：完成本地初始化到首次推送。

步骤：
1. 新建目录并 `git init`
2. 创建 `README.md`
3. commit
4. 在 GitHub 创建仓库
5. 添加 remote
6. push

验收：
- 本地 `git log --oneline` 至少有 1 条提交
- GitHub 页面能看到 README

## 练习 2：分支开发

目标：理解 branch 不会直接污染主分支。

步骤：
1. 从 `main` 切出 `feature/about-me`
2. 修改 `README.md`
3. 提交
4. 切回 `main`
5. 对比文件
6. merge 回来

验收：
- 学员能口头解释“为什么分支安全”

## 练习 3：制造并解决 merge conflict

目标：不再害怕冲突。

步骤：
1. 两个分支修改同一行
2. 执行 merge
3. 阅读冲突标记
4. 解决冲突并提交

验收：
- 能说明 `<<<<<<<`、`=======`、`>>>>>>>` 的含义

## 练习 4：可视化 rebase

目标：理解 rebase 是“换基础提交”。

工具：Learn Git Branching
- https://learngitbranching.js.org/

验收：
- 学员能描述 merge 和 rebase 的历史图差别

## 练习 5：GitHub 协作模拟

目标：走完一次最小协作流程。

步骤：
1. 创建 Issue
2. 创建分支
3. 修改文件并推送
4. 发起 PR
5. 在 PR 描述中关联 Issue
6. 合并 PR 并关闭 Issue

验收：
- Issue、分支、PR 三者能串起来

## 适合放入 28 天课程的拆分建议

如果后续要并入《零基础计划》总课表，Git / GitHub 建议占 **5 天主线 + 1 次周末整合练习**：

- Day 1：版本控制概念、Git 与 GitHub 区别
- Day 2：`init`、`status`、`add`、`commit`
- Day 3：`branch`、`switch`、`merge`
- Day 4：remote、push、pull、GitHub 仓库
- Day 5：Issue、PR、GitHub flow
- 周末整合：完成一次从 Issue 到 PR 的小协作练习

## 课程编写提醒

1. 每个命令首次出现时都要配中文解释。  
2. 每节课都要有“看得见的结果”，如 `git status`、`git log --oneline`、GitHub 页面截图。  
3. `rebase` 必须附带“不要改写公共历史”的警示。  
4. PR 模板里应要求填写：改了什么、为什么改、怎么验证。  
5. 练习素材应尽量用文本文件和 README，减少环境配置干扰。

## 来源与可追溯性

- Pro Git 第二版总目录与章节结构：https://git-scm.com/book/en/v2
- Pro Git《Getting a Git Repository》：https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository
- Git 官方命令参考：https://git-scm.com/docs
- git-init 手册：https://git-scm.com/docs/git-init
- git-commit 手册：https://git-scm.com/docs/git-commit
- git-branch 手册：https://git-scm.com/docs/git-branch
- git-merge 手册：https://git-scm.com/docs/git-merge
- git-rebase 手册：https://git-scm.com/docs/git-rebase
- git-remote 手册：https://git-scm.com/docs/git-remote
- GitHub Docs《Using Git》：https://docs.github.com/get-started/using-git
- GitHub Docs《GitHub flow》：https://docs.github.com/en/get-started/using-github/github-flow
- GitHub Docs《About issues》：https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
- GitHub Docs《Quickstart for repositories》：https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories
- GitHub Docs《Contributing to open source》：https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source
- Learn Git Branching：https://learngitbranching.js.org/
