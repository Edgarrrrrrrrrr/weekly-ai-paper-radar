# Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs

> 中文标题：Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Image + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-05-08 |
| 作者 | Sree Bhattacharyya, Samarth Khanna, Leona Chen, Lucas Craig, Tharun Dilliraj, James Z. Wang |
| 原文入口 | [Abstract](http://arxiv.org/abs/2605.07806v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2605.07806v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Large Language Models (LLMs) are increasingly used in settings where reliable self-assessment is critical. Assessing model reliability has evolved from using probabilistic correctness estimates to, more recently, eliciting verbalized confidence. Confidence, however, has been shown to be an inconsistent and overoptimistic predictor of model correctness. Drawing on cognitive appraisal theory, a framework from human psychology that decomposes self-evaluation into multiple components, we propose a multidimensional perspective on model self-assessment. We elicit six appraisal-based dimensions of self-assessment, alongside confidence, and evaluate their utility for predicting model failure across 12 LLMs and 38 tasks spanning eight domains. We find that competence-related appraisal dimensions, particularly effort and ability, consistently match or outperform confidence across most settings. Effort additionally yields less overoptimistic estimates that remain stable across model sizes. In contrast, affective dimensions provide marginally predictive signals. Furthermore, the most informative dimension varies systematically with task characteristics: effort is most predictive for reasoning-intensive tasks, while ability and confidence dominate on retrieval-oriented tasks. Broadly, our findings indicate that structured multidimensional self-assessment is a promising approach to improving the reliability and safety of language model deployment across diverse real-world settings.

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

Large Language Models (LLMs) are increasingly used in settings where reliable self-assessment is critical. Assessing model reliability has evolved from using probabilistic correctness estimates to, more recently, eliciting verbalized confidence. Confidence, however, has been shown to be an inconsistent and overoptimistic predictor of model correctness. Drawing on cognitive appraisal theory, a framework from human psychology that decomposes self-evaluation into multiple components, we propose a multidimensional perspective on model self-assessment. We elicit six appraisal-based dimensions of self-assessment, alongside confidence, and evaluate their utility for predicting model failure across 12 LLMs and 38 tasks spanning eight domains. We find that competence-related appraisal dimensions, particularly effort and ability, consistently match or outperform confidence across most settings. Effort additionally yields less overoptimistic estimates that remain stable across model sizes. In contrast, affective dimensions provide marginally predictive signals. Furthermore, the most informative dimension varies systematically with task characteristics: effort is most predictive for reasoning-intensive tasks, while ability and confidence dominate on retrieval-oriented tasks. Broadly, our findings indicate that structured multidimensional self-assessment is a promising approach to improving the reliability and safety of language model deployment across diverse real-world settings.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。
