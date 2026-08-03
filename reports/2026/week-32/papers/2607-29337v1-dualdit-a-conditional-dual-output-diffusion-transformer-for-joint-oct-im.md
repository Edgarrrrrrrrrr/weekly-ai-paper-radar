# DualDiT: A Conditional Dual-Output Diffusion Transformer for Joint OCT Image and Segmentation Mask Generation

> 中文标题：DualDiT: A Conditional Dual-Output Diffusion Transformer for Joint OCT Image and Segmentation Mask Generation

> 这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 的关键特征。

| 字段 | 内容 |
| --- | --- |
| 方向 | Text-to-Image |
| 类型 | 本期关注 |
| 来源 | arXiv |
| 发布时间 | 2026-07-31 |
| 作者 | Fernando García-Torres, Rocío del Amor, Sandra Morales, Álvaro Barroso, Peter Heiduschka, Björn Kemper |
| 原文入口 | [Abstract](http://arxiv.org/abs/2607.29337v1) |
| PDF | [Download PDF](https://arxiv.org/pdf/2607.29337v1) |

## 为什么值得看

这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。

## 核心方法 / 关键贡献

Background and Objective: Generating realistic medical images with anatomically accurate segmentation masks helps address the shortage of annotated data in medical imaging, particularly in optical coherence tomography (OCT) of mouse eyes, where manual retinal layer delineation is labour-intensive due to tiny structures and required expertise, resulting in scarce datasets. While diffusion models perform well in medical image synthesis, joint image-mask generation has relied mainly on U-Net-based denoisers, leaving diffusion transformers largely unexplored. Methods: We propose a conditional dual-output Diffusion Transformer (DualDiT) for joint synthesis of OCT B-scans and segmentation masks of the upper retinal cell layers in ex vivo mouse retina. DualDiT encodes both modalities into a shared latent space via a pretrained VAE, concatenates their latent representations, and performs conditional diffusion over the joint tensor. We compared DualDiT against two adapted diffusion baselines: DDPM and LDM. Generative quality was assessed via Fréchet Inception Distance (FID) and spatial FID (sFID); practical utility via synthetic data augmentation for downstream U-Net segmentation; and perceptual realism via evaluation by three domain experts. Results: DualDiT achieved the best generative quality (FID 56.14, sFID 114.35), outperforming DDPM and LDM. Expert panels misclassified 46% of synthetic samples as real and 42% of real samples as synthetic. Adding DualDiT-generated images and masks improved Dice and IoU scores on a held-out segmentation test set. Conclusions: DualDiT shows that transformer-based diffusion models can effectively learn the joint distribution of OCT images and segmentation masks, surpassing DDPM- and LDM-based baselines in generative fidelity, downstream utility, and perceptual realism, highlighting its potential for data augmentation in annotation-scarce medical imaging.

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

Background and Objective: Generating realistic medical images with anatomically accurate segmentation masks helps address the shortage of annotated data in medical imaging, particularly in optical coherence tomography (OCT) of mouse eyes, where manual retinal layer delineation is labour-intensive due to tiny structures and required expertise, resulting in scarce datasets. While diffusion models perform well in medical image synthesis, joint image-mask generation has relied mainly on U-Net-based denoisers, leaving diffusion transformers largely unexplored. Methods: We propose a conditional dual-output Diffusion Transformer (DualDiT) for joint synthesis of OCT B-scans and segmentation masks of the upper retinal cell layers in ex vivo mouse retina. DualDiT encodes both modalities into a shared latent space via a pretrained VAE, concatenates their latent representations, and performs conditional diffusion over the joint tensor. We compared DualDiT against two adapted diffusion baselines: DDPM and LDM. Generative quality was assessed via Fréchet Inception Distance (FID) and spatial FID (sFID); practical utility via synthetic data augmentation for downstream U-Net segmentation; and perceptual realism via evaluation by three domain experts. Results: DualDiT achieved the best generative quality (FID 56.14, sFID 114.35), outperforming DDPM and LDM. Expert panels misclassified 46% of synthetic samples as real and 42% of real samples as synthetic. Adding DualDiT-generated images and masks improved Dice and IoU scores on a held-out segmentation test set. Conclusions: DualDiT shows that transformer-based diffusion models can effectively learn the joint distribution of OCT images and segmentation masks, surpassing DDPM- and LDM-based baselines in generative fidelity, downstream utility, and perceptual realism, highlighting its potential for data augmentation in annotation-scarce medical imaging.

## 一句话结论

这是这个方向近期更值得跟踪的新工作之一，它同时命中了 文生图 的关键特征。
