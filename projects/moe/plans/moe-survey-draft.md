# MoE 结构化综述初稿

- Timestamp: 2026-03-24T04:08:21Z
- Project: `projects/moe`
- Status: draft
- Scope: 用当前仓库内已沉淀的 literature / analysis artifacts 组装首版结构化综述；其中 architecture 与 routing 已有较强来源支撑，systems 主题先按当前来源地图与任务定义形成首版比较框架。

## Artifact map

### Literature artifacts

1. `projects/moe/literature/2026-03-24-moe-source-map.md`
   - Current source inventory for papers, implementations, and engineering references.
2. Source families currently registered there:
   - Foundational / architecture: `Sparsely-Gated MoE`, `GShard`, `Mixtral of Experts`
   - Routing / balancing / stability: `Switch Transformers`, `BASE Layers`, `ST-MoE`
   - Systems / implementation: `GShard`, `DeepSpeed MoE`, `Megatron-LM`, `fairseq`, Hugging Face `SwitchTransformers` docs

### Analysis artifacts

1. `projects/moe/analysis/2026-03-24-problem-framing.md`
   - Defines the project’s priority questions and treats architecture, routing, and systems as P0 themes.
2. `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`
   - Provides the current source-backed comparison of routing families and balancing/stability tradeoffs.
3. `projects/moe/analysis/2026-03-24-workspace-audit.md`
   - Records the early workspace baseline and why structured research artifacts are required.

## Executive summary

This repository’s current MoE evidence base supports a three-part survey structure:

1. **Architecture:** MoE’s defining move is to replace a dense FFN path with sparse conditional expert activation, making “active parameters” and expert selection first-class design variables.
   - Provenance: `projects/moe/plans/2026-03-24-initial-execution-plan.md` priority themes; `projects/moe/literature/2026-03-24-moe-source-map.md` entries for `Sparsely-Gated MoE`, `GShard`, and `Mixtral of Experts`.
2. **Routing:** The best-supported comparison axis today is the tradeoff among top-k token-choice routing, top-1 simplified routing, balancing-by-assignment, and stability-oriented refinements.
   - Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`.
3. **Systems:** Current repository evidence already identifies dispatch, all-to-all communication, and expert parallelism as the main systems bottleneck candidates, but these have not yet been expanded into a dedicated source-backed systems analysis note.
   - Provenance: `projects/moe/analysis/2026-03-24-problem-framing.md`; `projects/moe/TASKS.md`; `projects/moe/literature/2026-03-24-moe-source-map.md`.

## 1. Architecture

### 1.1 What makes MoE different from dense Transformer blocks

The project’s current framing treats MoE primarily as a Transformer/LLM design where not every token traverses the same feed-forward path; instead, a router chooses which expert subnetwork processes each token.
- Provenance: `projects/moe/analysis/2026-03-24-problem-framing.md` identifies expert, router, capacity, load balancing, and active parameters as core concepts; `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` explains that MoE layers differ from dense FFN blocks because tokens are dispatched to one or more experts.

A useful architectural consequence is that MoE must be described along at least three axes:
1. **Expert structure** — how many experts exist and where expert layers are inserted.
2. **Activation sparsity** — how many experts a token activates.
3. **Capacity control** — what happens when too many tokens want the same expert.
- Provenance: synthesized from the priority-theme list in `projects/moe/plans/2026-03-24-initial-execution-plan.md` and the routing control knobs named in `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`.

### 1.2 Architecture lineage in the current source map

The literature map already organizes a compact architecture lineage:

| Architecture role in this repo | Current anchor sources | Why they matter here |
|---|---|---|
| Foundational sparse-expert starting point | `Sparsely-Gated MoE` | Establishes expert sparsity and conditional computation as the modern baseline entry point. |
| Scaling architecture + distributed training bridge | `GShard` | Connects MoE layer design with large-scale sharding and system-scale execution. |
| Recent open-model reference point | `Mixtral of Experts` | Gives the project a practical modern checkpoint for open-model MoE configuration discussion. |

Provenance: row content and intended-use text in `projects/moe/literature/2026-03-24-moe-source-map.md`.

### 1.3 Working architecture synthesis

At the current draft stage, the repository supports the following architectural synthesis:

1. **MoE should be analyzed as a sparse-compute architectural pattern, not merely a larger parameter count.**
   - Provenance: `projects/moe/analysis/2026-03-24-problem-framing.md` prioritizes architecture, routing, and systems together rather than treating size alone as the main question.
2. **Architecture and routing are inseparable in practice.** A model cannot be described just by “number of experts”; experts-per-token and capacity handling change both model behavior and execution cost.
   - Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` identifies experts-per-token, capacity enforcement, and balancing as linked design choices.
3. **Architecture and systems are also inseparable.** `GShard` is explicitly included in the source map because it bridges MoE layer design to sharding and large-scale execution.
   - Provenance: `projects/moe/literature/2026-03-24-moe-source-map.md` entry for `GShard`.

### 1.4 Architecture gaps still open

The current repo still lacks a dedicated architecture note comparing, for example, expert placement, shared-vs-per-layer router structure, or recent open-model layout choices.
- Provenance: `projects/moe/plans/2026-03-24-initial-execution-plan.md` lists architecture as a priority theme, but `projects/moe/analysis/` currently contains problem framing, routing, and workspace audit only.

## 2. Routing

### 2.1 Current best-supported comparison frame

The routing analysis artifact already establishes four routing-design families / tradeoff frames:

1. **Top-k token-choice routing**
   - Representative sources: `Sparsely-Gated MoE`, `GShard`
2. **Top-1 token-choice routing**
   - Representative sources: `Switch Transformers`, Hugging Face `SwitchTransformers` docs
3. **Balanced-assignment routing**
   - Representative source: `BASE Layers`
4. **Stability-oriented routing refinement**
   - Representative source: `ST-MoE`

Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`.

### 2.2 Main routing tradeoffs

The routing artifact supports four cross-cutting tradeoff lenses that should anchor later comparisons:

| Tradeoff | Current synthesis | Provenance |
|---|---|---|
| Top-k expressivity vs top-1 simplicity | More active experts preserve mixture behavior; top-1 simplifies routing and lowers per-token overhead. | `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` |
| Auxiliary-loss balancing vs assignment-balanced routing | Some designs preserve router freedom and penalize imbalance later; others make balance part of assignment itself. | `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` |
| Utilization efficiency vs training stability | Balanced average load is not equivalent to stable optimization. | `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` |
| Routing quality vs systems overhead | Richer routing can increase token movement and distributed coordination cost. | `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` |

### 2.3 Routing implications for this project

Based on the current repository evidence, the routing section of the MoE project is already mature enough to support two practical decisions:

1. **`Switch Transformers`, `BASE Layers`, and `ST-MoE` are the strongest immediate trio for a first comparison table.**
   - Why: `projects/moe/TASKS.md` explicitly names them as the next sources for extracting routing, balancing loss, and stability intervention dimensions.
   - Provenance: `projects/moe/TASKS.md`; `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`.
2. **Future implementation notes should separate three router knobs: experts-per-token, capacity handling, and balancing/stability regularization.**
   - Provenance: implication section of `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`.

### 2.4 Current routing takeaway

For this repository, routing is not a narrow subtopic; it is the hinge connecting model quality, training stability, expert utilization, and eventual systems cost.
- Provenance: `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md` and P0 question list in `projects/moe/analysis/2026-03-24-problem-framing.md`.

## 3. Systems

### 3.1 Current evidence status

The systems theme is already present in project planning, but it is less mature than routing. The repo currently supports a **structured systems outline** rather than a finished systems conclusion.
- Provenance: `projects/moe/TASKS.md` still leaves `分析 MoE 系统瓶颈与效率权衡` open; `projects/moe/analysis/` contains no dedicated systems analysis file yet.

### 3.2 What the current repo already supports

Even before a dedicated systems note exists, three system-level bottleneck families are already named consistently across project artifacts:

1. **Dispatch / token movement**
2. **All-to-all communication**
3. **Expert parallelism and distributed execution strategy**

Provenance:
- `projects/moe/analysis/2026-03-24-problem-framing.md` lists dispatch, all-to-all, memory, and expert imbalance as the main systems bottleneck questions.
- `projects/moe/TASKS.md` instructs the systems task to extract dispatch, all-to-all, and expert parallelism items from `GShard`, `DeepSpeed MoE`, and `Megatron-LM`.
- `projects/moe/literature/2026-03-24-moe-source-map.md` includes those sources specifically for sharding, token dispatch, and expert parallelism analysis.

### 3.3 Systems source roles in the current source map

| Systems theme | Current source anchors | Why these sources are in scope |
|---|---|---|
| Distributed MoE scaling | `GShard` | Included to connect conditional computation to automatic sharding and large-scale Transformer execution. |
| Training-framework implementation knobs | `DeepSpeed MoE` | Included to extract capacity factor, auxiliary loss, expert parallelism, and token dispatch controls. |
| Large-scale parallel composition | `Megatron-LM` | Included to examine how MoE combines with tensor / pipeline / expert parallelism. |
| Research-oriented implementation reference | `fairseq` | Included for comparison of training scripts, router loss settings, and experiment configuration expression. |
| User-facing configuration surface | Hugging Face `SwitchTransformers` docs | Included to locate implementation-layer parameter names and serving-side usage constraints. |

Provenance: intended-use text in `projects/moe/literature/2026-03-24-moe-source-map.md`.

### 3.4 Provisional systems synthesis

The current repository justifies the following provisional systems synthesis:

1. **MoE systems analysis must not be collapsed into a generic “larger model” discussion.** The named bottlenecks are communication- and routing-specific.
   - Provenance: `projects/moe/analysis/2026-03-24-problem-framing.md`.
2. **Training and inference likely need separate comparison frames, but the repo does not yet have literature-backed proof strong enough to close that question.**
   - Provenance: progress note under the systems task in `projects/moe/TASKS.md`, which says repo-internal synthesis suggests this separation but that the claim is not yet literature-backed.
3. **The first systems baseline should come from code/documentation surfaces that expose configuration knobs clearly enough for extraction.**
   - Provenance: implementation-source descriptions in `projects/moe/literature/2026-03-24-moe-source-map.md` for `DeepSpeed MoE`, `Megatron-LM`, `fairseq`, and Hugging Face docs.

### 3.5 Systems gaps still open

This draft cannot yet answer, with source-backed confidence, which bottleneck dominates under which operating regime, because the dedicated systems-analysis task remains open.
- Provenance: absence of a systems analysis artifact under `projects/moe/analysis/` and open systems task in `projects/moe/TASKS.md`.

## 4. Cross-theme synthesis

Across the current repo, the most reusable synthesis is:

1. **Architecture defines the sparse-compute pattern.**
2. **Routing determines how that sparse capacity is actually exercised.**
3. **Systems determine whether the theoretical sparse-compute gain survives dispatch and communication overhead.**

Provenance: combined reading of `projects/moe/plans/2026-03-24-initial-execution-plan.md`, `projects/moe/analysis/2026-03-24-problem-framing.md`, `projects/moe/analysis/2026-03-24-routing-and-load-balancing.md`, and `projects/moe/TASKS.md`.

This yields a practical project rule: future MoE notes should avoid treating architecture, routing, or systems as isolated dimensions, because the existing evidence base already shows they interact directly.
- Provenance: same artifact set as above; especially the routing note’s statement that routing analysis cannot be fully separated from systems analysis.

## 5. Recommended next increments

1. **Add a dedicated systems analysis note** in `projects/moe/analysis/` using `GShard`, `DeepSpeed MoE`, and `Megatron-LM` as the first extraction set.
   - Provenance: `projects/moe/TASKS.md` Next step for the systems task.
2. **Add an architecture-focused comparison note** covering expert placement, active-parameter framing, and the role of modern open-model references such as `Mixtral of Experts`.
   - Provenance: architecture priority theme in `projects/moe/plans/2026-03-24-initial-execution-plan.md` plus currently missing dedicated architecture artifact.
3. **Turn the routing section into a compact matrix** with columns for experts-per-token, balancing method, stability intervention, and expected systems cost.
   - Provenance: routing note and source-map suggestions in `projects/moe/literature/2026-03-24-moe-source-map.md`.

## Open questions

1. In the first implementation-knob extraction pass, should `DeepSpeed MoE` be preferred over `Megatron-LM` and `fairseq` because its source-map rationale is the most configuration-oriented, or should the first baseline instead be whichever implementation exposes the clearest expert-parallel + dispatch path?
   - Provenance: open question 2 in `projects/moe/README.md`; source descriptions in `projects/moe/literature/2026-03-24-moe-source-map.md`.
2. Should the next survey revision wait for a dedicated systems artifact before introducing any stronger systems conclusions?
   - Provenance: current evidence-status gap described in this draft and the open systems task in `projects/moe/TASKS.md`.
3. What is the smallest architecture note that would let this survey move from “draft structure” to “first comparative review”? 
   - Provenance: absence of a dedicated architecture analysis artifact in `projects/moe/analysis/`.
