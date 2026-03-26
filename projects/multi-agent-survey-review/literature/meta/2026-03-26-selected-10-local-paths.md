# 2026-03-26 十篇综述本地路径清单

来源清单基于 `projects/multi-agent-survey-review/analysis/2026-03-26-latest-10-multi-agent-survey-selection.md` 的最终入选十篇；文件存在性、PDF 头、页数、SHA256 和标题片段由 `python3` + `pypdf.PdfReader` 在 2026-03-26T23:10:48+08:00 本地校验。

| 序号 | 论文标题 | 年份 | 来源链接 | 保存格式 | 本地路径 | exists | readable | 页数 | 大小(bytes) | 备注 |
|---|---|---:|---|---|---|---|---|---:|---:|---|
| 1 | A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | 2024 | https://link.springer.com/article/10.1007/s44336-024-00009-2 | PDF | `projects/multi-agent-survey-review/literature/pdf/2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf` | true | true | 43 | 3482567 | Springer OA PDF |
| 2 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | 2024 | https://arxiv.org/abs/2402.01680 | PDF | `projects/multi-agent-survey-review/literature/pdf/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | true | true | 15 | 1243493 | arXiv PDF |
| 3 | A survey of multi-agent deep reinforcement learning with communication | 2024 | https://dblp.org/rec/journals/aamas/ZhuDW24 | PDF | `projects/multi-agent-survey-review/literature/pdf/2024-zhu-et-al-a-survey-of-multi-agent-deep-reinforcement-learning-with-communication-doi-10.1007-s10458-023-09633-6.pdf` | true | true | 48 | 2154897 | 通过 Springer PDF 直链补齐 |
| 4 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | 2025 | https://arxiv.org/abs/2412.17481 | PDF | `projects/multi-agent-survey-review/literature/pdf/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | true | true | 13 | 404537 | arXiv PDF |
| 5 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | https://arxiv.org/abs/2501.06322 | PDF | `projects/multi-agent-survey-review/literature/pdf/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | true | true | 35 | 2420086 | arXiv PDF |
| 6 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2025 | https://arxiv.org/abs/2502.14321 | PDF | `projects/multi-agent-survey-review/literature/pdf/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | true | true | 16 | 1147688 | arXiv PDF |
| 7 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | 2025 | https://arxiv.org/abs/2502.16804 | PDF | `projects/multi-agent-survey-review/literature/pdf/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | true | true | 18 | 2307367 | arXiv PDF |
| 8 | A Comprehensive Survey on Multi-Agent Cooperative Decision-Making: Scenarios, Approaches, Challenges and Perspectives | 2025 | https://arxiv.org/abs/2503.13415 | PDF | `projects/multi-agent-survey-review/literature/pdf/2025-misc-a-comprehensive-survey-on-multi-agent-cooperative-decision-making-scenarios-approaches-challenges-and-perspectives-arxiv-2503.13415.pdf` | true | true | 54 | 11793042 | 本轮补下载成功 |
| 9 | Creativity in LLM-based Multi-Agent Systems: A Survey | 2025 | https://arxiv.org/abs/2505.21116 | PDF | `projects/multi-agent-survey-review/literature/pdf/2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf` | true | true | 23 | 1461659 | arXiv PDF |
| 10 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | 2026 | https://arxiv.org/abs/2602.11583 | PDF | `projects/multi-agent-survey-review/literature/pdf/2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf` | true | true | 143 | 3848111 | 本轮重新下载修复先前损坏副本 |

## 结论
- 最终十篇均已有本地可读 PDF，无需退化到可读文本替代方案。
- 新补齐的两篇为：
  - `2024-zhu-et-al-a-survey-of-multi-agent-deep-reinforcement-learning-with-communication-doi-10.1007-s10458-023-09633-6.pdf`
  - `2025-misc-a-comprehensive-survey-on-multi-agent-cooperative-decision-making-scenarios-approaches-challenges-and-perspectives-arxiv-2503.13415.pdf`
- 本轮还发现并修复了 `2602.11583` 的本地损坏问题：旧文件一度仅 36864 bytes，重新从 arXiv PDF 直链下载后恢复为 3848111 bytes，并通过 `pypdf` 读取到 143 页。

## 机器可读索引
- `projects/multi-agent-survey-review/literature/meta/2026-03-26-selected-10-download-manifest.json`
- `projects/multi-agent-survey-review/literature/meta/download_report.json`（旧有下载报告，包含此前 10 条记录但与最终入选清单存在偏差，后续应以下述 manifest 为准）
