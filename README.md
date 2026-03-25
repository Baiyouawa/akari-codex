# OpenAkari-Codex

**自主知识获取与研究智能体系统 —— 基于 Codex/OpenAI 构建**

OpenAkari-Codex 是一套完整的自主研究操作系统，以「仓库即大脑」为核心理念，让 LLM Agent 在无状态会话之间保持持久记忆。系统的前端交互角色名为**「小白」**——它不是简单的聊天机器人，而是一个**拥有统一 Skill 体系、多轮自主推理能力的顶层智能 Agent**，同时担任 Multi-Agent 系统的队长。通过 QQ（OneBot/NapCat）、GitHub、CLI 等多通道与用户互动，背后由统一 Skill 引擎、Multi-Agent 并行调度、三层记忆反思系统驱动。

---

## 目录

- [项目概览](#项目概览)
- [系统架构](#系统架构)
- [统一 Skill 体系](#统一-skill-体系)
- [目录结构](#目录结构)
- [核心模块详解](#核心模块详解)
  - [Runner 引擎层](#runner-引擎层)
  - [Multi-Agent 系统](#multi-agent-系统)
  - [Integrations 集成层](#integrations-集成层)
- [Agent 身份与角色系统](#agent-身份与角色系统)
- [工作流与使用方法](#工作流与使用方法)
  - [快速开始](#快速开始)
  - [CLI 交互模式](#cli-交互模式)
  - [QQ 机器人模式](#qq-机器人模式)
  - [GitHub 远程指令](#github-远程指令)
  - [自主研究会话](#自主研究会话)
  - [Multi-Agent 并行任务](#multi-agent-并行任务)
- [完整功能清单](#完整功能清单)
- [数据流与存储](#数据流与存储)
- [环境变量配置](#环境变量配置)
- [设计理念](#设计理念)
- [项目起源](#项目起源)

---

## 项目概览

OpenAkari-Codex 是一套以**仓库为持久记忆**的 LLM 自主研究系统。它不仅仅是一个聊天机器人——它是一个完整的研究操作系统，能够：

- **自主推理执行**：小白作为顶层 Agent，通过多轮 JSON 推理循环自主分析任务、选择 Skill、执行操作
- **统一 Skill 体系**：28 个复合 Skill + 12 个原子工具 + 33 个系统操作（含多媒体/电话），全部统一在一个 SkillRegistry 中，共计 72+ 个 Skill
- **多媒体交互**：发送/识别图片（Vision LLM）、发送/识别语音（TTS + Whisper STT）、发送文件和表情包
- **真实电话能力**：通过 SIP trunk 拨打真实电话——实时语音对话（OpenAI Realtime API）或语音通知外呼（TTS 播放）
- **全文件系统访问**：读取本机任意位置文件（只读），删除操作需审批
- **Multi-Agent 并行调度**：小白判断任务复杂度后，可将复杂任务分配给 Multi-Agent 系统（以百合动漫角色命名的 Worker）并行处理
- **多通道交互**：通过 QQ 私聊/群聊（支持富媒体）、GitHub Issue/Discussion 评论、本地终端与用户互动
- **三层记忆系统**：短期对话记忆 → 长期事实记忆 → 定期反思总结
- **角色扮演系统**：主人可为不同 QQ 用户设定独立的角色人设，小白会以完全不同的身份与他们对话
- **完整治理体系**：审批门控、溯源记录、架构决策日志（ADR）、预算管控

```
┌──────────────────────────────────────────────────────────────┐
│                     用户交互层                                │
│  QQ(OneBot/NapCat) │ QQ官方Bot │ GitHub Actions │ CLI终端    │
├──────────────────────────────────────────────────────────────┤
│                   统一网关 (Gateway)                          │
│  消息清洗 → 权限校验 → 敏感信息过滤 → 审计日志               │
├──────────────────────────────────────────────────────────────┤
│           小白 — 顶层智能 Agent (AgentLoop)                   │
│  think → use_skill → progress → delegate/reply               │
│  统一 Skill Registry │ 多轮推理循环 │ 复杂度判断              │
├──────────────────────────────────────────────────────────────┤
│              统一 Skill 体系 (SkillRegistry)                  │
│  原子(12) │ 复合(28) │ 系统(17) │ 多媒体(7) │ 电话(5) │ 文件(4) │
├──────────────────────────────────────────────────────────────┤
│           Multi-Agent 系统 (FleetScheduler)                   │
│  任务扫描 → 认领分配 → 并发执行 → 空闲探索 → 进度仪表盘      │
├──────────────────────────────────────────────────────────────┤
│              仓库记忆层 (Repo as Brain)                       │
│  tasks/ │ logs/ │ decisions/ │ skills/ │ projects/ │ ...     │
└──────────────────────────────────────────────────────────────┘
```

---

## 系统架构

### 数据流总览

```
[QQ 用户] ──→ NapCat(OneBot WS) ──→ onebot_client.py ──┐
[GitHub 评论] ──→ Actions Workflow ──→ gateway CLI ─────┤
[终端用户] ──→ python -m runner.chat ───────────────────┤
                                                        ▼
                              ┌─────────────────────────────┐
                              │  runner.gateway              │
                              │  (消息清洗/权限/日志)         │
                              └──────────┬──────────────────┘
                                         ▼
                              ┌─────────────────────────────┐
                              │  runner.chat (ChatBot/小白)   │
                              │  ┌───────────────────────┐   │
                              │  │ 顶层 Agent (AgentLoop) │   │
                              │  │ 多轮 JSON 推理循环     │   │
                              │  │                        │   │
                              │  │ think → 分析任务       │   │
                              │  │ use_skill → 执行 Skill │   │
                              │  │ progress → 播报进展    │   │
                              │  │ delegate → 分配任务    │   │
                              │  │ reply → 最终回复       │   │
                              │  └───────┬───────────────┘   │
                              │          │                    │
                              │  ┌───────┴───────────────┐   │
                              │  │ SkillRegistry          │   │
                              │  │ 原子/复合/系统 Skill   │   │
                              │  └───────────────────────┘   │
                              └──────────┬──────────────────┘
                    ┌────────────────────┼────────────────────┐
                    ▼                    ▼                    ▼
          ┌─────────────┐    ┌──────────────────┐   ┌──────────────┐
          │ SessionRunner│    │ Multi-Agent 系统  │   │ ToolExecutor │
          │ (单任务执行)  │    │ (FleetScheduler) │   │ (原子Skill)  │
          └──────┬──────┘    └────────┬─────────┘   └──────────────┘
                 ▼                    ▼
          ┌─────────────┐    ┌──────────────────┐
          │ CodexBackend│    │ fleet.executor   │
          │ (工具循环)   │    │ (子进程Worker)   │
          └──────┬──────┘    └────────┬─────────┘
                 ▼                    ▼
          ┌─────────────────────────────────────┐
          │          OpenAI API (GPT-5.4)        │
          └─────────────────────────────────────┘
```

---

## 统一 Skill 体系

小白的一切能力都统一在 `SkillRegistry` 中，分为三类：

### 原子 Skill（12 个）

直接执行的工具操作，一步到位：

| Skill | 说明 |
|-------|------|
| `read_file` | 读取仓库内文件内容 |
| `write_file` | 写入/创建文件 |
| `list_files` | 列出目录内容 |
| `search_text` | 使用 ripgrep 搜索文本 |
| `run_shell` | 执行 shell 命令 |
| `git_status` | 查看 git 仓库状态 |
| `log_decision` | 记录架构决策 (ADR) |
| `request_approval` | 加入审批队列 |
| `web_search` | DuckDuckGo 互联网搜索 |
| `web_fetch` | 抓取网页并提取文本 |
| `get_current_time` | 获取当前北京时间 |
| `calculate` | 安全执行数学表达式 |

### 复合 Skill（28 个）

多步流程技能，每个对应一个 `skills/*/SKILL.md` 文件。小白读取 SKILL.md 作为执行指南，按步骤调用原子 Skill 完成：

| Skill | 复杂度 | 说明 |
|-------|--------|------|
| `lit-review` | medium | 文献调研：搜索论文 → 分类 → 写笔记 → 识别研究空白 |
| `orient` | opus-only | 定向评估：仓库状态扫描 → 任务选择 |
| `compound` | medium | 经验嵌入：将发现固化为 conventions/skills/patterns |
| `architecture` | high | 架构重设计：模块拆分 / 跨切面重构 |
| `design` | opus-only | 实验设计：确保方法论严谨性 |
| `diagnose` | opus-only | 结果解读：意外结果分析和归因 |
| `critique` | opus-only | 对抗审查：计划/设计的红队验证 |
| `develop` | high | 开发实现：新功能 / Bug 修复 / 代码修改 |
| `review` | high | 实验验证：指标检查 + 结论验证 |
| `publish` | high | 投稿准备：论文稿准备和提交 |
| `horizon-scan` | medium | 前沿扫描：主动探索 GenAI 新进展 |
| `report` | medium | 报告生成：状态报告 / 研究摘要 / 实验对比 |
| `project` | opus-only | 项目创建：提案/脚手架模式 |
| `synthesize` | opus-only | 综合分析：跨实验发现整合 |
| `web-search` | low | 互联网搜索封装 |
| `web-fetch` | low | 网页抓取封装 |
| `time-and-calc` | low | 时间/计算封装 |
| ... | | 共 28 个（详见 `skills/` 目录） |

### 系统 Skill（17 个核心 + 16 个多媒体/文件/电话）

Python 直接执行的内部操作：

| Skill | 说明 |
|-------|------|
| `memo_add` / `memo_list` / `memo_complete` | 备忘录管理 |
| `reminder_add` / `reminder_list` | 提醒管理 |
| `create_project` / `create_task` | 项目和任务管理 |
| `orient` | 仓库状态概览 |
| `set_persona` / `clear_persona` / `list_personas` | 角色人设管理 |
| `multiagent_start` / `multiagent_status` / `multiagent_stop` | Multi-Agent 系统控制 |
| `multiagent_report` / `multiagent_scale` / `multiagent_tasks` | Multi-Agent 报告与管理 |

#### 多媒体 Skill（7 个）

| Skill | 说明 |
|-------|------|
| `send_image` | 发送图片到 QQ（本地路径或 URL，通过 `[IMG:...]` 标签） |
| `recognize_image` | 图片识别（Vision LLM），接收图片自动触发 |
| `send_voice` | 发送语音消息（edge-tts 合成，通过 `[VOICE:...]` 标签） |
| `recognize_speech` | 语音转文字（Whisper STT），接收语音自动触发 |
| `send_file` | 发送本机文件到 QQ（通过 `[FILE:...]` 标签） |
| `send_emoji` | 发送 QQ 表情（通过 `[FACE:ID]` 标签） |
| `tts_generate` | 文字转语音，生成 mp3 文件 |

#### 文件系统 Skill（4 个）

| Skill | 说明 |
|-------|------|
| `read_system_file` | 读取本机**任意位置**文件（只读，系统关键路径受限） |
| `list_system_dir` | 列出本机任意目录内容 |
| `get_file_for_send` | 获取文件元信息（准备发送） |
| `request_file_delete` | 提交删除请求到审批队列（需主人确认后执行） |

#### 电话 Skill（5 个）

| Skill | 说明 |
|-------|------|
| `phone_check_setup` | 检查 SIP/Realtime API 配置状态 |
| `phone_call_realtime` | **实时语音对话电话** — SIP 拨号 → OpenAI Realtime API 双向通话 |
| `phone_call_notification` | **语音通知电话** — TTS 合成消息 → SIP 播放给对方（单向） |
| `phone_call_status` | 查询活跃通话状态 |
| `phone_recent_calls` | 列出最近通话记录 |

---

## 目录结构

```
openakari-codex/
├── runner/                     # 核心引擎层
│   ├── config.py               #   环境配置与 CodexConfig
│   ├── chat.py                 #   小白顶层 Agent (ChatBot + AgentLoop 集成)
│   ├── agent_loop.py           #   多轮 JSON 推理循环引擎
│   ├── skill_registry.py       #   统一 Skill 注册表 (原子/复合/系统/多媒体/电话)
│   ├── openai_backend.py       #   OpenAI API 后端 + 流式工具循环
│   ├── tools.py                #   12 种原子工具定义与执行器
│   ├── media_tools.py          #   多媒体工具层 (TTS/Vision/STT/文件/CQ码)
│   ├── phone_tools.py          #   真实电话工具 (SIP外呼/OpenAI Realtime)
│   ├── codex_session_runner.py #   单会话编排 (orient→select→execute→commit)
│   ├── scheduler.py            #   基于 jobs/*.json 的定时调度
│   ├── gateway.py              #   远程通道统一入口
│   ├── persona.py              #   角色系统 + Agent Prompt + 百合动漫命名
│   ├── memory.py               #   三层记忆系统 (短期/长期/反思)
│   └── memo.py                 #   备忘录与提醒系统
│
├── fleet/                      # Multi-Agent 系统
│   ├── config.py               #   Multi-Agent 配置与核心数据类型
│   ├── scheduler.py            #   Multi-Agent 主调度循环 (refill loop)
│   ├── executor.py             #   Worker 子进程执行器
│   ├── task_scanner.py         #   TASKS.md 解析与任务发现
│   ├── task_claims.py          #   任务认领与释放 (原子锁)
│   ├── task_supply.py          #   跨项目任务供给统计
│   ├── prompt_builder.py       #   Worker prompt 构建器
│   ├── idle_tasks.py           #   空闲探索任务 (horizon-scan 等)
│   ├── dashboard.py            #   终端进度仪表盘
│   ├── status.py               #   Multi-Agent 指标追踪
│   ├── rebase_push.py          #   Git rebase/push 管理
│   ├── file_lock.py            #   文件级锁
│   ├── console.py              #   Multi-Agent 控制台 UI
│   └── workstreams.yaml        #   工作流配置
│
├── integrations/               # 外部平台集成
│   ├── config_qq.py            #   OneBot/QQ 配置
│   ├── onebot_client.py        #   NapCat WebSocket 客户端 (支持多媒体收发)
│   └── qq_bot.py               #   QQ 官方 Bot SDK (频道/群)
│
├── prompts/                    # Agent 系统提示词
│   ├── system.md               #   系统 prompt
│   └── developer.md            #   开发者 prompt (仓库规范)
│
├── projects/                   # 研究项目工作区
│   ├── akari/                  #   元项目 — 系统自改进
│   ├── moe/                    #   MoE 研究工作区
│   └── multi-agent-survey/     #   多智能体系统综述
│
├── skills/                     # 28 种复合 Skill (SKILL.md)
├── decisions/                  # 67+ 架构决策记录 (ADR)
├── tasks/                      # 全局任务定义
├── jobs/                       # 调度作业配置 (JSON)
├── logs/                       # 会话日志 + 记忆存储
│   ├── sessions/               #   研究会话日志 (JSON)
│   ├── xiaobai/                #   小白记忆 (JSONL)
│   └── remote-invocations.jsonl #  远程调用审计日志
├── artifacts/                  # 会话溯源记录
├── approvals/                  # 审批归档
├── docs/                       # 设计文档与 SOP
├── examples/                   # 示例项目脚手架
├── .fleet/                     # Multi-Agent 运行时状态
├── .github/workflows/          # GitHub Actions 工作流
│
├── AGENTS.md                   # Agent 操作手册
├── MIGRATION_MAP.md            # 从 OpenAkari 迁移记录
├── APPROVAL_QUEUE.md           # 人类审批队列
├── LICENSE                     # MIT 许可证
└── requirements.txt            # Python 依赖
```

---

## 核心模块详解

### Runner 引擎层

Runner 是整个系统的核心引擎，包含小白 Agent、推理循环、Skill 注册表、工具执行和用户交互。

#### `runner/agent_loop.py` — 多轮 Agent 推理循环（**新核心**）

`AgentLoop` 是小白作为顶层 Agent 的推理引擎。每一轮，小白输出一个 JSON action，AgentLoop 执行后反馈结果，进入下一轮：

```
while not done and turn < max_turns:
    1. 小白分析当前状态（think）
    2. 选择一个 Skill 和参数（use_skill），或播报进展（progress）
    3. 执行 Skill，收集结果
    4. 结果反馈给 LLM，回到 1
    5. 任务完成，输出最终回复（reply）
```

支持的 5 种 action：

| Action | 说明 |
|--------|------|
| `think` | 内部推理——分析任务、规划策略（用户不可见） |
| `use_skill` | 调用一个 Skill（原子/复合/系统均可） |
| `progress` | 向用户播报当前执行进展 |
| `delegate` | 将复杂任务分配给 Multi-Agent 系统 |
| `reply` | 最终回复用户，结束循环 |

**复合 Skill 执行机制**：当小白选择一个复合 Skill（如 `lit-review`）时，AgentLoop 读取对应的 `SKILL.md` 全文注入对话上下文，小白按步骤调用原子 Skill 依次完成。

#### `runner/skill_registry.py` — 统一 Skill 注册表（**新核心**）

`SkillRegistry` 在启动时自动扫描并注册所有 Skill：

1. 扫描 `skills/*/SKILL.md` → 注册为复合 Skill（解析 frontmatter 获取名称/描述/复杂度）
2. 注册 `tools.py` 中所有工具 → 注册为原子 Skill
3. 注册备忘/提醒/项目管理/人设/Multi-Agent 操作 → 注册为系统 Skill

提供 `build_skill_catalog()` 方法生成 Skill 目录文本，动态注入 Agent 的 system prompt。

#### `runner/chat.py` — 小白交互中枢

`ChatBot` 是整个系统的用户交互核心，所有入口（CLI / QQ / GitHub）最终都调用 `ChatBot.process_message()`：

**处理流程**：
1. **权限判断**：`role="owner"` → 主人模式（完整权限），`role="public"` → 普通用户（仅聊天）
2. **硬编码指令匹配**：正则匹配人设设定指令（绕过 LLM，确保可靠执行）
3. **到期提醒检查**：检查是否有到期的备忘提醒
4. **启动 Agent 循环**：创建 `AgentLoop` 实例，注入 Skill 目录、记忆上下文、仓库状态
5. **多轮推理执行**：小白自主 think → use_skill → progress → reply
6. **记忆保存**：每轮对话保存到短期记忆，定期触发反思

与旧架构的区别：
- ~~旧：意图路由器（1轮）→ 固定 handler 执行 → 结果润色（1轮）~~
- **新：多轮 Agent 循环——小白自主分析、选择 Skill、按步骤执行、播报进展、汇总回复**

#### `runner/config.py` — 环境配置

`CodexConfig` 数据类，从环境变量加载所有配置：

| 配置项 | 环境变量 | 说明 |
|--------|----------|------|
| API 密钥 | `OPENAI_API_KEY` | OpenAI 兼容 API 的认证密钥 |
| API 端点 | `OPENAI_BASE_URL` | API 地址（默认 `https://code.vangularcode.asia/v1`） |
| 模型 | `OPENAI_MODEL` | 使用的模型（默认 `gpt-5.4`） |
| 仓库根路径 | `OPENAKARI_HOME` | 仓库根目录（默认当前目录） |
| 最大轮次 | `CODEX_MAX_TURNS` | Agent 单次任务最大推理轮次 |
| Shell 白名单 | — | 允许执行的 shell 命令前缀列表 |
| Shell 黑名单 | — | 禁止执行的 shell 命令关键词 |
| 写入作用域 | `write_scope` | Multi-Agent Worker 的文件写入范围限制 |

#### `runner/openai_backend.py` — AI 后端

`CodexBackend` 是底层 AI 推理模块（主要供 Multi-Agent Worker 使用），实现流式工具调用循环。小白自身使用 `AgentLoop` 驱动推理，不再依赖此模块的 function calling。

#### `runner/tools.py` — 工具执行器

`ToolExecutor` 提供 12 种原子工具的 Python 执行实现。安全机制包括路径沙盒、写入作用域、Shell 白/黑名单、文件大小限制。

#### `runner/media_tools.py` — 多媒体工具层

提供 QQ 多媒体交互的完整工具链：

| 功能 | 实现 |
|------|------|
| **TTS 语音合成** | `edge-tts` 引擎，支持多种中文语音（女声/男声/温柔/播音），生成 mp3 |
| **图片识别** | OpenAI Vision API，支持本地文件路径或 URL，自动 base64 编码 |
| **语音识别** | OpenAI Whisper API，AMR/MP3/WAV 格式，中文优化 |
| **全文件系统访问** | 只读访问本机任意路径，系统关键路径受限，二进制文件检测 |
| **文件删除审批** | 写入 APPROVAL_QUEUE.md，需主人确认后手动执行 |
| **CQ 码构建** | 自动构建图片/语音/表情的 CQ 码用于 QQ 发送 |
| **CQ 码解析** | 从 raw_message 提取图片/语音/文件信息 |

#### `runner/phone_tools.py` — 真实电话工具

两种电话模式：

| 模式 | 架构 | 用途 |
|------|------|------|
| **实时语音对话** | SIP trunk → RTP → WebSocket → OpenAI Realtime API | 双向通话，AI 实时与对方交流 |
| **语音通知外呼** | edge-tts → mp3 → SIP → 对方手机 | 单向播放语音消息（提醒/通知） |

通话全程自动记录到 `logs/phone-calls.jsonl`（时间戳、通话时长、完整转录文本）。

#### `runner/persona.py` — 角色与人设系统

核心 Prompt 定义：

| 组件 | 说明 |
|------|------|
| `XIAOBAI_AGENT_PROMPT` | **顶层 Agent 核心 Prompt**——定义小白身份、Skill 使用、action 格式、复杂度判断、Multi-Agent 调度 |
| `XIAOBAI_SYSTEM_PROMPT` | 主人模式人设（活泼可爱、第三人称自称、禁止模板回复） |
| `XIAOBAI_PUBLIC_PROMPT` | 普通用户模式（友好聊天、不暴露系统信息） |
| `AgentRole` | Multi-Agent 角色枚举：KNOWLEDGE / IMPLEMENTATION / DEFAULT / IDLE |
| `AGENT_NAME_POOLS` | 百合动漫角色命名池（调研组/执行组/通用组/探索组） |
| 角色扮演系统 | 主人可为任意 QQ 用户设定自定义人设 |

#### `runner/memory.py` — 三层记忆系统

| 层级 | 文件 | 说明 |
|------|------|------|
| **短期记忆** | `short_term.jsonl` | 最近 50 轮对话，自动滚动淘汰 |
| **长期记忆** | `long_term.jsonl` | 从对话中提炼的重要事实，最多 200 条 |
| **反思日志** | `reflections.jsonl` | 每 10 轮对话自动反思，总结要点和洞察 |

#### `runner/memo.py` — 备忘与提醒

| 功能 | 说明 |
|------|------|
| 备忘录 | 添加/列出/完成备忘条目 |
| 定时提醒 | 设置提醒时间，到期时自动提示 |
| 时间解析 | 支持自然语言时间描述（"明天下午3点"、"2小时后"等） |

#### `runner/codex_session_runner.py` — 单会话编排

`SessionRunner` 实现自主研究会话的完整生命周期：Orient → Select → Execute → Commit

#### `runner/gateway.py` — 远程通道网关

所有外部通道的统一入口：消息清洗、权限校验、敏感信息脱敏、结果截断、审计日志。

---

### Multi-Agent 系统

Multi-Agent 系统实现了多 Agent 并行任务执行，由小白作为队长统一调度。

#### `fleet/scheduler.py` — Multi-Agent 主调度器

`FleetScheduler` 实现周期性 refill 循环：

```
每 30 秒一个 tick:
  1. 检查空闲 Worker 槽位
  2. 扫描所有项目的 TASKS.md 发现待办任务
  3. 排除已认领/阻塞/不符合筛选条件的任务
  4. 按项目并发上限 (K=4) 分配任务
  5. 派遣 Worker 子进程执行
  6. 剩余槽位 → 空闲探索任务
  7. 收集已完成 Worker 的结果
  8. 定期清理会话分支
```

**关键特性**：每项目并发上限 K、连续失败熔断、后台运行、优雅排空、Kill Switch (`FLEET_SIZE=0`)。

#### 其他 Fleet 模块

| 模块 | 说明 |
|------|------|
| `fleet/executor.py` | Worker 子进程执行器，scoped 配置 + CodexBackend |
| `fleet/task_scanner.py` | TASKS.md 解析与任务发现 |
| `fleet/task_claims.py` | 基于 `.fleet/claims.json` 的原子认领 |
| `fleet/idle_tasks.py` | 空闲探索任务（horizon-scan / open-question / self-audit） |
| `fleet/dashboard.py` | 终端实时进度仪表盘 |
| `fleet/workstreams.yaml` | 工作流与技能映射配置 |

---

### Integrations 集成层

#### `integrations/onebot_client.py` — NapCat/OneBot QQ 客户端

通过 OneBot v11 正向 WebSocket 协议连接 NapCat，支持完整多媒体交互：

- **主人私聊**：完整权限，可执行所有操作
- **普通用户私聊**：需主人先设定人设才能对话
- **群聊**：仅响应 @机器人 的消息
- **好友请求自动同意**：通过后通知主人设定人设
- **长消息分片** / **`|||` 多段发送** / **主动 follow-up** / **人性化延迟**

多媒体能力：

| 方向 | 能力 | 实现 |
|------|------|------|
| **接收图片** | 自动下载 + Vision LLM 识别 | `[收到图片，内容识别: ...]` 注入消息 |
| **接收语音** | 自动下载 + Whisper STT 转文字 | `[收到语音消息，识别内容: ...]` 注入消息 |
| **发送图片** | 回复中检测 `[IMG:...]` 标签 | 自动构建 `[CQ:image]` 发送 |
| **发送语音** | 回复中检测 `[VOICE:...]` 标签 | 自动 TTS 合成 → `[CQ:record]` 发送 |
| **发送文件** | 回复中检测 `[FILE:...]` 标签 | 调用 `upload_private_file` / `upload_group_file` |
| **发送表情** | 回复中检测 `[FACE:ID]` 标签 | 内嵌 `[CQ:face]` |

#### `.github/workflows/akari-command.yml` — GitHub Actions

在 Issue 或 Discussion 中评论 `/akari <命令>` 触发自动执行。

---

## Agent 身份与角色系统

### 小白（顶层 Agent + Multi-Agent 队长）

| 属性 | 值 |
|------|-----|
| **名字** | 小白 |
| **主人** | 白侑（小侑） |
| **性格** | 活泼可爱、二次元风格、偶尔卖萌但做事靠谱 |
| **自称** | 第三人称（"小白觉得..."、"小白帮你看看~"） |
| **角色** | **顶层智能 Agent** + Multi-Agent 系统队长 |
| **能力** | 拥有完整 Skill 体系，多轮自主推理，任务复杂度判断，Multi-Agent 调度 |

小白的工作模式：

- **简单任务**（闲聊、简单问答、单次查询）→ think + reply，或 1 个原子 Skill
- **中等任务**（需多步操作的调研、分析）→ 使用复合 Skill 按步骤执行
- **复杂任务**（跨项目、多任务并行、大规模调研）→ delegate 给 Multi-Agent 系统

小白有两种权限模式：

- **主人模式** (`role="owner"`)：对白侑使用，拥有完整 Skill 权限
- **普通用户模式** (`role="public"`)：对其他人使用，仅限日常聊天

### Multi-Agent Worker（百合动漫角色）

小白是队长，手下的 Worker Agent 以百合动漫角色命名：

| 组别 | 角色名 | 职责 |
|------|--------|------|
| **调研组** (knowledge) | 灯里、沙弥香、柑奈、日向、文乃、千早、理世、绫 | 文献调研、知识梳理、数据分析 |
| **执行组** (implementation) | 千束、柚子、安达、心奈、真白、青叶、宁宁、芽衣 | 代码编写、任务执行、Bug 修复 |
| **通用组** (default) | 侑、岛村、智乃、结衣、由希奈、枫、花阳、果穗 | 灵活支援各种任务 |
| **探索组** (idle) | 京子、莲华、可可、面码 | 好奇心旺盛，负责前沿探索 |

### 自主研究 Agent

遵循 `AGENTS.md` 操作手册的无状态研究 Agent：每个会话从 orient → select → execute → commit，仅通过仓库文件保持跨会话记忆。

### 角色扮演代理

主人可以为任意 QQ 用户设定独立的角色人设。一旦设定，小白以完全不同的身份和该用户对话，并使用 `|||` 分隔多条消息模拟真人 QQ 聊天。

---

## 工作流与使用方法

### 快速开始

```bash
# 1. 设置环境变量
export OPENAI_API_KEY="your_key"
export OPENAI_BASE_URL="https://code.vangularcode.asia/v1"
export OPENAI_MODEL="gpt-5.4"
export OPENAKARI_HOME="$(pwd)"

# 2. 安装依赖
pip install -r requirements.txt

# 3. 选择运行方式（见下方各模式说明）
```

### CLI 交互模式

```bash
# 交互模式
python -m runner.chat

# 单条命令模式
python -m runner.chat "看看现在什么状态"
```

可以说的话示例：
- `"看看现在什么状态"` → 小白自主 orient，汇报仓库和项目状态
- `"帮我调研一下多智能体系统的最新进展"` → 小白加载 lit-review 复合 Skill 按步骤执行
- `"创建一个关于 RAG 优化的项目"` → 小白调用 create_project 系统 Skill
- `"启动8个Agent跑任务"` → 小白调用 multiagent_start 系统 Skill
- `"搜索一下今天哈尔滨天气"` → 小白调用 web_search 原子 Skill
- `"记住：明天要提交周报"` → 小白调用 memo_add 系统 Skill
- `"对123456扮演一个大学学姐"` → 硬编码匹配，直接执行

### QQ 机器人模式

```bash
export ONEBOT_SELF_QQ="你的QQ号"
export ONEBOT_WS_URL="ws://localhost:3001"
export ONEBOT_OWNER_QQ="主人的QQ号"
python3 -m integrations.onebot_client
```

### GitHub 远程指令

在 Issue 或 Discussion 中评论：`/akari 帮我看看目前有什么未完成的任务`

### 自主研究会话

```bash
python -m runner.codex_session_runner --task tasks/demo_task.md
python -m runner.codex_session_runner --orient-only
python -m runner.scheduler
```

### Multi-Agent 并行任务

```bash
# 方式一：CLI 直接启动
python -m fleet.scheduler --max-workers 8

# 方式二：通过小白启动（CLI / QQ 均可）
"启动8个Agent跑任务"
"启动4个Agent只跑moe项目"

# 查看状态
"Multi-Agent 状态"
"伙伴们在干嘛"

# 调整规模
"调整到12个Agent"

# 查看结果
"看看报告"

# 停止
"停止 Multi-Agent"
```

---

## 完整功能清单

### 聊天与问答
- 日常闲聊、知识问答
- 多轮对话记忆（记住之前聊了什么）
- 自动反思总结（每 10 轮对话提炼重要事实）

### 自主推理执行
- 多轮 Agent 循环（think → use_skill → progress → reply）
- 任务复杂度判断（简单/中等/复杂）
- 流式进展播报

### 信息获取
- 联网搜索（DuckDuckGo）
- 网页内容抓取
- 当前时间查询（北京时间）
- 数学表达式计算

### 研究项目管理
- 创建新研究项目
- 添加/查看/管理任务
- 文献调研（加载 lit-review Skill 按步骤执行）
- 查看仓库和项目状态

### Multi-Agent 系统
- 启动/停止/缩放 Multi-Agent 系统
- 查看运行状态和仪表盘
- 查看执行报告
- 按项目筛选任务
- 空闲探索（前沿扫描、自审计、开放问题调研）

### 备忘与提醒
- 添加/列出/完成备忘录
- 设置定时提醒（支持自然语言时间）
- 到期自动提示

### 角色扮演
- 为任意 QQ 用户设定自定义角色人设
- 列出/清除已设定的人设
- 新好友自动通知主人确认人设

### 多媒体交互
- **发送图片**：本地文件路径或 URL，自动构建 CQ 码发送
- **识别图片**：接收 QQ 图片后自动用 Vision LLM 识别内容，支持 OCR
- **发送语音消息**：edge-tts 合成中文语音条，多种音色可选（女声/男声/温柔/播音）
- **识别语音消息**：接收 QQ 语音条后自动用 Whisper 转文字
- **发送文件**：发送本机任意文件到 QQ 对话
- **发送表情**：QQ 标准表情

### 文件系统访问
- **全系统只读**：读取本机任意位置的文件和目录（系统关键路径受限）
- **删除需审批**：删除请求写入 APPROVAL_QUEUE.md，需主人手动确认
- **二进制检测**：自动识别二进制文件，仅发送不显示内容

### 真实电话
- **实时语音对话**：SIP 拨号 → 双向音频流 → OpenAI Realtime API，AI 实时与对方通话
- **语音通知外呼**：TTS 合成消息 → SIP 播放给对方手机（闹钟/提醒/通知）
- **通话记录**：自动保存通话时间、时长、完整转录到 `logs/phone-calls.jsonl`
- **配置检查**：`phone_check_setup` 一键检查 SIP 和 API 配置状态

### 治理与审计
- 架构决策记录 (ADR) — 67+ 条记录
- 审批门控、会话溯源、远程调用审计日志

---

## 数据流与存储

```
logs/
├── sessions/                  # 研究会话日志
├── xiaobai/                   # 小白记忆存储
│   ├── short_term.jsonl       #   短期记忆 (最近 50 轮对话)
│   ├── long_term.jsonl        #   长期记忆 (重要事实)
│   ├── reflections.jsonl      #   反思日志
│   ├── memos.jsonl            #   备忘录
│   └── reminders.jsonl        #   定时提醒
└── remote-invocations.jsonl   # 远程通道调用审计日志

artifacts/
└── provenance-session-*.json  # 会话溯源

decisions/
└── 0001-*.md ~ 0067-*.md      # 架构决策记录 (ADR)

.fleet/
├── claims.json                # 任务认领状态
└── idle-cooldown.json         # 空闲探索冷却
```

---

## 环境变量配置

### 必需

| 变量 | 说明 |
|------|------|
| `OPENAI_API_KEY` | OpenAI 兼容 API 密钥 |

### 推荐

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `OPENAI_BASE_URL` | `https://code.vangularcode.asia/v1` | API 端点 |
| `OPENAI_MODEL` | `gpt-5.4` | 使用的模型 |
| `OPENAKARI_HOME` | 当前目录 | 仓库根路径 |

### QQ 机器人

| 变量 | 说明 |
|------|------|
| `ONEBOT_SELF_QQ` | 机器人 QQ 号 |
| `ONEBOT_WS_URL` | NapCat WebSocket 地址（默认 `ws://localhost:3001`） |
| `ONEBOT_OWNER_QQ` | 主人 QQ 号 |
| `ONEBOT_TOKEN` | 连接 Token（可选） |

### Multi-Agent 系统

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `FLEET_SIZE` | `32` | 最大 Worker 数 |
| `FLEET_MAX_PER_PROJECT` | `4` | 每项目并发上限 |
| `FLEET_POLL_INTERVAL` | `30` | 轮询间隔（秒） |
| `FLEET_WORKER_MAX_TURNS` | `64` | 单 Worker 最大轮次 |
| `FLEET_WORKER_TIMEOUT` | `900` | 单 Worker 超时（秒） |
| `FLEET_IDLE_EXPLORATION` | `1` | 启用空闲探索 |

### 真实电话（SIP + OpenAI Realtime）

| 变量 | 说明 |
|------|------|
| `SIP_SERVER` | SIP 服务器地址（如 `sip.qcloud.com`） |
| `SIP_USERNAME` | SIP 账号 |
| `SIP_PASSWORD` | SIP 密码 |
| `SIP_CALLER_ID` | 主叫号码 |

实时语音对话电话还需要 `OPENAI_API_KEY` + OpenAI Realtime API 访问权限。

### 多媒体依赖

| Python 包 | 用途 |
|-----------|------|
| `edge-tts` | 文字转语音（TTS）合成 |
| `openai` | Vision 图片识别、Whisper 语音识别 |
| `websockets` | OneBot 连接 + OpenAI Realtime API |

安装：`pip install edge-tts openai websockets`

SIP 外呼还需要系统级安装 PJSIP：`apt-get install pjsua`

---

## 设计理念

- **仓库即大脑** — Agent 在会话之间没有内存，仓库就是它的持久记忆。所有发现、决策、状态都以文件形式存在仓库中。
- **Skill 即能力** — 一切操作统一为 Skill。原子工具、多步流程、系统操作共存于同一个 Registry，Agent 通过 JSON action 调用。
- **Agent 即思考者** — 小白不是路由器，而是真正的 Agent。它会 think、plan、execute、reflect，自主决定用什么 Skill、是否需要 Multi-Agent 协作。
- **溯源优于断言** — 每个数值声明必须关联到产生它的脚本+数据文件，或内联的引用数据算术。
- **约定优于配置** — 统一的模式和 SOP 减少漂移。
- **知识产出优于任务完成** — 系统的根本效率指标是"每美元产出的发现数"。
- **角色即接口** — 不同用户看到不同的小白：主人看到全能 Agent，普通用户看到聊天伙伴，角色扮演用户看到主人设定的人设。

---

## 项目起源

从 [OpenAkari](https://github.com/victoriacity/openakari)（MIT 许可证）迁移而来。原项目基于 Claude Code / Anthropic Claude Agent SDK，本项目将整个后端替换为 OpenAI Responses API / Codex 模型，并新增了 QQ 集成、角色系统、记忆系统、Multi-Agent 调度、统一 Skill 体系等功能。

完整迁移记录见 [MIGRATION_MAP.md](MIGRATION_MAP.md)。
