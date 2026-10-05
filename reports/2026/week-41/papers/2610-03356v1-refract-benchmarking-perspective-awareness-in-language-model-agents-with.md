# ReFract: Benchmarking Perspective Awareness in Language Model Agents with Text World Models

> 中文标题：ReFract: Benchmarking Perspective Awareness in Language Model Agents with Text World Models

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Video + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-10-02 |
| 作者 | Hainiu Xu, Vítor N. Lourenço, Mohnish Dubey, Yunfei Bai, Yulan He, Caroline Catmur |
| 原文入口 | [Abstract](http://arxiv.org/abs/2610.03356v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2610.03356v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Large Language Model (LLM) agents are increasingly deployed in high-stakes settings such as industrial maintenance and equipment fault troubleshooting, where workers occupy a variety of roles. A capable agent must therefore act in a way that is calibrated to user's role: taking actions and providing information that respect the role's knowledge and capability boundaries. Unlike coding, where mistakes are usually recoverable, agent responses in these settings are enacted on physical equipment, and can therefore cause irreversible equipment damage, production loss, or personnel harm. Existing benchmarks, however, largely overlook the need for agents to infer what a role intends and acting only through tools that role may legitimately use, a capability which we term Perspective Awareness. To this end, we introduce ReFract, a benchmark of 150 expert-validated entries in which an agent must act differently in response to the same query depending on user's role. Entries of ReFract are grounded in anonymized queries from domain support conversations, against which we construct Text World Models that simulate the agent's operating environments and assemble perspective-aware action trajectories. State-of-the-art LLMs solve at most 69% of the tasks with more than 50% of their trajectories contain attempts of taking perspective-violating actions. ReFract exposes perspective awareness as a distinct, largely unsolved axis of agent evaluation and motivates agents that calibrate not just how to act, but for whom.

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

Large Language Model (LLM) agents are increasingly deployed in high-stakes settings such as industrial maintenance and equipment fault troubleshooting, where workers occupy a variety of roles. A capable agent must therefore act in a way that is calibrated to user's role: taking actions and providing information that respect the role's knowledge and capability boundaries. Unlike coding, where mistakes are usually recoverable, agent responses in these settings are enacted on physical equipment, and can therefore cause irreversible equipment damage, production loss, or personnel harm. Existing benchmarks, however, largely overlook the need for agents to infer what a role intends and acting only through tools that role may legitimately use, a capability which we term Perspective Awareness. To this end, we introduce ReFract, a benchmark of 150 expert-validated entries in which an agent must act differently in response to the same query depending on user's role. Entries of ReFract are grounded in anonymized queries from domain support conversations, against which we construct Text World Models that simulate the agent's operating environments and assemble perspective-aware action trajectories. State-of-the-art LLMs solve at most 69% of the tasks with more than 50% of their trajectories contain attempts of taking perspective-violating actions. ReFract exposes perspective awareness as a distinct, largely unsolved axis of agent evaluation and motivates agents that calibrate not just how to act, but for whom.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 + Agentic AI 的关键特征。
