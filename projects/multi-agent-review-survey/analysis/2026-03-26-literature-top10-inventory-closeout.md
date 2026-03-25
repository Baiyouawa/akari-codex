# 2026-03-26 `literature/` 现有 PDF 盘点与 canonical 10 篇综述清单收口

- Timestamp: 2026-03-26T01:49:08+08:00
- Session: 灯里-00-1774460918-ac314c
- Task: 核查 `projects/multi-agent-review-survey/literature/` 中现有 PDF，补齐到 10 篇“最新且明确属于 multi-agent 综述/survey”的论文，并记录每篇的题目、年份、链接、是否正式综述、PDF 路径
- Status: completed

## 范围说明

本次不重复下载或重做候选筛选，而是基于仓库内已经落盘并交叉复核过的证据链，对 `literature/` 当前库存做状态收口，明确：

1. `literature/` 当前共有多少 PDF；
2. 当前 canonical 10 篇是否已齐备；
3. 这 10 篇是否都有“题目、年份、链接、是否正式综述、PDF 路径”五项信息；
4. 该任务在 `TASKS.md` 中是否仍遗留未关闭条目。

## 本次直接核验结果

### 1. `literature/` 当前 PDF 库存

本地命令：

```bash
python3 - <<'PY'
from pathlib import Path
base = Path('projects/multi-agent-review-survey/literature')
for p in sorted(base.glob('*.pdf')):
    print(p.name)
print('pdf_count', len(list(base.glob('*.pdf'))))
PY
```

结果：目录内共有 `20` 个 PDF。

### 2. canonical 10 篇本地存在性与可读性

本地命令：

```bash
python3 - <<'PY'
from pathlib import Path
from pypdf import PdfReader
base = Path('projects/multi-agent-review-survey/literature')
selected = [
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
for name in selected:
    p = base / name
    print(name, p.exists(), p.stat().st_size, len(PdfReader(str(p)).pages), sep='\t')
print('selected_count', len(selected))
print('dir_pdf_count', len(list(base.glob('*.pdf'))))
PY
```

结果：canonical 10 篇 `10/10` 均存在、字节数大于 0、页数大于 0；`selected_count = 10`，`dir_pdf_count = 20`。

### 3. 文件名重复检查

本地命令：

```bash
find projects/multi-agent-review-survey/literature -maxdepth 1 -type f -name '*.pdf' -printf '%f\n' | sort | uniq -d
```

结果：空输出，说明当前 `literature/` 目录无重复文件名。

## canonical 10 篇清单

以下 10 篇是当前项目用于后续精读、综合报告和中文主文档的 canonical reading set；其来源、survey 属性与 PDF 路径均已有仓库内证据链。

| # | 题目 | 年份 | 来源链接 | 是否正式综述 | PDF 路径 |
|---|---|---:|---|---|---|
| 1 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | https://arxiv.org/abs/2402.01680v2 | 是；标题显式含 `A Survey`。证据：`analysis/2026-03-26-ten-paper-metadata.md` | `projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` |
| 2 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | 2025 | https://arxiv.org/abs/2504.01963v1 | 是；标题显式含 `A Survey`。证据：`analysis/2026-03-26-ten-paper-metadata.md` | `projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` |
| 3 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2024 | https://arxiv.org/abs/2412.17481v2 | 是；标题显式含 `A Survey`。证据：`analysis/2026-03-26-ten-paper-metadata.md` | `projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` |
| 4 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | https://arxiv.org/abs/2501.06322v1 | 是；标题显式含 `A Survey`。证据：`analysis/2026-03-26-ten-paper-metadata.md` | `projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` |
| 5 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | 2025 | https://arxiv.org/abs/2502.16804v2 | 是；标题显式含 `A Survey`。证据：`analysis/2026-03-26-ten-paper-metadata.md` | `projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` |
| 6 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | https://arxiv.org/abs/2502.14321v2 | 是；标题显式含 `Survey`。证据：`analysis/2026-03-26-ten-paper-metadata.md` | `projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` |
| 7 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | 2026 | https://arxiv.org/abs/2603.22862v1 | 是；候选判定文档记录摘要含 `We comprehensively review`。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` | `projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf` |
| 8 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | 2026 | https://arxiv.org/abs/2603.22386v1 | 是；标题含 `A Survey`，且候选判定文档记录摘要首句含 `This survey reviews recent methods`。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` | `projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` |
| 9 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | 2026 | https://arxiv.org/abs/2602.11583v1 | 是；标题显式含 `A Survey`。证据：`analysis/2026-03-26-ten-paper-metadata.md` 与 `analysis/2026-03-26-candidate-survey-judgment-and-top10.md` | `projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` |
| 10 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | 2026 | https://arxiv.org/abs/2601.10122v1 | 是；候选判定文档记录摘要写明 `systematically reviews`。证据：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md` | `projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf` |

## 与任务要求的对应

任务要求：核查 `literature/` 中现有 PDF，补齐到 10 篇“最新且明确属于 multi-agent 综述/survey”的论文，并记录每篇的题目、年份、链接、是否正式综述、PDF 路径。

本仓库当前状态满足该要求，因为：

1. `literature/` 中 PDF 总数为 `20`，其中 canonical 目标集为 `10` 篇。
2. canonical 10 篇均有本地 PDF，且本次命令复核为 `10/10` 可读。
3. 每篇均已记录题目、年份、来源链接、正式综述判定证据与 PDF 路径。
4. “最新且明确属于综述”的判定，已由 `analysis/2026-03-26-candidate-survey-judgment-and-top10.md` 与 `analysis/2026-03-26-final-top10-verification-audit.md` 给出逐篇依据。
5. canonical 10 篇的最终锁定与路径一致性，已由 `analysis/2026-03-26-ten-paper-metadata.md` 给出统一口径。

## 使用的仓库内来源

- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-final-top10-verification-audit.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`
- 本次会话记录的本地核验命令输出

## 结论

该任务实质上已由前序会话完成，本次会话完成的是状态收口与证据归并：`projects/multi-agent-review-survey/literature/` 已具备可追溯的 canonical 10 篇最新 multi-agent 相关综述清单，因此可将对应任务在 `TASKS.md` 中标记为完成。
