# 开发工具链零基础调研：Cursor / VS Code / 终端 / 包管理 / 环境配置 / 基本调试

- 项目：`projects/zero-basics-plan`
- 任务：调研开发工具链资料
- 产出人：Fleet Worker `千束-00-1774523931-1f5474`
- 日期：2026-03-26

## 调研范围

本调研面向《零基础计划》的第 1 周到第 2 周工具链部分，覆盖：

1. Cursor
2. VS Code
3. 终端基础
4. 包管理
5. Python 环境配置
6. 基本调试方法
7. 面向零基础学习者的 VibeCoding 入门实践

## 结论摘要

1. **最适合零基础的主线是：VS Code 基础操作 → 终端基础 → Python 虚拟环境 → Cursor Agent/Rules/Terminal → 小项目调试。**
2. **Cursor 官方文档已经把零基础最需要的内容拆成了可教学单元**：Agents、Developing Features、Customizing Agents、Rules、Terminal、Debug Mode、CLI Installation，适合直接映射到课程日程。
3. **VS Code 官方文档适合承担“编辑器基本功”**：界面、扩展、集成终端、Python 调试都更系统，适合作为 Cursor 之前或并行的基础层。
4. **包管理不应一次讲太多**：零基础阶段只需先讲 4 类——系统包管理器（`apt` / `winget` / Homebrew）、语言包管理器（`pip`）、环境隔离（`venv`）、“优先看官方文档”的安装习惯。
5. **VibeCoding 初学者最容易踩坑的不是“不会提示词”，而是不会验证结果。** 所以课程里必须把“先跑起来、再看报错、再最小化复现、再修”作为固定动作。

## 面向零基础的教学排序

### 推荐顺序

1. **VS Code 入门**：认识编辑器、文件夹、扩展、终端入口
2. **终端入门**：会 `pwd` / `ls` / `cd`，知道“当前目录”概念
3. **Python 环境**：安装、创建 `venv`、用 `pip` 装包
4. **Cursor 入门**：Chat / Agent / Rules / Terminal
5. **基本调试**：看报错、打断点、单步执行、打印日志
6. **VibeCoding 小项目**：让 AI 帮做，但每一步都人工验证

### 不推荐顺序

- 一上来就讲多模型、复杂 Prompt Engineering、MCP、自动化工作流
- 一上来就让学员跨平台同时学 `apt + winget + brew`
- 一上来就做大型项目，而不是 30~60 分钟能完成的小练习

## 资料清单与推荐理由

## 1. Cursor

### 1.1 Cursor Docs 首页
- URL: `https://cursor.com/docs`
- 页面标题：Cursor Docs
- 页面描述：Built to make you extraordinarily productive, Cursor is the best way to build software with AI.
- 推荐理由：官方入口，适合作为总导航页。
- 适合程度：高
- 难度：入门

### 1.2 Agents | Cursor Learn
- URL: `https://cursor.com/learn/agents`
- 页面标题：Agents | Cursor Learn
- 页面描述：Documentation for Agents
- 推荐理由：适合解释“让 AI 帮你执行多步任务”是什么，帮助零基础学员把 Chat 和 Agent 区分开。
- 适合程度：中高
- 难度：入门到初级

### 1.3 Developing Features | Cursor Learn
- URL: `https://cursor.com/learn/creating-features`
- 页面标题：Developing Features | Cursor Learn
- 页面描述：Learn how to plan features, use test-driven development with agents, and build working code you can trust.
- 推荐理由：非常适合做 VibeCoding 的“正确姿势”教材，因为它强调可验证、可运行、可信任，而不是只让 AI 一把梭。
- 适合程度：高
- 难度：初级

### 1.4 Customizing Agents | Cursor Learn
- URL: `https://cursor.com/learn/customizing-agents`
- 页面标题：Customizing Agents | Cursor Learn
- 页面描述：Learn how to shape agent behavior with rules for static context and skills for dynamic capabilities.
- 推荐理由：适合引入“规则（Rules）”概念，让新手知道如何给 AI 持续约束，而不是每次重写提示词。
- 适合程度：高
- 难度：初级

### 1.5 Rules | Cursor Docs
- URL: `https://cursor.com/docs/rules`
- 页面标题：Rules | Cursor Docs
- 页面描述：Configure persistent instructions with Project, Team, and User Rules, plus AGENTS.md. Learn best practices for effective coding guidelines.
- 推荐理由：适合零基础学员建立“项目约定”的意识，可直接转化为课程中的 `.md` 规范练习。
- 适合程度：高
- 难度：初级

### 1.6 Terminal | Cursor Docs
- URL: `https://cursor.com/docs/agent/tools/terminal`
- 页面标题：Terminal | Cursor Docs
- 页面描述：Execute commands through Agent with sandboxing, preserved history, and native terminal integration. Configure sandbox.json for network and filesystem policies.
- 推荐理由：能把“AI 能调用终端”和“人要理解终端输出”连起来，适合做 VibeCoding 安全边界案例。
- 适合程度：高
- 难度：初级

### 1.7 Debug Mode | Cursor Docs
- URL: `https://cursor.com/docs/agent/debug-mode`
- 页面标题：Debug Mode | Cursor Docs
- 页面描述：Find root causes and fix tricky bugs using hypothesis generation, log instrumentation, and runtime analysis.
- 推荐理由：适合把“猜问题”升级成“定位根因”，可作为调试课扩展阅读。
- 适合程度：中高
- 难度：初级到中级

### 1.8 Debugging with Cursor | Cursor Docs
- URL: `https://cursor.com/for/debugging`
- 页面标题：Debugging with Cursor | Cursor Docs
- 页面描述：How to use Cursor to trace errors, find root causes, and fix bugs faster
- 推荐理由：可作为“AI 辅助调试”专题材料，适合课程后半段。
- 适合程度：中高
- 难度：初级到中级

### 1.9 CLI Installation | Cursor Docs
- URL: `https://cursor.com/docs/cli/installation`
- 页面标题：CLI Installation | Cursor Docs
- 页面描述：Install Cursor CLI on macOS, Linux, and Windows with a single command. Verify installation and configure PATH for optimal setup.
- 推荐理由：适合解释 PATH、命令行安装、验证安装结果这些基础概念。
- 适合程度：高
- 难度：入门

## 2. VS Code

### 2.1 Getting Started with Visual Studio Code
- URL: `https://code.visualstudio.com/docs/getstarted/getting-started`
- 页面标题：Tutorial: Get started with Visual Studio Code
- 页面描述：This tutorial gives you an overview of the key features of Visual Studio Code to help you get started quickly.
- 推荐理由：最适合零基础的编辑器总入口，可以承接“认识界面、打开文件夹、安装扩展、使用终端”。
- 适合程度：高
- 难度：入门

### 2.2 Getting Started with Python in VS Code
- URL: `https://code.visualstudio.com/docs/python/python-tutorial`
- 页面标题：Getting Started with Python in VS Code
- 页面描述：A Python hello world tutorial using the Python extension in Visual Studio Code
- 推荐理由：非常适合作为“第一次运行 Python 程序”的正式教材。
- 适合程度：高
- 难度：入门

### 2.3 Terminal Basics
- URL: `https://code.visualstudio.com/docs/terminal/basics`
- 页面标题：Terminal Basics
- 页面描述：Visual Studio Code has an integrated terminal to enable working in your shell of choice without leaving the editor.
- 推荐理由：适合把“写代码”和“运行命令”放在一个界面里教学，降低切换成本。
- 适合程度：高
- 难度：入门

### 2.4 Python debugging in VS Code
- URL: `https://code.visualstudio.com/docs/python/debugging`
- 页面标题：Python debugging in VS Code
- 页面描述：Details on configuring the Visual Studio Code debugger for different Python applications.
- 推荐理由：适合引入断点、变量查看、逐步执行，是零基础学员第一次接触“真正调试器”的好入口。
- 适合程度：高
- 难度：初级

## 3. 终端与命令行

### 3.1 Ubuntu: The Linux command line for beginners
- URL: `https://ubuntu.com/tutorials/command-line-for-beginners`
- 页面标题：The Linux command line for beginners | Ubuntu
- 页面描述：Ubuntu is an open source software operating system that runs from the desktop, to the cloud, to all your internet connected things.
- 推荐理由：标题就面向 beginners，适合作为“终端是什么、为什么要学终端”的第一份外部阅读。
- 适合程度：高
- 难度：入门

### 3.2 VS Code Terminal Basics
- URL: `https://code.visualstudio.com/docs/terminal/basics`
- 推荐理由：如果学员先在 VS Code 内置终端里操作，会比直接开系统终端更不容易迷路。
- 适合程度：高
- 难度：入门

### 3.3 Cursor Terminal
- URL: `https://cursor.com/docs/agent/tools/terminal`
- 推荐理由：适合说明 AI 可以代执行命令，但学习者必须看懂输出、知道风险边界。
- 适合程度：高
- 难度：初级

## 4. 包管理

### 4.1 WinGet
- URL: `https://learn.microsoft.com/en-us/windows/package-manager/winget/`
- 页面标题：Use WinGet to install and manage applications | Microsoft Learn
- 页面描述：The WinGet command line tool enables developers to discover, install, upgrade, remove and configure applications on Windows computers.
- 推荐理由：Windows 新手安装开发工具时，`winget` 是最容易建立“命令式安装”概念的官方入口。
- 适合程度：高
- 难度：入门

### 4.2 Homebrew
- URL: `https://brew.sh/`
- 页面标题：Homebrew — The Missing Package Manager for macOS (or Linux)
- 页面描述：The Missing Package Manager for macOS (or Linux).
- 推荐理由：适合 macOS 学员建立统一安装习惯。
- 适合程度：高
- 难度：入门

### 4.3 apt manpage
- URL: `https://manpages.ubuntu.com/manpages/jammy/en/man8/apt.8.html`
- 页面标题：Ubuntu Manpage: apt - command-line interface
- 推荐理由：适合作为 Linux 学员理解系统包管理器的权威参考，但对纯新手偏硬，建议教师先做二次讲解。
- 适合程度：中
- 难度：初级

### 4.4 Installing Python Modules
- URL: `https://docs.python.org/3/installing/index.html`
- 页面标题：Installing Python Modules — Python 3.14.3 documentation
- 页面描述：As a popular open source development project, Python has an active supporting community...
- 推荐理由：适合解释 `pip` 装的是 Python 包，不是系统软件。
- 适合程度：高
- 难度：初级

## 5. 环境配置

### 5.1 venv — Creation of virtual environments
- URL: `https://docs.python.org/3/library/venv.html`
- 页面标题：venv — Creation of virtual environments — Python 3.14.3 documentation
- 页面描述：The venv module supports creating lightweight “virtual environments”...
- 推荐理由：零基础阶段最值得学的环境概念就是虚拟环境；能显著减少“装坏全局环境”的挫败感。
- 适合程度：高
- 难度：初级

### 5.2 CLI Installation | Cursor Docs
- URL: `https://cursor.com/docs/cli/installation`
- 推荐理由：适合顺带讲解 PATH、命令找不到、安装后验证等典型问题。
- 适合程度：高
- 难度：入门

## 6. 基本调试方法

建议给零基础学员固定 5 步法：

1. **先复现**：确认错误稳定出现
2. **读完整报错**：先看最后一行，再看 traceback / 文件名 / 行号
3. **最小化问题**：删掉无关代码，只保留能复现的最小示例
4. **双轨调试**：先 `print` / 日志，再用断点调试器
5. **修完再回归**：重新运行，确认没有引入新错误

### 对应资料

- VS Code Python debugging: `https://code.visualstudio.com/docs/python/debugging`
- Cursor Debug Mode: `https://cursor.com/docs/agent/debug-mode`
- Cursor Debugging: `https://cursor.com/for/debugging`

## 7. VibeCoding 入门实践建议

> 本文中的“VibeCoding”是课程内部使用的教学标签，指“借助 AI 进行快速迭代式编程，但每一步都要人工验证结果”的入门实践方式。

### 7.1 适合零基础的 VibeCoding 原则

1. **AI 先给脚手架，人来验证运行结果**
2. **一次只改一个点**，不要让 AI 一口气重写整个项目
3. **永远要求可运行结果**：文件、命令、预期输出、下一步验证
4. **优先做小项目**：计算器、待办清单、命令行记账、天气脚本
5. **把 Rules 当作护栏**：例如“回答时先解释再改代码”“任何改动都要给运行命令”
6. **把终端输出当事实来源**，不要把 AI 口头描述当事实

### 7.2 最适合入门的练习模板

#### 模板 A：Hello World 到小功能
- 让 Cursor 生成一个最小 Python 脚本
- 人工在 VS Code / 终端中运行
- 如果报错，让 Cursor 解释报错含义并提出最小修复
- 修完后再次运行

#### 模板 B：有规则的 AI 协作
- 在项目中写一份简短规则文件，约束 AI：
  - 先解释目标
  - 每次只改一个文件
  - 给出运行命令
  - 如果不确定就说明假设
- 然后让 Cursor 帮做一个小功能
- 教学重点：让学员看到“约束 AI 会明显提升结果质量”

#### 模板 C：调试驱动学习
- 故意给一个带 bug 的小程序
- 先人工阅读报错
- 再让 Cursor 用 Debug Mode 思路给出假设
- 最后用 VS Code 断点验证

### 7.3 初学者常见误区

1. **把 AI 当作“保证正确”的老师**
2. **不运行代码，只看回答就以为完成**
3. **同时改太多文件，出了问题找不到原因**
4. **不会区分系统包、Python 包、虚拟环境**
5. **命令能复制，但不知道自己当前在哪个目录**
6. **不会保存证据**：不知道应该记录命令、输出、报错截图

## 课程落地建议

## 推荐拆成 5 个教学单元

### 单元 1：认识编辑器与终端
- 主资料：VS Code Getting Started、Terminal Basics、Ubuntu command line for beginners
- 目标：学员能打开项目文件夹、打开终端、切换目录、运行简单命令

### 单元 2：安装与环境配置
- 主资料：WinGet / Homebrew / apt / Python installing / venv / Cursor CLI Installation
- 目标：学员能独立安装软件，并理解“系统环境”和“项目环境”不同

### 单元 3：Cursor 入门
- 主资料：Cursor Docs、Agents、Rules、Terminal
- 目标：学员知道什么时候用 Chat，什么时候让 Agent 执行，什么时候要加规则

### 单元 4：基本调试
- 主资料：VS Code Python debugging、Cursor Debug Mode、Debugging with Cursor
- 目标：学员会看报错、打断点、最小化复现

### 单元 5：VibeCoding 小项目
- 主资料：Developing Features、Customizing Agents
- 目标：学员完成一个 1~2 文件的小项目，并提交“需求 → AI 协作 → 运行验证 → 修 bug”全过程记录

## 对《零基础计划》编排的直接建议

1. **先讲 VS Code，再讲 Cursor。** 因为 Cursor 的体验建立在编辑器和终端基础之上。
2. **终端必须跟“当前目录”一起讲。** 这是零基础最常见的根因问题。
3. **包管理必须分层讲。** 系统安装器、Python 包、虚拟环境三者不要混讲。
4. **调试要早讲。** 不要等学员连续报错后才补课。
5. **VibeCoding 一定要和验证绑定。** 每次 AI 协作都要求：运行命令、预期输出、实际输出、下一步。

## 建议纳入课程的最小资料包

如果每个主题只留一份主资料，建议保留：

1. VS Code Getting Started  
   `https://code.visualstudio.com/docs/getstarted/getting-started`
2. VS Code Terminal Basics  
   `https://code.visualstudio.com/docs/terminal/basics`
3. VS Code Python Tutorial  
   `https://code.visualstudio.com/docs/python/python-tutorial`
4. VS Code Python Debugging  
   `https://code.visualstudio.com/docs/python/debugging`
5. Cursor Docs  
   `https://cursor.com/docs`
6. Cursor Learn: Developing Features  
   `https://cursor.com/learn/creating-features`
7. Cursor Docs: Rules  
   `https://cursor.com/docs/rules`
8. Cursor Docs: Terminal  
   `https://cursor.com/docs/agent/tools/terminal`
9. Python venv  
   `https://docs.python.org/3/library/venv.html`
10. Ubuntu command line for beginners  
   `https://ubuntu.com/tutorials/command-line-for-beginners`

## Provenance

本文件中的标题、页面描述、可访问性检查来自以下命令与抓取：

- `python3 - <<'PY' ... urllib.request.urlopen(...) ... PY` 对以下页面进行状态检查与标题/描述抽取：
  - `https://cursor.com/docs`
  - `https://code.visualstudio.com/docs/getstarted/getting-started`
  - `https://code.visualstudio.com/docs/python/debugging`
  - `https://learn.microsoft.com/en-us/windows/package-manager/winget/`
  - `https://brew.sh/`
  - `https://docs.python.org/3/installing/index.html`
  - `https://docs.python.org/3/library/venv.html`
  - `https://ubuntu.com/tutorials/command-line-for-beginners`
  - `https://manpages.ubuntu.com/manpages/jammy/en/man8/apt.8.html`
- `curl -L --max-time 20 -s https://cursor.com/docs | head -n 80`
- `python3 - <<'PY' ... re.findall('"filePath":"([^"]+)"', html) ... PY` 从 Cursor Docs 首页提取内部文档路径，用于定位：
  - `/learn/agents`
  - `/learn/creating-features`
  - `/learn/customizing-agents`
  - `/for/debugging`
  - `/docs/rules`
  - `/docs/agent/tools/terminal`
  - `/docs/agent/debug-mode`
  - `/docs/cli/installation`

## Open questions

1. 是否要为 Windows / macOS / Linux 分别做 3 套安装截图版教程？
2. 是否在 28 天课程中统一使用 VS Code，还是允许 Cursor 作为第 2 周升级路线？
3. 是否需要额外补充中文视频教程，以降低纯英文官方文档门槛？
