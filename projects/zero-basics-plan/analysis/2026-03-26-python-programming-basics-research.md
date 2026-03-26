# Python 与编程基础资料调研

- 项目：`projects/zero-basics-plan`
- 任务：调研 Python 与编程基础资料：覆盖语法、数据结构、函数、模块、文件读写、虚拟环境，为后续 AI / 深度学习学习做铺垫
- 产出人：Fleet Worker `智乃-02-1774524441-80ede7`
- 日期：2026-03-26

## 调研目标

为《零基础计划》第 3 周的 Python 学习段筛选适合初学者的资料，要求覆盖：

1. 语法基础
2. 数据结构
3. 函数
4. 模块
5. 文件读写
6. 虚拟环境
7. 面向 28 天课程的课程映射与练习建议

## 结论摘要

1. **主线资料应以 Python 官方教程为骨架**，因为它系统覆盖了语法、控制流、函数、数据结构、模块、文件读写、虚拟环境等主题。
2. **但 Python 官方教程明确说明它“面向刚接触 Python 的程序员，而不是完全没有编程基础的新手”**，因此若课程对象真的是“零基础”，必须补充更平缓的入门材料。来源：`https://docs.python.org/3/tutorial/index.html`。
3. **最适合的补充材料是 PY4E（Python for Everybody）**，因为其课程首页直接写明“even if you have no programming background”，并按变量、条件、函数、循环、字符串、文件、列表、字典逐步展开。来源：`https://www.py4e.com/lessons`。
4. **练习材料可优先采用 Google's Python Class Basic Exercises**，其官方页面明确提供 `string1.py`、`list1.py`、`wordcount.py` 三类基础练习，正好对应字符串、列表、字典/文件读写。来源：`https://developers.google.com/edu/python/exercises/basic`。
5. **若需要更完整的视频化课程，可把 CS50P 作为扩展路线**，因为课程首页明确覆盖 functions、variables、conditionals、loops、exceptions、libraries、file I/O、unit tests，并说明适合“with or without prior programming experience”。来源：`https://cs50.harvard.edu/python/`。
6. **虚拟环境部分应坚持官方 `venv` 路线**，因为 Python 官方教程已直接给出创建、激活、用 `pip` 管理包的最小路径。来源：`https://docs.python.org/3/tutorial/venv.html`。

## 推荐资料清单

## 1. Python 官方教程（主线骨架）

### 1.1 The Python Tutorial
- URL: `https://docs.python.org/3/tutorial/index.html`
- 适合内容：课程总导航、整体知识图谱
- 关键发现：官方教程说明它适合“new to the Python language”，但不是“beginners who are new to programming”。
- 推荐理由：覆盖面完整，适合作为课程主干与查漏补缺的权威来源。
- 难度：入门到初级
- 使用建议：作为教师编排课程的核心索引，而不是直接让零基础学生从头硬啃全文。

### 1.2 An Informal Introduction to Python
- URL: `https://docs.python.org/3/tutorial/introduction.html`
- 适合内容：解释器、数字、字符串、列表、注释、第一批语法感知
- 推荐理由：适合 Day 15 的“第一个 Python 程序 + 解释器体验”。
- 难度：入门

### 1.3 More Control Flow Tools
- URL: `https://docs.python.org/3/tutorial/controlflow.html`
- 适合内容：`if`、`for`、`range()`、`break`、`continue`、函数定义、默认参数、关键字参数、lambda、文档字符串
- 推荐理由：语法基础与函数内容基本都在这一章，适合 Day 16~17。
- 难度：入门到初级

### 1.4 Data Structures
- URL: `https://docs.python.org/3/tutorial/datastructures.html`
- 适合内容：列表、元组、集合、字典、推导式、序列比较
- 推荐理由：数据结构讲解集中，能直接支撑列表/字典练习。
- 难度：初级

### 1.5 Modules
- URL: `https://docs.python.org/3/tutorial/modules.html`
- 适合内容：模块、`import`、模块搜索路径、包
- 推荐理由：非常适合讲“把代码拆到多个 `.py` 文件中”的最小工程化概念。
- 难度：初级

### 1.6 Input and Output
- URL: `https://docs.python.org/3/tutorial/inputoutput.html`
- 适合内容：`print()`、格式化输出、读取与写入文件、`json`
- 推荐理由：直接覆盖文件读写与输出格式，是第 18 天的核心资料。
- 难度：初级

### 1.7 Virtual Environments and Packages
- URL: `https://docs.python.org/3/tutorial/venv.html`
- 适合内容：为什么需要虚拟环境、`python -m venv .venv`、激活、`pip` 管理包
- 推荐理由：足够支撑零基础阶段的环境隔离需求，不需要一开始引入更复杂工具。
- 难度：初级

## 2. 面向“完全零基础”的补充资料

### 2.1 Python for Everybody (PY4E)
- URL: `https://www.py4e.com/lessons`
- 覆盖内容：Installing Python、Why Program、Variables、Conditional Execution、Functions、Loops、Strings、Files、Lists、Dictionaries、Tuples
- 推荐理由：课程页面直接声明适合没有编程背景的人，且章节顺序天然贴合初学者认知曲线。
- 难度：零基础到入门
- 最适合用途：作为学生的主读材料或配套视频课。

### 2.2 CS50’s Introduction to Programming with Python
- URL: `https://cs50.harvard.edu/python/`
- 覆盖内容：Functions、Variables、Conditionals、Loops、Exceptions、Libraries、Unit Tests、File I/O、Regular Expressions、OOP
- 推荐理由：适合作为扩展学习路径；内容更完整，也更强调调试与测试。
- 难度：入门到初级
- 最适合用途：课程后半段扩展、优等生加餐、教师备课参考。

## 3. 练习资料

### 3.1 Google’s Python Class — Basic Python Exercises
- URL: `https://developers.google.com/edu/python/exercises/basic`
- 覆盖内容：`string1.py`、`list1.py`、`wordcount.py`
- 推荐理由：官方练习结构清晰，且 `wordcount.py` 同时涉及字符串、字典、文件，适合 Week 3 后半段练手。
- 难度：入门到初级

## 按任务要求映射资料

| 任务要求 | 推荐主资料 | 补充资料 | 课程落点 |
|---|---|---|---|
| 语法基础 | Python Tutorial: Introduction / Control Flow | PY4E Variables / Conditionals / Loops | Day 15-16 |
| 数据结构 | Python Tutorial: Data Structures | PY4E Lists / Dictionaries / Tuples | Day 17 |
| 函数 | Python Tutorial: Control Flow → Defining Functions | PY4E Functions / CS50P Functions | Day 17 |
| 模块 | Python Tutorial: Modules | CS50P Libraries | Day 18 |
| 文件读写 | Python Tutorial: Input and Output | PY4E Files / Google `wordcount.py` | Day 18 |
| 虚拟环境 | Python Tutorial: Virtual Environments and Packages | VS Code Python Tutorial（来自既有工具链调研） | Day 15 / Day 18 |

## 适合零基础课程的教学顺序

### 推荐顺序

1. 先认识 Python 解释器、脚本与 `print()`
2. 再学变量、输入输出、条件、循环
3. 然后过渡到列表、字典、函数
4. 接着讲模块与“把代码拆分到文件里”
5. 再讲文件读写
6. 最后补虚拟环境与 `pip`

### 不推荐顺序

- 一上来讲类、装饰器、生成器、复杂异常体系
- 一上来把 `pip`、包、模块、解释器、虚拟环境混成一团
- 一开始就让学生在没有理解变量/列表前直接做 AI / 深度学习代码

## 面向《零基础计划》的 4 天 Python 基础拆分建议

结合现有 `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md` 中的 Week 3 结构，可把 Python 基础进一步细化为：

### Day 15 — Python 环境与第一段程序
- 目标：知道 Python 解释器、`.py` 文件、`print()`、运行脚本
- 主资料：
  - `https://docs.python.org/3/tutorial/index.html`
  - `https://docs.python.org/3/tutorial/introduction.html`
  - `https://www.py4e.com/lessons`
- 练习：
  - 写 `hello.py`
  - 在终端中运行 `python hello.py`
  - 修改输出 3 次，确认自己真的会运行脚本

### Day 16 — 变量、条件与循环
- 目标：能写简单交互程序
- 主资料：
  - `https://docs.python.org/3/tutorial/controlflow.html`
  - `https://www.py4e.com/lessons`
- 练习：
  - 分数等级判断器
  - 1~100 求和
  - 猜数字游戏（可选）

### Day 17 — 列表、字典与函数
- 目标：理解“把多个数据放在一起”和“把重复逻辑封装起来”
- 主资料：
  - `https://docs.python.org/3/tutorial/datastructures.html`
  - `https://docs.python.org/3/tutorial/controlflow.html`
  - `https://developers.google.com/edu/python/exercises/basic`
- 练习：
  - 待办事项列表
  - 通讯录字典
  - 把重复代码改造成函数

### Day 18 — 模块、文件读写、虚拟环境
- 目标：理解小项目的基本结构
- 主资料：
  - `https://docs.python.org/3/tutorial/modules.html`
  - `https://docs.python.org/3/tutorial/inputoutput.html`
  - `https://docs.python.org/3/tutorial/venv.html`
  - `https://developers.google.com/edu/python/exercises/basic`
- 练习：
  - 把任务列表写入文本文件再读出来
  - 建立 `.venv`
  - 用 `pip` 安装 1 个简单包并记录 `pip list`

## 适合直接纳入课程的练习建议

## 练习组 1：解释器与脚本
1. 在终端输入 `python` 或 `python3` 进入解释器。
2. 试算 `2 + 2`、`10 / 3`、`10 // 3`。
3. 保存为 `hello.py` 后再从终端运行。

对应来源：
- `https://docs.python.org/3/tutorial/introduction.html`

## 练习组 2：条件与循环
1. 输入一个整数，判断它是正数、负数还是零。
2. 用 `for` 循环打印 1 到 10。
3. 用 `while` 做一个最多尝试 3 次的密码模拟。

对应来源：
- `https://docs.python.org/3/tutorial/controlflow.html`
- `https://www.py4e.com/lessons`

## 练习组 3：列表与字典
1. 建一个购物清单列表。
2. 用字典保存 3 个同学的名字和分数。
3. 统计一句话中每个单词出现的次数。

对应来源：
- `https://docs.python.org/3/tutorial/datastructures.html`
- `https://developers.google.com/edu/python/exercises/basic`

## 练习组 4：函数与模块
1. 写 `add(a, b)`、`max_of_three(a, b, c)`。
2. 把函数放进 `utils.py`，在 `main.py` 中导入使用。
3. 解释 `import module` 和 `from module import name` 的差别。

对应来源：
- `https://docs.python.org/3/tutorial/controlflow.html`
- `https://docs.python.org/3/tutorial/modules.html`

## 练习组 5：文件读写与虚拟环境
1. 把 5 行待办事项写入 `tasks.txt`。
2. 从文件里读取后逐行打印。
3. 在项目目录执行 `python -m venv .venv`，并记录激活命令。

对应来源：
- `https://docs.python.org/3/tutorial/inputoutput.html`
- `https://docs.python.org/3/tutorial/venv.html`

## 初学者常见误区

1. **把会复制代码误当成会编程。** 必须要求“自己运行、自己改一处、自己解释输出”。
2. **把列表、字典、模块、包混为一谈。** 课程中应明确“数据结构”和“代码组织”是两层概念。
3. **只在编辑器里写，不会在终端运行。** 这会直接影响后续 Git、虚拟环境、深度学习环境配置。
4. **不理解报错要看最后一行和 traceback。** 这会让 AI / Cursor 阶段的调试能力非常薄弱。
5. **虚拟环境讲得太晚。** 如果在安装第三方包前不讲 `.venv`，容易污染全局环境。

## 对后续 AI / 深度学习学习的铺垫价值

Python 基础阶段至少要让学生真正掌握以下能力，后续 AI / 深度学习才不会被卡死：

1. 会在终端运行 `.py` 文件
2. 会读懂变量、条件、循环
3. 会使用列表和字典保存数据
4. 会把代码拆到不同文件并 `import`
5. 会读写本地文本文件
6. 会建立 `.venv` 并用 `pip` 安装包

这些能力正好对应后续 NumPy / PyTorch 的前置门槛：
- NumPy 需要列表、切片、变量概念
- PyTorch 需要函数调用、模块导入、环境配置
- 跑深度学习 demo 需要文件组织、命令行运行、包安装

## 最小资料包建议

如果课程正文只保留 6 份主资料，建议保留：

1. Python Tutorial 总入口  
   `https://docs.python.org/3/tutorial/index.html`
2. Python Tutorial: Control Flow  
   `https://docs.python.org/3/tutorial/controlflow.html`
3. Python Tutorial: Data Structures  
   `https://docs.python.org/3/tutorial/datastructures.html`
4. Python Tutorial: Modules  
   `https://docs.python.org/3/tutorial/modules.html`
5. Python Tutorial: Input and Output  
   `https://docs.python.org/3/tutorial/inputoutput.html`
6. Python Tutorial: Virtual Environments and Packages  
   `https://docs.python.org/3/tutorial/venv.html`

若允许补充 3 份零基础友好材料，则加上：

7. PY4E Lessons  
   `https://www.py4e.com/lessons`
8. Google Basic Python Exercises  
   `https://developers.google.com/edu/python/exercises/basic`
9. CS50P  
   `https://cs50.harvard.edu/python/`

## Provenance

本文件结论来自本次会话内对以下页面的检索与抓取：

- `https://docs.python.org/3/tutorial/index.html`
- `https://docs.python.org/3/tutorial/introduction.html`
- `https://docs.python.org/3/tutorial/controlflow.html`
- `https://docs.python.org/3/tutorial/datastructures.html`
- `https://docs.python.org/3/tutorial/modules.html`
- `https://docs.python.org/3/tutorial/inputoutput.html`
- `https://docs.python.org/3/tutorial/venv.html`
- `https://www.py4e.com/lessons`
- `https://developers.google.com/edu/python/exercises/basic`
- `https://cs50.harvard.edu/python/`

以及项目内既有材料：
- `projects/zero-basics-plan/analysis/dev-toolchain-beginner-research.md`
- `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`

## Open questions

1. 是否需要额外补一份“完全不懂编程的人如何理解变量 / 函数 / 数据结构”的中文类比讲义？
2. 第 3 周是否统一要求先用 VS Code 完成 Python 基础，再切到 Cursor 做 AI 辅助编码？
3. 虚拟环境是否要分 Windows PowerShell / macOS / Linux 三套激活命令分别展示？
