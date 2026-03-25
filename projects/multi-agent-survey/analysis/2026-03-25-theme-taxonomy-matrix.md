# 2026-03-25 主题分类矩阵（机器可读统计的人工整理视图）

## Scope

本页是对 `projects/multi-agent-survey/analysis/2026-03-25-theme-classification.json` 的人工整理摘要，目的是为后续综述写作直接提供“主题 × venue × 代表论文 × 写作切入点”矩阵。

数据来源严格限制为仓库内已有三份文献清单：

- `projects/multi-agent-survey/literature/icml-2023-2025.md`
- `projects/multi-agent-survey/literature/iclr-2025-2026.md`
- `projects/multi-agent-survey/literature/neurips-2024-2025.md`

机器统计来源：

- `projects/multi-agent-survey/scripts/classify_theme_synthesis.py`
- `projects/multi-agent-survey/analysis/2026-03-25-theme-classification.json`

## Corpus totals

- 总条目数：367
- ICML：83
- ICLR：146
- NeurIPS：138
- Inline arithmetic: `83 + 146 + 138 = 367`

Provenance: `projects/multi-agent-survey/analysis/2026-03-25-theme-classification.json`

## Theme × venue matrix

> 说明：同一论文可命中多个主题，因此各主题计数不可相加为 367。

| 主题 | 总命中数 | ICML | ICLR | NeurIPS | 写作切入点 |
| --- | ---: | ---: | ---: | ---: | --- |
| 协作规划 | 134 | 16 | 57 | 61 | 从 cooperative MARL 过渡到 agentic task planning |
| 通信 | 59 | 6 | 31 | 22 | 从 message passing 到 debate / KV sharing / semantic state sharing |
| 博弈/对齐 | 45 | 16 | 17 | 12 | 从均衡与鲁棒性延伸到价值偏差、攻防与集体对齐 |
| 工具使用 | 14 | 2 | 8 | 4 | 从“协作推理”转向“可执行 workflow” |
| 多智能体LLM系统 | 167 | 54 | 70 | 43 | 当前最强主线，应作为综述主章节 |
| 训练与评测 | 42 | 6 | 20 | 16 | 从 benchmark 扩展到归因、安全与 test-time scaling |

Provenance: `projects/multi-agent-survey/analysis/2026-03-25-theme-classification.json`

## Representative papers by theme

### 1. 协作规划

代表样本（来自 JSON examples 字段与原始清单交叉核对）：

- `Context-Aware Bayesian Network Actor-Critic Methods for Cooperative Multi-Agent Reinforcement Learning` — ICML 2023
- `Multi-Agent Reinforcement Learning with Hierarchical Coordination for Emergency Responder Stationing` — ICML 2024
- `Cross-environment Cooperation Enables Zero-shot Multi-agent Coordination` — ICML 2025
- `Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments` — NeurIPS 2024
- `Agent-Oriented Planning in Multi-Agent Systems` — ICLR inventory, year field absent in source file but venue evidence exists
- `ATLAS: Constraints-Aware Multi-Agent Collaboration for Real-World Travel Planning` — ICLR inventory, year field absent in source file but venue evidence exists

建议写法：先写策略级 coordination，再写任务级 planning / decomposition / topology-aware collaboration。

### 2. 通信

代表样本：

- `Cooperative Multi-Agent Reinforcement Learning: Asynchronous Communication and Linear Function Approximation` — ICML 2023
- `Improving Factuality and Reasoning in Language Models through Multiagent Debate` — ICML 2024
- `Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs` — ICML 2024
- `From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium` — ICML 2025
- `Benefits and Limitations of Communication in Multi-Agent Reasoning` — ICLR inventory
- `KVComm: Enabling Efficient LLM Communication through Selective KV Sharing` — ICLR inventory
- `Multi-Agent Coordination via Multi-Level Communication` — NeurIPS 2024

建议写法：按三层展开——显式消息、语言辩论、内部状态共享。

### 3. 博弈/对齐

代表样本：

- `A Game-Theoretic Framework for Managing Risk in Multi-Agent Systems` — ICML 2023
- `Oracles & Followers: Stackelberg Equilibria in Deep Multi-Agent Reinforcement Learning` — ICML 2023
- `Breaking the Curse of Multiagency in Robust Multi-Agent Reinforcement Learning` — ICML 2025
- `Convex Markov Games: A New Frontier for Multi-Agent Reinforcement Learning` — ICML 2025
- `Aligning Individual and Collective Objectives in Multi-Agent Cooperation` — NeurIPS 2024
- `Secret Collusion among AI Agents: Multi-Agent Deception via Steganography` — NeurIPS 2024

建议写法：把 game-theoretic analysis、robustness/safety、social/value alignment 放进同一“interaction constraints”大节。

### 4. 工具使用

代表样本：

- `AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML` — ICML 2025
- `ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL` — ICLR inventory
- `Self-Evolving Multi-Agent Collaboration Networks for Software Development` — ICLR inventory
- `CoAct-1: Computer-using Multi-agent System with Coding Actions` — ICLR inventory
- `M$^2$-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining` — ICLR inventory
- `MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution` — NeurIPS 2024
- `Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration` — NeurIPS 2024

建议写法：强调 role specialization、environment interface、tool feedback loop 与 workflow orchestration。

### 5. 多智能体LLM系统

代表样本：

- `Scaling Large Language Model-based Multi-Agent Collaboration` — ICLR 2025 high-relevance subset
- `Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration` — ICLR 2026 high-relevance subset
- `Unlocking the Power of Multi-Agent LLM for Reasoning: From Lazy Agents to Deliberation` — ICLR 2026 high-relevance subset
- `MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference` — ICLR 2026 high-relevance subset
- `MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines` — ICML 2025
- `MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems` — ICML 2025
- `Reflective Multi-Agent Collaboration based on Large Language Models` — NeurIPS 2024
- `FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making` — NeurIPS 2024

建议写法：以系统工程为主线，细分为 topology、self-configuration、reasoning enhancement、fault tolerance、domain applications。

### 6. 训练与评测

代表样本：

- `FightLadder: A Benchmark for Competitive Multi-Agent Reinforcement Learning` — ICML 2024
- `MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems` — ICML 2025
- `Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems` — ICML 2025
- `A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems` — ICLR 2026 high-relevance subset
- `LiveResearchBench: Benchmarking Single- and Multi-Agent Systems for Citation-Grounded Deep Research` — ICLR 2026 high-relevance subset
- `SocialJax: An Evaluation Suite for Multi-agent Reinforcement Learning in Sequential Social Dilemmas` — ICLR 2026 high-relevance subset
- `ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination` — NeurIPS 2024

建议写法：区分 environment benchmark、system benchmark、security benchmark、failure attribution 四类。

## Strongest synthesis claims supported by current repo

1. 当前仓库样本中，“多智能体LLM系统”是命中数最高主题，达到 167。
   - Provenance: `projects/multi-agent-survey/analysis/2026-03-25-theme-classification.json`
2. “协作规划”仍然是第二大主题，达到 134，说明传统 coordination/MARL 线并未消失，而是在与 LLM system 线合流。
   - Provenance: same JSON artifact.
3. ICLR 在六个主题上都给出最高或并列最高的可验证命中数，尤其在协作规划、通信、工具使用、多智能体LLM系统、训练与评测上最突出。
   - Provenance: `venue_theme_counts` in the same JSON artifact.
4. 工具使用只有 14 次命中，数量最少，但其代表论文高度贴近 production-style agent workflow，因此综述价值高于单纯计数占比。
   - Provenance: `theme_counts.工具使用 = 14` in the JSON artifact; representative titles listed above come from the same artifact plus cited source lists.

## Caveats

1. `classify_theme_synthesis.py` 采用标题/标签规则，属于高层归类，不等于精读后 taxonomy。
2. `iclr-2025-2026.md` 的部分条目在脚本解析时缺少 `Year:` 字段，因此 JSON 中一些 ICLR examples 的 `year` 为 `null`；这不影响 venue 级统计，但限制了逐年统计。
3. NeurIPS 目前仍是候选池式 inventory，且仓库内缺少 2023 和更完整的 2025 元数据，因此该矩阵是“当前仓库证据边界内”的综述准备材料，而非最终定稿。
