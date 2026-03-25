# 2026-03-26 literature/ 全量论文元数据清单（20 篇修订版）

- Timestamp: 2026-03-26T00:52:11+08:00
- Session: 智乃-02-1774457492-d9ccb6
- Scope: 汇总 `projects/multi-agent-review-survey/literature/` 当前全部已落盘 PDF 的元数据，并核对元数据与实际文件一致。

## 元数据来源

### arXiv / arXiv API

本次使用 `export.arxiv.org` API 批量核对当前 `literature/` 中可识别 arXiv 文件的题目、作者、发布时间、abs 页面与 PDF 链接：

```text
https://export.arxiv.org/api/query?id_list=2402.01680,2412.17481,2501.06322,2502.14321,2504.01963,2505.21116,2502.16804,2506.09656,2603.22862,2603.22386,2603.07670,2602.11583,2601.10122,2508.17281,2510.17491,2602.20867,2603.22928,2603.11088
```

其中返回了以下与当前本地文件一一对应的 arXiv 记录：

- `2402.01680v2` — Guo et al. 2024
- `2412.17481v2` — Chen et al. 2024/2025
- `2501.06322v1` — Tran et al. 2025
- `2502.14321v2` — Yan et al. 2025
- `2502.16804v2` — Wu et al. 2025
- `2504.01963v1` — Aratchige & Ilmini 2025
- `2505.21116v1` — Lin et al. 2025
- `2506.09656v2` — Zeng et al. 2025
- `2508.17281v2` — Chowa et al. 2025
- `2510.17491v1` — Tang et al. 2025
- `2601.10122v1` — Wang et al. 2026
- `2602.11583v1` — Chen et al. 2026
- `2602.20867v1` — Jiang et al. 2026
- `2603.07670v1` — Du 2026
- `2603.11088v1` — Kim et al. 2026
- `2603.22386v1` — Yue et al. 2026
- `2603.22862v1` — Xu et al. 2026
- `2603.22928v1` — Dehghantanha & Homayoun 2026

### DOI / Crossref / 出版社页面

对 Springer 正式发表论文使用 DOI 与 Crossref 核验元数据：

- `https://doi.org/10.1007/s44336-024-00009-2`
- `https://api.crossref.org/works/10.1007/s44336-024-00009-2`

对 `2025-chowa-et-al-llms-as-autonomous-agents-and-tool-users.pdf`，PDF 内嵌元数据与 arXiv API 同时指向：

- arXiv: `https://arxiv.org/abs/2508.17281v2`
- DOI: `https://doi.org/10.1007/s10462-025-11471-9`

## 本地文件核验

执行以下本地命令核对 `literature/` 文件存在、文件大小非零、文件头为 PDF、且可被 `pypdf.PdfReader` 打开：

```bash
find projects/multi-agent-review-survey/literature -maxdepth 1 -type f -name '*.pdf' -printf '%f\t%s\n' | sort
```

```bash
python3 - <<'PY'
from pathlib import Path
from pypdf import PdfReader
for p in sorted(Path('projects/multi-agent-review-survey/literature').glob('*.pdf')):
    with p.open('rb') as f:
        head=f.read(8)
    print(f'{p.name}\t{p.stat().st_size}\t{head!r}\tpages={len(PdfReader(str(p)).pages)}')
PY
```

截至本次记录时，`literature/` 共包含 `20` 个 PDF 文件；20/20 文件大小大于 0、文件头均为 `%PDF-*`，且都能被 `pypdf.PdfReader` 打开。

## 元数据总表

| 序号 | 题目 | 作者 | 年份 | 来源 | 来源页面 | PDF 路径 |
|---|---|---|---:|---|---|---|
| 1 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | Taicheng Guo; Xiuying Chen; Yaqi Wang; Ruidi Chang; Shichao Pei; Nitesh V. Chawla; Olaf Wiest; Xiangliang Zhang | 2024 | arXiv:2402.01680v2 | https://arxiv.org/abs/2402.01680v2 | `projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` |
| 2 | A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | Xinyi Li; Sai Wang; Siqi Zeng; Yu Wu; Yi Yang | 2024 | Springer / DOI:10.1007/s44336-024-00009-2 | https://doi.org/10.1007/s44336-024-00009-2 | `projects/multi-agent-review-survey/literature/2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf` |
| 3 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | R. M. Aratchige; W. M. K. S. Ilmini | 2025 | arXiv:2504.01963v1 | https://arxiv.org/abs/2504.01963v1 | `projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` |
| 4 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | Shuaihang Chen; Yuanxing Liu; Wei Han; Weinan Zhang; Ting Liu | 2024 | arXiv:2412.17481v2 | https://arxiv.org/abs/2412.17481v2 | `projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` |
| 5 | From Language to Action: A Review of Large Language Models as Autonomous Agents and Tool Users | Sadia Sultana Chowa; Riasad Alvi; Subhey Sadi Rahman; Md Abdur Rahman; Mohaimenul Azam Khan Raiaan; Md Rafiqul Islam; Mukhtar Hussain; Sami Azam | 2025 | arXiv:2508.17281v2 / DOI:10.1007/s10462-025-11471-9 | https://doi.org/10.1007/s10462-025-11471-9 | `projects/multi-agent-review-survey/literature/2025-chowa-et-al-llms-as-autonomous-agents-and-tool-users.pdf` |
| 6 | Creativity in LLM-based Multi-Agent Systems: A Survey | Yi-Cheng Lin; Kang-Chieh Chen; Zhe-Yan Li; Tzu-Heng Wu; Tzu-Hsuan Wu; Kuan-Yu Chen; Hung-yi Lee; Yun-Nung Chen | 2025 | arXiv:2505.21116v1 | https://arxiv.org/abs/2505.21116v1 | `projects/multi-agent-review-survey/literature/2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf` |
| 7 | Empowering Real-World: A Survey on the Technology, Practice, and Evaluation of LLM-driven Industry Agents | Yihong Tang; Kehai Chen; Liang Yue; Jinxin Fan; Caishen Zhou; Xiaoguang Li; Yuyang Zhang; Mingming Zhao; Shixiong Kai; Kaiyang Guo; Xingshan Zeng; Wenjing Cun; Lifeng Shang; Min Zhang | 2025 | arXiv:2510.17491v1 | https://arxiv.org/abs/2510.17491v1 | `projects/multi-agent-review-survey/literature/2025-tang-et-al-industry-agents-survey.pdf` |
| 8 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | Khanh-Tung Tran; Dung Dao; Minh-Duong Nguyen; Quoc-Viet Pham; Barry O'Sullivan; Hoang D. Nguyen | 2025 | arXiv:2501.06322v1 | https://arxiv.org/abs/2501.06322v1 | `projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` |
| 9 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | Yaozu Wu; Dongyuan Li; Yankai Chen; Renhe Jiang; Henry Peng Zou; Wei-Chieh Huang; Yangning Li; Liancheng Fang; Zhen Wang; Philip S. Yu | 2025 | arXiv:2502.16804v2 | https://arxiv.org/abs/2502.16804v2 | `projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` |
| 10 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | Bingyu Yan; Zhibo Zhou; Litian Zhang; Lian Zhang; Ziyi Zhou; Dezhuang Miao; Zhoujun Li; Chaozhuo Li; Xiaoming Zhang | 2025 | arXiv:2502.14321v2 | https://arxiv.org/abs/2502.14321v2 | `projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` |
| 11 | Multi-level Value Alignment in Agentic AI Systems: Survey and Perspectives | Wei Zeng; Hengshu Zhu; Chuan Qin; Han Wu; Yihang Cheng; Sirui Zhang; Xiaowei Jin; Yinuo Shen; Zhenxing Wang; Feimin Zhong; Hui Xiong | 2025 | arXiv:2506.09656v2 | https://arxiv.org/abs/2506.09656v2 | `projects/multi-agent-review-survey/literature/2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf` |
| 12 | SoK: Agentic Skills -- Beyond Tool Use in LLM Agents | Yanna Jiang; Delong Li; Haiyu Deng; Baihe Ma; Xu Wang; Qin Wang; Guangsheng Yu | 2026 | arXiv:2602.20867v1 | https://arxiv.org/abs/2602.20867v1 | `projects/multi-agent-review-survey/literature/2026-agentic-skills-beyond-tool-use-in-llm-agents.pdf` |
| 13 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | Jingdi Chen; Hanqing Yang; Zongjun Liu; Carlee Joe-Wong | 2026 | arXiv:2602.11583v1 | https://arxiv.org/abs/2602.11583v1 | `projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` |
| 14 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | Jingdi Chen; Hanqing Yang; Zongjun Liu; Carlee Joe-Wong | 2026 | arXiv:2602.11583v1 | https://arxiv.org/abs/2602.11583v1 | `projects/multi-agent-review-survey/literature/2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf` |
| 15 | SoK: The Attack Surface of Agentic AI -- Tools, and Autonomy | Ali Dehghantanha; Sajad Homayoun | 2026 | arXiv:2603.22928v1 | https://arxiv.org/abs/2603.22928v1 | `projects/multi-agent-review-survey/literature/2026-dehghantanha-homayoun-attack-surface-of-agentic-ai.pdf` |
| 16 | Memory for Autonomous LLM Agents:Mechanisms, Evaluation, and Emerging Frontiers | Pengfei Du | 2026 | arXiv:2603.07670v1 | https://arxiv.org/abs/2603.07670v1 | `projects/multi-agent-review-survey/literature/2026-du-memory-for-autonomous-llm-agents.pdf` |
| 17 | The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey | Juhee Kim; Xiaoyuan Liu; Zhun Wang; Shi Qiu; Bo Li; Wenbo Guo; Dawn Song | 2026 | arXiv:2603.11088v1 | https://arxiv.org/abs/2603.11088v1 | `projects/multi-agent-review-survey/literature/2026-kim-et-al-attack-and-defense-landscape-of-agentic-ai.pdf` |
| 18 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | Ye Wang; Jiaxing Chen; Hongjiang Xiao | 2026 | arXiv:2601.10122v1 | https://arxiv.org/abs/2601.10122v1 | `projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf` |
| 19 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | Haoyuan Xu; Chang Li; Xinyan Ma; Xianhao Ou; Zihan Zhang; Tao He; Xiangyu Liu; Zixiang Wang; Jiafeng Liang; Zheng Chu; Runxuan Liu; Rongchuan Mu; Ming Liu; Bing Qin | 2026 | arXiv:2603.22862v1 | https://arxiv.org/abs/2603.22862v1 | `projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf` |
| 20 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | Ling Yue; Kushal Raj Bhandari; Ching-Yun Ko; Dhaval Patel; Shuxin Lin; Nianjun Zhou; Jianxi Gao; Pin-Yu Chen; Shaowu Pan | 2026 | arXiv:2603.22386v1 | https://arxiv.org/abs/2603.22386v1 | `projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` |

## 文件一致性核验

| 文件名 | 字节数 | 文件头 | 页数 | 结论 |
|---|---:|---|---:|---|
| `2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | 1243493 | `%PDF-1.5` | 15 | 通过 |
| `2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf` | 3482567 | `%PDF-1.4` | 43 | 通过 |
| `2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` | 195656 | `%PDF-1.5` | 12 | 通过 |
| `2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | 404537 | `%PDF-1.5` | 13 | 通过 |
| `2025-chowa-et-al-llms-as-autonomous-agents-and-tool-users.pdf` | 4283675 | `%PDF-1.6` | 38 | 通过 |
| `2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf` | 1461659 | `%PDF-1.5` | 23 | 通过 |
| `2025-tang-et-al-industry-agents-survey.pdf` | 2239244 | `%PDF-1.7` | 33 | 通过 |
| `2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | 2420086 | `%PDF-1.5` | 35 | 通过 |
| `2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | 2307367 | `%PDF-1.7` | 18 | 通过 |
| `2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | 1147688 | `%PDF-1.5` | 16 | 通过 |
| `2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf` | 1250677 | `%PDF-1.7` | 32 | 通过 |
| `2026-agentic-skills-beyond-tool-use-in-llm-agents.pdf` | 5450171 | `%PDF-1.7` | 20 | 通过 |
| `2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` | 3848111 | `%PDF-1.7` | 143 | 通过 |
| `2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf` | 3848111 | `%PDF-1.7` | 143 | 通过 |
| `2026-dehghantanha-homayoun-attack-surface-of-agentic-ai.pdf` | 699066 | `%PDF-1.7` | 16 | 通过 |
| `2026-du-memory-for-autonomous-llm-agents.pdf` | 313563 | `%PDF-1.7` | 15 | 通过 |
| `2026-kim-et-al-attack-and-defense-landscape-of-agentic-ai.pdf` | 2472764 | `%PDF-1.7` | 33 | 通过 |
| `2026-wang-et-al-role-playing-agents.pdf` | 421897 | `%PDF-1.7` | 15 | 通过 |
| `2026-xu-et-al-tool-use-in-llm-agents.pdf` | 2119320 | `%PDF-1.7` | 42 | 通过 |
| `2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` | 1576067 | `%PDF-1.7` | 31 | 通过 |

## 发现

1. 先前 `analysis/2026-03-26-literature-metadata-inventory.md` 仍停留在 `14` 篇旧状态；当前 `literature/` 实际已增至 `20` 篇，因此本次已按现状修订。
2. `literature/` 中存在一组重复内容文件：
   - `2026-chen-et-al-five-ws-of-multi-agent-communication.pdf`
   - `2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf`
   两者字节数同为 `3848111`、页数同为 `143`、题目相同，均对应 arXiv `2602.11583v1`。本任务只要求元数据与实际文件一致，因此在清单中保留两条映射，不擅自删除文件。

## 结论

截至本次记录，`projects/multi-agent-review-survey/literature/` 中当前全部 `20` 个 PDF 文件均已建立元数据映射，且每条记录的 `PDF 路径` 与仓库内实际文件一致；“元数据清单完整且与实际文件一致”这一任务现已满足。