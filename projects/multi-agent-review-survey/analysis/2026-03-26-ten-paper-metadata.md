# 2026-03-26 十篇 multi-agent 综述语料元数据与落盘核验

- Timestamp: 2026-03-26T00:15:25+08:00
- Session: 侑-00-1774454754-20fa0d
- Scope: 为本次综述报告锁定 10 篇 multi-agent / agentic AI 相关综述，记录来源、年份、作者、本地 PDF 路径，并验证文件可打开。

## 语料选择方法

本次不是在空仓状态下重新“发现”论文，而是基于项目 `literature/` 中已存在的 20 个 PDF，结合 arXiv API / 出版社页面元数据，选择 10 篇更贴近以下范围的综述：

1. 主题与 `multi-agent systems`、`LLM-based multi-agent systems`、`agentic AI systems` 直接相关；
2. 时间尽量新，以 2024-2026 为主；
3. 优先选择“总览型”或“关键子方向型”综述，而不是单一任务实验论文；
4. 至少覆盖：总体框架、协作/通信、技术栈、应用扩展、治理/对齐等层次。

## 元数据来源

### 1. arXiv API

使用以下查询获取 9 篇 arXiv 论文的题目、作者、发布日期、摘要与 PDF 链接：

```text
http://export.arxiv.org/api/query?id_list=2402.01680,2412.17481,2501.06322,2502.14321,2502.16804,2504.01963,2505.21116,2506.09656,2602.11583
```

### 2. 出版社页面 / PDF 首页

Springer 论文《A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges》由本地 PDF 首页给出 DOI 与期刊信息：

- DOI: `10.1007/s44336-024-00009-2`
- 本地 PDF: `projects/multi-agent-review-survey/literature/2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf`

## 本地核验方法

### 文件存在性与总量

```bash
python3 - <<'PY'
from pathlib import Path
from collections import Counter
files=sorted(Path('projects/multi-agent-review-survey/literature').glob('*.pdf'))
print('total_pdfs', len(files))
selected=[
'2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf',
'2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf',
'2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf',
'2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf',
'2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf',
'2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf',
'2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf',
'2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf',
'2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf',
'2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf',
]
print('selected_count', len(selected))
print('all_exist', all((Path('projects/multi-agent-review-survey/literature')/f).exists() for f in selected))
print('selected_bytes', sum((Path('projects/multi-agent-review-survey/literature')/f).stat().st_size for f in selected))
print('year_counts', Counter(f[:4] for f in selected))
PY
```

输出：

- `total_pdfs = 20`
- `selected_count = 10`
- `all_exist = True`
- `selected_bytes = 17761841`
- `year_counts = Counter({'2025': 7, '2024': 2, '2026': 1})`

### PDF 可打开性

```bash
python3 - <<'PY'
from pathlib import Path
from pypdf import PdfReader
for p in sorted(Path('projects/multi-agent-review-survey/literature').glob('*.pdf')):
    head = p.read_bytes()[:8]
    reader = PdfReader(str(p))
    print(f'{p.name}\t{p.stat().st_size}\t{head!r}\tpages={len(reader.pages)}')
PY
```

本次所选 10 篇均成功被 `pypdf.PdfReader` 打开，文件头为 `%PDF`，页数大于 0。

## 10 篇最终语料清单

| 序号 | 题目 | 作者 | 发布年份 | 来源 | 来源页面 | 本地 PDF 路径 | 页数 |
|---|---|---|---:|---|---|---|---:|
| 1 | A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | Xinyi Li; Sai Wang; Siqi Zeng; Yu Wu; Yi Yang | 2024 | Vicinagearth / Springer | https://doi.org/10.1007/s44336-024-00009-2 | `projects/multi-agent-review-survey/literature/2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf` | 43 |
| 2 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | Taicheng Guo; Xiuying Chen; Yaqi Wang; Ruidi Chang; Shichao Pei; Nitesh V. Chawla; Olaf Wiest; Xiangliang Zhang | 2024 | arXiv:2402.01680v2 | https://arxiv.org/abs/2402.01680v2 | `projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | 15 |
| 3 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | Shuaihang Chen; Yuanxing Liu; Wei Han; Weinan Zhang; Ting Liu | 2024 | arXiv:2412.17481v2 | https://arxiv.org/abs/2412.17481v2 | `projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | 13 |
| 4 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | Khanh-Tung Tran; Dung Dao; Minh-Duong Nguyen; Quoc-Viet Pham; Barry O'Sullivan; Hoang D. Nguyen | 2025 | arXiv:2501.06322v1 | https://arxiv.org/abs/2501.06322v1 | `projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | 35 |
| 5 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | Bingyu Yan; Zhibo Zhou; Litian Zhang; Lian Zhang; Ziyi Zhou; Dezhuang Miao; Zhoujun Li; Chaozhuo Li; Xiaoming Zhang | 2025 | arXiv:2502.14321v2 | https://arxiv.org/abs/2502.14321v2 | `projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | 16 |
| 6 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | Yaozu Wu; Dongyuan Li; Yankai Chen; Renhe Jiang; Henry Peng Zou; Wei-Chieh Huang; Yangning Li; Liancheng Fang; Zhen Wang; Philip S. Yu | 2025 | arXiv:2502.16804v2 | https://arxiv.org/abs/2502.16804v2 | `projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | 18 |
| 7 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | R. M. Aratchige; W. M. K. S. Ilmini | 2025 | arXiv:2504.01963v1 | https://arxiv.org/abs/2504.01963v1 | `projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` | 12 |
| 8 | Creativity in LLM-based Multi-Agent Systems: A Survey | Yi-Cheng Lin; Kang-Chieh Chen; Zhe-Yan Li; Tzu-Heng Wu; Tzu-Hsuan Wu; Kuan-Yu Chen; Hung-yi Lee; Yun-Nung Chen | 2025 | arXiv:2505.21116v1 | https://arxiv.org/abs/2505.21116v1 | `projects/multi-agent-review-survey/literature/2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf` | 23 |
| 9 | Multi-level Value Alignment in Agentic AI Systems: Survey and Perspectives | Wei Zeng; Hengshu Zhu; Chuan Qin; Han Wu; Yihang Cheng; Sirui Zhang; Xiaowei Jin; Yinuo Shen; Zhenxing Wang; Feimin Zhong; Hui Xiong | 2025 | arXiv:2506.09656v2 | https://arxiv.org/abs/2506.09656v2 | `projects/multi-agent-review-survey/literature/2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf` | 32 |
| 10 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | Jingdi Chen; Hanqing Yang; Zongjun Liu; Carlee Joe-Wong | 2026 | arXiv:2602.11583v1 / TMLR accepted | https://arxiv.org/abs/2602.11583v1 | `projects/multi-agent-review-survey/literature/2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf` | 143 |

## 选择说明

未把 `literature/` 中全部 20 个 PDF 都纳入本轮综合报告，原因如下：

1. 本轮报告要求是“综合 10 篇综述撰写中文 Markdown 报告”，因此需要先固定一个 10 篇工作语料子集；
2. 本次优先保留能组成“总览 → 协作/通信 → 技术要素 → 应用特化 → 治理/价值”链条的语料组合；
3. 已存在的其他 PDF 中，有些更偏 agent security、tool use、memory、workflow 等 agentic AI 子专题综述，本轮未全部纳入，是为了保持“multi-agent 主线”更集中。

## 与报告文件的关系

本元数据文件对应的综合报告为：

- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
