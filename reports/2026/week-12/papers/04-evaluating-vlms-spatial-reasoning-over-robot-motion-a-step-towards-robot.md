# 4. Evaluating VLMs' Spatial Reasoning Over Robot Motion: A Step Towards Robot Planning with Motion Preferences

> 中文标题：Evaluating VLMs' Spatial Reasoning Over Robot Motion: A Step Towards Robot Planning with Motion Preferences

> 这篇论文同时命中了 Agentic AI 方向的关键词，而且发布时间很近，适合作为本周优先跟踪对象。

| 字段 | 内容 |
| --- | --- |
| 方向 | Agentic AI |
| 来源 | arXiv |
| 发布时间 | 2026-03-13 |
| 作者 | Wenxi Wu, Jingjing Zhang, Martim Brandão |
| 原文入口 | [Abstract](http://arxiv.org/abs/2603.13100v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2603.13100v1) |

## 为什么值得看

从关键词覆盖、发布时间和主题贴合度来看，这篇论文值得进入本周跟踪列表。

## 核心方法

Understanding user instructions and object spatial relations in surrounding environments is crucial for intelligent robot systems to assist humans in various tasks

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

> Understanding user instructions and object spatial relations in surrounding environments is crucial for intelligent robot systems to assist humans in various tasks. The natural language and spatial reasoning capabilities of Vision-Language Models (VLMs) have the potential to enhance the generalization of robot planners on new tasks, objects, and motion specifications. While foundation models have been applied to task planning, it is still unclear the degree to which they have the capability of spatial reasoning required to enforce user preferences or constraints on motion, such as desired distances from objects, topological properties, or motion style preferences. In this paper, we evaluate the capability of four state-of-the-art VLMs at spatial reasoning over robot motion, using four different querying methods. Our results show that, with the highest-performing querying method, Qwen2.5-VL achieves 71.4% accuracy zero-shot and 75% on a smaller model after fine-tuning, and GPT-4o leads to lower performance. We evaluate two types of motion preferences (object-proximity and path-style), and we also analyze the trade-off between accuracy and computation cost in number of tokens. This work shows some promise in the potential of VLM integration with robot motion planning pipelines.

## 一句话结论

这篇论文同时命中了 Agentic AI 方向的关键词，而且发布时间很近，适合作为本周优先跟踪对象。
