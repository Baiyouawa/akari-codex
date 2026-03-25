# 2026-03-26 入选 10 篇论文的综述身份证据链核验

- Timestamp: 2026-03-26T01:49:23+08:00
- Session: 沙弥香-01-1774460918-65c44f
- Task: 对每篇论文做证据链核验：至少核对摘要、引言、结论与 survey/review 定位表述，避免把普通论文误判为综述；如遇边界论文，写明保留或剔除理由
- Scope: 仅核验当前 canonical reading set，见 `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`

## 方法与证据来源

本次只使用项目内已落盘 PDF 与既有元数据，不新增外部来源。

### 输入文件

1. `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
2. `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
3. `projects/multi-agent-review-survey/literature/*.pdf`

### 本地核验命令

使用本地 `python3` + `pypdf.PdfReader` 从 PDF 提取文本，检查摘要、引言、结论中是否存在明确的 survey/review/self-positioning 表述。会话内实际执行过的命令包括：

```bash
python3 - <<'PY'
from pathlib import Path
from pypdf import PdfReader
base=Path('projects/multi-agent-review-survey/literature')
files=[
'2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf',
'2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf',
'2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf',
'2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf',
'2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf',
'2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf',
'2026-xu-et-al-tool-use-in-llm-agents.pdf',
'2026-yue-et-al-workflow-optimization-for-llm-agents.pdf',
'2026-chen-et-al-five-ws-of-multi-agent-communication.pdf',
'2026-wang-et-al-role-playing-agents.pdf',
]
for name in files:
    p=base/name
    text='\n'.join((page.extract_text() or '') for page in PdfReader(str(p)).pages)
    print(name, len(text))
PY
```

以及用于定位 `abstract / introduction / conclusion / survey / review` 关键词的 `python3` 检索脚本；相关输出已在本会话工具记录中保留。

## 判定标准

判为“明确综述”需满足以下链条中的多数，且不能出现“明显是新方法论文”的反证：

1. **题名定位**：标题含 `survey` / `review` / `SoK` / `taxonomy`，或等价综述定位。
2. **摘要定位**：摘要明确写 `this survey` / `this review` / `systematically reviews` / `comprehensively review` 等。
3. **引言定位**：引言明确说明本文目的在于综述、梳理、统一、分类既有研究，而非只提出单个新方法。
4. **结论定位**：结论明确回顾“本文综述了什么”，而非只总结作者自己的新系统表现。
5. **结构证据**：全文结构以 taxonomy / categories / challenges / future directions / benchmarks / related surveys 为主，而不是 method + experiments 主导。

### 边界判定规则

若论文不是“通用 multi-agent survey”，但其摘要/引言/结论清楚自称综述，仍可判为“**综述型但边界偏专题**”；是否保留再单独说明。

## 逐篇核验结果

### 1. Guo et al. 2024 — 保留，明确综述

- 文件：`projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf`
- 题名证据：标题直接包含 `A Survey of Progress and Challenges`
- 摘要证据：摘要写明 `we present this survey to offer an in-depth discussion on the essential aspects of multi-agent systems based on LLMs, as well as the challenges`
- 引言证据：引言写明 `an absence of a systematic review to summarize them ... This underscores the significance of our work and serves as the motivation behind presenting this survey paper`
- 结论证据：结论写明 `In this survey, we first systematically review the development of LLM-MA systems`
- 判定：**明确综述**
- 保留理由：摘要、引言、结论三处都把本文定位为对 LLM-based multi-agent systems 的系统综述，而非单一方法论文。

### 2. Aratchige & Ilmini 2025 — 保留，明确综述

- 文件：`projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf`
- 题名证据：标题直接包含 `A Survey on the Technological Aspects ...`
- 摘要证据：摘要首句为 `This survey investigates foundational technologies essential for developing effective ... multi-agent systems`
- 引言证据：引言写明 `This survey aims to address this gap by answering two research questions: What state-of-the-art technologies and approaches are available for LLM multi-agent systems? And, which of these are most effective in practice?`
- 结论证据：结论段标题为 `V. CONCLUSION`，正文写明 `This review has identified core frameworks and methodologies that enhance system effectiveness`
- 判定：**明确综述**
- 保留理由：虽然文本格式偏 IEEE 且自动抽取引言/结论时需要额外匹配，但摘要、引言、结论都明确表明其工作是技术综述。

### 3. Chen et al. 2025 — 保留，明确综述

- 文件：`projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf`
- 题名证据：标题直接包含 `A Survey on LLM-based Multi-Agent System`
- 摘要证据：摘要写明 `This paper presents a comprehensive survey of these studies`
- 引言证据：引言明确对比前人综述，指出 `we provide a new perspective based on previous reviews ... with a focus on recent advancements`
- 结论证据：结论写明 `In this survey, we systematically summarize existing research in the LLM-based Multi-Agent Systems (LLM-MAS) field`
- 判定：**明确综述**
- 保留理由：题名、摘要、结论均为强证据；引言还显式说明与先前综述的关系。

### 4. Tran et al. 2025 — 保留，明确综述

- 文件：`projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf`
- 题名证据：标题直接包含 `A Survey of LLMs`
- 摘要证据：首页摘要段写明 `This work provides an extensive survey of the collaborative aspect of MASs`
- 引言证据：引言说明本文关注 collaboration-centric approaches，并指出 `The convergence of these fields has given rise to LLM-based MASs`
- 结论证据：结论写明 `Through our extensive review of the collaborative aspect of LLM-based MASs, we introduce a structured and extensible framework`
- 判定：**明确综述**
- 保留理由：虽更聚焦 collaboration 机制，但全文自定位为对协作机制的 survey/review，不是新协作算法论文。

### 5. Wu et al. 2025 — 保留，明确综述但偏领域专题

- 文件：`projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf`
- 题名证据：标题直接包含 `A Survey of Recent Advances`
- 摘要证据：摘要写明 `This paper provides a frontier survey of this emerging intersection between NLP and multi-agent ADSs`
- 引言证据：引言先讲 ADS 与 agentic driving 背景，再引出 `LLM-based multi-agent ADSs`
- 结论证据：结论写明 `This paper systematically reviews LLM-based multi-agent ADSs and traces their evolution from single-agent to multi-agent systems`
- 判定：**明确综述，且为专题综述**
- 保留理由：不是通用 multi-agent survey，而是自动驾驶垂直方向的综述；但它明确是 survey，不是普通 ADS 方法论文。
- 边界说明：若目标是“通用 multi-agent 主线综述 top 10”，它有被更通用的 2026 论文替换的风险；但若目标是“multi-agent 相关综述的已读集合”，它仍可保留。

### 6. Yan et al. 2025 — 保留，明确综述

- 文件：`projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf`
- 题名证据：标题直接包含 `A Communication-Centric Survey`
- 摘要证据：摘要写明 `this paper presents a comprehensive survey of LLM-MAS from a communication-centric perspective`
- 引言证据：引言明确指出 `several surveys have appeared ... however, they often provide limited coverage of the communication and coordination workflows among agents`
- 结论证据：结论写明 `In this survey, we have presented a communication-centric framework for understanding LLM-MAS`
- 判定：**明确综述**
- 保留理由：survey 身份非常清楚，且是对 general/domain survey 缺口的回应，而非新通信模型论文。

### 7. Xu et al. 2026 — 保留，边界综述

- 文件：`projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf`
- 题名证据：标题**不含** `survey`，这是边界点
- 摘要证据：摘要写明 `We comprehensively review recent progress in multi-tool LLM agents and analyzes the state of the art in this rapidly developing area`
- 引言证据：引言写明 `This survey is motivated by two gaps in the current literature`
- 结论证据：结论写明 `This survey has reviewed work on multi-tool agents across inference-time planning, training, safety, efficiency, capability completeness, benchmarks, and applications`
- 判定：**综述型边界论文，保留**
- 保留理由：尽管标题不像典型 survey paper，但摘要、引言、结论三处均明确自称 survey/review；全文结构也是 taxonomy + benchmark + challenges + applications。
- 边界说明：它更偏 `LLM agents / multi-tool orchestration`，而不是狭义 `multi-agent systems`。因此它属于“对 agent 集群工程化高度相关的专题综述”，不是最纯粹的 multi-agent 通用综述。

### 8. Yue et al. 2026 — 保留，边界综述

- 文件：`projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf`
- 题名证据：标题直接包含 `A Survey of Workflow Optimization for LLM Agents`
- 摘要证据：摘要写明 `This survey reviews recent methods for designing and optimizing such workflows`
- 引言证据：前言部分以 `Survey Structure` 和 `Conceptual Framework and Taxonomy` 明确展示其综述组织方式
- 结论证据：结论写明 `This survey conceptualizes agentic systems as executable workflows and reviews methods for optimizing them`
- 判定：**综述型边界论文，保留**
- 保留理由：survey 身份明确；虽然对象偏 workflow optimization，而不是 agent 间协作本身，但对 agent 集群设计直接相关。
- 边界说明：若仅接受“直接研究 multi-agent communication/collaboration 的综述”，它会偏题；若接受“multi-agent/agentic AI 关键工程子方向综述”，则应保留。

### 9. Chen et al. 2026 — 保留，明确综述

- 文件：`projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf`
- 题名证据：副标题直接写 `A Survey from MARL to Emergent Language and LLMs`
- 摘要证据：摘要写明 `This paper provides a unified survey of MA-Comm across MARL, EL, and LLM-based multi-agent systems`
- 引言证据：目录与引言前部含 `The Need for a Dedicated Survey`、`Methodology and Scope of the Survey`、`Inclusion and Exclusion Criteria`
- 结论证据：结论写明 `This survey presented a comprehensive overview of multi-agent communication through the unifying lens of the Five Ws`
- 判定：**明确综述**
- 保留理由：survey identity 非常强；还具备 search strategy / inclusion criteria 等方法学章节，是 10 篇里证据链最完整的综述之一。

### 10. Wang et al. 2026 — 保留，边界综述

- 文件：`projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf`
- 题名证据：标题**不含** `survey`，这是边界点
- 摘要证据：摘要写明 `This paper systematically reviews the current development and key technologies of RPLAs`
- 引言证据：引言将 RPLA 定义为持续增长的研究方向，并围绕 character/personality/memory/evaluation 展开综述式背景铺陈
- 结论证据：结论写明 `This paper systematically reviews the research progress and challenges in the field of RPLAs driven by LLMs`
- 判定：**综述型边界论文，保留**
- 保留理由：虽然标题没有 `survey`，但摘要与结论都明确写 `systematically reviews`；全文也按技术路径、数据、评测、未来方向组织。
- 边界说明：它更偏 role-playing agents / social agents；与通用 multi-agent systems 有交叉，但属于主题较窄的专题综述。

## 边界论文汇总

| 论文 | 是否为综述 | 边界原因 | 当前建议 |
|---|---|---|---|
| Wu 2025 | 是 | 自动驾驶垂直领域综述，不是通用 MAS 总览 | 可保留为专题综述；若追求更通用 top 10，可替换 |
| Xu 2026 | 是 | 标题不含 survey，且更偏 multi-tool agents 而非 MAS 主线 | 保留 |
| Yue 2026 | 是 | 更偏 workflow optimization / agentic systems | 保留 |
| Wang 2026 | 是 | 标题不含 survey，且更偏 role-playing/social agents | 保留 |

## 未发现被误判为普通论文的条目

对当前 canonical reading set，本次未发现“标题像方法论文、摘要/引言/结论也没有综述自定位”的条目。也就是说：

- **0/10** 篇被判定为“普通方法论文误入”
- **6/10** 篇为“通用或主线 multi-agent 综述”
- **4/10** 篇为“专题/边界综述，但仍属真正综述”

其中 6 与 4 的划分如下：

- 主线/通用：Guo 2024、Aratchige 2025、Chen 2025、Tran 2025、Yan 2025、Chen 2026
- 边界/专题：Wu 2025、Xu 2026、Yue 2026、Wang 2026

## 对“保留/剔除”的建议口径

如果项目目标是：

1. **“只要是 multi-agent/agentic AI 高相关综述都可读”**
   - 当前 10 篇都可保留。

2. **“必须是最纯粹、最通用的 multi-agent systems 主线综述”**
   - 建议优先考虑替换 `Wu 2025`，其次再视口径讨论 `Xu 2026 / Yue 2026 / Wang 2026`。
   - 该建议与 `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md` 中“Wu 2025 可被更通用 2026 综述替换”的判断一致。

## 结论

本次证据链核验确认：当前 canonical reading set 中 **10/10 篇都属于真正的综述型文献**，没有普通方法论文被误判为 survey。

但这 10 篇并不全是“通用 multi-agent systems 总综述”：其中 `Wu 2025`、`Xu 2026`、`Yue 2026`、`Wang 2026` 更准确地说是 **专题/边界综述**。若后续要进一步收紧名单，应围绕“是否接受专题综述”做选择，而不是围绕“它们是不是综述”做争论。
