# multi-agent-survey

Priority: high
Status: active
Mission: 小侑要求组织 Agent 集群开展大规模文献调研与综述写作，覆盖近三年 ICLR/ICML/NeurIPS 及近三个月 OpenReview 上 ICML 2026 的 multi-agent 相关论文，并产出下载清单、逐篇总结、未来课题设计与 KDD 风格 LaTeX 综述，适合并行拆分执行。

## Log

### 2026-03-25

项目创建。

- 2026-03-25T13:44:06Z — Recovered three previously deleted but still HEAD-addressable NeurIPS artifacts back into the working tree: `literature/neurips-2024-2025.md`, `scripts/harvest_neurips_crossref.py`, and `logs/2026-03-23T161441Z-neurips-2024-harvest.md`. Added `analysis/2026-03-25-neurips-inventory-recovery-and-gap-assessment.md` to record what this prior work does and does not satisfy. Provenance: `python3` + `git show HEAD:<path>` restored the files; session regex counting over `literature/neurips-2024-2025.md` printed `count_2024 138` and `count_2025 0`, confirming that the repository currently supports a 138-entry NeurIPS 2024 candidate pool but still lacks NeurIPS 2023 coverage, actual 2025 records, and the requested PDF/OpenReview/conference-page metadata.
- 2026-03-25T21:44:14+08:00 — Recovered the in-repo ICLR 2025-2026 inventory into the working tree and distilled it into `literature/2026-03-25-iclr-high-relevance-2025-2026.md`, a 26-paper high-relevance subset with title, authors, year, OpenReview URL, derived PDF URL, and conference-page provenance. Provenance: `projects/multi-agent-survey/literature/iclr-2025-2026.md` reports `2025 papers listed: 54`, `2026 papers listed: 92`, total `146`; the new subset artifact records `6` selected papers from 2025 and `20` from 2026, with inline arithmetic `6 + 20 = 26`. Caveat: no in-repo ICLR 2024 artifact was found in this session, so the full “近三年 ICLR” task remains incomplete.
- 2026-03-25T21:47:04+08:00 — Harvested an ICML 2023-2025 high-relevance multi-agent inventory into `literature/icml-2023-2025.md` and recorded the reproducible parser in `scripts/harvest_icml_pmlr.py`. Provenance: the script parsed `https://proceedings.mlr.press/v202/`, `https://proceedings.mlr.press/v235/`, and `https://proceedings.mlr.press/v267/`; verification over the generated markdown counted `2023=22`, `2024=22`, `2025=39`, so inline arithmetic gives `22 + 22 + 39 = 83`, and a second regex check found `pdf_fields 83` plus `openreview_fields 83`, confirming per-entry PDF and OpenReview metadata coverage.
- 2026-03-25T21:49:44+08:00 — Checked whether the repo can support per-paper structured summaries and found the task blocked by missing paper-content sources. Provenance: `projects/multi-agent-survey/literature/2026-03-25-iclr-high-relevance-2025-2026.md`, `projects/multi-agent-survey/literature/iclr-2025-2026.md`, and `projects/multi-agent-survey/literature/neurips-2024-2025.md` provide title/authors/links/tags but not abstracts, methods, experiments, or limitations; `search_text(pattern="Abstract:|摘要|Motivation|核心创新点|实验结论|局限|方法论/技术路线", path="projects/multi-agent-survey/literature", max_results=200)` and `search_text(pattern="abstract|summary|motivation|limitation", path="projects/multi-agent-survey", max_results=200)` returned no matches. Logged blocker details in `logs/2026-03-25T21:49:44+08:00-structured-summaries-blocked.md` and kept the task blocked until repository-local abstracts/full texts/notes or approved retrieval-derived notes are added.
- 2026-03-25T21:54:37+08:00 — Re-checked the zero-resource ICML 2026 OpenReview assignment and confirmed it remains blocked after a fourth repository-only pass. Provenance: `list_files(path="projects/multi-agent-survey", recursive=true)` still showed no ICML 2026 OpenReview inventory/export artifact; `read_file("projects/multi-agent-survey/logs/2026-03-25T21:43:41+08:00-icml-2026-openreview-blocked.md")`, `read_file("projects/multi-agent-survey/logs/2026-03-25T21:47:18+08:00-icml-2026-openreview-blocked.md")`, and `read_file("projects/multi-agent-survey/logs/2026-03-25T21:50:40+08:00-icml-2026-openreview-blocked-third-check.md")` show the same blocker diagnosis; `git_status()` showed only unrelated pending changes `.fleet/claims.json` and `projects/multi-agent-survey/analysis/2026-03-25-theme-synthesis.md`, not a hidden local ICML 2026 source snapshot.

## Open questions

- 谁来提供最近三个月 ICML 2026 OpenReview 投稿列表的仓库内快照/导出，以便在零资源约束下完成结构化整理？
- 如果必须直接从 OpenReview 抓取，后续会话是否会提供获批的联网检索路径？
- 谁来把纳入论文的摘要、PDF、全文摘录或已验证笔记写入仓库，以便在不猜测的前提下产出逐篇结构化总结？
