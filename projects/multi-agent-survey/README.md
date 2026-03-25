# multi-agent-survey

Priority: high
Status: active
Mission: 小侑要求组织 Agent 集群开展大规模文献调研与综述写作，覆盖近三年 ICLR/ICML/NeurIPS 及近三个月 OpenReview 上 ICML 2026 的 multi-agent 相关论文，并产出下载清单、逐篇总结、未来课题设计与 KDD 风格 LaTeX 综述，适合并行拆分执行。

## Log

### 2026-03-25

项目创建。

- 2026-03-25T13:44:06Z — Recovered three previously deleted but still HEAD-addressable NeurIPS artifacts back into the working tree: `literature/neurips-2024-2025.md`, `scripts/harvest_neurips_crossref.py`, and `logs/2026-03-23T161441Z-neurips-2024-harvest.md`. Added `analysis/2026-03-25-neurips-inventory-recovery-and-gap-assessment.md` to record what this prior work does and does not satisfy. Provenance: `python3` + `git show HEAD:<path>` restored the files; session regex counting over `literature/neurips-2024-2025.md` printed `count_2024 138` and `count_2025 0`, confirming that the repository currently supports a 138-entry NeurIPS 2024 candidate pool but still lacks NeurIPS 2023 coverage, actual 2025 records, and the requested PDF/OpenReview/conference-page metadata.
- 2026-03-25T21:44:14+08:00 — Recovered the in-repo ICLR 2025-2026 inventory into the working tree and distilled it into `literature/2026-03-25-iclr-high-relevance-2025-2026.md`, a 26-paper high-relevance subset with title, authors, year, OpenReview URL, derived PDF URL, and conference-page provenance. Provenance: `projects/multi-agent-survey/literature/iclr-2025-2026.md` reports `2025 papers listed: 54`, `2026 papers listed: 92`, total `146`; the new subset artifact records `6` selected papers from 2025 and `20` from 2026, with inline arithmetic `6 + 20 = 26`. Caveat: no in-repo ICLR 2024 artifact was found in this session, so the full “近三年 ICLR” task remains incomplete.
- 2026-03-25T22:05:00+08:00 — Added a repo-grounded thematic synthesis at `analysis/2026-03-25-theme-synthesis.md` and a reproducible classifier script at `scripts/classify_theme_synthesis.py` for the cross-paper review task. Provenance: `cd projects/multi-agent-survey && python3 scripts/classify_theme_synthesis.py` counted `367` total entries from `83` ICML + `146` ICLR + `138` NeurIPS papers, and theme hits of `134` 协作规划, `59` 通信, `45` 博弈/对齐, `14` 工具使用, `167` 多智能体LLM系统, and `42` 训练与评测; because entries can map to multiple themes, these are overlapping theme-hit counts rather than a partition.
- 2026-03-25T22:05:00+08:00 — Added `analysis/2026-03-25-future-research-directions.md`, which proposes five follow-up research directions with problem definitions, hypotheses, method sketches, benchmark choices, experiment plans, metrics, risks, and feasibility notes. Provenance: the artifact is grounded in `analysis/2026-03-25-theme-synthesis.md` plus paper-title evidence from `literature/icml-2023-2025.md`, `literature/2026-03-25-iclr-high-relevance-2025-2026.md`, and `literature/neurips-2024-2025.md`; the ranking rationale reuses theme-hit counts `167`, `134`, `59`, `45`, and `42` from the classifier-backed synthesis.

## Open questions

- 谁来提供最近三个月 ICML 2026 OpenReview 投稿列表的仓库内快照/导出，以便在零资源约束下完成结构化整理？
- 如果必须直接从 OpenReview 抓取，后续会话是否会提供获批的联网检索路径？
- 谁来把纳入论文的摘要、PDF、全文摘录或已验证笔记写入仓库，以便在不猜测的前提下产出逐篇结构化总结？