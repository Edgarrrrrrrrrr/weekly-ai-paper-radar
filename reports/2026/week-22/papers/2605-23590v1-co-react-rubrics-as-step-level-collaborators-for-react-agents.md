# Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents

> 中文标题：Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-05-22 |
| 作者 | Jiazheng Kang, Bowen Zhang, Zixin Song, Jiangwang Chen, Xiao Yang, Da Zhu |
| 原文入口 | [Abstract](http://arxiv.org/abs/2605.23590v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2605.23590v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

ReAct-style agents for search-intensive, multi-step reasoning tasks rely largely on their own internal judgment to decide what evidence to seek, which reasoning or action step to take next, and when to stop, often producing shallow, redundant, or poorly targeted trajectories. Prior work has explored rubrics as external quality signals, but existing uses are mostly evaluative rather than action-guiding: rubrics typically serve as training-time rewards or post-hoc evaluators of completed outputs, and in deep-research settings they are often coarse-grained and report-level rather than step-level. We introduce Co-ReAct, a rubric-guided action-selection framework that uses rubrics as step-level guidance during inference. At each decision step, Co-ReAct injects a rubric into the agent's context to guide the next Reason-or-Act decision, specifying what the agent should target in evidence seeking, search, reasoning, or self-evaluation. To make this guidance reliable, we train a dedicated rubric generator with GRPO. Unlike prior pairwise or binary preference formulations, our objective optimizes a list-wise Spearman rank-correlation reward against multi-judge expert consensus rankings, encouraging rubrics that are discriminative rather than merely plausible. On DeepResearchBench and SQA-CS-V2, Co-ReAct consistently improves over ReAct and representative test-time compute baselines across search agents built on both 8B/14B open-source and frontier closed-source base models. The trained rubric generator can also serve as a drop-in component that improves these baselines without changing their underlying decision mechanisms. Our code is publicly available at https://github.com/ZBWpro/Co-ReAct.

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

ReAct-style agents for search-intensive, multi-step reasoning tasks rely largely on their own internal judgment to decide what evidence to seek, which reasoning or action step to take next, and when to stop, often producing shallow, redundant, or poorly targeted trajectories. Prior work has explored rubrics as external quality signals, but existing uses are mostly evaluative rather than action-guiding: rubrics typically serve as training-time rewards or post-hoc evaluators of completed outputs, and in deep-research settings they are often coarse-grained and report-level rather than step-level. We introduce Co-ReAct, a rubric-guided action-selection framework that uses rubrics as step-level guidance during inference. At each decision step, Co-ReAct injects a rubric into the agent's context to guide the next Reason-or-Act decision, specifying what the agent should target in evidence seeking, search, reasoning, or self-evaluation. To make this guidance reliable, we train a dedicated rubric generator with GRPO. Unlike prior pairwise or binary preference formulations, our objective optimizes a list-wise Spearman rank-correlation reward against multi-judge expert consensus rankings, encouraging rubrics that are discriminative rather than merely plausible. On DeepResearchBench and SQA-CS-V2, Co-ReAct consistently improves over ReAct and representative test-time compute baselines across search agents built on both 8B/14B open-source and frontier closed-source base models. The trained rubric generator can also serve as a drop-in component that improves these baselines without changing their underlying decision mechanisms. Our code is publicly available at https://github.com/ZBWpro/Co-ReAct.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 Agentic AI 的关键特征。
