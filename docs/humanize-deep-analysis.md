# Humanize 深度分析报告

> 生成日期：2026-03-26
> 仓库地址：https://github.com/humania-org/humanize/tree/main
> 当前版本：1.14.0
> 本地安装路径：`/home/devcontainers/.cursor/skills/humanize/`

---

## 一、概述

Humanize 是一个 **Claude Code 插件 + Codex CLI 技能系统**，核心理念是：**让一个 AI 写代码，让另一个 AI 独立审查代码，形成持续的反馈循环，直到所有验收标准全部通过**。

名字 RLCR 一语双关：
- **R**alph-**L**oop with **C**odex **R**eview（官方含义）
- **R**einforcement **L**earning with **C**ode **R**eview（隐含含义——通过外部审查反馈迭代优化代码）

---

## 二、完整功能清单

### 2.1 RLCR Loop — 核心迭代开发循环

工作流程：

```
Plan.md → Claude 实现 → Claude 写总结 → Codex 审查总结 
                ↑                                    ↓
                └──── 反馈循环（发现问题就继续）←────┘
                                                     ↓ (输出 COMPLETE)
                                            Codex Code Review
                                            ↓ 发现 [P0-9] 问题
                                            Claude 修复 → 再次审查
                                            ↓ 无问题
                                            Finalize → 完成
```

**两个阶段**：
- **实现阶段（Build Phase）**：Claude 按计划编码，Codex 审查工作摘要，不满意就打回继续
- **代码审查阶段（Review Phase）**：`codex review --base <branch>` 做 diff 级别的代码审查，按 `[P0]`~`[P9]` 标记问题严重程度

**参数选项**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `path/to/plan.md` | 实现计划文件 | 必填（除非 `--skip-impl`） |
| `--max N` | 最大迭代次数 | 42 |
| `--codex-model MODEL:EFFORT` | Codex 模型和推理力度 | `gpt-5.4:xhigh` |
| `--codex-timeout SECONDS` | 单次 Codex 审查超时 | 5400s (1.5h) |
| `--base-branch BRANCH` | 代码审查的基准分支 | 自动检测 |
| `--full-review-round N` | 全面对齐检查间隔 | 5轮 |
| `--skip-impl` | 跳过实现，直接代码审查 | false |
| `--track-plan-file` | 追踪 plan 文件不可变性 | false |
| `--push-every-round` | 每轮后推送到远程 | false |
| `--claude-answer-codex` | Claude 自行回答 Codex 的开放问题 | false |
| `--agent-teams` | 启用 Agent Teams 并行模式 | false |

### 2.2 PR Loop — 自动化 PR Review 处理

自动监控 GitHub PR 上的 Bot Review，形成修复循环：

1. 检测当前分支关联的 PR
2. 获取指定 bot（`--claude` 和/或 `--codex`）的 review 评论
3. Claude 分析并修复问题
4. 推送变更，@bot 触发重新 review
5. 轮询等待 bot 新评论（每 30s 轮询一次，每个 bot 15 分钟超时）
6. 本地 Codex 验证远程关注点是否已解决
7. 循环直到所有 bot 批准或达到最大迭代次数

### 2.3 Gen Plan — 从草稿生成结构化计划

将粗糙的草稿文档转换为标准化实现计划，包含：
- 明确的目标描述
- TDD 风格的验收标准（AC-X 格式，含正向/反向测试用例）
- 路径边界（最大/最小范围、允许/禁止的选择）
- 可行性建议和概念方案
- 依赖关系和里程碑排序

### 2.4 Ask Codex — 单次 Codex 咨询

一次性向 Codex 提问，不进入循环。用于快速获取代码审查意见、架构建议等。

### 2.5 Agent Teams Mode — 并行开发

当启用 `--agent-teams` 时，Claude 不再自己编码，而是作为 **Team Leader**：
- 将工作拆分为独立的并行任务
- 用 Task 工具创建 agent 团队
- 协调团队成员，防止文件冲突
- 监控进度，必要时重新分配工作

### 2.6 Goal Tracker 系统 — 防止目标漂移

每个 RLCR 循环维护一个 `goal-tracker.md`：
- **不可变部分**：终极目标 + 验收标准（Round 0 后锁定）
- **可变部分**：活跃任务、已完成项、延迟项、计划演变日志
- 每 N 轮（默认 5 轮）做全面对齐检查，检测停滞

### 2.7 监控仪表盘

```bash
source "/home/devcontainers/.cursor/skills/humanize/scripts/humanize.sh"
humanize monitor rlcr   # RLCR 循环监控
humanize monitor pr     # PR 循环监控
humanize monitor skill  # Ask-Codex 调用监控
```

提供实时 TUI 仪表盘：固定顶部状态栏（轮次、模型、AC 进度、Git 状态）+ 底部滚动日志。

### 2.8 Hook 系统 — 深度行为控制

| Hook | 触发时机 | 功能 |
|------|---------|------|
| `UserPromptSubmit` | 用户提交 prompt | 验证 plan 文件 |
| `PreToolUse (Write)` | 写文件前 | 防止篡改 state/summary/prompt 文件 |
| `PreToolUse (Edit)` | 编辑文件前 | 同上 |
| `PreToolUse (Read)` | 读文件前 | 防止读取 todo 等受保护文件 |
| `PreToolUse (Bash)` | 执行命令前 | 防止 force push、绕过操作等 |
| `PostToolUse (Bash)` | 命令执行后 | 捕获 session ID |
| `Stop` | Claude 试图退出时 | 触发 Codex 审查，决定放行还是打回 |

---

## 三、Codex 使用方式

### 3.1 Cursor Skill 模式（当前环境）

```bash
# 启动 RLCR 循环
"/home/devcontainers/.cursor/skills/humanize/scripts/setup-rlcr-loop.sh" path/to/plan.md

# 每轮结束后运行 gate（替代 Stop hook）
"/home/devcontainers/.cursor/skills/humanize/scripts/rlcr-stop-gate.sh"
```

Gate 返回码：`0` = 可退出，`10` = 继续下一轮，`20` = 基础设施错误

### 3.2 一次性咨询

```bash
"/home/devcontainers/.cursor/skills/humanize/scripts/ask-codex.sh" "你的问题"
"/home/devcontainers/.cursor/skills/humanize/scripts/ask-codex.sh" --codex-model gpt-5.4:high "审查 src/api/ 的错误处理"
```

### 3.3 Codex 审查提示模板

Codex 收到的审查指令要求：
- 先读原始计划文件理解全貌
- 深度批判性审查，找出实现与设计之间的差距
- 不允许接受延迟/跳过决策——必须全部完成
- 为未完成工作起草具体实现方案
- 做目标对齐检查
- 每 5 轮做全面对齐审计 + 停滞检测

---

## 四、最大化利用策略

### 策略 1：写好 Plan 是一切的基础

```bash
"/home/devcontainers/.cursor/skills/humanize/scripts/validate-gen-plan-io.sh" --input draft.md --output plan.md
```

好的 plan：清晰目标、3-7 个可验证 AC（含正反测试）、路径边界、里程碑。

### 策略 2：`--skip-impl` 审查存量代码

```bash
"/home/devcontainers/.cursor/skills/humanize/scripts/setup-rlcr-loop.sh" --skip-impl
```

### 策略 3：Agent Teams 并行化大型项目

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
"/home/devcontainers/.cursor/skills/humanize/scripts/setup-rlcr-loop.sh" plan.md --agent-teams
```

### 策略 4：PR Loop 管理 GitHub 协作

```bash
"/home/devcontainers/.cursor/skills/humanize/scripts/setup-pr-loop.sh" --claude --codex
```

### 策略 5：监控仪表盘追踪进度

```bash
source "/home/devcontainers/.cursor/skills/humanize/scripts/humanize.sh"
humanize monitor rlcr
```

### 策略 6：调节模型参数优化性价比

- 快速迭代：`--codex-model gpt-5.4:medium`
- 深度审查：`--codex-model gpt-5.4:xhigh`（默认）
- 控制成本：`--max 10`
- 缩短超时：`--codex-timeout 1800`

### 策略 7：让 Codex 的问题回到用户

默认 `ask_codex_question=true` 会将 Codex 的开放问题转给用户。推荐保持默认。

---

## 五、数据存储结构

```
.humanize/
├── rlcr/              # RLCR 循环数据
│   └── <timestamp>/
│       ├── state.md
│       ├── goal-tracker.md
│       ├── plan.md
│       ├── round-N-prompt.md
│       ├── round-N-summary.md
│       ├── round-N-review-result.md
│       ├── finalize-state.md
│       └── complete-state.md
├── pr-loop/           # PR 循环数据
│   └── <timestamp>/
│       ├── state.md
│       └── resolution-N.md
└── skill/             # 一次性咨询数据
    └── <timestamp>/
        ├── input.md
        ├── output.md
        └── metadata.md
```

---

## 六、前置依赖

- `codex` — OpenAI Codex CLI
- `gh` — GitHub CLI（PR Loop 需要）
- `git` — 版本控制
- `jq` — JSON 处理
