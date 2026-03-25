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

- [ ] 对全部论文进行主题归类与横向综述，形成研究脉络：协作规划、通信、博弈/对齐、工具使用、多智能体LLM系统、训练与评测等 [zero-resource]
  Done when: 基于仓库内可验证文献清单输出一份带主题计数、代表论文与研究脉络的横向综述，并为计数提供脚本级 provenance
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-theme-synthesis.md`; `projects/multi-agent-survey/scripts/classify_theme_synthesis.py`

- [x] 自由探索并提出5个最值得后续开展的研究课题方向；对每个方向给出问题定义、研究假设、方法设计、数据/benchmark、实验方案、评测指标、潜在风险与可行性分析 [zero-resource]
  Completed: 2026-03-25T22:05:00+08:00
  Evidence: `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`; `projects/multi-agent-survey/logs/2026-03-25T22:05:00+08:00-future-research-directions.md`

- [ ] 汇总所有引用与下载信息，生成标准化参考文献表与论文下载清单，确保链接可追溯 [zero-resource]
  Done when: TBD

- [ ] 撰写一篇完整的 LaTeX 综述论文，采用 KDD 风格结构，包含摘要、引言、相关工作、分类综述、逐方向分析、未来课题设计、结论与参考文献 [zero-resource]
  Done when: TBD
