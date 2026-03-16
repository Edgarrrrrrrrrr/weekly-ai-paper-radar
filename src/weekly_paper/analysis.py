from __future__ import annotations

from weekly_paper.models import PaperAnalysis, TopicReport, WeeklyEditorial, RankedPaper
from weekly_paper.openai_client import OpenAIJSONClient


def enhance_topic_reports_with_llm(
    client: OpenAIJSONClient,
    topic_reports: list[TopicReport],
    language: str,
) -> list[TopicReport]:
    updated: list[TopicReport] = []
    for report in topic_reports:
        system_prompt = (
            "You are a senior AI research editor. "
            "Write concise, specific weekly direction notes. "
            "Use only the provided titles, rationales, and summaries. "
            "Return strict JSON."
        )
        payload = {
            "topic": report.topic_name_zh,
            "landmarks": [
                {
                    "title": item.paper.title,
                    "reason": item.selection_reason,
                    "summary": item.paper.abstract,
                }
                for item in report.landmark_papers
            ],
            "recent": [
                {
                    "title": item.paper.title,
                    "reason": item.selection_reason,
                    "summary": item.paper.abstract,
                }
                for item in report.recent_papers
            ],
        }
        user_prompt = (
            f"Language: {language}\n"
            "Return JSON with this schema:\n"
            "{"
            '"summary":"...",'
            '"trend_signals":["...", "...", "..."]'
            "}\n"
            f"Direction data:\n{payload}"
        )
        response = client.complete_json(system_prompt=system_prompt, user_prompt=user_prompt)
        updated.append(
            TopicReport(
                topic_name=report.topic_name,
                topic_name_zh=report.topic_name_zh,
                topic_slug=report.topic_slug,
                summary=response["summary"],
                trend_signals=list(response["trend_signals"]),
                landmark_papers=report.landmark_papers,
                recent_papers=report.recent_papers,
            )
        )
    return updated


def enhance_editorial_with_llm(
    client: OpenAIJSONClient,
    topic_reports: list[TopicReport],
    language: str,
) -> WeeklyEditorial:
    system_prompt = (
        "You are a sharp but grounded AI strategy editor. "
        "Summarize the weekly state of research directions based only on the supplied notes. "
        "Return strict JSON."
    )
    payload = [
        {
            "topic": report.topic_name_zh,
            "summary": report.summary,
            "trends": report.trend_signals,
            "landmarks": [item.paper.title for item in report.landmark_papers],
            "recent": [item.paper.title for item in report.recent_papers],
        }
        for report in topic_reports
    ]
    user_prompt = (
        f"Language: {language}\n"
        "Return JSON with this schema:\n"
        "{"
        '"headline":"...",'
        '"overview":"...",'
        '"trend_signals":["...", "...", "..."],'
        '"watchlist":["...", "...", "..."]'
        "}\n"
        f"Direction reports:\n{payload}"
    )
    response = client.complete_json(system_prompt=system_prompt, user_prompt=user_prompt)
    return WeeklyEditorial(
        headline=response["headline"],
        overview=response["overview"],
        trend_signals=list(response["trend_signals"]),
        watchlist=list(response["watchlist"]),
    )


def analyze_paper(
    client: OpenAIJSONClient,
    paper: RankedPaper,
    language: str,
) -> PaperAnalysis:
    system_prompt = (
        "You are a thoughtful technical editor writing elegant, concrete research digests. "
        "Use only the provided paper metadata and summary. "
        "Do not hallucinate experiments or claims beyond the supplied information. "
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
        f"Direction: {paper.direction_fit}\n"
        f"Collection kind: {paper.paper.collection_kind}\n"
        f"Selection reason: {paper.selection_reason}\n"
        f"Summary: {paper.paper.abstract}\n"
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
    first_sentence = paper.paper.abstract.split("。")[0].strip()
    if not first_sentence:
        first_sentence = paper.paper.abstract.split(". ")[0].strip()
    if not first_sentence:
        first_sentence = paper.paper.abstract[:180].strip()

    if paper.paper.collection_kind == "landmark":
        importance = "这是一篇值得长期反复回看的基石论文，用来建立这个方向的共同语言和判断框架。"
        applications = [
            "适合做方向入门和团队知识对齐。",
            "适合用来判断今天很多新工作究竟是在延续哪条主线。",
        ]
        follow_ups = [
            "回看它之后的代表性继承工作和变体路线。",
            "把它和本期新工作放在一起看，判断哪些是真创新，哪些只是工程封装。",
        ]
    else:
        importance = "这是当前阶段值得跟踪的新工作，适合拿来观察研究重心是否正在发生迁移。"
        applications = [
            "适合作为近期方向判断和技术情报输入。",
            "适合帮助你发现哪些问题开始被研究社区反复强调。",
        ]
        follow_ups = [
            "和同方向过去 4 到 8 周的工作做横向比较。",
            "重点看实验设置、任务定义和是否真的解决了生产可用性问题。",
        ]

    return PaperAnalysis(
        title_zh=paper.paper.title,
        tagline=paper.selection_reason,
        importance=importance,
        core_innovation=first_sentence,
        technical_takeaways=[
            "建议先把这篇放回整个方向脉络里看，而不是孤立地看一篇论文。",
            "如果你在做路线判断，比起单个指标，更要看它重新定义了什么任务边界。",
            "真正的价值通常体现在是否改变了后续研究的默认范式。",
        ],
        applications=applications,
        limitations=[
            "当前分析基于论文摘要或配置中的方向摘记，不等价于完整精读。",
            "真正的工程价值仍然需要结合实验设计、复现难度和系统成本来判断。",
        ],
        who_should_read=[
            "需要做方向判断的研究负责人",
            "在做生成式产品或 Agent 产品路线规划的人",
            "需要追踪交叉方向机会的多模态团队",
        ],
        follow_ups=follow_ups,
        one_line=paper.selection_reason,
    )
