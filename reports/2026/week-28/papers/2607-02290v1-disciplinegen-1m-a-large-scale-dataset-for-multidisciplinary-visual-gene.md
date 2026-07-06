# DisciplineGen-1M: A Large-Scale Dataset for Multidisciplinary Visual Generation and Editing

> 中文标题：DisciplineGen-1M: A Large-Scale Dataset for Multidisciplinary Visual Generation and Editing

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Image / Text-to-Image + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-07-02 |
| 作者 | Zhaokai Wang, Mingxin Liu, Zirun Zhu, Ziqian Fan, Yiguo He, Mohan Zhang |
| 原文入口 | [Abstract](http://arxiv.org/abs/2607.02290v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2607.02290v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Recent image generation and editing models can produce visually appealing natural images, yet they remain unreliable when the target image is a knowledge-intensive diagram whose correctness depends on disciplinary concepts, symbolic structure, and precise spatial relations. We introduce DisciplineGen-1M, a million-scale multidisciplinary dataset that supports text-to-image generation and image editing. It contains 1.2M samples spanning mathematics, physics, chemistry, biology, geography, computer science, economics, history, music, and sports. To construct the dataset, we design a scalable framework that combines vector-graphics rendering, OCR-based editing, curated programmatic synthesis, and large-scale text-to-image filtering. These pipelines produce captions, editing instructions, structured annotations, and paired images with controllable semantic differences. Building on DisciplineGen-1M, we further introduce a discipline-informed reasoning-generation model for both text-to-image generation and image editing. Experiments on discipline-related benchmarks, GenExam and GRADE, show substantial improvements over open-source baselines, while evaluations on general reasoning-informed benchmarks, WISE and RISE, further indicate broader transfer. The results suggest that large-scale structured academic visual data is a key ingredient for moving image generation from aesthetic plausibility toward verifiable knowledge-grounded visual creation. We will publicly release our dataset, model, and source code of the data curation pipeline to ensure reproducibility and benefit future research.

## 技术要点

- 建议先把这篇放回整个方向脉络里看，而不是孤立地看一篇论文。
- 如果你在做路线判断，比起单个指标，更要看它重新定义了什么任务边界。
- 真正的价值通常体现在是否改变了后续研究的默认范式。

## 应用价值

- 适合作为近期方向判断和技术情报输入。
- 适合帮助你发现哪些问题开始被研究社区反复强调。

## 风险与局限

- 当前分析基于论文摘要或配置中的方向摘记，不等价于完整精读。
- 真正的工程价值仍然需要结合实验设计、复现难度和系统成本来判断。

## 推荐谁读

- 需要做方向判断的研究负责人
- 在做生成式产品或 Agent 产品路线规划的人
- 需要追踪交叉方向机会的多模态团队

## 建议继续追问的问题

- 和同方向过去 4 到 8 周的工作做横向比较。
- 重点看实验设置、任务定义和是否真的解决了生产可用性问题。

## 摘要 / 内容摘记

Recent image generation and editing models can produce visually appealing natural images, yet they remain unreliable when the target image is a knowledge-intensive diagram whose correctness depends on disciplinary concepts, symbolic structure, and precise spatial relations. We introduce DisciplineGen-1M, a million-scale multidisciplinary dataset that supports text-to-image generation and image editing. It contains 1.2M samples spanning mathematics, physics, chemistry, biology, geography, computer science, economics, history, music, and sports. To construct the dataset, we design a scalable framework that combines vector-graphics rendering, OCR-based editing, curated programmatic synthesis, and large-scale text-to-image filtering. These pipelines produce captions, editing instructions, structured annotations, and paired images with controllable semantic differences. Building on DisciplineGen-1M, we further introduce a discipline-informed reasoning-generation model for both text-to-image generation and image editing. Experiments on discipline-related benchmarks, GenExam and GRADE, show substantial improvements over open-source baselines, while evaluations on general reasoning-informed benchmarks, WISE and RISE, further indicate broader transfer. The results suggest that large-scale structured academic visual data is a key ingredient for moving image generation from aesthetic plausibility toward verifiable knowledge-grounded visual creation. We will publicly release our dataset, model, and source code of the data curation pipeline to ensure reproducibility and benefit future research.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。
