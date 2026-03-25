# multi-agent-review-survey — 任务列表

- [ ] 检索近年与 multi-agent 相关的最新综述论文，优先覆盖 2024-2026，筛选最相关且具有代表性的 5 篇综述，记录来源链接（arXiv/OpenReview/出版社页面）与入选理由。 [zero-resource] [blocked-by: 当前项目 `literature/`、`analysis/`、`logs/` 在会话开始时为空，且仓库检索未发现可验证的 2024-2026 multi-agent 综述候选元数据/来源链接；在仅允许 `read_file` + `search_text` 的本地证据约束下，无法判定“最新五篇”及入选理由。详见 `projects/multi-agent-review-survey/analysis/2026-03-25-latest-review-selection-blocker-assessment.md`]
  Done when: 仓库内补齐可追溯的候选综述元数据或来源页面快照，并据此完成 5 篇综述的筛选、来源记录与入选理由说明。

- [ ] 将筛选出的 5 篇综述论文下载到本地 paper 目录，优先保存 PDF，并整理文件名、元数据与下载来源；若下载受阻，立即报告具体阻塞论文、来源与缺失资料。 [zero-resource] [blocked-by: 上游“5 篇综述筛选”任务未完成，当前仓库内不存在已确认的目标论文清单与来源页面。]
  Done when: 仓库内存在已确认的 5 篇目标综述及其来源页面，并将 PDF/元数据保存到本地 `paper/` 目录。

- [ ] 对第 1 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 1 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 对第 2 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 2 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 对第 3 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 3 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 对第 4 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 4 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 对第 5 篇综述进行详读，提炼研究背景、问题定义、分类体系、核心方法脉络、实验/benchmark、局限性与未来方向，输出中文详细笔记。 [zero-resource] [blocked-by: 目标综述尚未筛定，且仓库内没有该论文的 PDF、摘要摘录或已验证笔记。]
  Done when: 第 5 篇综述已在仓库内具备可追溯全文或已验证阅读材料，并形成中文详细笔记。

- [ ] 综合 5 篇综述，撰写一份中文 markdown 报告，包含：五篇综述分别的详细解读、横向比较、研究空白总结。 [zero-resource] [blocked-by: 前置的 5 篇综述筛选、下载与逐篇详读任务均未完成。]
  Done when: 5 篇综述的中文详细笔记全部完成，并整合为横向综述报告。

- [ ] 基于 5 篇综述的共同空白与趋势，提出 5 个可做的研究 idea；每个 idea 需要写清问题动机、核心假设、方法设计、数据/benchmark、评测指标、潜在风险与预期贡献。 [zero-resource] [blocked-by: 缺少前置的 5 篇综述比较与研究空白总结。]
  Done when: 基于已完成的 5 篇综述比较，产出 5 个结构完整的研究 idea。

- [ ] 检索 multi-agent 相关最新5篇综述论文，优先覆盖 arXiv 与 OpenReview，可补充可信学术来源 [zero-resource] [blocked-by: 仓库内仍无可验证的本地候选综述清单、来源页面快照、PDF、摘要摘录或已验证笔记；`search_text(pattern="multi-agent|survey|综述|review|arXiv|OpenReview", path="projects/multi-agent-review-survey", max_results=200)` 在本会话返回 no matches，因此在零外部检索约束下无法确认“最新5篇”。详见 `projects/multi-agent-review-survey/logs/2026-03-25T23:27:42+08:00-fleet-沙弥香-01-1774452423-4754bc-latest-five-surveys-blocked.md`]
  Done when: 仓库内补齐候选综述的可追溯元数据或来源页面快照，并据此确认5篇目标综述。

- [ ] 将确认后的5篇综述下载到本地 paper 目录，并记录来源链接与文件名映射 [zero-resource] [blocked-by: 上游“确认5篇综述”任务未完成；当前仓库内没有已确认论文标题、来源链接或 PDF 地址，无法生成可追溯下载与文件名映射。]
  Done when: 仓库内已有确认后的5篇综述及其来源链接，并已将对应文件保存到 `projects/multi-agent-review-survey/paper/`，同时记录来源链接与文件名映射。

- [ ] 逐篇精读5篇综述，提取研究问题、分类框架、核心方法、数据集/基准、优缺点与未来方向 [zero-resource] [blocked-by: 缺少已确认并下载到仓库内的5篇综述全文或等效可追溯阅读材料；本次复核仍确认仓库内无已筛定五篇综述与逐篇可读源。详见 `projects/multi-agent-review-survey/logs/2026-03-25T23:29:31+08:00-fleet-结衣-03-1774452423-785487-five-survey-deep-reading-blocked.md`。]
  Done when: 5篇综述均具备本地全文或可追溯阅读材料，并完成逐篇结构化笔记。

- [ ] 汇总生成中文 Markdown 文档，分别详述5篇综述的内容与价值 [zero-resource] [blocked-by: 前置逐篇精读任务尚未完成。]
  Done when: 基于5篇综述的结构化笔记生成中文 Markdown 汇总文档。

- [ ] 基于5篇综述提出5个可做的研究 idea，并为每个 idea 写出具体方法设计、可行性与潜在贡献 [zero-resource] [blocked-by: 缺少前置综述比较与研究空白综合。]
  Done when: 形成5个结构完整、来源可追溯的研究 idea。

- [x] 若任一论文缺失、下载失败或信息不全，立即报告阻塞详情：哪个Agent卡住、卡点与缺失资料 [zero-resource]
  Completed: 2026-03-25T23:32:11+08:00
  Evidence: `projects/multi-agent-review-survey/analysis/2026-03-25-blocker-rollup.md`; `projects/multi-agent-review-survey/logs/2026-03-25T23:32:11+08:00-fleet-岛村-01-1774452693-235d22-blocker-rollup.md`

- [ ] 将 multi-agent 相关最新综述的检索范围从5篇扩展到10篇，确保时间新、相关性强且尽量覆盖不同子方向 [zero-resource] [blocked-by: 当前仓库既没有已确认的5篇综述基线，也没有本地候选综述题录/来源快照/PDF/笔记库可用于 provenance-backed 的 10 篇筛选；详见 `projects/multi-agent-review-survey/logs/2026-03-25T23:32:28+08:00-fleet-智乃-02-1774452693-e956e9-ten-survey-expansion-blocked.md`]
  Done when: 仓库内先补齐已确认的5篇综述清单，或补齐可追溯的 recent multi-agent 综述候选库，再据此筛出时间新、相关性强且覆盖不同子方向的10篇综述。

- [ ] 对新增的5篇综述完成来源核验，优先从 arXiv 或 OpenReview 获取原文并下载到本地 paper 目录 [zero-resource] [blocked-by: 上游“扩展到10篇”任务未完成，且当前仓库没有新增5篇综述的已确认题录、来源页或 PDF 地址。]
  Done when: 仓库内已确认新增5篇综述及其来源页面，并将原文/元数据保存到 `projects/multi-agent-review-survey/paper/`。

- [ ] 对全部10篇综述逐篇精读，补充研究问题、方法框架、任务分类、评测设置、优缺点与未来方向 [zero-resource] [blocked-by: 缺少10篇已确认综述的本地全文、摘要摘录或已验证阅读笔记。]
  Done when: 10篇综述均具备本地全文或等效可追溯阅读材料，并完成逐篇结构化笔记。

- [ ] 更新最终中文 Markdown，将原来的5篇综述详述扩展为10篇综述详述 [zero-resource] [blocked-by: 前置的10篇综述筛选、下载与逐篇精读尚未完成。]
  Done when: 基于10篇综述的结构化笔记产出更新后的中文 Markdown 总结文档。

- [ ] 检查原任务中的 idea 部分是否需要根据10篇综述重新提炼，如无额外指示则先保持输出5个高质量 idea 并用10篇综述作为依据 [zero-resource] [blocked-by: 缺少基于10篇综述的横向比较与研究空白综合。]
  Done when: 明确 idea 输出口径，并完成基于10篇综述证据的 idea 校正或重提炼。

- [ ] 检索 multi-agent 相关最新 10 篇综述论文，优先 arXiv、OpenReview、期刊官网与会议官方页面，确认题目、年份、来源与 PDF 链接 [zero-resource]
  Done when: TBD

- [ ] 将确认后的 10 篇综述论文 PDF 下载到项目 literature 文件夹中，确保文件可打开且命名规范 [zero-resource]
  Done when: TBD

- [ ] 记录每篇论文的元数据（题目、作者、年份、来源、PDF 路径）并汇总到项目文档中 [zero-resource]
  Done when: TBD

- [ ] 若下载受阻或缺失 PDF，第一时间汇报具体卡住的 Agent、阻塞点与缺失资料 [zero-resource]
  Done when: TBD

