# multi-agent-survey — 任务列表

- [ ] 检索并汇总近三年 ICLR 会议所有与 multi-agent 相关论文，筛选高相关条目并整理论文标题、作者、年份、链接、PDF下载地址、OpenReview/会议页面 [zero-resource] [blocked-by: 当前仓库仅能验证 ICLR 2025-2026 清单与高相关子集，未发现 ICLR 2024 inventory，因此无法满足“近三年 ICLR”完整覆盖]
  Done when: 基于可追溯来源补齐 ICLR 2024/2025/2026 高相关条目，并为每条提供标题、作者、年份、链接、PDF下载地址、OpenReview/会议页面
  Evidence: `projects/multi-agent-survey/literature/2026-03-25-iclr-high-relevance-2025-2026.md`; `projects/multi-agent-survey/logs/2026-03-25T21:44:14+08:00-iclr-high-relevance-subset.md`

- [x] 检索并汇总近三年 ICML 会议所有与 multi-agent 相关论文，筛选高相关条目并整理论文标题、作者、年份、链接、PDF下载地址、OpenReview/会议页面 [zero-resource]
  Completed: 2026-03-25T21:47:04+08:00
  Evidence: `projects/multi-agent-survey/literature/icml-2023-2025.md`; `projects/multi-agent-survey/scripts/harvest_icml_pmlr.py`; `projects/multi-agent-survey/logs/2026-03-25T21:47:04+08:00-icml-2023-2025-pmlr-harvest.md`

- [ ] 检索并汇总近三年 NeurIPS 会议所有与 multi-agent 相关论文，筛选高相关条目并整理论文标题、作者、年份、链接、PDF下载地址、OpenReview/会议页面 [zero-resource] [blocked-by: 当前仓库仅恢复出 NeurIPS 2024 的 138 条 Crossref 候选池，2025 在既有快照中为 0 条，且缺少 2023、PDF、OpenReview/会议页面元数据]
  Done when: 基于可追溯来源补齐 NeurIPS 2023/2024/2025 高相关条目，并为每条提供标题、作者、年份、链接、PDF下载地址、OpenReview/会议页面
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-neurips-inventory-recovery-and-gap-assessment.md`

- [ ] 检索最近三个月 OpenReview 上 ICML 2026 中与 multi-agent 相关的投稿/论文，整理标题、作者、提交时间、链接、PDF地址与主题归类 [zero-resource] [blocked-by: 当前仓库缺少最近三个月 ICML 2026 OpenReview 投稿列表的本地快照/导出，且本会话无获批联网检索路径；详见 `projects/multi-agent-survey/logs/2026-03-25T21:54:37+08:00-icml-2026-openreview-blocked-shamixiang.md`]
  Done when: 基于仓库内可追溯来源补齐最近三个月 ICML 2026 OpenReview multi-agent 投稿的标题、作者、提交时间、链接、PDF地址与主题归类
  Evidence: `projects/multi-agent-survey/logs/2026-03-25T21:54:37+08:00-icml-2026-openreview-blocked-shamixiang.md`

- [ ] 对每篇纳入论文撰写结构化总结，必须包含 Motivation、核心创新点、方法论/技术路线、任务设定、实验结论与局限 [zero-resource] [blocked-by: 当前仓库仅有标题级 inventory 与链接，缺少纳入论文的摘要、全文、实验细节或已验证笔记，无法在 provenance 约束下产出逐篇结构化总结；详见 `projects/multi-agent-survey/logs/2026-03-25T21:49:44+08:00-structured-summaries-blocked.md`]
  Done when: 每篇纳入论文都在仓库内具备可追溯内容来源（摘要、全文摘录或已验证笔记），并据此补齐 Motivation、核心创新点、方法论/技术路线、任务设定、实验结论与局限
  Evidence: `projects/multi-agent-survey/logs/2026-03-25T21:49:44+08:00-structured-summaries-blocked.md`

- [x] 对全部论文进行主题归类与横向综述，形成研究脉络：协作规划、通信、博弈/对齐、工具使用、多智能体LLM系统、训练与评测等 [zero-resource]
  Completed: 2026-03-25T21:58:14+08:00
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-theme-synthesis.md`; `projects/multi-agent-survey/analysis/2026-03-25-theme-classification.json`; `projects/multi-agent-survey/analysis/2026-03-25-theme-taxonomy-matrix.md`; `projects/multi-agent-survey/scripts/classify_theme_synthesis.py`; `projects/multi-agent-survey/logs/2026-03-25T21:58:14+08:00-theme-taxonomy-matrix.md`

- [x] 自由探索并提出5个最值得后续开展的研究课题方向；对每个方向给出问题定义、研究假设、方法设计、数据/benchmark、实验方案、评测指标、潜在风险与可行性分析 [zero-resource]
  Completed: 2026-03-25T22:05:00+08:00
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`; `projects/multi-agent-survey/logs/2026-03-25T22:05:00+08:00-future-research-directions.md`

- [x] 汇总所有引用与下载信息，生成标准化参考文献表与论文下载清单，确保链接可追溯 [zero-resource]
  Completed: 2026-03-25T22:01:52+08:00
  Evidence: `projects/multi-agent-survey/literature/2026-03-25-reference-table-and-download-manifest.md`; `projects/multi-agent-survey/logs/2026-03-25T21:55:15+08:00-reference-table-and-download-manifest.md`; `projects/multi-agent-survey/logs/2026-03-25T22:01:52+08:00-reference-manifest-task-closeout.md`

- [x] 撰写一篇完整的 LaTeX 综述论文，采用 KDD 风格结构，包含摘要、引言、相关工作、分类综述、逐方向分析、未来课题设计、结论与参考文献 [zero-resource]
  Completed: 2026-03-25T22:16:29+08:00
  Evidence: `projects/multi-agent-survey/paper/2026-03-25-kdd-style-multi-agent-survey.tex`; `projects/multi-agent-survey/logs/2026-03-25T22:06:18+08:00-fleet-侑-00-1774447517-67e5d0-kdd-style-survey.md`; `projects/multi-agent-survey/logs/2026-03-25T22:14:36+08:00-fleet-枫-05-1774448027-f90ccd-kdd-task-closeout.md`; `projects/multi-agent-survey/logs/2026-03-25T22:17:00+08:00-fleet-岛村-01-1774448153-bc66bc-kdd-survey-task-verification.md`

- [ ] 调研近三年 ICLR 上与 multi-agent 相关的论文，整理每篇论文的 Motivation、创新点、方法论、下载链接与简要综述 [zero-resource] [blocked-by: 当前仓库仅有 ICLR 2025-2026 metadata，缺少 ICLR 2024 inventory，且无摘要、全文摘录或已验证笔记支撑逐篇总结；详见 `projects/multi-agent-survey/logs/2026-03-25T22:14:01+08:00-fleet-由希奈-04-1774447997-36efe8-iclr-per-paper-summaries-blocked.md`]
  Done when: 仓库内补齐 ICLR 2024/2025/2026 纳入论文清单，并为每篇提供可追溯摘要、全文摘录或已验证笔记，再据此整理 Motivation、创新点、方法论、下载链接与简要综述
  Evidence: `projects/multi-agent-survey/literature/2026-03-25-iclr-high-relevance-2025-2026.md`; `projects/multi-agent-survey/logs/2026-03-25T22:14:01+08:00-fleet-由希奈-04-1774447997-36efe8-iclr-per-paper-summaries-blocked.md`

- [ ] 调研近三年 ICML 上与 multi-agent 相关的论文，整理每篇论文的 Motivation、创新点、方法论、下载链接与简要综述 [zero-resource] [blocked-by: 当前仓库仅有 `projects/multi-agent-survey/literature/icml-2023-2025.md` 的 83 篇标题/作者/链接级 metadata，缺少可支撑逐篇 Motivation、创新点、方法论与简要综述的摘要、全文摘录或已验证笔记；详见 `projects/multi-agent-survey/logs/2026-03-25T22:16:30+08:00-fleet-由希奈-04-1774448153-4fec1d-icml-per-paper-summaries-blocked.md`]
  Done when: 仓库内为 ICML 2023-2025 纳入论文补齐可追溯摘要、全文摘录或已验证笔记，并据此整理每篇论文的 Motivation、创新点、方法论、下载链接与简要综述
  Evidence: `projects/multi-agent-survey/literature/icml-2023-2025.md`; `projects/multi-agent-survey/logs/2026-03-25T22:16:30+08:00-fleet-由希奈-04-1774448153-4fec1d-icml-per-paper-summaries-blocked.md`

- [ ] 调研近三年 NeurIPS 上与 multi-agent 相关的论文，整理每篇论文的 Motivation、创新点、方法论、下载链接与简要综述 [zero-resource] [blocked-by: 当前仓库缺少 NeurIPS 2023/2025 完整纳入清单，且现有 NeurIPS artifact 仅含标题级候选条目与 DOI 链接，不含摘要/PDF/OpenReview/会议页面或已验证笔记，无法在 provenance 约束下写出逐篇 Motivation/创新点/方法论综述；详见 `projects/multi-agent-survey/logs/2026-03-25T22:10:02+08:00-neurips-per-paper-summaries-blocked-yui.md`]
  Done when: 基于仓库内可追溯来源补齐 NeurIPS 2023/2024/2025 纳入论文的清单、下载元数据与论文内容来源，并据此完成逐篇 Motivation、创新点、方法论、下载链接与简要综述
  Evidence: `projects/multi-agent-survey/logs/2026-03-25T22:10:02+08:00-neurips-per-paper-summaries-blocked-yui.md`; `projects/multi-agent-survey/analysis/2026-03-25-neurips-inventory-recovery-and-gap-assessment.md`; `projects/multi-agent-survey/literature/neurips-2024-2025.md`

- [ ] 调研最近三个月 OpenReview 上 ICML 2026 的 multi-agent 相关论文，整理每篇论文的 Motivation、创新点、方法论、下载链接与简要综述 [zero-resource] [blocked-by: 当前仓库缺少最近三个月 ICML 2026 OpenReview 投稿列表的本地快照/导出，且缺少这些论文的摘要、全文摘录或已验证笔记；详见 `projects/multi-agent-survey/logs/2026-03-25T22:31:53+08:00-fleet-理世-06-1774449059-3e4211-icml-2026-openreview-per-paper-blocked.md`]
  Done when: 仓库内补齐最近三个月 ICML 2026 OpenReview multi-agent 投稿清单，并为每篇提供可追溯摘要、全文摘录或已验证笔记，再据此整理 Motivation、创新点、方法论、下载链接与简要综述
  Evidence: `projects/multi-agent-survey/logs/2026-03-25T22:31:53+08:00-fleet-理世-06-1774449059-3e4211-icml-2026-openreview-per-paper-blocked.md`

- [x] 综合全部调研结果，提出 5 个最适合继续开展的研究课题方向，并为每个方向给出详细方法设计与切入建议 [zero-resource]
  Completed: 2026-03-25T22:16:36+08:00
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`; `projects/multi-agent-survey/logs/2026-03-25T22:16:36+08:00-fleet-智乃-02-1774448153-5d259e-research-directions-closeout.md`

- [ ] 调研近三年 ICLR 的 multi-agent 相关论文，逐篇整理 Motivation、创新点、方法论，并收集论文下载链接 [zero-resource] [blocked-by: 当前仓库仅有 ICLR 2025-2026 metadata，缺少 ICLR 2024 inventory，且无摘要、全文摘录或已验证笔记支撑逐篇 Motivation/创新点/方法论整理；详见 `projects/multi-agent-survey/logs/2026-03-25T22:16:29+08:00-fleet-结衣-03-1774448153-cf924a-iclr-per-paper-methodology-blocked.md`]
  Done when: 仓库内补齐 ICLR 2024/2025/2026 纳入论文清单，并为每篇提供可追溯摘要、全文摘录或已验证笔记，再据此整理 Motivation、创新点、方法论与下载链接
  Evidence: `projects/multi-agent-survey/literature/2026-03-25-iclr-high-relevance-2025-2026.md`; `projects/multi-agent-survey/logs/2026-03-25T22:16:29+08:00-fleet-结衣-03-1774448153-cf924a-iclr-per-paper-methodology-blocked.md`

- [ ] 调研近三年 ICML 的 multi-agent 相关论文，逐篇整理 Motivation、创新点、方法论，并收集论文下载链接 [zero-resource] [blocked-by: 当前仓库仅有 `projects/multi-agent-survey/literature/icml-2023-2025.md` 的 83 篇标题/作者/链接级 metadata，缺少可支撑逐篇 Motivation、创新点与方法论整理的摘要、全文摘录或已验证笔记；详见 `projects/multi-agent-survey/logs/2026-03-25T22:20:58+08:00-fleet-枫-05-1774448424-fe99a5-icml-per-paper-methodology-blocked.md`]
  Done when: 仓库内为 ICML 2023-2025 纳入论文补齐可追溯摘要、全文摘录或已验证笔记，并据此逐篇整理 Motivation、创新点、方法论与下载链接
  Evidence: `projects/multi-agent-survey/literature/icml-2023-2025.md`; `projects/multi-agent-survey/logs/2026-03-25T22:20:58+08:00-fleet-枫-05-1774448424-fe99a5-icml-per-paper-methodology-blocked.md`

- [ ] 调研近三年 NeurIPS 的 multi-agent 相关论文，逐篇整理 Motivation、创新点、方法论，并收集论文下载链接 [zero-resource] [blocked-by: 当前仓库仅有 NeurIPS 2024 的 `138` 条候选记录、2025 为 `0`、且缺少 2023 覆盖与 PDF/OpenReview/会议页面元数据；同时现有条目仅含 `Authors`、DOI `Link`、`Tags`、`Retrieved via query`，没有摘要、全文摘录或已验证笔记，无法在 provenance 约束下逐篇整理 Motivation、创新点、方法论与下载链接；详见 `projects/multi-agent-survey/logs/2026-03-25T22:41:32+08:00-fleet-枫-05-1774449660-faa7e8-neurips-per-paper-review-blocked.md`]
  Done when: 仓库内补齐 NeurIPS 2023/2024/2025 纳入论文清单，并为每篇提供 PDF/OpenReview/会议页面元数据以及可追溯摘要、全文摘录或已验证笔记，再据此逐篇整理 Motivation、创新点、方法论与下载链接
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-neurips-inventory-recovery-and-gap-assessment.md`; `projects/multi-agent-survey/literature/neurips-2024-2025.md`; `projects/multi-agent-survey/logs/2026-03-25T22:41:32+08:00-fleet-枫-05-1774449660-faa7e8-neurips-per-paper-review-blocked.md`

- [ ] 调研最近三个月 OpenReview 上 ICML 2026 的 multi-agent 相关论文，逐篇整理 Motivation、创新点、方法论，并收集论文下载链接 [zero-resource]
  Done when: TBD

- [x] 基于上述论文提出 5 个最适合继续开展的研究课题/方向，并为每个方向给出详细方法设计 [zero-resource]
  Completed: 2026-03-25T22:44:14+08:00
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`; `projects/multi-agent-survey/logs/2026-03-25T22:44:14+08:00-fleet-花阳-06-1774449810-e08dbd-research-directions-closeout.md`

- [x] 汇总全部调研结果并形成最终综述报告 [zero-resource]
  Completed: 2026-03-25T22:25:42+08:00
  Evidence: `projects/multi-agent-survey/paper/2026-03-25-kdd-style-multi-agent-survey.tex`; `projects/multi-agent-survey/analysis/2026-03-25-theme-synthesis.md`; `projects/multi-agent-survey/literature/2026-03-25-reference-table-and-download-manifest.md`; `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`; `projects/multi-agent-survey/logs/2026-03-25T22:25:42+08:00-fleet-结衣-03-1774448699-f66c79-final-survey-closeout.md`

- [ ] 调研近三年 ICLR 的 multi-agent 相关论文，筛选并整理每篇论文的 Motivation、创新点、方法论、论文下载链接与简要综述 [zero-resource] [blocked-by: 当前仓库仅有 ICLR 2025-2026 metadata，缺少 ICLR 2024 inventory，且无摘要、全文摘录或已验证笔记支撑逐篇 Motivation/创新点/方法论与简要综述；详见 `projects/multi-agent-survey/logs/2026-03-25T22:35:22+08:00-fleet-岛村-01-1774449300-e674b9-iclr-per-paper-review-blocked.md`]
  Done when: 仓库内补齐 ICLR 2024/2025/2026 纳入论文清单，并为每篇提供可追溯摘要、全文摘录或已验证笔记，再据此筛选整理每篇论文的 Motivation、创新点、方法论、论文下载链接与简要综述
  Evidence: `projects/multi-agent-survey/literature/2026-03-25-iclr-high-relevance-2025-2026.md`; `projects/multi-agent-survey/logs/2026-03-25T22:35:22+08:00-fleet-岛村-01-1774449300-e674b9-iclr-per-paper-review-blocked.md`

- [ ] 调研近三年 ICML 的 multi-agent 相关论文，筛选并整理每篇论文的 Motivation、创新点、方法论、论文下载链接与简要综述 [zero-resource] [blocked-by: 当前仓库仅有 `projects/multi-agent-survey/literature/icml-2023-2025.md` 的 83 篇标题/作者/链接级 metadata，缺少可支撑逐篇 Motivation、创新点、方法论与简要综述的摘要、全文摘录或已验证笔记；详见 `projects/multi-agent-survey/logs/2026-03-25T22:31:51+08:00-fleet-侑-08-1774449059-91011e-icml-per-paper-review-blocked.md`]
  Done when: 仓库内为 ICML 2023-2025 纳入论文补齐可追溯摘要、全文摘录或已验证笔记，并据此筛选整理每篇论文的 Motivation、创新点、方法论、论文下载链接与简要综述
  Evidence: `projects/multi-agent-survey/literature/icml-2023-2025.md`; `projects/multi-agent-survey/logs/2026-03-25T22:31:51+08:00-fleet-侑-08-1774449059-91011e-icml-per-paper-review-blocked.md`

- [ ] 调研近三年 NeurIPS 的 multi-agent 相关论文，筛选并整理每篇论文的 Motivation、创新点、方法论、论文下载链接与简要综述 [zero-resource] [blocked-by: 当前仓库仅有 NeurIPS 2024 的 `138` 条候选记录、2025 为 `0`、且缺少 2023 覆盖；现有条目仅含标题级 metadata 与 DOI 链接，不含 PDF/OpenReview/会议页面、摘要、全文摘录或已验证笔记，无法在 provenance 约束下整理逐篇 Motivation、创新点、方法论、下载链接与简要综述；详见 `projects/multi-agent-survey/logs/2026-03-25T22:41:32+08:00-fleet-枫-05-1774449660-faa7e8-neurips-per-paper-review-blocked.md`]
  Done when: 仓库内补齐 NeurIPS 2023/2024/2025 纳入论文清单，并为每篇提供 PDF/OpenReview/会议页面元数据以及可追溯摘要、全文摘录或已验证笔记，再据此筛选整理每篇论文的 Motivation、创新点、方法论、论文下载链接与简要综述
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-neurips-inventory-recovery-and-gap-assessment.md`; `projects/multi-agent-survey/literature/neurips-2024-2025.md`; `projects/multi-agent-survey/logs/2026-03-25T22:41:32+08:00-fleet-枫-05-1774449660-faa7e8-neurips-per-paper-review-blocked.md`

- [ ] 调研最近三个月 OpenReview 上 ICML 2026 的 multi-agent 相关论文，整理每篇论文的 Motivation、创新点、方法论、论文下载链接与简要综述 [zero-resource] [blocked-by: 当前仓库缺少最近三个月 ICML 2026 OpenReview 投稿列表的本地快照/导出，且缺少这些论文的摘要、全文摘录或已验证笔记；详见 `projects/multi-agent-survey/logs/2026-03-25T22:47:33+08:00-fleet-灯里-08-1774450021-b9068e-icml-2026-openreview-per-paper-review-blocked.md`]
  Done when: 仓库内补齐最近三个月 ICML 2026 OpenReview multi-agent 投稿清单，并为每篇提供可追溯摘要、全文摘录或已验证笔记，再据此整理每篇论文的 Motivation、创新点、方法论、论文下载链接与简要综述
  Evidence: `projects/multi-agent-survey/logs/2026-03-25T22:47:33+08:00-fleet-灯里-08-1774450021-b9068e-icml-2026-openreview-per-paper-review-blocked.md`

- [x] 基于上述论文综述，提出 5 个最适合继续开展的研究课题/方向，并给出每个方向的详细方法设计 [zero-resource]
  Completed: 2026-03-25T22:44:14+08:00
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`; `projects/multi-agent-survey/logs/2026-03-25T22:44:14+08:00-fleet-花阳-06-1774449810-e08dbd-research-directions-closeout.md`

- [x] 汇总全部调研结果，形成最终综述报告 [zero-resource]
  Completed: 2026-03-25T22:25:42+08:00
  Evidence: `projects/multi-agent-survey/paper/2026-03-25-kdd-style-multi-agent-survey.tex`; `projects/multi-agent-survey/analysis/2026-03-25-theme-synthesis.md`; `projects/multi-agent-survey/literature/2026-03-25-reference-table-and-download-manifest.md`; `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`; `projects/multi-agent-survey/logs/2026-03-25T22:25:42+08:00-fleet-结衣-03-1774448699-f66c79-final-survey-closeout.md`

- [ ] 调研近三年 ICLR 的 multi-agent 相关论文，整理每篇论文的 Motivation、创新点、方法论与获取方式 [zero-resource]
  Done when: TBD

- [ ] 调研近三年 ICML 的 multi-agent 相关论文，整理每篇论文的 Motivation、创新点、方法论与获取方式 [zero-resource]
  Done when: TBD

- [ ] 调研近三年 NeurIPS 的 multi-agent 相关论文，整理每篇论文的 Motivation、创新点、方法论与获取方式 [zero-resource] [blocked-by: 当前仓库仅有 NeurIPS 2024 的 `138` 条候选记录、2025 为 `0`、且缺少 2023 覆盖；现有条目仅含 `Authors`、DOI `Link`、`Tags`、`Retrieved via query`，不含摘要、全文摘录或已验证笔记，也缺少 PDF/OpenReview/会议页面等获取方式元数据；详见 `projects/multi-agent-survey/logs/2026-03-25T22:58:10+08:00-fleet-侑-08-1774450652-74a259-neurips-per-paper-methodology-blocked.md`]
  Done when: 仓库内补齐 NeurIPS 2023/2024/2025 纳入论文清单，并为每篇提供可追溯摘要、全文摘录或已验证笔记以及 PDF/OpenReview/会议页面等获取方式元数据，再据此整理每篇论文的 Motivation、创新点、方法论与获取方式
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-neurips-inventory-recovery-and-gap-assessment.md`; `projects/multi-agent-survey/literature/neurips-2024-2025.md`; `projects/multi-agent-survey/logs/2026-03-25T22:58:10+08:00-fleet-侑-08-1774450652-74a259-neurips-per-paper-methodology-blocked.md`

- [ ] 调研近三个月 OpenReview 上 ICML 2026 的 multi-agent 相关论文，整理每篇论文的 Motivation、创新点、方法论与获取方式 [zero-resource]
  Done when: TBD

- [ ] 基于全部调研结果撰写综述，并提出 5 个最适合继续做的课题方向及详细方法设计 [zero-resource]
  Done when: TBD
