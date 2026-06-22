# WeGenBench: A Multidimensional Diagnostic Benchmark towards Text-to-Image Model Optimization

> 中文标题：WeGenBench: A Multidimensional Diagnostic Benchmark towards Text-to-Image Model Optimization

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Image / Text-to-Image + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-06-18 |
| 作者 | Qian Liang, Xiaomin Li, Ying Zhang, Jia Xu, Lihao Ni, Hongrui Li |
| 原文入口 | [Abstract](http://arxiv.org/abs/2606.20100v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2606.20100v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Recent text-to-image generation models have demonstrated remarkable capabilities in synthesizing highly realistic images from text inputs alone. Although existing benchmarks can evaluate the generation capabilities of various models to some extent, they struggle to comprehensively and accurately measure performance across multiple dimensions, often failing to reveal the inherent deficiencies of models in specific categories. To address these limitations, we propose WeGenBench, a novel benchmark designed for the comprehensive, multi-perspective evaluation of text-to-image generation capabilities. Our benchmark comprises a total of 4,000 test prompts across two primary categories, meticulously balanced between Chinese and English to evaluate bilingual and cross-cultural generation capabilities. Beyond macroscopic scene classification, we annotate each prompt with multi-dimensional tags tailored to the distinct content and challenges of each language, thereby refining the generation tasks into more specific sub-categories. Through a cross-dimensional evaluation mechanism leveraging both scene classifications and multi-dimensional tags, WeGenBench can precisely pinpoint model shortcomings in specific generation categories. Furthermore, to measure generation quality more accurately, we design and validate several novel evaluation metrics by integrating Vision-Language Models (VLMs), which assess model performance on domain-specific tasks from three core aspects. Crucially, our approach yields both the assessment outcomes and the detailed reasoning trajectories, facilitating a rigorous verification of the accuracy and soundness of the evaluation results. Finally, we conduct systematic benchmarking on current state-of-the-art methods and provide an in-depth analysis of the limitations present in existing models.

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

Recent text-to-image generation models have demonstrated remarkable capabilities in synthesizing highly realistic images from text inputs alone. Although existing benchmarks can evaluate the generation capabilities of various models to some extent, they struggle to comprehensively and accurately measure performance across multiple dimensions, often failing to reveal the inherent deficiencies of models in specific categories. To address these limitations, we propose WeGenBench, a novel benchmark designed for the comprehensive, multi-perspective evaluation of text-to-image generation capabilities. Our benchmark comprises a total of 4,000 test prompts across two primary categories, meticulously balanced between Chinese and English to evaluate bilingual and cross-cultural generation capabilities. Beyond macroscopic scene classification, we annotate each prompt with multi-dimensional tags tailored to the distinct content and challenges of each language, thereby refining the generation tasks into more specific sub-categories. Through a cross-dimensional evaluation mechanism leveraging both scene classifications and multi-dimensional tags, WeGenBench can precisely pinpoint model shortcomings in specific generation categories. Furthermore, to measure generation quality more accurately, we design and validate several novel evaluation metrics by integrating Vision-Language Models (VLMs), which assess model performance on domain-specific tasks from three core aspects. Crucially, our approach yields both the assessment outcomes and the detailed reasoning trajectories, facilitating a rigorous verification of the accuracy and soundness of the evaluation results. Finally, we conduct systematic benchmarking on current state-of-the-art methods and provide an in-depth analysis of the limitations present in existing models.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。
