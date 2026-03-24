# Session Log — Single-Agent + Tools vs Multi-Agent Boundary Synthesis

- Timestamp: 2026-03-23T17:05:00Z
- Project: `projects/multi-agent-survey`
- Task: investigate open question in project README
- Classification: ROUTINE
- Status: completed within repo scope; stronger answer blocked on external research

## Summary

Reviewed current project artifacts for evidence about the performance boundary between multi-agent systems and single-agent + tools. There is still no direct in-repo benchmark study that equalizes tools, memory, and token budget across both settings, but the available literature supports a useful provisional rule: **default to single-agent + tools unless coordination, communication, robustness, or topology design is itself the hard part of the task**.

## Findings

1. The current repository still contains no dedicated benchmark synthesis directly comparing multi-agent against single-agent + tools under matched budgets.
   - Provenance: `search_text` over `projects/multi-agent-survey` for `single-agent`, `single agent`, `single-agent + tools`, `shared memory`, `message passing`, `tool use`, `coordination overhead`, and related terms returned no direct comparison note.

2. The NeurIPS artifact contains strong single-agent/tool-centric baselines that justify a single-agent-first prior.
   - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md` includes `SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering` and `WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment`.

3. The same NeurIPS artifact also contains papers where the problem formulation is inherently multi-agent because communication or zero-shot coordination is the main difficulty.
   - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md` includes `Multi-Agent Coordination via Multi-Level Communication`, `ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination`, and `N-agent Ad Hoc Teamwork`.

4. ICML 2025 adds evidence that multi-agent systems become more valuable when robustness, failure attribution, and shared-memory collaboration matter.
   - Provenance: `projects/multi-agent-survey/literature/icml-2024-2025.md` includes `On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents`, `Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems`, and `Agent Reviewers: Domain-specific Multimodal Agents with Shared Memory for Paper Review`.

5. Recent arXiv evidence suggests multi-agent scaling is not monotonic, which argues against using multi-agent systems by default.
   - Provenance: `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md` entry `Dual Latent Memory for Visual Multi-agent System` states in its abstract snippet that increasing agent turns can produce a `scaling wall` and degrade performance.

6. Recent arXiv evidence also suggests that communication topology itself is becoming a first-class optimization target, which is a concrete reason to prefer multi-agent designs only when routing structure matters.
   - Provenance: `projects/multi-agent-survey/literature/2026-03-23-goagent-communication-topology.md` and the corresponding entry in `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md` for `GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems`.

## Answer recorded in README

The README log now records this provisional answer:
- Use **single-agent + tools first** for tasks that are mostly serial planning + tool invocation around one coherent objective with stable interfaces.
- Use **multi-agent** when success depends on explicit role specialization, distributed viewpoints, inter-agent communication, zero-shot coordination, robustness to faulty participants, failure attribution, or learnable communication topology/shared-memory structure.

## What is still needed

External research is still required for a stronger empirical claim. Specifically:
1. 2024-2026 papers with direct head-to-head comparisons between multi-agent and single-agent + tools on the same tasks.
2. Ablations that collapse multi-agent systems into one agent while holding tools, memory, and token budget fixed.
3. Evaluation papers quantifying when coordination overhead is outweighed by gains in quality, robustness, or latency.
