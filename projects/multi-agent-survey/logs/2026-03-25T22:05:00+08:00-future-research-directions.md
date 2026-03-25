# Session log — future research directions for multi-agent systems

- Session: 柑奈-02-1774446826-02348b
- Timestamp: 2026-03-25T22:05:00+08:00
- Task: 自由探索并提出5个最值得后续开展的研究课题方向；对每个方向给出问题定义、研究假设、方法设计、数据/benchmark、实验方案、评测指标、潜在风险与可行性分析
- Classification: ROUTINE
- Outcome: completed

## What was done

1. Read repository and project context:
   - `AGENTS.md`
   - `README.md`
   - `projects/multi-agent-survey/README.md`
   - `projects/multi-agent-survey/TASKS.md`
2. Read the repo-grounded survey materials that summarize the currently available corpus:
   - `projects/multi-agent-survey/analysis/2026-03-25-theme-synthesis.md`
   - `projects/multi-agent-survey/literature/icml-2023-2025.md`
   - `projects/multi-agent-survey/literature/2026-03-25-iclr-high-relevance-2025-2026.md`
   - `projects/multi-agent-survey/literature/neurips-2024-2025.md`
3. Synthesized a five-direction research agenda in `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`.
4. Updated `projects/multi-agent-survey/TASKS.md` to mark this task complete.

## Findings with provenance

- The current repo-grounded corpus is dominated by `多智能体LLM系统` and `协作规划`, which makes organization design and communication efficiency the most natural future directions.
  - Provenance: `projects/multi-agent-survey/analysis/2026-03-25-theme-synthesis.md` reports theme hits of `167` for `多智能体LLM系统` and `134` for `协作规划`, produced by `cd projects/multi-agent-survey && python3 scripts/classify_theme_synthesis.py`.
- Communication, alignment/safety, and evaluation also appear as strong secondary bottlenecks rather than niche topics.
  - Provenance: the same synthesis artifact reports `59` communication hits, `45` game/alignment hits, and `42` training/evaluation hits.
- The final five selected directions were:
  1. adaptive topology and role co-design,
  2. information-bottleneck communication,
  3. failure attribution and self-repair,
  4. safe tool-using multi-agent systems,
  5. transferable evaluation and training loops.
  - Provenance: `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`.
- Each proposed direction is tied back to concrete in-repo paper titles such as `Graph-of-Agents`, `Multi-Agent Design`, `KVComm`, `Cut the Crap`, `Which Agent Causes Task Failures and When?`, `DoVer`, `A2ASecBench`, `CoAct-1`, `LiveResearchBench`, and `MARTI`.
  - Provenance: titles appear in `projects/multi-agent-survey/literature/2026-03-25-iclr-high-relevance-2025-2026.md` and `projects/multi-agent-survey/literature/icml-2023-2025.md`.

## Deliverables

- `projects/multi-agent-survey/analysis/2026-03-25-future-research-directions.md`
- `projects/multi-agent-survey/TASKS.md`

## Notes

- This artifact is intentionally forward-looking and stays within repository provenance constraints by grounding every direction in title-level evidence and the existing theme synthesis, rather than inventing paper details not present in the repo.
- The next natural step would be to connect these five directions to the eventual KDD-style survey outline once the remaining blocked corpus tasks are unblocked.