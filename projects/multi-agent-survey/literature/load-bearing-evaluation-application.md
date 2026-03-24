# Load-bearing papers for Phase 2 — Evaluation & Application

Timestamp: 2026-03-23T17:10:00Z

Purpose: make the repository-level `load-bearing` set explicit for the Phase 2 task `精读 Phase 1 中标记为 load-bearing 的论文（Evaluation & Application 类）`.

Selection rule used in this session:
- Start from Phase 1 artifacts already present in `projects/multi-agent-survey/literature/`.
- Prefer papers tagged `Evaluation`, `Benchmark`, or `Application` in those artifacts.
- Prioritize papers that are likely to carry survey conclusions about practical value, benchmark design, or real-world deployment.
- Keep the set small enough to support close reading in this phase.

## Selected load-bearing papers

1. **Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale**
   - Bucket: Evaluation
   - Why load-bearing: explicit large-scale benchmark for realistic computer-use agents; directly informs the project open question on multi-agent evaluation benchmarks.
   - Provenance: `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 13.

2. **What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities**
   - Bucket: Evaluation
   - Why load-bearing: benchmark paper centered on multidimensional capability measurement and controllable task complexity.
   - Provenance: `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 14.

3. **Ad-Hoc Human-AI Coordination Challenge**
   - Bucket: Evaluation
   - Why load-bearing: benchmark/evaluation work on human-AI coordination rather than agent-only task success; relevant to practical deployment settings.
   - Provenance: `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 22.

4. **Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast**
   - Bucket: Evaluation / Safety application stress test
   - Why load-bearing: evaluates a concrete failure mode that becomes specific to multi-agent settings at scale.
   - Provenance: `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 3.

5. **ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination**
   - Bucket: Evaluation
   - Why load-bearing: coordination benchmark from NeurIPS 2024 candidate pool; useful anchor for comparing MARL-style evaluation against LLM-agent benchmarks.
   - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md`, entry 19.

6. **MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making**
   - Bucket: Application
   - Why load-bearing: domain application in a high-stakes setting; representative of where multi-agent claims must cash out as practical value.
   - Provenance: `projects/multi-agent-survey/literature/neurips-2024-2025.md`, entry 9.

7. **AI Agents Can Already Autonomously Perform Experimental High Energy Physics**
   - Bucket: Application
   - Why load-bearing: recent arXiv application paper claiming substantial autonomous scientific-work capability; important for the survey's forward-looking application section.
   - Provenance: `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`, 2026-03 entry 1.

8. **DIG to Heal: Scaling General-purpose Agent Collaboration via Explainable Dynamic Decision Paths**
   - Bucket: Evaluation / Application-enabling systems
   - Why load-bearing: explicitly studies scaling and explainability for general-purpose agent collaboration, which affects real-world usability.
   - Provenance: `projects/multi-agent-survey/literature/arxiv-2026-01-to-2026-03.md`, 2026-02 entry 3.

## Coverage note

This session marks 8 papers as the repository's current load-bearing set for the Evaluation & Application bucket.
- Inline arithmetic: 5 evaluation-heavy papers + 3 application-oriented papers = 8 total.

## Scope boundary

This file only defines the load-bearing set for the Evaluation & Application task. It does not claim to settle the load-bearing set for Architecture or Coordination & Communication.