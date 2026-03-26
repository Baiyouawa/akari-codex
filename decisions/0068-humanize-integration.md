# ADR 0068: Humanize (RLCR / Codex Review) 集成

## Status

Accepted

## Date

2026-03-26

## Context

本仓库由 LLM Agent 自主运行，拥有完善的治理框架（governance.py, ADR, SOP）、
Fleet 多 Agent 调度系统、以及 QQ 消息集成。但缺乏系统化的 **代码级质量审查闭环**：
当 Agent 修改 `agent_loop.py`、`onebot_client.py` 等核心模块时，没有独立 reviewer
拦截低质量变更。

Humanize (v1.14.0) 提供了 RLCR (Ralph-Loop with Codex Review) 工作流——让一个 AI
实现代码，另一个 AI (Codex) 独立审查，形成持续反馈循环直到所有验收标准通过。

## Decision

将 Humanize 三层递进式集成到 OpenAkari-Codex 框架：

### Layer 0: 环境准备
- `.gitignore` 加入 `.humanize/`
- 创建 `runner/humanize_bridge.py` 作为 Python 桥接层
- 创建 `jobs/code-audit.json` 审计作业定义

### Layer 1: 日常开发融入
- `SkillRegistry` 注册 Humanize 系统 Skill（`humanize_review`, `humanize_rlcr_setup`, `humanize_status`）
- `AgentLoop._sys_humanize()` 实现执行逻辑
- 创建 `docs/sops/humanize-workflow.md` 标准操作流程

### Layer 2: 全自动化闭环
- `fleet/executor.py` 在代码任务完成后自动触发 Codex 审查
- `governance.py` 的 `ProvenanceRecord` 增加 `humanize_reviews` 字段
- `ProvenanceTracker` 增加 `log_humanize_review()` 方法

## Key Design Decisions

1. **渐进式失败**：所有 Humanize 调用都用 try/except 包裹，不可用时静默跳过，不影响现有功能。
2. **Fleet 审查仅标记不阻断**：post-task review 发现 P0/P1 问题时标记 blocked，但不回滚代码。
3. **桥接层隔离**：`humanize_bridge.py` 封装所有 shell 脚本调用，上层代码不直接调 shell。
4. **与 AGENTS.md 对齐**：RLCR Round 0 对应 Orient + Plan，后续 Round 对应 Execute + Review。

## Consequences

- Agent 代码变更有了独立审查闭环
- Fleet worker 产出的代码自动经过质量检查
- Provenance 记录中可追溯审查历史
- 新增依赖：`codex` CLI 需要在运行环境中可用
- 运行时成本增加：每次 Fleet 代码任务额外 ~600s Codex 调用

## Files Changed

- `.gitignore` — 加入 `.humanize/`
- `runner/humanize_bridge.py` — 新建，Python 桥接层
- `runner/skill_registry.py` — 注册 Humanize Skill
- `runner/agent_loop.py` — 添加 `_sys_humanize()` 方法
- `runner/governance.py` — ProvenanceRecord 增加审查字段
- `fleet/executor.py` — post-task Codex 审查
- `jobs/code-audit.json` — 新建，周期审计作业
- `docs/sops/humanize-workflow.md` — 新建，SOP
- `docs/humanize-deep-analysis.md` — 新建，分析报告
- `docs/humanize-integration-plan.md` — 新建，集成方案
