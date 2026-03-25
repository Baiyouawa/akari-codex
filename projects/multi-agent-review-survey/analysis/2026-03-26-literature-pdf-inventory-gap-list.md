# 2026-03-26 literature/ 现有 PDF 盘点：真实 multi-agent 综述、重复项、不合格项与缺口清单

- Timestamp: 2026-03-26T02:47:46+08:00
- Session: 日向-03-1774464404-45ea29
- Task: 盘点 `projects/multi-agent-review-survey/literature/` 现有 PDF，核对哪些是真正的 multi-agent 综述/survey、哪些重复或不合格，形成缺口清单
- Status: completed

## 1. 盘点范围与方法

本次只盘点项目内**已经落盘**的 PDF，不重新扩展候选池。判定与结论均绑定到仓库内既有工件和本次本地校验结果。

### 1.1 输入工件

1. `projects/multi-agent-review-survey/literature/` 当前全部 PDF
2. `projects/multi-agent-review-survey/analysis/2026-03-26-literature-metadata-inventory.md`
3. `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
4. `projects/multi-agent-review-survey/analysis/2026-03-26-final-selected-10-and-exclusion-list.md`
5. `projects/multi-agent-review-survey/analysis/2026-03-26-survey-identity-evidence-chain-audit.md`
6. `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
7. `projects/multi-agent-review-survey/analysis/2026-03-26-latest-five-review-evidence-verification.md`

### 1.2 本地核验命令

本次会话实际执行以下命令，确认目录总数、页数、字节数与 SHA256；并据此识别重复文件。

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
from pypdf import PdfReader
base=Path('projects/multi-agent-review-survey/literature')
files=sorted(base.glob('*.pdf'))
print('pdf_count', len(files))
for p in files:
    data=p.read_bytes()
    sha=hashlib.sha256(data).hexdigest()
    pages=len(PdfReader(str(p)).pages)
    print(f'{p.name}\t{p.stat().st_size}\t{pages}\t{sha}')
PY
```

本次输出显示：

- `pdf_count = 20`
- 20/20 文件可由 `pypdf.PdfReader` 打开
- 存在 1 组**同内容重复文件**：两份 `2602.11583` 的 SHA256 完全相同，均为 `5c8a6a3368056ff0bb0c36d1a432e68d6a358e4ecbeabeae2565b94146ee8fdc`

## 2. 判定口径

本次将 20 个 PDF 划分为四类：

1. **A 类：真正的 multi-agent 核心综述/调查**
   - 明确是 survey/review/SoK/taxonomy 型文献；
   - 且主题直接面向 multi-agent systems、LLM-based multi-agent systems、communication、collaboration 等主线。
2. **B 类：真正的综述，但属于 agentic/专题边界综述**
   - 也是货真价实的综述；
   - 但主题中心更偏 workflow、tool use、role-play、memory、安全、行业/创意等专题，而非 multi-agent 主线本体。
3. **C 类：重复文件**
   - 内容相同、只是文件名不同；属于库存问题，不是文献质量问题。
4. **D 类：当前目标集下的不合格项**
   - 这里的“不合格”特指：**不适合作为“最终 10 篇 multi-agent 核心综述”成员**；
   - 不等于“不是综述”。

## 3. 全量盘点结果

### 3.1 A 类：真正的 multi-agent 核心综述/调查（9 篇唯一文件）

> 这些论文同时满足“是真综述”与“直接面向 multi-agent 主线”。

| # | 文件名 | 判定 | 依据 |
|---|---|---|---|
| 1 | `2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | A | 标题含 `A Survey`，且 `survey-identity-evidence-chain-audit.md` 认定为“明确综述”；主题是 LLM-based multi-agent systems 总览 |
| 2 | `2024-li-et-al-a-survey-on-llm-based-multi-agent-systems-workflow-infrastructure-and-challenges-springer-10.1007-s44336-024-00009-2.pdf` | A | 标题直接为 `A survey on LLM-based multi-agent systems`；虽未进入 canonical 10，但从题名与 metadata 可知属于 multi-agent 总综述 |
| 3 | `2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` | A | 标题含 `A Survey`；`survey-identity-evidence-chain-audit.md` 认定为“明确综述”；主题直接是 LLM-based MAS |
| 4 | `2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | A | 标题含 `A Survey`；证据链工件认定为“明确综述”；主题直接是 LLM-based MAS |
| 5 | `2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | A | 标题含 `A Survey`；证据链工件认定为“明确综述”；主题直接是 collaboration mechanisms |
| 6 | `2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | A（应用专题但仍属 multi-agent） | `survey-identity-evidence-chain-audit.md` 明确判为“明确综述，且为专题综述”；虽偏自动驾驶，但对象仍是 multi-agent ADS |
| 7 | `2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | A | communication-centric multi-agent 核心综述；证据链工件认定为“明确综述” |
| 8 | `2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` | A | `latest-five-review-evidence-verification.md` 与 `survey-identity-evidence-chain-audit.md` 都认定为 multi-agent communication 核心 survey |
| 9 | `2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf` | C（重复），原论文归 A | 内容与上一文件相同；同一篇核心综述的重复落盘 |

### 3.2 B 类：真正的综述，但属于 agentic/专题边界综述（10 篇唯一文件）

| # | 文件名 | 判定 | 依据 |
|---|---|---|---|
| 1 | `2025-chowa-et-al-llms-as-autonomous-agents-and-tool-users.pdf` | B | 综述对象偏 autonomous agents / tool users，而非 multi-agent 主线 |
| 2 | `2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf` | B | 虽是 multi-agent systems survey，但主题聚焦 creativity 专题，不是通用主线 |
| 3 | `2025-tang-et-al-industry-agents-survey.pdf` | B | 行业 agent 综述，更偏 industry agents/应用实践 |
| 4 | `2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf` | B | agentic AI 对齐综述，不是 multi-agent 主线综述 |
| 5 | `2026-agentic-skills-beyond-tool-use-in-llm-agents.pdf` | B | SoK/综述型文献，但主题是 agentic skills |
| 6 | `2026-dehghantanha-homayoun-attack-surface-of-agentic-ai.pdf` | B | `latest-five-review-evidence-verification.md` 判为“边界保留”；主题主轴是 agentic AI 安全 |
| 7 | `2026-du-memory-for-autonomous-llm-agents.pdf` | B | `candidate-survey-judgment-and-top10.md` 明确列为 memory 专题综述 |
| 8 | `2026-kim-et-al-attack-and-defense-landscape-of-agentic-ai.pdf` | B | agentic AI 安全/攻防综述 |
| 9 | `2026-wang-et-al-role-playing-agents.pdf` | B | `survey-identity-evidence-chain-audit.md` 判为“综述型边界论文”；偏 social / role-playing agents |
| 10 | `2026-xu-et-al-tool-use-in-llm-agents.pdf` | B | `survey-identity-evidence-chain-audit.md` 判为“综述型边界论文”；偏 multi-tool agents |
| 11 | `2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` | B | `survey-identity-evidence-chain-audit.md` 与 `latest-five-review-evidence-verification.md` 均判为 workflow optimization 边界综述 |

### 3.3 C 类：重复文件（1 组，2 个文件）

| 重复组 | 文件 | 证据 |
|---|---|---|
| 2602.11583 | `2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` | SHA256 `5c8a6a3368056ff0bb0c36d1a432e68d6a358e4ecbeabeae2565b94146ee8fdc` |
| 2602.11583 | `2026-chen-et-al-the-five-ws-of-multi-agent-communication-who-talks-to-whom-when-what-and-why-a-survey-from-marl-to-emergent-language-and-llms-arxiv-2602.11583.pdf` | SHA256 `5c8a6a3368056ff0bb0c36d1a432e68d6a358e4ecbeabeae2565b94146ee8fdc` |

判定：这是**同内容重复落盘**，应只保留一份规范文件名版本。

### 3.4 D 类：当前目标集下“不合格”的文件

这里的“不合格”指：**不应被算入“最终 10 篇 multi-agent 核心综述”**。按这个口径，本目录里当前有两类不合格：

1. **重复项**：1 个冗余文件
   - 即第二份 `2602.11583`
2. **边界专题综述**：若目标是“10 篇 multi-agent 核心综述”，则以下 10 篇不应直接占用核心名额
   - `2025-chowa-et-al-llms-as-autonomous-agents-and-tool-users.pdf`
   - `2025-lin-et-al-creativity-in-llm-based-multi-agent-systems-a-survey-arxiv-2505.21116.pdf`
   - `2025-tang-et-al-industry-agents-survey.pdf`
   - `2025-zeng-et-al-multi-level-value-alignment-in-agentic-ai-systems-survey-and-perspectives-arxiv-2506.09656.pdf`
   - `2026-agentic-skills-beyond-tool-use-in-llm-agents.pdf`
   - `2026-dehghantanha-homayoun-attack-surface-of-agentic-ai.pdf`
   - `2026-du-memory-for-autonomous-llm-agents.pdf`
   - `2026-kim-et-al-attack-and-defense-landscape-of-agentic-ai.pdf`
   - `2026-wang-et-al-role-playing-agents.pdf`
   - `2026-xu-et-al-tool-use-in-llm-agents.pdf`
   - `2026-yue-et-al-workflow-optimization-for-llm-agents.pdf`

> 注：上面列出 11 个文件名，但其中并不是“坏文件”；它们多数是**真综述但偏题**。真正必须处理的库存问题只有 1 个：重复的 `2602.11583`。

## 4. 数量汇总

基于本地目录与上述口径：

- 目录 PDF 总数：`20`
- 重复文件组数：`1`
- 重复冗余文件数：`1`（内联算术：`20 - 19 = 1`）
- 去重后唯一论文数：`19`
- 其中可视为“真正的 multi-agent 核心综述/调查”的唯一论文数：`8`（若把 Wu 2025 计入应用专题但仍属 multi-agent，则为 `9`）
- 其中“真综述但偏 agentic/专题边界”的唯一论文数：`10`（或在 Wu 2025 归入边界时为 `11`）

## 5. 缺口清单

### 5.1 结构性缺口

1. **核心 multi-agent 综述净数仍不足 10 篇**
   - 以较严格口径计算，当前目录里真正直接面向 multi-agent 主线的唯一论文只有 `8` 篇；
   - 若放宽把 `Wu 2025` 作为 multi-agent 应用专题计入，也只有 `9` 篇；
   - 因而距离“10 篇高相关 multi-agent 核心综述”的目标还差 `1-2` 篇。
   - Provenance: 本文件第 3 节分类 + `analysis/2026-03-26-final-selected-10-and-exclusion-list.md` + `analysis/2026-03-26-candidate-survey-judgment-and-top10.md`

2. **canonical reading set 混入边界综述**
   - 当前 canonical 10 篇中包含 `Xu 2026`、`Yue 2026`、`Wang 2026` 这 3 篇边界综述；
   - `candidate-survey-judgment-and-top10.md` 还指出更偏 multi-agent 主线的 `Game-Theoretic Lens on LLM-based Multi-Agent Systems` 可替换 `Wu 2025`。
   - 这说明“已精读稳定集”和“更严格的核心 multi-agent top 10”之间仍存在口径差。

### 5.2 库存治理缺口

1. **需要删除或归档重复文件 1 个**
   - `2602.11583` 当前落盘两次。
2. **需要给 literature/ 增加“canonical / non-canonical / duplicate”标记或清单**
   - 否则后续会话仅看目录会把全部 20 个 PDF 误当成同等优先级候选。
3. **需要补 1-2 篇更强的 multi-agent 主线综述来替换边界项**
   - 候选线索已在项目内出现：`Game-Theoretic Lens on LLM-based Multi-Agent Systems`、`Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents)` 等；
   - 但当前它们尚未以最终 canonical PDF 方式落盘到本目录。

## 6. 建议的最小后续动作

按紧急性排序：

1. **先去重**：删除/归档第二份 `2602.11583` 重复文件。
2. **再锁定核心口径**：明确最终目标是“通用 multi-agent 核心综述 10 篇”还是“multi-agent + agentic 邻近综述 10 篇”。
3. **若采用严格核心口径**：补下载并核验 `1-2` 篇更直接的 multi-agent 主线综述，用于替换 `Xu 2026 / Yue 2026 / Wang 2026` 中优先级最低者，或替换 `Wu 2025` 这一应用专题项。

## 7. 结论

`projects/multi-agent-review-survey/literature/` 当前共有 `20` 个 PDF，去重后为 `19` 篇唯一论文。目录中绝大多数文件都是真综述型文献，但它们并不都属于“multi-agent 核心综述”。当前最明确的问题不是“伪综述混入”，而是：

- 有 **1 个重复文件**；
- 有 **多篇 agentic/专题边界综述占据了原本应属于 core multi-agent surveys 的名额**；
- 因而按严格口径，目录里距离“10 篇高相关 multi-agent 核心综述”仍有 **1-2 篇缺口**。

## Provenance

- `projects/multi-agent-review-survey/analysis/2026-03-26-literature-metadata-inventory.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-final-selected-10-and-exclusion-list.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-survey-identity-evidence-chain-audit.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-latest-five-review-evidence-verification.md`
- 本会话 `python3` + `pypdf` + `sha256` 校验命令输出
