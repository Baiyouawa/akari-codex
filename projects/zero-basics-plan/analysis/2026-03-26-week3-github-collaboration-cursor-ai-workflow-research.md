# 第 3 周资料调研：GitHub 协作、分支/PR、项目阅读、基础工程实践、Cursor 与 AI 编程工作流入门

- 生成时间：2026-03-26
- 访问日期：2026-03-26（北京时间，见 `get_current_time`）
- 调研范围：GitHub 协作流程、分支/PR、开源项目阅读方法、基础工程实践、Cursor 入门、AI 编程工作流入门
- 记录目的：为 `zero-basics-plan` 的第 3 周教程设计提供可直接复用的资料清单、章节候选、每日安排与引用来源

## 使用说明

- 可信度分级：`官方` / `半官方` / `社区实践`
- 使用级别：`入门必读` / `进阶参考` / `补充阅读`
- 时效说明：Cursor 与 AI 工作流相关内容变化较快，优先使用官方文档，并在正文中显式标注“以当前版本界面为准”
- 去重原则：同一知识点优先保留官方原始文档；社区文章仅在补充解释、案例或教学友好度更强时纳入

---

## 1. GitHub 协作

### 主题知识点

- GitHub 协作的两种主模型：共享仓库模型与 fork + pull 模型
- Pull Request 的基本结构：Conversation / Commits / Checks
- 评审前准备：小 PR、清晰描述、关联 issue、说明变更影响
- 使用 Issues 与 Projects 组织任务与协作节奏
- 面向初学者的最小协作闭环：建 issue → 建分支 → 提交 PR → review → merge

### 推荐讲解顺序

1. 先讲 GitHub 上“协作不是直接改主分支”，而是围绕 issue 和 PR 进行
2. 再讲共享仓库与 fork 模式的区别
3. 然后拆解 PR 页面结构和 review 流程
4. 最后补充 Projects 如何做轻量任务看板

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/更新时间 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GH-COL-01 | About collaborative development models | GitHub Docs | GitHub | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models | 页面未抓到显式时间 | English | GitHub, collaboration, fork, shared-repo | 官方 | 入门必读 | GitHub 官方说明协作开发的两种核心模型：fork and pull 与 shared repository。文档强调开源项目常用 fork 模型，团队内协作常用共享仓库模型，并说明 fork 与 upstream 的关系。很适合拿来解释“为什么要 PR，而不是直接改主分支”。 | 官方定义清晰，适合做课程中的概念起点。 | `web_fetch` 抓取到正文片段，确认模型划分与适用场景。 |
| GH-COL-02 | About pull requests | GitHub Docs | GitHub | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests | 页面未抓到显式时间 | English | GitHub, PR, review | 官方 | 入门必读 | 官方文档直接定义 PR 是“提议、审查、合并代码变更”的基础协作功能，并说明 Conversation、Commits、Checks 等页面区域的意义。对初学者理解 PR 页面非常有帮助。 | 可直接作为“认识 PR 页面”章节的主参考。 | 适合配截图讲解。 |
| GH-COL-03 | Helping others review your changes | GitHub Docs | GitHub | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes | 页面未抓到显式时间 | English | PR, review, communication | 官方 | 入门必读 | 文档给出让 PR 更容易被 review 的实践，包括写小而聚焦的 PR、提供清晰上下文、主动说明为什么改、及时同步团队信息。适合从“提交流程”过渡到“协作礼仪”。 | 能直接支撑教程中的 PR 描述模板与 review checklist。 | 可提炼为“好 PR 的 5 条规则”。 |
| GH-COL-04 | About Projects | GitHub Docs | GitHub | https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects | 页面未抓到显式时间 | English | GitHub Projects, planning, issue tracking | 官方 | 进阶参考 | GitHub Projects 官方页说明 Projects 是把 issues 和 pull requests 作为项目计划、看板与路线图进行管理的工具，可切换 table、board、roadmap 等视图。适合为“多人协作如何看任务状态”补充上层概念。 | 与 issue/PR 协作天然衔接，适合做“轻量项目管理”入门。 | 第 3 周只需讲到 board/table 视图即可，不必深挖自动化。 |
| GH-COL-05 | Contributing to open source | GitHub Docs | GitHub | https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source | 页面未抓到显式时间 | English | open source, contribution, collaboration | 官方 | 补充阅读 | 文档面向 GitHub 用户解释如何找到项目、理解贡献方式、开始参与开源。它不是专门的 PR 教程，但能帮助初学者建立“协作=参与项目”的整体视角。 | 适合在“为什么要学 GitHub 协作”部分使用。 | 更偏心智建立，不是具体命令教程。 |

### 小结

- 主参考优先级：`GH-COL-01` → `GH-COL-02` → `GH-COL-03`
- 第 3 周正文可直接写入的章节候选：
  - 认识 GitHub 协作：共享仓库 vs Fork
  - Pull Request 页面怎么读
  - 怎样提交一个容易 review 的 PR
  - 用 Issues 和 Projects 管住任务流转

---

## 2. 分支 / PR

### 主题知识点

- 分支的作用：隔离改动、并行开发、降低主分支风险
- 常见工作流：feature branch、GitHub Flow
- 分支命名与提交粒度
- PR 与 merge/rebase 的区别及教学边界
- 冲突与 review 的最小处理方法

### 推荐讲解顺序

1. 先讲“为什么开分支”
2. 再讲 feature branch workflow
3. 然后讲 PR 流程与 review
4. 最后点到 merge / rebase 的概念差异，不要求初学者在第 3 周深挖历史整理

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/更新时间 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BR-PR-01 | Git - Branching Workflows | Pro Git Book / git-scm.com | Scott Chacon, Ben Straub / Git 社区 | https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows | 页面展示为长期维护书籍，抓取结果未含具体时间 | English | git, branching, workflow | 官方 | 入门必读 | Pro Git 书中系统解释长期分支、主题分支等工作流思路。它不是 GitHub 专属文档，但能帮助学习者理解分支设计背后的原因。 | Git 官方生态中的经典材料，适合支撑“为什么需要分支”。 | 第 3 周可只取主题分支思想，不展开复杂发布分支。 |
| BR-PR-02 | Git Feature Branch Workflow | Atlassian Git Tutorials | Atlassian | https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow | 页面抓取未包含显式时间 | English | feature branch, workflow, collaboration | 半官方 | 入门必读 | 文档聚焦 feature branch workflow：所有功能在专用分支开发，再通过 pull request 合并。对初学者建立“每个任务一个分支”非常直观。 | 教学表达友好，适合与 GitHub Docs 交叉验证。 | Atlassian 属实践教程，不是 GitHub 官方，但可读性强。 |
| BR-PR-03 | About pull requests | GitHub Docs | GitHub | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests | 页面未抓到显式时间 | English | PR, merge, checks | 官方 | 入门必读 | 该文档对 PR 结构、讨论、自动检查、合并前把关有直接定义。适合和 feature branch workflow 一起讲，形成“分支 → PR → 合并”的闭环。 | 可直接对应实践任务：新建分支、提交 PR、观察 Checks。 | 与 GH-COL-02 重合，但在此主题仍需保留作为主参考。 |
| BR-PR-04 | Helping others review your changes | GitHub Docs | GitHub | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes | 页面未抓到显式时间 | English | PR review, reviewability | 官方 | 进阶参考 | 文档强调小 PR、清晰上下文、分步说明、减少 reviewer 负担。可作为“如何让 review 更顺滑”的协作规范补充。 | 适合把“技术流程”延伸到“工程沟通质量”。 | 与 BR-PR-03 配套。 |
| BR-PR-05 | Contributing to Open Source（Quick Tip for Beginners） | Open Source Guides | GitHub | https://opensource.guide/how-to-contribute/ | 页面未抓到显式时间 | 多语言，含中文入口 | branching, commits, PR habits | 半官方 | 补充阅读 | 指南中给出适合新手的协作建议，包括创建新分支、写清楚提交信息、在提交 PR 前先本地验证。比纯工具文档更像“贡献者行为准则”。 | 非常适合做新手习惯养成补充。 | GitHub 维护的开放指南，可信度较高。 |

### 小结

- 主参考优先级：`BR-PR-02` → `BR-PR-03` → `BR-PR-01`
- 第 3 周正文可直接写入的章节候选：
  - 为什么要用功能分支
  - 从一个小任务走完整个 PR 流程
  - merge 和 rebase 先知道什么，不急着全会
  - 写小 PR，比写大 PR 更重要

---

## 3. 项目阅读

### 主题知识点

- 读项目先看 README、文档站、安装方式、运行方式
- 再看 CONTRIBUTING、Issue、Pull Request、Roadmap，理解项目怎么协作
- 通过目录结构定位入口文件、配置文件、脚本与测试
- 用真实仓库做案例，比抽象讲方法更有效
- 先求“能跑起来 + 看懂主干”，再逐步下钻实现细节

### 推荐讲解顺序

1. 先讲项目阅读的总路径：README → 运行 → 目录 → issue/PR
2. 再讲如何通过 CONTRIBUTING 和项目规则理解协作方式
3. 最后用真实仓库做演示：VS Code 或 Flask

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/更新时间 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PROJ-READ-01 | Contributing to open source | GitHub Docs | GitHub | https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source | 页面未抓到显式时间 | English | open source, reading projects, contribution | 官方 | 入门必读 | 该指南从“如何找到项目、如何开始贡献”的角度，天然包含阅读项目时应关注的入口：文档、任务、协作方式。对初学者很友好。 | 适合把“读项目”与“参与项目”连接起来。 | 偏通识，但适合第 3 周初学者。 |
| PROJ-READ-02 | How to Contribute to Open Source | Open Source Guides | GitHub | https://opensource.guide/how-to-contribute/ | 页面未抓到显式时间 | 多语言，含中文入口 | project orientation, README, contributing | 半官方 | 入门必读 | 文档专门有“Orienting yourself to a new project”部分，强调先理解项目为什么存在、问题在哪、贡献流程是什么。非常适合作为“怎样快速读懂一个仓库”的方法论材料。 | 结构化强，适合转写为阅读 checklist。 | 与 GitHub Docs 互补。 |
| PROJ-READ-03 | Visual Studio Code README | GitHub 仓库原始文档 | Microsoft | https://raw.githubusercontent.com/microsoft/vscode/main/README.md | 仓库当前 main 分支内容；抓取时未记录 commit SHA | English | README, real project, repository orientation | 官方 | 进阶参考 | VS Code README 展示了一个大型开源项目如何用 README 说明仓库定位、路线图、贡献入口、文档位置。适合作为“大仓库怎么从 README 获取全局图”的案例。 | 真实度高，能演示从 README 提取项目信息。 | 可提醒学员：大型项目不要一上来就啃源码。 |
| PROJ-READ-04 | Visual Studio Code CONTRIBUTING | GitHub 仓库原始文档 | Microsoft | https://raw.githubusercontent.com/microsoft/vscode/main/CONTRIBUTING.md | 仓库当前 main 分支内容；抓取时未记录 commit SHA | English | CONTRIBUTING, issue triage, project workflow | 官方 | 进阶参考 | 文档详细说明如何提问、反馈、报 issue、寻找已有 issue、定位仓库边界。适合说明“CONTRIBUTING 文件比源码更能快速告诉你项目怎么运作”。 | 是项目阅读中常被忽视但极高价值的入口。 | 适合作为教学中的“第二个必看文件”。 |
| PROJ-READ-05 | Flask README | GitHub 仓库原始文档 | Pallets | https://raw.githubusercontent.com/pallets/flask/main/README.md | 仓库当前 main 分支内容；抓取时未记录 commit SHA | English | small project, README, framework repo | 官方 | 补充阅读 | Flask README 是相对中小型项目案例，能展示与 VS Code 这种大型仓库不同的阅读方式：先看用途、示例、安装与文档，再看贡献入口。适合给初学者一个较低心理门槛的案例。 | 可与 VS Code 案例形成“大项目/中项目”对照。 | 若课程时间有限，可二选一。 |

### 项目阅读方法清单

1. 先看 README：项目是什么、解决什么问题、怎么运行
2. 再看 CONTRIBUTING：团队如何收 issue、怎么提 PR、风格要求是什么
3. 看仓库根目录：`src/`、`docs/`、`tests/`、配置文件、脚本
4. 用 issue / PR 判断项目当前关注点
5. 先跑通一个最小示例，再回来看核心模块

### 小结

- 主参考优先级：`PROJ-READ-02` → `PROJ-READ-03` → `PROJ-READ-04`
- 第 3 周正文可直接写入的章节候选：
  - 第一次读开源项目，先看什么
  - README 和 CONTRIBUTING 是两个最高回报入口
  - 用 VS Code / Flask 演示项目阅读路径

---

## 4. 基础工程实践

### 主题知识点

- 格式化与 Lint：为什么要让代码风格自动化
- 日志：为什么别只靠 `print`
- 本地验证：提交前至少能跑、能看日志、能自检
- 文档与贡献规范：README / CONTRIBUTING / issue 模板的作用
- 初学者最小工程习惯：可运行、可读、可复现、可 review

### 推荐讲解顺序

1. 先讲“工程实践不是大厂流程，而是降低出错成本”
2. 再讲 formatter / linter 的最小配合
3. 然后讲 logging 与调试思维
4. 最后回到文档与提交流程

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/更新时间 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ENG-PRAC-01 | What is Prettier? | Prettier Docs | Prettier 团队 | https://prettier.io/docs/ | 页面抓取为文档站当前 stable 版本 | English | formatter, style, consistency | 官方 | 入门必读 | Prettier 官方文档解释它是“有明确风格立场的代码格式化工具”，目标是让代码风格一致、减少格式争论。非常适合给新手建立“格式交给工具”的观念。 | 概念清楚，门槛低，适合作为 formatter 的唯一主资料。 | 更偏 JavaScript 生态，但理念通用。 |
| ENG-PRAC-02 | Getting Started with ESLint | ESLint Docs | ESLint 团队 | https://eslint.org/docs/latest/use/getting-started | 页面抓取为 v10/v9 文档导航页 | English | linter, code quality, rules | 官方 | 入门必读 | ESLint 官方入门页展示如何把 lint 接入项目，强调它是可插拔的 JavaScript Linter。适合解释 formatter 与 linter 的分工不同：一个统一格式，一个发现潜在问题。 | 能直接支撑“格式化 ≠ 静态检查”的核心知识点。 | 课程中只讲理念与最小使用即可。 |
| ENG-PRAC-03 | Logging HOWTO | Python Docs | Python Software Foundation / Vinay Sajip | https://docs.python.org/3/howto/logging.html | 抓取页面为 Python 3.14.3 文档 | English | logging, debugging, observability | 官方 | 入门必读 | Python 官方文档从“什么时候用 logging”切入，直接对比 `print()`、`warnings.warn()`、异常与 logger 的使用场景。对初学者理解“日志是排错基础设施”很有帮助。 | 内容结构极适合转成中文教程中的“什么时候该打日志”。 | 尽管是 Python 文档，但原则通用。 |
| ENG-PRAC-04 | Open Source Guides CONTRIBUTING | GitHub 仓库原始文档 | GitHub | https://raw.githubusercontent.com/github/opensource.guide/main/CONTRIBUTING.md | 仓库当前 main 分支内容；抓取时未记录 commit SHA | English | contributing, commit message, test locally | 半官方 | 进阶参考 | 文档给了很适合新手的 quick tips：新分支、清晰 commit message、本地测试、遵循 style guide。虽然面向该项目自身，但这些规则本身就是基础工程实践。 | 非常适合做“提交前自查清单”的参考。 | 可与 GitHub PR 规范合并讲。 |
| ENG-PRAC-05 | Visual Studio Code CONTRIBUTING | GitHub 仓库原始文档 | Microsoft | https://raw.githubusercontent.com/microsoft/vscode/main/CONTRIBUTING.md | 仓库当前 main 分支内容；抓取时未记录 commit SHA | English | issue reporting, workflow, reproducibility | 官方 | 补充阅读 | VS Code 的贡献文档强调复现问题、先搜已有 issue、准确描述环境与问题。对“写 issue / 写 bug 报告也是工程实践”这一点有很强示范意义。 | 可让学员看到成熟项目如何要求信息完整性。 | 更适合补充，不是入门唯一主资料。 |

### 基础工程实践最小清单

- 提交前至少运行一次最小验证
- 用 formatter 保持风格一致
- 用 linter 找出明显问题
- 用 logging 记录关键过程和异常线索
- README 说明如何运行；必要时补充 CONTRIBUTING
- commit message 与 PR 描述要能让别人接手

### 小结

- 主参考优先级：`ENG-PRAC-01` → `ENG-PRAC-02` → `ENG-PRAC-03`
- 第 3 周正文可直接写入的章节候选：
  - 为什么要把代码风格交给工具
  - formatter、linter、logging 各管什么
  - 提交前自检，是最小工程习惯

---

## 5. Cursor 入门

### 主题知识点

- Cursor 的统一 AI 界面：Ask / Edit / Agent
- Agent 模式可以读写代码、搜索仓库、运行终端、网页搜索
- 上下文机制：@ 符号、自动上下文、代码库索引
- 规则系统：项目规则 `.cursor/rules` 与全局规则
- Yolo 模式、终端防护栏、工具调用上限等注意事项

### 推荐讲解顺序

1. 先讲 Cursor 是“编辑器里的 AI 工作台”，不是单一聊天框
2. 再讲 Chat/Ask/Edit/Agent 的区别
3. 然后讲规则、上下文和代码库索引
4. 最后讲 Yolo 模式与安全边界

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/更新时间 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CUR-01 | Cursor Docs | Cursor 官方文档 | Cursor | https://cursor.com/docs | 文档首页；抓取结果仅返回标题 | English | cursor, docs, entrypoint | 官方 | 入门必读 | 官方文档入口页，适合作为资料索引总入口。虽然抓取文本较少，但可作为后续跳转到 Agent、Chat、Rules 等具体页面的稳定来源。 | 作为总索引必须保留。 | 正文引用时更建议链接到子页面。 |
| CUR-02 | Chat 概述 | Cursor 文档 | Cursor | https://docs.cursor.ac.cn/chat/overview | 页面未抓到显式时间 | 中文 | cursor, chat, ask, edit, agent | 官方 | 入门必读 | 中文文档清楚解释 Cursor 的统一 AI 界面，区分 Ask、Edit、Agent 三种模式，并说明自动上下文、应用更改、检查点、lint 迭代等能力。适合给零基础用户建立操作全景图。 | 中文可读性强，教学友好度高。 | 页面提到长对话会被模型摘要，说明上下文有限。 |
| CUR-03 | Agent | Cursor 文档 | Cursor | https://docs.cursor.ac.cn/chat/agent | 页面未抓到显式时间 | 中文 | agent, tools, terminal, yolo | 官方 | 入门必读 | 文档说明 Agent 可读写代码、搜索代码库、调用 MCP、运行终端、自动网页搜索，并说明 25 次工具调用上限、终端配置文件选择、Yolo 模式与命令防护栏。适合讲“Agent 能做什么、不能盲放什么权限”。 | 直接支撑“Cursor Agent 入门与风险”章节。 | 强时效内容，正文应提示版本变化。 |
| CUR-04 | AI 规则 | Cursor 文档 | Cursor | https://docs.cursor.ac.cn/context/rules-for-ai | 页面未抓到显式时间 | 中文 | rules, .cursor/rules, global rules | 官方 | 入门必读 | 文档系统解释项目规则与全局规则的区别，明确推荐把项目规则放在 `.cursor/rules` 中并通过 glob 与语义描述自动附加。非常适合讲“如何让 AI 按团队约定工作”。 | 是把 Cursor 从“会聊天”升级到“能协作”的关键资料。 | 需提醒 `.cursorrules` 为兼容方案，官方建议迁移。 |
| CUR-05 | Chat 概述中的 迭代 lint / 自动上下文 说明 | Cursor 文档 | Cursor | https://docs.cursor.ac.cn/chat/overview | 页面未抓到显式时间 | 中文 | lint, context, workflow | 官方 | 补充阅读 | 同一页面中关于自动上下文、检查点、lint 迭代的说明，能帮助初学者理解为什么 Cursor 适合做“小步迭代 + 看 diff + 回滚”。 | 很适合转成“先让 AI 改，再看 diff 再决定”的工作流建议。 | 与 CUR-02 同页，可在正文中合并引用。 |

### 小结

- 主参考优先级：`CUR-02` → `CUR-03` → `CUR-04`
- 第 3 周正文可直接写入的章节候选：
  - Ask、Edit、Agent 有什么区别
  - Cursor Agent 能帮你做哪些事
  - 用 `.cursor/rules` 管住 AI 输出
  - 为什么先看 diff，再点接受

---

## 6. AI 编程工作流入门

### 主题知识点

- 先拆任务，再让 AI 动手；不要把模糊大需求一次性扔给模型
- 明确上下文、限制、输出格式和验证方式
- 先让 AI 产出小改动，再通过 diff / lint / test / 人审复核
- 规则、检查点、日志、PR 描述都是 AI 协作的一部分
- 把 AI 当副驾，不是无监督自动驾驶

### 推荐讲解顺序

1. 从“AI 不是魔法，会受上下文和指令约束”讲起
2. 再讲一个最小闭环：明确任务 → 给上下文 → 生成改动 → 运行校验 → 人工 review
3. 然后结合 Cursor 的规则、检查点、lint 迭代能力
4. 最后补充 prompt 设计和风险提示

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/更新时间 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AIWF-01 | Prompt engineering | OpenAI Platform Docs | OpenAI | https://platform.openai.com/docs/guides/prompt-engineering | 抓取失败：403，但 `web_search` 返回官方文档入口 | English | prompt engineering, constraints, examples | 官方 | 入门必读 | 虽然页面抓取受限，但官方文档入口可确认该主题存在且属于 OpenAI 官方指南。用于支撑“提示词需要给清晰目标、上下文、约束与示例”的原则性引用。 | 适合做 AI 编程工作流中的提示词原则来源。 | 因 403 无法摘录正文，课程中应只引用为官方进一步阅读入口。 |
| AIWF-02 | Prompt engineering best practices 2025 PDF | OpenAI Platform | OpenAI | https://platform.openai.com/assets/prompt-engineering-best-practices-2025.pdf | 抓取失败：403，但 `web_search` 返回该 PDF 链接 | English | prompting, best practices | 官方 | 进阶参考 | 搜索结果显示 OpenAI 提供 prompt engineering best practices PDF。虽然当前会话无法直接读取 PDF 内容，但可作为后续人工补充下载与核对的入口。 | 为后续扩展保留高价值官方线索。 | 需要下一轮用可下载方式核验正文。 |
| AIWF-03 | Chat 概述 | Cursor 文档 | Cursor | https://docs.cursor.ac.cn/chat/overview | 页面未抓到显式时间 | 中文 | AI workflow, context, diff, checkpoints | 官方 | 入门必读 | 该文档说明 Cursor 支持自动上下文、检查点、应用更改、lint 迭代，本质上就是“AI 生成 → 看变更 → 回滚/接受 → 再修”的 IDE 工作流。非常适合把抽象 AI 编程流程落到具体工具上。 | 比抽象 prompt 教程更贴近实际操作。 | 可与 AIWF-04 组合。 |
| AIWF-04 | Agent | Cursor 文档 | Cursor | https://docs.cursor.ac.cn/chat/agent | 页面未抓到显式时间 | 中文 | AI coding agent, terminal, guardrails | 官方 | 入门必读 | 文档说明 Agent 有工具调用能力，但也有调用上限、终端配置、Yolo 模式和防护栏等边界。适合告诉学员：AI 能自动做很多事，但必须设置验证与权限边界。 | 能把“AI 协助”与“安全边界”同时讲清楚。 | 是 AI 工具风险教育的重要来源。 |
| AIWF-05 | AI 规则 | Cursor 文档 | Cursor | https://docs.cursor.ac.cn/context/rules-for-ai | 页面未抓到显式时间 | 中文 | rules, system guidance, repeatability | 官方 | 进阶参考 | 规则系统本质上是在把团队约定、代码风格、架构偏好前置为系统提示。适合说明“让 AI 稳定输出，关键不是多问，而是事先写规则”。 | 对团队协作和长期复用价值高。 | 与 `.cursor/rules` 实操非常贴合。 |

### AI 编程工作流最小闭环

1. 写清楚任务：目标、边界、输入输出
2. 提供上下文：相关文件、目录、约束、风格
3. 让 AI 先做小步改动
4. 看 diff，不盲信结果
5. 跑 lint / test / 最小手工验证
6. 用 PR 描述记录为什么改
7. 发现高风险任务时改为人工主导

### 小结

- 主参考优先级：`AIWF-03` → `AIWF-04` → `AIWF-01`
- 第 3 周正文可直接写入的章节候选：
  - AI 编程最小闭环：说清楚、看 diff、做验证
  - 什么时候该让 Agent 自动跑，什么时候不该
  - 规则文件比“灵光一闪的 prompt”更稳定

---

## 7. 初筛与去重结论

### 优先保留

- GitHub Docs：协作模型、PR、review、Projects
- Git 官方 / Pro Git：分支工作流原理
- Cursor 官方文档：Chat、Agent、Rules
- Python / Prettier / ESLint 官方文档：基础工程实践
- 真实开源仓库 README / CONTRIBUTING：项目阅读案例

### 降级为补充阅读

- Open Source Guides：方法论与新手习惯很好，但不替代官方工具文档
- 大型仓库 README/CONTRIBUTING：适合案例演示，不必全部逐字读

### 当前缺口

- 缺少高质量、可直接引用的中文 GitHub Projects 教程；当前以 GitHub Docs 英文版为主
- OpenAI 官方 prompt engineering 正文因 403 未成功抓取，后续若要大篇幅引用需补做下载或人工核验
- 暂未补充视频类资料；当前以文档型资料为主，更利于准确引用，但若最终教程需要“视频辅助”，需补采 B 站或 YouTube 官方演讲

---

## 8. 面向第 3 周教程的骨架映射

### 建议的 7 天安排

| 天数 | 学习主题 | 核心目标 | 主要资料 |
|---|---|---|---|
| Day 15 | GitHub 协作全景 | 理解 issue、PR、fork、shared repo 的关系 | GH-COL-01, GH-COL-02 |
| Day 16 | 分支与 PR 实操 | 学会 feature branch → commit → PR 的闭环 | BR-PR-02, BR-PR-03, BR-PR-04 |
| Day 17 | 如何阅读一个开源项目 | 学会 README → CONTRIBUTING → 目录 → issue/PR 的阅读路径 | PROJ-READ-02, PROJ-READ-03, PROJ-READ-04 |
| Day 18 | 基础工程实践 1 | 理解 formatter / linter 的作用与分工 | ENG-PRAC-01, ENG-PRAC-02 |
| Day 19 | 基础工程实践 2 | 理解 logging、最小验证、提交流程 | ENG-PRAC-03, ENG-PRAC-04 |
| Day 20 | Cursor 入门 | 会区分 Ask/Edit/Agent，会用上下文与规则 | CUR-02, CUR-03, CUR-04 |
| Day 21 | AI 编程工作流入门 + 周复盘 | 形成“拆任务 → 生成 → 看 diff → 验证”的闭环 | AIWF-03, AIWF-04, AIWF-01 |

### 章节候选标题

1. GitHub 协作不是“上传代码”，而是围绕 PR 协同工作
2. 每个任务一个分支：最小 Feature Branch 工作流
3. 第一次读开源项目：先看 README，再看 CONTRIBUTING
4. 基础工程实践：格式化、Lint、日志、最小验证
5. Cursor 入门：Ask、Edit、Agent 三种模式怎么配合
6. AI 编程工作流：先说清楚，再看 diff，最后做验证

### 练习建议

- 练习 1：基于一个 toy repo 提一个只改 README 的小 PR
- 练习 2：为一个 issue 新建分支并提交最小改动
- 练习 3：阅读一个开源仓库，写出“我先看了哪些文件、为什么”
- 练习 4：给一个小项目接入 formatter / linter，并写一段日志
- 练习 5：在 Cursor 中写一条规则，让 Agent 生成符合项目约定的改动

---

## 9. 可信度与使用建议总评

- **官方优先**：GitHub Docs、Git/Pro Git、Cursor Docs、Python Docs、Prettier Docs、ESLint Docs
- **半官方/高可信补充**：Open Source Guides、Atlassian Git Tutorials
- **社区经验暂未大量引入**：本轮优先保证稳定、可追溯、便于团队复核
- **高时效风险主题**：Cursor、Agent、AI prompt engineering
  - 使用建议：正文中标注“界面和能力可能迭代，请以当前官方文档为准”
  - 使用建议：避免把工具调用次数、支持模型列表等写成长期不变事实

## 10. 来源记录（按本次调研实际使用）

- GitHub Docs: https://docs.github.com/
- Git / Pro Git: https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows
- Atlassian Git Tutorial: https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow
- Open Source Guides: https://opensource.guide/how-to-contribute/
- VS Code README: https://raw.githubusercontent.com/microsoft/vscode/main/README.md
- VS Code CONTRIBUTING: https://raw.githubusercontent.com/microsoft/vscode/main/CONTRIBUTING.md
- Flask README: https://raw.githubusercontent.com/pallets/flask/main/README.md
- Open Source Guides CONTRIBUTING: https://raw.githubusercontent.com/github/opensource.guide/main/CONTRIBUTING.md
- Python Logging HOWTO: https://docs.python.org/3/howto/logging.html
- Prettier Docs: https://prettier.io/docs/
- ESLint Docs: https://eslint.org/docs/latest/use/getting-started
- Cursor Docs: https://cursor.com/docs
- Cursor Chat 概述: https://docs.cursor.ac.cn/chat/overview
- Cursor Agent: https://docs.cursor.ac.cn/chat/agent
- Cursor AI 规则: https://docs.cursor.ac.cn/context/rules-for-ai
- OpenAI Prompt Engineering: https://platform.openai.com/docs/guides/prompt-engineering
- OpenAI Prompt Engineering PDF: https://platform.openai.com/assets/prompt-engineering-best-practices-2025.pdf
