from __future__ import annotations

from weekly_paper.config import PipelineConfig
from weekly_paper.models import PaperAnalysis, RankedPaper, WeeklyEditorial
from weekly_paper.openai_client import OpenAIJSONClient


def rank_with_llm(
    client: OpenAIJSONClient,
    ranked_candidates: list[RankedPaper],
    config: PipelineConfig,
) -> tuple[list[RankedPaper], WeeklyEditorial]:
    papers = [item.paper for item in ranked_candidates[: config.candidate_pool]]
    items = []
    for paper in papers:
        items.append(
            {
                "paper_id": paper.paper_id,
                "title": paper.title,
                "abstract": paper.abstract,
                "authors": paper.authors[:6],
                "categories": paper.categories,
                "published": paper.published.isoformat(),
                "matched_topics": paper.matched_topics,
                "keyword_score": paper.keyword_score,
            }
        )

    system_prompt = (
        "You are a world-class AI research analyst. "
        "Choose the most important papers for an applied research team tracking "
        "Text-to-Image, Text-to-Video, and Agentic AI. "
        "Only use the provided metadata and abstracts. "
        "Return strict JSON."
    )
    user_prompt = (
        "Select the most important papers for this week.\n"
        f"Need exactly {config.max_papers} papers.\n"
        "Language for all narrative fields: Simplified Chinese.\n"
        "Return JSON with this schema:\n"
        "{"
        '"selected":[{"paper_id":"...","rank":1,"importance_score":85,"why_now":"...","direction_fit":"..."}],'
        '"editorial":{"headline":"...","overview":"...","trend_signals":["..."],"watchlist":["..."]}'
        "}\n"
        f"Candidates:\n{items}"
    )

    response = client.complete_json(system_prompt=system_prompt, user_prompt=user_prompt)
    selected_lookup = {item["paper_id"]: item for item in response["selected"]}
    updated: list[RankedPaper] = []

    for candidate in papers:
        chosen = selected_lookup.get(candidate.paper_id)
        if not chosen:
            continue
        updated.append(
            RankedPaper(
                paper=candidate,
                rank=int(chosen["rank"]),
                importance_score=int(chosen["importance_score"]),
                why_now=chosen["why_now"],
                direction_fit=chosen["direction_fit"],
            )
        )

    updated.sort(key=lambda item: item.rank)

    if len(updated) < config.max_papers:
        chosen_ids = {item.paper.paper_id for item in updated}
        for candidate in ranked_candidates:
            if candidate.paper.paper_id in chosen_ids:
                continue
            updated.append(
                RankedPaper(
                    paper=candidate.paper,
                    rank=len(updated) + 1,
                    importance_score=candidate.importance_score,
                    why_now=candidate.why_now,
                    direction_fit=candidate.direction_fit,
                )
            )
            if len(updated) == config.max_papers:
                break

    editorial_data = response["editorial"]
    editorial = WeeklyEditorial(
        headline=editorial_data["headline"],
        overview=editorial_data["overview"],
        trend_signals=list(editorial_data["trend_signals"]),
        watchlist=list(editorial_data["watchlist"]),
    )
    return updated[: config.max_papers], editorial


def analyze_paper(
    client: OpenAIJSONClient,
    paper: RankedPaper,
    language: str,
) -> PaperAnalysis:
    system_prompt = (
        "You are a thoughtful technical editor writing elegant, concrete research digests. "
        "Use only the provided paper metadata and abstract. "
        "Do not hallucinate experiments or numbers that are not implied by the abstract. "
        "Return strict JSON."
    )
    user_prompt = (
        f"Write a polished analysis in {language}.\n"
        "Return JSON with this schema:\n"
        "{"
        '"title_zh":"...",'
        '"tagline":"...",'
        '"importance":"...",'
        '"core_innovation":"...",'
        '"technical_takeaways":["..."],'
        '"applications":["..."],'
        '"limitations":["..."],'
        '"who_should_read":["..."],'
        '"follow_ups":["..."],'
        '"one_line":"..."'
        "}\n"
        f"Paper title: {paper.paper.title}\n"
        f"Matched topics: {paper.paper.matched_topics}\n"
        f"Why now: {paper.why_now}\n"
        f"Abstract: {paper.paper.abstract}\n"
    )
    response = client.complete_json(system_prompt=system_prompt, user_prompt=user_prompt)
    return PaperAnalysis(
        title_zh=response["title_zh"],
        tagline=response["tagline"],
        importance=response["importance"],
        core_innovation=response["core_innovation"],
        technical_takeaways=list(response["technical_takeaways"]),
        applications=list(response["applications"]),
        limitations=list(response["limitations"]),
        who_should_read=list(response["who_should_read"]),
        follow_ups=list(response["follow_ups"]),
        one_line=response["one_line"],
    )


def fallback_analysis(paper: RankedPaper) -> PaperAnalysis:
    first_sentence = paper.paper.abstract.split(". ")[0].strip()
    if not first_sentence:
        first_sentence = paper.paper.abstract[:180].strip()

    return PaperAnalysis(
        title_zh=paper.paper.title,
        tagline=paper.why_now,
        importance=(
            "从关键词覆盖、发布时间和主题贴合度来看，这篇论文值得进入本周跟踪列表。"
        ),
        core_innovation=first_sentence,
        technical_takeaways=[
            "论文摘要显示其核心贡献和当前关注方向高度相关。",
            "如果你在做路线判断，这篇更适合拿来快速理解最新思路。",
            "建议结合原文的实验部分进一步确认真实增益。"
        ],
        applications=[
            "可作为相关方向的技术情报输入。",
            "可辅助判断近期研究热点是否发生迁移。",
        ],
        limitations=[
            "当前分析基于摘要，不等价于完整精读。",
            "真正的工程可用性还需要看实验设计和复现实验。"
        ],
        who_should_read=[
            "做多模态生成研究的人",
            "做视频生成或 Agent 产品判断的人",
            "需要跟踪前沿技术路线的团队负责人"
        ],
        follow_ups=[
            "阅读原文方法部分与实验设置。",
            "对比最近 4 到 6 周同方向论文的变化。"
        ],
        one_line=paper.why_now,
    )
