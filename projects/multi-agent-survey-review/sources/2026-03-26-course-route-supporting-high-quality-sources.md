# 2026-03-26 可支撑 28 天课程路线的高质量资料与综述来源清单

- 任务：检索并收集可支撑该课程路线的高质量资料与综述来源，优先整理可追溯链接、标题、摘要与适用章节
- 适用课程：`projects/zero-basics-plan/analysis/2026-03-26-28-day-course-outline.md`
- 边界依据：`projects/multi-agent-survey-review/analysis/2026-03-26-zero-basics-plan-survey-scope-for-28-day-route.md`
- 生成时间：2026-03-26

## 1. 检索范围与筛选口径

### 1.1 课程章节映射口径
本清单按 28 天课程主线分组：
1. 导学与零基础边界
2. 环境搭建、Remote SSH、Linux 基础
3. Git / GitHub 协作与项目阅读
4. AI 编程工作流与 Agent 工具入门
5. 深度学习基础、训练与推理
6. 课程后延伸：multi-agent / agent framework 综述

### 1.2 检索来源
- 仓库内既有调研：
  - `projects/zero-basics-plan/analysis/2026-03-26-week1-resource-survey-zero-basics-env-vscode-remote-ssh-linux.md`
  - `projects/zero-basics-plan/analysis/2026-03-26-week2-linux-ssh-git-resource-survey.md`
  - `projects/zero-basics-plan/analysis/2026-03-26-week3-github-collaboration-cursor-ai-workflow-research.md`
  - `projects/zero-basics-plan/analysis/2026-03-26-week4-vibe-coding-ai-assisted-development-deep-learning-training-inference-capstone-research.md`
  - `projects/multi-agent-survey-review/analysis/2026-03-26-final-chinese-multi-agent-survey-report.md`
  - `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`
- 本次追加联网核验：
  - `https://link.springer.com/article/10.1007/s44336-024-00009-2`
  - `https://arxiv.org/abs/2402.01680`
  - `https://arxiv.org/abs/2412.17481`
  - `https://arxiv.org/abs/2501.06322`
  - `https://arxiv.org/abs/2502.14321`
  - `https://arxiv.org/abs/2502.16804`
  - `https://arxiv.org/abs/2503.13415`
  - `https://arxiv.org/abs/2505.21116`
  - `https://arxiv.org/abs/2602.11583`
  - `https://microsoft.github.io/autogen/dev/`
  - `https://docs.langchain.com/oss/python/langgraph/overview`
  - `https://docs.crewai.com/`

### 1.3 纳入标准
- 可追溯到官方文档、出版社页、arXiv、GitHub Docs、框架官方文档或高质量长期维护教程。
- 与 28 天课程某个章节直接相关，或可作为后续进阶延伸。
- 摘要能明确说明“这条资料对课程有什么用”。
- 按 `核心 / 重要 / 补充` 分级。

### 1.4 排除与去重原则
- 不纳入无法稳定抓取正文且无法二次核验来源的低可信转载页。
- 对同主题重复内容，优先保留官方文档，其次保留教学友好的中文补充。
- multi-agent 综述仅保留与“AI 工作流延伸 / 后续进阶路线”直接相关者，不强行塞入 28 天主线。

---

## 2. 资料总览索引

| 分组 | 目标 | 数量 | 备注 |
|---|---|---:|---|
| A 导学与零基础边界 | 明确适用对象、学习目标、学习方式 | 3 | 优先课程首页、导学页 |
| B 环境搭建 / SSH / Linux | 支撑第 1–2 周环境与命令行主线 | 7 | 官方文档 + 高可执行教程为主 |
| C Git / GitHub 协作 | 支撑第 2–3 周版本管理与协作 | 6 | GitHub Docs + Pro Git 为主 |
| D AI 编程工作流 | 支撑第 3–4 周 Cursor / Agent / AI coding | 7 | Cursor / Claude Code / 工程实践 |
| E 深度学习基础与训练推理 | 支撑第 4 周概念与最小实验 | 6 | Google / PyTorch / Hugging Face 为主 |
| F 进阶延伸：multi-agent / frameworks | 支撑结课后延伸阅读或附录 | 8 | 明确标注为延伸，不直接并入主线 |

---

## 3. A 导学与零基础边界

| 优先级 | 标题 | 作者/机构 | 年份 | 来源类型 | 原始链接 | 摘要 | 适用章节 | 入选理由 | 证据来源 |
|---|---|---|---:|---|---|---|---|---|---|
| 核心 | 编程学习全指南：从零基础到职业发展的实用路径 | 腾讯云开发者 / qife122 | 2025 | 长文教程 | https://developer.cloud.tencent.com/article/2571989 | 文章不是教某个单点工具，而是先解释零基础学习编程的路径、资料使用方式与实践节奏，适合给课程首页补“为什么先环境、后工具、再项目”的方法论说明。 | 导学；Day 1；课程首页“如何使用本路线” | 可直接支撑学习路径说明，且对零基础焦虑有缓冲作用。 | `projects/zero-basics-plan/analysis/2026-03-26-week1-resource-survey-zero-basics-env-vscode-remote-ssh-linux.md` |
| 核心 | 计算机学习路线大全（2025版） | 编程指北 | 2025 | 路线图 / 导航页 | https://csguide.cn/roadmap/ | 以路线图方式呈现基础计算机学习方向，适合在课程首页说明“本 28 天路线只覆盖环境、Linux、Git、AI 工作流、DL 入门，不覆盖更广泛 CS 主体”。 | 导学；课程首页“范围与边界” | 可帮助学习者理解课程主线与未覆盖内容，减少目标漂移。 | `projects/zero-basics-plan/analysis/2026-03-26-week1-resource-survey-zero-basics-env-vscode-remote-ssh-linux.md` |
| 重要 | 机器学习速成课程 | Google for Developers | 2026 访问版 | 官方课程入口 | https://developers.google.cn/machine-learning/crash-course?hl=zh-cn | 虽主要面向机器学习，但课程目录结构非常适合作为“第 4 周只是深度学习最小入门，不是完整机器学习课程”的边界说明，也可用于结课后的下一阶段路线建议。 | 导学；第 4 周前言；后续 30 天路线 | 官方中文课程，适合做“课程后怎么继续学”的出口。 | `projects/zero-basics-plan/analysis/2026-03-26-week4-vibe-coding-ai-assisted-development-deep-learning-training-inference-capstone-research.md` |

### A 组结论
- 最适合直接并入课程首页的是“学习路径解释 + 路线边界说明”。
- 本组资料应放在导学区，而不是分散插入每一天正文。

---

## 4. B 环境搭建、Remote SSH、Linux 基础

| 优先级 | 标题 | 作者/机构 | 年份 | 来源类型 | 原始链接 | 摘要 | 适用章节 | 入选理由 | 证据来源 |
|---|---|---|---:|---|---|---|---|---|---|
| 核心 | 使用 SSH 进行远程开发 | Microsoft / VS Code 文档 | 持续维护 | 官方文档 | https://vscode.js.cn/docs/remote/ssh | 官方解释 Remote SSH 的工作模型、前提条件与连接方式，最适合作为 Day 2–3 的权威主资料。它直接说明“本地 VS Code + 远程主机”这条关系。 | Day 2–3；系统课 1 | 官方、稳定、与课程目标完全一致。 | `projects/zero-basics-plan/analysis/2026-03-26-week1-resource-survey-zero-basics-env-vscode-remote-ssh-linux.md` |
| 核心 | Remote development over SSH | Microsoft / VS Code Docs | 持续维护 | 官方文档 | https://code.visualstudio.com/docs/remote/ssh-tutorial | 英文原始教程可作为中文页的对照来源，适合用于课程编写者核验术语、连接步骤与扩展行为。 | Day 2–3；编写时术语核验 | 适合做官方双语校验，避免二手教程表述漂移。 | 同上 |
| 核心 | SSH Essentials: Working with SSH Servers, Clients, and Keys | DigitalOcean | 持续维护 | 教程 | https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys | 该文对 SSH 登录、密钥、客户端与服务器关系讲得清楚，特别适合补 Day 3–4 的“为什么要生成 key、什么是 known_hosts、为什么第一次连接会提示 host key”。 | Day 3；Day 10；系统课 2 | 对零基础用户非常实操，比 man page 更易上手。 | 同上 |
| 核心 | 小白零基础教程：安装 Conda + VSCode 配置 Python 开发环境 | Zeeklog / Ne0inhk | 2026 | 中文教程 | https://zeeklog.com/xiao-bai-ling-ji-chu-jiao-cheng-an-zhuang-conda-vscode-pei-zhi-python-kai-fa-huan-jing-9/ | 详细覆盖 Miniconda、环境创建、VS Code 解释器配置与常见问题，适合 Day 1–2 的 Python / VS Code 环境准备。 | Day 1–2 | 新、细、面向小白，补足官方文档在中文教学友好度上的不足。 | 同上 |
| 核心 | The Linux command line for beginners | Ubuntu Tutorials | 持续维护 | 官方教程 | https://ubuntu.com/tutorials/command-line-for-beginners | 按新手视角介绍命令行、文件与目录操作，是第 1 周命令行起步的理想主资料。 | Day 3–6 | 官方教程、难度适中、与命令行入门高度匹配。 | `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-outline.md` |
| 重要 | Linux Journey | Linux Journey | 持续维护 | 长期维护教程 | https://linuxjourney.com/ | 站点将 Linux 基础拆成清晰模块，适合为 Day 3–6 及 Day 8–12 提供更细的词条式补充，如权限、进程、文件系统。 | Day 3–6；Day 8–12 | 适合作为“查漏补缺”型资源。 | `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-outline.md` |
| 重要 | 新手一周入门 Linux，看这篇就够了！ | 博客园 / JChe | 2025 线索 | 中文教程 | https://www.cnblogs.com/jche/p/18900912/study_linux | 文章按 7 天组织 Linux 入门内容，适合作为中文练习路径参考，特别适合把命令行学习转成每天可完成的小目标。 | Day 3–7 | 教学编排友好，可被改写为“每日练习 / 复盘模板”。 | `projects/zero-basics-plan/analysis/2026-03-26-week1-resource-survey-zero-basics-env-vscode-remote-ssh-linux.md` |

### B 组结论
- 主线应采用“官方文档 + 1 篇中文小白教程 + 1 个长期维护教程”的组合。
- Remote SSH 与 Linux 命令不能只靠社区文，必须保留官方链接做溯源。

---

## 5. C Git / GitHub 协作与项目阅读

| 优先级 | 标题 | 作者/机构 | 年份 | 来源类型 | 原始链接 | 摘要 | 适用章节 | 入选理由 | 证据来源 |
|---|---|---|---:|---|---|---|---|---|---|
| 核心 | Pro Git 中文版（第二版） | Scott Chacon, Ben Straub / Git 社区 | 持续维护 | 官方书籍 | https://git-scm.com/book/zh/v2 | Git 最系统的官方材料，适合作为第 2 周 Git 基础、分支、远程仓库、协作的主参考。 | Day 11–16；系统课 2–3 | 体系完整，能从“Git 是什么”一直讲到 branch / merge。 | `projects/zero-basics-plan/analysis/2026-03-26-week2-linux-ssh-git-resource-survey.md` |
| 核心 | About Git | GitHub Docs | 持续维护 | 官方文档 | https://docs.github.com/en/get-started/using-git/about-git | 定义 Git 与 GitHub 的关系，适合给零基础学习者建立“本地版本控制 vs 远程协作平台”的基础概念。 | Day 11–13 | 概念边界清楚，适合作为 Day 11 开场。 | 同上 |
| 核心 | Hello World | GitHub Docs（中文） | 持续维护 | 官方文档 | https://docs.github.com/zh/get-started/start-your-journey/hello-world | 中文版一步步完成建仓、分支、提交、PR、合并，是 Day 15–16 最适合直接演示的材料。 | Day 15–16 | 中文、官方、实践闭环短。 | `projects/zero-basics-plan/analysis/2026-03-26-week3-github-collaboration-cursor-ai-workflow-research.md` |
| 核心 | 协作处理拉取请求 | GitHub Docs（中文） | 持续维护 | 官方文档 | https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests | 作为中文总入口，能帮助学员理解 PR、冲突、review、合并等协作环节。 | Day 15–16；系统课 3 | 适合做第 3 周 GitHub 协作总导航。 | 同上 |
| 重要 | About collaborative development models | GitHub Docs | 持续维护 | 官方文档 | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models | 解释 shared repository 与 fork-and-pull 两种协作模型，适合作为“为什么不是人人直接改主分支”的理论支撑。 | Day 15 | 协作模型定义清楚。 | 同上 |
| 重要 | Chinese README | Andy / 社区翻译实践 | 持续维护 | 社区规范文 | https://sunyctf.github.io/ChineseREADME/ | 用中文总结 README 常见结构，如背景、安装、用法、贡献方式，适合作为 Day 17 项目阅读与文档写作的检查表。 | Day 17；Day 27 README 编写 | 中文化程度高，能直接转写为“读 README / 写 README checklist”。 | 同上 |

### C 组结论
- Day 11–16 以 Pro Git + GitHub Docs 中文页为主；社区中文材料只做辅助解释。
- Day 17 的项目阅读材料不能只靠理论，建议配合真实仓库 README / CONTRIBUTING 做实操。

---

## 6. D AI 编程工作流与 Agent 工具入门

| 优先级 | 标题 | 作者/机构 | 年份 | 来源类型 | 原始链接 | 摘要 | 适用章节 | 入选理由 | 证据来源 |
|---|---|---|---:|---|---|---|---|---|---|
| 核心 | Chat 概述 | Cursor 中文文档 | 持续维护 | 官方文档 | https://docs.cursor.ac.cn/chat/overview | 说明 Ask / Edit / Agent 的统一界面、自动上下文、应用更改、检查点与 lint 迭代，是第 3 周 Cursor 入门的最佳入口。 | Day 18–21；Day 26 | 中文官方文档，最贴近课程实践。 | `projects/zero-basics-plan/analysis/2026-03-26-week3-github-collaboration-cursor-ai-workflow-research.md` |
| 核心 | Agent | Cursor 中文文档 | 持续维护 | 官方文档 | https://docs.cursor.ac.cn/chat/agent | 明确 Agent 的读写代码、运行终端、搜索代码库能力，以及工具调用上限、Yolo 模式、防护栏等风险点。 | Day 20–21；Day 26–27 | 可直接支撑“能做什么 / 不能盲信什么”教学。 | 同上；本次 `web_fetch` 复核 |
| 核心 | AI 规则 | Cursor 中文文档 | 持续维护 | 官方文档 | https://docs.cursor.ac.cn/context/rules-for-ai | 系统解释 `.cursor/rules` 与全局规则的区别，适合作为“如何把团队约定写给 AI”的主资料。 | Day 20–21；Day 26 | 对零基础学员理解“规则比临时 prompt 稳定”很关键。 | 同上 |
| 核心 | Common workflows | Claude Code Docs | 持续维护 | 官方文档 | https://code.claude.com/docs/en/common-workflows | 覆盖理解代码库、修 bug、重构、写测试、创建 PR 等常见任务流程，是 AI coding workflow 的高质量原始来源。 | Day 19–21；Day 27 | 非常适合改写成“AI 编程四步流程”。 | `projects/zero-basics-plan/analysis/2026-03-26-week4-vibe-coding-ai-assisted-development-deep-learning-training-inference-capstone-research.md` |
| 核心 | Best practices | Claude Code Docs | 持续维护 | 官方文档 | https://code.claude.com/docs/en/best-practices | 强调“先探索，再计划，再编码”“给 AI 验证路径”“主动管理上下文”，是课程中“AI 生成 ≠ 已验证”的最好护栏来源。 | Day 19–21；Day 26–27 | 可直接转成课程守则。 | 同上；本次 `web_fetch` 复核 |
| 重要 | What is Prettier? | Prettier Docs | 持续维护 | 官方文档 | https://prettier.io/docs/ | 解释格式化工具为何重要，适合支撑“AI 改完代码之后仍要有格式化与最小工程纪律”的章节。 | Day 18；Day 26 | 与 Cursor / Agent 结合后可构成最小工程闭环。 | `projects/zero-basics-plan/analysis/2026-03-26-week3-github-collaboration-cursor-ai-workflow-research.md` |
| 重要 | Logging HOWTO | Python Docs | Python Software Foundation | 2026 访问版 | 官方文档 | https://docs.python.org/3/howto/logging.html | 直接解释什么时候用 logging 而不是 print，适合支撑 Day 19 与 Day 26 的调试和复盘实践。 | Day 19；Day 26 | 工程实践价值高，可直接用在实验脚本与结课项目。 | 同上 |

### D 组结论
- 本组最重要的不是“会点按钮”，而是建立验证、规则、diff、回退这套工作流。
- 课程正文应把 Cursor / Claude Code 文档改写成中文 checklist，而不是直接堆文档链接。

---

## 7. E 深度学习基础、训练与推理

| 优先级 | 标题 | 作者/机构 | 年份 | 来源类型 | 原始链接 | 摘要 | 适用章节 | 入选理由 | 证据来源 |
|---|---|---|---:|---|---|---|---|---|---|
| 核心 | 机器学习速成课程 | Google for Developers | 2026 访问版 | 官方课程 | https://developers.google.cn/machine-learning/crash-course?hl=zh-cn | 课程中文化、模块化，适合作为“什么是模型、数据、神经网络、过拟合”的概念入口。 | Day 22；Day 24；结课后继续学习 | 适合作为概念总导航。 | `projects/zero-basics-plan/analysis/2026-03-26-week4-vibe-coding-ai-assisted-development-deep-learning-training-inference-capstone-research.md` |
| 核心 | PyTorch 深度学习：60 分钟闪电入门 | PyTorch 中文文档 | PyTorch | 2024 验证版 | 官方教程 | https://docs.pytorch.ac.cn/tutorials/beginner/deep_learning_60min_blitz.html | 覆盖张量、autograd、神经网络、训练分类器四步，是第 4 周最适合直接改写为课程实验的主资料。 | Day 23–25 | 既讲概念，又能跑通最小实验。 | 同上 |
| 核心 | Transformers 能做什么？ | Hugging Face 课程（中文） | Hugging Face | 2026 访问版 | 官方课程 | https://huggingface.co/docs/course/zh-CN/chapter1/3 | 用 `pipeline()` 直接做推理，最适合解释“推理是什么”和“如何快速做一个可展示的 AI demo”。 | Day 25–27；结课项目 | 零基础门槛低，演示效果好。 | 同上 |
| 核心 | 第 3 章本章简介 | Hugging Face 课程（中文） | Hugging Face | 2026 访问版 | 官方课程 | https://huggingface.co/docs/course/zh-CN/chapter3/1 | 明确给出微调训练的目标、数据集、Trainer API 与自定义训练流程，适合作为“训练是什么”的升级入口。 | Day 27；结课加分项 | 能把训练与推理区分开。 | 同上 |
| 重要 | TensorFlow 学习 | TensorFlow 中文官网 | Google / TensorFlow | 2026 访问版 | 官方文档入口 | https://tensorflow.google.cn/learn?hl=zh-cn | 从平台角度展示构建、微调、部署、推断的更宽视角，适合作为第 4 周课后延伸。 | Day 24–28；后续进阶 | 用于补“训练后还有部署与生产化”。 | 同上 |
| 补充 | Neural Networks | 3Blue1Brown | Grant Sanderson | 2026 访问版 | 高质量解释性内容 | https://www.3blue1brown.com/topics/neural-networks | 用可视化方式讲清神经网络、梯度下降和反向传播，适合补 Day 22–24 的概念直觉。 | Day 22–24；补充阅读 | 对数学直觉帮助大，但不应替代框架教程。 | 同上 |

### E 组结论
- 第 4 周最稳妥的路径是：Google MLCC 建概念 → PyTorch Blitz 跑最小实验 → Hugging Face pipeline 做展示型推理 demo。
- 训练与推理必须显式分开讲，避免学习者误以为“调用模型就是训练模型”。

---

## 8. F 进阶延伸：multi-agent / agent frameworks

> 本组不建议直接并入 28 天主线；适合放入结课后的“后续路线 / 延伸阅读 / 想做 Agent 系统可以看什么”。

| 优先级 | 标题 | 作者/机构 | 年份 | 来源类型 | 原始链接 | 摘要 | 适用章节 | 入选理由 | 证据来源 |
|---|---|---|---:|---|---|---|---|---|---|
| 核心 | A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | Li et al. / Springer | 2024 | 综述论文 | https://link.springer.com/article/10.1007/s44336-024-00009-2 | 以 profile、perception、self-action、mutual interaction、evolution 五段工作流组织 LLM-based MAS，是理解“多 agent 系统长什么样”的最佳总览之一。 | 结课后延伸；附录“Agent 系统总览” | 官方出版、框架清晰，适合作为进阶总入口。 | `projects/multi-agent-survey-review/analysis/2026-03-26-final-chinese-multi-agent-survey-report.md`；本次 `web_fetch` |
| 核心 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | Guo et al. | 2024 | arXiv 综述 | https://arxiv.org/abs/2402.01680 | 讨论 LLM-based multi-agent 的进展、通信、能力增长机制、benchmark 和挑战，适合从“系统能力与问题”角度继续深入。 | 结课后延伸 | 适合从单 Agent 过渡到多 Agent。 | 同上；本次 `web_fetch` |
| 核心 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | Tran et al. | 2025 | arXiv 综述 | https://arxiv.org/abs/2501.06322 | 用 actors、types、structures、strategies、protocols 组织协作机制，适合延伸理解“多 Agent 为什么不是多开几个模型”。 | 结课后延伸；协作机制专题 | taxonomy 清晰，进阶价值高。 | 同上；本次 `web_fetch` |
| 核心 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | Yan et al. | 2025 | arXiv 综述 | https://arxiv.org/abs/2502.14321 | 把 communication 作为多 Agent 系统核心变量，适合给完成第 3–4 周 AI 工作流的学习者展示下一层研究问题。 | 结课后延伸；通信专题 | 与协作机制和系统架构形成互补。 | 同上；本次 `web_fetch` |
| 重要 | Creativity in LLM-based Multi-Agent Systems: A Survey | Lin et al. | 2025 | arXiv 综述 | https://arxiv.org/abs/2505.21116 | 聚焦创意生成中的多 Agent 协作、persona design、生成技术与评测，适合作为“AI 创作型 Agent”方向延伸。 | 结课后延伸；创意方向 | 让课程后续路线不只停留在工程工具。 | 同上；本次 `web_fetch` |
| 重要 | The Five Ws of Multi-Agent Communication | Chen et al. | 2026 | arXiv / TMLR accepted | https://arxiv.org/abs/2602.11583 | 用 Who / Whom / When / What / Why 框架统一 MARL、涌现语言与 LLM 多 Agent 通信研究，是通信方向的高质量近期综述。 | 结课后延伸；研究导向 | 可作为更高层次的研究框架阅读。 | 同上；本次 `web_fetch` |
| 重要 | AutoGen | Microsoft | 2024–2026 文档版 | 官方框架文档 | https://microsoft.github.io/autogen/dev/ | 文档首页将 AutoGen 定义为构建单 Agent 与多 Agent 应用的框架，区分 AgentChat、Core、Studio，适合做“实际能用哪些框架搭 Agent 系统”的入口。 | 结课后延伸；框架选型 | 官方文档可追溯、工程导向强。 | 本次 `web_fetch` |
| 重要 | LangGraph overview | LangChain | 2026 文档版 | 官方框架文档 | https://docs.langchain.com/oss/python/langgraph/overview | 文档将 LangGraph 定位为低层 orchestration framework，强调 durable execution、human-in-the-loop、stateful agents，适合作为 agent orchestration 进阶入口。 | 结课后延伸；框架选型 | 与 AutoGen 形成互补：一个偏事件驱动核心，一个偏图式编排。 | 本次 `web_fetch` |
| 补充 | CrewAI Documentation | CrewAI | 2026 文档版 | 官方框架文档 | https://docs.crewai.com/ | 文档强调 agents、crews、flows、guardrails、memory、knowledge、observability，适合作为“多 Agent 流程化产品框架”的补充入口。 | 结课后延伸；框架选型 | 可用于展示业界多 Agent 框架的不同取向。 | 本次 `web_fetch` |

### F 组结论
- 这些资料质量高，但不应提前塞进零基础主线。
- 更合理的做法是在 Day 28 的“后续 30 天计划”里给出“如果想继续做 Agent / multi-agent，可从这组开始”。

---

## 9. 可直接并入课程路线的建议

| 课程位置 | 建议并入资料 | 状态 | 用法 |
|---|---|---|---|
| 课程首页 / 导学 | 腾讯云编程学习全指南、编程指北路线图 | 直接并入 | 作为“适用对象、路线边界、学习方法”阅读入口 |
| Day 1–2 | Zeeklog Conda + VS Code；VS Code Python 官方教程 | 直接并入 | 作为环境搭建主资料与备查资料 |
| Day 2–3 | VS Code Remote SSH 中文官方页、英文原页 | 直接并入 | 作为 Remote SSH 主线资料 |
| Day 3–6 | Ubuntu 命令行教程、Linux Journey | 直接并入 | 作为命令行入门与查漏补缺资料 |
| Day 11–16 | Pro Git 中文版、GitHub Docs 中文 Hello World、协作处理拉取请求 | 直接并入 | 作为 Git / GitHub 协作主资料 |
| Day 17 | Chinese README + 真实仓库 README / CONTRIBUTING | 改写后并入 | 写成“如何读项目 / 如何写 README”检查表 |
| Day 18–21 | Cursor Chat / Agent / Rules；Claude Code workflows / best practices | 直接并入 | 作为 AI 工作流主资料与护栏资料 |
| Day 22–25 | Google MLCC、PyTorch Blitz | 直接并入 | 作为概念主线与最小实验主资料 |
| Day 25–27 | Hugging Face pipeline / chapter3 | 直接并入 | 作为推理 demo 与训练升级材料 |
| Day 28 延伸阅读 | multi-agent surveys + AutoGen / LangGraph / CrewAI | 改写后并入 | 仅放“后续路线 / 进阶阅读”，不前置到主线 |

---

## 10. 缺口与后续补采建议

1. **中文视频型资料仍偏少**：当前主清单以文档为主。若正式教程需要“看视频也能跟上”，建议为每周再补 1–2 个高质量视频入口。
2. **GitHub Projects 中文高质量资料不足**：目前更适合直接链接英文官方页，或由教程自行改写为中文说明。
3. **OpenAI prompt engineering 官方正文本轮未稳定抓到**：如果后续课程要专门讲“提示词工程”，建议单独执行一次下载与核验任务。
4. **multi-agent 框架中文官方资料不足**：当前更适合作为结课后英文进阶材料，而不是主教程内容。

---

## 11. 去重与初步缺口标记

### 已去重处理
- Remote SSH 保留 2 条官方页 + 1 条 SSH 基础教程，不再重复纳入多篇相似博客。
- Git / GitHub 保留 Pro Git + GitHub Docs 中文主线，不重复纳入大量二手 Git 入门贴。
- Cursor / AI coding 以官方中文文档为核心，社区经验文不再重复堆叠。
- 深度学习保留 Google / PyTorch / Hugging Face 三组主线，不再扩展过多框架教程。

### 薄弱章节
- Day 17 项目阅读：真实仓库案例还可再补一份更小型、纯 Python 项目。
- Day 19–21 AI coding：仍可追加一条“中文化的 AI 工程守则”高质量来源。
- Day 28 后续路线：可在下一轮补一份“30 天进阶计划模板”型资料。

---

## 12. 最终判断

对当前 28 天课程路线而言，**最值得优先并入的不是更多资料数量，而是更稳定的资料结构**：
- 第 1–2 周：官方环境与 Linux 文档 + 中文小白教程
- 第 2–3 周：Pro Git + GitHub Docs 中文页
- 第 3–4 周：Cursor / Claude Code 官方文档 + 最小工程实践
- 第 4 周：Google MLCC + PyTorch Blitz + Hugging Face 中文课程
- 结课后延伸：multi-agent 综述与 Agent 框架文档

这份清单已经满足“可追溯链接、标题、摘要与适用章节”的首轮资料库要求，可直接供后续“并入 zero-basics-plan 的综述摘要”任务使用。