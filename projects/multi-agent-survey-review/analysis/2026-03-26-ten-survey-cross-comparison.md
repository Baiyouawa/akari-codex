# 2026-03-26 十篇 multi-agent 综述交叉比较与统一分析框架

## 0. 任务定义与证据边界
本文件服务于计划 `projects/multi-agent-survey-review/plans/交叉比较-10-篇综述的主题覆盖-方法谱系-研究空白与趋势-形成统一分析框架.md`，目标是对当前项目最终入选的 10 篇综述建立**统一口径**的横向比较框架，并给出可复用的多代理抽取模板。

### 0.1 权威样本集
本文件只使用当前项目已经锁定并已下载到本地的 10 篇综述，不混入未入选候选：

| ID | 论文 | 年份 | 直接来源 | 本地 PDF |
|---|---|---:|---|---|
| S1 | Li et al. — *A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges* | 2024 | https://link.springer.com/article/10.1007/s44336-024-00009-2 | `projects/multi-agent-survey-review/literature/pdf/2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf` |
| S2 | Guo et al. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* | 2024 | https://arxiv.org/abs/2402.01680 | `projects/multi-agent-survey-review/literature/pdf/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` |
| S3 | Zhu et al. — *A survey of multi-agent deep reinforcement learning with communication* | 2024 | https://dblp.org/rec/journals/aamas/ZhuDW24 | `projects/multi-agent-survey-review/literature/pdf/2024-zhu-et-al-a-survey-of-multi-agent-deep-reinforcement-learning-with-communication-doi-10.1007-s10458-023-09633-6.pdf` |
| S4 | Chen et al. — *A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application* | 2025 | https://arxiv.org/abs/2412.17481 | `projects/multi-agent-survey-review/literature/pdf/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` |
| S5 | Tran et al. — *Multi-Agent Collaboration Mechanisms: A Survey of LLMs* | 2025 | https://arxiv.org/abs/2501.06322 | `projects/multi-agent-survey-review/literature/pdf/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` |
| S6 | Yan et al. — *Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems* | 2025 | https://arxiv.org/abs/2502.14321 | `projects/multi-agent-survey-review/literature/pdf/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` |
| S7 | Wu et al. — *Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances* | 2025 | https://arxiv.org/abs/2502.16804 | `projects/multi-agent-survey-review/literature/pdf/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` |
| S8 | Jin et al. — *A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives* | 2025 | https://arxiv.org/abs/2503.13415 | `projects/multi-agent-survey-review/literature/pdf/2025-misc-a-comprehensive-survey-on-multi-agent-cooperative-decision-making-scenarios-approaches-challenges-and-perspectives-arxiv-2503.13415.pdf` |
| S9 | Lin et al. — *Creativity in LLM-based Multi-Agent Systems: A Survey* | 2025 | https://arxiv.org/abs/2505.21116 | `projects/multi-agent-survey-review/literature/pdf/2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf` |
| S10 | Chen et al. — *The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why — A Survey from MARL to Emergent Language and LLMs* | 2026 | https://arxiv.org/abs/2602.11583 | `projects/multi-agent-survey-review/literature/pdf/2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf` |

### 0.2 证据来源
1. 样本锁定与来源链接：`projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`
2. 逐篇结构化笔记：`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-detailed-reading-notes.md`
3. 本地 PDF 与页数/可读性校验：`projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json`
4. 本地路径清单：`projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-local-paths.md`
5. 当前会话通过 `pypdf.PdfReader` 对 10 篇 PDF 首页/前两页摘要区抽取的文本证据；命令已记录于会话溯源。

### 0.3 证据边界说明
- 本文件优先使用摘要、引言前段、章节总览、既有精读笔记中的结构化结论。
- 对 S3、S8、S9 等此前精读覆盖较浅的论文，本文件仍给出标准化抽取，但结论只下到“摘要级/框架级”，不伪造页码级断言。
- 当某篇综述未明确涉及某一维度时，本文件区分为“未覆盖”与“不是主轴但有提及”，避免把“未强调”误写为“真实研究空白”。

---

## 1. 统一编码手册（供多代理并行抽取）

### 1.1 核心维度与取值规则

| 维度 | 定义 | 允许取值/编码 | 记录规则 | 歧义处理 |
|---|---|---|---|---|
| 主题覆盖 | 综述讨论的研究主题面 | `H`=重点覆盖，`M`=中等覆盖，`L`=边缘提及，`0`=未覆盖 | 必须基于摘要、目录或主章节 | 若只在挑战/未来工作中一笔带过，记 `L` |
| 方法谱系主轴 | 综述如何组织方法分类 | 工作流、组件、协作结构、通信、场景、决策方法、创造流程、治理对齐、跨范式理论 | 记录“原文主轴”+“统一归并主轴” | 若论文混合多种主轴，保留前两位 |
| 研究对象 | 论文针对哪类 MAS | 通用 LLM-MAS、MARL 通信、协同决策 MAS、垂直领域 MAS、创造型 MAS、跨范式通信 | 用一句摘要级定义 | 若对象跨多类，以题目/摘要第一句优先 |
| 评价维度 | 综述显式强调的评测/benchmark 维度 | 任务质量、通信效率、协作稳定性、成本时延、安全治理、创造性、角色一致性、场景真实性 | 至少列 1-3 个 | 若仅泛称 benchmark，标注为“任务质量（泛）” |
| 应用场景 | 综述关注的任务或领域 | 通用问题求解、场景仿真、自动驾驶、灾害/无人机/军事、创意生成、社会交互等 | 只记摘要/目录可证实的场景 | 过泛的“real-world”不单独编码 |
| 数据/基准 | 综述提到的数据集或 benchmark 族群 | 通用能力型、交互型、通信专项型、垂直场景型、系统级复合型 | 允许记“族群”而非穷举列表 | 若只有“datasets and benchmarks”字样但无清单，记族群而非具体名 |
| 研究空白 | 作者显式提出或跨篇对照可归纳的不足 | taxonomy 缺失、benchmark 缺失、成本/安全不足、场景落地不足、通信/工作流割裂、治理不足等 | 标记“显式空白/跨篇归纳空白” | 不得把单篇未提到的内容直接当真实空白 |
| 趋势判断 | 论文对未来方向的判断 | 已发生趋势、正在形成趋势、作者预测 | 必须注明依据类型 | 若只是 challenge，不自动升级为趋势 |
| 证据定位 | 本条目主要依据 | `摘要` / `引言前段` / `精读笔记` / `PDF首页抽取` | 每行至少一种 | 不足时回退到 selection 文件 |

### 1.2 统一主题词表

| 统一主题 | 同义/变体表述 | 归并规则 |
|---|---|---|
| 工作流编排 | workflow, orchestration, pipeline, graph, runtime | 只要核心关注任务流、控制流或执行图，归入“工作流编排” |
| 协作结构 | collaboration mechanism, coordination structure, organization, topology | 若强调角色关系与组织结构，归入“协作结构” |
| 通信机制 | communication, protocol, message passing, multi-agent communication | 只要核心问题是消息、通信对象、时机、内容，归入“通信机制” |
| 决策方法 | rule-based, game theory, evolutionary, MARL, cooperative decision-making | 只要聚焦多主体决策范式，归入“决策方法” |
| 垂直应用 | autonomous driving, domain-specific scenarios, industrial settings | 面向明确行业/场景的综述归入“垂直应用” |
| 创造性协作 | creativity, persona, divergent exploration, collaborative synthesis | 关注创意生成与开放式协作的归入“创造性协作” |
| 治理与对齐 | value alignment, safety, governance, trustworthiness | 聚焦价值、规范、治理框架的归入“治理与对齐” |
| 跨范式统一理论 | Five Ws, bridge MARL/EL/LLM, unified taxonomy | 目标是打通不同研究传统的归入“统一理论” |

### 1.3 真实空白 vs 综述未覆盖

| 类型 | 定义 | 判断标准 | 例子 |
|---|---|---|---|
| 真实研究空白 | 多篇综述共同指出该问题尚缺方法/benchmark/理论 | 至少两篇独立综述显式指出，或跨篇对照后呈现系统缺口 | 缺统一 multi-agent 系统级 benchmark |
| 综述视角局限 | 某篇因主题聚焦而未展开，不代表领域没有研究 | 其他综述已有专章或系统覆盖 | 创造力综述未展开自动驾驶，不算自动驾驶空白 |
| 时间滞后空白 | 早期综述未覆盖新议题，主要因时间点早 | 后续年份综述已补上 | 2024 总览未系统覆盖 Five Ws |
| 证据不足空白 | 被提出为方向，但缺清晰实验协议或数据支持 | 文中只有展望，没有成熟评测 | communication efficiency benchmarking |
| 落地不足空白 | 理论存在，但真实高风险部署验证不足 | 综述反复提 deployment/safety constraints | 自动驾驶、治理落地 |

---

## 2. 十篇综述标准化抽取总表

> 说明：本表为统一模板抽取层，服务 AC-1/AC-3。每条结论至少可追溯到 selection 文件、精读笔记或 PDF 摘要区。

| ID | 年份 | 研究对象 | 原文主分类轴 | 统一归并主轴 | 应用/场景重点 | 评价/benchmark 重点 | 作者显式或可直接读取的主要挑战 | 趋势判断 | 证据定位 |
|---|---:|---|---|---|---|---|---|---|---|
| S1 | 2024 | 通用 LLM-MAS | `profile / perception / self-action / mutual interaction / evolution` | 工作流编排 + 系统组件 | 复杂任务、工业工程、科学实验、embodied、game、societal simulation | 任务质量、系统组件完整性、早期 benchmark 汇总 | 缺系统化综合、需明确结构与挑战 | 已发生：从单 agent 走向 workflow 化 MAS | S1 PDF 摘要；`analysis/2026-03-26-ten-survey-detailed-reading-notes.md` |
| S2 | 2024 | 通用 LLM-MAS | components + applications + challenges | 系统组件 + 应用总览 | problem solving、world simulation、dialogue data generation | 通用任务 benchmark + 交互 benchmark | communication、management、capacity growth、benchmark 组织 | 已发生：多 agent 成为复杂问题求解与世界模拟载体 | S2 PDF 摘要；精读笔记 |
| S3 | 2024 | MARL 通信 | 9 communication dimensions | 决策方法 + 通信机制 | autonomous driving、sensor networks、robotics、game playing | learning performance、partial observability、non-stationarity 缓解 | 缺系统性分类，Comm-MADRL 维度组合仍未穷尽 | 已发生：通信被视为 MARL 的关键机制 | S3 PDF 摘要首页 |
| S4 | 2025 | LLM-MAS 应用前沿 | solving complex tasks / simulating scenarios / evaluating generative agents | 应用场景 + 系统组件 | 复杂任务、特定场景仿真、生成式 agent 评测 | 任务质量、系统行为评测、agent-specific benchmark | 既有综述难跟上新工作，交互挑战与应用前沿快速扩张 | 正在形成：评测对象从答案转向系统行为 | S4 PDF 摘要；精读笔记 |
| S5 | 2025 | LLM-MAS 协作机制 | actors / types / structures / strategies / coordination protocols | 协作结构 | 5G/6G、Industry 5.0、QA/NLG、社会文化场景 | 结构差异、协作效果、协议质量 | collaboration 机制仍需统一框架；需面向复杂真实任务扩展 | 已发生：从 isolated models 转向 collaboration-centric approaches | S5 PDF 摘要首页 |
| S6 | 2025 | communication-centric LLM-MAS | system-level comm + internal comm | 通信机制 | 通用 LLM-MAS 场景 | communication efficiency、security、benchmarking、scalability | 效率、安全漏洞、benchmark 不足、可扩展性 | 正在形成：communication 从附属模块升级为中心变量 | S6 PDF 摘要与图 1 文字；精读笔记 |
| S7 | 2025 | 自动驾驶 LLM-MAS | 按 agent interaction modes 分类 | 垂直应用 + 协作/通信 | 多车、多路侧、多助手、人机交互 | 资源、数据集、挑战、协同感知/决策 | limited perception、insufficient collaboration、high computational demands | 已发生：语言驱动协作进入高风险场景 | S7 PDF 摘要与 Figure 1 说明；精读笔记 |
| S8 | 2025 | 协同决策 MAS | 场景/平台/任务形式/奖励分配/方法类型 | 决策方法 + 场景平台 | 自动驾驶、无人机、灾害救援、军事对抗 | simulation environments、reward allocation、方法分类 | 方法虽多，但真实协同挑战与场景复杂性仍高 | 已发生：从规则/博弈走向 MARL + LLM 混合综述 | S8 PDF 摘要首页 |
| S9 | 2025 | 创造性 LLM-MAS | proactivity/persona + generation techniques + evaluation | 创造性协作 | 文本/图像创意任务 | 创造性指标、human/objective evaluation、统一 benchmark 缺失 | 标准不一致、偏见缓解不足、协调冲突、缺统一 benchmark | 正在形成：creative MAS 从案例走向标准化 | S9 PDF 摘要与 Figure 1 说明 |
| S10 | 2026 | 跨 MARL/EL/LLM 的多智能体通信 | Who / Whom / When / What / Why | 跨范式统一理论 + 通信机制 | real-world sequential decision-making、autonomous vehicles、robotics、AI assistants | coordination、uncertainty reduction、跨范式比较 | task-specific/弱解释协议、grounding/generalization/scalability 难题 | 已发生+预测：以 5W 统一多代理通信研究 | S10 PDF 摘要首页 |

---

## 3. 主题覆盖交叉矩阵

### 3.1 主题覆盖定义
- `H`：以该主题为全文主轴。
- `M`：有独立章节或贯穿多节，但不是唯一主轴。
- `L`：边缘提及、通常在挑战或案例中出现。
- `0`：当前证据范围内未见实质覆盖。

### 3.2 交叉矩阵

| 主题 \ 综述 | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 通用系统框架 | H | H | 0 | M | M | L | L | M | L | L |
| 工作流/编排 | H | M | 0 | M | M | L | M | L | M | L |
| 协作结构 | M | M | M | M | H | M | H | M | M | M |
| 通信机制 | M | H | H | M | H | H | H | M | L | H |
| 决策方法谱系 | L | L | H | L | M | L | M | H | L | M |
| 应用场景总览 | M | M | M | H | M | L | H | H | M | L |
| benchmark / evaluation | M | M | M | H | M | H | H | M | H | M |
| 安全/治理/对齐 | L | L | L | L | M | M | H | M | L | L |
| 创造性/开放式生成 | 0 | 0 | 0 | L | L | 0 | 0 | 0 | H | 0 |
| 跨范式统一理论 | 0 | 0 | M | 0 | 0 | M | 0 | M | 0 | H |

### 3.3 从矩阵读出的覆盖规律
1. **通用框架主导 2024 年早期综述**：S1、S2 强，S4 补应用。
2. **通信是十篇中最强交叉主题**：S2/S3/S5/S6/S7/S10 全部高强度涉及。
3. **场景化加深在 2025 年明显增加**：S4、S7、S8、S9 比 2024 样本更强调具体领域。
4. **治理与对齐覆盖仍偏弱**：只有 S7、S8、S6 有中高强度提及，说明这是一个真实薄弱面。
5. **创造性与开放式任务是稀缺但重要支线**：只有 S9 以该主题为核心。

---

## 4. 方法谱系归并：从原文 taxonomy 到统一方法树

### 4.1 统一方法树

```text
Multi-Agent Survey Method Tree
├─ A. 系统构造视角
│  ├─ A1. 工作流/执行流（S1, S2）
│  ├─ A2. 架构/记忆/规划框架（可由 S1/S2/S4 间接支持）
│  └─ A3. 应用系统构成（S4, S7）
├─ B. 组织协作视角
│  ├─ B1. actors / roles / relation types（S5）
│  ├─ B2. structures / topology / coordination（S5）
│  └─ B3. 人机/车路/多主体交互（S7）
├─ C. 通信视角
│  ├─ C1. Comm-MADRL 维度（S3）
│  ├─ C2. system-level / internal communication（S6）
│  └─ C3. Five Ws（S10）
├─ D. 决策与算法视角
│  ├─ D1. rule-based
│  ├─ D2. game theory
│  ├─ D3. evolutionary algorithms
│  ├─ D4. MARL
│  └─ D5. LLM reasoning / agentic methods（S8）
├─ E. 场景任务视角
│  ├─ E1. 复杂任务求解（S4）
│  ├─ E2. 场景仿真/社会系统（S4）
│  ├─ E3. 自动驾驶（S7）
│  └─ E4. 创造性生成（S9）
└─ F. 治理与统一理论视角
   ├─ F1. benchmark/evaluation（S4/S6/S9）
   ├─ F2. safety & deployment（S6/S7/S8）
   └─ F3. unified cross-paradigm communication theory（S10）
```

### 4.2 异名同义、同名异义与上下位关系

| 原文术语 | 来自 | 统一映射 | 关系说明 |
|---|---|---|---|
| workflow | S1 | 工作流编排 | 与 orchestration、pipeline 同层 |
| orchestration | S2 | 工作流编排 | 常偏执行控制，但与 workflow 可并表 |
| structures | S5 | 协作结构 | 与 topology、organization 同层 |
| system-level communication architecture | S6 | 通信机制/组织拓扑 | 兼具架构与通信双属性 |
| Who/Whom | S10 | 通信对象与拓扑 | 对 S5 的 actors/structures 做了通信重述 |
| coordination protocols | S5 | 协议层 | 与 S6 的 protocol 是异名同义 |
| communication dimensions | S3 | 通信机制维度 | 属于更早的 MARL 通信分析框架 |
| reward allocation / task formats | S8 | 决策任务设定 | 是决策方法谱系的上游条件，不等于方法本身 |
| proactivity / persona design | S9 | 创造性协作机制 | 属于开放式生成场景下的角色/行为设计 |

### 4.3 统一回答“不同综述如何描述同一方法族”
- **中心化/层级化组织**：S1 用 workflow 阶段暗含，S5 用 centralized/distributed structures 明说，S7 在车-路-人协作中以系统功能角色体现。
- **通信作为核心机制**：S3 从 Comm-MADRL 角度分析，S6 从 communication-centric taxonomy 分析，S10 用 5W 做统一抽象。
- **多主体决策**：S8 用 rule/game/evolution/MARL/LLM 五类方法串联，S3 是其通信子谱系，S10 则从 communication lens 重新组织。
- **开放式多角色协作**：S4 在 generative agents evaluation 中边缘触及，S9 将其提升为 creativity 主轴。

---

## 5. benchmark 与数据集脉络

### 5.1 统一 benchmark 族群

| 族群 | 典型来源综述 | 功能 | 当前缺口 |
|---|---|---|---|
| 通用能力迁移型 | S1, S2, S4 | 测多 agent 是否提升问答/推理/代码质量 | 不是原生 multi-agent benchmark |
| 多主体交互/博弈型 | S2, S4, S5, S10 | 测讨论、协作、对抗、角色互动 | 协议不统一，跨论文难比 |
| 通信专项型 | S3, S6, S10 | 测消息必要性、通信效率、协调收益 | 缺跨 MARL/LLM 通用评测范式 |
| 垂直场景型 | S7, S8, S9 | 测自动驾驶、协同决策、创意任务 | 可迁移性弱，容易 benchmark silo |
| 系统级复合型 | S4, S6 | 测系统行为、工具链、综合执行 | 多数仍缺成本/安全/治理统一口径 |

### 5.2 演化阶段
1. **阶段 A：借用单 agent/通用能力 benchmark**
   - 典型作用：先验证“多 agent 是否比单 agent 更强”。
   - 代表样本：S1、S2 时代的常见做法。
2. **阶段 B：引入角色交互与协作环境 benchmark**
   - 典型作用：测协商、讨论、合作、竞争。
   - 代表样本：S4、S5、部分 S10。
3. **阶段 C：形成通信/场景/创造性专项 benchmark 簇**
   - 典型作用：开始测 communication efficiency、safety、creativity、scenario realism。
   - 代表样本：S6、S7、S9、S10。

### 5.3 benchmark 层面的真实空白
- 缺统一系统级协议：质量、成本、通信效率、安全、对齐未被一体化评估。
- 缺跨范式可比性：MARL communication 与 LLM communication 的评测语言仍不统一。
- 缺高风险真实部署评测：S7 强调了这一点，但跨领域仍薄弱。
- 缺开放式任务标准：S9 明确指出创造性任务 benchmark 不统一。

---

## 6. 研究空白：区分真实缺口与综述未覆盖

### 6.1 真实研究空白（跨篇共同支持）

| 空白 | 依据 | 类型 |
|---|---|---|
| 缺统一 multi-agent 系统级 benchmark | S4/S6/S9 均显式提到 benchmark 不足；S10 也强调跨范式比较困难 | 真实研究空白 |
| 通信研究与工作流/工程研究割裂 | S6/S10 强调 communication；S1/S2/S4 更偏 workflow/应用；二者缺统一接口 | 真实研究空白 |
| 高风险场景部署与治理不足 | S7 强调自动驾驶部署约束；S6 提到 security/scalability；S8 提到现实协同挑战 | 真实研究空白 |
| 跨 MARL / EL / LLM 的共同 taxonomy 缺失 | S3、S10 直接展示了桥接需求；S8 的方法谱系也说明研究传统分裂 | 真实研究空白 |
| 创造性/开放式任务评测标准不统一 | S9 摘要显式指出 inconsistent evaluation standards 与 lack of unified benchmarks | 真实研究空白 |

### 6.2 综述视角局限（不能误判为空白）

| 现象 | 正确解释 |
|---|---|
| S9 不讨论自动驾驶 | 因为 S9 是 creativity 专题，不表示自动驾驶研究空白 |
| S7 不系统讨论 MARL 通信理论 | 因为 S7 是自动驾驶垂直综述，不表示 MARL 通信空白 |
| S1/S2 未覆盖 2026 Five Ws | 主要是时间滞后，不应误判为领域没人研究 |
| S3 不讨论创意生成 | 因为其研究对象是 Comm-MADRL，不代表 creative MAS 不存在 |

### 6.3 研究空白分类法（供后续复用）
1. **理论空白**：缺统一 taxonomy、缺跨范式框架。
2. **评测空白**：缺 benchmark、缺过程指标、缺多目标协议。
3. **系统空白**：communication 与 workflow、memory、tool-use 尚未一体化。
4. **场景空白**：高风险/真实部署验证不足。
5. **治理空白**：安全、权限、价值对齐没有充分嵌入协作协议。
6. **开放任务空白**：创造性、社会性、角色一致性评测仍不稳定。

---

## 7. 趋势、共识、分歧与演化方向

### 7.1 共识
1. **多 agent 的价值不再被解释为“多几个模型”，而是组织与交互设计收益。**
   - 支撑：S1 workflow、S5 collaboration、S6 communication-centric、S10 Five Ws。
2. **通信已经从子模块升级为主变量。**
   - 支撑：S2/S3/S5/S6/S7/S10。
3. **评测正在从静态答案转向系统行为。**
   - 支撑：S4、S6、S7、S9。
4. **开放复杂环境正在替代封闭 demo 场景成为主战场。**
   - 支撑：S4、S7、S8、S9。

### 7.2 分歧
1. **multi-agent 的边界定义不统一**：是“多主体决策系统”还是“多个 LLM 角色工作流”。
2. **方法分类轴不统一**：按工作流、按组件、按协作结构、按通信、按场景、按决策谱系都有人采用。
3. **benchmark 取向不统一**：是沿用通用基准还是自建场景化/通信专项基准。
4. **价值来源判断不统一**：有的认为核心是 communication，有的认为是 organization，有的认为是 decision theory 或 deployment。

### 7.3 时间线演化

| 时段 | 主要问题 | 代表综述 | 演化特征 |
|---|---|---|---|
| 2024 早期 | “LLM-MAS 是什么？” | S1, S2, S3 | 从单 agent 扩展到通用多 agent 架构与 MARL 通信视角 |
| 2025 中期 | “多 agent 靠什么变强？” | S4, S5, S6, S7, S8, S9 | 专题化：应用、协作、通信、垂直场景、创造性 |
| 2026 初期 | “如何统一理论并提升可比性？” | S10 | Five Ws 试图打通 MARL / EL / LLM 三条传统 |

### 7.4 已发生趋势 vs 作者预测
- **已发生趋势**：专题化加深、通信中心化、场景化增强、benchmark 变复杂。
- **正在形成趋势**：系统级复合评测、creative/open-ended MAS 标准化、治理与部署约束前置。
- **作者预测趋势**：统一 taxonomy、跨范式通信理论、可扩展安全协议、高风险真实部署闭环。

---

## 8. 统一分析框架（可复用模板）

### 8.1 框架目标
本框架用于让多个代理并行阅读不同综述后，能产出**可直接汇总**的标准化结果，避免各自用不同分类口径。

### 8.2 输入模板

```markdown
# Survey Extraction Card
- paper_id:
- title:
- year:
- source_url:
- local_pdf_path:
- research_object:
- original_taxonomy_axes:
- unified_axes:
- main_topics:
- application_scenarios:
- benchmark_families:
- explicit_challenges:
- trend_statements:
- evidence_scope: [摘要/引言/目录/精读笔记]
- evidence_snippets:
```

### 8.3 汇总模板

```markdown
# Cross-Survey Merge Row
- paper_id:
- topic_coverage:
  - general_framework:
  - workflow_orchestration:
  - collaboration_structure:
  - communication:
  - decision_method:
  - application:
  - benchmark_eval:
  - safety_alignment:
  - creativity_social:
  - unified_theory:
- taxonomy_mapping:
- gap_type:
- trend_type:
- confidence:
- merge_notes:
```

### 8.4 任务拆分规则
- **按论文分工**：每个代理负责 1-2 篇，填写 `Survey Extraction Card`。
- **按维度复核**：另一组代理横向检查所有卡片中的通信、benchmark、研究空白、趋势编码是否统一。
- **主汇总代理**：只负责归并、冲突处理与形成总表，不重写逐篇笔记。

### 8.5 冲突合并机制

| 冲突类型 | 处理规则 |
|---|---|
| 同一论文被标成不同主轴 | 以题目与摘要第一句优先，其次看目录最高层章节 |
| 同一主题覆盖等级不一致 | 取较保守值，并在 `merge_notes` 记录原因 |
| 某结论只有单篇支持 | 只能写成“单篇观点”，不得升级为跨篇共识 |
| 某空白只是某篇没提到 | 归入“综述未覆盖”，不得标“真实空白” |
| benchmark 名称不统一 | 先映射到 benchmark 族群，再决定是否保留原名 |

### 8.6 适用范围与边界
- **适用**：10 篇综述横向比较、后续增量纳入新综述、multi-agent 集群并行精读。
- **不适用**：单篇深度 review、需要页码级引文的正式投稿版本、跨语言 OCR 质量不稳定时的自动抽取。

---

## 9. 对应验收标准的闭环核对

| 验收项 | 本文件对应位置 |
|---|---|
| AC-1 基础信息归档与可追踪清单 | 第 0 节样本清单；第 2 节标准化抽取总表 |
| AC-2 统一比较维度与编码手册 | 第 1 节 |
| AC-3 10 篇标准化信息抽取 | 第 2 节 |
| AC-4 方法谱系映射与归并规则 | 第 4 节 |
| AC-5 主题覆盖交叉矩阵 | 第 3 节 |
| AC-6 区分真实空白与综述未覆盖 | 第 6 节 |
| AC-7 趋势、共识、分歧、演化方向 | 第 7 节 |
| AC-8 可复用模板支持 multi-agent 并行 | 第 8 节 |
| AC-9 可交付成果完整性 | 本文件 + 计划 progress/self-review/summary + README/TASKS/log 更新 |

---

## 10. 结论
从这 10 篇综述的交叉比较可得一个清晰判断：multi-agent 研究已经从“多模型协作 demo”阶段进入“组织结构、通信机制、决策范式、评测协议与部署治理协同设计”的阶段。最强共识集中在通信重要性、系统组织设计价值、benchmark 正在系统化、复杂开放场景已成为主战场；最明显分歧则在于 multi-agent 的定义边界、总 taxonomy 以及 benchmark 取向。

对后续研究最有价值的，不是再做一篇宽泛综述，而是沿以下方向做增量：
1. 建立统一系统级 benchmark；
2. 打通 communication 与 workflow/runtime 研究；
3. 在高风险场景中把治理与部署约束前置；
4. 为 creative/open-ended MAS 建立更稳健的评价协议；
5. 提出能同时覆盖 MARL、LLM-MAS、垂直应用与开放任务的统一分析语言。

这正是本文件给出的统一分析框架想要支撑的后续工作。