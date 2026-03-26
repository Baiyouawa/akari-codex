# 2026-03-26 十篇 cross-reviewed multi-agent / agentic 综述元数据清单（修订版）

- Timestamp: 2026-03-26T00:40:55+08:00
- Session: 灯里-00-1774456784-9d98b8
- Scope: 对当前用于结构化精读、综合报告与 research ideas 的 10 篇论文进行交叉复核，统一 canonical reading set，并修正先前文档间的选文不一致问题。
- Supersedes: 先前同名文件中的 10 篇子集定义；本修订版以 `analysis/2026-03-26-ten-survey-structured-reading-notes.md` 与 `analysis/2026-03-26-ten-survey-research-ideas.md` 实际使用的论文集合为准。

> 2026-03-26 source-of-truth 注记：本文件现为项目**最终唯一** 10 篇清单；`analysis/2026-03-26-high-quality-survey-top10-cross-review.md` 仅保留为比较性审计工件，不再作为 metadata / 精读笔记 / 中文主报告的并列 Top 10 口径。统一决议见 `analysis/2026-03-26-source-of-truth-unification.md`。

## 发现并修正的问题

复核 `analysis/2026-03-26-ten-paper-metadata.md`、`analysis/2026-03-26-ten-survey-structured-reading-notes.md`、`analysis/2026-03-26-ten-survey-synthesis-report.md` 后，发现三份文档引用的 10 篇论文集合不一致：

- 旧元数据/旧综合报告包含：Li 2024、Lin 2025、Zeng 2025
- 结构化精读笔记/research ideas 包含：Xu 2026、Yue 2026、Wang 2026

为避免后续会话在“到底读的是哪 10 篇”上继续漂移，本文件将 canonical reading set 锁定为已被结构化精读笔记实际覆盖、且本地 PDF 已验证可读的如下 10 篇。

## 本地核验命令

```bash
python3 - <<'PY'
from pathlib import Path
from pypdf import PdfReader
from collections import Counter
base=Path('projects/multi-agent-review-survey/literature')
selected=[
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
print('selected_count', len(selected))
print('selected_bytes', sum((base/f).stat().st_size for f in selected))
print('year_counts', Counter(f[:4] for f in selected))
for f in selected:
    p=base/f
    print(f'{f}\t{p.stat().st_size}\tpages={len(PdfReader(str(p)).pages)}')
PY
```

本次命令输出：

- `selected_count = 10`
- `selected_bytes = 15684222`
- `year_counts = Counter({'2025': 5, '2026': 4, '2024': 1})`
- 10/10 文件均可被 `pypdf.PdfReader` 打开，页数 `> 0`

## canonical reading set

| 序号 | 题目 | 作者 | 年份 | 来源 | 来源页面 | 本地 PDF 路径 | 页数 |
|---|---|---|---:|---|---|---|---:|
| 1 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | Taicheng Guo; Xiuying Chen; Yaqi Wang; Ruidi Chang; Shichao Pei; Nitesh V. Chawla; Olaf Wiest; Xiangliang Zhang | 2024 | arXiv:2402.01680v2 | https://arxiv.org/abs/2402.01680v2 | `projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | 15 |
| 2 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | R. M. Aratchige; W. M. K. S. Ilmini | 2025 | arXiv:2504.01963v1 | https://arxiv.org/abs/2504.01963v1 | `projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` | 12 |
| 3 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | Shuaihang Chen; Yuanxing Liu; Wei Han; Weinan Zhang; Ting Liu | 2024 | arXiv:2412.17481v2 | https://arxiv.org/abs/2412.17481v2 | `projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | 13 |
| 4 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | Khanh-Tung Tran; Dung Dao; Minh-Duong Nguyen; Quoc-Viet Pham; Barry O'Sullivan; Hoang D. Nguyen | 2025 | arXiv:2501.06322v1 | https://arxiv.org/abs/2501.06322v1 | `projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | 35 |
| 5 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | Yaozu Wu; Dongyuan Li; Yankai Chen; Renhe Jiang; Henry Peng Zou; Wei-Chieh Huang; Yangning Li; Liancheng Fang; Zhen Wang; Philip S. Yu | 2025 | arXiv:2502.16804v2 | https://arxiv.org/abs/2502.16804v2 | `projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | 18 |
| 6 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | Bingyu Yan; Zhibo Zhou; Litian Zhang; Lian Zhang; Ziyi Zhou; Dezhuang Miao; Zhoujun Li; Chaozhuo Li; Xiaoming Zhang | 2025 | arXiv:2502.14321v2 | https://arxiv.org/abs/2502.14321v2 | `projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | 16 |
| 7 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | Haoyuan Xu; Chang Li; Xinyan Ma; Xianhao Ou; Zihan Zhang; Tao He; Xiangyu Liu; Zixiang Wang; Jiafeng Liang; Zheng Chu; Runxuan Liu; Rongchuan Mu; Ming Liu; Bing Qin | 2026 | arXiv:2603.22862v1 | https://arxiv.org/abs/2603.22862v1 | `projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf` | 42 |
| 8 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | Ling Yue; Kushal Raj Bhandari; Ching-Yun Ko; Dhaval Patel; Shuxin Lin; Nianjun Zhou; Jianxi Gao; Pin-Yu Chen; Shaowu Pan | 2026 | arXiv:2603.22386v1 | https://arxiv.org/abs/2603.22386v1 | `projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` | 31 |
| 9 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | Jingdi Chen; Hanqing Yang; Zongjun Liu; Carlee Joe-Wong | 2026 | arXiv:2602.11583v1 | https://arxiv.org/abs/2602.11583v1 | `projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` | 143 |
| 10 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | Ye Wang; Jiaxing Chen; Hongjiang Xiao | 2026 | arXiv:2601.10122v1 | https://arxiv.org/abs/2601.10122v1 | `projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf` | 15 |

## 与其他分析文件的对应关系

该 10 篇与以下文件现在一一对应：

- 结构化精读：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- 综合报告：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
- research ideas：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-research-ideas.md`
- 交叉 review 记录：`projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`

## 结论

本修订版解决了“元数据清单、综合报告、结构化笔记引用的论文集合不一致”这一质量问题；后续若继续扩展或替换论文，应先更新本文件，再联动更新相关分析文档。
