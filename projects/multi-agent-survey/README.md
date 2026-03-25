# multi-agent-survey

Priority: high
Status: active
Mission: 小侑要求组织 Agent 集群开展大规模文献调研与综述写作，覆盖近三年 ICLR/ICML/NeurIPS 及近三个月 OpenReview 上 ICML 2026 的 multi-agent 相关论文，并产出下载清单、逐篇总结、未来课题设计与 KDD 风格 LaTeX 综述，适合并行拆分执行。

## Log

### 2026-03-25

项目创建。

- 2026-03-25T13:44:06Z — Recovered three previously deleted but still HEAD-addressable NeurIPS artifacts back into the working tree: `literature/neurips-2024-2025.md`, `scripts/harvest_neurips_crossref.py`, and `logs/2026-03-23T161441Z-neurips-2024-harvest.md`. Added `analysis/2026-03-25-neurips-inventory-recovery-and-gap-assessment.md` to record what this prior work does and does not satisfy. Provenance: `python3` + `git show HEAD:<path>` restored the files; session regex counting over `literature/neurips-2024-2025.md` printed `count_2024 138` and `count_2025 0`, confirming that the repository currently supports a 138-entry NeurIPS 2024 candidate pool but still lacks NeurIPS 2023 coverage, actual 2025 records, and the requested PDF/OpenReview/conference-page metadata.
- 2026-03-25T21:47:18+08:00 — Re-checked the assigned ICML 2026 OpenReview multi-agent harvest task and confirmed it remains blocked. Provenance: `list_files(path="projects/multi-agent-survey/literature", recursive=true)` showed no ICML 2026 OpenReview artifact; `list_files(path="projects/multi-agent-survey/analysis", recursive=true)` showed only the NeurIPS gap note; `read_file("projects/multi-agent-survey/logs/2026-03-25T21:43:41+08:00-icml-2026-openreview-blocked.md")` confirmed an earlier same-day blocked attempt; `search_text(pattern="ICML 2026|OpenReview|multi-agent", path="projects/multi-agent-survey", max_results=100)` returned no matches. Logged blocker details in `logs/2026-03-25T21:47:18+08:00-icml-2026-openreview-blocked.md` and updated `TASKS.md` to keep the task blocked until a local snapshot/export or an approved web-enabled session exists.

## Open questions

- 谁来提供最近三个月 ICML 2026 OpenReview 投稿列表的仓库内快照/导出，以便在零资源约束下完成结构化整理？
- 如果必须直接从 OpenReview 抓取，后续会话是否会提供获批的联网检索路径？
