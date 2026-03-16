# 3. Semantic Invariance in Agentic AI

> 中文标题：Semantic Invariance in Agentic AI

> 这篇论文同时命中了 Agentic AI 方向的关键词，而且发布时间很近，适合作为本周优先跟踪对象。

| 字段 | 内容 |
| --- | --- |
| 方向 | Agentic AI |
| 来源 | arXiv |
| 发布时间 | 2026-03-13 |
| 作者 | I. de Zarzà, J. de Curtò, Jordi Cabot, Pietro Manzoni, Carlos T. Calafate |
| 原文入口 | [Abstract](http://arxiv.org/abs/2603.13173v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2603.13173v1) |

## 为什么值得看

从关键词覆盖、发布时间和主题贴合度来看，这篇论文值得进入本周跟踪列表。

## 核心方法

Large Language Models (LLMs) increasingly serve as autonomous reasoning agents in decision support, scientific problem-solving, and multi-agent coordination systems

## 技术要点

- 论文摘要显示其核心贡献和当前关注方向高度相关。
- 如果你在做路线判断，这篇更适合拿来快速理解最新思路。
- 建议结合原文的实验部分进一步确认真实增益。

## 应用价值

- 可作为相关方向的技术情报输入。
- 可辅助判断近期研究热点是否发生迁移。

## 风险与局限

- 当前分析基于摘要，不等价于完整精读。
- 真正的工程可用性还需要看实验设计和复现实验。

## 推荐谁读

- 做多模态生成研究的人
- 做视频生成或 Agent 产品判断的人
- 需要跟踪前沿技术路线的团队负责人

## 建议继续追问的问题

- 阅读原文方法部分与实验设置。
- 对比最近 4 到 6 周同方向论文的变化。

## 摘要摘录

> Large Language Models (LLMs) increasingly serve as autonomous reasoning agents in decision support, scientific problem-solving, and multi-agent coordination systems. However, deploying LLM agents in consequential applications requires assurance that their reasoning remains stable under semantically equivalent input variations, a property we term semantic invariance.Standard benchmark evaluations, which assess accuracy on fixed, canonical problem formulations, fail to capture this critical reliability dimension. To address this shortcoming, in this paper we present a metamorphic testing framework for systematically assessing the robustness of LLM reasoning agents, applying eight semantic-preserving transformations (identity, paraphrase, fact reordering, expansion, contraction, academic context, business context, and contrastive formulation) across seven foundation models spanning four distinct architectural families: Hermes (70B, 405B), Qwen3 (30B-A3B, 235B-A22B), DeepSeek-R1, and gpt-oss (20B, 120B). Our evaluation encompasses 19 multi-step reasoning problems across eight scientific domains. The results reveal that model scale does not predict robustness: the smaller Qwen3-30B-A3B achieves the highest stability (79.6% invariant responses, semantic similarity 0.91), while larger models exhibit greater fragility.

## 一句话结论

这篇论文同时命中了 Agentic AI 方向的关键词，而且发布时间很近，适合作为本周优先跟踪对象。
