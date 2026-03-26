# Git 本地工作流入门补齐：`init` / `add` / `commit` / `log` / `branch` / `merge`

- 调研时间：2026-03-26
- 适用项目：`projects/zero-basics-plan`
- 适用读者：第一次在纯本地环境使用 Git 的初学者
- 范围边界：只讲本地仓库工作流，不把 `push` / `pull` / PR 作为主线；远程协作留给第 3 周
- 资料要求：优先官方文档，辅以中文教程、博客与社区资料，保证新手可读性与可追溯性

## 学习目标

学完本节后，读者应能独立完成下面这条本地闭环：

1. 新建练习目录并执行 `git init`
2. 创建或修改文件后用 `git add` 放入暂存区
3. 用 `git commit` 保存一次可回看的历史快照
4. 用 `git log --oneline` 查看历史
5. 创建并切换到新分支，继续修改并提交
6. 切回主线并执行 `git merge`
7. 遇到最常见报错时，知道先看什么、怎么修

## 一条主线先看懂：工作区、暂存区、提交历史

Git 本地工作流里最容易卡住的，不是命令拼写，而是不知道“改动现在到底在哪一层”。

- **工作区（working directory）**：你眼前真实可见的文件夹和文件
- **暂存区（stage / index）**：准备纳入下一次提交的改动清单
- **提交历史（commit history）**：已经正式保存下来的版本节点

廖雪峰在《工作区和暂存区》中把这三层关系讲得很直白：`git add` 是把修改加入暂存区，`git commit` 是把暂存区内容一次性提交到当前分支。Git 官方 `gittutorial` 也把“importing a new project → making changes → viewing project history → managing branches”作为入门主线。

## 最小可复现练习：从空目录到一次分支合并

下面这组命令故意只依赖本地 Git，不依赖 GitHub。

```bash
mkdir git-local-demo
cd git-local-demo

git init

echo "# Git Local Demo" > README.md
git add README.md
git commit -m "init"

git log --oneline

git branch feature-notes
git switch feature-notes

echo "first branch line" >> README.md
git add README.md
git commit -m "add branch note"

git switch master   # 如果你的默认分支名是 main，这里改成 main
git merge feature-notes

git log --oneline --graph --decorate --all
```

### 你在这条主线里做了什么

1. `git init`：把当前目录变成 Git 仓库
2. `git add README.md`：告诉 Git，README 这次要纳入下一次提交
3. `git commit -m "init"`：正式保存一个历史节点
4. `git log --oneline`：确认历史里真的有这次提交
5. `git branch feature-notes`：创建一条新分支
6. `git switch feature-notes`：切到新分支继续做实验，不影响主线
7. 再次 `add` + `commit`：把分支上的修改单独保存下来
8. `git merge feature-notes`：把分支工作并回当前分支

### 命令执行后你应该看到的现象

- `git init` 后目录中会出现隐藏目录 `.git`
- 第一次 `commit` 后，`git log --oneline` 至少能看到 1 条提交
- 分支提交完成后，`git log --oneline --graph --decorate --all` 应能看到主线和 `feature-notes` 都指向相关提交
- 如果主线在切回后没有额外改动，合并大概率会显示 **fast-forward**

## 六个核心命令逐个讲

## `git init`

### 它是干什么的

Git 官方 `git-init` 文档说明：这个命令会“创建一个空的 Git 仓库，或者重新初始化一个已存在仓库”，本质上是在目录下创建 `.git` 元数据目录，并建立一个还没有提交记录的初始分支。

### 什么时候用

- 第一次把普通文件夹纳入 Git 管理
- 做练习时新建一个本地实验仓库

### 最小示例

```bash
git init
```

也可以直接对一个新目录执行：

```bash
git init my-first-repo
cd my-first-repo
```

### 注意事项

- `git init` 只是“建仓库”，**不会自动生成第一次提交**
- 看到 `.git` 目录说明仓库初始化成功，但此时历史还是空的
- Git 官方文档还提到可用 `-b <分支名>` 指定初始分支名；入门阶段知道有这个能力就够了，不必一开始就背参数

### 新手常见误区

- 误以为 `git init` 之后文件就已经“保存到 Git 里了”——其实还没有，需要 `add` 和 `commit`
- 在错误目录执行 `git init`，把上层大目录整个变成仓库

## `git add`

### 它是干什么的

Git 官方 `git-add` 文档把它定义为“Add file contents to the index”，也就是把文件内容加入索引/暂存区。廖雪峰教程则用更适合新手的话解释：`git add` 是把要提交的修改先放到暂存区。

### 什么时候用

- 你已经改完某个文件，准备让它进入下一次提交
- 你想先挑一部分文件进入本次提交，而不是把所有改动一次性都交上去

### 最小示例

```bash
git add README.md
```

添加当前目录所有已跟踪与未跟踪改动时，经常会写：

```bash
git add .
```

### 注意事项

- `git add` 不会生成历史记录，只是“放入待提交清单”
- 想确认哪些内容已经进入暂存区，先看 `git status`
- 对新手来说，优先练熟“按文件 add”，再用 `git add .`

### 新手常见误区

- 误以为 `git add` 就等于“提交成功”
- 在不确认文件范围时直接 `git add .`，把不该提交的临时文件也带进去了

## `git commit`

### 它是干什么的

Git 官方 `git-commit` 文档说明：`git commit` 是把暂存区内容与项目元数据一起记录成一次提交。你可以把它理解成“把这次确定好的改动保存成一个可回看的版本节点”。

### 什么时候用

- 已经确认暂存区中的内容就是你本次想保存的改动
- 想让当前工作形成一个明确的阶段性历史点

### 最小示例

```bash
git commit -m "init"
```

### 提交信息怎么写更适合初学者

入门阶段先做到两点：

- 一次提交只表达一件事
- 提交信息能让未来的你看懂

例如：

- `init`
- `add readme introduction`
- `fix typo in notes`
- `merge feature-notes`

### 注意事项

- 没先 `git add`，通常就没有可提交内容
- 首次提交前，经常需要先配置用户名和邮箱
- `git commit` 保存的是**暂存区**，不是“工作区里所有看得见的最新内容”

### 新手常见误区

- 修改完文件就直接 `git commit -m "..."`，结果提示没东西可提交
- 提交信息只写 `update`、`test`、`1`，后面很难回看

## `git log`

### 它是干什么的

Git 官方 `git-log` 文档的核心用途是查看提交历史。对初学者来说，它的价值是：你不再只靠记忆，而是能真的看到“刚才提交过什么”。

### 什么时候用

- 想确认某次提交是否成功
- 想按时间顺序回看历史
- 想观察分支和合并后的历史形状

### 最小示例

```bash
git log --oneline
```

稍微更直观一点：

```bash
git log --oneline --graph --decorate --all
```

### 注意事项

- 初学者优先使用 `--oneline`，不然默认输出容易太长
- 看分支合并效果时，`--graph --decorate --all` 很有帮助

### 新手常见误区

- 只会提交，不会回头看历史，导致不知道自己到底保存了什么
- 看到一大段完整日志就紧张，其实先看一行版就够了

## `git branch`

### 它是干什么的

Git 官方 `git-branch` 文档用于“列出、创建或删除分支”。廖雪峰在《创建与合并分支》中用指针移动来解释：新分支本质上是一条指向某个提交的新指针，所以创建分支很快。

### 什么时候用

- 想隔离一项新尝试，不直接在主线上乱改
- 想并行试验两个版本

### 最小示例

查看分支：

```bash
git branch
```

创建分支：

```bash
git branch feature-notes
```

更常见的新写法是直接切换：

```bash
git switch -c feature-notes
```

### 注意事项

- `git branch feature-notes` 只创建，不切换
- 当前分支前面会有 `*`
- 分支只是帮你隔离工作，不是复制一整个项目目录

### 新手常见误区

- 以为建了分支就自动切过去了
- 在主分支上继续改，忘了先切到功能分支

## `git merge`

### 它是干什么的

Git 官方 `git-merge` 文档说明：它会把某个分支的历史整合进当前分支。GitHub Docs 对冲突的解释也很适合入门：当两个分支有相互竞争的修改，Git 需要你来决定最终保留什么内容。

### 什么时候用

- 分支上的修改已经完成，准备并回主线
- 想把另一条本地分支的结果纳入当前分支

### 最小示例

先切回主线：

```bash
git switch master   # 或 main
```

再执行合并：

```bash
git merge feature-notes
```

### 注意事项

- `git merge feature-notes` 的意思是：**把 `feature-notes` 合进当前分支**
- 如果两边没有竞争修改，可能直接 fast-forward
- 如果两边改了同一行，可能出现冲突，需要手动解决

### 新手常见误区

- 在错误分支上执行 merge，结果把方向弄反
- 看到冲突就以为仓库坏了；其实冲突是协作和并行修改里的正常现象

## 一张表看懂六个命令的顺序关系

| 命令 | 在工作流里的位置 | 你可以把它理解成什么 | 最小示例 |
|---|---|---|---|
| `git init` | 起点 | 建立仓库 | `git init` |
| `git add` | 提交前 | 把改动放进待提交清单 | `git add README.md` |
| `git commit` | 保存节点 | 正式记下一次版本快照 | `git commit -m "init"` |
| `git log` | 回看历史 | 看自己已经保存过什么 | `git log --oneline` |
| `git branch` | 并行开发 | 给新任务开一条支线 | `git branch feature-notes` |
| `git merge` | 收束分支 | 把支线成果并回当前线 | `git merge feature-notes` |

## 常见错误处理：至少先看 `git status`

下面这些问题，都是初学者本地练习时高频会遇到的。

## 1. `Author identity unknown` / 要求配置用户名邮箱

### 常见现象

第一次提交时，Git 提示你没有配置 `user.name` 和 `user.email`。

### 原因

Git 需要知道这次提交是谁创建的。

### 解决方法

```bash
git config --global user.name "你的名字"
git config --global user.email "you@example.com"
```

配置后再重新提交：

```bash
git commit -m "init"
```

### 提醒

- `--global` 会作用于当前用户后续仓库
- 如果是公共机器，先确认是否应该使用全局配置

### 来源

- `gittutorial` 明确建议开始操作前先介绍自己的名字和公开邮箱
- `git-commit` 官方手册用于核对提交行为

## 2. `nothing to commit, working tree clean`

### 常见现象

你刚敲完 `git commit -m "..."`，却看到“nothing to commit”。

### 原因

通常是两种情况：

1. 你其实没有新改动
2. 你改动过，但已经提交过，当前工作区又恢复成干净状态

### 排查步骤

```bash
git status
git log --oneline -n 3
```

### 解决方法

- 如果本来就没有新改动：无需修
- 如果忘了改文件：先改，再 `git add` + `git commit`

### 提醒

不要把这条提示当报错；很多时候它只是在告诉你“仓库目前是干净的”。

## 3. 改了文件却提示“no changes added to commit”

### 常见现象

`git status` 显示有 modified 文件，但提交时没有进入提交记录。

### 原因

你只改了工作区，还没执行 `git add`。

### 解决方法

```bash
git add 文件名
git commit -m "describe change"
```

### 提醒

这是理解“工作区 ≠ 暂存区”的关键练习题。

### 来源

- 廖雪峰《工作区和暂存区》
- `git-add` 官方文档

## 4. 创建了分支，但切换时报“pathspec ... did not match”或找不到分支

### 常见现象

你想切换到某个分支，但 Git 说找不到。

### 原因

- 分支名拼错
- 你只记得要切分支，但其实还没创建

### 排查步骤

```bash
git branch
```

### 解决方法

如果还没创建：

```bash
git switch -c feature-notes
```

如果已经创建，只是没切过去：

```bash
git switch feature-notes
```

### 提醒

先 `git branch` 看现状，比盲猜分支名更稳。

## 5. `git merge` 出现冲突

### 常见现象

Git 提示：

```text
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

### 原因

GitHub Docs 说明：当两个分支对同一行或相互竞争的内容做了修改时，Git 无法自动判断最终保留哪一版。

### 排查步骤

```bash
git status
```

打开冲突文件，你通常会看到类似标记：

```text
<<<<<<< HEAD
当前分支内容
=======
待合并分支内容
>>>>>>> feature-notes
```

### 解决方法

1. 手动编辑文件，保留你真正想要的最终内容
2. 删除冲突标记 `<<<<<<<`、`=======`、`>>>>>>>`
3. 保存文件
4. 执行：

```bash
git add README.md
git commit -m "resolve merge conflict"
```

### 如果现在不想继续这次合并

```bash
git merge --abort
```

### 提醒

- 先理解两边分别想改什么，再决定最终内容
- 冲突不是事故，而是 Git 请你做最后裁决

### 来源

- GitHub Docs: About merge conflicts
- 廖雪峰《解决冲突》

## 6. 不小心把错误文件放进暂存区，想撤销 `git add`

### 常见现象

`git status` 里出现了本次不想提交的文件。

### 原因

常见于随手执行了 `git add .`。

### 解决方法

在廖雪峰旧教程里会看到：

```bash
git reset HEAD <file>
```

如果你只需要知道“把文件从暂存区拿出来”，先记住这个思路即可。入门阶段也可以直接重新练一遍最小仓库，不必急着背更多撤销命令。

### 风险提示

- 撤销暂存区和删除工作区文件不是一回事
- 先看 `git status` 再做撤销，避免把还想保留的改动也清掉

### 来源

- 廖雪峰《工作区和暂存区》中的 `git reset HEAD <file>` 示例
- Liuqi.dev《Git 工作流完全指南》中的“撤销 git add”案例

## 7. 默认分支不是 `master`，命令照抄后切换失败

### 常见现象

教程里写 `git switch master`，但你的仓库默认分支实际叫 `main`。

### 原因

不同 Git 版本和个人配置下，初始分支名可能不同。`git-init` 官方文档也说明可以通过 `--initial-branch` 指定初始分支名。

### 排查步骤

```bash
git branch
```

### 解决方法

看到当前主分支叫什么，就切回那个名字：

```bash
git switch main
```

或：

```bash
git switch master
```

### 提醒

入门教程里可以把“主线分支”理解为“当前主分支”，不要死记一个名字。

## 三组递进练习任务

## 练习 1：第一次本地提交

### 目标

完成一个从空目录到首个提交的闭环。

### 操作要求

1. 新建目录 `git-practice-1`
2. 执行 `git init`
3. 创建 `README.md`
4. 用 `git add README.md`
5. 用 `git commit -m "init"` 提交
6. 用 `git log --oneline` 查看历史

### 自检方式

- `git status` 应显示工作区干净
- `git log --oneline` 至少有 1 条提交
- 仓库根目录有隐藏的 `.git` 目录

## 练习 2：体验暂存区与分支

### 目标

理解“修改文件 ≠ 已提交”，并完成一次分支提交。

### 操作要求

1. 在练习 1 的仓库里再创建一个文件 `notes.txt`
2. 只把 `notes.txt` 加入暂存区并提交
3. 新建分支 `feature-notes`
4. 切到该分支，对 `README.md` 追加一行
5. 提交这次修改
6. 用 `git branch` 与 `git log --oneline --graph --decorate --all` 观察结果

### 自检方式

- 至少应看到 2 次提交
- `git branch` 应能看到当前所在分支前面的 `*`
- 图形日志里应能看到 `feature-notes` 指向较新的提交

## 练习 3：制造并解决一次简单合并冲突

### 目标

主动体验冲突，而不是等真实项目里第一次撞上时才慌。

### 操作要求

1. 在主分支和 `feature-notes` 分支分别修改 `README.md` 的同一行
2. 两边都各自提交
3. 切回主分支执行 `git merge feature-notes`
4. 观察冲突标记
5. 手动编辑为你想保留的最终文本
6. `git add README.md` 后 `git commit -m "resolve merge conflict"`

### 自检方式

- 冲突时 `git status` 会显示 unmerged paths
- 解决后 `git status` 应恢复干净
- `git log --oneline --graph --decorate --all` 能看到冲突解决后的提交

## 教学友好写法建议：可以直接并入 28 天教程

如果把这部分并回现有 28 天教程，建议拆成四个小模块：

1. **概念模块**：工作区、暂存区、提交历史
2. **命令模块**：`init/add/commit/log/branch/merge`
3. **错误处理模块**：配置身份、空提交、漏暂存、分支找不到、合并冲突、撤销误暂存
4. **练习模块**：首个提交、分支实验、冲突实验

这能直接补强现有 Day 12 与 Day 14，使读者不是只会抄命令，而是真的能跑通本地版本管理。

## 多样化参考资料清单

| 标题 | 来源类型 | 链接 | 用途说明 |
|---|---|---|---|
| Git 官方入门教程 `gittutorial` | 官方文档 | https://git-scm.com/docs/gittutorial | 作为本地工作流主线依据，覆盖导入项目、修改、历史、分支管理 |
| `git-init` 官方文档 | 官方文档 | https://git-scm.com/docs/git-init | 核对仓库初始化定义、`.git` 目录与初始分支说明 |
| `git-add` 官方文档 | 官方文档 | https://git-scm.com/docs/git-add | 核对“加入暂存区 / index”这一官方表述 |
| `git-commit` 官方文档 | 官方文档 | https://git-scm.com/docs/git-commit | 核对提交行为、版本更新信息与参数语义 |
| `git-log` 官方文档 | 官方文档 | https://git-scm.com/docs/git-log | 核对查看历史的标准命令 |
| `git-branch` 官方文档 | 官方文档 | https://git-scm.com/docs/git-branch | 核对分支创建、列出、删除的基础语义 |
| `git-merge` 官方文档 | 官方文档 | https://git-scm.com/docs/git-merge | 核对 fast-forward、冲突与合并行为 |
| 廖雪峰《工作区和暂存区》 | 中文教程 | https://liaoxuefeng.com/books/git/time-travel/working-stage/index.html | 用中文解释工作区、暂存区、提交三层关系 |
| 廖雪峰《创建与合并分支》 | 中文教程 | https://liaoxuefeng.com/books/git/branch/create/index.html | 用图和指针思路帮助新手理解分支与 fast-forward |
| 廖雪峰《解决冲突》 | 中文教程 | https://liaoxuefeng.com/books/git/branch/merge/index.html | 给出冲突标记样例与手工解决步骤 |
| GitHub Docs: About merge conflicts | 官方平台文档 | https://docs.github.com/articles/about-merge-conflicts | 用简洁语言解释冲突为何发生，适合错误处理段落 |
| Liuqi.dev《Git 工作流完全指南》 | 博客 | https://www.liuqi.dev/blog/git-workflow-complete-guide | 补充撤销暂存、日志查看、冲突处理等新手常见实践 |
| 知乎《Git 详细使用教程》 | 中文社区 | https://zhuanlan.zhihu.com/p/2014475666620448968 | 作为中文社区视角备选来源；本次抓取受 403 限制，保留作补充阅读而不作核心证据 |

## 本次采用与未采用说明

### 优先采用

- Git 官方文档与 `gittutorial`
- 廖雪峰教程
- GitHub Docs 的冲突说明
- 博客中的少量实践总结，用于补充新手排错视角

### 未作为主依据

- 知乎正文：本轮抓取遇到 403，无法在仓内完整核验正文，因此只保留为补充阅读入口，不把它写成关键事实来源
- 聚合转载站：虽然命令列表很多，但容易缺少上下文与风险提示

## 与现有 28 天教程的整合建议

- **Day 12**：加入工作区 / 暂存区 / 提交历史解释，并把 `git log --oneline` 提前为当天必做
- **Day 14**：把“系统课”中的 Git 部分改成“本地分支 → 合并 → 冲突处理”主线，再把远程 `push` 作为补充项
- **第 3 周**：再承接远程协作、Pull Request、GitHub Flow，避免初学者在还没理解本地工作流时就被远程概念压住

## 关键来源与版本记录

- Git 官方 `gittutorial`：页面显示 `last updated in 2.46.1`，抓取时间 2026-03-26
- Git 官方 `git-init`：页面显示 `last updated in 2.52.0`，抓取时间 2026-03-26
- Git 官方 `git-add`：页面显示 `last updated in 2.52.0`，抓取时间 2026-03-26
- Git 官方 `git-commit`：页面显示 `last updated in 2.53.0 / 2026-02-02`
- Git 官方 `git-log`：页面显示 `last updated in 2.53.0`
- Git 官方 `git-branch`：页面显示 `last updated in 2.51.0`
- Git 官方 `git-merge`：页面显示 `last updated in 2.53.0`
- GitHub Docs `About merge conflicts`：抓取时间 2026-03-26
- 廖雪峰《工作区和暂存区》《创建与合并分支》《解决冲突》：抓取时间 2026-03-26

## 结论

这部分内容已经满足“本地 Git 入门”可直接写入教程的最低闭环要求：

- 六个核心命令均已覆盖
- 已给出纯本地可复现主线
- 已覆盖至少 5 类高频错误
- 已提供 3 组递进练习
- 已给出官方 + 中文教程 + 博客 / 社区的多源参考资料

后续若继续扩写正式讲义，可再补：

1. 一张“工作区 / 暂存区 / 历史”的示意图
2. 一组 `git status` 典型输出截图
3. 一份专门面向 `main` 默认分支的新手提示框
