# multi-agent-survey

Priority: high
Status: active
Mission: 小侑要求组织 Agent 集群开展大规模文献调研与综述写作，覆盖近三年 ICLR/ICML/NeurIPS 及近三个月 OpenReview 上 ICML 2026 的 multi-agent 相关论文，并产出下载清单、逐篇总结、未来课题设计与 KDD 风格 LaTeX 综述，适合并行拆分执行。

## Log

### 2026-03-25

项目创建。

- 2026-03-25T13:44:06Z — Recovered three previously deleted but still HEAD-addressable NeurIPS artifacts back into the working tree: `literature/neurips-2024-2025.md`, `scripts/harvest_neurips_crossref.py`, and `logs/2026-03-23T161441Z-neurips-2024-harvest.md`. Added `analysis/2026-03-25-neurips-inventory-recovery-and-gap-assessment.md` to record what this prior work does and does not satisfy. Provenance: `python3` + `git show HEAD:<path>` restored the files; session regex counting over `literature/neurips-2024-2025.md` printed `count_2024 138` and `count_2025 0`, confirming that the repository currently supports a 138-entry NeurIPS 2024 candidate pool but still lacks NeurIPS 2023 coverage, actual 2025 records, and the requested PDF/OpenReview/conference-page metadata.
- 2026-03-25T21:44:14+08:00 — Recovered the in-repo ICLR 2025-2026 inventory into the working tree and distilled it into `literature/2026-03-25-iclr-high-relevance-2025-2026.md`, a 26-paper high-relevance subset with title, authors, year, OpenReview URL, derived PDF URL, and conference-page provenance. Provenance: `projects/multi-agent-survey/literature/iclr-2025-2026.md` reports `2025 papers listed: 54`, `2026 papers listed: 92`, total `146`; the new subset artifact records `6` selected papers from 2025 and `20` from 2026, with inline arithmetic `6 + 20 = 26`. Caveat: no in-repo ICLR 2024 artifact was found in this session, so the full “近三年 ICLR” task remains incomplete.
- 2026-03-25T21:50:40+08:00 — Re-checked the repository for the assigned ICML 2026 OpenReview harvest task and confirmed it remains blocked. Provenance: `projects/multi-agent-survey/literature/icml-2023-2025.md` is limited to PMLR-based ICML 2023-2025 coverage and reports `0` listed papers; `search_text(pattern="OpenReview|ICML 2026|multi-agent|multi agent|Multi-Agent", path="projects/multi-agent-survey", max_results=200)` returned no matches; the blocker evidence is recorded in `projects/multi-agent-survey/logs/2026-03-25T21:43:41+08:00-icml-2026-openreview-blocked.md`, `projects/multi-agent-survey/logs/2026-03-25T21:47:18+08:00-icml-2026-openreview-blocked.md`, and `projects/multi-agent-survey/logs/2026-03-25T21:50:40+08:00-icml-2026-openreview-blocked-third-check.md`.

## Open questions

- Where should the repository store a durable snapshot/export of ICML 2026 OpenReview submissions so fleet workers can complete the requested recent-three-month harvest without relying on unrecorded external browsing?
