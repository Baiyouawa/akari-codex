# Humanize 集成方案 — OpenAkari-Codex 最大化利用指南

> 生成日期：2026-03-26
> 前置文档：[docs/humanize-deep-analysis.md](humanize-deep-analysis.md)

---

## 一、项目现状诊断

### 1.1 当前架构

```
openakari-codex/
├── runner/          # Agent 循环引擎（AgentLoop + SessionRunner + 调度）
├── fleet/           # 多 Agent 并行调度（FleetScheduler + claims）
├── integrations/    # QQ/OneBot 消息集成
├── projects/        # 研究项目工作区（akari, moe, multi-agent-*）
├── skills/          # 技能注册表
├── decisions/       # 68 条 ADR
├── tasks/           # 全局任务列表
├── prompts/         # 系统提示词
├── jobs/            # 调度作业定义
├── docs/            # 设计文档与 SOP
└── .fleet/          # Fleet 运行时状态
```

### 1.2 当前的代码审查机制

| 机制 | 状态 | 覆盖范围 |
|------|------|---------|
| `skills/review/` | 存在，人工触发 | 指标/发现记录 |
| `skills/critique/` | 存在 | 单次批判 |
| `skills/self-audit/` | 存在，周期运行 | 合规性检查 |
| `runner/governance.py` | 运行时 | 操作溯源 |
| `.fleet/` cross-review | 已用于论文 | 研究内容复核 |
| **Codex 独立代码审查** | **未启用** | **无** |

**关键缺口**：项目有完善的治理框架和溯源机制，但**没有系统化的代码级质量审查闭环**。当 `agent_loop.py`、`onebot_client.py` 等核心模块修改时，没有独立 reviewer 拦截低质量变更。

### 1.3 已发现的代码质量问题

调研中发现的典型问题（正是 Humanize 能解决的）：

1. `qq_bot.py` 导入不存在的 `QQBotConfig`，无法运行
2. `onebot_client.py` 的 `get_image` 共享 WS 轮询可能丢包
3. `agent_loop.py` 大量访问私有属性，耦合紧密
4. `.fleet/claims.json` 无归档机制，长期膨胀
5. `gateway.py` 每次请求新建 `ChatBot`，无缓存
6. `_call_llm` 失败返回错误字符串被当作 reply 发给用户

---

## 二、集成方案总览

### 分三层递进式引入 Humanize

```
Layer 0: 环境准备与即时收益    ← 立即可做，零风险
Layer 1: 日常开发融入 RLCR    ← 改变开发流程，显著提升质量
Layer 2: 全自动化闭环          ← 与 Fleet 和 CI 集成
```

---

## 三、Layer 0 — 环境准备与即时收益（30分钟内完成）

### 3.0.1 将 .humanize/ 加入 .gitignore

`.humanize/` 目录包含循环运行时状态，不应入库：

```bash
echo '.humanize/' >> .gitignore
```

### 3.0.2 用 Ask-Codex 做现有代码的即时审计

不需要任何计划文件，直接审查现有代码：

```bash
# 审查 onebot_client.py 的 WebSocket 并发安全性
"/home/devcontainers/.cursor/skills/humanize/scripts/ask-codex.sh" \
  "Review integrations/onebot_client.py focusing on: 1) WebSocket message routing safety in get_image(), 2) Race conditions in _poll_blocked_notifications, 3) Media tag parsing edge cases in _process_media_tags_and_send"

# 审查 agent_loop.py 的架构耦合问题
"/home/devcontainers/.cursor/skills/humanize/scripts/ask-codex.sh" \
  "Review runner/agent_loop.py for: 1) Tight coupling via private attribute access, 2) Error handling in _call_llm that silently converts failures to replies, 3) Potential race conditions in fleet integration methods"

# 审查 qq_bot.py 的导入问题
"/home/devcontainers/.cursor/skills/humanize/scripts/ask-codex.sh" \
  --codex-model gpt-5.4:medium \
  "Check integrations/qq_bot.py: it imports QQBotConfig from config_qq but that class doesn't exist. Diagnose the issue and propose a fix."
```

### 3.0.3 用 --skip-impl 对存量代码做全面 Code Review

```bash
# 在新分支上运行
git checkout -b humanize/code-review-baseline

"/home/devcontainers/.cursor/skills/humanize/scripts/setup-rlcr-loop.sh" \
  --skip-impl \
  --max 5 \
  --codex-model gpt-5.4:high
```

这会让 Codex 对 main 分支到当前所有差异做 diff 级审查，输出 `[P0]`~`[P9]` 标记的问题清单。

---

## 四、Layer 1 — 日常开发融入 RLCR

### 4.1 场景匹配表

| 开发场景 | 推荐 Humanize 工作流 | 参数建议 |
|---------|---------------------|---------|
| 修复 `onebot_client.py` 的 WS 并发问题 | RLCR + plan | `--max 10 --codex-model gpt-5.4:xhigh` |
| 重构 `agent_loop.py` 解耦 | RLCR + plan + agent-teams | `--agent-teams --max 15` |
| 修复 `qq_bot.py` 导入问题 | Ask-Codex 一次性 | `--codex-model gpt-5.4:medium` |
| 新增 Fleet 功能 | Gen-Plan → RLCR | 标准流程 |
| 研究项目代码（如文献处理脚本） | Ask-Codex | 快速咨询 |
| 提交到远程的 PR | PR Loop | `--claude --codex` |

### 4.2 示例：用 RLCR 修复 onebot_client.py

#### Step 1: 写草稿

创建 `plans/fix-onebot-ws-safety-draft.md`：

```markdown
# 修复 onebot_client.py 的 WebSocket 并发安全问题

## 问题
1. get_image() 在共享 ws.recv() 上轮询匹配 echo，并发事件可能丢包
2. _poll_blocked_notifications 和主消息循环存在竞态
3. _process_media_tags_and_send 中表情分支逻辑不清晰

## 期望
- 引入请求-响应路由机制，避免共享 recv 冲突
- 用 asyncio.Queue 或类似机制隔离消息派发
- 清理 media tag 解析边界条件
```

#### Step 2: 生成结构化计划

```bash
"/home/devcontainers/.cursor/skills/humanize/scripts/validate-gen-plan-io.sh" \
  --input plans/fix-onebot-ws-safety-draft.md \
  --output plans/fix-onebot-ws-safety-plan.md
```

然后在 Cursor 中使用 `humanize-gen-plan` 技能生成完整计划。

#### Step 3: 启动 RLCR 循环

```bash
git checkout -b fix/onebot-ws-safety

"/home/devcontainers/.cursor/skills/humanize/scripts/setup-rlcr-loop.sh" \
  plans/fix-onebot-ws-safety-plan.md \
  --max 10 \
  --codex-timeout 3600 \
  --base-branch main
```

#### Step 4: 监控进度（另一个终端）

```bash
source "/home/devcontainers/.cursor/skills/humanize/scripts/humanize.sh"
humanize monitor rlcr
```

### 4.3 示例：用 Agent Teams 重构 agent_loop.py

大型重构涉及多个文件（runner/ 下 16 个模块），适合并行化：

```bash
git checkout -b refactor/agent-loop-decoupling

export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

"/home/devcontainers/.cursor/skills/humanize/scripts/setup-rlcr-loop.sh" \
  plans/refactor-agent-loop-plan.md \
  --agent-teams \
  --max 20 \
  --full-review-round 4
```

Claude 作为 Team Leader 会：
- 将重构拆分为独立任务（如：提取接口、解耦 fleet 集成、统一错误处理）
- 分配给不同 agent，每个 agent 负责明确的文件集
- 协调避免文件冲突
- Codex 在每轮审查整体一致性

### 4.4 研究项目中的使用

对 `projects/multi-agent-review-survey/` 类研究项目，Humanize 的价值主要在辅助脚本的质量：

```bash
# 审查文献检索脚本的质量
"/home/devcontainers/.cursor/skills/humanize/scripts/ask-codex.sh" \
  "Review projects/multi-agent-review-survey/sources/gather_arxiv_multi_agent_survey_candidates.py for correctness, error handling, and edge cases"
```

---

## 五、Layer 2 — 与 Fleet 和 CI 集成

### 5.1 Fleet 任务中嵌入 Humanize 审查

在 Fleet 执行完代码修改任务后，自动触发 Codex 审查。在 `fleet/executor.py` 中增加 post-task hook：

```python
# 概念设计：Fleet worker 完成代码任务后自动触发 Codex 审查
def post_task_review(project_root, base_branch):
    """在 Fleet worker 完成代码变更后，用 ask-codex 做快速审查"""
    import subprocess
    result = subprocess.run(
        [HUMANIZE_SCRIPTS + "/ask-codex.sh",
         "--codex-model", "gpt-5.4:medium",
         "--codex-timeout", "600",
         f"Review the git diff from {base_branch} to HEAD in this repo. "
         f"Flag any [P0] critical issues."],
        capture_output=True, text=True
    )
    return result.stdout
```

### 5.2 PR Loop 与 GitHub 集成

当代码通过 RLCR 审查后，推送到 GitHub 并启动 PR Loop：

```bash
git push -u origin fix/onebot-ws-safety
gh pr create --title "Fix OneBot WS concurrency" --body "..."

# 启动 PR Loop，让 claude[bot] 和 codex[bot] 自动审查
"/home/devcontainers/.cursor/skills/humanize/scripts/setup-pr-loop.sh" \
  --claude --codex \
  --max 10
```

### 5.3 调度作业中嵌入定期代码审计

在 `jobs/` 中增加定期代码审计作业：

```json
{
  "name": "weekly-code-audit",
  "schedule": "weekly",
  "task": "Run skip-impl RLCR on all modified files since last audit",
  "humanize_config": {
    "mode": "skip-impl",
    "max": 3,
    "codex_model": "gpt-5.4:high"
  }
}
```

---

## 六、推荐的标准操作流程（SOP）

### 6.1 新功能开发 SOP

```
1. 写草稿 draft.md
2. gen-plan → plan.md（生成结构化计划）
3. git checkout -b feature/xxx
4. setup-rlcr-loop plan.md（启动 RLCR）
5. 开发 → 提交 → 写摘要 → Codex 审查 → 修复 → 循环...
6. Code Review 通过 → Finalize
7. git push → gh pr create
8. setup-pr-loop --claude --codex（可选）
9. 合并
```

### 6.2 Bug 修复 SOP

```
1. ask-codex "诊断 <文件> 中的 <问题>"（快速定位）
2. git checkout -b fix/xxx
3. 写简短 plan.md（或直接 --skip-impl）
4. setup-rlcr-loop --max 5
5. 修复 → Codex 审查 → 完成
```

### 6.3 代码审计 SOP

```
1. git checkout -b audit/xxx
2. setup-rlcr-loop --skip-impl --max 3
3. 收集 [P0-P9] 问题清单
4. 按优先级逐个修复
5. 将审计发现记录到 decisions/ 或项目 README
```

---

## 七、优先行动清单

### 立即执行（今天）

| # | 行动 | 命令 | 预期收益 |
|---|------|------|---------|
| 1 | `.gitignore` 加入 `.humanize/` | `echo '.humanize/' >> .gitignore` | 防止运行时状态入库 |
| 2 | Ask-Codex 审查 `onebot_client.py` | 见 §3.0.2 | 发现 WS 并发问题的具体修复方案 |
| 3 | Ask-Codex 诊断 `qq_bot.py` 导入问题 | 见 §3.0.2 | 快速修复已知 bug |
| 4 | --skip-impl 全面审查存量代码 | 见 §3.0.3 | 获得完整的代码问题清单 |

### 本周执行

| # | 行动 | 预期收益 |
|---|------|---------|
| 5 | 为 `onebot_client.py` WS 修复写 plan → RLCR | 系统化修复核心集成层 |
| 6 | 为 `agent_loop.py` 重构写 plan → RLCR + Agent Teams | 解耦核心引擎 |
| 7 | 写一条 ADR 记录 Humanize 集成决策 | 持久化决策，后续 agent 可循此操作 |

### 持续执行

| # | 行动 | 频率 |
|---|------|------|
| 8 | 所有代码变更走 RLCR | 每次提交 |
| 9 | 定期 --skip-impl 审计 | 每周 |
| 10 | PR Loop 管理远程 review | 每个 PR |

---

## 八、模型参数速查表

| 场景 | `--codex-model` | `--max` | `--codex-timeout` |
|------|-----------------|---------|-------------------|
| 快速咨询 | `gpt-5.4:medium` | N/A | 600 |
| 日常 RLCR | `gpt-5.4:xhigh` | 10 | 3600 |
| 大型重构 | `gpt-5.4:xhigh` | 20 | 5400 |
| 存量审计 | `gpt-5.4:high` | 5 | 3600 |
| PR Review | `gpt-5.4:medium` | 10 | 900 |

---

## 九、与现有 AGENTS.md 工作流的对齐

Humanize 与 AGENTS.md 定义的自主执行流程完全兼容：

| AGENTS.md 原则 | Humanize 对齐方式 |
|---------------|------------------|
| Orient → Select → Execute → Commit | RLCR Round 0 = Orient + Plan; 后续 Round = Execute + Review |
| 发现立即写入文件 | Goal Tracker 强制每轮记录进展 |
| 决策写 ADR | Codex 审查发现可触发新 ADR |
| 会话结束必须提交 | RLCR gate 强制 git clean 才能退出 |
| 不重复争论已记 ADR | Goal Tracker 不可变部分 Round 0 后锁定 |
| 知识产出优先 | 每轮审查摘要 + review-result 自动积累知识 |
| 审批门控 | RLCR 不触碰生产 PR；需人工审批的写 APPROVAL_QUEUE |
