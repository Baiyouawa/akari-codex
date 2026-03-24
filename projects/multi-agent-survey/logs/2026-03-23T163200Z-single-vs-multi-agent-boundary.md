# Session Log — Single-Agent + Tools vs Multi-Agent Boundary

- Timestamp: 2026-03-23T16:32:00Z
- Project: `projects/multi-agent-survey`
- Task: investigate open question in project README
- Classification: ROUTINE
- Status: partial answer recorded; external research required for stronger conclusion

## Summary

Searched the current repository for prior analysis on the performance boundary between multi-agent systems and single-agent + tools. No existing synthesized note was found. Based on the current in-repo evidence, I wrote a provisional answer into `projects/multi-agent-survey/README.md` and explicitly marked the remaining evidence gap.

## Findings

1. There is no prior in-repo synthesis directly answering the boundary question.
   - Provenance: `search_text` over `projects/multi-agent-survey` and repo root for `性能边界`, `什么时候值得用多智能体`, `single-agent`, `single agent`, `multi-agent`, `multi agent`, `tool use`, and `tools` returned no relevant matches.

2. The only current literature artifact in this project is the NeurIPS 2024-2025 candidate list.
   - Provenance: `list_files("projects/multi-agent-survey/literature", recursive=true)` returned only `projects/multi-agent-survey/literature/neurips-2024-2025.md`.

3. The current artifact supports only a title-level, not benchmark-level, answer.
   - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md` contains titles suggestive of multi-agent value under coordination/communication/interacting-policy settings, including `Multi-Agent Coordination via Multi-Level Communication`, `Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication`, `N-agent Ad Hoc Teamwork`, `ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination`, `WFCRL: A Multi-Agent Reinforcement Learning Benchmark for Wind Farm Control`, and `Secret Collusion among AI Agents: Multi-Agent Deception via Steganography`.

4. The same artifact also contains single-agent/tool-centric baselines that make "single-agent + tools first" a defensible default hypothesis.
   - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md` includes `SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering` and `WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment`.

## Action taken

1. Added one README log entry summarizing the provisional answer and the evidence gap.
2. Added a more specific note under `## Open questions` in `projects/multi-agent-survey/README.md`.

## What is still needed

External research is required to answer the question well. Specifically:
1. 2024-2026 papers with direct multi-agent vs single-agent + tools comparisons on the same benchmark/task.
2. Ablation studies that collapse a multi-agent design into one agent with equivalent tools, memory, and token budget.
3. Evaluation papers defining when coordination overhead improves quality, robustness, or wall-clock time enough to justify extra agents.
