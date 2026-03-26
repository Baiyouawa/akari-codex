# OpenAkari-Codex

**自主知识获取与研究智能体系统 —— 基于 OpenAI Codex 构建**

OpenAkari-Codex 是一套完整的自主研究操作系统，以「**仓库即大脑**」为核心理念，让 LLM Agent 在无状态会话之间保持持久记忆。系统的前端交互角色名为**「小白」**——它不是简单的聊天机器人，而是一个拥有统一 Skill 体系、多轮自主推理能力的**顶层智能 Agent**，同时担任 Multi-Agent 系统的队长。

通过 **QQ（OneBot/NapCat）、GitHub Issue/Discussion、CLI 终端**等多通道与用户互动，背后由统一 Skill 引擎、Multi-Agent 并行调度（30+ Worker）、三层记忆反思系统、独立代码审查闭环（Humanize/RLCR）驱动。

---

## 目录

- [快速开始](#快速开始)
  - [环境要求](#环境要求)
  - [安装步骤](#安装步骤)
  - [第一次运行](#第一次运行)
- [系统架构总览](#系统架构总览)
  - [数据流全景图](#数据流全景图)
  - [目录结构](#目录结构)
- [四种运行模式](#四种运行模式)
  - [模式 1: CLI 终端交互](#模式-1-cli-终端交互)
  - [模式 2: QQ 机器人](#模式-2-qq-机器人)
  - [模式 3: GitHub 远程指令](#模式-3-github-远程指令)
  - [模式 4: 自主研究调度](#模式-4-自主研究调度)
- [统一 Skill 体系](#统一-skill-体系)
  - [原子 Skill（12 个）](#原子-skill12-个)
  - [复合 Skill（30 个）](#复合-skill30-个)
  - [系统 Skill（33 个）](#系统-skill33-个)
- [核心模块详解](#核心模块详解)
  - [AgentLoop — 多轮推理循环引擎](#agentloop--多轮推理循环引擎)
  - [SkillRegistry — 统一能力注册表](#skillregistry--统一能力注册表)
  - [ChatBot — 交互中枢](#chatbot--交互中枢)
  - [Gateway — 远程通道网关](#gateway--远程通道网关)
  - [三层记忆系统](#三层记忆系统)
  - [备忘与提醒](#备忘与提醒)
  - [CodexBackend — AI 推理后端](#codexbackend--ai-推理后端)
  - [SessionRunner — 自主研究会话](#sessionrunner--自主研究会话)
  - [治理与溯源](#治理与溯源)
- [Multi-Agent 系统（Fleet）](#multi-agent-系统fleet)
  - [架构概述](#架构概述)
  - [调度机制](#调度机制)
  - [Worker 角色与命名](#worker-角色与命名)
  - [任务扫描与认领](#任务扫描与认领)
  - [空闲探索机制](#空闲探索机制)
  - [Git 推送与冲突处理](#git-推送与冲突处理)
  - [启动与操控](#启动与操控)
- [QQ 机器人完整指南](#qq-机器人完整指南)
  - [多媒体交互](#多媒体交互)
  - [角色扮演系统](#角色扮演系统)
  - [消息机制](#消息机制)
- [高级功能](#高级功能)
  - [真实电话外呼](#真实电话外呼)
  - [全文件系统访问](#全文件系统访问)
  - [Humanize 代码审查](#humanize-代码审查)
  - [GitHub Actions 集成](#github-actions-集成)
- [环境变量完整参考](#环境变量完整参考)
- [研究项目管理](#研究项目管理)
  - [创建新项目](#创建新项目)
  - [任务系统（TASKS.md）](#任务系统tasksmd)
  - [预算管理](#预算管理)
- [SOP 标准操作流程](#sop-标准操作流程)
- [常见问题与故障排查](#常见问题与故障排查)
- [开发与扩展指南](#开发与扩展指南)
  - [新增 Skill](#新增-skill)
  - [新增原子工具](#新增原子工具)
  - [新增系统 Skill](#新增系统-skill)
- [设计理念](#设计理念)
- [项目起源](#项目起源)

---

## 快速开始

### 环境要求

| 要求 | 最低版本 | 说明 |
|------|----------|------|
| Python | 3.10+ | 核心运行环境 |
| Git | 2.30+ | 仓库管理和 Fleet rebase/push |
| OpenAI 兼容 API | — | 必须有可用的 API 端点和密钥 |

可选依赖（按功能需要安装）：

| 依赖 | 用途 | 安装 |
|------|------|------|
| `edge-tts` | TTS 语音合成 | `pip install edge-tts` |
| `botpy` / `qq-botpy` | QQ 官方 Bot SDK | `pip install qq-botpy` |
| `pjsua` | SIP 电话外呼 | `apt-get install pjsua` |
| `codex` CLI | Humanize/RLCR 代码审查 | 另行安装 |

### 安装步骤

```bash
# 1. 克隆仓库
git clone <repo-url> openakari-codex
cd openakari-codex

# 2. 安装 Python 依赖
pip install -r requirements.txt
# requirements.txt 包含: openai>=1.0.0, websockets>=12.0

# 3. 安装可选依赖（如需 QQ 多媒体功能）
pip install edge-tts

# 4. 设置必需环境变量
export OPENAI_API_KEY="your_api_key_here"
```

### 第一次运行

最快的上手方式是 CLI 交互模式：

```bash
# 设置环境
export OPENAI_API_KEY="your_key"
export OPENAI_BASE_URL="https://code.vangularcode.asia/v1"   # 可选, 有默认值
export OPENAI_MODEL="gpt-5.4"                                  # 可选, 有默认值
export OPENAKARI_HOME="$(pwd)"                                 # 可选, 默认当前目录

# 启动交互模式
python -m runner.chat
```

启动后直接和小白对话即可。试试以下命令：

```
你好！
看看现在什么状态
帮我搜索一下今天的科技新闻
记住：明天下午3点开会
```

---

## 系统架构总览

### 数据流全景图

```
┌───────────────────── 用户交互层 ──────────────────────────┐
│                                                            │
│  [QQ 用户]                                                 │
│    ├── NapCat/OneBot v11 WS ──→ onebot_client.py          │
│    │   (私聊/群@/好友请求/图片/语音/文件)                    │
│    └── 官方 Bot SDK ──→ qq_bot.py                          │
│                                                            │
│  [GitHub 评论] ──→ Actions Workflow ──→ gateway CLI         │
│  [终端用户] ──→ python -m runner.chat                       │
│                                                            │
└───────────────────────────────────────────────────────────┘
                              │
                              ▼
┌───────────────── 统一网关 (Gateway) ──────────────────────┐
│  消息清洗 → 前缀剥离 → 用户白名单 → 敏感信息脱敏          │
│  → 结果截断(4000字) → 审计日志(remote-invocations.jsonl)  │
└─────────────────────────┬────────────────────────────────┘
                          ▼
┌────────── 小白 — 顶层智能 Agent (ChatBot) ───────────────┐
│                                                           │
│  ┌─────── AgentLoop: 多轮 JSON 推理循环 ────────────┐    │
│  │                                                    │    │
│  │  1. think   — 分析任务，规划策略（用户不可见）      │    │
│  │  2. use_skill — 调用 Skill（原子/复合/系统）       │    │
│  │  3. progress — 向用户播报进展                      │    │
│  │  4. delegate — 分配给 Multi-Agent 系统             │    │
│  │  5. reply   — 最终回复用户，结束循环               │    │
│  │                                                    │    │
│  └───────────┬────────────────────────────────────────┘    │
│              │                                             │
│  ┌───────────┴────────────────────────────┐               │
│  │ SkillRegistry                           │               │
│  │ 原子(12) + 复合(30) + 系统(33) = 75+   │               │
│  └────────────────────────────────────────┘               │
│              │                                             │
│  ┌───────────┴────────────────────────────┐               │
│  │ 记忆系统: 短期(50轮) + 长期 + 反思     │               │
│  │ 备忘/提醒 │ 角色人设 │ 仓库状态感知     │               │
│  └────────────────────────────────────────┘               │
│                                                           │
└─────────────────────────┬────────────────────────────────┘
               ┌──────────┴──────────┐
               ▼                     ▼
┌──── SessionRunner ────┐  ┌──── Fleet 系统 ──────────────┐
│ 自主研究会话:          │  │ Multi-Agent 并行调度:         │
│ Orient → Select        │  │ TASKS.md扫描 → 认领 → 执行   │
│ → Execute → Commit     │  │ → Humanize审查 → push → 报告 │
│                        │  │ (百合动漫角色命名, 32 Worker) │
│ CodexBackend + 工具循环│  │ + 空闲探索(前沿扫描/自审计)  │
└────────────────────────┘  └──────────────────────────────┘
               │                     │
               └──────────┬──────────┘
                          ▼
              ┌──────────────────────┐
              │  OpenAI API (GPT-5.4) │
              └──────────────────────┘
```

### 目录结构

```
openakari-codex/
│
├── runner/                         # 核心引擎层 (5800+ 行)
│   ├── config.py                   #   CodexConfig: API/模型/安全配置
│   ├── chat.py                     #   ChatBot: 小白主入口 + AgentLoop 集成
│   ├── agent_loop.py               #   AgentLoop: 多轮 JSON 推理循环引擎
│   ├── skill_registry.py           #   SkillRegistry: 统一能力注册表
│   ├── openai_backend.py           #   CodexBackend: 流式工具循环(供 Fleet/SessionRunner)
│   ├── tools.py                    #   ToolExecutor: 12 种原子工具定义与执行
│   ├── codex_session_runner.py     #   SessionRunner: 自主会话编排
│   ├── scheduler.py                #   基于 jobs/*.json 的定时调度器
│   ├── gateway.py                  #   远程通道统一网关
│   ├── persona.py                  #   角色/人设/命名系统 + Agent Prompt
│   ├── memory.py                   #   三层记忆系统
│   ├── memo.py                     #   备忘录与定时提醒
│   ├── media_tools.py              #   多媒体: TTS/Vision/STT/文件/CQ码
│   ├── phone_tools.py              #   真实电话: SIP外呼 + OpenAI Realtime
│   ├── governance.py               #   溯源追踪 + 审批门控
│   └── humanize_bridge.py          #   Humanize RLCR/Ask-Codex 桥接层
│
├── fleet/                          # Multi-Agent 系统 (3600+ 行)
│   ├── config.py                   #   FleetConfig + 核心数据类型
│   ├── scheduler.py                #   FleetScheduler: 主调度循环
│   ├── executor.py                 #   Worker 子进程执行器 + Humanize 审查
│   ├── task_scanner.py             #   TASKS.md 解析与任务发现
│   ├── task_claims.py              #   原子任务认领(.fleet/claims.json)
│   ├── task_supply.py              #   跨项目任务供给统计
│   ├── prompt_builder.py           #   Worker 系统提示构建
│   ├── idle_tasks.py               #   空闲探索(horizon-scan/self-audit等)
│   ├── dashboard.py                #   终端实时进度仪表盘
│   ├── status.py                   #   Fleet 指标追踪
│   ├── rebase_push.py              #   Git rebase/push + session 分支兜底
│   ├── file_lock.py                #   文件级锁(fcntl)
│   ├── console.py                  #   Fleet 控制台 UI
│   └── workstreams.yaml            #   工作流/技能映射/空闲探索配置
│
├── integrations/                   # 外部平台集成 (1200+ 行)
│   ├── config_qq.py                #   OneBotConfig: QQ 连接配置
│   ├── onebot_client.py            #   NapCat WebSocket 客户端(完整多媒体)
│   └── qq_bot.py                   #   QQ 官方 Bot SDK(频道/群)
│
├── prompts/                        # Agent 系统提示词
│   ├── system.md                   #   核心系统 Prompt(安全边界/工具/原则)
│   └── developer.md                #   仓库结构说明 + 执行约定
│
├── skills/                         # 30 种复合 Skill (SKILL.md)
│   ├── architecture/               #   架构重设计
│   ├── lit-review/                 #   文献调研
│   ├── develop/                    #   代码开发
│   ├── orient/                     #   定向评估
│   ├── humanize/                   #   RLCR 代码审查
│   ├── horizon-scan/               #   前沿扫描
│   ├── critique/                   #   对抗式审查
│   └── ...                         #   共 30 个
│
├── projects/                       # 研究项目工作区
│   ├── akari/                      #   元项目 — 系统自改进
│   ├── moe/                        #   MoE 研究
│   ├── multi-agent-review-survey/  #   多智能体综述
│   └── ...                         #
│
├── jobs/                           # 调度作业配置 (JSON)
│   ├── default.json                #   默认研究会话(每小时)
│   ├── code-audit.json             #   每周代码审计(Humanize)
│   ├── multi-agent-survey.json     #   多智能体调研专项
│   └── smoke-test.json             #   冒烟测试
│
├── decisions/                      # 69 条架构决策记录 (ADR)
├── docs/                           # 设计文档
│   ├── design.md                   #   核心设计理念
│   ├── getting-started.md          #   入门指南
│   └── sops/                       #   9 份标准操作流程
│       ├── autonomous-work-cycle.md
│       ├── commit-workflow.md
│       ├── fleet-operations.md
│       ├── humanize-workflow.md
│       ├── task-lifecycle.md
│       └── ...
│
├── logs/                           # 运行时日志与记忆
│   ├── sessions/                   #   研究会话日志 (JSON)
│   ├── xiaobai/                    #   小白记忆 (JSONL)
│   │   ├── short_term.jsonl        #     短期记忆(最近50轮)
│   │   ├── long_term.jsonl         #     长期记忆(重要事实)
│   │   ├── reflections.jsonl       #     反思日志
│   │   ├── memos.jsonl             #     备忘录
│   │   └── reminders.jsonl         #     定时提醒
│   └── remote-invocations.jsonl    #   远程调用审计
│
├── artifacts/                      # 会话溯源 JSON
├── examples/                       # 示例项目脚手架
│   └── my-research-project/        #   README + TASKS + budget.yaml
├── .fleet/                         # Fleet 运行时状态(claims/cooldown)
├── .humanize/                      # Humanize RLCR 运行时数据(已 gitignore)
├── .github/workflows/              # GitHub Actions
│   └── akari-command.yml           #   Issue/Discussion 评论触发
│
├── AGENTS.md                       # Agent 操作手册
├── MIGRATION_MAP.md                # OpenAkari → Codex 迁移记录
├── APPROVAL_QUEUE.md               # 人类审批队列
├── LICENSE                         # MIT 许可证
└── requirements.txt                # Python 依赖
```

---

## 四种运行模式

OpenAkari-Codex 支持四种独立的运行模式，各有不同的适用场景：

### 模式 1: CLI 终端交互

**适用场景**：本地开发、日常使用、快速问答

```bash
# 交互模式 — 进入持续对话
python -m runner.chat

# 单条命令模式 — 执行一条指令后退出
python -m runner.chat "看看现在什么状态"
```

**你可以说的话**：

| 类别 | 示例 | 小白会做什么 |
|------|------|-------------|
| 闲聊 | `"你好！"` | 直接回复 |
| 状态查询 | `"看看现在什么状态"` | 调用 `orient` 扫描仓库 |
| 联网搜索 | `"搜索一下最新的 GPT 进展"` | 调用 `web_search` → 整理结果 |
| 文献调研 | `"调研多智能体系统最新论文"` | 加载 `lit-review` 复合 Skill 按步骤执行 |
| 项目管理 | `"创建一个 RAG 优化的项目"` | 调用 `create_project` 生成目录和文件 |
| 备忘 | `"记住明天提交周报"` | 调用 `memo_add` |
| 提醒 | `"2小时后提醒我吃药"` | 调用 `reminder_add` |
| 写文件 | `"帮我写一个 Python 脚本"` | 调用 `write_file` |
| Multi-Agent | `"启动8个Agent跑任务"` | 调用 `multiagent_start` |
| 代码审查 | `"审查一下 runner/agent_loop.py"` | 调用 `humanize_review` |

**ChatBot 内部处理流程**：

```
用户输入
  ↓
1. 权限判断: role="owner" → 完整 Agent / role="public" → 仅聊天
  ↓
2. 硬编码指令匹配: 角色扮演命令直接执行(绕过 LLM)
  ↓
3. 到期提醒检查: 前缀注入到期提醒
  ↓
4. 构建 AgentLoop:
   - 注入 SkillRegistry(75+ Skill 目录)
   - 注入记忆上下文(短期+长期+反思)
   - 注入仓库状态信息
  ↓
5. 多轮推理执行: think → use_skill → progress → reply
  ↓
6. 保存记忆: 对话存短期记忆, 每 10 轮自动反思
```

### 模式 2: QQ 机器人

**适用场景**：通过 QQ 远程与小白交互，支持完整多媒体

**前置条件**：需要运行 NapCat（OneBot v11 协议实现）。

```bash
# 设置 QQ 配置
export ONEBOT_SELF_QQ="123456789"           # 机器人 QQ 号
export ONEBOT_WS_URL="ws://localhost:3001"   # NapCat WebSocket 地址
export ONEBOT_OWNER_QQ="987654321"           # 主人 QQ 号
export ONEBOT_TOKEN=""                        # 可选, 连接 Token

# 可选: 配置其他参数
export ONEBOT_ADMIN_USERS=""                  # 管理员 QQ 号列表(逗号分隔)
export ONEBOT_REPLY_PRIVATE="true"            # 是否回复私聊
export ONEBOT_REPLY_GROUP_AT="true"           # 是否回复群 @

# 启动
python3 -m integrations.onebot_client
```

**QQ 交互权限模型**：

| 场景 | 条件 | 小白行为 |
|------|------|---------|
| **主人私聊** | QQ号 = `ONEBOT_OWNER_QQ` | 完整 Agent 权限(所有 Skill) |
| **普通用户私聊** | 已设定人设 | 按人设对话 |
| **普通用户私聊** | 未设人设 | 提示主人先设定人设 |
| **群聊 @** | @ 机器人 | role="public" 友好聊天 |
| **好友请求** | 自动同意 | 通知主人设定人设 |

详细的多媒体和角色扮演功能见 [QQ 机器人完整指南](#qq-机器人完整指南)。

### 模式 3: GitHub 远程指令

**适用场景**：在 GitHub Issue 或 Discussion 中远程操控小白

在 Issue 或 Discussion 中发评论，小白会自动回复：

```
你好小白，帮我看看目前有什么未完成的任务
```

**前置条件**：配置 GitHub Secrets：

| Secret | 说明 |
|--------|------|
| `OPENAI_API_KEY` | API 密钥 |
| `OPENAI_BASE_URL` | API 端点 |
| `OPENAI_MODEL` | 模型名称 |

**权限要求**：评论者必须是 OWNER / MEMBER / COLLABORATOR。

**工作流细节**（`.github/workflows/akari-command.yml`）：
1. 评论触发 → 给评论加 :eyes: 反应表示已收到
2. 安装 Python 依赖
3. 通过 `runner.gateway` 处理命令（最多重试 3 次，指数退避）
4. 结果回复到 Issue/Discussion（超 3800 字自动截断）
5. 成功加 :rocket: / 失败加 :confused: 反应

### 模式 4: 自主研究调度

**适用场景**：无人值守的自动研究、批量任务执行

```bash
# 方式 A: 指定任务执行单次会话
python -m runner.codex_session_runner --task tasks/demo_task.md

# 方式 B: 仅执行 Orient 阶段(查看状态和建议)
python -m runner.codex_session_runner --orient-only

# 方式 C: 启动定时调度器(按 jobs/*.json 配置循环执行)
python -m runner.scheduler

# 方式 D: Dry-run 模式(不真正执行, 仅打印计划)
python -m runner.codex_session_runner --dry-run
```

**SessionRunner 生命周期**：

```
Orient (读仓库状态、扫描任务、检查最近日志)
  ↓
Select (选择一个任务: 优先级 → 无阻塞 → skill 匹配)
  ↓
Classify (判断范围: ROUTINE / RESOURCE / STRUCTURAL)
  ↓
Execute (调用 CodexBackend 工具循环: 读文件/写文件/搜索/shell/...)
  ↓
Commit (写会话日志 + 溯源记录 + git commit)
```

**定时调度配置**（`jobs/*.json` 格式）：

```json
{
  "job_id": "default-research",
  "project_path": ".",
  "task_selector": "auto",
  "frequency_seconds": 3600,
  "model": "",
  "max_budget_usd": 10.0,
  "approval_policy": "standard",
  "output_location": "logs/sessions",
  "enabled": true
}
```

| 字段 | 说明 |
|------|------|
| `task_selector` | `"auto"` = 自动选任务; 或指定文件路径 |
| `frequency_seconds` | 执行间隔(秒). `0` = 仅执行一次 |
| `max_budget_usd` | 单次预算上限 |
| `approval_policy` | `"standard"` = 标准审批; `"relaxed"` = 宽松 |

---

## 统一 Skill 体系

小白的一切能力都统一在 `SkillRegistry` 中。启动时自动扫描注册，通过 JSON action 统一调用。

### 原子 Skill（12 个）

直接执行的工具操作，一步到位。定义在 `runner/tools.py`。

| Skill | 说明 | 参数 |
|-------|------|------|
| `read_file` | 读取仓库内文件 | `path` |
| `write_file` | 写入/创建文件 | `path`, `content` |
| `list_files` | 列出目录内容 | `path` |
| `search_text` | ripgrep 搜索文本 | `pattern`, `path`(可选) |
| `run_shell` | 执行 shell 命令 | `command` |
| `git_status` | 查看 git 状态 | — |
| `log_decision` | 记录 ADR 决策 | `title`, `content` |
| `request_approval` | 提交审批请求 | `action_type`, `description` |
| `web_search` | DuckDuckGo 搜索 | `query` |
| `web_fetch` | 抓取网页文本 | `url` |
| `get_current_time` | 获取北京时间 | — |
| `calculate` | 数学表达式计算 | `expression` |

**安全机制**：
- 路径沙盒：原子工具限制在仓库根目录内
- Shell 白名单/黑名单：`config.py` 中定义允许/禁止的命令
- 写入作用域：Fleet Worker 受 `write_scope` 限制，只能写入任务相关文件

### 复合 Skill（30 个）

多步流程技能，每个对应一个 `skills/<name>/SKILL.md` 文件。小白读取 SKILL.md 作为执行指南，通过后续多轮 Agent 循环按步骤调用原子 Skill 完成。

| Skill | 复杂度 | 说明 |
|-------|--------|------|
| `lit-review` | medium | 文献调研: 搜索论文 → 分类 → 笔记 → 研究空白识别 |
| `orient` | opus-only | 定向评估: 仓库状态扫描 → 任务选择建议 |
| `orient-simple` | medium | 简化版定向评估 |
| `compound` | medium | 经验嵌入: 发现固化为 conventions/skills/patterns |
| `compound-simple` | medium | 简化版经验嵌入 |
| `architecture` | high | 架构重设计: 模块拆分 / 跨切面重构 |
| `design` | opus-only | 实验设计: 方法论严谨性保证 |
| `develop` | high | 代码开发: 新功能 / Bug 修复 / 重构 |
| `diagnose` | opus-only | 结果解读: 异常分析与归因 |
| `critique` | opus-only | 对抗审查: 计划/设计的红队验证 |
| `review` | high | 实验验证: 指标检查 + 结论验证 |
| `publish` | high | 投稿准备: 论文稿 → arXiv 提交 |
| `synthesize` | opus-only | 综合分析: 跨实验发现整合 |
| `report` | medium | 报告生成: 状态/研究摘要/对比 |
| `horizon-scan` | medium | 前沿扫描: GenAI 新动态探索 |
| `project` | opus-only | 项目创建: 提案/脚手架 |
| `postmortem` | medium | 事后分析: Agent 产出错误根因 |
| `feedback` | medium | 反馈处理: PI/人类反馈响应 |
| `gravity` | medium | 基建判断: 是否需要基建化 |
| `self-audit` | medium | 自检: 对照 AGENTS.md 合规 |
| `refresh-skills` | medium | 技能刷新: 与源码同步 |
| `simplify` | medium | 减负: 过度复杂实现简化 |
| `audit-references` | medium | 引用核查: 文献引用验证 |
| `coordinator` | low | 运维协调 |
| `humanize` | high | RLCR 迭代开发 + Codex 审查 |
| `web-search` | low | 互联网搜索封装 |
| `web-fetch` | low | 网页抓取封装 |
| `time-and-calc` | low | 时间/计算封装 |
| `pua` | medium | 穷尽式问题解决(反复失败时触发) |
| `slack-diagnosis` | medium | Bot 行为异常排查 |

**复合 Skill 执行机制**：
1. 小白选择 `use_skill: "lit-review"`
2. AgentLoop 读取 `skills/lit-review/SKILL.md` 全文
3. SKILL.md 内容注入到对话上下文中作为执行指南
4. 小白在后续轮次中按指南步骤，依次调用原子 Skill
5. 每完成一步，用 `progress` 播报进展
6. 全部完成后，用 `reply` 汇报最终结果

### 系统 Skill（33 个）

Python 直接执行的内部操作，不经过工具循环。

**核心系统（11 个）**：

| Skill | 说明 |
|-------|------|
| `memo_add` | 记录备忘事项 |
| `memo_list` | 列出所有备忘 |
| `memo_complete` | 完成一条备忘 |
| `reminder_add` | 设置定时提醒 |
| `reminder_list` | 列出所有提醒 |
| `create_project` | 创建研究项目(自动生成 README/TASKS/目录) |
| `create_task` | 向项目添加任务 |
| `orient` | 查看仓库和项目状态 |
| `set_persona` | 为 QQ 用户设定角色人设 |
| `clear_persona` | 清除用户角色人设 |
| `list_personas` | 列出所有角色扮演 |

**Multi-Agent 操控（6 个）**：

| Skill | 说明 |
|-------|------|
| `multiagent_start` | 启动 Fleet 并行执行. 参数: `project`, `tasks`, `max_workers`, `reason` |
| `multiagent_status` | 查看运行状态 + Dashboard |
| `multiagent_stop` | 停止 Fleet |
| `multiagent_report` | 查看执行报告 |
| `multiagent_scale` | 调整 Worker 数量 |
| `multiagent_tasks` | 列出可执行任务 |

**多媒体（7 个）**：

| Skill | 说明 | 输出标签 |
|-------|------|---------|
| `send_image` | 发送图片到 QQ | `[IMG:路径或URL]` |
| `recognize_image` | Vision LLM 识别图片 | — |
| `send_voice` | TTS 合成 → 发送语音 | `[VOICE:文字]` |
| `recognize_speech` | Whisper STT 语音转文字 | — |
| `send_file` | 发送本机文件 | `[FILE:路径]` |
| `send_emoji` | 发送 QQ 表情 | `[FACE:ID]` |
| `tts_generate` | 生成 mp3 语音文件 | — |

**文件系统访问（4 个）**：

| Skill | 说明 |
|-------|------|
| `read_system_file` | 读取本机**任意位置**文件(只读, 系统路径受限) |
| `list_system_dir` | 列出本机任意目录 |
| `get_file_for_send` | 获取文件元信息(准备发送) |
| `request_file_delete` | 提交删除审批(不立即执行) |

**Humanize 代码审查（3 个）**：

| Skill | 说明 |
|-------|------|
| `humanize_review` | 请求 Codex 独立审查. 参数: `target`(文件路径), `focus`(审查重点) |
| `humanize_rlcr_setup` | 启动 RLCR 迭代循环. 参数: `plan_file`, `max`, `skip_impl` |
| `humanize_status` | 查看 Humanize 系统状态 |

**电话外呼（5 个）**：

| Skill | 说明 |
|-------|------|
| `phone_check_setup` | 检查 SIP/Realtime API 配置 |
| `phone_call_realtime` | **实时语音对话**: SIP → WebSocket → OpenAI Realtime API, 双向通话 |
| `phone_call_notification` | **语音通知外呼**: TTS → SIP, 单向播放消息 |
| `phone_call_status` | 查询通话状态 |
| `phone_recent_calls` | 列出最近通话记录 |

---

## 核心模块详解

### AgentLoop — 多轮推理循环引擎

**文件**: `runner/agent_loop.py`

AgentLoop 是小白作为顶层 Agent 的核心推理引擎。每一轮，LLM 输出一个 JSON action，AgentLoop 解析并执行，将结果反馈到消息上下文中，进入下一轮。

**5 种 Action**：

```json
// 1. think — 内部推理(用户不可见)
{"action": "think", "thought": "用户想查论文，我应该用 lit-review 技能"}

// 2. use_skill — 调用 Skill
{"action": "use_skill", "skill": "web_search", "args": {"query": "LLM agent 2026"}}

// 3. progress — 播报进展
{"action": "progress", "message": "已找到 5 篇相关论文，正在整理..."}

// 4. delegate — 分配给 Multi-Agent
{"action": "delegate", "project": "moe", "max_workers": 4, "tasks": ["调研 MoE 路由算法"]}

// 5. reply — 最终回复
{"action": "reply", "message": "调研完成！以下是主要发现..."}
```

**关键配置**：

| 配置 | 默认值 | 说明 |
|------|--------|------|
| `max_turns` | 20 | 最大推理轮次(环境变量 `CODEX_MAX_TURNS`) |
| `temperature` | 0.3 | LLM 温度 |
| `max_tokens` | 4096 | 每轮最大生成 token |
| API 重试 | 3 次 | 指数退避(3s, 6s, 9s) |

### SkillRegistry — 统一能力注册表

**文件**: `runner/skill_registry.py`

启动时自动完成三步注册：

1. **扫描 `skills/*/SKILL.md`** → 解析 YAML frontmatter → 注册为复合 Skill
2. **读取 `tools.py` 的 `TOOL_DEFINITIONS`** → 注册为原子 Skill
3. **注册系统 Skill 列表** → 备忘/提醒/多媒体/电话/Humanize/Multi-Agent 等

提供 `build_skill_catalog()` 生成 Skill 目录文本，动态注入 Agent 的 system prompt，让小白"知道"自己有哪些能力。

### ChatBot — 交互中枢

**文件**: `runner/chat.py`

所有入口（CLI / QQ / GitHub）最终都汇聚到 `ChatBot.process_message(message, role, user)`。

**两种角色模式**：
- `role="owner"` — 主人模式：完整 Agent 循环，所有 Skill 可用
- `role="public"` — 普通用户：仅聊天，不执行任何操作

**核心方法**：
- `process_message()` — 主入口
- `_build_prompt()` — 构建 LLM system prompt
- `_gather_context()` — 收集记忆和仓库状态
- `_maybe_reflect()` — 每 10 轮触发反思
- `run_interactive()` — CLI 交互循环
- `_try_hardcoded_persona_cmd()` — 硬编码的角色扮演命令

### Gateway — 远程通道网关

**文件**: `runner/gateway.py`

统一入口函数 `process_remote_message(source, user, text, config, role)`:

1. 剥离消息前缀（如 `/akari`）
2. 可选用户白名单检查（`AKARI_ALLOWED_USERS`）
3. 敏感信息脱敏（API 密钥、Token 等模式替换为 `[REDACTED]`）
4. 结果截断（最大 4000 字符）
5. 审计日志写入 `logs/remote-invocations.jsonl`

**CLI 用法**：
```bash
python -m runner.gateway --source github --user octocat --message "查看状态"
```

### 三层记忆系统

**文件**: `runner/memory.py`

| 层级 | 文件 | 容量 | 机制 |
|------|------|------|------|
| **短期记忆** | `logs/xiaobai/short_term.jsonl` | 最近 50 轮 | 每轮对话自动保存，超出滚动淘汰 |
| **长期记忆** | `logs/xiaobai/long_term.jsonl` | 最多 200 条 | 从对话中提炼的重要事实 |
| **反思日志** | `logs/xiaobai/reflections.jsonl` | 累积 | 每 10 轮自动反思总结 |

**反思触发**：`should_reflect()` 在对话轮数是 `REFLECT_EVERY_N=10` 的倍数时返回 True，`build_reflect_messages()` 构建反思 prompt 让 LLM 总结近期对话的要点。

**记忆注入**：`load_context()` 将三层记忆拼接为文本，注入 Agent 的 system prompt。

### 备忘与提醒

**文件**: `runner/memo.py`

| 功能 | 存储 | 说明 |
|------|------|------|
| 备忘录 | `logs/xiaobai/memos.jsonl` | 添加/列出/完成 |
| 定时提醒 | `logs/xiaobai/reminders.jsonl` | 到期自动提示 |

**时间解析**支持自然语言：
- `"5分钟后"` / `"2小时后"` / `"3天后"`
- `"今天下午3点"` / `"明天上午10点"` / `"后天晚上8点"`
- `"2026-04-01 14:00"`

### CodexBackend — AI 推理后端

**文件**: `runner/openai_backend.py`

基于 OpenAI Chat Completions + tools 的流式工具循环。主要供 **SessionRunner** 和 **Fleet Worker** 使用（小白自身使用 AgentLoop）。

**核心方法**：
- `run_session(task, system_prompt, tool_definitions)` — 运行完整会话
- `_stream_completion()` — 流式 API 调用
- `_assemble_messages()` — 拼装 `prompts/system.md` + `prompts/developer.md` + 任务 prompt

### SessionRunner — 自主研究会话

**文件**: `runner/codex_session_runner.py`

编排自主研究会话的完整生命周期。集成 `CodexBackend`、`ToolExecutor`、`ProvenanceTracker`、`ApprovalGate`。

**CLI 参数**：
- `--task <file>` — 指定任务文件
- `--orient-only` — 仅执行 Orient
- `--scheduler` — 调度器模式
- `--dry-run` — 不真正执行

### 治理与溯源

**文件**: `runner/governance.py`

| 组件 | 说明 |
|------|------|
| `ProvenanceRecord` | 完整会话溯源: session_id, 任务来源, 模型, 执行的命令, 读写文件, 决策, 审批, Token用量, Humanize审查 |
| `ProvenanceTracker` | 追踪工具调用 → 写入 `artifacts/provenance-*.json` |
| `ApprovalGate` | 审批门控: `auto`(只读操作) / `approval_required`(危险操作) / `denied`(永远阻止) |

**ApprovalGate 安全级别**：

| 级别 | 操作示例 |
|------|---------|
| `auto` | `read_file`, `list_files`, `search_text`, `git_status` |
| `approval_required` | `git push`, `rm -r`, `deploy`, 写 `AGENTS.md`/`decisions/` |
| `denied` | `rm -rf /`, `mkfs`, `dd if=`, `shutdown`, `reboot` |

---

## Multi-Agent 系统（Fleet）

### 架构概述

Fleet 是小白手下的 Multi-Agent 并行任务系统，由小白担任队长统一调度：

```
小白 (AgentLoop, 队长)
  ↓ multiagent_start
FleetScheduler (主调度循环, 每 30s tick)
  ├── TaskScanner — 扫描各项目 TASKS.md
  ├── TaskClaimStore — 原子认领(文件锁)
  ├── PromptBuilder — 构建 Worker prompt
  ├── Executor — 子进程执行
  │   ├── Worker "灯里-01" (调研组)
  │   ├── Worker "千束-02" (执行组)
  │   └── Worker "京子-03" (探索组)
  ├── IdleTasks — 空闲探索任务
  ├── DashboardRenderer — 终端仪表盘
  └── StatusTracker — 指标追踪
```

### 调度机制

**每 30 秒一个 tick**：

1. 检查空闲 Worker 槽位
2. 扫描所有项目 `TASKS.md` 发现待办任务
3. 排除已认领 / 阻塞 / 不符合筛选条件的任务
4. 按项目并发上限(默认 K=4)分配任务
5. 派遣 Worker 子进程执行
6. 剩余槽位 → 空闲探索任务
7. 收集已完成 Worker 的结果
8. 定期清理 session 分支

**安全机制**：
- Kill Switch: `FLEET_SIZE=0` 立即禁用
- 连续失败熔断: `max_consecutive_failures` 后暂停
- 每项目并发上限: 避免单项目独占资源
- 优雅排空: `stop_fleet()` 等待运行中任务完成
- 写入隔离: 每个 Worker 有 `write_scope` 限制

### Worker 角色与命名

Worker 以百合动漫角色命名（`runner/persona.py`），分四个组别：

| 组别 | `WorkerRole` | 角色 | 分配的 SkillType |
|------|-------------|------|-----------------|
| **调研组** | `knowledge` | 灯里、沙弥香、柑奈、日向、文乃、千早、理世、绫 | `record`, `persist`, `analyze` |
| **执行组** | `implementation` | 千束、柚子、安达、心奈、真白、青叶、宁宁、芽衣 | `execute`, `diagnose` |
| **通用组** | `default` | 侑、岛村、智乃、结衣、由希奈、枫、花阳、果穗 | `govern`, `persist` |
| **探索组** | `idle` | 京子、莲华、可可、面码 | 空闲探索任务 |

Worker ID 格式: `{角色名}-{序号}-{session_hash}`（如 `灯里-01-a3b2c1`）

### 任务扫描与认领

**TaskScanner** (`fleet/task_scanner.py`)：

- 扫描 `projects/*/TASKS.md` 中以 `- [ ]` 开头的行
- 跳过 `[in-progress]`、`[approval-needed]` 标记
- 解析 `[blocked-by: ...]` → 标记为阻塞
- `[requires-opus]` → `fleet_eligible = False`
- `[zero-resource]` → 标记为零资源任务
- 支持 `Done when:` / `Why:` 续行
- 按关键词启发式分类 `skill_type`

**TaskClaimStore** (`fleet/task_claims.py`)：

- 存储: `.fleet/claims.json`
- 锁机制: `fcntl` 文件锁实现原子认领
- 方法: `try_claim(task_id, worker_id, session_id, project)` → `claim_id` 或 None

### 空闲探索机制

当任务队列为空时，Fleet 自动进行探索性工作（`fleet/idle_tasks.py`）：

| 探索类型 | 权重 | 说明 |
|---------|------|------|
| `horizon-scan` | 3 | 扫描 GenAI 前沿动态 |
| `open-question` | 2 | 从项目 README 抽取未解决问题 |
| `self-audit` | 1 | 对照 AGENTS.md 做合规自检 |
| `stale-blocker-check` | 1 | 检查长期阻塞任务是否有进展 |

每种类型有独立冷却时间（默认 6 小时），状态持久化到 `.fleet/idle-cooldown.json`。

### Git 推送与冲突处理

**RebasePush** (`fleet/rebase_push.py`)：

Worker 完成后的 Git 推送策略：

1. 检查是否有未推送提交
2. 尝试 `git pull --rebase --autostash`（最多 3 次）
3. 成功 → `git push`
4. 失败 → 创建 `session-{id}` 分支推送，避免代码丢失
5. 定期清理过旧的远程 `session-*` 分支

### 启动与操控

**方式 1: CLI 直接启动**

```bash
python -m fleet.scheduler --max-workers 8
```

**方式 2: 通过小白(CLI 或 QQ)**

```
"启动8个Agent跑任务"           → multiagent_start(max_workers=8)
"启动4个Agent只跑moe项目"      → multiagent_start(project="moe", max_workers=4)
"Multi-Agent 状态"              → multiagent_status
"伙伴们在干嘛"                  → multiagent_status
"调整到12个Agent"               → multiagent_scale(count=12)
"看看报告"                      → multiagent_report
"停止 Multi-Agent"              → multiagent_stop
"列出可执行任务"                → multiagent_tasks
```

**方式 3: 小白自动 delegate**

当小白判断任务复杂度高时，会主动输出 `delegate` action:

```json
{
  "action": "delegate",
  "project": "multi-agent-review-survey",
  "max_workers": 4,
  "tasks": ["下载论文 2501.06322", "整理文献笔记"],
  "reason": "多论文调研适合并行执行"
}
```

---

## QQ 机器人完整指南

### 多媒体交互

**接收多媒体（自动处理）**：

| 收到 | 处理方式 | 注入消息格式 |
|------|---------|-------------|
| 图片 | 自动下载 → Vision LLM 识别 | `[收到图片，内容识别: 这是一张...]` |
| 语音 | 自动下载 → Whisper STT 转文字 | `[收到语音消息，识别内容: ...]` |
| 文件 | 记录文件信息 | `[收到文件: filename]` |

**发送多媒体（小白输出标签）**：

小白在回复中包含以下标签，`onebot_client.py` 自动解析并转换为 CQ 码发送：

| 标签 | 示例 | 效果 |
|------|------|------|
| `[IMG:路径或URL]` | `[IMG:/tmp/chart.png]` | 发送图片 |
| `[VOICE:文字]` | `[VOICE:你好呀~]` | TTS 合成后发送语音条 |
| `[FILE:路径]` | `[FILE:docs/report.pdf]` | 发送文件 |
| `[FACE:ID]` | `[FACE:21]` | 发送 QQ 表情 |

**TTS 语音合成**：

| 语音名 | 说明 |
|--------|------|
| `zh-CN-XiaoxiaoNeural` | 默认女声 |
| `zh-CN-YunxiNeural` | 男声 |
| 更多 | 见 `edge-tts --list-voices` |

### 角色扮演系统

主人可以为任意 QQ 用户设定独立的角色人设：

```
# 在 QQ 私聊中对主人小白说:
对 123456789 扮演一个温柔的学姐

# 小白会确认设定
# 之后 123456789 私聊小白时, 小白以"温柔学姐"身份回复
```

**管理命令**（主人私聊）：

| 命令 | 说明 |
|------|------|
| `对 <QQ号> 扮演 <人设描述>` | 设定人设（硬编码匹配，绕过 LLM） |
| `取消 <QQ号> 的角色` | 清除人设 |
| `列出所有人设` | 查看当前所有角色扮演 |

**角色人设工作原理**：
1. 主人设定 → `set_persona_override(target_qq, description)` 存入内存
2. 目标用户发消息 → `get_persona_prompt_for_user(user_qq)` 获取人设
3. 人设覆盖默认 system prompt → 小白以新身份回复
4. 回复使用 `|||` 分隔多条消息，模拟真人 QQ 聊天节奏

### 消息机制

**消息聚合**：连续快速发送的多条消息会在 `MSG_AGGREGATE_WINDOW` 窗口内聚合为一条。

**长消息分片**：超过 QQ 单条限制的回复自动拆分。

**多段发送**：小白回复中的 `|||` 分隔符会被拆成独立消息依次发送，模拟自然对话节奏。

**好友请求**：自动同意后通知主人设定人设。

**人性化延迟**：消息之间添加适当延迟，避免机器人感。

---

## 高级功能

### 真实电话外呼

**文件**: `runner/phone_tools.py`

两种电话模式：

| 模式 | 架构 | 用途 |
|------|------|------|
| **实时语音对话** | SIP trunk → RTP → WebSocket → OpenAI Realtime API | 双向实时通话 |
| **语音通知外呼** | edge-tts → mp3 → SIP → 对方手机 | 单向语音消息播放 |

**环境变量**：

```bash
export SIP_SERVER="sip.example.com"
export SIP_USERNAME="your_sip_account"
export SIP_PASSWORD="your_sip_password"
export SIP_CALLER_ID="+8612345678"
```

**通话记录**: 自动保存到 `logs/phone-calls.jsonl`（时间戳、通话时长、完整转录）。

**使用示例**（通过小白）：

```
"打电话给 13800138000，告诉他明天开会时间改到下午3点"  → phone_call_notification
"给 13800138000 打个实时通话电话"                       → phone_call_realtime
"看看最近的通话记录"                                    → phone_recent_calls
```

### 全文件系统访问

小白可以读取本机任意位置的文件（只读），但有以下限制：

| 操作 | 权限 | 说明 |
|------|------|------|
| 读取 | 允许 | 任意路径，系统关键路径(`/etc/shadow`等)受限 |
| 列目录 | 允许 | 任意目录 |
| 删除 | 需审批 | 写入 `APPROVAL_QUEUE.md`，主人手动确认后执行 |
| 写入 | 仅仓库内 | 原子工具 `write_file` 限制在仓库根目录内 |

### Humanize 代码审查

**文件**: `runner/humanize_bridge.py`, `docs/sops/humanize-workflow.md`

集成 Humanize (RLCR / Ask-Codex / PR-Loop) 实现独立 AI 代码审查：

**三种审查模式**：

| 模式 | 触发方式 | 说明 |
|------|---------|------|
| Ask-Codex | 小白 `humanize_review` 或手动 | 一次性代码审查 |
| RLCR Loop | 小白 `humanize_rlcr_setup` 或手动 | 迭代开发循环: 实现 → 审查 → 修复 → 审查 |
| Fleet Post-Task | Fleet executor 自动 | Worker 完成代码任务后自动触发 |

**RLCR 工作原理**：

```
Plan (写计划文件 → gen-plan)
  ↓
Round 0: 实现代码 (Claude/小白)
  ↓
Codex Review: 独立审查 (找 P0-P4 问题)
  ↓
Round 1: 修复问题 (根据审查反馈)
  ↓
Codex Review: 再次审查
  ↓
... 重复直到所有验收标准通过或达到最大迭代
```

**Fleet 强制审查（每个任务必审，无例外）**：

`fleet/executor.py` 在**每个 Worker 完成后**（无论是代码任务、文档任务还是空闲探索任务）都会强制执行审查。审查策略：

1. 如果 Humanize/codex CLI 可用 → 使用 `codex review`（外部独立审查）
2. 否则 → **自动回退到直接 OpenAI API 审查**（读取文件内容 → 让 LLM 审查 → 解析 P0-P3 级问题）

这意味着审查**不依赖任何外部工具**，只要 `OPENAI_API_KEY` 可用就一定会执行。发现 P0/P1 级问题时标记任务为 `blocked`，通知主人定夺。审查记录写入 `governance.py` 的溯源系统。

**手动使用**：

```bash
# Ask-Codex: 一次性咨询
~/.cursor/skills/humanize/scripts/ask-codex.sh "审查 runner/agent_loop.py 的并发安全性"

# RLCR: 迭代开发
~/.cursor/skills/humanize/scripts/setup-rlcr-loop.sh plans/my-plan.md --max 10
```

### GitHub Actions 集成

**文件**: `.github/workflows/akari-command.yml`

在 Issue 或 Discussion 中评论即可触发小白执行命令。

**触发条件**：
- 事件: `issue_comment.created` 或 `discussion_comment.created`
- 身份: OWNER / MEMBER / COLLABORATOR
- 排除: 以 `✅` 或 `❌` 开头的评论（小白自己的回复）
- 排除: `github-actions[bot]` 的评论

**执行流程**：
1. 加 :eyes: 反应
2. `pip install -r requirements.txt`
3. `python -m runner.gateway --source github --user $USER --message "$COMMAND"`
4. 最多 3 次重试（指数退避: 15s, 30s, 60s）
5. 回复结果（限 3800 字）
6. 加成功/失败反应

---

## 环境变量完整参考

### 核心 API（必需）

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `OPENAI_API_KEY` | *无, 必填* | OpenAI 兼容 API 密钥 |
| `OPENAI_BASE_URL` | `https://code.vangularcode.asia/v1` | API 端点 |
| `OPENAI_MODEL` | `gpt-5.4` | 模型标识 |
| `OPENAKARI_HOME` | 当前工作目录 | 仓库根路径 |

### Agent 配置

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `CODEX_MAX_TURNS` | `20` | Agent 单次最大推理轮次 |
| `CODEX_TEMPERATURE` | `0.3` | LLM 温度 |

### QQ 机器人

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `ONEBOT_SELF_QQ` | — | 机器人 QQ 号 |
| `ONEBOT_WS_URL` | `ws://localhost:3001` | NapCat WebSocket 地址 |
| `ONEBOT_OWNER_QQ` | — | 主人 QQ 号 |
| `ONEBOT_TOKEN` | 空 | 连接 Token |
| `ONEBOT_ADMIN_USERS` | 空 | 管理员列表(逗号分隔) |
| `ONEBOT_REPLY_PRIVATE` | `true` | 是否回复私聊 |
| `ONEBOT_REPLY_GROUP_AT` | `true` | 是否回复群 @ |

### Multi-Agent 系统

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `FLEET_SIZE` | `32` | 最大 Worker 数. `0` = **Kill Switch 禁用** |
| `FLEET_MAX_PER_PROJECT` | `4` | 每项目并发上限 |
| `FLEET_POLL_INTERVAL` | `30` | 调度轮询间隔(秒) |
| `FLEET_WORKER_MAX_TURNS` | `64` | 单 Worker 最大轮次 |
| `FLEET_WORKER_TIMEOUT` | `900` | 单 Worker 超时(秒) |
| `FLEET_IDLE_EXPLORATION` | `1` | 启用空闲探索. `0` = 禁用 |

### 电话外呼

| 变量 | 说明 |
|------|------|
| `SIP_SERVER` | SIP 服务器地址 |
| `SIP_USERNAME` | SIP 账号 |
| `SIP_PASSWORD` | SIP 密码 |
| `SIP_CALLER_ID` | 主叫号码 |

### 代码审查

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `HUMANIZE_ROOT` | `~/.cursor/skills/humanize` | Humanize 安装路径 |

### 网关安全

| 变量 | 说明 |
|------|------|
| `AKARI_ALLOWED_USERS` | 允许的远程用户列表(逗号分隔, 空=允许所有) |

### 多媒体

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `MEDIA_CACHE_TTL` | — | 多媒体缓存过期时间 |
| `MEDIA_CACHE_MAX_MB` | — | 多媒体缓存大小上限 |

---

## 研究项目管理

### 创建新项目

**方式 1: 通过小白**

```
"创建一个关于 RAG 优化的项目"
```

小白自动生成:
```
projects/rag-优化/
├── README.md        # 包含 Status/Mission/Log 模板
├── TASKS.md         # 任务列表
├── literature/      # 文献存储
├── analysis/        # 分析产出
└── plans/           # 计划文件
```

**方式 2: 手动创建**

从脚手架复制:
```bash
cp -r examples/my-research-project projects/my-project
vim projects/my-project/README.md
vim projects/my-project/TASKS.md
```

### 任务系统（TASKS.md）

任务使用 Markdown checkbox 格式，支持以下标签：

```markdown
# 项目名 — 任务列表

- [ ] 调研 LLM Agent 的记忆机制 [skill: analyze]
  Done when: 完成至少 5 篇论文的笔记
  Why: 为记忆系统设计提供理论基础

- [ ] 实现分布式任务队列 [skill: execute]
  Done when: 通过集成测试
  [blocked-by: 需要先完成 API 设计]

- [ ] 更新项目文档 [zero-resource] [skill: record]
  Done when: README 反映最新架构

- [x] 完成初始调研 ← 已完成
```

**标签说明**：

| 标签 | 说明 |
|------|------|
| `[skill: type]` | 技能类型: record/persist/govern/execute/diagnose/analyze/orient/multi |
| `[blocked-by: ...]` | 阻塞原因, Fleet 不会认领 |
| `[in-progress: YYYY-MM-DD]` | 正在执行中, Fleet 不会重复认领 |
| `[approval-needed]` | 需要人类审批 |
| `[approved: YYYY-MM-DD]` | 已审批, 可执行 |
| `[zero-resource]` | 不消耗预算 |
| `[requires-opus]` | 需要高级模型, Fleet 不认领 |

### 预算管理

每个项目可以在 `budget.yaml` 中设定预算：

```yaml
resources:
  max_budget_usd: 50.0
  max_sessions: 100
deadline: "2026-06-30"
```

---

## SOP 标准操作流程

系统内置 9 份 SOP（`docs/sops/`），覆盖日常操作：

| SOP | 说明 |
|-----|------|
| `autonomous-work-cycle.md` | 自主工作循环: orient → select → classify → execute → compound |
| `commit-workflow.md` | Git 提交规范: stage → validate → commit |
| `fleet-operations.md` | Fleet 扩缩容、监控、故障处理 |
| `humanize-workflow.md` | Humanize/RLCR 代码审查完整流程 |
| `task-lifecycle.md` | 任务标签与认领 API |
| `tdd-workflow.md` | 测试驱动开发 |
| `url-verification.md` | 文献 URL/DOI 核实 |
| `synthesis-preflight-audit.md` | 综合写作前的数据/来源审查 |
| `opencode-contention-runbook.md` | SQLite 争用排查 |

---

## 常见问题与故障排查

### Q: 启动报错 "OPENAI_API_KEY not set"

`CodexConfig.from_env()` 在没有 `OPENAI_API_KEY` 时会立即抛出异常。确保设置了环境变量：

```bash
export OPENAI_API_KEY="your_key"
```

### Q: QQ 机器人连不上

1. 确认 NapCat 正在运行且 WebSocket 端口正确
2. 检查 `ONEBOT_WS_URL` 是否指向正确地址
3. 如果使用了 Token，确保 `ONEBOT_TOKEN` 匹配
4. 查看 `onebot_client.py` 的日志输出

### Q: 小白不回复普通 QQ 用户

普通用户需要主人先设定人设才能对话。在主人私聊中说：
```
对 <QQ号> 扮演一个友好的助手
```

### Q: Multi-Agent 启动了但没有任务在跑

1. 检查 `projects/*/TASKS.md` 中是否有 `- [ ]` 格式的开放任务
2. 确认任务没有 `[blocked-by]`、`[in-progress]`、`[approval-needed]` 标签
3. 如果指定了 `project` 过滤，确认该项目下有任务
4. 检查 `.fleet/claims.json` 是否有残留的过期认领

### Q: Fleet Worker 的代码提交冲突了

`fleet/rebase_push.py` 会自动处理：
1. 先尝试 `git pull --rebase --autostash`（最多 3 次）
2. 失败则创建 `session-{id}` 分支推送
3. 手动合并 session 分支：`git merge session-xxx`

### Q: Humanize/RLCR 不可用

1. 确认 Humanize Skill 已安装到 `~/.cursor/skills/humanize/`
2. 检查 `scripts/` 目录下是否有 `ask-codex.sh` 等脚本
3. 确认 `codex` CLI 可执行
4. 设置 `HUMANIZE_ROOT` 环境变量（如果安装路径不同）

### Q: 多媒体功能（TTS/Vision/STT）不工作

```bash
# 安装 TTS 依赖
pip install edge-tts

# Vision 和 STT 依赖 OpenAI API, 确保 API 支持
# Vision: gpt-4-vision 或更新模型
# STT: whisper-1 模型
```

### Q: 电话功能配置

```bash
# 安装 SIP 依赖
apt-get install pjsua

# 配置环境变量
export SIP_SERVER="your_sip_server"
export SIP_USERNAME="your_account"
export SIP_PASSWORD="your_password"
export SIP_CALLER_ID="+86..."

# 检查配置
python -c "from runner.phone_tools import check_phone_setup; print(check_phone_setup())"
```

---

## 开发与扩展指南

### 新增 Skill

**新增复合 Skill**：

1. 创建目录 `skills/my-skill/`
2. 创建 `SKILL.md`，包含 YAML frontmatter：

```markdown
---
name: my-skill
description: 我的新技能的简短描述
complexity: medium
allowed-tools: [read_file, write_file, search_text]
---

# My Skill

## 执行步骤

1. 第一步: ...
2. 第二步: ...
3. 最终: 用 reply 汇报结果
```

3. 重启系统，`SkillRegistry` 会自动扫描并注册

### 新增原子工具

在 `runner/tools.py` 中：

1. 在 `TOOL_DEFINITIONS` 字典中添加新工具定义
2. 在 `ToolExecutor` 中实现执行逻辑
3. `SkillRegistry` 会自动将其注册为原子 Skill

### 新增系统 Skill

1. 在 `runner/skill_registry.py` 的 `_register_system_skills()` 中添加条目
2. 在 `runner/agent_loop.py` 的 `_execute_system()` 中添加处理逻辑
3. 实现具体功能

### 新增研究项目

```bash
cp -r examples/my-research-project projects/my-new-project
vim projects/my-new-project/README.md    # 设置 Mission/Priority
vim projects/my-new-project/TASKS.md     # 添加任务
```

### 新增 ADR 决策记录

```bash
# 通过小白
"记录一个架构决策: 选择 WebSocket 而非 HTTP polling 作为实时通信方案"

# 或手动创建
vim decisions/0070-my-decision.md
```

### 新增调度作业

在 `jobs/` 下创建 JSON 文件：

```json
{
  "job_id": "my-weekly-task",
  "project_path": "projects/my-project",
  "task_selector": "auto",
  "frequency_seconds": 604800,
  "max_budget_usd": 5.0,
  "enabled": true
}
```

---

## 设计理念

| 理念 | 说明 |
|------|------|
| **仓库即大脑** | Agent 在会话间无内存，仓库是持久记忆。发现、决策、状态全部落盘为文件 |
| **Skill 即能力** | 原子工具、多步流程、系统操作统一为 Skill，Agent 通过 JSON action 调用 |
| **Agent 即思考者** | 小白不是路由器，会 think → plan → execute → reflect，自主决定策略 |
| **溯源优于断言** | 每个数值声明关联到脚本+数据文件或引用数据的内联算术 |
| **约定优于配置** | 统一模式和 SOP 减少漂移 |
| **知识产出优于任务完成** | 根本效率指标：**findings per dollar**（每美元产出的发现数） |
| **角色即接口** | 不同用户看到不同的小白：主人=全能Agent，普通用户=聊天伙伴，角色用户=自定义人设 |
| **渐进式失败** | 可选功能(Humanize/电话/TTS)不可用时静默降级，不影响核心 |

---

## 项目起源

从 [OpenAkari](https://github.com/victoriacity/openakari)（MIT 许可证）迁移而来。原项目基于 Claude Code / Anthropic Claude Agent SDK，本项目将整个后端替换为 **OpenAI Responses API / Codex 模型**，并在此基础上大幅扩展：

| 新增功能 | 说明 |
|---------|------|
| 多轮 Agent 推理循环 | AgentLoop + 5 种 Action |
| 统一 Skill 体系 | 75+ Skill 统一注册表 |
| Multi-Agent 并行系统 | Fleet 30+ Worker 调度 |
| QQ 完整多媒体 | 图片/语音/文件收发与识别 |
| 真实电话外呼 | SIP + OpenAI Realtime |
| 角色扮演系统 | 按用户定制人设 |
| 三层记忆系统 | 短期/长期/反思 |
| Humanize 代码审查 | RLCR 独立审查闭环 + Fleet 每任务强制审查(API fallback) |
| 治理与溯源 | 69 条 ADR + 审批门控 + 溯源记录 |

完整迁移记录见 [MIGRATION_MAP.md](MIGRATION_MAP.md)。
