from __future__ import annotations

from typing import Iterable

from weekly_paper.config import PipelineConfig, TopicConfig
from weekly_paper.models import Paper, RankedPaper, WeeklyEditorial


def annotate_papers(papers: Iterable[Paper], topics: list[TopicConfig]) -> list[Paper]:
    annotated: list[Paper] = []
    for paper in papers:
        haystack = f"{paper.title} {paper.abstract}".lower()
        matched_topics: list[str] = []
        keyword_score = 0.0

        for topic in topics:
            topic_hits = 0
            for keyword in topic.keywords:
                lowered = keyword.lower()
                title_hits = paper.title.lower().count(lowered)
                body_hits = paper.abstract.lower().count(lowered)
                topic_hits += (title_hits * 3) + body_hits
            if topic_hits > 0:
                matched_topics.append(topic.name)
                keyword_score += float(topic_hits)

        if matched_topics:
            paper.matched_topics = matched_topics
            paper.keyword_score = keyword_score
            annotated.append(paper)

    annotated.sort(key=lambda item: (item.keyword_score, item.published), reverse=True)
    return annotated


def heuristic_rank(papers: list[Paper], config: PipelineConfig) -> tuple[list[RankedPaper], WeeklyEditorial]:
    selected = papers[: config.candidate_pool]
    ranked: list[RankedPaper] = []

    for index, paper in enumerate(selected, start=1):
        direction_fit = " / ".join(paper.matched_topics)
        ranked.append(
            RankedPaper(
                paper=paper,
                rank=index,
                importance_score=max(60, min(95, int(60 + paper.keyword_score * 4))),
                why_now=(
                    f"这篇论文同时命中了 {direction_fit} 方向的关键词，"
                    "而且发布时间很近，适合作为本周优先跟踪对象。"
                ),
                direction_fit=direction_fit,
            )
        )

    editorial = WeeklyEditorial(
        headline="本周研究重点围绕生成质量、视频时序一致性和 Agent 能力边界展开。",
        overview=(
            "从近期候选论文看，图像与视频生成继续朝更强的控制性和更高的效率演化，"
            "而 Agentic AI 更关注工具调用、规划和系统级可靠性。"
        ),
        trend_signals=[
            "生成模型仍在追求更强控制信号与更低成本推理。",
            "视频方向持续强调长时序、一致性与编辑能力。",
            "Agent 研究更偏向真实任务完成度，而不只是 benchmark 得分。",
        ],
        watchlist=[
            "多模态生成与 Agent 能力的融合是否开始加速。",
            "是否出现能显著降低训练或推理成本的新方法。",
            "是否出现真正可落地的视频长序列架构。",
        ],
    )
    return ranked, editorial
