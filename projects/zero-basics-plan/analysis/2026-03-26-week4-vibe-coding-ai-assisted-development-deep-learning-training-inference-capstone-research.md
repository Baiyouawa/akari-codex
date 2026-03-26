# 第 4 周资料调研：Vibe Coding 方法、AI 辅助开发实践、深度学习基础概念、训练 / 推理入门、综合实战与结课安排

- 生成时间：2026-03-26
- 访问时间：2026-03-26T21:49:42+08:00（来源：`get_current_time`）
- 适用项目：`projects/zero-basics-plan`
- 记录目的：为 28 天教程第 4 周编写提供可直接复用的资料清单、知识结构、课程映射、结课项目与来源记录

## 使用说明

- 可信度分级：`官方` / `半官方` / `社区实践`
- 使用级别：`入门必读` / `进阶参考` / `补充阅读`
- 本轮优先保留：官方文档、官方中文镜像 / 中文文档、可持续维护的课程页面、对初学者友好的高质量解释材料
- 本轮谨慎使用：Vibe Coding 相关内容高度时效化，且“原始定义”主要来自 Karpathy 的 X 帖文；由于 `web_fetch` 无法直接读取 X 动态正文，本轮采用可追溯的二级来源交叉记录，并在文中显式标注该限制
- 去重原则：同类知识点优先保留官方原始文档；媒体解读只在补充概念边界、案例或风险时保留

---

## 1. Vibe Coding 方法

### 主题知识点

- Vibe Coding 的核心心智：从“逐行精确编程”转向“高层意图表达 + 快速反馈修正”
- 典型流程：描述目标 → 让 AI 生成 → Accept / Apply → 运行验证 → 继续口头 / 文字修正
- 适用场景：原型验证、周末项目、简单功能、UI 骨架、脚手架搭建
- 风险边界：可维护性、隐藏 bug、错误抽象、对底层实现失去掌控
- 与第 3 周 AI 工作流的区别：第 3 周偏“工具入门”，第 4 周偏“方法论升级与风险管理”

### 推荐讲解顺序

1. 先解释 Vibe Coding 为什么会出现：AI 工具把“写代码”部分越来越外包给模型
2. 再讲它不是“不会编程也能永远搞定一切”，而是“把注意力转向意图、验证和决策”
3. 然后讲适合场景与不适合场景
4. 最后补“如何在教程里安全地教”：强调 checkpoints、diff、测试和回退机制

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/版本 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VC-01 | Andrej Karpathy 提出"Vibe Coding": AI 时代的新型编程范式 | 火山引擎开发者社区 | 火山引擎社区编辑 | https://developer.volcengine.com/articles/7468990507067113511 | 页面抓取于 2026-03-26；文内描述指向 2025-02 概念提出 | 中文 | vibe coding, AI coding, prototyping | 社区实践 | 入门必读 | 文章概括 Vibe Coding 的几个核心特征：极简交互、LLM 驱动、快速迭代、专注功能实现、弱化代码理解成本，并明确指出它特别适合周末原型、小功能和非关键系统。还同时列出可维护性与质量控制风险。 | 中文表述清晰，适合作为零基础课程里对概念的第一层解释。 | 不是原始定义，属于二级解读资料；需与 VC-02 / VC-03 交叉使用。 |
| VC-02 | 资讯 \\| 大神 Andrej Karpathy 提出 Vibe 编码：提示、明白、后悔？尚未发现的 Vibe 趋势的风险 | 智源社区 | 智源社区转载编辑 | https://hub.baai.ac.cn/view/44664 | 2025-04-04 | 中文 | vibe coding, risks, AI programming | 社区实践 | 入门必读 | 页面明确写出该词由 Andrej Karpathy 提出，并转述“fully give in to the vibes… forget that the code even exists”的核心表述，同时强调了主流讨论中的兴奋与担忧并存。 | 能补上“概念来源 + 风险讨论”的两个关键面。 | 同样不是 X 原帖直引；适合作为说明 Karpathy 原始表述的可访问替代来源。 |
| VC-03 | Who Coined Vibe Coding? The Andrej Karpathy Origin Story | Natively | Timothy Lindblom | https://natively.dev/articles/vibe-coding-origin | 2026-01 | English | origin, history, Karpathy | 社区实践 | 进阶参考 | 文章专门梳理 Vibe Coding 的概念来源、传播路径与行业影响，明确把 2025-02-02 的 Karpathy 帖文作为起点。 | 适合课程编写者追溯概念脉络。 | 含大量趋势型数字，正文若引用需单独核验；本轮只采其“概念来源脉络”而不采市场数字。 |
| VC-04 | Cursor - 概述 | Cursor 中文文档 | Cursor | https://docs.cursor.ac.cn/chat/overview | 页面未抓到显式时间 | 中文 | ask, edit, agent, apply, checkpoints | 官方 | 入门必读 | 官方文档说明统一 AI 界面包含 Ask / Edit / Agent 三种模式，并强调自动上下文、应用更改、检查点、迭代 lint 等机制。它实际上给出了 Vibe Coding 得以成立的 IDE 工作流基础。 | 能把抽象方法论落到可操作工具能力上。 | 适合和 VC-05、VC-06 组合讲“想法 → 改动 → 回退”。 |
| VC-05 | Cursor – 代理（Agent） | Cursor 中文文档 | Cursor | https://docs.cursor.ac.cn/chat/agent | 页面未抓到显式时间 | 中文 | agent, tools, terminal, yolo | 官方 | 入门必读 | 文档说明 Agent 可读取 / 写入代码、搜索代码库、调用 MCP、运行终端命令、自动网页搜索，并有 25 次工具调用上限、Yolo 模式和终端防护栏。 | 直接支撑“Vibe Coding 不是单次补全，而是 agentic 编程”的核心认识。 | 强时效页面，正式教程需显式标注“以当前版本为准”。 |
| VC-06 | Best Practices for Claude Code | Claude Code Docs | Anthropic | https://code.claude.com/docs/en/best-practices | 页面抓取于 2026-03-26 | English | verify, explore-plan-code, context | 官方 | 入门必读 | 官方最佳实践明确提出“Give Claude a way to verify its work”“Explore first, then plan, then code”“Manage context aggressively”等原则。它从反面说明：Vibe Coding 要有效，不能只有 vibe，还必须设计验证手段。 | 很适合拿来给 Vibe Coding 做“护栏”，避免学员把它误解成盲信 AI。 | 英文资料，教学时建议中文化提炼。 |

### 小结

- 主参考优先级：`VC-04` → `VC-05` → `VC-06` → `VC-01`
- 第 4 周正文可直接写入的章节候选：
  - 什么是 Vibe Coding：为什么大家开始“先说需求，再看结果”
  - Vibe Coding 适合做什么，不适合做什么
  - 没有验证的 Vibe Coding，很容易变成技术债
  - 用 checkpoints、diff、测试把“氛围”拉回工程闭环

---

## 2. AI 辅助开发实践

### 主题知识点

- AI 辅助开发不等于“一键生成”，而是“上下文工程 + 小步验证 + 人类兜底”
- 常见能力：解释代码、生成草稿、自动修改、运行命令、生成 PR、做 review 辅助
- 关键护栏：权限控制、diff 审查、自动化验证、规则文件、上下文边界
- 多工具视角：IDE 内 Agent、CLI Agent、云端 coding agent
- 对初学者的最小工作流：明确任务 → 提供上下文 → 生成更改 → 看 diff → 本地运行 / 测试 → 记录结论

### 推荐讲解顺序

1. 先讲“AI 辅助开发”的边界：辅助的是开发流程，不只是写代码
2. 再讲三类常见形态：IDE 内、CLI、平台托管 agent
3. 然后讲共通做法：规则、上下文、验证、回退
4. 最后给出可直接模仿的最小工作流模板

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/版本 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AID-01 | Common workflows | Claude Code Docs | Anthropic | https://code.claude.com/docs/en/common-workflows | 页面抓取于 2026-03-26 | English | workflows, codebase, tests, PRs | 官方 | 入门必读 | 官方工作流页覆盖理解新代码库、修 bug、重构、写测试、创建 PR、并行会话、计划模式等常见任务，并给出可复用提示词与执行路径。 | 对“AI 如何真正参与完整开发流程”解释最完整。 | 非常适合转写成教程中的流程图或 checklist。 |
| AID-02 | Best Practices for Claude Code | Claude Code Docs | Anthropic | https://code.claude.com/docs/en/best-practices | 页面抓取于 2026-03-26 | English | best practices, verification, context | 官方 | 入门必读 | 文档强调给 Agent 验证路径、先探索再规划再编码、尽早纠偏、主动管理上下文、使用子代理等原则。 | 可作为“AI 辅助开发守则”的主参考。 | 与 AID-01 配合使用效果最好。 |
| AID-03 | About GitHub Copilot coding agent | GitHub Docs | GitHub | https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | 页面抓取于 2026-03-26 | English | coding agent, sessions, PR | 官方 | 入门必读 | GitHub Docs 将 coding agent 放在 agent、PR、session、review、hooks、自定义技能等体系中，说明 AI 辅助开发已经从补全工具演进为平台级工作流组件。 | 适合帮助学员理解“agent = 可被管理的开发参与者”。 | 抓取正文偏导航型，但路径与主题边界清晰，适合做资料入口。 |
| AID-04 | Responsible use of GitHub Copilot coding agent on GitHub.com | GitHub Docs | GitHub | https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent | 页面抓取于 2026-03-26 | English | responsible use, risk, oversight | 官方 | 入门必读 | 该页面位于 GitHub Copilot 的 Responsible use 路径下，表明 GitHub 将 coding agent 明确纳入负责任使用框架，强调监督、审阅与风险管理是产品级要求。 | 很适合做“为什么不能把 agent 当自动驾驶”的权威来源。 | `web_fetch` 抓到的正文以导航为主，正式教程中宜链接到该页并做原则性引用。 |
| AID-05 | GitHub Copilot coding agent | Visual Studio Code Docs | VS Code Docs | https://code.visualstudio.com/docs/copilot/copilot-coding-agent | 页面抓取于 2026-03-26 | English | VS Code, copilot, agents | 官方 | 进阶参考 | VS Code 文档导航显示 Copilot 已有 Agents、Planning、Memory、Tools、Subagents、Cloud Agents 等完整概念体系。 | 说明 AI 辅助开发的主流 IDE 正在把 agent 作为一等能力建设。 | 适合做“生态全景”补充，不适合本周唯一主资料。 |
| AID-06 | Cursor - AI 规则 | Cursor 中文文档 | Cursor | https://docs.cursor.ac.cn/context/rules-for-ai | 页面未抓到显式时间 | 中文 | rules, prompting, system guidance | 官方 | 入门必读 | 文档明确项目规则存储在 `.cursor/rules` 中，可按 glob 自动附加到请求；全局规则则适用于所有项目。其本质是把团队约定、输出格式、代码风格前置为稳定上下文。 | 对初学者理解“为什么规则比临时 prompt 更稳定”非常关键。 | 可与第 3 周内容衔接。 |

### AI 辅助开发最小闭环

1. 说清楚任务目标、边界和完成标准
2. 把相关文件、目录、约束和规则给到 AI
3. 让 AI 先做小步改动或先做计划
4. 查看 diff / 解释 / 终端输出
5. 运行最小验证：lint、test、手工检查
6. 用 PR、日志或笔记记录改动原因与风险

### 小结

- 主参考优先级：`AID-01` → `AID-02` → `AID-06` → `AID-04`
- 第 4 周正文可直接写入的章节候选：
  - AI 辅助开发不是“帮你写完”，而是“帮你走流程”
  - 规则、上下文、验证：AI 开发三件套
  - 为什么每次都要看 diff、看终端、看测试
  - 从 IDE Agent 到平台 Agent：AI 开发工具正在怎么演化

---

## 3. 深度学习基础概念

### 主题知识点

- 深度学习与机器学习、神经网络、张量之间的关系
- 神经网络的最小结构：输入层、隐藏层、输出层、激活函数
- 训练的最小心智模型：前向传播、损失函数、梯度下降、反向传播
- 工具视角：PyTorch / TensorFlow 都是“张量 + 自动微分 + 神经网络构建”体系
- 面向零基础的重点：先理解概念和流程，再进入框架 API

### 推荐讲解顺序

1. 先回答“深度学习到底在干什么”
2. 再讲神经网络的最小组件
3. 然后讲训练怎么发生：预测 → 算误差 → 调参数
4. 最后用 PyTorch / Google MLCC 做框架与概念对应

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/版本 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DL-01 | 机器学习速成课程 | Google for Developers | Google | https://developers.google.cn/machine-learning/crash-course?hl=zh-cn | 页面抓取于 2026-03-26；站点说明新版 MLCC 已发布 | 中文 | MLCC, neural networks, overfitting | 官方 | 入门必读 | Google 官方中文课程页把内容分为模型、数据、高级模型、现实世界机器学习等模块，其中“神经网络”“数据集、泛化和过拟合”“大型语言模型简介”都适合第 4 周概念入门。 | 中文官方课程，面向初学者教学友好度高。 | 非单页教程，更适合作为课程目录和模块入口。 |
| DL-02 | PyTorch 深度学习：60 分钟闪电入门 | PyTorch 中文文档 | PyTorch / Soumith Chintala | https://docs.pytorch.ac.cn/tutorials/beginner/deep_learning_60min_blitz.html | 创建于 2017-03-24；最后更新于 2023-05-31；最后验证于 2024-11-05 | 中文 | PyTorch, tensor, autograd, neural network | 官方 | 入门必读 | 教程明确目标是从高层次理解 Tensor 库和神经网络，并训练一个小型神经网络进行图像分类；目录拆成张量、autograd、神经网络、训练分类器四段，正好对应第 4 周的学习链。 | 是把抽象概念落到实践 API 的最佳主资料之一。 | 时间信息完整，适合作为正文引用。 |
| DL-03 | PyTorch 文档 | PyTorch 中文文档 | PyTorch | https://docs.pytorch.ac.cn/docs/stable/index.html | 页面抓取于 2026-03-26 | 中文 | tensors, torch.nn, autograd | 官方 | 进阶参考 | 文档首页将 PyTorch 定义为“优化的张量库，用于使用 GPU 和 CPU 进行深度学习”，并按 torch、torch.nn、autograd 等模块组织。 | 可作为“术语与 API 索引”的稳定来源。 | 更偏参考手册，不宜直接给新手通读。 |
| DL-04 | TensorFlow 学习 | TensorFlow 中文官网 | Google / TensorFlow | https://tensorflow.google.cn/learn?hl=zh-cn | 页面抓取于 2026-03-26 | 中文 | tensorflow, training, deployment | 官方 | 入门必读 | TensorFlow 中文页按“构建和微调模型”“部署模型”“生产型机器学习”等路径组织内容，说明深度学习不仅是训练，还包括部署与推断。 | 适合从生态视角补齐“训练之后还有推理与部署”。 | 页面内容较宽，正式教程中宜聚焦初学者相关段落。 |
| DL-05 | Neural Networks | 3Blue1Brown | Grant Sanderson | https://www.3blue1brown.com/topics/neural-networks | 页面抓取于 2026-03-26 | English | neural network, gradient descent, backpropagation | 半官方 | 补充阅读 | 专题页汇总“什么是神经网络”“梯度下降”“反向传播”等可视化文章与视频，是理解抽象概念的高质量解释性资源。 | 极适合补强直觉，不会和官方框架文档重复。 | 非框架文档，更适合作为补充阅读或视频推荐。 |

### 小结

- 主参考优先级：`DL-01` → `DL-02` → `DL-04` → `DL-05`
- 第 4 周正文可直接写入的章节候选：
  - 深度学习在做什么：从输入到预测再到调参
  - 神经网络、张量、梯度，这些词各是什么意思
  - 为什么初学时要先理解流程，再去记 API
  - PyTorch 和 TensorFlow 各自像什么工具箱

---

## 4. 训练 / 推理入门

### 主题知识点

- 训练与推理的根本区别：训练会更新参数，推理只使用已有参数做预测
- 训练流程：数据 → 前向传播 → 损失 → 反向传播 → 参数更新
- 推理流程：输入 → 预处理 → 模型前向 → 输出结果 → 后处理
- 初学者能感知的框架对应：Trainer、pipeline、Serving、Lite / Edge 推理
- 本周教学边界：建立流程认知，不要求学员掌握大规模训练

### 推荐讲解顺序

1. 先用一句话区分 training 与 inference
2. 再用 Hugging Face pipeline 讲推理，用 PyTorch 训练分类器讲训练
3. 然后补充数据、显存 / 设备、速度、部署的不同关注点
4. 最后给出一个从“调用预训练模型”到“微调小模型”的升级路径

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/版本 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TI-01 | Transformers 能做什么？ | Hugging Face 课程 | Hugging Face | https://huggingface.co/docs/course/zh-CN/chapter1/3 | 页面抓取于 2026-03-26 | 中文 | pipeline, inference, pretrained model | 官方 | 入门必读 | 页面使用 `pipeline()` 函数展示如何把模型与预处理 / 后处理串起来，直接输入文本即可得到推理结果。它非常适合讲“什么叫推理”：拿一个已经训练好的模型来处理新输入。 | 中文官方资料，示例简洁，教学转化成本低。 | 可直接做课堂 live demo。 |
| TI-02 | 第 3 章 本章简介 | Hugging Face 课程 | Hugging Face | https://huggingface.co/docs/course/zh-CN/chapter3/1 | 页面抓取于 2026-03-26 | 中文 | fine-tuning, training, trainer | 官方 | 入门必读 | 页面明确指出本章要解决“如何使用自己的数据集微调预训练模型”，并列出加载数据集、使用 Trainer API、使用自定义训练过程、利用 Accelerate 运行训练过程等目标。 | 非常适合作为“训练入门”概念入口。 | 比直接上源码更友好。 |
| TI-03 | PyTorch 深度学习：60 分钟闪电入门 | PyTorch 中文文档 | PyTorch / Soumith Chintala | https://docs.pytorch.ac.cn/tutorials/beginner/deep_learning_60min_blitz.html | 创建于 2017-03-24；最后更新于 2023-05-31；最后验证于 2024-11-05 | 中文 | classifier, train, autograd | 官方 | 入门必读 | 教程最后一部分是训练分类器，与前面的张量、autograd、神经网络组成一个最小训练闭环。 | 很适合做“训练是什么”的第一套动手材料。 | 与 TI-01 可形成“推理先行，训练再进阶”的节奏。 |
| TI-04 | TensorFlow 学习 | TensorFlow 中文官网 | Google / TensorFlow | https://tensorflow.google.cn/learn?hl=zh-cn | 页面抓取于 2026-03-26 | 中文 | training, deployment, inference | 官方 | 进阶参考 | 页面分别讲了构建 / 微调模型与部署 / 推断环境，能够帮助学员理解训练和推理在工具链上的不同位置。 | 适合给“训练后怎么上线”一个宽视角。 | 更偏平台导览。 |
| TI-05 | 机器学习速成课程 | Google for Developers | Google | https://developers.google.cn/machine-learning/crash-course?hl=zh-cn | 页面抓取于 2026-03-26 | 中文 | datasets, overfitting, neural networks | 官方 | 入门必读 | MLCC 中的数据、泛化和过拟合模块能帮助解释训练过程中为什么会“学得太死”或“泛化不好”，是区分训练效果与推理效果的重要背景资料。 | 能避免课程只讲 API、不讲模型行为。 | 可选讲“过拟合”作为第 4 周最低限度理论。 |

### 训练 / 推理对照表（用于教程正文）

| 维度 | 训练 | 推理 |
|---|---|---|
| 目标 | 让模型参数变好 | 用已有模型产出结果 |
| 是否更新参数 | 是 | 否 |
| 输入 | 带标签或有明确训练目标的数据 | 新输入样本 |
| 关注点 | 损失、梯度、学习率、过拟合 | 延迟、吞吐、稳定性、结果质量 |
| 初学者对应工具 | Trainer、PyTorch training loop | pipeline、预测 API、部署服务 |

### 小结

- 主参考优先级：`TI-01` → `TI-02` → `TI-03` → `TI-05`
- 第 4 周正文可直接写入的章节候选：
  - 训练和推理到底有什么区别
  - 为什么先学调用预训练模型，再学微调
  - 过拟合是什么，为什么训练好不等于真正会用
  - 从 pipeline 到 Trainer：一条最小升级路径

---

## 5. 综合实战与结课安排

### 主题知识点

- 第 4 周需要把前 3 周的环境、Git / GitHub、AI 工作流与本周的深度学习概念串起来
- 实战不应追求“大而全”，而应追求“能在有限时间里闭环”
- 结课项目最好同时包含：需求描述、AI 辅助开发、模型推理调用、最小部署 / 演示、GitHub 协作记录
- 结课安排应包含：项目演示、复盘、答疑、延伸路线

### 推荐讲解顺序

1. 先给一个小而完整的结课项目
2. 再把项目拆成需求、数据 / 模型、推理调用、前端 / CLI、测试与 README
3. 然后给出每一天如何推进
4. 最后做复盘：学到了什么、还没学什么、后面怎么继续

### 资料卡片

| 编号 | 标题 | 来源平台 | 作者/机构 | 链接 | 发布时间/版本 | 语言 | 标签 | 可信度 | 使用级别 | 摘要 | 推荐理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAP-01 | Common workflows | Claude Code Docs | Anthropic | https://code.claude.com/docs/en/common-workflows | 页面抓取于 2026-03-26 | English | workflow, PR, tests, docs | 官方 | 入门必读 | 该页覆盖“理解代码库、修 bug、写测试、创建 PR、处理文档”等日常工作流，适合作为结课项目执行清单来源。 | 能把项目执行拆成可管理步骤。 | 可转成中文 checklist。 |
| CAP-02 | Cursor - 概述 | Cursor 中文文档 | Cursor | https://docs.cursor.ac.cn/chat/overview | 页面未抓到显式时间 | 中文 | checkpoints, apply, lint | 官方 | 入门必读 | 文档里的 apply、checkpoints、迭代 lint 很适合结课项目阶段使用，帮助学员保留回退能力。 | 对“边做边纠错”非常实用。 | 可在项目实战前再次复习。 |
| CAP-03 | Cursor – 代理（Agent） | Cursor 中文文档 | Cursor | https://docs.cursor.ac.cn/chat/agent | 页面未抓到显式时间 | 中文 | agent, terminal, guardrails | 官方 | 入门必读 | Agent 页给出工具能力、Yolo 模式与防护栏，适合在结课项目中强调“能自动做事，但要配权限和验证”。 | 很适合与项目风险管理结合。 | 强时效页面。 |
| CAP-04 | Transformers 能做什么？ | Hugging Face 课程 | Hugging Face | https://huggingface.co/docs/course/zh-CN/chapter1/3 | 页面抓取于 2026-03-26 | 中文 | inference, demo, pipeline | 官方 | 入门必读 | 可直接用 `pipeline()` 快速搭建文本分类、情感分析等演示型应用，是初学者做结课 demo 的低门槛入口。 | 适合把“深度学习”变成“可展示功能”。 | 建议选现成任务，避免自己训练大模型。 |
| CAP-05 | 第 3 章 本章简介 | Hugging Face 课程 | Hugging Face | https://huggingface.co/docs/course/zh-CN/chapter3/1 | 页面抓取于 2026-03-26 | 中文 | fine-tuning, training project | 官方 | 进阶参考 | 对于学有余力的学员，可在结课项目中尝试用小数据集做“微调演示”而不是仅调用现成模型。 | 给进阶组留出上升空间。 | 仅建议作为加分项，不应成为所有人的强制要求。 |

### 推荐结课项目

#### 方案 A：AI 辅助开发一个“文本情绪 / 主题分析小工具”

- 项目形态：CLI 或简单网页
- 最小功能：
  - 输入一段文本
  - 使用 Hugging Face `pipeline()` 做情绪分类或主题判断
  - 展示结果与概率
  - 写 README 说明如何运行
- 第 1–3 周能力映射：
  - Linux / 环境：安装依赖、运行脚本
  - Git / GitHub：建仓、提交、分支、PR
  - Cursor / Claude Code：生成脚手架、补测试、写文档
  - 深度学习：理解“这是推理，不是从零训练”
- 优点：门槛低、闭环快、结果可展示

#### 方案 B：AI 辅助开发一个“本地图片分类 / 手写数字识别演示”

- 项目形态：Notebook 或脚本
- 最小功能：
  - 跑通 PyTorch 入门教程中的分类示例
  - 展示训练过程中的 loss / accuracy
  - 对测试样本做推理
- 适合人群：愿意多花一点时间理解训练流程的学员
- 风险：环境依赖和运行时间高于方案 A

#### 方案 C：双层结课制

- 基础线：完成一个调用预训练模型的小应用
- 进阶线：在现成数据集上完成一次最小微调
- 好处：避免所有人都被训练环节卡住，同时保留进阶挑战

### 第 4 周建议的 7 天安排

| 天数 | 学习主题 | 核心目标 | 主要资料 |
|---|---|---|---|
| Day 22 | Vibe Coding 方法 | 理解“意图表达 + 快速验证”的方法与边界 | VC-04, VC-05, VC-06, VC-01 |
| Day 23 | AI 辅助开发实践 | 学会规则、上下文、验证、diff 审查 | AID-01, AID-02, AID-06, AID-04 |
| Day 24 | 深度学习基础概念 1 | 理解神经网络、张量、梯度与训练最小闭环 | DL-01, DL-02, DL-05 |
| Day 25 | 深度学习基础概念 2 | 认识框架视角下的模型构建、训练与部署 | DL-02, DL-04, DL-03 |
| Day 26 | 推理入门 | 会调用预训练模型完成一个最小推理 demo | TI-01, TI-03 |
| Day 27 | 训练 / 微调入门 | 理解微调与训练流程，完成可选小实验 | TI-02, TI-03, TI-05 |
| Day 28 | 结课项目与复盘 | 完成演示、README、答辩式复盘与后续路线规划 | CAP-01, CAP-02, CAP-04 |

### 结课日建议安排

1. **项目展示（40% 时间）**：每人 / 每组演示功能、讲输入输出、展示代码结构
2. **工程回顾（20% 时间）**：展示 commit 历史、README、遇到的问题与修复方法
3. **AI 协作回顾（20% 时间）**：分享哪些 prompt / 规则 / 验证方式有效，哪些会出错
4. **深度学习概念回顾（10% 时间）**：再区分一次训练与推理
5. **后续路线（10% 时间）**：给出“继续学 Python / 数据处理 / 模型微调 / 部署”的路线图

---

## 6. 面向第 4 周教程的骨架映射

### 建议章节标题

1. Vibe Coding：为什么现在很多开发者开始“先说再改”
2. AI 辅助开发的正确姿势：规则、上下文、验证
3. 深度学习入门：神经网络、张量、梯度到底是什么
4. 训练与推理：同一个模型，两个完全不同的阶段
5. 用预训练模型做一个最小 AI 应用
6. 结课项目：把 AI 开发流程和模型调用真正串起来

### 可直接放入正文的教学提醒

- 不要把 Vibe Coding 教成“完全不用看代码”
- 不要把训练和推理混为一谈
- 第 4 周的重点是建立概念与闭环，不是追求大模型工程深度
- 结课项目优先保证“能运行、能解释、能复盘”而不是“功能越多越好”

---

## 7. 初筛、优先级与去重结论

### 优先保留

- Cursor 官方中文文档：最适合支撑 Vibe Coding 与 AI 辅助开发实践
- Claude Code Docs：最适合支撑 agentic coding 的流程和最佳实践
- Google MLCC 中文课程：最适合支撑深度学习概念的教学入口
- PyTorch 中文教程：最适合连接“概念 → 代码 → 最小训练实践”
- Hugging Face 中文课程：最适合连接“推理 → 微调 → demo”

### 降级为补充阅读

- 3Blue1Brown：适合建立直觉，但不替代框架与课程型主资料
- 各类社区对 Vibe Coding 的评论文章：适合补充风险与语境，不应替代官方工具文档

### 当前缺口

- Karpathy 原始 X 帖文因 `web_fetch` 无法执行 JavaScript 页面，未能直接抓取原文；本轮已用多条可访问二级来源交叉记录概念来源，但正式教程若需逐字引用，建议后续补做截图或可访问镜像核验
- 本轮视频资料较少；如果最终教程需要“视频辅助学习”，建议补充 3Blue1Brown 神经网络系列与官方演示视频入口
- 训练 / 推理部分仍以概念入门与小型示例为主，尚未覆盖部署工程细节；这符合 28 天零基础教程边界

---

## 8. 第 4 周课程建议总评

- **最适合零基础的主线**：Vibe Coding 方法 → AI 辅助开发守则 → 深度学习最小概念 → 推理 demo → 可选微调 → 结课项目
- **最稳妥的结课项目**：调用预训练模型完成一个文本分析小工具，并配合 AI 工具完成代码、文档和 GitHub 协作
- **最容易翻车的点**：
  - 把 Vibe Coding 教成“闭眼 Accept All”
  - 把训练和推理讲成同一件事
  - 给所有学生统一要求做训练项目，导致环境和时间成本过高
- **教学建议**：采用“双层结课制”，基础线做推理应用，进阶线尝试微调实验

## 9. 来源记录（按本次调研实际使用）

- 火山引擎：`https://developer.volcengine.com/articles/7468990507067113511`
- 智源社区：`https://hub.baai.ac.cn/view/44664`
- Natively：`https://natively.dev/articles/vibe-coding-origin`
- Cursor 概述：`https://docs.cursor.ac.cn/chat/overview`
- Cursor Agent：`https://docs.cursor.ac.cn/chat/agent`
- Cursor AI 规则：`https://docs.cursor.ac.cn/context/rules-for-ai`
- Claude Code Best Practices：`https://code.claude.com/docs/en/best-practices`
- Claude Code Common workflows：`https://code.claude.com/docs/en/common-workflows`
- GitHub Copilot coding agent（概念）：`https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent`
- GitHub Copilot coding agent（负责任使用）：`https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent`
- VS Code Copilot coding agent：`https://code.visualstudio.com/docs/copilot/copilot-coding-agent`
- Google MLCC 中文：`https://developers.google.cn/machine-learning/crash-course?hl=zh-cn`
- PyTorch 深度学习：60 分钟闪电入门：`https://docs.pytorch.ac.cn/tutorials/beginner/deep_learning_60min_blitz.html`
- PyTorch 中文文档：`https://docs.pytorch.ac.cn/docs/stable/index.html`
- TensorFlow 中文学习页：`https://tensorflow.google.cn/learn?hl=zh-cn`
- 3Blue1Brown Neural Networks：`https://www.3blue1brown.com/topics/neural-networks`
- Hugging Face 课程：Transformers 能做什么？`https://huggingface.co/docs/course/zh-CN/chapter1/3`
- Hugging Face 课程：第 3 章本章简介：`https://huggingface.co/docs/course/zh-CN/chapter3/1`
