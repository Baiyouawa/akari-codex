# 2026-03-26 最终 10 篇论文清单（题目 / 年份 / PDF / 入选理由 / 中文摘要入口）

- Timestamp: 2026-03-26T02:25:27+08:00
- Session: 千早-05-1774463081-d98617
- Task: 完成后整理最终清单：10 篇论文题目、年份、PDF 文件名/路径、入选理由、中文摘要入口，确保文档与 `literature/` 文件夹一一对应
- Status: completed

## 目的

本文件只做一件事：把当前项目已经 cross-review 锁定的 canonical 10 篇综述，整理成一个可直接核对的最终清单，并明确给出：

1. 论文题目
2. 年份
3. 本地 PDF 文件名 / 路径
4. 入选理由
5. 中文摘要入口

其中：

- canonical reading set 以 `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md` 为 source of truth；
- PDF 实体存在性与页数，以本次会话运行的 `python3 + pypdf.PdfReader` 核验输出为准；
- 中文摘要入口统一指向 `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 中对应的逐篇精读卡片标题；
- 入选理由依据 `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`、`projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`、`projects/multi-agent-review-survey/analysis/2026-03-26-literature-top10-inventory-closeout.md` 的既有判定，不新增无来源判断。

## 本次核验命令

```bash
python3 - <<'PY'
from pathlib import Path
from pypdf import PdfReader
base = Path('projects/multi-agent-review-survey/literature')
files = [
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
for f in files:
    p=base/f
    print(f"{p}\texists={p.exists()}\tsize={p.stat().st_size if p.exists() else 'NA'}\tpages={len(PdfReader(str(p)).pages) if p.exists() else 'NA'}")
PY
```

核验结果：10/10 文件均存在，字节数大于 0，页数大于 0。直接证据见本次会话 shell 输出，以及既有核验工件 `projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-verification.md`。

## 最终清单

| # | 论文题目 | 年份 | PDF 文件名 | PDF 路径 | 入选理由 | 中文摘要入口 |
|---|---|---:|---|---|---|---|
| 1 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | `2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | `projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | 作为 2024 基线总览综述保留；题目显式含 `A Survey`，用于提供 multi-agent/LLM-MAS 的组件、应用与挑战总图谱。Provenance: `analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-final-top10-verification-audit.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 1：Guo et al. 2024` |
| 2 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | 2025 | `2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` | `projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` | 技术底座导向综述；题目显式含 `A Survey`，覆盖 architecture / memory / planning / frameworks，是 canonical set 中的系统构建主线。 Provenance: `analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-literature-top10-inventory-closeout.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 2：Aratchige & Ilmini 2025` |
| 3 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2024 | `2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | `projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | 应用前沿导向综述；题目显式含 `A Survey`，用于补足复杂任务、仿真与应用场景视角。年份口径以 canonical metadata 的 2024 为准。 Provenance: `analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-final-markdown-cross-review.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 3：Chen et al. 2024` |
| 4 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | `2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | `projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | 协作机制 taxonomy 代表综述；题目显式含 `A Survey`，为 canonical set 提供 actor / relation / structure / protocol 的协作主线。 Provenance: `analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-candidate-survey-judgment-and-top10.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 4：Tran et al. 2025` |
| 5 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | 2025 | `2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | `projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | 垂直高风险场景综述；题目显式含 `A Survey`，当前 canonical set 保留它以覆盖自动驾驶中的多主体协作、部署约束与真实系统压力。 Provenance: `analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-final-top10-verification-audit.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 5：Wu et al. 2025` |
| 6 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | `2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | `projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | 通信中心视角核心综述；标题显式含 `Survey`，是项目里 communication 主线的重要证据节点。 Provenance: `analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-literature-top10-inventory-closeout.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 6：Yan et al. 2025` |
| 7 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | 2026 | `2026-xu-et-al-tool-use-in-llm-agents.pdf` | `projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf` | 2026 工具编排综述；候选判定文档记录摘要含 `We comprehensively review`，因此被认定为真正综述，并用于覆盖 multi-tool orchestration 主线。 Provenance: `analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `analysis/2026-03-26-ten-paper-metadata.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 7：Xu et al. 2026` |
| 8 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | 2026 | `2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` | `projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` | 2026 workflow 优化综述；标题显式含 `A Survey`，并由候选判定文档记录摘要首句 `This survey reviews recent methods`，用于覆盖 runtime graph / workflow optimization 主线。 Provenance: `analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `analysis/2026-03-26-ten-paper-metadata.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 8：Yue et al. 2026` |
| 9 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | 2026 | `2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` | `projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` | 2026 通信理论综述；标题显式含 `A Survey`，并在项目内承担 5W 通信统一框架的核心位置。 Provenance: `analysis/2026-03-26-ten-paper-metadata.md`; `analysis/2026-03-26-candidate-survey-judgment-and-top10.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 9：Chen et al. 2026` |
| 10 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | 2026 | `2026-wang-et-al-role-playing-agents.pdf` | `projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf` | 2026 social / role-playing agents 综述；候选判定文档记录摘要含 `systematically reviews`，用于覆盖社会型 agent、人格与长期互动分支。 Provenance: `analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `analysis/2026-03-26-ten-paper-metadata.md` | `projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` → `### 卡片 10：Wang et al. 2026` |

## 一一对应核验

### 1. 文档行数与 canonical 目标数一致

- 本清单条目数：10
- canonical reading set 条目数：10  
Provenance: `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`

### 2. 本清单 10 个 PDF 路径均在 `literature/` 中存在

本次会话 shell 输出确认 10/10 均满足：

- `exists=True`
- `size>0`
- `pages>0`

### 3. 本清单与中文主报告逐篇卡片一一对应

`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md` 中可检出：

- `### 卡片 1：Guo et al. 2024`
- `### 卡片 2：Aratchige & Ilmini 2025`
- `### 卡片 3：Chen et al. 2024`
- `### 卡片 4：Tran et al. 2025`
- `### 卡片 5：Wu et al. 2025`
- `### 卡片 6：Yan et al. 2025`
- `### 卡片 7：Xu et al. 2026`
- `### 卡片 8：Yue et al. 2026`
- `### 卡片 9：Chen et al. 2026`
- `### 卡片 10：Wang et al. 2026`

因此，本文件中的“中文摘要入口”可直接映射到主报告中的对应卡片。

## 结论

该任务现可判定为完成：项目中已经存在一份与 `literature/` 目标 10 篇 PDF 一一对应的最终清单，并补齐了“入选理由 + 中文摘要入口”两项之前未集中整理的字段。

## Provenance

- canonical 名单与题目 / 年份 / PDF 路径：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- 基础信息与年份分布：`projects/multi-agent-review-survey/analysis/2026-03-26-basic-info-for-10-papers.md`
- survey 判定与 top10 审计：`projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`; `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
- `literature/` 收口盘点：`projects/multi-agent-review-survey/analysis/2026-03-26-literature-top10-inventory-closeout.md`
- 中文主报告：`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`
- PDF 可读性核验：`projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-verification.md`
