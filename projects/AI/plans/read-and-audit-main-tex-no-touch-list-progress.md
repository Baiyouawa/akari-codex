# 进度记录：`projects/AI/main.tex` 可改写区域与禁止改动清单

## Milestone 1 — 边界确认
- 已读取 `AGENTS.md`、仓库 `README.md`、`tasks/TASKS.md`、近期会话日志，以及 `projects/AI/TASKS.md`。
- 已读取 `projects/AI/main.tex` 全文，并通过 `python3` 输出带行号版本用于定位。
- 证明：`python3 - <<'PY' ... Path('projects/AI/main.tex').read_text() ... PY` 输出了 1--196 行源码；本记录中的所有行号均据此整理。

## Milestone 2 — 可改写纯文字区域识别
以下区域属于“可改写的纯文字区域”，前提是仅改写自然语言措辞，不改动所在 LaTeX 命令、结构或引用键。

### A. 标题页中的纯文字
1. 第 42--48 行：封面标题文字
   - 包含课程名、报告标题、系统名称、副标题。
   - 可改写范围仅限花括号中的纯文字内容；命令层如 `{\Large ...}`、`\\[...]` 不可改。
2. 第 62--66 行：封面信息表中的单元格文字
   - 就后续安全改写规则而言，此处虽然承载纯文字，但因为位于 `table`/`tabularx` 环境内部，纳入禁止改动清单，不建议作为可改写区域处理。
3. 第 70 行：封面结尾说明句
   - 该句为表格外的纯说明文字，可在不改变命令包裹方式的前提下改写。

### B. 主体正文段落
1. 第 77 行：Introduction 正文段。
2. 第 88 行：Use Case Diagram 小节首段。
3. 第 110 行：关于 `<<include>>` / `<<extend>>` 的解释段。
4. 第 112--113 行：Use case specification 行内说明。
   - 可改写其中的自然语言说明。
   - 但 `\smallskip`、`\noindent`、`\textbf{...}`、`\textit{...}`、`\quad`、`\;`、`\textrightarrow` 等命令及排版结构不可改。
5. 第 115 行：约束与伦理治理说明段。
6. 第 118 行：对 Figure~1 的完整性与可辩护性的评价段。
7. 第 127 行：Activity Diagram 小节首段。
8. 第 130 行：Amazon POS lane、并发控制、人工复核与超时机制说明段。
9. 第 132 行：结束逻辑与 UML 完整性评价段。
10. 第 136 行：结论段。
11. 第 140--141 行：Recommendations 两条建议项中的纯文字。
    - 仅条目文本可改写；`\begin{enumerate}`、`\item`、加粗命令等结构不可改。

### C. 参考文献条目中的书目信息文字
- 第 146--153 行中的书目内容严格依赖 `\bibitem{...}` 引用键与现有文献条目信息。
- 本专项将其归入禁止改动项，不作为安全可改写区。

### D. 附录反思文字
1. 第 173--178 行：Fu Renjie 反思文字。
2. 第 181--186 行：Wu Renxuan 反思文字。
3. 第 189--194 行：Cui Zhiqing 反思文字。
- 这些段落为连续自然语言，可在不改变署名格式、命令骨架和段落顺序的前提下改写。

## Milestone 3 — 禁止改动清单（执行版）

### 1. 表格整体禁止改动
- 第 57--68 行：标题页 `table` / `tabularx` 环境全部冻结。
- 第 90--108 行：Requirement Analysis Table 的 `table` / `tabular` 环境全部冻结。
- 第 159--169 行：Effort Allocation Sheet 的 `table` / `tabularx` 环境全部冻结。
- 规则：禁止改列数、列宽、行序、单元格边界、`\hline`、`\rowcolor`、图片签名嵌入、百分号写法等。

### 2. 图题禁止改动
- 第 82 行：`\caption{Amazon Enterprise Online POS Use Case Diagram}`
- 第 123 行：`\caption{Activity Diagram for Checkout Confirmation, Shipping, and Payment}`
- 规则：caption 全文字面内容保持不变。

### 3. 图片引用禁止改动
- 第 81 行：`{UML.drawio.pdf}`
- 第 122 行：`{ActivityDiagram.drawio.pdf}`
- 第 165--167 行：三处签名图片文件名引用
- 规则：禁止修改文件名、路径、`\includegraphics` 参数、裁切参数、宽度、旋转参数。

### 4. 公式禁止改动
- 当前文件中未出现数学公式环境，也未出现独立公式编号。
- 结论：本项在当前文件中“未出现”；若后续版本涉及公式，公式内容、数学命令与结构同样应冻结。

### 5. 标签禁止改动
- 当前文件中未出现 `\label{...}`。
- 结论：本项在当前文件中“未出现”；若后续补充标签，不应在纯文字改写任务中增删改。

### 6. 引用键禁止改动
- 第 146--153 行：`\bibitem{acm2018}`、`\bibitem{booch1999}`、`\bibitem{dennis2015}`、`\bibitem{fowler2004}`、`\bibitem{omg2017}`、`\bibitem{pcissc2022}`、`\bibitem{sommerville2016}`、`\bibitem{w3c2018}`。
- 同时，第 77、88、110、115、118、127、130、132、136 行中的括号式文内引文也应保持原有文献对应关系不变。
- 规则：禁止改动引用键、作者-年份对应关系、文献条目顺序。

### 7. 章节结构禁止改动
- 第 75 行：`\section{Introduction}`
- 第 84 行：`\section{The OO Analysis and Design with UML Techniques}`
- 第 86 行：`\subsection{The Design of Functional Requirements with Use Case Diagrams}`
- 第 125 行：`\subsection{The Design of Functional Behaviour with Activity Diagrams}`
- 第 134 行：`\section{Conclusions and Recommendations}`
- 第 157 行：`\section*{Effort Allocation Sheet}`
- 第 171 行：`\section*{Appendix: Individual Reflections}`
- 规则：禁止改章节层级、顺序、标题名称、带星号与否。

### 8. 环境命令禁止改动
- 包括但不限于：`\begin{document}` / `\end{document}`、`titlepage`、`table`、`tabularx`、`tabular`、`figure`、`thebibliography`、`enumerate`。
- 具体出现位置：第 36/196、38/71、57/68、90/108、79/83、120/124、144/154、139/142、159/169 行等。
- 规则：禁止增删环境、调整嵌套关系、改环境参数。

### 9. 文档类、宏包与版式命令禁止改动
- 第 1--34 行全部属于导言区配置。
- 规则：禁止改动 `\documentclass`、`\usepackage`、字体、页边距、颜色、标题间距、caption 样式、列表样式等命令。

### 10. 特定 LaTeX 命令骨架禁止改动
- 第 110、112、118、127、130、132、138--141、173、181、189 行等处出现的 `\texttt`、`\textit`、`\textbf`、`\quad`、`\;`、`\textrightarrow`、`\bigskip`、`\\` 等排版命令与结构符号，均应保持。
- 允许改写的仅是命令包裹的自然语言文本，不包括命令名、参数层次和排版控制符。

## 执行建议：后续改写时的安全边界
1. 优先改写的主区域：第 77、88、110、115、118、127、130、132、136、140--141、174--178、182--186、190--194 行中的连续自然语言。
2. 谨慎改写区域：第 42--48、70、112--113、173、181、189 行等带命令包裹的文本，只能改文字，不能碰命令骨架。
3. 不应改写区域：所有表格内容、所有图题、所有 `\includegraphics`、全部参考文献条目、全部章节标题与环境命令。

## 当前结论
本次审查已足以支撑后续“只改纯文字、不碰结构”的安全改写。`projects/AI/main.tex` 目前不存在公式与 `\label`，但用户要求中的这两类项目仍应纳入通用禁止改动规则。