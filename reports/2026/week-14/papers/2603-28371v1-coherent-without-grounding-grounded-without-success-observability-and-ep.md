# Coherent Without Grounding, Grounded Without Success: Observability and Epistemic Failure

> 中文标题：Coherent Without Grounding, Grounded Without Success: Observability and Epistemic Failure

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Image + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-03-30 |
| 作者 | Camilo Chacón Sartori |
| 原文入口 | [Abstract](http://arxiv.org/abs/2603.28371v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2603.28371v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

When an agent can articulate why something works, we typically take this as evidence of genuine understanding. This presupposes that effective action and correct explanation covary, and that coherent explanation reliably signals both. I argue that this assumption fails for contemporary Large Language Models (LLMs). I introduce what I call the Bidirectional Coherence Paradox: competence and grounding not only dissociate but invert across epistemic conditions. In low-observability domains, LLMs often act successfully while misidentifying the mechanisms that produce their success. In high-observability domains, they frequently generate explanations that accurately track observable causal structure yet fail to translate those diagnoses into effective intervention. In both cases, explanatory coherence remains intact, obscuring the underlying dissociation. Drawing on experiments in compiler optimization and hyperparameter tuning, I develop the Epistemic Triangle, a model of how priors, signals, and domain knowledge interact under varying observability. The results suggest that neither behavioral success nor explanatory accuracy alone suffices for attributing understanding. I argue that evaluating artificial epistemic agents requires a tripartite framework -- coherence, grounding, and a proper basing relation linking explanation to action. The systematic separation of knowing-that and knowing-how in LLMs thus challenges assumptions inherited from both epistemology and current AI evaluation practice.

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

When an agent can articulate why something works, we typically take this as evidence of genuine understanding. This presupposes that effective action and correct explanation covary, and that coherent explanation reliably signals both. I argue that this assumption fails for contemporary Large Language Models (LLMs). I introduce what I call the Bidirectional Coherence Paradox: competence and grounding not only dissociate but invert across epistemic conditions. In low-observability domains, LLMs often act successfully while misidentifying the mechanisms that produce their success. In high-observability domains, they frequently generate explanations that accurately track observable causal structure yet fail to translate those diagnoses into effective intervention. In both cases, explanatory coherence remains intact, obscuring the underlying dissociation. Drawing on experiments in compiler optimization and hyperparameter tuning, I develop the Epistemic Triangle, a model of how priors, signals, and domain knowledge interact under varying observability. The results suggest that neither behavioral success nor explanatory accuracy alone suffices for attributing understanding. I argue that evaluating artificial epistemic agents requires a tripartite framework -- coherence, grounding, and a proper basing relation linking explanation to action. The systematic separation of knowing-that and knowing-how in LLMs thus challenges assumptions inherited from both epistemology and current AI evaluation practice.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。
