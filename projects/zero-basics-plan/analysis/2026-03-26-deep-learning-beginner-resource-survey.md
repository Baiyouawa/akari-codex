# 基础深度学习入门资料调研笔记

- 项目：`projects/zero-basics-plan`
- 任务：调研基础深度学习入门资料：覆盖 Python 科学计算、NumPy、PyTorch 基础、张量、自动求导、简单神经网络、训练与推理概念，保证零基础可理解
- 日期：2026-03-26
- 产出人：Fleet Worker `侑-00-1774524982-beb96f`
- 面向对象：完全零基础，希望在 28 天课程中建立 Python 科学计算、NumPy、PyTorch、张量、自动求导、简单神经网络、训练与推理最小心智模型的学习者

## 调研目标

按任务要求，本调研覆盖以下主题，并强调“零基础可理解”：

1. Python 科学计算
2. NumPy 基础
3. PyTorch 基础
4. 张量
5. 自动求导
6. 简单神经网络
7. 训练与推理概念

同时需要与项目内既有 Week 3 Python 基础、Week 4 课程框架保持衔接，避免深度学习部分脱离前置能力独立漂浮。

## 结论摘要

1. **最适合零基础的主线顺序是：Python 基础语法 → NumPy 数组 → PyTorch 张量 → 自动求导 → `nn.Module` 神经网络 → 训练 / 推理。**
   - 原因：NumPy 官方把 `ndarray` 作为数值计算核心对象；PyTorch 的初学者路径则默认学习者已经接受“多维数组 / shape / 运算”这套心智模型。
   - 来源：
     - NumPy Absolute Beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
     - PyTorch Learn the Basics: https://docs.pytorch.org/tutorials/beginner/basics/intro.html
     - PyTorch Tensor Tutorial: https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html

2. **NumPy 应承担“科学计算启蒙层”，不应让初学者一上来直接跳到深度学习框架。**
   - NumPy 官方说明其是 science and engineering 中广泛使用的开源 Python 库，核心是多维数组和围绕数组的高效运算；这正适合解释“为什么不用纯 Python 列表做数值计算”。
   - 来源：
     - https://numpy.org/doc/stable/user/absolute_beginners.html
     - https://numpy.org/learn/

3. **PyTorch 官方初学材料天然适合放在 28 天课程后段。**
   - `Learn the Basics` 已将主题切成 Quickstart、Tensors、Datasets & DataLoaders、Build the Neural Network、Autograd、Optimization、Save & Load Model、Inference 等模块，适合逐日拆分。
   - 来源：https://docs.pytorch.org/tutorials/beginner/basics/intro.html

4. **“张量”最好先讲成“带形状的多维数字表”，不要先讲抽象数学定义。**
   - PyTorch Tensor Tutorial 面向初学者展示创建张量、shape、datatype、device、索引、拼接、矩阵乘法、reshape 等操作；零基础课程更需要可操作直觉，而不是一开始进入严谨线代定义。
   - 来源：https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html

5. **自动求导不应从公式推导开始，而应从“参数改一点，损失怎么变”开始。**
   - `A Gentle Introduction to torch.autograd` 围绕 computation graph、gradient、`requires_grad` 展开，更适合把反向传播解释成“系统自动记录依赖并计算梯度”。
   - 来源：https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html

6. **简单神经网络最好先讲结构与数据流，再讲优化器细节。**
   - `Neural Networks` 教程用 `nn.Module`、层、前向传播和损失函数来说明“输入如何一层层变成输出”；对零基础来说，先理解“层”和“前向计算”比先背优化器参数更重要。
   - 来源：https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html

7. **训练与推理必须明确分开讲。**
   - PyTorch 的 Quickstart、Learn the Basics、Start Locally 页面共同形成一个清晰闭环：先安装与验证，再训练，再保存 / 加载，再推理。这说明“训练模型”和“拿模型做预测”是不同阶段。
   - 来源：
     - https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
     - https://docs.pytorch.org/tutorials/beginner/basics/intro.html
     - https://docs.pytorch.org/get-started/locally/

8. **零基础课程默认应采用 CPU 路线，而不是把 GPU / CUDA 当成前置条件。**
   - PyTorch Start Locally 页面明确提供 CPU 安装选项，且示例验证只要求构造一个随机张量；这说明 CPU 安装是标准支持路径之一。
   - 来源：https://docs.pytorch.org/get-started/locally/

9. **Week 4 的深度学习部分应该围绕 `shape` 组织，而不是围绕库函数名组织。**
   - 从 NumPy `array.shape` 到 Tensor `shape`，再到模型输入 / 输出 shape，这条主线最能降低初学者“看得懂代码但不知道数据在流什么”的风险。
   - 来源：
     - https://numpy.org/doc/stable/user/absolute_beginners.html
     - https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html
     - https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html

## 面向零基础的教学原则

### 1. 先讲“为什么”，再讲 API

零基础学习者最容易迷失在 `tensor`、`autograd`、`optimizer` 这些名词里。课程编排应先回答：

- 为什么科学计算常用数组，而不是列表？
- 为什么深度学习库喜欢“张量”这种数据结构？
- 为什么训练模型需要“自动求导”？
- 为什么训练和推理不是一回事？

### 2. 每个主题只保留一个最小动作

建议每节课只要求一个可运行动作：

- NumPy：创建数组并查看 `shape`
- Tensor：创建张量并做一次矩阵乘法
- Autograd：对一个简单表达式求梯度
- Neural Network：跑通一个最小网络的前向传播
- Training：看懂一次 loss 下降
- Inference：输入新样本并得到预测结果

### 3. 不从线性代数证明开始

本任务要求“零基础可理解”，因此第一阶段不要把重点放在矩阵求导公式、链式法则推导、卷积数学定义上，而应先建立：

- 数据有形状
- 模型有参数
- 预测会出错
- 梯度告诉我们该往哪个方向改参数
- 训练是反复改参数
- 推理是拿训练好的参数去预测

### 4. 用“可见输出”帮助理解

对每个概念，都应该让学习者看到一个输出：

- `array.shape`
- `tensor.shape`
- `grad`
- `loss`
- `predicted class`

这样比只读概念说明更容易建立直觉。

### 5. 深度学习部分必须建立在 Python 前置能力之上

根据项目内既有 Python 调研，后续深度学习学习至少要求学习者已经会：

- 在终端运行 `.py` 文件
- 使用 `venv` 和 `pip`
- 看懂变量、函数、列表和字典
- 使用 `import`

来源：`projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`

## 推荐资料清单

## 1. Python 科学计算总入口

### 1.1 Scientific Python Lectures — NumPy: creating and manipulating numerical data
- 链接：https://lectures.scientific-python.org/intro/numpy/index.html
- 类型：科学 Python 体系中的 NumPy 章节
- 适合程度：中高
- 难度：入门到初级
- 推荐理由：把 NumPy 放进更大的 scientific Python 生态里，适合课程编写者理解“为什么 NumPy 是科学计算基础层”。
- 适合用法：教师备课参考；不一定要求学生全文精读。

### 1.2 SciPy Lecture Notes — NumPy: creating and manipulating numerical data
- 链接：https://scipy-lectures.org/intro/numpy/index.html
- 类型：NumPy 系统讲义
- 适合程度：中高
- 难度：初级
- 推荐理由：结构完整，覆盖数组对象、索引切片、数值运算、broadcasting、shape manipulation、exercises。
- 适合用法：作为 NumPy 章节的扩展练习池。

## 2. NumPy 入门

### 2.1 NumPy: the absolute basics for beginners
- 链接：https://numpy.org/doc/stable/user/absolute_beginners.html
- 类型：官方入门教程
- 适合程度：高
- 难度：入门
- 推荐理由：标题就明确面向 absolute beginners；内容从 `import numpy as np`、数组、shape、索引和基础运算开始，语言非常适合第一次接触数值计算的人。
- 可承担主题：
  - 什么是 NumPy
  - 为什么 NumPy 适合处理 homogeneous data
  - 数组与列表区别
  - 创建数组、读取形状、基础运算

### 2.2 NumPy Learn 页面
- 链接：https://numpy.org/learn/
- 类型：官方学习资源导航
- 适合程度：高
- 难度：入门
- 推荐理由：NumPy 官方把 `NumPy Quickstart Tutorial`、`Scientific Python Lectures`、`NumPy: the absolute basics for beginners` 等 beginner 资源集中列出，可作为后续课程资源审查时的“源头导航页”。
- 课程用途：帮助筛选延伸阅读，而不是直接当讲义。

## 3. PyTorch 总入口与安装

### 3.1 Learn the Basics — PyTorch Tutorials
- 链接：https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- 类型：官方初学者路线
- 适合程度：高
- 难度：入门到初级
- 推荐理由：主题切分天然适合课程拆分，包括 Quickstart、Tensors、Autograd、Build Model、Optimization、Save/Load、Inference。
- 课程用途：Week 4 的主线教材。

### 3.2 Quickstart — PyTorch Tutorials
- 链接：https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
- 类型：快速开始
- 适合程度：高
- 难度：入门
- 推荐理由：适合让学习者尽快获得“我真的把 PyTorch 跑起来了”的正反馈。
- 课程用途：Day 26 训练 / 推理闭环的主要示例来源。

### 3.3 Start Locally — PyTorch
- 链接：https://docs.pytorch.org/get-started/locally/
- 类型：官方安装页
- 适合程度：高
- 难度：入门
- 推荐理由：提供安装命令与验证样例，并明确说明 Python 3.9+ 前提和 CPU 路线的安装方式。
- 课程用途：环境配置与安装核验。

### 3.4 Deep Learning with PyTorch: A 60 Minute Blitz
- 链接：https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- 类型：官方入门总览
- 适合程度：中高
- 难度：入门到初级
- 推荐理由：比单篇 Quickstart 更系统，能帮助课程设计者看到 Tensor、Autograd、Neural Networks、Training a Classifier 之间的关系。
- 课程用途：教师统筹 Week 4 结构时的总导航。

## 4. 张量入门

### 4.1 Tensors — PyTorch Tutorials
- 链接：https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html
- 类型：官方张量教程
- 适合程度：高
- 难度：入门到初级
- 推荐理由：直接覆盖创建张量、属性、运算、索引、拼接、矩阵乘法、in-place 操作等初学者最常用内容。
- 课程用途：
  - 解释 tensor 是什么
  - 对比 NumPy array 和 tensor
  - 引入 shape、dtype、device

## 5. 自动求导入门

### 5.1 A Gentle Introduction to torch.autograd
- 链接：https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html
- 类型：官方自动求导教程
- 适合程度：高
- 难度：初级
- 推荐理由：名字本身就强调 gentle introduction，适合首次解释 computation graph、gradient、`requires_grad`。
- 课程用途：
  - 解释梯度是什么
  - 说明 PyTorch 如何自动记录运算
  - 帮助学习者建立“优化参数”的直觉

## 6. 简单神经网络

### 6.1 Neural Networks — PyTorch Tutorials
- 链接：https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
- 类型：官方网络教程
- 适合程度：高
- 难度：初级
- 推荐理由：展示如何定义网络、进行前向传播、计算损失、查看参数梯度；很适合当“第一个神经网络”材料。
- 课程用途：
  - 解释层与参数
  - 解释前向传播
  - 把 autograd 与 loss 连接起来

## 7. 训练与推理

### 7.1 Quickstart 中的训练 / 测试 / 推理流程
- 链接：https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
- 类型：快速闭环教程
- 适合程度：高
- 难度：入门到初级
- 推荐理由：相较 CIFAR10 教程更短，更适合零基础先跑通“训练一个模型，再拿它预测”的闭环。
- 课程用途：优先作为学生主线实验。

### 7.2 Training a Classifier — PyTorch Tutorials
- 链接：https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
- 类型：官方训练示例
- 适合程度：中高
- 难度：初级到中级
- 推荐理由：虽然篇幅更长，但它把数据加载、网络、损失函数、优化器、训练循环、测试预测串成完整闭环，是理解“训练 vs 推理”的关键实例。
- 课程用途：教师裁剪后可作为综合 demo 来源，不建议完全原样丢给零基础学生。

## 按任务要求映射资料

| 任务要求 | 推荐主资料 | 补充资料 | 课程落点 |
|---|---|---|---|
| Python 科学计算 | NumPy Absolute Beginners | Scientific Python Lectures / SciPy Lecture Notes | Day 22 |
| NumPy 基础 | NumPy Absolute Beginners | NumPy Learn | Day 22 |
| PyTorch 基础 | PyTorch Learn the Basics / Start Locally | 60 Minute Blitz | Day 23 |
| 张量 | Tensor Tutorial | NumPy Absolute Beginners（数组类比） | Day 23 |
| 自动求导 | Autograd Tutorial | Learn the Basics | Day 24 |
| 简单神经网络 | Neural Networks Tutorial | 60 Minute Blitz | Day 25 |
| 训练与推理概念 | Quickstart Tutorial | CIFAR10 Tutorial | Day 26-27 |

## 零基础课程的主题映射建议

## 1. Python 科学计算

建议讲法：
- Python 是通用编程语言
- NumPy 是 Python 中做数值计算的基础工具
- 深度学习框架不是替代 Python，而是建立在 Python 生态上的专门工具

建议先修要求：
- 会写变量、函数、循环
- 能运行 `.py` 文件
- 会安装 Python 包

推荐资料：
- Python Tutorial: https://docs.python.org/3/tutorial/
- Scientific Python Lectures NumPy 章节: https://lectures.scientific-python.org/intro/numpy/index.html

## 2. NumPy

必须覆盖：
- `np.array`
- shape
- indexing / slicing
- elementwise operations
- reductions（如 `sum` / `mean`）
- reshape

最小练习：
1. 创建一维、二维数组
2. 查看 `.shape`
3. 取出某一行某一列
4. 求平均值
5. 改变数组形状

推荐资料：
- https://numpy.org/doc/stable/user/absolute_beginners.html
- https://scipy-lectures.org/intro/numpy/index.html

## 3. PyTorch 基础

必须覆盖：
- 安装与导入 `torch`
- 创建 tensor
- shape / dtype
- 基础运算
- NumPy 与 tensor 的关系

最小练习：
1. 创建随机张量
2. 查看 shape
3. 做一次矩阵乘法
4. 把一个 NumPy array 转成 tensor

推荐资料：
- https://docs.pytorch.org/get-started/locally/
- https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html

## 4. 张量

零基础解释模板：
- 标量：一个数字
- 向量：一行数字
- 矩阵：二维数字表
- 张量：更一般的多维数字表

注意事项：
- 第一轮不要强调严谨数学定义
- 第一轮只强调“数据有维度和形状”
- 把图片、批量样本、词向量都解释为“有形状的数据”

## 5. 自动求导

零基础解释模板：
- 模型会根据输入算出输出
- 输出和正确答案之间有差距，这个差距叫 loss
- 梯度告诉我们：参数朝哪个方向改，loss 更可能下降
- autograd 负责自动算这些梯度

最小练习：
1. 创建一个 `requires_grad=True` 的张量
2. 构造一个简单函数，例如平方和
3. 调用 `backward()`
4. 打印 `.grad`

推荐资料：
- https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html

## 6. 简单神经网络

建议顺序：
1. 先讲“网络就是很多层可学习函数的组合”
2. 再讲输入层、隐藏层、输出层
3. 再展示 `nn.Module`
4. 最后展示 loss 与 optimizer

最小练习：
1. 定义一个两层网络
2. 给随机输入做 forward
3. 打印输出 shape
4. 看看参数张量长什么样

推荐资料：
- https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html

## 7. 训练与推理概念

建议一定明确区分：

### 训练（training）
- 需要数据和标签
- 会反复前向 + 计算 loss + 反向传播 + 更新参数
- 目标是让模型参数逐步变好

### 推理（inference）
- 用已经训练好的参数
- 不再更新参数
- 目标是对新输入做预测

最小练习：
1. 跑一个短训练循环
2. 记录每轮 loss
3. 用训练好的模型对一个新样本做预测
4. 比较训练阶段和推理阶段代码差别

推荐资料：
- https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
- https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html

## 与 28 天课程框架的对齐建议

项目内既有课程总表已经将 Week 4 预留为 `Day 22` 到 `Day 28`。结合该框架，建议保持 **5 天主线 + 1 天综合实验 + 1 天总复盘**：

### Day 22：Python 科学计算与 NumPy 入门
- 目标：理解为什么需要数组计算
- 练习：创建数组、看 shape、做求和与均值
- 主资料：NumPy Absolute Beginners

### Day 23：NumPy 进阶到 PyTorch Tensor
- 目标：从数组过渡到张量
- 练习：创建 tensor、做矩阵乘法、reshape
- 主资料：Tensor Tutorial

### Day 24：自动求导
- 目标：理解 gradient、loss、`requires_grad`
- 练习：跑最小 autograd 例子
- 主资料：Autograd Tutorial

### Day 25：第一个神经网络
- 目标：认识 `nn.Module`、forward、parameter
- 练习：定义并运行最小网络
- 主资料：Neural Networks Tutorial

### Day 26：训练与推理
- 目标：区分训练循环与预测阶段
- 练习：跑 Quickstart 中的训练与推理片段
- 主资料：Quickstart Tutorial

### Day 27：综合 demo
- 目标：串联数据、模型、训练、预测
- 练习：运行精简版分类 demo，并把结果提交到 GitHub
- 主资料：Quickstart / CIFAR10 Tutorial（教师裁剪版）

### Day 28：结营复盘
- 目标：把 Linux / Git / Python / Cursor / Deep Learning 全链路串起来
- 练习：总结术语、提交作品、说明自己真正理解了什么

对应来源：`projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`

## 适合直接放入课程的练习建议

## 练习组 1：NumPy 数组感觉建立
1. 用 `np.array([1, 2, 3, 4])` 创建一维数组。
2. 用二维数组表示 2 行 3 列数字表。
3. 打印 `.shape`。
4. 计算总和和平均值。
5. 用 `reshape` 改成新形状。

对应来源：
- https://numpy.org/doc/stable/user/absolute_beginners.html

## 练习组 2：Tensor 与 shape
1. 创建 `torch.tensor([[1, 2], [3, 4]])`。
2. 打印 `shape`、`dtype`。
3. 做一次加法。
4. 做一次矩阵乘法。
5. 比较 NumPy array 与 tensor 的相似之处。

对应来源：
- https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html

## 练习组 3：Autograd 最小例子
1. 创建 `requires_grad=True` 的张量。
2. 构造一个简单表达式，例如 `y = x.pow(2).sum()`。
3. 调用 `backward()`。
4. 打印 `x.grad`。
5. 用自己的话说明为什么会出现这个梯度值。

对应来源：
- https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html

## 练习组 4：第一个网络
1. 定义一个最小两层网络。
2. 输入随机张量。
3. 打印输出。
4. 查看网络参数名和参数 shape。
5. 解释“哪部分是模型结构，哪部分是参数”。

对应来源：
- https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html

## 练习组 5：训练 vs 推理
1. 运行一个短训练循环。
2. 记录 3 次以上 loss。
3. 切换到新样本预测。
4. 比较训练阶段和推理阶段的代码差异。
5. 用一句话解释为什么推理阶段不更新参数。

对应来源：
- https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html

## 初学者常见误区

### 1. 把 NumPy 和 PyTorch 当成两个互不相关的东西

更好的讲法：
- NumPy 负责建立数组计算直觉
- PyTorch 在张量、自动求导、神经网络训练上更进一步

### 2. 一上来就追求 GPU / CUDA

对零基础课程，CPU 就够。先建立概念，再考虑硬件加速。
- 依据：PyTorch Start Locally 页面提供 CPU 安装路径，说明这是标准支持路径之一。
- 来源：https://docs.pytorch.org/get-started/locally/

### 3. 只背 API，不理解 shape

很多初学者真正卡住的不是函数名，而是不知道数据的形状怎么流动。课程中必须高频打印：
- `array.shape`
- `tensor.shape`
- 模型输出 shape

### 4. 把 autograd 当成魔法

应该反复强调：
- 它不是“神秘智能”
- 它是在记录运算关系后自动求梯度
- 目的是让参数更新更高效

### 5. 训练和推理混在一起

必须明确：
- 训练会更新参数
- 推理不会更新参数
- 两者代码结构、目标和成本都不同

### 6. 在没有 Python 前置能力时硬上 PyTorch

如果学习者连 `import`、函数、列表、命令行运行都不熟练，深度学习教程会迅速变成纯复制粘贴。课程中必须把 Python 基础与深度学习前置关系说清楚。

## 课程编写时的直接建议

1. **Week 4 不要再引入太多新工具。** 重点应放在概念建立与最小可运行 demo。
2. **每节课都要有“看得见的数字输出”。** 深度学习初学阶段最怕抽象漂浮。
3. **优先官方材料，辅以教师二次解释。** 这样证据链最清晰。
4. **训练 demo 必须做裁剪。** CIFAR10 官方教程适合作为教师参考，不适合完全原样丢给零基础学习者。
5. **把 shape 作为全周主线。** 从 NumPy 到 tensor 再到 network output，都围绕 shape 解释。
6. **默认 CPU 安装与验证。** 降低环境复杂度，避免显卡驱动问题吞掉学习热情。

## 最小资料包建议

如果只保留最核心的 8 份资料，建议是：

1. Python Tutorial  
   https://docs.python.org/3/tutorial/
2. NumPy Absolute Beginners  
   https://numpy.org/doc/stable/user/absolute_beginners.html
3. NumPy Learn  
   https://numpy.org/learn/
4. PyTorch Learn the Basics  
   https://docs.pytorch.org/tutorials/beginner/basics/intro.html
5. PyTorch Start Locally  
   https://docs.pytorch.org/get-started/locally/
6. PyTorch Tensor Tutorial  
   https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html
7. PyTorch Autograd Tutorial  
   https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html
8. PyTorch Neural Networks / Quickstart  
   https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html  
   https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html

## Provenance

本文件的结论和链接来自本次会话实际检索与抓取：

- `web_search`: `official beginner deep learning PyTorch NumPy tensor autograd tutorial zero basics`
- `web_fetch`: `https://numpy.org/doc/stable/user/absolute_beginners.html`
- `web_fetch`: `https://numpy.org/learn/`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/basics/intro.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/get-started/locally/`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html`
- `web_fetch`: `https://scipy-lectures.org/intro/numpy/index.html`
- `web_fetch`: `https://lectures.scientific-python.org/intro/numpy/index.html`
- `read_file`: `projects/zero-basics-plan/analysis/2026-03-26-python-programming-basics-research.md`
- `read_file`: `projects/zero-basics-plan/analysis/2026-03-26-28-day-course-framework.md`

## Open questions

1. Week 4 是否明确要求统一采用 CPU 安装路线，避免 Windows + CUDA 环境配置把课程拖复杂？
2. 是否需要额外补一份“张量 / 梯度 / loss / epoch / batch”中文术语卡，降低第一次接触英文官方文档的门槛？
3. Day 27 的综合 demo 是否要统一为同一个最小分类任务，以便所有学习者更容易互相对照结果？
