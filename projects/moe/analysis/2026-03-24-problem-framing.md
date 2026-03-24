# MoE Problem Framing — 2026-03-24

## Purpose

将“继续推进 MoE 任务”拆解为可持续执行的零资源研究问题，避免后续 session 继续在空泛任务描述上重复 orient。

## Baseline observations

1. `projects/moe` 已具备项目工作空间，但当前任务列表只有 1 个计划任务和 1 个泛化推进任务。
   - Provenance: `projects/moe/TASKS.md` read in this session.
2. 当前 README 的 open questions 仍是高层方向选择题，尚未落到可直接产出 artifact 的研究问题。
   - Provenance: `projects/moe/README.md` read in this session.
3. 当前仓库中除 `projects/moe/` 外没有既有 MoE 内容可复用，因此首轮推进应优先建设问题框架与来源地图。
   - Provenance: `search_text("MoE|moe", path=".", max_results=100)` returned no matches before this session's MoE updates.

## Priority research questions

### P0

1. **MoE 在 LLM / Transformer 中解决的核心瓶颈是什么？**
   - Target artifact: architecture overview note
2. **主流 routing 机制如何在质量、负载均衡、稳定性之间权衡？**
   - Target artifact: routing analysis
3. **MoE 的系统瓶颈主要出现在哪些环节：dispatch、all-to-all、memory、expert imbalance？**
   - Target artifact: systems analysis

### P1

4. **开源 MoE 实现最常见的配置旋钮有哪些，分别影响什么？**
   - Target artifact: implementation/source map
5. **训练阶段与推理阶段的 MoE 关注点有何不同？**
   - Target artifact: comparison note

### P2

6. **MoE 的典型失败模式有哪些，已有工作如何缓解？**
7. **Dense 模型、MoE 模型、其他稀疏化方法之间该如何比较？**

## Immediate implication

下一步最高价值零资源动作不是继续抽象讨论“做 MoE”，而是先建立一份可验证 source map，用于支撑上述问题的后续分析。
