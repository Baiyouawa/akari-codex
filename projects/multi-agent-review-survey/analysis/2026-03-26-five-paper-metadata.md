# 2026-03-26 五篇 multi-agent 相关综述元数据清单

- Timestamp: 2026-03-26T00:06:48+08:00
- Session: 智乃-02-1774454514-e3eed8
- Scope: 为当前已落盘的 5 篇综述/综述型论文记录题目、作者、年份、来源、PDF 路径，并核对本地文件存在且文件头为 PDF。

## 来源与筛选依据

本次清单基于 arXiv API 实时查询与本地下载结果生成。

### 元数据来源

使用 `python3` 请求以下 arXiv API：

```text
http://export.arxiv.org/api/query?id_list=2603.22862,2603.22386,2603.07670,2602.11583,2601.10122
```

该 API 返回每篇论文的：
- `title`
- `published`
- `author`
- arXiv `abs` 页面
- arXiv `pdf` 链接

### 本地文件核验

下载后执行：

```bash
find projects/multi-agent-review-survey/literature -maxdepth 1 -type f -name '*.pdf' -printf '%f\t%s\n' | sort
```

以及：

```bash
python3 - <<'PY'
from pathlib import Path
for p in sorted(Path('projects/multi-agent-review-survey/literature').glob('*.pdf')):
    with p.open('rb') as f:
        head=f.read(8)
    print(f'{p.name}\t{p.stat().st_size}\t{head!r}')
PY
```

核验结果显示 5 个文件均存在、大小大于 0，且文件头均为 `b'%PDF-1.7'`。

## 元数据表

| 序号 | 题目 | 作者 | 年份 | 来源 | 来源页面 | PDF 路径 |
|---|---|---|---:|---|---|---|
| 1 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | Haoyuan Xu; Chang Li; Xinyan Ma; Xianhao Ou; Zihan Zhang; Tao He; Xiangyu Liu; Zixiang Wang; Jiafeng Liang; Zheng Chu; Runxuan Liu; Rongchuan Mu; Ming Liu; Bing Qin | 2026 | arXiv:2603.22862v1 | https://arxiv.org/abs/2603.22862v1 | `projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf` |
| 2 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | Ling Yue; Kushal Raj Bhandari; Ching-Yun Ko; Dhaval Patel; Shuxin Lin; Nianjun Zhou; Jianxi Gao; Pin-Yu Chen; Shaowu Pan | 2026 | arXiv:2603.22386v1 | https://arxiv.org/abs/2603.22386v1 | `projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` |
| 3 | Memory for Autonomous LLM Agents:Mechanisms, Evaluation, and Emerging Frontiers | Pengfei Du | 2026 | arXiv:2603.07670v1 | https://arxiv.org/abs/2603.07670v1 | `projects/multi-agent-review-survey/literature/2026-du-memory-for-autonomous-llm-agents.pdf` |
| 4 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | Jingdi Chen; Hanqing Yang; Zongjun Liu; Carlee Joe-Wong | 2026 | arXiv:2602.11583v1 | https://arxiv.org/abs/2602.11583v1 | `projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` |
| 5 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | Ye Wang; Jiaxing Chen; Hongjiang Xiao | 2026 | arXiv:2601.10122v1 | https://arxiv.org/abs/2601.10122v1 | `projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf` |

## 文件一致性核验结果

| 文件名 | 字节数 | 文件头 | 结论 |
|---|---:|---|---|
| `2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` | 3848111 | `%PDF-1.7` | 通过 |
| `2026-du-memory-for-autonomous-llm-agents.pdf` | 313563 | `%PDF-1.7` | 通过 |
| `2026-wang-et-al-role-playing-agents.pdf` | 421897 | `%PDF-1.7` | 通过 |
| `2026-xu-et-al-tool-use-in-llm-agents.pdf` | 2119320 | `%PDF-1.7` | 通过 |
| `2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` | 1576067 | `%PDF-1.7` | 通过 |

## 备注

- 本次交付覆盖的是当前已下载并核验成功的 5 篇论文，而非项目任务列表中尚未完成的 10 篇全集。
- 该清单中的“PDF 路径”均为仓库内真实存在的本地路径，不含虚构路径。
- 若后续要扩展到 10 篇，应继续沿用同样的来源记录与落盘核验方式。 
