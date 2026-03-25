# 2026-03-26 literature/ 中 10 个目标 PDF 核验

## 任务

验证 `projects/multi-agent-review-survey/literature/` 中本轮综述工作语料锁定的 10 个 PDF 是否：

1. 可正常打开；
2. 文件不为空；
3. 命名无冲突。

本次核验对象采用 `analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md` 与 `analysis/2026-03-26-ten-paper-metadata.md` 已固定的 10 篇最终语料子集，而不是目录中的全部 20 个 PDF。

## 核验方法

使用本地 `python3` + `pypdf.PdfReader` 对 10 个目标文件逐个检查：

- 文件是否存在；
- 文件大小是否 `> 0`；
- 文件头前 5 字节是否为 `%PDF-`；
- 是否可被 `pypdf.PdfReader` 成功打开并读取页数；
- 10 个目标文件名是否重复；
- `literature/` 目录中现有 PDF 文件名是否存在重复。

执行命令：

```bash
python3 - <<'PY'
from pathlib import Path
from collections import Counter
from pypdf import PdfReader
base = Path('projects/multi-agent-review-survey/literature')
selected = [
'2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf',
'2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf',
'2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf',
'2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf',
'2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf',
'2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf',
'2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf',
'2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf',
'2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf',
'2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf',
]
name_counts = Counter(selected)
print('duplicate_selected_names', [n for n,c in name_counts.items() if c>1])
for name in selected:
    path = base / name
    exists = path.exists()
    size = path.stat().st_size if exists else None
    head = path.read_bytes()[:5] if exists else b''
    pages = len(PdfReader(str(path)).pages) if exists else None
    print(f'{name}\t{exists}\t{size}\t{head!r}\tpages={pages}')
all_names = [p.name for p in base.glob('*.pdf')]
print('duplicate_dir_names', [n for n,c in Counter(all_names).items() if c>1])
print('selected_count', len(selected))
print('dir_pdf_count', len(all_names))
PY
```

补充目录级重名检查：

```bash
find projects/multi-agent-review-survey/literature -maxdepth 1 -type f -name '*.pdf' -printf '%f\n' | sort | uniq -d
```

该命令输出为空，表示目录内 PDF 文件名无重复。

## 逐文件结果

| # | File | Exists | Bytes | Header | Pages | Result |
|---|---|---|---:|---|---:|---|
| 1 | `2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | True | 1,243,493 | `%PDF-` | 15 | pass |
| 2 | `2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf` | True | 3,482,567 | `%PDF-` | 43 | pass |
| 3 | `2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | True | 404,537 | `%PDF-` | 13 | pass |
| 4 | `2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | True | 2,420,086 | `%PDF-` | 35 | pass |
| 5 | `2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | True | 1,147,688 | `%PDF-` | 16 | pass |
| 6 | `2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | True | 2,307,367 | `%PDF-` | 18 | pass |
| 7 | `2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` | True | 195,656 | `%PDF-` | 12 | pass |
| 8 | `2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf` | True | 1,461,659 | `%PDF-` | 23 | pass |
| 9 | `2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf` | True | 1,250,677 | `%PDF-` | 32 | pass |
| 10 | `2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf` | True | 3,848,111 | `%PDF-` | 143 | pass |

## 汇总结论

### 1. 可正常打开

10/10 目标文件均可被 `pypdf.PdfReader` 成功打开，且页数均大于 0，因此“可正常打开”检查通过。

### 2. 文件不为空

10/10 目标文件大小均大于 0 字节；其中最小文件为 `195,656` bytes，最大文件为 `3,848,111` bytes，因此“文件不为空”检查通过。

### 3. 命名无冲突

- 目标 10 文件内部重复名列表：`[]`
- 整个 `literature/` 目录 PDF 重复名列表：空输出

因此“命名无冲突”检查通过。

## 结论

截至 `2026-03-26T00:19:05+08:00`，本轮锁定的 10 个综述 PDF 已全部通过本地核验：

- 每个文件都存在；
- 每个文件都非空；
- 每个文件都具有 `%PDF-` 文件头；
- 每个文件都能被 `pypdf.PdfReader` 打开并读取页数；
- 目标 10 文件与整个 `literature/` 目录均无文件名冲突。

因此，任务“验证 literature 文件夹中的 10 个 PDF 是否可正常打开、文件不为空、命名无冲突”已完成。

## Provenance

- 目标 10 文件名单来源：
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-pdf-links-and-download-record.md`
  - `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- 本地核验命令：见上文 `python3` 与 `find ... | uniq -d`。
- 字节数、文件头、页数数据：均来自本次本地脚本直接读取 `projects/multi-agent-review-survey/literature/`。