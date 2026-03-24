# MoE Source Map — 2026-03-24

- Date: 2026-03-24T03:56:30Z
- Status: first-pass populated

## Purpose

作为 MoE 项目的来源入口索引，后续 session 在补充文献、博客、实现或 benchmark 时，统一登记到此文件并补充 provenance。

## Usage rule

新增来源时需至少记录：
1. title / repo name
2. source URL or in-repo path
3. why it matters to one of the project research questions
4. retrieval date

## Source map

| Category | Title | Source | Why it matters / intended use | Retrieval date |
|---|---|---|---|---|
| Paper | Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer | https://arxiv.org/abs/1701.06538 | 作为现代深度学习 MoE 的经典起点，用于回溯 expert sparsity、conditional computation 与早期 load-balancing 设计。支撑 `projects/moe/analysis/` 后续的基础概念说明。 | 2026-03-24 |
| Paper | GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding | https://arxiv.org/abs/2006.16668 | 用于连接“MoE 层设计”与“大规模 Transformer 分片训练”两个主题，特别适合后续整理 expert parallelism、automatic sharding 与系统扩展路径。 | 2026-03-24 |
| Paper | Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | https://arxiv.org/abs/2101.03961 | 用于分析 top-1 routing、训练稳定性与简化路由策略的工程收益，是 routing / load balancing 分析的核心来源之一。 | 2026-03-24 |
| Paper | BASE Layers: Simplifying Training of Large, Sparse Models | https://arxiv.org/abs/2103.16716 | 提供另一条路由与负载分配思路，可用于与 Switch / GShard 对比“均衡约束如何影响训练与实现复杂度”。 | 2026-03-24 |
| Paper | ST-MoE: Designing Stable and Transferable Sparse Expert Models | https://arxiv.org/abs/2202.08906 | 面向“训练稳定性”和“迁移可用性”问题，适合作为后续整理 MoE 失败模式与稳定化手段的来源入口。 | 2026-03-24 |
| Paper | Mixtral of Experts | https://arxiv.org/abs/2401.04088 | 提供近期开源权重背景下的高关注度 Transformer MoE 参考点，可用于连接学术设计与实际开源模型配置（如 experts-per-token / active parameters）分析。 | 2026-03-24 |
| Open-source implementation | DeepSpeed MoE | https://github.com/microsoft/DeepSpeed | 作为训练框架集成实现入口，用于抽取 capacity factor、auxiliary loss、expert parallelism、token dispatch 等工程配置旋钮；也可作为后续代码级 provenance 的上游入口。 | 2026-03-24 |
| Open-source implementation | Megatron-LM | https://github.com/NVIDIA/Megatron-LM | 作为大规模训练实现参考，适合后续查看 MoE 与 tensor / pipeline / expert parallelism 的组合方式，支撑 systems 分析。 | 2026-03-24 |
| Open-source implementation | Fairseq examples / MoE | https://github.com/facebookresearch/fairseq | 适合作为较早期、研究导向的 Transformer MoE 实现参考，用于比对训练脚本、router loss 设置和实验配置表达方式。 | 2026-03-24 |
| Engineering reference | Hugging Face Transformers — SwitchTransformers documentation | https://huggingface.co/docs/transformers/model_doc/switch_transformers | 提供面向使用者的模型接口与配置说明，适合在后续任务中快速定位实现层参数名、配置字段与推理侧调用约束。 | 2026-03-24 |

## Coverage note

本首版来源地图已覆盖至少三类来源：
1. 论文（foundational / routing / stability / recent open model）
2. 开源实现（训练框架与研究实现入口）
3. 工程参考（面向配置与使用的文档入口）

## Suggested next uses

1. 从 `Switch Transformers`、`BASE Layers`、`ST-MoE` 中抽取 routing / balancing / stability 的对比表。
2. 从 `DeepSpeed MoE`、`Megatron-LM`、`Fairseq` 中抽取共有配置旋钮，形成实现配置地图。
3. 将 `GShard` 与 `Megatron-LM` 组合用于系统并行与通信路径分析。
