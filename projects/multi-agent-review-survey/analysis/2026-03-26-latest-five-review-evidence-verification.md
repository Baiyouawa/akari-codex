# 最新五篇候选综述的证据链核验（multi-agent / agentic AI 方向）

- Session: 日向-03-1774461369-d0939c
- Timestamp: 2026-03-26T01:57:28+08:00
- Scope: 对本地已下载候选综述中的“最新五篇”做综述定位核验；至少核对摘要、引言、结论与 survey/review/SoK 定位表述，避免将普通研究论文误判为综述；如属边界论文，明确保留/剔除理由。
- Candidate pool provenance:
  - `projects/multi-agent-survey/plans/2026-03-26-yui-10-review-reading-plan.json`
  - `projects/multi-agent-survey/downloads/recent-review-pdfs/`
  - `projects/multi-agent-survey/downloads/recent-review-sources/`

## 选择规则

按 `projects/multi-agent-survey/plans/2026-03-26-yui-10-review-reading-plan.json` 中列出的候选综述，取时间上最新的 5 篇：

1. `2603.22928` — *SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy*
2. `2603.22386` — *From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents*
3. `2602.11583` — *The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs*
4. `2602.04813` — *Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents*
5. `2601.12560` — *Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents*

说明：这 5 篇并不都等价于“严格意义上的 multi-agent 综述”。本核验的目标不是强行全部纳入，而是给出**保留 / 边界保留 / 剔除**判断，并写清证据链。

## 结论总表

| arXiv ID | 标题（简写） | 摘要是否自述综述/SoK | 引言是否声明 survey/review 目标 | 结论是否回收综述定位 | 与 multi-agent 的关系 | 判定 |
|---|---|---|---|---|---|---|
| 2603.22928 | Attack Surface of Agentic AI | 是：`In this systematization`、`literature review` | 是：Introduction 说明研究的是 tools/RAG/autonomy/multi-agent loops 的攻击面 | 是：`We systematize this surface` | 相关但更偏 agentic AI 安全 | **边界保留** |
| 2603.22386 | Survey of Workflow Optimization for LLM Agents | 是：摘要直接写 `This survey reviews recent methods` | 是：引言以工作流优化为对象搭建综述问题空间 | 是：`This survey conceptualizes... and reviews methods` | 相关，但主题中心是 LLM agent workflow，不限 multi-agent | **边界保留** |
| 2602.11583 | Five Ws of Multi-Agent Communication | 是：摘要/摘要文件明确写 survey，且指出缺少 dedicated survey | 是：引言有 `The Need for a Dedicated Survey` | 是：结论首句 `This survey presented...` | **直接 multi-agent 核心综述** | **保留** |
| 2602.04813 | Agentic AI in Healthcare & Medicine | 是：摘要写 `We address this by reviewing 49 studies` | 是：Introduction 为领域综述与 taxonomy 搭桥 | 是：Conclusion 回收 taxonomy/survey 贡献 | 与 multi-agent 仅部分重叠，核心是 healthcare agentic AI | **剔除** |
| 2601.12560 | Agentic AI: Architectures, Taxonomies, and Evaluation | 是：摘要写 `review current evaluation practices` | 是：Introduction 以 agentic AI landscape/taxonomy 为综述目标 | 是：Conclusions 总结 taxonomy / evaluation / challenge landscape | 与 multi-agent 有重叠，但主轴是 agentic AI 总论 | **边界保留** |

## 逐篇核验

### 1. `2603.22928` — *SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy*

- Local PDF: `projects/multi-agent-survey/downloads/recent-review-pdfs/2603.22928.pdf`
- Local source: `projects/multi-agent-survey/downloads/recent-review-sources/2603.22928.tar.gz`
- Main TeX evidence file: `sample-sigconf-authordraft.tex`

#### 证据链

- 标题直接标记为 `SoK`。
  - Provenance: `sample-sigconf-authordraft.tex` title: `SoK: The Attack Surface of Agentic AI — Tools, and Autonomy`.
- 摘要明确自述为 systematization / literature review，而非提出单一新方法。
  - Provenance: abstract contains `In this systematization, we map out the trust boundaries and security risks of agentic LLM-based systems.`
  - Provenance: abstract also contains `Through a detailed literature review, we synthesize evidence from 2023–2025...`.
- 引言给出综述范围定义，而不是单一实验任务设定。
  - Provenance: introduction contains `Motivation and scope` and defines the studied class as systems that `(a) use external tools/APIs ... (b) rely on RAG ... and/or (c) exhibit autonomous planning or multi-agent loops`.
- 结论回收的是 taxonomy / systematization / defense synthesis。
  - Provenance: conclusion contains `We systematize this surface via a threat-driven taxonomy...` and summarizes layered defenses rather than reporting one new algorithm’s benchmark gains.

#### 判定

- **判定：边界保留。**
- 原因：它是货真价实的 SoK / 综述型论文，但主题主轴是 **agentic AI attack surface/security**，multi-agent 只是其覆盖范围之一，而非全文唯一中心。因此若目标是“multi-agent 相关最新综述”，可作为**相关综述**纳入；若目标收窄为“multi-agent systems 本体综述”，则不应列为核心 5 篇之一。

### 2. `2603.22386` — *From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents*

- Local PDF: `projects/multi-agent-survey/downloads/recent-review-pdfs/2603.22386.pdf`
- Local source: `projects/multi-agent-survey/downloads/recent-review-sources/2603.22386.tar.gz`
- Main TeX evidence file: `main.tex`

#### 证据链

- 标题直接标记为 `A Survey`。
  - Provenance: `main.tex` title: `From Static Templates to Dynamic Runtime Graphs: \\A Survey of Workflow Optimization for LLM Agents`.
- 摘要明确写出 survey 目标与组织方式。
  - Provenance: abstract contains `This survey reviews recent methods for designing and optimizing such workflows...`.
- 引言讨论的是 workflow 作为研究对象，并搭建 taxonomy，而非单一方法实验。
  - Provenance: introduction defines workflow as an executable organization of `LLM calls, tool use, information retrieval, code execution, memory updates, and verification` and frames the paper as an overview of workflow optimization for LLM-agent systems.
- 结论再次明确其是综述论文。
  - Provenance: conclusion begins `This survey conceptualizes agentic systems as executable workflows and reviews methods for optimizing them.`

#### 判定

- **判定：边界保留。**
- 原因：它无疑是综述，但中心对象是 **LLM agent workflow / agentic computation graph**。其中可能包含 multi-agent workflow，但并不限定于 multi-agent。若我们的选题允许“agentic / multi-agent 邻近综述”，可保留；若要求“multi-agent 为核心对象”，它应降级为外围参考综述。

### 3. `2602.11583` — *The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs*

- Local PDF: `projects/multi-agent-survey/downloads/recent-review-pdfs/2602.11583.pdf`
- Local source: `projects/multi-agent-survey/downloads/recent-review-sources/2602.11583.tar.gz`
- Main TeX evidence files:
  - `main.tex`
  - `0-Abstract.tex`
  - `1-Introduction.tex`
  - `2-Method-Updated.tex`
  - `5-Conclusion.tex`

#### 证据链

- 标题直接标注 `A Survey`，且对象明确是 `Multi-Agent Communication`。
  - Provenance: `main.tex` title: `Learning to Communicate in Multi-Agent Systems: A Survey across Multi-agent Reinforcement Learning, Emergent Language, and Large Language Models`.
- 摘要文件直接写明 survey 目标，并强调“尚无 dedicated survey”。
  - Provenance: `0-Abstract.tex` contains `there is still no dedicated survey that brings together these different lines of work`.
- 引言中存在专门的小节 `The Need for a Dedicated Survey`。
  - Provenance: `1-Introduction.tex` contains subsection text `The Need for a Dedicated Survey` and contrasts this paper with broader MARL reviews.
- 方法部分明确声明采用 systematic literature review methodology。
  - Provenance: `2-Method-Updated.tex` contains `Methodology and Scope of the Survey` and `This survey follows a systematic literature review methodology`.
- 结论首句直接回收 survey 身份。
  - Provenance: `5-Conclusion.tex` begins `This survey presented a comprehensive overview of multi-agent communication...`.

#### 判定

- **判定：保留。**
- 原因：这是 5 篇中证据链最完整、与 multi-agent 主题最直接对齐的一篇。它在标题、摘要、引言、方法、结论五处都明确把自己定位为综述/调查论文，而不是普通方法论文。

### 4. `2602.04813` — *Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents*

- Local PDF: `projects/multi-agent-survey/downloads/recent-review-pdfs/2602.04813.pdf`
- Local source: `projects/multi-agent-survey/downloads/recent-review-sources/2602.04813.tar.gz`
- Main TeX evidence file: `access.tex`

#### 证据链

- 摘要明确是 review/taxonomy 型工作，而非普通方法论文。
  - Provenance: abstract contains `We address this by reviewing 49 studies using a seven-dimensional taxonomy...`.
- 引言建立的是 healthcare & medicine 场景下的 agentic AI 文献组织框架。
  - Provenance: `access.tex` includes `\\section{Introduction}` and the paper title itself already constrains domain to healthcare & medicine.
- 结论回收的是 taxonomy 与评估框架价值。
  - Provenance: `\\section{Conclusion}` exists and the paper closes by summarizing taxonomy-style synthesis rather than a single new model.

#### 判定

- **判定：剔除。**
- 原因：它确实是综述，但属于**医疗场景下的 agentic AI 领域综述**，不是 multi-agent 核心综述。即便其中会涉及多代理/多角色协作，主题中心仍然是 healthcare agentic AI empirical taxonomy。若我们的任务是“multi-agent 相关最新五篇综述”，该文相关性不足，建议从最终核心阅读名单中剔除，放入“领域侧边综述”候补层。

### 5. `2601.12560` — *Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents*

- Local PDF: `projects/multi-agent-survey/downloads/recent-review-pdfs/2601.12560.pdf`
- Local source: `projects/multi-agent-survey/downloads/recent-review-sources/2601.12560.tar.gz`
- Main TeX evidence file: `TAI_template.tex`

#### 证据链

- 虽然标题未直接写 `survey`，但摘要明确写其工作是 landscape-style investigation/review。
  - Provenance: abstract states the landscape is hard to navigate and says the paper investigates architectures/protocols, covers environments, and `review current evaluation practices`.
- 引言定位为对 agentic AI landscape 进行 taxonomy 化整理。
  - Provenance: `TAI_template.tex` includes `\\section{Introduction}` and frames the rise from single-loop agents to `hierarchical multi agent systems` as part of a broader taxonomy problem.
- 结论回收 taxonomy / evaluation / challenge landscape，而非报告单篇方法实验结果。
  - Provenance: `\\section{Conclusions}` exists and summarizes architectures, evaluation, and open challenges.

#### 判定

- **判定：边界保留。**
- 原因：它是标准的综述/综述近邻论文，但主题主轴是 **agentic AI / LLM agents 总体架构、taxonomy、evaluation**。其中包含 multi-agent systems，但并非只聚焦 multi-agent。因此适合作为 multi-agent 综述写作的背景总论，不适合作为“纯 multi-agent 核心综述”唯一依据。

## 保留/剔除后的名单建议

### 建议保留为本轮“multi-agent 相关综述”

1. `2602.11583` — 直接 multi-agent communication survey，**核心保留**。
2. `2603.22928` — agentic AI 安全 SoK，覆盖 multi-agent loops，**边界保留**。
3. `2603.22386` — LLM agent workflow survey，包含多代理工作流，**边界保留**。
4. `2601.12560` — agentic AI 总论综述，含 multi-agent systems，**边界保留**。

### 建议剔除出“核心 5 篇 multi-agent 综述”

- `2602.04813` — 医疗场景 agentic AI 综述；是综述，但不是 multi-agent 主线。

## 本轮核验得到的关键发现

1. **这 5 篇里没有明显“伪装成综述的普通研究论文”。**
   - 证据：5 篇都能在标题、摘要、引言、方法或结论中找到 `survey` / `review` / `SoK` / `systematization` / taxonomy-style literature synthesis 表述。唯一差异在于它们是不是“multi-agent 核心综述”。
2. **真正需要防止的误判，不是“把普通论文误判成综述”，而是“把广义 agentic AI 综述误判成 multi-agent 核心综述”。**
   - 证据：`2603.22928`、`2603.22386`、`2601.12560` 都是综述，但主题外延显著大于 multi-agent；`2602.04813` 甚至主要是垂直领域综述。
3. **目前 5 篇中最稳的核心 multi-agent survey 是 `2602.11583`。**
   - 证据：标题、摘要、引言、方法、结论五处同时成立，且研究对象就是 multi-agent communication。

## 与项目内既有 10 篇核验工件的关系

- 本文件是对“最新五篇候选”的补充核验，聚焦于 `projects/multi-agent-survey/downloads/recent-review-sources/` 这一批本地源文件。
- 项目内已有更大范围的 10 篇 canonical reading set 综述身份证据链核验，见：
  - `projects/multi-agent-review-survey/analysis/2026-03-26-survey-identity-evidence-chain-audit.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
- 本次 5 篇核验的增量价值在于：明确区分“真正综述”与“真正属于 multi-agent 核心主线的综述”这两个不同问题。

## 后续建议

- 若目标是严格完成“multi-agent 相关最新五篇综述”的逐篇详读，下一步应优先把 `2602.11583` 作为核心基线，再从本地 10 篇候选中继续筛掉偏单领域/偏总论的条目，补进更直接的 multi-agent survey。
- 当前 5 篇中，`2602.04813` 更适合作为“领域应用侧综述”候补，不建议继续占用核心 5 篇名额。
- `2603.22928`、`2603.22386`、`2601.12560` 可在最终中文综述中放入“agentic AI 邻近综述”或“边界综述”小节，避免与纯 multi-agent survey 混写。
