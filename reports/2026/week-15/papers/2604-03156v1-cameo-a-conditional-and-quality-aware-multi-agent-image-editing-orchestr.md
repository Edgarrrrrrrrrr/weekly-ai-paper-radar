# CAMEO: A Conditional and Quality-Aware Multi-Agent Image Editing Orchestrator

> 中文标题：CAMEO: A Conditional and Quality-Aware Multi-Agent Image Editing Orchestrator

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Agentic AI / Text-to-Image / Text-to-Image + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-04-03 |
| 作者 | Yuhan Pu, Hao Zheng, Ziqian Mo, Hill Zhang, Tianyi Fan, Shuhong Wu |
| 原文入口 | [Abstract](http://arxiv.org/abs/2604.03156v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2604.03156v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Conditional image editing aims to modify a source image according to textual prompts and optional reference guidance. Such editing is crucial in scenarios requiring strict structural control (i.e., anomaly insertion in driving scenes and complex human pose transformation). Despite recent advances in large-scale editing models (i.e., Seedream, Nano Banana, etc), most approaches rely on single-step generation. This paradigm often lacks explicit quality control, may introduce excessive deviation from the original image, and frequently produces structural artifacts or environment-inconsistent modifications, typically requiring manual prompt tuning to achieve acceptable results. We propose \textbf{CAMEO}, a structured multi-agent framework that reformulates conditional editing as a quality-aware, feedback-driven process rather than a one-shot generation task. CAMEO decomposes editing into coordinated stages of planning, structured prompting, hypothesis generation, and adaptive reference grounding, where external guidance is invoked only when task complexity requires it. To overcome the lack of intrinsic quality control in existing methods, evaluation is embedded directly within the editing loop. Intermediate results are iteratively refined through structured feedback, forming a closed-loop process that progressively corrects structural and contextual inconsistencies. We evaluate CAMEO on anomaly insertion and human pose switching tasks. Across multiple strong editing backbones and independent evaluation models, CAMEO consistently achieves 20\% more win rate on average compared to multiple state-of-the-art models, demonstrating improved robustness, controllability, and structural reliability in conditional image editing.

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

Conditional image editing aims to modify a source image according to textual prompts and optional reference guidance. Such editing is crucial in scenarios requiring strict structural control (i.e., anomaly insertion in driving scenes and complex human pose transformation). Despite recent advances in large-scale editing models (i.e., Seedream, Nano Banana, etc), most approaches rely on single-step generation. This paradigm often lacks explicit quality control, may introduce excessive deviation from the original image, and frequently produces structural artifacts or environment-inconsistent modifications, typically requiring manual prompt tuning to achieve acceptable results. We propose \textbf{CAMEO}, a structured multi-agent framework that reformulates conditional editing as a quality-aware, feedback-driven process rather than a one-shot generation task. CAMEO decomposes editing into coordinated stages of planning, structured prompting, hypothesis generation, and adaptive reference grounding, where external guidance is invoked only when task complexity requires it. To overcome the lack of intrinsic quality control in existing methods, evaluation is embedded directly within the editing loop. Intermediate results are iteratively refined through structured feedback, forming a closed-loop process that progressively corrects structural and contextual inconsistencies. We evaluate CAMEO on anomaly insertion and human pose switching tasks. Across multiple strong editing backbones and independent evaluation models, CAMEO consistently achieves 20\% more win rate on average compared to multiple state-of-the-art models, demonstrating improved robustness, controllability, and structural reliability in conditional image editing.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。
