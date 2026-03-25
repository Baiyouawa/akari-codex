# 2026-03-26 候选综述交叉 review：剔除伪综述/教程/观点文/单篇方法总结/重复主题后的高质量 Top 10

- Timestamp: 2026-03-26T02:53:21+08:00
- Session: 绫-07-1774464764-3670ea
- Task: 对候选综述做交叉 review，剔除伪综述、教程、观点文、单篇方法总结和重复主题，最终确定 10 篇高质量综述清单
- Status: completed

## 1. 目标与口径

本次不是重复做一轮“有没有 10 篇可读论文”的宽松盘点，而是基于项目内已经落盘的候选池、survey 身份核验、`web_fetch` 元信息核验、PDF 库存盘点与最终名单审计，收紧为一份**高质量、主题尽量不重复、且更贴近 multi-agent 主线**的 Top 10。

本次交叉 review 重点剔除五类条目：

1. **伪综述**：标题像综述，但缺少 survey/review/SoK/taxonomy 自定位证据。
2. **教程/观点文**：主要在提倡方向、讲经验或展望，而非系统综述已有文献。
3. **单篇方法总结**：本质是围绕一个框架/系统/技能写的扩展说明，而不是文献综述。
4. **重复主题**：同一主题已有更强、更通用或更新的综述时，优先保留证据链更完整者。
5. **偏题边界项**：虽是真综述，但主题中心更像 agentic AI 邻近专题，而非 multi-agent 主线。

## 2. 使用的证据链

本次只使用仓库内既有工件，不新增无落盘断言：

1. 候选池初筛：`projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
2. 重新联网检索后的 20 篇候选池：`projects/multi-agent-review-survey/analysis/2026-03-26-web-search-redo-2024-2026-survey-candidates-and-pdf-refresh.md`
3. `web_fetch` 逐篇核验：`projects/multi-agent-review-survey/analysis/2026-03-26-web-fetch-candidate-validation.md`
4. survey 身份证据链审计：`projects/multi-agent-review-survey/analysis/2026-03-26-survey-identity-evidence-chain-audit.md`
5. 最新五篇边界论文核验：`projects/multi-agent-review-survey/analysis/2026-03-26-latest-five-review-evidence-verification.md`
6. 候选逐篇判定与重排：`projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
7. literature 库存缺口盘点：`projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-inventory-gap-list.md`
8. 当前 canonical reading set：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`

## 3. 交叉 review 判定规则

### 3.1 质量门槛

入选 Top 10 需同时满足：

- 年份位于 `2024-2026`；
- 有明确 survey/review/SoK/taxonomy 证据；
- 主题与 `multi-agent systems / LLM-based MAS / communication / collaboration / coordination / architecture` 直接相关，或是高价值总论/代表性应用综述；
- 与已入选条目相比不构成明显重复；
- 不是单一技能子题的狭窄扩写。

### 3.2 重复主题去重规则

- **communication**：保留一篇 general communication survey + 一篇更新、更方法论化的 communication survey，但不再继续堆叠第三篇同类综述。
- **general LLM-MAS overview**：保留 2024 基线、2024/2025 应用综述、2025 技术栈综述，形成时间演化，而不保留更多功能相近的总览综述。
- **agentic 邻近主题**：仅保留一篇能覆盖 single-agent → hierarchical multi-agent systems 的高质量总论；不同时保留 tool-use / workflow / role-play 三篇边界综述。

## 4. 剔除结论

### 4.1 明确剔除：不作为本轮高质量 Top 10 成员

| 条目 | 剔除原因 | 证据 |
|---|---|---|
| Xu 2026 — *The Evolution of Tool Use in LLM Agents* | 真综述，但中心是 multi-tool LLM agents；`web-fetch-candidate-validation.md` 将其判为“边界相关”，`survey-identity-evidence-chain-audit.md` 也注明其不是狭义 MAS 主线 | `analysis/2026-03-26-web-fetch-candidate-validation.md`; `analysis/2026-03-26-survey-identity-evidence-chain-audit.md` |
| Yue 2026 — *A Survey of Workflow Optimization for LLM Agents* | 真综述，但更偏 workflow / agentic computation graph；若保留它，再保留 general MAS 与 communication/collaboration 综述会造成主题配额挤占 | `analysis/2026-03-26-web-fetch-candidate-validation.md`; `analysis/2026-03-26-latest-five-review-evidence-verification.md` |
| Wang 2026 — *Role-Playing Agents Driven by Large Language Models* | 真综述，但更偏 social / role-playing 子方向；`web-fetch-candidate-validation.md` 判为“边界相关” | `analysis/2026-03-26-web-fetch-candidate-validation.md`; `analysis/2026-03-26-survey-identity-evidence-chain-audit.md` |
| 2602.04813 — *Agentic AI in Healthcare & Medicine* | 医疗垂直领域综述；`latest-five-review-evidence-verification.md` 明确建议剔除出核心清单 | `analysis/2026-03-26-latest-five-review-evidence-verification.md` |
| 2603.22928 / 2603.09002 / 2603.07670 等安全或 memory 专题综述 | 都是货真价实综述，但主题更窄，适合作为补位或专题层，不是本轮“高质量 multi-agent 主线 Top 10”首选 | `analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `analysis/2026-03-26-literature-pdf-inventory-gap-list.md` |
| 重复文件：第二份 `2602.11583` | 同一篇论文重复落盘，不构成独立入选项 | `analysis/2026-03-26-literature-pdf-inventory-gap-list.md` |

### 4.2 不是“伪综述”的说明

根据 `candidate-survey-judgment-and-top10.md` 与 `web-fetch-candidate-validation.md`，本轮主要被剔除的边界条目**大多仍是真综述**，被剔除的主因是**偏题或主题重复**，而不是“它们根本不是综述”。

## 5. 最终确定的 10 篇高质量综述清单

> 说明：这是面向“高质量 + multi-agent 主线 + 主题去重”口径的最终清单，不等同于此前为了下游精读交付而锁定的 canonical reading set。

| # | 论文 | 年份 | 保留理由 |
|---|---|---:|---|
| 1 | Guo et al. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* | 2024 | 2024 基线总览；`survey-identity-evidence-chain-audit.md` 给出摘要/引言/结论三重 survey 证据，是后续 2025-2026 综述的共同起点 |
| 2 | Li et al. — *A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges* | 2024 | 正式发表的 multi-agent systems 总综述，可补足 workflow/infrastructure/challenges 的系统化视角，且与 Guo 2024 构成同年不同焦点互补 | `analysis/2026-03-26-literature-metadata-inventory.md` |
| 3 | Chen et al. — *A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application* | 2024 | 通用 LLM-MAS 综述里更偏应用前沿，和 Guo/Li 形成“基础总览—系统构建—应用扩展”分工 | `analysis/2026-03-26-web-fetch-candidate-validation.md`; `analysis/2026-03-26-survey-identity-evidence-chain-audit.md` |
| 4 | Aratchige & Ilmini — *LLMs Working in Harmony* | 2025 | 2025 年技术栈综述，直接覆盖构建有效 LLM-based MAS 的核心技术要素，是 general MAS 主线高质量代表 | `analysis/2026-03-26-web-fetch-candidate-validation.md`; `analysis/2026-03-26-survey-identity-evidence-chain-audit.md` |
| 5 | Tran et al. — *Multi-Agent Collaboration Mechanisms: A Survey of LLMs* | 2025 | collaboration 主线综述；与 communication 综述形成互补而非重复 | `analysis/2026-03-26-web-fetch-candidate-validation.md`; `analysis/2026-03-26-survey-identity-evidence-chain-audit.md` |
| 6 | Yan et al. — *Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems* | 2025 | communication 主线综述；从 LLM-MAS 通信视角系统整理已有工作，是 2025 年最直接的 communication survey 之一 | `analysis/2026-03-26-web-fetch-candidate-validation.md`; `analysis/2026-03-26-survey-identity-evidence-chain-audit.md` |
| 7 | Wu et al. — *Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances* | 2025 | 保留 1 篇高质量垂直应用综述，用于补足“真实高约束场景中的 MAS”维度；避免 Top 10 全是通用综述 | `analysis/2026-03-26-survey-identity-evidence-chain-audit.md`; `analysis/2026-03-26-final-selected-10-and-exclusion-list.md` |
| 8 | Chen et al. — *The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why* | 2026 | 2026 年最强的 communication 核心 survey，方法学最完整；相较 Yan 2025 提供更统一的 Five Ws 框架 | `analysis/2026-03-26-web-fetch-candidate-validation.md`; `analysis/2026-03-26-latest-five-review-evidence-verification.md` |
| 9 | Hao et al. — *Game-Theoretic Lens on LLM-based Multi-Agent Systems* | 2026 | `candidate-survey-judgment-and-top10.md` 已指出它按“最新性+相关性”应优先于部分旧 canonical 成员；它补上理论统一视角，减少对边界 agentic 综述的依赖 | `analysis/2026-03-26-candidate-survey-judgment-and-top10.md`; `analysis/2026-03-26-web-fetch-candidate-validation.md` |
| 10 | *Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and Evaluation of Large Language Model Agents* | 2026 | 作为唯一保留的 agentic AI 总论条目，用于覆盖 single-agent → hierarchical multi-agent systems 的统一 taxonomy；比 tool-use/workflow/role-play 三篇边界综述更适合占据最后一个 Top 10 名额 | `analysis/2026-03-26-web-fetch-candidate-validation.md`; `analysis/2026-03-26-latest-five-review-evidence-verification.md` |

## 6. 为什么这份 Top 10 比旧 canonical reading set 更“高质量”

旧 canonical reading set 为了与已完成的 PDF 下载、结构化精读与中文主报告对齐，保留了：

- Xu 2026（tool use）
- Yue 2026（workflow optimization）
- Wang 2026（role-playing）

但 `survey-identity-evidence-chain-audit.md`、`web-fetch-candidate-validation.md` 与 `literature-pdf-inventory-gap-list.md` 已经共同说明：这三篇都属于**真综述但偏边界/专题**，而非最直接的 multi-agent 主线综述。

本次高质量 Top 10 用以下替换关系收紧口径：

- `Xu 2026` → `Li 2024`
- `Yue 2026` → `Hao 2026`
- `Wang 2026` → `Agentic AI 2601.12560`

这样得到的结果是：

- 通用 MAS 总览更完整；
- communication / collaboration / theory / application 四条主线更均衡；
- agentic 邻近综述只保留 1 篇总论，不再重复堆叠 tool/workflow/role-play 三个子方向。

## 7. 数量与去重核对

- 最终入选：`10` 篇。
- 其中通用/主线 multi-agent 综述：`8` 篇（Guo, Li, Chen-2412, Aratchige, Tran, Yan, Chen-2602, Hao）。
- agentic / 总论补位：`1` 篇（2601.12560）。
- 垂直应用补位：`1` 篇（Wu 2025）。
- 内联算术：`8 + 1 + 1 = 10`。

## 8. 结论

基于项目内既有候选池、`web_fetch` 核验、survey 身份证据链审计、candidate ranking 与 literature 缺口盘点，本次交叉 review 已完成：

1. 剔除重复文件与明显偏边界的专题综述；
2. 不把 tool-use / workflow / role-playing 等单一子题综述继续当作核心 multi-agent Top 10 成员；
3. 最终确定一份更严格、更平衡的 **10 篇高质量综述清单**。

这份清单应视为项目在“高质量候选筛选”任务下的最终答案；若后续还要继续做下载、精读或重写主报告，应以本文件为 stricter source of truth，再决定是否联动替换旧 canonical reading set。

## Provenance

- `projects/multi-agent-review-survey/analysis/2026-03-26-latest-multi-agent-survey-candidates.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-web-search-redo-2024-2026-survey-candidates-and-pdf-refresh.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-web-fetch-candidate-validation.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-survey-identity-evidence-chain-audit.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-latest-five-review-evidence-verification.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-inventory-gap-list.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-literature-metadata-inventory.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
