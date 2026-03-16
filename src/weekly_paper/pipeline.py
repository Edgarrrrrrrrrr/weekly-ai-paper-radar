from __future__ import annotations

from argparse import ArgumentParser
from datetime import date, datetime, timezone
from pathlib import Path

from weekly_paper.analysis import analyze_paper, fallback_analysis, rank_with_llm
from weekly_paper.arxiv_client import fetch_recent_papers
from weekly_paper.config import load_config
from weekly_paper.openai_client import OpenAIJSONClient
from weekly_paper.ranking import annotate_papers, heuristic_rank
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

    papers = fetch_recent_papers(
        categories=config.categories,
        days_back=config.days_back,
        max_results=config.max_results,
        feed_text=feed_text,
        now=now,
    )
    annotated = annotate_papers(papers, config.topics)

    if not annotated:
        parser.error("No candidate papers were found for the configured date window.")

    heuristic_candidates, editorial = heuristic_rank(annotated, config)
    client = OpenAIJSONClient()

    ranked = heuristic_candidates[: config.max_papers]
    if client.enabled and not args.offline:
        try:
            ranked, editorial = rank_with_llm(client, heuristic_candidates, config)
        except Exception as exc:
            print(f"LLM ranking failed, using heuristic ranking instead: {exc}")

    analyses = {}
    for paper in ranked:
        if client.enabled and not args.offline:
            try:
                analyses[paper.paper.paper_id] = analyze_paper(client, paper, config.language)
                continue
            except Exception as exc:
                print(f"LLM analysis failed for {paper.paper.paper_id}, using fallback: {exc}")
        analyses[paper.paper.paper_id] = fallback_analysis(paper)

    output_dir = Path(args.output_dir)
    bundle_dir = write_report_bundle(output_dir, target_date, editorial, ranked, analyses)

    print(f"Generated report bundle at {bundle_dir}")
    return 0
