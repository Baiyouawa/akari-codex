# MoE inference-specific systems evidence — 2026-03-24

- Date: 2026-03-24T13:42:29Z
- Status: new external evidence captured during horizon scan

## Why this note exists

This note captures external evidence relevant to the open project question of whether MoE **training** and **inference/serving** should be modeled separately. The current repo already had a general systems note, but it did not yet contain direct literature evidence that serving-time bottlenecks differ materially from training-time concerns.

## What is new relative to current repo state

Two external sources add stronger support for splitting training and inference analysis:

1. **Toward Efficient Inference for Mixture of Experts** (NeurIPS 2024) explicitly frames deployment difficulty around **large model size** and **complex communication pattern** during inference, then proposes three serving-oriented optimizations: **dynamic gating**, **expert buffering**, and **expert load balancing**.
   - Source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/98bf3b8505c611ac21055dd9d355c66e-Abstract-Conference.html
   - Retrieval date: 2026-03-24
2. **MegaScale-Infer: Serving Mixture-of-Experts at Scale with Disaggregated Expert Parallelism** (arXiv 2025) states that MoE sparsity can make FFNs **memory-intensive during inference**, causing **lower GPU utilization** and higher serving cost; it proposes **disaggregated attention/FFN deployment**, **ping-pong pipeline parallelism**, and an M2N communication library to reduce token-dispatch and synchronization overhead.
   - Source: https://arxiv.org/abs/2504.02263
   - Retrieval date: 2026-03-24

## Evidence details

### Source 1: Toward Efficient Inference for Mixture of Experts (NeurIPS 2024)

From the fetched abstract:

- MoE models are difficult to deploy for inference because of **their large model size and complex communication pattern**.
- The paper characterizes two inference workloads: **language modeling (LM)** and **machine translation (MT)**.
- It proposes three inference-specific optimizations:
  1. **Dynamic gating**
  2. **Expert Buffering**
  3. **Expert load balancing**
- Reported abstract-level gains include:
  - dynamic gating improves maximum throughput by **6.21–11.55×** for LM,
  - **5.75–10.98×** for MT Encoder,
  - **2.58–5.71×** for MT Decoder,
  - reduces memory usage by up to **1.36×** for LM and **1.1×** for MT,
  - Expert Buffering reduces static memory allocation by **1.47×**.
- Provenance: direct text from the NeurIPS proceedings abstract page fetched in this session.

### Source 2: MegaScale-Infer (arXiv 2025)

From the fetched abstract:

- During inference, MoE sparsity shifts FFNs from **compute-intensive** to **memory-intensive**.
- The abstract ties this shift to **substantially lower GPU utilization** and **increased operational costs**.
- The proposed system response is serving-specific rather than training-specific:
  1. **disaggregated attention and FFN modules**,
  2. **independent scaling and tailored parallelism** for those modules,
  3. **ping-pong pipeline parallelism** for micro-batches,
  4. a communication library to reduce **GPU-to-CPU copies**, **group initialization overhead**, and **GPU synchronization**.
- The abstract reports up to **1.90×** higher per-GPU throughput than state-of-the-art solutions.
- Provenance: direct text from the arXiv abstract page fetched in this session.

## Implication for `projects/moe`

This is the strongest direct evidence currently in-repo that **serving/inference should be analyzed separately from training** rather than treated as only a subcase of the generic systems note.

Specifically, the new sources add serving-dominant bottleneck classes not yet explicit in the project literature set:

1. **memory-intensiveness of sparse FFNs during inference**;
2. **serving-specific expert residency / buffering decisions**;
3. **latency/throughput-oriented communication hiding and module disaggregation**.

These are materially different from the repo’s current training-oriented baseline emphasis on dispatch, expert parallelism, and capacity-factor tuning.

## Gap that remains

This note strengthens the case for a train-vs-infer split, but it does **not** yet answer whether one unified bridge metric should compare both regimes. The new sources mainly report serving-oriented throughput, memory, and utilization gains; a later pass would still need a metric-mapping note if the project wants one table spanning both training and inference.

## Session provenance

- Existing repo baseline checked against:
  - `projects/moe/analysis/2026-03-24-systems-bottlenecks-and-efficiency-tradeoffs.md`
  - `projects/moe/literature/2026-03-24-moe-source-map.md`
- External retrieval method:
  - `web_search` for recent MoE inference bottleneck / serving literature
  - `web_fetch` on the NeurIPS proceedings abstract page and arXiv abstract page
