# SOP: Humanize 代码审查工作流

## 目的

规范 Humanize (RLCR / Ask-Codex / PR-Loop) 在本仓库中的使用方式，确保代码变更经过独立 AI 审查。

## 适用场景

| 场景 | 推荐工作流 | 触发方式 |
|------|-----------|---------|
| 小修复（< 50 行） | Ask-Codex | 手动或 AgentLoop `humanize_review` skill |
| 新功能开发 | Gen-Plan → RLCR | 手动 |
| 大型重构（> 3 文件） | RLCR + Agent Teams | 手动 |
| Fleet 完成代码任务后 | 自动 Post-Task Review | Fleet executor 自动触发 |
| 周期性审计 | Skip-Impl RLCR | Scheduler 定期触发 |
| PR 合并前 | PR Loop | 手动 |

## 标准流程

### 1. 新功能开发

```bash
# 1. 写草稿
vim plans/my-feature-draft.md

# 2. 生成结构化计划
"/home/devcontainers/.cursor/skills/humanize/scripts/validate-gen-plan-io.sh" \
  --input plans/my-feature-draft.md \
  --output plans/my-feature-plan.md

# 3. 创建分支并启动 RLCR
git checkout -b feature/my-feature
"/home/devcontainers/.cursor/skills/humanize/scripts/setup-rlcr-loop.sh" \
  plans/my-feature-plan.md --max 10

# 4. 监控（另一终端）
source "/home/devcontainers/.cursor/skills/humanize/scripts/humanize.sh"
humanize monitor rlcr
```

### 2. Bug 修复

```bash
# 快速诊断
"/home/devcontainers/.cursor/skills/humanize/scripts/ask-codex.sh" \
  "诊断 <文件> 中的 <问题>"

# 或走简短 RLCR
git checkout -b fix/my-bug
"/home/devcontainers/.cursor/skills/humanize/scripts/setup-rlcr-loop.sh" \
  --skip-impl --max 5
```

### 3. Fleet 自动审查

Fleet executor 在代码任务完成后自动调用 `humanize_bridge.fleet_post_task_review()`。
如果发现 P0/P1 级别问题，会标记为 blocked 并通知主人。

### 4. AgentLoop 中使用

小白可通过系统 Skill 调用审查：

```json
{
  "action": "use_skill",
  "skill": "humanize_review",
  "args": {
    "target": "integrations/onebot_client.py",
    "focus": "WebSocket 并发安全"
  }
}
```

## Plan 文件规范

参考 `/home/devcontainers/.cursor/skills/humanize/prompt-template/plan/gen-plan-template.md`：

- 必须包含: Goal Description, Acceptance Criteria (AC-X), Path Boundaries
- AC 需包含正向和反向测试用例
- 不少于 5 行有效内容

## 模型参数速查

| 场景 | `--codex-model` | `--max` | `--codex-timeout` |
|------|-----------------|---------|-------------------|
| 快速咨询 | `gpt-5.4:medium` | N/A | 600 |
| 日常 RLCR | `gpt-5.4:xhigh` | 10 | 3600 |
| 大型重构 | `gpt-5.4:xhigh` | 20 | 5400 |
| Fleet 自动审查 | `gpt-5.4:medium` | N/A | 600 |
| 存量审计 | `gpt-5.4:high` | 5 | 3600 |

## 数据位置

- RLCR 运行时: `.humanize/rlcr/<timestamp>/`（已 gitignore）
- 审查结果归档: `artifacts/humanize-reviews/`
- Fleet 审查日志: `logs/sessions/` 中的 JSONL
