# Literature Note — Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast

- Timestamp: 2026-03-23T17:15:00Z
- Category: Evaluation / Safety
- Load-bearing provenance: `projects/multi-agent-survey/literature/load-bearing-evaluation-application.md`
- Source provenance:
  - Listing metadata from `projects/multi-agent-survey/literature/icml-2024-2025.md`, entry 3.
  - Abstract text verified from `https://proceedings.mlr.press/v235/gu24e.html` via in-session `python3 requests` retrieval.

## Citation

Xiangming Gu, Xiaosen Zheng, Tianyu Pang, Chao Du, Qian Liu, Ye Wang, Jing Jiang, Min Lin. **Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast**. ICML 2024. PMLR page: `https://proceedings.mlr.press/v235/gu24e.html`. DBLP: `https://dblp.org/rec/conf/icml/GuZPDLWJL24`.

## What this paper studies

The paper analyzes a safety failure that emerges specifically in multi-agent settings: after one multimodal agent is jailbroken, harmful behavior can propagate to many other agents through interaction, producing what the authors call an infectious jailbreak.

## Key contributions

1. Defines the notion of **infectious jailbreak** in multi-agent environments.
2. Demonstrates the failure mode in simulated environments with up to **one million** LLaVA-1.5 agents.
3. Uses randomized pair-wise chat as the proof-of-concept interaction mechanism.
4. Argues that a single adversarial image inserted into one agent's memory can trigger large-scale spread.
5. Provides a principle for reasoning about whether defenses can provably restrain propagation.

## Evidence from source

Abstract excerpt, verified from the PMLR page:
> "It entails the adversary simply jailbreaking a single agent, and without any further intervention from the adversary, (almost) all agents will become infected exponentially fast and exhibit harmful behaviors... we simulate multi-agent environments containing up to one million LLaVA-1.5 agents..."

## Why it matters for the survey

- It shows that evaluation of multi-agent systems must include contagion-like failure analysis, not just average task success.
- The paper is practically important because multi-agent deployment creates attack surfaces that single-agent evaluation can miss.
- It broadens the meaning of "application value": a multi-agent system that scales capabilities may also scale failures.

## Method / evaluation lens

This is best understood as a stress-test evaluation paper:
- attack one agent,
- allow normal inter-agent communication,
- measure spread of harmful behavior through the population.

That evaluation framing is valuable for the survey because it highlights system-level externalities in agent societies.

## Limits / caveats

1. The abstract confirms the core phenomenon, but the current repository state does not yet verify the exact communication assumptions or defense effectiveness tables.
2. The proof-of-concept uses randomized pair-wise chat; real systems may have different topologies and memory controls.
3. Simulated scale does not automatically imply equivalent real-world deployment scale.

## Relevance to open questions

- **什么时候值得用多智能体？** This paper is a reminder that using more agents can amplify risk as well as capability.
- **Agent-to-agent communication 的最新范式是什么？** Any communication paradigm should also be judged by how it propagates failures.

## One-sentence takeaway

Agent Smith is load-bearing because it identifies a distinctly multi-agent safety failure mode: harmful behavior can spread across agents exponentially after a single jailbreak.