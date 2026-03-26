# 2026-03-26 十篇 multi-agent 综述交叉比较

## 背景与证据范围
本文件围绕项目中已经筛定的 10 篇 multi-agent 相关综述，抽取共同趋势、分歧点、研究空白、数据集与 benchmark 脉络、系统设计范式，并为最终中文总报告提供可复用骨架。

### 样本来源
核心样本以 `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md` 为准；该文件给出最终入选 10 篇综述、来源链接与纳入理由。为补足交叉比较所需的摘要级证据，本次还使用以下直接来源：
- Springer 页面：`https://link.springer.com/article/10.1007/s44336-024-00009-2`
- arXiv 页面：`2402.01680`, `2412.17481`, `2501.06322`, `2502.14321`, `2502.16804`, `2503.13415`, `2505.21116`, `2506.09656`, `2602.11583`
- DBLP 页面：`https://dblp.org/rec/journals/aamas/ZhuDW24.html`
- 本地下载清单：`projects/multi-agent-survey-review/literature/meta/download_report.json`
- 已有结构化精读笔记：`projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-detailed-reading-notes.md`

### 证据边界
- 对 10 篇样本的题目、年份、来源、纳入理由，以筛选文件为准。
- 对 Guo 2024、Chen 2024/2025、Tran 2025、Yan 2025、Wu 2025、Chen 2026 的系统层细节，可进一步参考已有精读笔记。
- 对 Zhu 2024、Jin 2025、Lin 2025、Zeng 2025，本次主要使用 arXiv/DBLP 摘要与下载元数据进行交叉归纳，因此部分结论只下到“摘要级/主题级”而不做页码级断言。
- 本文件不把未入选样本混入主比较结论。

## 十篇样本概览

| 编号 | 论文 | 年份 | 主题定位 | 直接来源 |
|---|---|---:|---|---|
| S1 | Li et al. — *A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges* | 2024 | 通用工作流/基础设施综述 | Springer 页面 |
| S2 | Guo et al. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* | 2024 | 通用总览/组件与应用 | arXiv 2402.01680 |
| S3 | Zhu et al. — *A survey of multi-agent deep reinforcement learning with communication* | 2024 | MARL 通信综述 | DBLP + DOI |
| S4 | Chen et al. — *A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application* | 2024/2025 | 应用前沿综述 | arXiv 2412.17481 |
| S5 | Tran et al. — *Multi-Agent Collaboration Mechanisms: A Survey of LLMs* | 2025 | 协作机制综述 | arXiv 2501.06322 |
| S6 | Yan et al. — *Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems* | 2025 | 通信中心综述 | arXiv 2502.14321 |
| S7 | Wu et al. — *Multi-Agent Autonomous Driving Systems with Large Language Models* | 2025 | 自动驾驶垂直应用综述 | arXiv 2502.16804 |
| S8 | Jin et al. — *A Comprehensive Survey on Multi-Agent Cooperative Decision-Making* | 2025 | 协同决策综述，连接规则/博弈/进化/MARL/LLM | arXiv 2503.13415 |
| S9 | Lin et al. — *Creativity in LLM-based Multi-Agent Systems: A Survey* | 2025 | 创造力专题综述 | arXiv 2505.21116 |
| S10 | Chen et al. — *The Five Ws of Multi-Agent Communication* | 2026 | 跨 MARL/EL/LLM 的通信统一框架 | arXiv 2602.11583 |

### 时间分布
- 2024：4 篇（S1, S2, S3, S4）
- 2025：5 篇（S5, S6, S7, S8, S9）
- 2026：1 篇（S10）

该分布来自筛选文件中的最终样本表与年份统计，符合“优先覆盖 2024-2026”的项目要求，但也说明 2026 年可稳定核实的综述仍偏少。[来源：`analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`]

## 统一交叉比较矩阵

| 维度 | S1 工作流基础设施 | S2 通用总览 | S3 MARL通信 | S4 应用前沿 | S5 协作机制 | S6 通信中心 | S7 自动驾驶 | S8 协同决策 | S9 创造力 | S10 5W通信 |
|---|---|---|---|---|---|---|---|---|---|---|
| 研究对象 | LLM-MAS 通用系统 | LLM-MAS 通用系统 | 多智能体 DRL 通信 | LLM-MAS 应用版图 | LLM-MAS 协作机制 | LLM-MAS 通信机制 | ADS 场景下 LLM-MAS | 协同决策 MAS | 创意型 LLM-MAS | MA communication 跨范式 |
| 主分类轴 | workflow 五阶段 | 组件/应用/挑战 | 通信驱动 MARL 方法 | 应用类型 | actors/types/structures/strategies/protocols | architecture/goals/protocols + internal comm | 交互对象与协同任务 | 场景/方法/挑战 | persona/生成流程/评测 | who/whom/when/what/why |
| 是否强调通信 | 中 | 高 | 核心 | 中 | 核心 | 核心 | 高 | 高 | 中 | 核心 |
| 是否强调系统架构 | 核心 | 核心 | 中 | 中 | 高 | 高 | 高 | 中 | 中 | 中 |
| 是否强调评测/benchmark | 中 | 高 | 中 | 高 | 中 | 高 | 高 | 中 | 高 | 高 |
| 是否强调垂直场景 | 低 | 中 | 低 | 高 | 中 | 低 | 核心 | 高 | 核心 | 低 |
| 是否连接传统 MAS/MARL | 弱 | 中 | 核心 | 弱 | 弱 | 中 | 中 | 核心 | 弱 | 核心 |
| 是否讨论安全/治理 | 挑战层讨论 | 挑战层讨论 | 低 | 中 | 中 | 核心挑战之一 | 核心约束之一 | 中 | 偏 bias / standards | 偏可解释性与可扩展性 |
| 典型贡献 | workflow 总骨架 | 早期全景地图 | 传统通信基线 | 应用新前沿 | 协作 taxonomy | communication taxonomy | 高风险场景实例 | 方法谱系横向综述 | 创造力专题首篇综述 | 5W 统一框架 |

矩阵依据：S1-S10 的题目、摘要和已落库精读笔记；其中 S1/S2/S4/S5/S6/S7/S10 可直接由摘要与已有精读记录双重支撑，S3/S8/S9 主要由摘要/DBLP 元数据支撑。

## 共同趋势

### 1. 研究重心从“多 Agent 是否有用”转向“多 Agent 如何组织”
多篇综述不再把 multi-agent 当作简单的 agent 数量扩展，而是把核心问题转成组织机制设计：
- S1 直接按 `profile / perception / self-action / mutual interaction / evolution` 给出工作流骨架。
- S5 明确用 `actors / types / structures / strategies / coordination protocols` 刻画协作机制。
- S6 从 communication-centric 视角重构系统，强调 communication 是能力变量而非附属 prompt。
- S10 用 5W 把通信问题拆解为主体、对象、时机、内容、动机。

共同结论：系统组织、交互拓扑、协调协议正在成为 multi-agent 研究的主变量，而不是底层 LLM 本身。[来源：S1/S5/S6/S10 摘要与 `analysis/2026-03-26-ten-survey-detailed-reading-notes.md`]

### 2. 研究版图正在从通用总览快速转向专题纵深
时间脉络非常明显：
- 2024 年样本（S1-S4）主要解决“这个方向是什么、有哪些组件/应用/挑战”。
- 2025 年样本（S5-S9）开始按协作、通信、自动驾驶、协同决策、创造力等专题深挖。
- 2026 年样本（S10）进一步尝试用跨范式理论框架统一已有通信研究。

这说明领域已经完成从“全景盘点”到“专题机制化”的第一轮迁移。[来源：样本年份统计与各论文标题/摘要]

### 3. 通信成为几乎所有高质量综述的显性主线
虽然不是每篇都以 communication 命名，但大多数综述把 communication 当成协作成败的核心：
- S2 在摘要中将 agent communication 作为关键问题之一。
- S3 直接聚焦 communication-enhanced MARL。
- S5 的协作机制框架中，structure 与 protocol 处于核心位置。
- S6/S10 更是把通信作为唯一主轴。
- S7 自动驾驶场景中强调通过 language-driven communication 缓解感知与协作不足。
- S8 协同决策综述把多主体共同决策建立在任务形式、奖励分配与方法选择之上，本质上也离不开信息共享。

共同结论：多 Agent 的“增益”越来越被解释为通信设计收益，而非纯并行收益。[来源：各摘要；S2/S5/S6/S7/S10 精读笔记]

### 4. benchmark 正在从通用单任务测试转向 agent-specific 评测
S2、S4、S6、S7、S9、S10 都显式讨论 benchmark / evaluation；其总体方向是：
- 早期借用 GSM8K、MMLU、HumanEval、HotpotQA 等通用能力任务；
- 中期出现 ChatArena、CAMEL、RoCoBench、AvalonBench、MultiAgentBench 等更贴近多 Agent 交互的任务；
- 专题综述进一步催生领域化 benchmark，例如自动驾驶、创造力、角色一致性/社交仿真、通信质量评测。

共同结论：multi-agent 评测正在从“任务正确率”走向“系统行为质量、通信效率、协调稳定性、成本与安全”的复合评测。[来源：S2/S4/S6/S7/S9/S10 摘要与精读笔记]

### 5. 研究对象正在从通用问题求解扩展到复杂开放环境
S4 归纳复杂任务、场景仿真和 generative-agent evaluation；S7 指向自动驾驶；S9 指向创意生成；S8 指向灾害救援、无人机导航、军事对抗等协同决策场景。说明领域已从“问答/代码 demo”走向：
- 真实或半真实高风险环境；
- 长时交互环境；
- 社会化或创造性环境；
- 需要协商与组织而非单次输出的环境。

共同结论：开放环境与复杂任务已成为多 Agent 综述中的标准动机，而非边缘应用。[来源：S4/S7/S8/S9 摘要]

## 主要分歧点

### 1. “multi-agent”的边界定义并不统一
- S1/S2/S4 把 LLM-based MAS 看成较宽泛的系统范式，凡是多角色协同、场景仿真、评测主体互动都可纳入。
- S3/S8/S10 明显保留传统 MAS / MARL / sequential decision-making 语境，强调多主体控制、通信与奖励结构。
- S9 把创意生成中的多 persona、多 agent 协同也纳入 MAS。

分歧本质：到底是“多主体决策系统”还是“多个 LLM 角色组成的协作工作流”都算 multi-agent？现有综述并未形成统一口径。

### 2. 方法分类轴不一致：按组件、按通信、按协作关系、按场景，还是按理论问题分解？
- S1/S2：偏组件式、工程式分类。
- S4/S7/S9：偏应用或场景分类。
- S5：按协作关系与组织结构分类。
- S6/S10：按通信问题分解分类。
- S8：按规则/博弈/进化/MARL/LLM 的方法谱系分类。

分歧结果：不同综述之间很难直接拼表，说明该领域尚未形成共识性的“总 taxonomy”。

### 3. 对“多 Agent 价值来源”的判断不同
- S5/S6/S10 倾向于认为价值主要来自协作机制与通信设计。
- S1/S2 更强调系统组件的整体协同，包括角色设定、管理、训练、编排。
- S8 则把优势解释为在不同任务结构下选择合适的决策方法，未把 LLM 通信绝对中心化。
- S7 认为在自动驾驶中，多 Agent 价值首先体现在协同感知、协同决策和多方交互，而不是单纯自然语言协商。

因此，领域内对“真正的瓶颈到底是 communication、organization、decision theory 还是 deployment”并无统一答案。

### 4. 对 benchmark 的态度不同：是复用通用任务，还是新建专项评测？
- S2/S4 较多复用通用推理、代码与问答 benchmark。
- S6/S10 倾向认为 communication 必须有专门 benchmark，否则很难测出真正的系统差异。
- S7/S9 则强调垂直场景 benchmark 的必要性，因为通用任务无法覆盖自动驾驶风险或创造力质量。

分歧本质：是追求跨论文可比的统一基准，还是追求贴近真实任务的专用基准，目前仍未统一。

### 5. 对未来方向的优先级排序不同
- 通用综述优先讲 scalability、efficiency、engineering reproducibility。
- 通信综述优先讲 protocol design、security、interpretability、communication efficiency。
- 垂直综述优先讲 domain safety、deployment constraints、human-in-the-loop。
- 创造力综述优先讲 evaluation inconsistency、bias mitigation、coordination conflict。
- 对齐综述 S9? 更正：对齐专题下载了 Zeng 2025，但不在最终十篇中，因此本文件不将其并入主结论。

说明 multi-agent 并不存在单一“下一步”；不同子社区关注点高度分化。

## 数据集与 benchmark 脉络

### 1. 脉络总览
从十篇综述可归纳出 5 类 benchmark 族群：

1. **通用能力迁移型**：GSM8K、MMLU、HumanEval、HotpotQA、MATH、BIG-bench  
   - 用途：检验多 Agent 是否提升推理、代码、问答能力。  
   - 典型出现：S2、S4，以及已有精读笔记中对 S1/S2 的 benchmark 摘录。  
   - 局限：原生不是 multi-agent benchmark，难测通信效率、组织稳定性。

2. **多 Agent 交互/博弈型**：ChatArena、CAMEL、RoCoBench、AvalonBench、LLMArena、AUCArena、ChatEval、BattleAgentBench  
   - 用途：评估对话协作、竞争/博弈、角色互动与团队行为。  
   - 典型出现：S2、S4、S5、S10。  
   - 局限：任务定义多样，协议不统一；不同论文常各自定制环境。

3. **通信专项型**：MultiAgentBench、GAMA-Bench、RealWorldBench 以及 S10 强调的跨范式 communication benchmarks  
   - 用途：衡量 communication necessity、message quality、coordination benefit。  
   - 典型出现：S6、S10。  
   - 局限：仍缺少跨 MARL / LLM / domain-specific setting 的统一评估协议。

4. **垂直场景型**：Waymo Open Motion Dataset、多 agent autonomous driving datasets、灾害救援/无人机/军事对抗模拟平台、创造力任务中的文本与图像生成数据集  
   - 用途：检验在自动驾驶、协同决策、创造力等复杂场景中的系统表现。  
   - 典型出现：S7、S8、S9。  
   - 局限：强场景依赖，难以与通用 benchmark 横向对比。

5. **系统级复合评测型**：AgentBench、MLAgentBench、ToolBench 等更接近 system behavior 的评测  
   - 用途：从单条答案对错转向复杂系统行为。  
   - 典型出现：S4 以及已有精读笔记横向小结。  
   - 局限：覆盖面还不够广，对 multi-agent 专属变量刻画仍不足。

### 2. benchmark 演化脉络
可粗分为三阶段：

- **阶段 A：借用单 Agent 或通用任务基准**  
  代表：GSM8K、MMLU、HumanEval、HotpotQA。  
  目的：先回答“多 Agent 是否优于单 Agent”。

- **阶段 B：引入交互环境和角色型评测**  
  代表：CAMEL、ChatArena、RoCoBench、AvalonBench、LLMArena。  
  目的：开始测协作、竞争、角色分工、社会互动。

- **阶段 C：形成专项化、系统化基准簇**  
  代表：MultiAgentBench、通信专项 benchmark、自动驾驶专用数据集、创造力评价指标。  
  目的：测 communication、workflow、场景安全、创意质量等更细粒度变量。

### 3. 当前 benchmark 脉络中的共同缺口
- **缺统一协议**：名称多、环境多、口径不统一。
- **缺成本维度**：大多数 benchmark 更重最终质量，较少系统性纳入 token、时延、协作代价。
- **缺安全维度**：高风险场景外，通用评测很少把 failure severity 纳入主指标。
- **缺跨范式可比性**：MARL、LLM-MAS、社会型 agents、创造力 MAS 的 benchmark 体系相互割裂。

## 系统设计范式

基于十篇综述，可以抽取出 6 类高频系统设计范式。

### 范式 A：中心化规划者 + 专家执行者
**定义**：一个 planner / manager 负责任务分解与路由，多个 specialized agents 执行子任务。  
**来源支撑**：S1 的 workflow/基础设施视角、S2 的 agent management、S5 的 centralized structure。  
**优点**：控制清晰、便于审计、适合工程落地。  
**风险**：中心节点成为瓶颈，鲁棒性与扩展性受限。

### 范式 B：点对点协作网络
**定义**：agents 之间直接交换信息、协商并共同收敛。  
**来源支撑**：S5 的 peer-to-peer structures；S6/S10 对通信拓扑的讨论。  
**优点**：去中心化、适合分布式协商。  
**风险**：通信开销大，冲突解决难。

### 范式 C：层级式协作系统
**定义**：高层目标规划、中层协调、低层执行分层组织。  
**来源支撑**：S1 workflow 拆分、S8 协同决策方法谱系、S7 车-路-人多层交互。  
**优点**：适合复杂任务和高风险场景。  
**风险**：层间信息传递失真，调参与评价都更复杂。

### 范式 D：通信驱动型系统
**定义**：系统性能主要由 communication architecture、protocol、content design 决定。  
**来源支撑**：S6 communication-centric taxonomy，S10 Five Ws，S3 MARL communication。  
**优点**：能统一解释协作收益。  
**风险**：容易低估 memory、tool-use、environment coupling 的作用。

### 范式 E：场景化协同决策系统
**定义**：围绕自动驾驶、灾害救援、军事对抗、创意生成等具体任务设计多 Agent 协作。  
**来源支撑**：S7、S8、S9。  
**优点**：贴近真实需求，评测目标明确。  
**风险**：结论可迁移性弱，容易形成 benchmark silo。

### 范式 F：社会化/角色化系统
**定义**：通过 persona、role、memory、motivation 形成稳定多主体行为。  
**来源支撑**：S9 创造力综述中对 agent personas 和 collaborative synthesis 的讨论；S4 对 generative agents evaluation 的强调。  
**优点**：适合创意生成、社交仿真、教育陪伴等开放场景。  
**风险**：评测标准弱，偏差与价值风险更难控。

### 设计维度统一框架
为了让后续报告可复用，本次将系统设计归到 7 个统一维度：
1. **角色组织**：中心化 / 分布式 / 层级式  
2. **协作拓扑**：peer-to-peer / manager-worker / mixed  
3. **通信机制**：自然语言、协议化消息、学习式通信  
4. **规划与控制**：静态流程、动态协商、决策驱动  
5. **记忆与共享状态**：局部记忆、共享黑板、场景状态同步  
6. **环境与工具交互**：纯对话、仿真环境、真实系统接口  
7. **安全与治理**：通信安全、场景安全、成本约束、人类监督  

这个框架综合了 S1/S5/S6/S8/S10 的分类思路，适合作为最终报告中的“统一分类框架”。

## 研究空白

### 空白 1：缺少跨范式统一 taxonomy
**证据**：S1/S2 按组件分类，S5 按协作结构分类，S6/S10 按通信问题分类，S8 按方法谱系分类。  
**为什么重要**：没有统一 taxonomy，就难以建立稳定 benchmark 和可比较实验。  
**可切入方向**：构建一个把 `组织结构 × 通信机制 × 决策方式 × 应用场景` 联结起来的四维 taxonomy。

### 空白 2：缺少统一的多 Agent 系统级 benchmark
**证据**：多篇综述都谈 benchmark，但大多仍停留在局部任务或局部变量；S6 明确指出 inadequate benchmarking，S9 指出 lack of unified benchmarks。  
**为什么重要**：没有统一 benchmark，很难回答“新的协作机制到底比旧机制好在哪里”。  
**可切入方向**：建立同时覆盖质量、成本、通信效率、安全性的复合评测协议。

### 空白 3：通信研究与工程工作流研究仍然割裂
**证据**：S6/S10 强调 communication；S1/S2 强调 workflow / orchestration；两者分类体系基本分开。  
**为什么重要**：现实系统里通信开销与 workflow 结构强耦合，割裂研究会导致局部最优。  
**可切入方向**：研究 communication-aware workflow optimization，把消息频次、消息内容与流程图优化联动起来。

### 空白 4：高风险场景中的安全治理研究不足
**证据**：S7 自动驾驶明确暴露 safety/deployment constraints；S6 也指出 communication security vulnerabilities。  
**为什么重要**：多 Agent 在高风险环境中的 failure mode 比单 Agent 更复杂。  
**可切入方向**：针对自动驾驶、机器人或工业控制建立 failure taxonomy 与 guardrail protocol。

### 空白 5：创造力与社会型 MAS 的评测标准仍弱
**证据**：S9 把 inconsistent evaluation standards、bias mitigation、coordination conflicts 列为核心挑战。  
**为什么重要**：如果没有可靠评测，creative / social MAS 很难进入稳健研究阶段。  
**可切入方向**：构建兼顾 novelty、coherence、diversity、persona consistency 的多维评价体系。

### 空白 6：传统 MARL 与 LLM-MAS 之间的桥接研究仍稀缺
**证据**：S3 从 MARL communication 出发，S10 明确试图连接 MARL、EL、LLM 三条线，说明桥接仍是新问题。  
**为什么重要**：MARL 在控制与训练上成熟，LLM-MAS 在开放语言协作上强；二者融合空间很大。  
**可切入方向**：研究“结构化 learned communication + 自然语言协商”的 hybrid architecture。

## 后续研究 idea 输入

### Idea 1：Communication-aware Workflow Benchmark
- 动机：通信综述与工作流综述之间存在明显断层。
- 问题定义：在相同任务质量目标下，如何共同优化工作流图结构与通信预算？
- 方法设计：构建同一任务的多种 workflow graph；控制消息频次、内容长度、拓扑结构；测质量-成本-时延三维 Pareto 前沿。
- 预期贡献：把 communication efficiency 纳入 workflow optimization 主评价。
- 潜在评测：在通用任务 + 协作任务上统一跑协议化评测。

### Idea 2：Hybrid MARL-LLM Communication Stack
- 动机：S3 与 S10 都表明 MARL 与 LLM communication 各有长短板。
- 问题定义：如何把 learned low-level communication 与 natural-language high-level coordination 结合？
- 方法设计：低层用结构化 latent protocol，高层用 LLM 语言协商；通过层级控制连接。
- 预期贡献：提升可解释性与泛化性，同时保留控制能力。
- 潜在评测：协同导航、灾害救援、自动驾驶仿真。

### Idea 3：Safety-Critical Multi-Agent Audit Protocol
- 动机：自动驾驶综述与通信综述都强调安全，但缺统一审计协议。
- 问题定义：多 Agent 在高风险环境中的失效如何被系统化发现与阻断？
- 方法设计：建立 failure taxonomy，加入消息污染、角色冲突、延迟、错误指挥等扰动。
- 预期贡献：为高风险场景 multi-agent 部署提供可复用安全测试框架。
- 潜在评测：自动驾驶与机器人仿真平台。

### Idea 4：Creative MAS Unified Evaluation Suite
- 动机：S9 指出创造力评测严重碎片化。
- 问题定义：如何同时评价 novelty、diversity、coherence、persona consistency 与 collaboration quality？
- 方法设计：构建文本/图像双模 creative tasks，并引入多裁判 + 行为日志指标。
- 预期贡献：为 creative MAS 提供标准化 benchmark 套件。
- 潜在评测：故事生成、广告创意、图文协同设计。

### Idea 5：General Taxonomy for Agentic Multi-Agent Systems
- 动机：现有十篇综述的分类轴彼此不兼容。
- 问题定义：能否提出一个覆盖传统 MAS、LLM-MAS、social/creative MAS 的统一 taxonomy？
- 方法设计：采用四轴编码：组织结构、通信机制、决策机制、场景压力；用现有十篇综述和代表系统进行编码验证。
- 预期贡献：为后续 benchmark、survey 和系统设计提供共同语言。
- 潜在评测：分类一致性评估 + 新论文映射实验。

## Agent 集群分工与复核机制

本任务并非单线程完成，已有仓库证据显示至少经过以下角色链路：
- **筛选角色**：`岛村-01-1774536172-2db8b0` 完成十篇样本筛选与来源核验，产出 `analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`。[来源：`logs/sessions/fleet-multi-agent-survey-review-b7f90835f37e7feb.jsonl`]
- **精读角色**：`结衣-03-1774536172-ceb168` 完成结构化逐篇精读，产出 `analysis/2026-03-26-ten-survey-detailed-reading-notes.md`。[来源：`logs/sessions/fleet-multi-agent-survey-review-70056d69a5ad291c.jsonl`]
- **交叉比较角色**：本会话 `日向-03-1774537746-870d38` 基于筛选文件、精读文件、下载清单与外部摘要进行横向比较与归纳。

复核机制：
1. 样本范围以筛选文件锁定，避免把未入选论文混入结论。  
2. 结论优先引用已落库文件；本地不足处再用 arXiv/Springer/DBLP 页面补证。  
3. 对无法由现有文件支撑的细节，不下页码级或实验级断言，只下摘要级判断。  

## 结论
十篇综述交叉比较后，可以得到一个较清晰的判断：multi-agent 研究已经从“用多个 LLM 做协作 demo”升级为“如何系统化设计组织结构、通信机制、决策方式与评测协议”的问题。当前最强共识集中在通信重要性、复杂环境需求、评测碎片化与组织设计价值；最明显分歧则在于 multi-agent 的定义边界、总 taxonomy 和 benchmark 取向。若后续要做真正有增量的研究，最值得切入的不是再做一个泛泛综述，而是构建能打通通信、工作流、场景安全与统一评测的新框架。

## 参考链接
- `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md`
- `projects/multi-agent-survey-review/analysis/2026-03-26-ten-survey-detailed-reading-notes.md`
- `projects/multi-agent-survey-review/literature/meta/download_report.json`
- `https://link.springer.com/article/10.1007/s44336-024-00009-2`
- `https://arxiv.org/abs/2402.01680`
- `https://dblp.org/rec/journals/aamas/ZhuDW24.html`
- `https://arxiv.org/abs/2412.17481`
- `https://arxiv.org/abs/2501.06322`
- `https://arxiv.org/abs/2502.14321`
- `https://arxiv.org/abs/2502.16804`
- `https://arxiv.org/abs/2503.13415`
- `https://arxiv.org/abs/2505.21116`
- `https://arxiv.org/abs/2602.11583`
