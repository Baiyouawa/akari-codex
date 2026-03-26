# 基础深度学习入门资料调研笔记

- 项目：`projects/zero-basics-plan`
- 任务：调研基础深度学习入门资料
- 日期：2026-03-26
- 面向对象：完全零基础，希望在 28 天课程中建立 Python 科学计算、NumPy、PyTorch、张量、自动求导、简单神经网络、训练与推理最小心智模型的学习者

## 任务范围

按任务要求，本调研覆盖以下主题，并强调“零基础可理解”：

1. Python 科学计算
2. NumPy 基础
3. PyTorch 基础
4. 张量
5. 自动求导
6. 简单神经网络
7. 训练与推理概念

## 结论摘要

1. **最适合零基础的主线顺序是：Python 基础语法 → NumPy 数组 → PyTorch 张量 → 自动求导 → `nn.Module` 神经网络 → 训练/推理。**
   - 原因：NumPy 官方明确把 `ndarray` 作为数值计算核心对象；PyTorch 入门页和 Tensor 教程则默认学习者已经接受“多维数组/shape/运算”这套心智模型。
   - 来源：
     - NumPy Absolute Beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
     - PyTorch Learn the Basics: https://docs.pytorch.org/tutorials/beginner/basics/intro.html
     - PyTorch Tensor Tutorial: https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html

2. **NumPy 应该承担“科学计算启蒙层”，不是直接跳到深度学习。**
   - NumPy 官方文档强调其是 science and engineering 中广泛使用的开源 Python 库，核心是多维数组和围绕数组的高效运算；这正适合给初学者解释“为什么不用纯 Python 列表做数值计算”。
   - 来源：
     - NumPy Absolute Beginners: https://numpy.org/doc/stable/user/absolute_beginners.html
     - NumPy Learn 页面把 `NumPy: the absolute basics for beginners`、Quickstart、Scientific Python Lectures 列为 beginner 资源：https://numpy.org/learn/

3. **PyTorch 官方初学材料已经天然适合 28 天课程后段使用。**
   - `Learn the Basics` 提供 Quickstart、Tensors、Datasets & DataLoaders、Transforms、Build the Neural Network、Autograd、Optimization、Save & Load Model、Inference 等主题入口。
   - 来源：https://docs.pytorch.org/tutorials/beginner/basics/intro.html

4. **“张量”最好用“带形状的多维数字表”来讲，而不是先讲抽象数学定义。**
   - PyTorch Tensor Tutorial 面向初学者展示创建张量、shape、datatype、device、索引、拼接、矩阵乘法、reshape 等操作；对零基础课程，先建立可操作直觉更重要。
   - 来源：https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html

5. **自动求导不能从公式推导开始，而应从“参数改一点，损失怎么变”开始。**
   - PyTorch `A Gentle Introduction to torch.autograd` 的入门路径就是围绕 computation graph、gradient 与 `requires_grad` 展开，适合把反向传播解释成“系统自动帮你记录依赖并计算梯度”。
   - 来源：https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html

6. **简单神经网络最好先讲结构与数据流，再讲优化细节。**
   - PyTorch `Neural Networks` 教程使用 `nn.Module`、卷积层、前向传播和损失函数说明“输入如何一层层变成输出”；对初学者来说，先理解“层”和“前向计算”比先背优化器参数更重要。
   - 来源：https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html

7. **训练与推理必须明确分开讲。**
   - PyTorch `Quickstart` 和 `Start Locally` 页面都强调先安装、验证、再运行模型；而 `Learn the Basics` 目录中将 optimization、save/load、inference 拆开，说明“训练模型”和“拿模型做预测”是不同阶段。
   - 来源：
     - Quickstart: https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
     - Start Locally: https://docs.pytorch.org/get-started/locally/
     - Learn the Basics: https://docs.pytorch.org/tutorials/beginner/basics/intro.html

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

## 推荐资料清单

## 1. Python 科学计算总入口

### 1.1 Scientific Python Lectures — NumPy: creating and manipulating numerical data
- 链接：https://lectures.scientific-python.org/intro/numpy/index.html
- 类型：科学 Python 体系中的 NumPy 章节
- 适合程度：中高
- 难度：入门到初级
- 推荐理由：把 NumPy 放进更大的 scientific Python 生态里，适合课程编写者理解“为什么 NumPy 是科学计算基础层”。
- 适合用法：教师备课参考；不一定全文要求学生精读。

### 1.2 SciPy Lecture Notes — NumPy: creating and manipulating numerical data
- 链接：https://scipy-lectures.org/intro/numpy/index.html
- 类型：NumPy 系统讲义
- 适合程度：中高
- 难度：初级
- 推荐理由：章节结构完整，覆盖数组对象、索引切片、数值运算、broadcasting、shape manipulation、exercises。
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
- 推荐理由：NumPy 官方把 beginner 资源集中列出，可作为后续课程资源审查时的“源头导航页”。
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
- 课程用途：Day 1/Day 2 的安装与最小运行验证。

### 3.3 Start Locally — PyTorch
- 链接：https://docs.pytorch.org/get-started/locally/
- 类型：官方安装页
- 适合程度：高
- 难度：入门
- 推荐理由：提供安装命令与验证样例，并明确说明 Python 版本前提和 `pip install torch torchvision` 等最小安装方式。
- 课程用途：环境配置与安装核验。

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

### 7.1 Training a Classifier — PyTorch Tutorials
- 链接：https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
- 类型：官方训练示例
- 适合程度：中高
- 难度：初级到中级
- 推荐理由：虽然比前面几篇更长，但它把数据加载、网络、损失函数、优化器、训练循环、测试预测串成完整闭环，是理解“训练 vs 推理”的关键实例。
- 课程用途：教师精简后可作为综合 demo 来源。

### 7.2 Quickstart 中的训练/测试/推理流程
- 链接：https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
- 类型：快速闭环教程
- 适合程度：高
- 难度：入门到初级
- 推荐理由：相较 CIFAR10 教程更短，更适合零基础先跑通“训练一个模型，再拿它预测”。
- 课程用途：优先作为学生主线实验。

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
- reductions（如 sum / mean）
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

## 适合放入 28 天课程的拆分建议

如果并入《零基础计划》Week 4，建议分成 **5 天主线 + 1 天综合实验 + 1 天总复盘**：

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
- 练习：跑 quickstart 中的训练与推理片段
- 主资料：Quickstart Tutorial

### Day 27：综合 demo
- 目标：串联数据、模型、训练、预测
- 练习：运行精简版分类 demo，并把结果提交到 GitHub
- 主资料：Quickstart / CIFAR10 Tutorial（教师裁剪版）

### Day 28：结营复盘
- 目标：把 Linux / Git / Python / Cursor / Deep Learning 全链路串起来
- 练习：总结术语、提交作品、说明自己真正理解了什么

## 初学者常见误区

### 1. 把 NumPy 和 PyTorch 当成“两个互不相关的东西”

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

## 课程编写时的直接建议

1. **Week 4 不要再引入太多新工具。** 重点应放在概念建立与最小可运行 demo。
2. **每节课都要有“看得见的数字输出”。** 深度学习初学阶段最怕抽象漂浮。
3. **优先官方材料，辅以教师二次解释。** 这样证据链最清晰。
4. **训练 demo 必须做裁剪。** CIFAR10 官方教程适合作为教师参考，不适合完全原样丢给零基础学习者。
5. **把 shape 作为全周主线。** 从 NumPy 到 tensor 再到 network output，都围绕 shape 解释。

## 最小资料包建议

如果只保留最核心的 7 份资料，建议是：

1. Python Tutorial  
   https://docs.python.org/3/tutorial/
2. NumPy Absolute Beginners  
   https://numpy.org/doc/stable/user/absolute_beginners.html
3. NumPy Learn  
   https://numpy.org/learn/
4. PyTorch Learn the Basics  
   https://docs.pytorch.org/tutorials/beginner/basics/intro.html
5. PyTorch Tensor Tutorial  
   https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html
6. PyTorch Autograd Tutorial  
   https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html
7. PyTorch Neural Networks / Quickstart  
   https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
   https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html

## Provenance

本文件的结论和链接来自本次会话实际抓取与检索：

- `web_search`: `Python scientific computing beginner tutorial official NumPy beginners PyTorch learn the basics automatic differentiation neural network beginner`
- `web_fetch`: `https://numpy.org/doc/stable/user/absolute_beginners.html`
- `web_fetch`: `https://numpy.org/learn/`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/basics/intro.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html`
- `web_fetch`: `https://docs.pytorch.org/get-started/locally/`
- `web_fetch`: `https://scipy-lectures.org/intro/numpy/index.html`
- `web_fetch`: `https://lectures.scientific-python.org/intro/numpy/index.html`
- `web_fetch`: `https://docs.python.org/3/tutorial/`
