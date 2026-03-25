# 2024-2026 年 multi-agent 相关综述初筛候选清单（含来源链接、年份、标题与摘要）

- Timestamp: 2026-03-26T01:23:42+08:00
- Session: 沙弥香-09-1774459295-5067c4
- Task: 检索 2024-2026 年最新的 multi-agent 相关综述/survey 论文，初筛候选论文并记录来源链接、年份、标题与摘要
- Status: completed

## 方法与来源

1. 读取项目内已有候选与元数据工件：
   - `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
   - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
   - `projects/multi-agent-review-survey/analysis/2026-03-26-five-paper-metadata.md`
2. 读取仓库内既有阅读计划与 PDF 目录，确认当前本地已持有的近期综述 PDF。
3. 使用 `web_search` 和 `web_fetch` 补抓 arXiv 摘要页，补齐可直接用于初筛的“年份、标题、来源链接、摘要”字段。
4. 使用 `curl -L` 下载此前缺失的 3 篇核心综述 PDF，并用 `python3` 复核 `projects/multi-agent-survey/downloads/recent-review-pdfs/` 当前共有 `13` 个 PDF。

## 初筛口径

- **高相关（A）**：直接讨论 multi-agent systems / LLM-based multi-agent systems / multi-agent communication / collaboration / agentic AI 中的多智能体协作。
- **补位（B）**：与 agentic / multi-agent 主线高度相关，但更偏 workflow、安全、memory 或某个领域专题。
- 本文件目标是形成“候选池 + 摘要证据”，不在此步最终锁定 canonical 10 篇。

## 初筛候选表

| 优先级 | 年份 | 标题 | 来源链接 | 摘要证据简述 |
|---|---:|---|---|---|
| A | 2026 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | https://arxiv.org/abs/2603.22386 | survey reviews workflow methods for LLM agents / agentic computation graphs |
| A | 2026 | SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy | https://arxiv.org/abs/2603.22928 | security SoK explicitly covers autonomous multi-agent decision loops |
| A | 2026 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | https://arxiv.org/abs/2602.11583 | direct survey of multi-agent communication across MARL, EL, LLMs |
| B | 2026 | Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents | https://arxiv.org/abs/2602.04813 | domain taxonomy; abstract notes multi-agent design dominant in healthcare agent papers |
| A | 2026 | Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents | https://arxiv.org/abs/2601.12560 | unified taxonomy covering hierarchical multi-agent systems |
| C | 2026 | LLM Agents in Law: Taxonomy, Applications, and Challenges | https://arxiv.org/abs/2601.06216 | domain survey on legal agents |
| C | 2026 | Agentic AI in Remote Sensing: Foundations, Taxonomy, and Emerging Systems | https://arxiv.org/abs/2601.01891 | domain survey distinguishing single-agent copilots and multi-agent systems |
| B | 2025 | Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills | https://arxiv.org/abs/2512.16301 | broad agent adaptation survey, useful as surrounding context |
| A | 2025 | SoK: Trust-Authorization Mismatch in LLM Agent Interactions | https://arxiv.org/abs/2512.06914 | SoK over 200 papers on agent security and interaction trust mismatch |
| A | 2025 | Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions | https://arxiv.org/abs/2512.02682 | taxonomy focused on collective/system-level risks in LLM-to-LLM ecosystems |
| A | 2025 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | https://arxiv.org/abs/2501.06322 | direct survey of LLM-based MAS collaboration mechanisms |
| A | 2024 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | https://arxiv.org/abs/2412.17481 | direct LLM-MAS application survey |
| A | 2024 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | https://arxiv.org/abs/2402.01680 | early broad survey of LLM-based multi-agent systems |

## 逐篇记录：标题、年份、来源、摘要

### 1) Large Language Model based Multi-Agents: A Survey of Progress and Challenges
- 年份：2024
- 来源链接：https://arxiv.org/abs/2402.01680
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2402.01680.pdf`
- 标题：Large Language Model based Multi-Agents: A Survey of Progress and Challenges
- 摘要：Large Language Models (LLMs) have achieved remarkable success across a wide array of tasks. Due to the impressive planning and reasoning abilities of LLMs, they have been used as autonomous agents to do many tasks automatically. Recently, based on the development of using one LLM as a single planning or decision-making agent, LLM-based multi-agent systems have achieved considerable progress in complex problem-solving and world simulation. To provide the community with an overview of this dynamic field, we present this survey to offer an in-depth discussion on the essential aspects of multi-agent systems based on LLMs, as well as the challenges. Our goal is for readers to gain substantial insights on the following questions: What domains and environments do LLM-based multi-agents simulate? How are these agents profiled and how do they communicate? What mechanisms contribute to the growth of agents' capacities? For those interested in delving into this field of study, we also summarize the commonly used datasets or benchmarks for them to have convenient access. To keep researchers updated on the latest studies, we maintain an open-source GitHub repository, dedicated to outlining the research on LLM-based multi-agent systems.
- 初筛判断：A。可作为 2024 基线总综述。

### 2) A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application
- 年份：2024（arXiv submitted on 2024-12-23；项目内常按 2025 阅读批次使用）
- 来源链接：https://arxiv.org/abs/2412.17481
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2412.17481.pdf`
- 标题：A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application
- 摘要：LLM-based Multi-Agent Systems ( LLM-MAS ) have become a research hotspot since the rise of large language models (LLMs). However, with the continuous influx of new related works, the existing reviews struggle to capture them comprehensively. This paper presents a comprehensive survey of these studies. We first discuss the definition of LLM-MAS, a framework encompassing much of previous work. We provide an overview of the various applications of LLM-MAS in (i) solving complex tasks, (ii) simulating specific scenarios, and (iii) evaluating generative agents. Building on previous studies, we also highlight several challenges and propose future directions for research in this field.
- 初筛判断：A。适合补“应用全景”维度。

### 3) Multi-Agent Collaboration Mechanisms: A Survey of LLMs
- 年份：2025
- 来源链接：https://arxiv.org/abs/2501.06322
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2501.06322.pdf`
- 标题：Multi-Agent Collaboration Mechanisms: A Survey of LLMs
- 摘要：With recent advances in Large Language Models (LLMs), Agentic AI has become phenomenal in real-world applications, moving toward multiple LLM-based agents to perceive, learn, reason, and act collaboratively. These LLM-based Multi-Agent Systems (MASs) enable groups of intelligent agents to coordinate and solve complex tasks collectively at scale, transitioning from isolated models to collaboration-centric approaches. This work provides an extensive survey of the collaborative aspect of MASs and introduces an extensible framework to guide future research. Our framework characterizes collaboration mechanisms based on key dimensions: actors (agents involved), types (e.g., cooperation, competition, or coopetition), structures (e.g., peer-to-peer, centralized, or distributed), strategies (e.g., role-based or model-based), and coordination protocols. Through a review of existing methodologies, our findings serve as a foundation for demystifying and advancing LLM-based MASs toward more intelligent and collaborative solutions for complex, real-world use cases. In addition, various applications of MASs across diverse domains, including 5G/6G networks, Industry 5.0, question answering, and social and cultural settings, are also investigated, demonstrating their wider adoption and broader impacts. Finally, we identify key lessons learned, open challenges, and potential research directions of MASs towards artificial collective intelligence.
- 初筛判断：A。与项目主线最贴近的协作机制综述之一。

### 4) Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions
- 年份：2025
- 来源链接：https://arxiv.org/abs/2512.02682
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2512.02682.pdf`
- 标题：Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions
- 摘要：This paper examines why safety mechanisms designed for human-model interaction do not scale to environments where large language models (LLMs) interact with each other. Most current governance practices still rely on single-agent safety containment, prompts, fine-tuning, and moderation layers that constrain individual model behavior but leave the dynamics of multi-model interaction ungoverned. These mechanisms assume a dyadic setting: one model responding to one user under stable oversight. Yet research and industrial development are rapidly shifting toward LLM-to-LLM ecosystems, where outputs are recursively reused as inputs across chains of agents. In such systems, local compliance can aggregate into collective failure even when every model is individually aligned. We propose a conceptual transition from model-level safety to system-level safety, introducing the framework of the Emergent Systemic Risk Horizon (ESRH) to formalize how instability arises from interaction structure rather than from isolated misbehavior. The paper contributes (i) a theoretical account of collective risk in interacting LLMs, (ii) a taxonomy connecting micro, meso, and macro-level failure modes, and (iii) a design proposal for InstitutionalAI, an architecture for embedding adaptive oversight within multi-agent systems.
- 初筛判断：A。安全主线的重要综述候选。

### 5) SoK: Trust-Authorization Mismatch in LLM Agent Interactions
- 年份：2025（v2 revised 2026-02）
- 来源链接：https://arxiv.org/abs/2512.06914
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2512.06914.pdf`
- 标题：SoK: Trust-Authorization Mismatch in LLM Agent Interactions
- 摘要：Large Language Models (LLMs) are evolving into autonomous agents capable of executing complex workflows via standardized protocols (e.g., MCP). However, this paradigm shifts control from deterministic code to probabilistic inference, creating a fundamental Trust-Authorization Mismatch: static permissions are structurally decoupled from the agent's fluctuating runtime trustworthiness. In this Systematization of Knowledge (SoK), we survey more than 200 representative papers to categorize the emerging landscape of agent security. We propose the Belief-Intention-Permission (B-I-P) framework as a unifying formal lens. By decomposing agent execution into three distinct stages-Belief Formation, Intent Generation, and Permission Grant-we demonstrate that diverse threats, from prompt injection to tool poisoning, share a common root cause: the desynchronization between dynamic trust states and static authorization boundaries. Using the B-I-P lens, we systematically map existing attacks and defenses and identify critical gaps where current mechanisms fail to bridge this mismatch. Finally, we outline a research agenda for shifting from static Role-Based Access Control (RBAC) to dynamic, risk-adaptive authorization.
- 初筛判断：A。偏安全，但综述广度与方法框架较强。

### 6) Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills
- 年份：2025（v3 revised 2026-03）
- 来源链接：https://arxiv.org/abs/2512.16301
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2512.16301.pdf`
- 标题：Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills
- 摘要：Large language model (LLM) agents are moving beyond prompting alone. ChatGPT marked the rise of general-purpose LLM assistants, DeepSeek showed that on-policy reinforcement learning with verifiable rewards can improve reasoning and tool use, and OpenClaw highlights a newer direction in which agents accumulate persistent memory and reusable skills. Yet the research landscape remains fragmented across post-training, retrieval, memory, and skill systems. This survey studies these developments under a single notion of adaptation: improving an agent, its tools, or their interaction after pretraining. We organize the field with a four-paradigm framework spanning agent adaptation and tool adaptation. On the agent side, A1 (tool-execution-signaled) and A2 (agent-output-signaled) improve the agent itself through supervised fine-tuning, preference optimization, and reinforcement learning with verifiable rewards. On the tool side, T1 (agent-agnostic) provides reusable pre-trained modules any agent can call, while T2 (agent-supervised) uses the agent's outputs to train memory systems, skill libraries, or lightweight subagents. Using this framework, we review post-training methods, adaptive memory architectures, and agent skills; compare their trade-offs in cost, flexibility, and generalization; and summarize evaluation practices across deep research, software development, computer use, and drug discovery. We conclude by outlining open problems in agent-tool co-adaptation, continual learning, safety, and efficient deployment.
- 初筛判断：B。更广义 agent 适配综述，作为多智能体上下文补位。

### 7) Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents
- 年份：2026
- 来源链接：https://arxiv.org/abs/2601.12560
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2601.12560.pdf`
- 标题：Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents
- 摘要：Artificial Intelligence is moving from models that only generate text to Agentic AI, where systems behave as autonomous entities that can perceive, reason, plan, and act. Large Language Models (LLMs) are no longer used only as passive knowledge engines but as cognitive controllers that combine memory, tool use, and feedback from their environment to pursue extended goals. This shift already supports the automation of complex workflows in software engineering, scientific discovery, and web navigation, yet the variety of emerging designs, from simple single loop agents to hierarchical multi agent systems, makes the landscape hard to navigate. In this paper, we investigate architectures and propose a unified taxonomy that breaks agents into Perception, Brain, Planning, Action, Tool Use, and Collaboration. We use this lens to describe the move from linear reasoning procedures to native inference time reasoning models, and the transition from fixed API calls to open standards like the Model Context Protocol (MCP) and Native Computer Use. We also group the environments in which these agents operate, including digital operating systems, embodied robotics, and other specialized domains, and we review current evaluation practices. Finally, we highlight open challenges, such as hallucination in action, infinite loops, and prompt injection, and outline future research directions toward more robust and reliable autonomous systems.
- 初筛判断：A。虽不是纯 multi-agent survey，但 collaboration 维度强，适合主池。

### 8) Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents
- 年份：2026
- 来源链接：https://arxiv.org/abs/2602.04813
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2602.04813.pdf`
- 标题：Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents
- 摘要：Large Language Model (LLM)-based agents that plan, use tools and act has begun to shape healthcare and medicine. Reported studies demonstrate competence on various tasks ranging from EHR analysis and differential diagnosis to treatment planning and research workflows. Yet the literature largely consists of overviews which are either broad surveys or narrow dives into a single capability (e.g., memory, planning, reasoning), leaving healthcare work without a common frame. We address this by reviewing 49 studies using a seven-dimensional taxonomy: Cognitive Capabilities, Knowledge Management, Interaction Patterns, Adaptation & Learning, Safety & Ethics, Framework Typology and Core Tasks & Subtasks with 29 operational sub-dimensions. Using explicit inclusion and exclusion criteria and a labeling rubric (Fully Implemented, Partially Implemented, Not Implemented), we map each study to the taxonomy and report quantitative summaries of capability prevalence and co-occurrence patterns. Our empirical analysis surfaces clear asymmetries. For instance, the External Knowledge Integration sub-dimension under Knowledge Management is commonly realized (~76% Fully Implemented) whereas Event-Triggered Activation sub-dimenison under Interaction Patterns is largely absent (~92% Not Implemented) and Drift Detection & Mitigation sub-dimension under Adaptation & Learning is rare (~98% Not Implemented). Architecturally, Multi-Agent Design sub-dimension under Framework Typology is the dominant pattern (~82% Fully Implemented) while orchestration layers remain mostly partial. Across Core Tasks & Subtasks, information centric capabilities lead e.g., Medical Question Answering & Decision Support and Benchmarking & Simulation, while action and discovery oriented areas such as Treatment Planning & Prescription still show substantial gaps (~59% Not Implemented).
- 初筛判断：B。高质量领域型补位综述。

### 9) The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs
- 年份：2026
- 来源链接：https://arxiv.org/abs/2602.11583
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2602.11583.pdf`
- 标题：The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs
- 摘要：Multi-agent sequential decision-making powers many real-world systems, from autonomous vehicles and robotics to collaborative AI assistants. In dynamic, partially observable environments, communication is often what reduces uncertainty and makes collaboration possible. This survey reviews multi-agent communication (MA-Comm) through the Five Ws: who communicates with whom, what is communicated, when communication occurs, and why communication is beneficial. This framing offers a clean way to connect ideas across otherwise separate research threads. We trace how communication approaches have evolved across three major paradigms. In Multi-Agent Reinforcement Learning (MARL), early methods used hand-designed or implicit protocols, followed by end-to-end learned communication optimized for reward and control. While successful, these protocols are frequently task-specific and hard to interpret, motivating work on Emergent Language (EL), where agents can develop more structured or symbolic communication through interaction. EL methods, however, still struggle with grounding, generalization, and scalability, which has fueled recent interest in large language models (LLMs) that bring natural language priors for reasoning, planning, and collaboration in more open-ended settings. Across MARL, EL, and LLM-based systems, we highlight how different choices shape communication design, where the main trade-offs lie, and what remains unsolved. We distill practical design patterns and open challenges to support future hybrid systems that combine learning, language, and control for scalable and interpretable multi-agent collaboration.
- 初筛判断：A。当前最值得优先精读的核心候选之一。

### 10) Agentic AI in Remote Sensing: Foundations, Taxonomy, and Emerging Systems
- 年份：2026
- 来源链接：https://arxiv.org/abs/2601.01891
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2601.01891.pdf`
- 标题：Agentic AI in Remote Sensing: Foundations, Taxonomy, and Emerging Systems
- 摘要：The paradigm of Earth Observation analysis is shifting from static deep learning models to autonomous agentic AI. Although recent vision foundation models and multimodal large language models advance representation learning, they often lack the sequential planning and active tool orchestration required for complex geospatial workflows. This survey presents the first comprehensive review of agentic AI in remote sensing. We introduce a unified taxonomy distinguishing between single-agent copilots and multi-agent systems while analyzing architectural foundations such as planning mechanisms, retrieval-augmented generation, and memory structures. Furthermore, we review emerging benchmarks that move the evaluation from pixel-level accuracy to trajectory-aware reasoning correctness. By critically examining limitations in grounding, safety, and orchestration, this work outlines a strategic roadmap for the development of robust, autonomous geospatial intelligence.
- 初筛判断：C。领域综述，可作边界样本。

### 11) LLM Agents in Law: Taxonomy, Applications, and Challenges
- 年份：2026
- 来源链接：https://arxiv.org/abs/2601.06216
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2601.06216.pdf`
- 标题：LLM Agents in Law: Taxonomy, Applications, and Challenges
- 摘要：Large language models (LLMs) have precipitated a dramatic improvement in the legal domain, yet the deployment of standalone models faces significant limitations regarding hallucination, outdated information, and verifiability. Recently, LLM agents have attracted significant attention as a solution to these challenges, utilizing advanced capabilities such as planning, memory, and tool usage to meet the rigorous standards of legal practice. In this paper, we present a comprehensive survey of LLM agents for legal tasks, analyzing how these architectures bridge the gap between technical capabilities and domain-specific needs. Our major contributions include: (1) systematically analyzing the technical transition from standard legal LLMs to legal agents; (2) presenting a structured taxonomy of current agent applications across distinct legal practice areas; (3) discussing evaluation methodologies specifically for agentic performance in law; and (4) identifying open challenges and outlining future directions for developing robust and autonomous legal assistants.
- 初筛判断：C。领域型综述，不建议列入主线 5 篇。

### 12) From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents
- 年份：2026
- 来源链接：https://arxiv.org/abs/2603.22386
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2603.22386.pdf`
- 标题：From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents
- 摘要：Large language model (LLM)-based systems are becoming increasingly popular for solving tasks by constructing executable workflows that interleave LLM calls, information retrieval, tool use, code execution, memory updates, and verification. This survey reviews recent methods for designing and optimizing such workflows, which we treat as agentic computation graphs (ACGs). We organize the literature based on when workflow structure is determined, where structure refers to which components or agents are present, how they depend on each other, and how information flows between them. This lens distinguishes static methods, which fix a reusable workflow scaffold before deployment, from dynamic methods, which select, generate, or revise the workflow for a particular run before or during execution. We further organize prior work along three dimensions: when structure is determined, what part of the workflow is optimized, and which evaluation signals guide optimization (e.g., task metrics, verifier signals, preferences, or trace-derived feedback). We also distinguish reusable workflow templates, run-specific realized graphs, and execution traces, separating reusable design choices from the structures actually deployed in a given run and from realized runtime behavior. Finally, we outline a structure-aware evaluation perspective that complements downstream task metrics with graph-level properties, execution cost, robustness, and structural variation across inputs. Our goal is to provide a clear vocabulary, a unified framework for positioning new methods, a more comparable view of existing body of literature, and a more reproducible evaluation standard for future work in workflow optimizations for LLM agents.
- 初筛判断：A。workflow 视角对多智能体系统编排很关键。

### 13) SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy
- 年份：2026
- 来源链接：https://arxiv.org/abs/2603.22928
- 本地 PDF：`projects/multi-agent-survey/downloads/recent-review-pdfs/2603.22928.pdf`
- 标题：SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy
- 摘要：Recent AI systems combine large language models with tools, external knowledge via retrieval-augmented generation (RAG), and even autonomous multi-agent decision loops. This agentic AI paradigm greatly expands capabilities - but also vastly enlarges the attack surface. In this systematization, we map out the trust boundaries and security risks of agentic LLM-based systems. We develop a comprehensive taxonomy of attacks spanning prompt-level injections, knowledge-base poisoning, tool/plug-in exploits, and multi-agent emergent threats. Through a detailed literature review, we synthesize evidence from 2023-2025, including more than 20 peer-reviewed and archival studies, industry reports, and standards. We find that agentic systems introduce new vectors for indirect prompt injection, code execution exploits, RAG index poisoning, and cross-agent manipulation that go beyond traditional AI threats. We define attacker models and threat scenarios, and propose metrics (e.g., Unsafe Action Rate, Privilege Escalation Distance) to evaluate security posture. Our survey examines defenses such as input sanitization, retrieval filters, sandboxes, access control, and "AI guardrails," assessing their effectiveness and pointing out the areas where protection is still lacking. To assist practitioners, we outline defensive controls and provide a phased security checklist for deploying agentic AI (covering design-time hardening, runtime monitoring, and incident response). Finally, we outline open research challenges in secure autonomous AI (robust tool APIs, verifiable agent behavior, supply-chain safeguards) and discuss ethical and responsible disclosure practices. We systematize recent findings to help researchers and engineers understand and mitigate security risks in agentic AI.
- 初筛判断：A。安全视角候选，且直接点名 multi-agent emergent threats。

## 建议优先进入下一轮精读的 5 篇

1. `2602.11583` — The Five Ws of Multi-Agent Communication
2. `2501.06322` — Multi-Agent Collaboration Mechanisms: A Survey of LLMs
3. `2412.17481` — A Survey on LLM-based Multi-Agent System
4. `2402.01680` — Large Language Model based Multi-Agents
5. `2601.12560` — Agentic Artificial Intelligence (AI)

若希望把“安全”作为主线之一，可用以下论文替换第 5 篇或加入扩展阅读：
- `2512.06914`
- `2512.02682`
- `2603.22928`

## 核验结果

- 已补下载 3 篇先前缺失的核心综述：
  - `2402.01680.pdf`
  - `2412.17481.pdf`
  - `2501.06322.pdf`
- 使用 `python3` 复核目录 `projects/multi-agent-survey/downloads/recent-review-pdfs/`，输出：
  - `pdf_count 13`
- 因此本轮用于初筛的 13 篇候选均已具备本地 PDF。

## 结论

1. 已形成一个可追溯的 2024-2026 multi-agent 相关综述初筛候选池，共 `13` 篇，均记录了来源链接、年份、标题与摘要。
2. 其中 `8` 篇可视为与项目主线高度直接相关的 A 类候选；其余为安全、workflow 或领域专题补位。
3. 该工件已满足“初筛候选论文并记录来源链接、年份、标题与摘要”的任务要求，可作为后续最终定稿与中文精读的上游输入。

## Provenance

- 项目内候选工件：
  - `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-five-paper-metadata.md`
- arXiv 摘要页抓取：
  - `web_fetch("https://arxiv.org/abs/2402.01680")`
  - `web_fetch("https://arxiv.org/abs/2412.17481")`
  - `web_fetch("https://arxiv.org/abs/2501.06322")`
  - `web_fetch("https://arxiv.org/abs/2512.02682")`
  - `web_fetch("https://arxiv.org/abs/2512.06914")`
  - `web_fetch("https://arxiv.org/abs/2512.16301")`
  - `web_fetch("https://arxiv.org/abs/2601.01891")`
  - `web_fetch("https://arxiv.org/abs/2601.06216")`
  - `web_fetch("https://arxiv.org/abs/2601.12560")`
  - `web_fetch("https://arxiv.org/abs/2602.04813")`
  - `web_fetch("https://arxiv.org/abs/2602.11583")`
  - `web_fetch("https://arxiv.org/abs/2603.22386")`
  - `web_fetch("https://arxiv.org/abs/2603.22928")`
- PDF 下载命令：
  - `curl -L https://arxiv.org/pdf/2402.01680.pdf -o projects/multi-agent-survey/downloads/recent-review-pdfs/2402.01680.pdf`
  - `curl -L https://arxiv.org/pdf/2412.17481.pdf -o projects/multi-agent-survey/downloads/recent-review-pdfs/2412.17481.pdf`
  - `curl -L https://arxiv.org/pdf/2501.06322.pdf -o projects/multi-agent-survey/downloads/recent-review-pdfs/2501.06322.pdf`
- PDF 数量核验：
  - `python3` over `projects/multi-agent-survey/downloads/recent-review-pdfs/` printed `pdf_count 13`
