# 2026-03-26 最新五篇 multi-agent 相关综述精读总结

## 任务说明

基于项目内已下载的本地 PDF，筛选并精读“multi-agent 相关最新五篇综述”，输出中文总结与研究 idea。本文仅使用仓库内本地 PDF 与对应 arXiv/论文页面元数据，不依赖未落库的外部二手总结。

## 选文方法与范围

### 本地候选池

本次会话先检查本地目录 `projects/multi-agent-survey/downloads/recent-review-pdfs/`，共看到 20 篇已下载 PDF：

- 2402.01680.pdf
- 2412.17481.pdf
- 2501.06322.pdf
- 2502.14321.pdf
- 2505.21116.pdf
- 2510.25445.pdf
- 2512.02682.pdf
- 2512.06914.pdf
- 2512.16301.pdf
- 2601.01891.pdf
- 2601.02749.pdf
- 2601.06216.pdf
- 2601.09822.pdf
- 2601.10122.pdf
- 2601.12560.pdf
- 2602.04813.pdf
- 2602.11583.pdf
- 2603.09002.pdf
- 2603.22386.pdf
- 2603.22928.pdf

来源：`cd . && python3` 遍历 `projects/multi-agent-survey/downloads/recent-review-pdfs` 输出文件名。

### 选择标准

从候选池中，按“时间尽可能新 + 与 multi-agent/agentic multi-agent 主题直接相关 + 属于 survey/review/taxonomy/systematization 论文”筛出 5 篇：

1. **2603.22386** — *From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents*
2. **2603.09002** — *Security Considerations for Multi-agent Systems*
3. **2602.11583** — *The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why — A Survey from MARL to Emergent Language and LLMs*
4. **2601.12560** — *Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents*
5. **2512.16301** — *Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills*

未纳入但接近主题的例子：

- `2603.22928` 关注 agentic AI 攻击面，覆盖 multi-agent emergent threats，但主题更偏 agentic 安全总览；
- `2602.04813` 为医疗场景 agentic AI taxonomy，multi-agent 成分明显，但领域更垂直；
- `2601.09822` 为软件工程场景 agentic systems 综述，范围也更垂直。

## 五篇综述总表

| 时间 | arXiv | 题目 | 本地 PDF | 核心覆盖面 |
|---|---|---|---|---|
| 2026-03-23 | 2603.22386 | From Static Templates to Dynamic Runtime Graphs | `downloads/recent-review-pdfs/2603.22386.pdf` | LLM agent 工作流/图结构优化 |
| 2026-03-09 | 2603.09002 | Security Considerations for Multi-agent Systems | `downloads/recent-review-pdfs/2603.09002.pdf` | 多智能体系统安全风险与框架评估 |
| 2026-02-12 | 2602.11583 | The Five Ws of Multi-Agent Communication | `downloads/recent-review-pdfs/2602.11583.pdf` | 多智能体通信：MARL/涌现语言/LLM |
| 2026-01-18 | 2601.12560 | Agentic Artificial Intelligence (AI) | `downloads/recent-review-pdfs/2601.12560.pdf` | Agentic AI 架构、taxonomy、评测 |
| 2025-12-18 | 2512.16301 | Adaptation of Agentic AI | `downloads/recent-review-pdfs/2512.16301.pdf` | agent 后训练、记忆、技能适配 |

## 逐篇精读总结

---

## 1. 2603.22386 — Workflow Optimization for LLM Agents

- **提交时间**：2026-03-23
- **URL**：https://arxiv.org/abs/2603.22386
- **本地 PDF**：`projects/multi-agent-survey/downloads/recent-review-pdfs/2603.22386.pdf`
- **本地抽取文本**：`projects/multi-agent-survey/analysis/tmp_extracts/2603.22386.txt`

### 论文要解决什么问题

这篇综述认为，Agent 系统的关键不只是“单次 LLM 调用能力”，而是**由哪些节点/代理组成、它们如何依赖、信息如何流动**的“工作流结构”本身。作者把这类结构统一抽象为 **agentic computation graphs (ACGs)**，试图把 workflow / pipeline / orchestration graph / communication graph 放进同一视角进行比较。

证据：摘要与第 1 节把工作流定义为“LLM calls、retrieval、tool use、code execution、memory updates、verification”的可执行组合；第 2 页目录显示主体被分为 static optimization、dynamic optimization、feedback signals、evaluation、trade-offs 与 open problems。来源：`analysis/tmp_extracts/2603.22386.txt` 第 1–5 页。

### 核心贡献

1. **提出 workflow-centered 的统一表述**：把 agent 系统看成 ACG，而不是只看 prompt 或单节点能力。  
2. **区分三种对象**：`template`、`realized graph`、`execution trace`，避免把“设计图”“运行时实例”“实际轨迹”混为一谈。  
3. **提出 static / dynamic workflow optimization taxonomy**：
   - static：部署前固定模板；
   - dynamic：运行前选择/生成，或运行中编辑图结构。  
4. **强调结构级评测**：不能只看任务成功率，还要看图属性、成本、鲁棒性、跨输入的结构变化。

### 对 multi-agent 研究最有价值的启发

- 多智能体系统可以被自然地纳入“图结构优化”框架：多 agent 的通信拓扑、角色分工、验证器放置位置、是否允许中途重规划，都是可优化变量。  
- 它把很多过去分散的问题串起来了：prompt 优化、team selection、verifier 插入、树状规划、manager-worker 架构，本质上都在改图。  
- 对你当前的 survey 项目尤其有用，因为它提供了一个能把 **ICML/ICLR/NeurIPS 各类多 agent 论文横向整理到同一坐标系** 的“统一外壳”。

### 局限

- 论文主要讨论 **LLM agents/workflows**，并不专门深挖传统 multi-agent systems 的博弈、协商或分布式控制理论。  
- 更多是“组织现有工作”的 survey，不直接给出可复用 benchmark 套件或统一实验协议实现。  
- 对真实部署中的安全、长期记忆漂移、人机协同治理，只是作为 open problems 提到。

### 一句话评价

**这是目前最适合充当“LLM multi-agent 结构总框架”的一篇新综述。**

---

## 2. 2603.09002 — Security Considerations for Multi-agent Systems

- **提交时间**：2026-03-09
- **URL**：https://arxiv.org/abs/2603.09002
- **本地 PDF**：`projects/multi-agent-survey/downloads/recent-review-pdfs/2603.09002.pdf`
- **本地抽取文本**：`projects/multi-agent-survey/analysis/tmp_extracts/2603.09002.txt`

### 论文要解决什么问题

这篇文章聚焦一个很具体但正在变得关键的问题：**多智能体系统（MAS）带来的安全威胁是否已经超出既有 AI 安全框架的覆盖能力？**

作者把 MAS 定义为具有 delegated tool authority、shared persistent memory、inter-agent communication 的系统，然后系统化梳理威胁，并拿 16 个安全/治理框架逐项对照评估。

证据：摘要直接说明其评估对象是 16 security frameworks；并组织出 **193 个威胁项、9 个风险大类**。来源：`analysis/tmp_extracts/2603.09002.txt` 第 1–2 页与 arXiv 摘要页 `https://arxiv.org/abs/2603.09002`。

### 核心贡献

1. **明确提出 MAS 的风险不同于 singular AI model**。  
2. **构建 193 项 threat taxonomy**，覆盖 agent-tool coupling、data leakage、memory poisoning、non-determinism、workflow architecture 等。  
3. **给出跨框架定量比较**：
   - OWASP Agentic Security Initiative 整体覆盖率最高；
   - CDAO toolkit 在开发/运维期更强；
   - 没有框架对任一风险大类实现多数覆盖。  
4. **把“non-determinism”本身视作安全与保障问题**，这对 multi-agent 很重要。

### 对 multi-agent 研究最有价值的启发

- 多智能体不是“多个单 agent 的叠加”，而是会出现**跨 agent 信任传递、共享记忆投毒、tool 权限扩散、重规划级联**等新风险。  
- 论文中大量案例可直接转化成 survey 的“风险分类章节”，尤其适合和工作流优化、通信设计结合起来讨论。  
- 它提醒我们：以后做 multi-agent benchmark 不能只看 task success，还要测 **授权边界、攻击传播、恢复能力、审计可见性**。

### 局限

- 130 页里很大部分是 threat catalog，深度很强，但更偏 framework gap analysis，不是全景式 multi-agent survey。  
- 威胁项规模很大，抽象层级不完全均匀，实际落地时需要二次整理。  
- 一些风险仍以专家建模和前瞻推断为主，真实世界 exploit 数据还在累积。

### 一句话评价

**如果你的综述想避免“只谈能力不谈代价”，这篇是多智能体安全章节的关键底稿。**

---

## 3. 2602.11583 — The Five Ws of Multi-Agent Communication

- **提交时间**：2026-02-12
- **URL**：https://arxiv.org/abs/2602.11583
- **本地 PDF**：`projects/multi-agent-survey/downloads/recent-review-pdfs/2602.11583.pdf`
- **本地抽取文本**：`projects/multi-agent-survey/analysis/tmp_extracts/2602.11583.txt`

### 论文要解决什么问题

作者认为，多智能体通信研究横跨 **MARL、Emergent Language、LLM-based MAS** 三条传统，但彼此割裂，因此提出用“五个 W”统一组织：

- **Who** talks  
- **Whom** to talk to  
- **What** to communicate  
- **When** to communicate  
- **Why** communication helps

证据：摘要与目录直接以 Five Ws 组织，且第 2–4 页清晰展开了 MARL、EL、LLM-powered multi-agent communication 三大板块。来源：`analysis/tmp_extracts/2602.11583.txt`。

### 核心贡献

1. **跨三大范式统一通信问题**：把传统 MARL、涌现语言、LLM agent communication 放到一个框架下。  
2. **系统整理通信设计变量**：接收者选择、消息内容、时机、拓扑、训练目标、评测方式。  
3. **强调跨范式 trade-off**：
   - MARL 通信可优化 reward，但可解释性弱；
   - EL 更关注结构化协议，但泛化和 grounding 难；
   - LLM communication 有自然语言先验，但成本高、稳定性与去中心化控制仍弱。  
4. **给出 future directions**：理论保证、算法发展、benchmark、人本 multi-agent communication。

### 对 multi-agent 研究最有价值的启发

- 这是五篇里**最“正宗”的 multi-agent 核心综述**，尤其适合作为“通信专题”的主线。  
- 对当前很多 LLM 多 agent 论文来说，通信往往只被粗略写成 message passing；这篇综述提醒我们要拆开问：谁和谁通信、通信什么、何时触发、为什么值得。  
- 它还提供了一个很好的桥：可把传统 MARL 的通信理论与新型 LLM-based multi-agent systems 接起来。

### 局限

- 143 页篇幅很长，覆盖广，某些子方向会不可避免地“广而不深”。  
- 因为跨越 MARL/EL/LLM 三界，读者若只关注 LLM agents，可能觉得前半部分转化成本较高。  
- 对工程部署问题（比如成本、权限、安全审计）着墨不如 workflow/security 两篇。

### 一句话评价

**这是当前最值得作为“multi-agent communication 基础综述”的一篇核心参考。**

---

## 4. 2601.12560 — Agentic AI: Architectures, Taxonomies, and Evaluation

- **提交时间**：2026-01-18
- **URL**：https://arxiv.org/abs/2601.12560
- **本地 PDF**：`projects/multi-agent-survey/downloads/recent-review-pdfs/2601.12560.pdf`
- **本地抽取文本**：`projects/multi-agent-survey/analysis/tmp_extracts/2601.12560.txt`

### 论文要解决什么问题

这篇文章要回答的是：**agentic AI 迅速从单轮对话走向感知-推理-规划-行动闭环后，系统架构该怎么统一描述？**

作者提出一个六维 taxonomy：

- Perception  
- Brain  
- Planning  
- Action  
- Tool Use  
- Collaboration

同时讨论 environment、evaluation、安全与挑战，试图给 agentic AI 建一张“总地图”。

证据：摘要与第 1–5 页明示六维 taxonomy，并把多智能体系统作为其中一大维度来分析 chain / star / mesh / workflow graph 等交互形态。来源：`analysis/tmp_extracts/2601.12560.txt` 与 `https://arxiv.org/abs/2601.12560`。

### 核心贡献

1. **给出面向工程实现的 agent architecture 视角**，而不只是应用罗列。  
2. **把 multi-agent collaboration 纳入统一框架**，并与 perception、memory、planning 等组件联动。  
3. **强调 controllable orchestration**：不是盲目提高 agent autonomy，而是通过 graph/state machine/guardrail 提高可控性。  
4. **把 evaluation 与 safety 直接放进架构空间中**：如 cost、latency、accuracy、security、stability。

### 对 multi-agent 研究最有价值的启发

- 很适合作为“大背景综述”：当你需要解释 multi-agent 为什么不是孤立主题，而是 agentic AI 架构演化的一部分，这篇很好用。  
- 它把 collaboration 从“附属功能”提升为体系化模块，适合拿来搭 survey 的总结构图。  
- 对系统实现者尤其有帮助，因为它重视 orchestration、tool connectivity、computer use、deployment 这些工程细节。

### 局限

- 虽覆盖 multi-agent，但焦点仍是 agentic AI 全景，不是专门深挖 multi-agent 某个子问题。  
- 传统 MAS 理论、机制设计、协商博弈等内容较少。  
- taxonomy 相对宏观，用来设计实验还需要更细的操作化变量。

### 一句话评价

**它是“multi-agent 综述”之外一篇极好的上位框架综述。**

---

## 5. 2512.16301 — Adaptation of Agentic AI

- **提交时间**：2025-12-18（v3 更新至 2026-03-09）
- **URL**：https://arxiv.org/abs/2512.16301
- **本地 PDF**：`projects/multi-agent-survey/downloads/recent-review-pdfs/2512.16301.pdf`
- **本地抽取文本**：`projects/multi-agent-survey/analysis/tmp_extracts/2512.16301.txt`

### 论文要解决什么问题

这篇综述试图解决一个经常被分散讨论的问题：**agent 能力提升，究竟是在调 agent 本身，还是在调其工具、记忆、技能系统？**

作者以“adaptation”为总概念，提出一个 2×2 四象限框架：

- A1：tool-execution-signaled agent adaptation  
- A2：agent-output-signaled agent adaptation  
- T1：agent-agnostic tool adaptation  
- T2：agent-supervised tool adaptation

证据：摘要、第 1–6 页和 Figure 1/2/3 都围绕四象限框架展开，并明确把 post-training、memory、skills 三者放到同一设计空间。来源：`analysis/tmp_extracts/2512.16301.txt` 与 `https://arxiv.org/abs/2512.16301`。

### 核心贡献

1. **把 post-training / memory / skills 统一成 adaptation 问题**。  
2. **清楚区分 agent adaptation 与 tool adaptation**，这对多智能体系统尤其重要，因为 agent 往往通过外部 memory / skill library / subagent 扩展。  
3. **强调模块化 trade-off**：成本、灵活性、泛化、灾难性遗忘、独立升级能力。  
4. **把 agentic memory and skills 作为关键适配机制系统整理**。

### 对 multi-agent 研究最有价值的启发

- 多智能体系统中的“角色 specialization”与“技能库复用”问题，可以直接映射到这篇 survey 的 adaptation 框架。  
- 对长期运行的 agent swarm 来说，**持续记忆、技能迁移、子 agent 工具化** 是决定是否可扩展的关键变量，这篇正好切中。  
- 它还能帮助解释：为什么很多系统改进不一定要重新训练主模型，而可以通过外部 skill/memory/tool 侧优化得到。

### 局限

- 重点是 adaptation，而不是 multi-agent coordination 本身。  
- 多智能体内容更多出现在“subagent-as-tool”“agentic memory/skills”等交叉位置，而非传统 MAS 主线。  
- 由于是超新综述，部分实证比较仍基于异构案例，横向结论还要谨慎引用。

### 一句话评价

**它是“多智能体如何持续进化”这一问题上非常前沿的一篇综述。**

## 跨论文综合：这五篇一起说明了什么？

### 1. multi-agent 研究正在从“是否使用多个 agent”转向“如何设计结构、通信、适配与治理”

- `2603.22386` 讲结构优化；
- `2602.11583` 讲通信设计；
- `2512.16301` 讲适配与技能/记忆积累；
- `2603.09002` 讲安全治理；
- `2601.12560` 则提供总架构视角。

**共同趋势**：multi-agent 已不再只是“把一个任务分给多个角色”，而是在走向一个完整系统工程问题。

### 2. 结构、通信、记忆/技能、权限边界，是四个最稳定的核心变量

从五篇中可以抽出最稳定的研究轴：

1. **结构**：team topology、graph plasticity、manager-worker / mesh / workflow graph；  
2. **通信**：谁对谁说、说什么、何时说、为什么说；  
3. **适配**：经验怎样固化成 memory / skills / tool improvements；  
4. **治理**：tool authority、memory poisoning、cross-agent manipulation、auditability。

### 3. 评测正在从单一 success rate 扩展到系统级指标

这五篇都反复暗示：只看任务是否完成已经不够。更合理的指标至少包括：

- 任务质量 / 正确率  
- 成本（token、工具调用、时间）  
- 结构复杂度 / 图属性  
- 通信开销与信息冗余  
- 鲁棒性 / 安全性 / 可审计性  
- 长期适应能力（记忆、技能复用、跨任务迁移）

## 对后续综述写作的中文结构建议

如果要把这五篇吸收到项目最终中文综述中，小白建议按下面结构组织：

1. **总览层**：用 `2601.12560` 搭“agentic AI → multi-agent”背景；  
2. **机制层**：用 `2603.22386` 写 workflow/graph 优化；  
3. **通信层**：用 `2602.11583` 写 communication taxonomy；  
4. **进化层**：用 `2512.16301` 写 memory/skills/adaptation；  
5. **治理层**：用 `2603.09002` 写 security/governance；  
6. **最后综合**：提出一个“结构-通信-适配-治理”四维框架。

## 研究 idea（面向后续可做课题）

### Idea 1：结构-通信联合优化的多智能体编排器

**动机**：现有工作常把“工作流结构优化”和“通信设计”分开处理，但 `2603.22386` 与 `2602.11583` 表明它们本质强耦合。  
**核心问题**：能否联合学习/搜索 agent graph 与 communication policy，而非分开设计？  
**可行方法**：

- 上层：搜索 agentic computation graph；
- 下层：对每条边学习“是否通信/何时通信/传什么摘要”；
- verifier 作为额外节点接入图；
- 目标函数联合考虑质量、成本、通信量与鲁棒性。

**潜在价值**：把“多 agent 更强”和“多 agent 更贵”之间的 trade-off 变成可显式优化的问题。

### Idea 2：面向长期任务的 skill-memory co-adaptation multi-agent system

**动机**：`2512.16301` 强调 adaptation 不是只调 agent 参数，还包括 memory 与 skills；这正适合长期运行的 agent 群。  
**核心问题**：多 agent 在长周期项目中，怎样把局部经验沉淀为可重用技能，而不导致记忆污染？  
**可行方法**：

- 每个 agent 保留局部 episodic memory；
- 共享 skill library，但需要 verifier 评估技能是否可推广；
- 技能调用失败时触发回滚与重写；
- 建立 skill provenance 与版本控制。

**潜在价值**：为“会越用越强”的研究 agent 集群提供真正可积累能力的机制。

### Idea 3：安全感知的多智能体工作流编译器

**动机**：`2603.09002` 说明 multi-agent 风险不是附属问题，而是架构内生问题。  
**核心问题**：能否在 workflow 生成时同步编译出权限边界、验证节点和审计点？  
**可行方法**：

- 输入任务需求；
- 自动生成 agent graph；
- 同时给每个节点分配 tool scope、memory scope、approval gate；
- 在高风险边（跨 agent 授权、外部工具调用、共享记忆写入）自动插入 guardrail/verifier。

**潜在价值**：把“先搭系统，再补安全”改成“安全即编排约束”。

### Idea 4：跨范式通信 benchmark（MARL ↔ EL ↔ LLM agents）

**动机**：`2602.11583` 的价值之一，是首次把 MARL、EL、LLM communication 串到同一图景。  
**核心问题**：能否构建一套统一 benchmark，让三类方法在同一任务族上比较？  
**可行方法**：

- 选取共享环境模板；
- 控制 partial observability、通信预算、角色异质性；
- 分别评估 reward、可解释性、zero-shot 迁移、自然语言可读性、通信成本；
- 为 LLM agent 加入 token-budget 约束，便于公平对比。

**潜在价值**：把传统多智能体学习和 LLM 多 agent 社区真正接轨。

### Idea 5：把多智能体评测从“结果评测”推进到“系统评测”

**动机**：五篇综述都在不同角度指出，评测维度需要升级。  
**核心问题**：怎样建立一套可复现实验协议，同时测质量、成本、结构、通信、安全与长期适应？  
**可行方法**：

- 统一记录 execution trace、graph structure、communication log、tool call log；
- 定义 system-level metrics：结构编辑率、冗余通信率、跨 agent 错误传播深度、权限越界率、技能复用成功率；
- 用固定任务集做 multi-run 稳定性评估。

**潜在价值**：帮助领域从“演示型系统”走向“可比较科学研究”。

## 最终结论

如果只保留一句话：**2026 年最新 multi-agent 相关综述的共识，不是“多加几个 agent 就会更强”，而是“必须把结构、通信、适配、治理视作同等重要的一体化系统设计问题”。**

在这五篇中：

- **最适合做总框架**：`2601.12560`  
- **最适合做 workflow 主线**：`2603.22386`  
- **最适合做通信主线**：`2602.11583`  
- **最适合做长期进化/能力积累主线**：`2512.16301`  
- **最适合做风险治理主线**：`2603.09002`

因此，后续项目若要继续推进中文综述与研究设计，小白建议采用：

> **Agentic 架构总览 → 工作流图优化 → 通信机制 → 记忆/技能适配 → 安全治理 → 系统级 benchmark 与新研究方向**

这条路线最容易把“最新五篇综述”的信息真正融合成一个有洞察的中文研究框架。
