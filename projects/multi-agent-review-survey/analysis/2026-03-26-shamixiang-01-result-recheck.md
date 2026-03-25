# 2026-03-26 沙弥香-01 新结果复核：是否把普通论文当综述、把旧论文当最新、或遗漏证据链

- Time: 2026-03-26T02:44:53+08:00
- Session: 沙弥香-01-1774464253-f4648d
- Scope: 复核项目内与“最新 multi-agent 综述”相关的既有结果，重点检查三类问题：
  1. 是否把普通论文误判为综述/survey/SoK；
  2. 是否把旧论文误判为“最新”；
  3. 是否存在证据链不完整。

## 复核对象

本次只复核项目内已落盘、且直接涉及“最新综述筛选/核验/最终名单”的三份关键工件：

1. `analysis/2026-03-26-latest-five-review-evidence-verification.md`
2. `analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
3. `analysis/2026-03-26-final-selected-10-and-exclusion-list.md`

## 复核结论总表

| 检查项 | 结论 | 证据 |
|---|---|---|
| 是否把普通论文误判为综述 | **未发现** | 三份工件对入选/边界/剔除条目均给出 `survey` / `review` / `SoK` / `systematization` / taxonomy 类自定位证据句；例如 `2602.11583` 在标题、摘要、引言、方法、结论五处都明确是 survey。来源：`analysis/2026-03-26-latest-five-review-evidence-verification.md`，`analysis/2026-03-26-candidate-survey-judgment-and-top10.md`。 |
| 是否把旧论文误判为“最新” | **未发现硬错误，但存在“最新”口径需结合时间窗理解** | `candidate-survey-judgment-and-top10.md` 明确以 `2026 > 2025 > 2024` 排序，且候选池限定在 `2024-2026`；最终名单中最早为 2024 两篇，属于项目定义的最近时间窗基线，而不是把更旧论文误当最新。来源：`analysis/2026-03-26-candidate-survey-judgment-and-top10.md`；`analysis/2026-03-26-final-selected-10-and-exclusion-list.md`。 |
| 是否存在证据链不完整 | **存在轻微口径风险，但主证据链完整** | 主名单工件已提供来源链接、PDF 链接、年份、survey 证据句与入选/剔除理由；但 `latest-five-review-evidence-verification.md` 与最终 canonical 10 篇并非同一任务口径，一个是“最新五篇候选核验”，另一个是“最终 10 篇 canonical reading set”。这不是证据缺失，而是需要显式区分用途。 |

## 详细复核

### 1. 是否把普通论文误判为综述

结论：**未发现把普通方法论文误判为综述的情况。**

原因：

- `analysis/2026-03-26-latest-five-review-evidence-verification.md` 对最新五篇候选逐篇核查了标题、摘要、引言、结论中的综述定位用语，并明确区分了：
  - **保留**：`2602.11583`
  - **边界保留**：`2603.22928`、`2603.22386`、`2601.12560`
  - **剔除**：`2602.04813`
- 该工件明确指出：真正要防止的不是“把普通论文误判成综述”，而是“把广义 agentic AI 综述误判成 multi-agent 核心综述”。
- `analysis/2026-03-26-candidate-survey-judgment-and-top10.md` 也写明：本轮 19 篇候选里，**19/19 都是综述型文献**；筛选的关键不是真假综述，而是与 multi-agent 主线的距离。

因此，沙弥香-01 关联结果并没有犯“把普通论文当综述”的硬错误。

### 2. 是否把旧论文误判为“最新”

结论：**未发现“旧论文误判为最新”的硬错误。**

原因：

- `analysis/2026-03-26-candidate-survey-judgment-and-top10.md` 的排序规则明确写成：`2026 > 2025 > 2024`。
- 最终 10 篇中保留 2024 论文，是为了构成 `2024-2026` 时间窗下的近年基线综述，而不是声称这些论文是“全体候选里最晚发表”。
- `analysis/2026-03-26-final-selected-10-and-exclusion-list.md` 也明确把 2024、2025、2026 三个年份都列出，并说明最终 canonical reading set 需要同时满足“已筛选”“已下载”“已核验”“已进入中文主报告”四个条件。

也就是说，这里使用的是**项目时间窗内的最新相关综述集**，不是只保留“最晚月份的 10 篇”。该口径在项目文档内是一致的。

### 3. 是否存在证据链不完整

结论：**主证据链完整，但要区分两个不同清单的用途。**

已具备的证据链：

- `analysis/2026-03-26-final-selected-10-and-exclusion-list.md`：给出最终入选 10 篇与剔除 9 篇，逐篇包含来源链接、PDF 链接、年份、survey 证据句与入选/剔除理由。
- `analysis/2026-03-26-candidate-survey-judgment-and-top10.md`：给出 19 篇候选逐篇 survey 判定，并说明 top 10 的重排逻辑。
- `analysis/2026-03-26-latest-five-review-evidence-verification.md`：对“最新五篇候选”做摘要/引言/结论层面的细粒度核验。

需要补充说明的口径风险：

- `latest-five-review-evidence-verification.md` 的对象是“最新五篇候选综述”；
- `final-selected-10-and-exclusion-list.md` 的对象是“项目最终 canonical 10 篇”；
- 这两者服务于不同任务：前者回答“最新五篇里哪些是核心/边界/剔除”，后者回答“项目最终交付用哪 10 篇”。

因此，这里不是证据链缺失，而是**多层清单并存**。只要后续引用时明确“最新五篇候选核验”与“最终 10 篇交付清单”不是同一个列表，就不会造成事实混淆。

## 本次复核给出的最终判断

### 可以确认成立的结论

1. **未发现把普通研究论文当成综述论文的错误。**
2. **未发现把 2023 及更早论文误说成最新的错误。** 当前时间窗明确是 `2024-2026`。
3. **主证据链完整。** 最终名单、候选重排、最新五篇核验三份工件可以互相回链。

### 需要后续使用时显式说明的事项

1. “最新五篇候选核验”不等于“最终 canonical 10 篇名单”。
2. `candidate-survey-judgment-and-top10.md` 中的“按最新性+相关性重排 top 10”与最终 canonical 10 篇存在 1 篇差异，这一点已经在该工件和 `final-selected-10-and-exclusion-list.md` 中写明：
   - 重排版更倾向保留 `Hao 2026`
   - canonical reading set 仍保留 `Wu 2025`
3. 因为最终中文主报告、PDF 下载与结构化精读已经围绕 canonical 10 篇落盘，所以当前项目的 source of truth 仍应以 `final-selected-10-and-exclusion-list.md` 和 `ten-paper-metadata.md` 为准。

## 结论

沙弥香-01 的新结果**通过复核**：

- 没有把普通论文误认成综述；
- 没有把超出时间窗的旧论文误说成最新；
- 证据链总体完整；
- 主要需要注意的是“最新五篇候选核验”与“最终 10 篇 canonical 清单”属于不同层次的交付物，后续引用时应明确其用途。

## Provenance

- `projects/multi-agent-review-survey/analysis/2026-03-26-latest-five-review-evidence-verification.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-candidate-survey-judgment-and-top10.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-final-selected-10-and-exclusion-list.md`
