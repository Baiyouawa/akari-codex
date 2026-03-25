# 2026-03-26 literature/ 全量论文元数据清单

- Timestamp: 2026-03-26T00:06:48+08:00
- Session: 智乃-02-1774454514-e3eed8
- Scope: 汇总 `projects/multi-agent-review-survey/literature/` 当前全部已落盘 PDF 的元数据，并核对元数据与实际文件一致。

## 元数据来源

### arXiv 论文

通过 `python3` 请求 arXiv API 获取论文题目、作者、发布日期、abs 页面与 pdf 链接。最终使用的 id 集合覆盖了当前 `literature/` 中全部 arXiv 文件：

```text
http://export.arxiv.org/api/query?id_list=2402.01680,2412.17481,2501.06322,2502.14321,2504.01963,2505.21116,2502.16804,2506.09656,2603.22862,2603.22386,2603.07670,2602.11583,2601.10122
```

### Springer 论文

对 DOI `10.1007/s44336-024-00009-2` 使用以下来源核验元数据：

- `https://doi.org/10.1007/s44336-024-00009-2`
- `https://api.crossref.org/works/10.1007/s44336-024-00009-2`

两者均返回题目 `A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges`，并指向 Springer / Vicinagearth 正式页面。

## 本地文件核验

执行以下本地命令核对 `literature/` 文件存在、文件大小非零、文件头为 PDF：

```bash
find projects/multi-agent-review-survey/literature -maxdepth 1 -type f -name '*.pdf' -printf '%f\t%s\n' | sort
```

```bash
python3 - <<'PY'
from pathlib import Path
for p in sorted(Path('projects/multi-agent-review-survey/literature').glob('*.pdf')):
    with p.open('rb') as f:
        head=f.read(8)
    print(f'{p.name}\t{p.stat().st_size}\t{head!r}')
PY
```

截至本次记录时，`literature/` 共包含 `14` 个 PDF 文件，且全部文件大小大于 0、文件头均为 `%PDF-*`。

## 元数据总表

| 序号 | 题目 | 作者 | 年份 | 来源 | 来源页面 | PDF 路径 |
|---|---|---|---:|---|---|---|
| 1 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | Taicheng Guo; Xiuying Chen; Yaqi Wang; Ruidi Chang; Shichao Pei; Nitesh V. Chawla; Olaf Wiest; Xiangliang Zhang | 2024 | arXiv:2402.01680v2 | https://arxiv.org/abs/2402.01680v2 | `projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` |
| 2 | A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | Xinyi Li; Sai Wang; Siqi Zeng; Yu Wu; Yi Yang | 2024 | Springer / Vicinagearth / DOI:10.1007/s44336-024-00009-2 | https://doi.org/10.1007/s44336-024-00009-2 | `projects/multi-agent-review-survey/literature/2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf` |
| 3 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | Shuaihang Chen; Yuanxing Liu; Wei Han; Weinan Zhang; Ting Liu | 2024 | arXiv:2412.17481v2 | https://arxiv.org/abs/2412.17481v2 | `projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` |
| 4 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | Khanh-Tung Tran; Dung Dao; Minh-Duong Nguyen; Quoc-Viet Pham; Barry O'Sullivan; Hoang D. Nguyen | 2025 | arXiv:2501.06322v1 | https://arxiv.org/abs/2501.06322v1 | `projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` |
| 5 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | Bingyu Yan; Zhibo Zhou; Litian Zhang; Lian Zhang; Ziyi Zhou; Dezhuang Miao; Zhoujun Li; Chaozhuo Li; Xiaoming Zhang | 2025 | arXiv:2502.14321v2 | https://arxiv.org/abs/2502.14321v2 | `projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` |
| 6 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | R. M. Aratchige; W. M. K. S. Ilmini | 2025 | arXiv:2504.01963v1 | https://arxiv.org/abs/2504.01963v1 | `projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` |
| 7 | Creativity in LLM-based Multi-Agent Systems: A Survey | Yi-Cheng Lin; Kang-Chieh Chen; Zhe-Yan Li; Tzu-Heng Wu; Tzu-Hsuan Wu; Kuan-Yu Chen; Hung-yi Lee; Yun-Nung Chen | 2025 | arXiv:2505.21116v1 | https://arxiv.org/abs/2505.21116v1 | `projects/multi-agent-review-survey/literature/2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf` |
| 8 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | Yaozu Wu; Dongyuan Li; Yankai Chen; Renhe Jiang; Henry Peng Zou; Wei-Chieh Huang; Yangning Li; Liancheng Fang; Zhen Wang; Philip S. Yu | 2025 | arXiv:2502.16804v2 | https://arxiv.org/abs/2502.16804v2 | `projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` |
| 9 | Multi-level Value Alignment in Agentic AI Systems: Survey and Perspectives | Wei Zeng; Hengshu Zhu; Chuan Qin; Han Wu; Yihang Cheng; Sirui Zhang; Xiaowei Jin; Yinuo Shen; Zhenxing Wang; Feimin Zhong; Hui Xiong | 2025 | arXiv:2506.09656v2 | https://arxiv.org/abs/2506.09656v2 | `projects/multi-agent-review-survey/literature/2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf` |
| 10 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | Haoyuan Xu; Chang Li; Xinyan Ma; Xianhao Ou; Zihan Zhang; Tao He; Xiangyu Liu; Zixiang Wang; Jiafeng Liang; Zheng Chu; Runxuan Liu; Rongchuan Mu; Ming Liu; Bing Qin | 2026 | arXiv:2603.22862v1 | https://arxiv.org/abs/2603.22862v1 | `projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf` |
| 11 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | Ling Yue; Kushal Raj Bhandari; Ching-Yun Ko; Dhaval Patel; Shuxin Lin; Nianjun Zhou; Jianxi Gao; Pin-Yu Chen; Shaowu Pan | 2026 | arXiv:2603.22386v1 | https://arxiv.org/abs/2603.22386v1 | `projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` |
| 12 | Memory for Autonomous LLM Agents:Mechanisms, Evaluation, and Emerging Frontiers | Pengfei Du | 2026 | arXiv:2603.07670v1 | https://arxiv.org/abs/2603.07670v1 | `projects/multi-agent-review-survey/literature/2026-du-memory-for-autonomous-llm-agents.pdf` |
| 13 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | Jingdi Chen; Hanqing Yang; Zongjun Liu; Carlee Joe-Wong | 2026 | arXiv:2602.11583v1 | https://arxiv.org/abs/2602.11583v1 | `projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` |
| 14 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | Ye Wang; Jiaxing Chen; Hongjiang Xiao | 2026 | arXiv:2601.10122v1 | https://arxiv.org/abs/2601.10122v1 | `projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf` |

## 文件一致性核验

| 文件名 | 字节数 | 文件头 | 结论 |
|---|---:|---|---|
| `2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | 1243493 | `%PDF-1.5` | 通过 |
| `2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf` | 3482567 | `%PDF-1.4` | 通过 |
| `2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` | 195656 | `%PDF-1.5` | 通过 |
| `2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | 404537 | `%PDF-1.5` | 通过 |
| `2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf` | 1461659 | `%PDF-1.5` | 通过 |
| `2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | 2420086 | `%PDF-1.5` | 通过 |
| `2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | 2307367 | `%PDF-1.7` | 通过 |
| `2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | 1147688 | `%PDF-1.5` | 通过 |
| `2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf` | 36864 | `%PDF-1.5` | 通过 |
| `2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` | 3848111 | `%PDF-1.7` | 通过 |
| `2026-du-memory-for-autonomous-llm-agents.pdf` | 313563 | `%PDF-1.7` | 通过 |
| `2026-wang-et-al-role-playing-agents.pdf` | 421897 | `%PDF-1.7` | 通过 |
| `2026-xu-et-al-tool-use-in-llm-agents.pdf` | 2119320 | `%PDF-1.7` | 通过 |
| `2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` | 1576067 | `%PDF-1.7` | 通过 |

## 结论

截至本次记录，`projects/multi-agent-review-survey/literature/` 中当前全部 `14` 个 PDF 文件均已建立元数据映射，且每条记录的 `PDF 路径` 与仓库内实际文件一致。