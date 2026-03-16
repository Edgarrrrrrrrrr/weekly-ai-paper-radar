from __future__ import annotations

from datetime import datetime, timezone

from weekly_paper.config import PipelineConfig, TopicConfig
from weekly_paper.models import Paper, RankedPaper, TopicReport, WeeklyEditorial


def annotate_papers(papers: list[Paper], topics: list[TopicConfig]) -> list[Paper]:
    annotated: list[Paper] = []
    for paper in papers:
        matched_topics: list[str] = []
        topic_scores: dict[str, float] = {}

        title_text = paper.title.lower()
        abstract_text = paper.abstract.lower()

        for topic in topics:
            group_scores: list[float] = []
            for group in topic.keyword_groups:
                score = 0.0
                for keyword in group:
                    lowered = keyword.lower()
                    score += title_text.count(lowered) * 3
                    score += abstract_text.count(lowered)
                group_scores.append(score)

            if group_scores and all(score > 0 for score in group_scores):
                total_score = sum(group_scores) + (len(group_scores) * 4)
                matched_topics.append(topic.name)
                topic_scores[topic.name] = total_score

        if matched_topics:
            paper.matched_topics = matched_topics
            paper.topic_scores = topic_scores
            paper.keyword_score = max(topic_scores.values())
            annotated.append(paper)

    annotated.sort(key=lambda item: (item.keyword_score, item.published), reverse=True)
    return annotated


def select_recent_papers_for_topic(
    papers: list[Paper],
    topic: TopicConfig,
    limit: int,
    exclude_ids: set[str] | None = None,
) -> list[RankedPaper]:
    exclude_ids = exclude_ids or set()
    candidates = [
        paper
        for paper in papers
        if topic.name in paper.matched_topics and paper.paper_id not in exclude_ids
    ]
    candidates.sort(
        key=lambda item: (item.topic_scores.get(topic.name, 0.0), item.published),
        reverse=True,
    )

    ranked: list[RankedPaper] = []
    for index, paper in enumerate(candidates[:limit], start=1):
        score = int(65 + min(25, paper.topic_scores.get(topic.name, 0.0) * 2))
        ranked.append(
            RankedPaper(
                paper=paper,
                rank=index,
                importance_score=score,
                selection_reason=(
                    f"这是这个方向近期更值得跟踪的新工作之一，"
                    f"它同时命中了 {topic.name_zh} 的关键特征。"
                ),
                direction_fit=topic.name_zh,
            )
        )
    return ranked


def build_topic_reports(
    config: PipelineConfig,
    landmark_papers: dict[str, list[RankedPaper]],
    recent_papers: list[Paper],
) -> list[TopicReport]:
    reports: list[TopicReport] = []
    landmark_ids = {
        ranked.paper.paper_id
        for ranked_list in landmark_papers.values()
        for ranked in ranked_list
    }

    for topic in config.topics:
        recents = select_recent_papers_for_topic(
            recent_papers,
            topic=topic,
            limit=config.recent_papers_per_topic,
            exclude_ids=landmark_ids,
        )
        reports.append(
            TopicReport(
                topic_name=topic.name,
                topic_name_zh=topic.name_zh,
                topic_slug=topic.slug,
                summary=_fallback_topic_summary(topic, recents),
                trend_signals=_fallback_topic_signals(topic, recents),
                landmark_papers=landmark_papers.get(topic.name, []),
                recent_papers=recents,
            )
        )
    return reports


def build_weekly_editorial(topic_reports: list[TopicReport], now: datetime | None = None) -> WeeklyEditorial:
    now = now or datetime.now(timezone.utc)
    active_topics = [report.topic_name_zh for report in topic_reports]
    headline = f"{now.year} 年当前阶段，更值得跟踪的是 Agent 与视觉生成交叉方向的系统化演进。"
    overview = (
        "这份周报不再只看最近几天的新论文，而是把每个方向的长期基石、近期值得关注的新工作、"
        "以及研究趋势放在一起看，帮助你做路线判断。"
    )
    trend_signals = [
        "Agentic AI 持续从单轮推理走向工具调用、规划和恢复能力。",
        "文生图 + Agent 方向更像在构建可编排的视觉工作流，而不只是单次生成。",
        "文生视频 + Agent 方向越来越接近世界模型、交互环境和长期控制。",
    ]
    watchlist = [
        f"当前跟踪方向：{' / '.join(active_topics)}",
        "关注是否出现真正可执行的多工具生成代理工作流。",
        "关注视频世界模型是否开始稳定支撑长时序 Agent 训练与评估。",
    ]
    return WeeklyEditorial(
        headline=headline,
        overview=overview,
        trend_signals=trend_signals,
        watchlist=watchlist,
    )


def _fallback_topic_summary(topic: TopicConfig, recents: list[RankedPaper]) -> str:
    if topic.slug == "agentic-ai":
        base = "这个方向的核心已经从“会不会推理”转向“能不能在真实任务中规划、调用工具并稳定完成任务”。"
    elif topic.slug == "text-to-image-agentic-ai":
        base = "这个方向更值得关注的是：大模型如何成为图像生成与编辑工具链的编排层，让生成流程可拆解、可修正、可多步执行。"
    else:
        base = "这个方向正在从单纯的视频生成走向可交互环境、世界模型和长时序控制，为 Agent 提供训练与模拟空间。"

    if not recents:
        return base
    titles = "；".join(item.paper.title for item in recents[:2])
    return f"{base} 本期可以重点留意：{titles}。"


def _fallback_topic_signals(topic: TopicConfig, recents: list[RankedPaper]) -> list[str]:
    signals: list[str]
    if topic.slug == "agentic-ai":
        signals = [
            "更强调工具使用与规划，而不只是语言推理。",
            "研究目标逐步转向真实环境任务完成度。",
            "鲁棒性、恢复能力和可验证性会越来越重要。",
        ]
    elif topic.slug == "text-to-image-agentic-ai":
        signals = [
            "图像生成逐步成为可被 Agent 拆解和调度的工作流。",
            "编辑、重绘、局部控制等能力会比单纯画质更重要。",
            "多模型协作会比单模型单次输出更值得关注。",
        ]
    else:
        signals = [
            "视频生成开始和世界模型、模拟环境概念靠近。",
            "长时序一致性和动作反馈是关键难点。",
            "这一方向更适合关注“环境可用性”而不是单段视频好不好看。",
        ]

    if recents:
        signals[0] = f"{signals[0]} 本期样本数：{len(recents)}。"
    return signals
