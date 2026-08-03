# MoRoute: Dynamic Routing for In-Context Multimodal Video Generation

> 中文标题：MoRoute: Dynamic Routing for In-Context Multimodal Video Generation

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Video |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-07-31 |
| 作者 | Chong Gao, Jie Ma, Zhan Peng, Chongxiao Wang, Haoxue Wu, Jun Liang |
| 原文入口 | [Abstract](http://arxiv.org/abs/2607.29545v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2607.29545v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Multimodal video generation aims to generate and edit videos conditioned on arbitrary combinations of text, images, and videos within a single model, allowing diverse tasks to share complementary data and generative priors. Unifying these tasks requires multimodal understanding of diverse conditions, which is typically provided by a pretrained vision-language model (VLM). A key challenge is how to connect the VLM's hierarchical multimodal representations with a pretrained video diffusion transformer (DiT). Existing methods either inject features from only the final or a few manually selected VLM layers, or jointly train architecture-matched understanding and generation streams, making it difficult to reuse heterogeneous pretrained backbones. We introduce MoRoute, a unified multimodal video generation framework that formulates a frozen VLM and a pretrained video DiT with different architectures as heterogeneous experts connected through dynamic layer routing. For each input, a lightweight block-wise router enables every DiT block to select the VLM layer most relevant to its generation stage, thereby learning an adaptive correspondence between multimodal understanding and video synthesis. MoRoute further incorporates reference images and source videos directly into the DiT token sequence through unified in-context conditioning, preserving fine-grained visual details across diverse generation and editing tasks. Experiments on IntelligentVBench, OpenVE-Bench, and RefVIE-Bench show that MoRoute consistently surpasses the best competing method on each benchmark, improving the average score by 0.15, 0.18, and 0.34 on a 1-5 scale, respectively.

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

Multimodal video generation aims to generate and edit videos conditioned on arbitrary combinations of text, images, and videos within a single model, allowing diverse tasks to share complementary data and generative priors. Unifying these tasks requires multimodal understanding of diverse conditions, which is typically provided by a pretrained vision-language model (VLM). A key challenge is how to connect the VLM's hierarchical multimodal representations with a pretrained video diffusion transformer (DiT). Existing methods either inject features from only the final or a few manually selected VLM layers, or jointly train architecture-matched understanding and generation streams, making it difficult to reuse heterogeneous pretrained backbones. We introduce MoRoute, a unified multimodal video generation framework that formulates a frozen VLM and a pretrained video DiT with different architectures as heterogeneous experts connected through dynamic layer routing. For each input, a lightweight block-wise router enables every DiT block to select the VLM layer most relevant to its generation stage, thereby learning an adaptive correspondence between multimodal understanding and video synthesis. MoRoute further incorporates reference images and source videos directly into the DiT token sequence through unified in-context conditioning, preserving fine-grained visual details across diverse generation and editing tasks. Experiments on IntelligentVBench, OpenVE-Bench, and RefVIE-Bench show that MoRoute consistently surpasses the best competing method on each benchmark, improving the average score by 0.15, 0.18, and 0.34 on a 1-5 scale, respectively.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生视频 的关键特征。
