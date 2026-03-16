from __future__ import annotations

from argparse import ArgumentParser
from datetime import date, datetime, timezone
from pathlib import Path

from weekly_paper.analysis import (
    analyze_paper,
    enhance_editorial_with_llm,
    enhance_topic_reports_with_llm,
    fallback_analysis,
)
from weekly_paper.arxiv_client import fetch_recent_papers
from weekly_paper.config import PipelineConfig, load_config
from weekly_paper.models import Paper, RankedPaper
from weekly_paper.openai_client import OpenAIJSONClient
from weekly_paper.ranking import annotate_papers, build_topic_reports, build_weekly_editorial
from weekly_paper.reporting import write_report_bundle


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Generate a weekly AI paper digest.")
    parser.add_argument("--config", default="config/pipeline.json")
    parser.add_argument("--output-dir", default="reports")
    parser.add_argument("--feed-file", default="")
    parser.add_argument("--today", default="")
    parser.add_argument("--offline", action="store_true")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    config = load_config(args.config)
    target_date = (
        date.fromisoformat(args.today)
        if args.today
        else datetime.now(timezone.utc).date()
    )
    now = datetime.combine(target_date, datetime.min.time(), tzinfo=timezone.utc)

    feed_text = None
    if args.feed_file:
        feed_text = Path(args.feed_file).read_text(encoding="utf-8")

    recent_papers = fetch_recent_papers(
        categories=config.categories,
        days_back=config.days_back,
        max_results=config.max_results,
        feed_text=feed_text,
        now=now,
    )
    recent_papers = annotate_papers(recent_papers, config.topics)

    _, landmark_rankings = build_landmark_rankings(config)
    topic_reports = build_topic_reports(
        config=config,
        landmark_papers=landmark_rankings,
        recent_papers=recent_papers,
    )
    editorial = build_weekly_editorial(topic_reports, now=now)

    client = OpenAIJSONClient()
    if client.enabled and not args.offline:
        try:
            topic_reports = enhance_topic_reports_with_llm(client, topic_reports, config.language)
        except Exception as exc:
            print(f"LLM topic summaries failed, using fallback summaries instead: {exc}")
        try:
            editorial = enhance_editorial_with_llm(client, topic_reports, config.language)
        except Exception as exc:
            print(f"LLM editorial failed, using fallback editorial instead: {exc}")

    analyses = build_analyses(topic_reports, client=client, language=config.language, offline=args.offline)
    output_dir = Path(args.output_dir)
    bundle_dir = write_report_bundle(output_dir, target_date, editorial, topic_reports, analyses)

    print(f"Generated report bundle at {bundle_dir}")
    return 0


def build_landmark_rankings(config: PipelineConfig) -> tuple[dict[str, Paper], dict[str, list[RankedPaper]]]:
    papers: dict[str, Paper] = {}
    rankings: dict[str, list[RankedPaper]] = {}

    for topic in config.topics:
        ranked_list: list[RankedPaper] = []
        for index, landmark in enumerate(topic.landmarks, start=1):
            paper = papers.get(landmark.paper_id)
            if paper is None:
                published_year = int(landmark.published_label[:4])
                published = datetime(published_year, 1, 1, tzinfo=timezone.utc)
                paper = Paper(
                    paper_id=landmark.paper_id,
                    source="arXiv",
                    title=landmark.title,
                    abstract=landmark.summary,
                    authors=landmark.authors,
                    categories=[],
                    published=published,
                    updated=published,
                    abs_url=landmark.abs_url,
                    pdf_url=landmark.pdf_url,
                    published_label=landmark.published_label,
                    collection_kind="landmark",
                )
                papers[landmark.paper_id] = paper

            if topic.name not in paper.matched_topics:
                paper.matched_topics.append(topic.name)
            paper.topic_scores[topic.name] = 100.0
            paper.keyword_score = max(paper.keyword_score, 100.0)

            ranked_list.append(
                RankedPaper(
                    paper=paper,
                    rank=index,
                    importance_score=max(90, 99 - index),
                    selection_reason=landmark.rationale,
                    direction_fit=topic.name_zh,
                )
            )
        rankings[topic.name] = ranked_list
    return papers, rankings


def build_analyses(
    topic_reports,
    client: OpenAIJSONClient,
    language: str,
    offline: bool,
) -> dict[str, object]:
    analyses = {}
    ranked_papers = collect_unique_ranked_papers(topic_reports)
    for paper in ranked_papers:
        if client.enabled and not offline:
            try:
                analyses[paper.paper.paper_id] = analyze_paper(client, paper, language)
                continue
            except Exception as exc:
                print(f"LLM analysis failed for {paper.paper.paper_id}, using fallback: {exc}")
        analyses[paper.paper.paper_id] = fallback_analysis(paper)
    return analyses


def collect_unique_ranked_papers(topic_reports) -> list[RankedPaper]:
    by_paper_id: dict[str, RankedPaper] = {}
    for report in topic_reports:
        for ranked in report.landmark_papers + report.recent_papers:
            existing = by_paper_id.get(ranked.paper.paper_id)
            if existing is None:
                by_paper_id[ranked.paper.paper_id] = ranked
                continue
            if existing.paper.collection_kind != "landmark" and ranked.paper.collection_kind == "landmark":
                by_paper_id[ranked.paper.paper_id] = ranked
    return list(by_paper_id.values())


if __name__ == "__main__":
    raise SystemExit(main())
