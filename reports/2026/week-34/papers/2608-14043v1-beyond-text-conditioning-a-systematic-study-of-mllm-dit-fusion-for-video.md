# Beyond Text Conditioning: A Systematic Study of MLLM-DiT Fusion for Video Generation

> 中文标题：Beyond Text Conditioning: A Systematic Study of MLLM-DiT Fusion for Video Generation

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Image / Text-to-Video / Text-to-Image + Agentic AI / Text-to-Video + Agentic AI |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-08-14 |
| 作者 | Yanbo Ding, Yijia Fan, Caihua Shan, Yifan Yang, Yifei Shen, Weijie Wang |
| 原文入口 | [Abstract](http://arxiv.org/abs/2608.14043v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2608.14043v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Diffusion Transformers (DiTs) have become the dominant paradigm for high-fidelity video generation, yet their ability to perform high-level semantic planning remains limited. While hybrid architectures integrating MLLMs with diffusion backbones have shown strong advantages in image synthesis, such designs remain underexplored in video generation, where existing approaches often treat MLLMs primarily as frozen feature encoders rather than semantic generators. To fill this gap, we systematically study how an MLLM should be integrated with a DiT for video generation by answering three questions: what intermediate representation should bridge the MLLM and DiT, how the MLLM should generate it, and how the DiT should incorporate it during diffusion rendering. Our analysis reveals three key findings: (1) discrete semantic visual tokens produced by an EMA-based tokenizer provide a stable and expressive interface, (2) autoregressive causal modeling is effective for generating these tokens, and (3) explicit visual-token conditioning is more effective than prompt refinement or latent bridging. Based on these findings, we propose BiVidGen, a hybrid framework where an MLLM first generates semantic visual tokens and a DiT renders videos conditioned on both text and these tokens via multi-layer cross-attention. Extensive experiments show that BiVidGen improves semantic alignment and temporal coherence over a fine-tuned DiT baseline, achieving stronger performance on VBench-Long. These results demonstrate that explicit MLLM-based visual planning provides an effective intermediate interface for text-to-video generation beyond text-only conditioning.

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

Diffusion Transformers (DiTs) have become the dominant paradigm for high-fidelity video generation, yet their ability to perform high-level semantic planning remains limited. While hybrid architectures integrating MLLMs with diffusion backbones have shown strong advantages in image synthesis, such designs remain underexplored in video generation, where existing approaches often treat MLLMs primarily as frozen feature encoders rather than semantic generators. To fill this gap, we systematically study how an MLLM should be integrated with a DiT for video generation by answering three questions: what intermediate representation should bridge the MLLM and DiT, how the MLLM should generate it, and how the DiT should incorporate it during diffusion rendering. Our analysis reveals three key findings: (1) discrete semantic visual tokens produced by an EMA-based tokenizer provide a stable and expressive interface, (2) autoregressive causal modeling is effective for generating these tokens, and (3) explicit visual-token conditioning is more effective than prompt refinement or latent bridging. Based on these findings, we propose BiVidGen, a hybrid framework where an MLLM first generates semantic visual tokens and a DiT renders videos conditioned on both text and these tokens via multi-layer cross-attention. Extensive experiments show that BiVidGen improves semantic alignment and temporal coherence over a fine-tuned DiT baseline, achieving stronger performance on VBench-Long. These results demonstrate that explicit MLLM-based visual planning provides an effective intermediate interface for text-to-video generation beyond text-only conditioning.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 + Agentic AI 的关键特征。
