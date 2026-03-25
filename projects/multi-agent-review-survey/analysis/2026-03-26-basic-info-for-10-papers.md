# 2026-03-26 十篇论文基础信息汇总（供后续中文解读整理）

- Timestamp: 2026-03-26T01:11:19+08:00
- Session: 岛村-01-1774458634-983f86
- Task: 汇总 10 篇论文的基础信息，准备后续中文解读整理
- Status: completed

## 说明

本文件不重新发明一套论文名单，而是直接采用当前项目已经过 cross-review 锁定的 canonical reading set，并把后续中文解读最常用的基础字段整理成单表，方便继续写逐篇解读、横向比较与 idea 设计。

canonical reading set 的直接来源：

- `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`
- `projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-verification.md`

## 汇总表

| # | 简题 | 年份 | 题目 | 作者 | 来源页面 | 本地 PDF 路径 | 页数 | 后续解读侧重点 |
|---|---|---:|---|---|---|---|---:|---|
| 1 | Guo 2024 | 2024 | Large Language Model based Multi-Agents: A Survey of Progress and Challenges | Taicheng Guo; Xiuying Chen; Yaqi Wang; Ruidi Chang; Shichao Pei; Nitesh V. Chawla; Olaf Wiest; Xiangliang Zhang | https://arxiv.org/abs/2402.01680v2 | `projects/multi-agent-review-survey/literature/2024-guo-et-al-large-language-model-based-multi-agents-a-survey-of-progress-and-challenges-arxiv-2402.01680.pdf` | 15 | 总览型基线；适合提炼 MAS 组件、应用与挑战总图谱 |
| 2 | Aratchige & Ilmini 2025 | 2025 | LLMs Working in Harmony: A Survey on the Technological Aspects of Building Effective LLM-Based Multi Agent Systems | R. M. Aratchige; W. M. K. S. Ilmini | https://arxiv.org/abs/2504.01963v1 | `projects/multi-agent-review-survey/literature/2025-aratchige-ilmini-llms-working-in-harmony-a-survey-on-the-technological-aspects-of-building-effective-llm-based-multi-agent-systems-arxiv-2504.01963.pdf` | 12 | 技术栈导向；适合提炼 architecture / memory / planning / frameworks |
| 3 | Chen et al. 2024/2025 | 2024 | A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers in Application | Shuaihang Chen; Yuanxing Liu; Wei Han; Weinan Zhang; Ting Liu | https://arxiv.org/abs/2412.17481v2 | `projects/multi-agent-review-survey/literature/2025-chen-et-al-a-survey-on-llm-based-multi-agent-system-recent-advances-and-new-frontiers-in-application-arxiv-2412.17481.pdf` | 13 | 应用导向；适合整理复杂任务、仿真、评测前沿 |
| 4 | Tran et al. 2025 | 2025 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | Khanh-Tung Tran; Dung Dao; Minh-Duong Nguyen; Quoc-Viet Pham; Barry O'Sullivan; Hoang D. Nguyen | https://arxiv.org/abs/2501.06322v1 | `projects/multi-agent-review-survey/literature/2025-tran-et-al-multi-agent-collaboration-mechanisms-a-survey-of-llms-arxiv-2501.06322.pdf` | 35 | 协作机制 taxonomy；适合整理 actor/type/structure/protocol |
| 5 | Wu et al. 2025 | 2025 | Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances | Yaozu Wu; Dongyuan Li; Yankai Chen; Renhe Jiang; Henry Peng Zou; Wei-Chieh Huang; Yangning Li; Liancheng Fang; Zhen Wang; Philip S. Yu | https://arxiv.org/abs/2502.16804v2 | `projects/multi-agent-review-survey/literature/2025-wu-et-al-multi-agent-autonomous-driving-systems-with-large-language-models-a-survey-of-recent-advances-arxiv-2502.16804.pdf` | 18 | 垂直领域案例；适合提炼车路协同、多主体交互、部署约束 |
| 6 | Yan et al. 2025 | 2025 | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | Bingyu Yan; Zhibo Zhou; Litian Zhang; Lian Zhang; Ziyi Zhou; Dezhuang Miao; Zhoujun Li; Chaozhuo Li; Xiaoming Zhang | https://arxiv.org/abs/2502.14321v2 | `projects/multi-agent-review-survey/literature/2025-yan-et-al-beyond-self-talk-a-communication-centric-survey-of-llm-based-multi-agent-systems-arxiv-2502.14321.pdf` | 16 | 通信中心视角；适合整理 protocol / strategy / object / content |
| 7 | Xu et al. 2026 | 2026 | The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration | Haoyuan Xu; Chang Li; Xinyan Ma; Xianhao Ou; Zihan Zhang; Tao He; Xiangyu Liu; Zixiang Wang; Jiafeng Liang; Zheng Chu; Runxuan Liu; Rongchuan Mu; Ming Liu; Bing Qin | https://arxiv.org/abs/2603.22862v1 | `projects/multi-agent-review-survey/literature/2026-xu-et-al-tool-use-in-llm-agents.pdf` | 42 | 工具编排主线；适合整理 long-horizon orchestration、efficiency 与 safety |
| 8 | Yue et al. 2026 | 2026 | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | Ling Yue; Kushal Raj Bhandari; Ching-Yun Ko; Dhaval Patel; Shuxin Lin; Nianjun Zhou; Jianxi Gao; Pin-Yu Chen; Shaowu Pan | https://arxiv.org/abs/2603.22386v1 | `projects/multi-agent-review-survey/literature/2026-yue-et-al-workflow-optimization-for-llm-agents.pdf` | 31 | workflow 优化主线；适合整理静态模板、动态图结构与 verifier |
| 9 | Chen et al. 2026 | 2026 | The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs | Jingdi Chen; Hanqing Yang; Zongjun Liu; Carlee Joe-Wong | https://arxiv.org/abs/2602.11583v1 | `projects/multi-agent-review-survey/literature/2026-chen-et-al-five-ws-of-multi-agent-communication.pdf` | 143 | 5W 通信框架；适合做横向比较总轴 |
| 10 | Wang et al. 2026 | 2026 | Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends | Ye Wang; Jiaxing Chen; Hongjiang Xiao | https://arxiv.org/abs/2601.10122v1 | `projects/multi-agent-review-survey/literature/2026-wang-et-al-role-playing-agents.pdf` | 15 | 社会型 agent / role-play 主线；适合整理人格、记忆与叙事协作 |

## 读取顺序建议

为便于后续中文解读，建议按“总览 → 主线专题 → 工程专题 → 垂直/社会场景”阅读：

1. Guo 2024
2. Chen et al. 2024/2025
3. Tran et al. 2025
4. Yan et al. 2025
5. Chen et al. 2026
6. Aratchige & Ilmini 2025
7. Xu et al. 2026
8. Yue et al. 2026
9. Wu et al. 2025
10. Wang et al. 2026

## 基础统计

统计直接来自 `projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`：

- 总论文数：10 篇
- 年份分布：2024 年 2 篇（Guo 2024；Chen 2412/2024），2025 年 4 篇，2026 年 4 篇
- 页数总和：15 + 12 + 13 + 35 + 18 + 16 + 42 + 31 + 143 + 15 = 340 页

## 与后续中文整理的衔接

后续若要写中文逐篇解读，可直接把这 10 篇映射到以下已有材料：

- 逐篇结构化笔记：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
- 横向综合：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-synthesis-report.md`
- 中文主报告：`projects/multi-agent-review-survey/ten_multi_agent_surveys_cn.md`

## Provenance

- 论文名单、作者、年份、来源页面、页数：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-paper-metadata.md`
- canonical set 锁定依据：`projects/multi-agent-review-survey/analysis/2026-03-26-cross-review-record.md`
- PDF 可读性与页数核验：`projects/multi-agent-review-survey/analysis/2026-03-26-literature-pdf-verification.md`
- 中文解读衔接：`projects/multi-agent-review-survey/analysis/2026-03-26-ten-survey-structured-reading-notes.md`
