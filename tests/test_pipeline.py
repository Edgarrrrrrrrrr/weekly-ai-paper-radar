from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from weekly_paper.arxiv_client import fetch_recent_papers
from weekly_paper.analysis import fallback_analysis
from weekly_paper.config import load_config
from weekly_paper.pipeline import build_landmark_rankings
from weekly_paper.ranking import annotate_papers, build_topic_reports, build_weekly_editorial
from weekly_paper.reporting import write_report_bundle


class PipelineTestCase(unittest.TestCase):
    def test_fixture_feed_produces_bundle(self) -> None:
        config = load_config(ROOT / "config/pipeline.json")
        feed_text = (ROOT / "tests/fixtures/arxiv_sample.xml").read_text(encoding="utf-8")
        now = datetime(2026, 3, 16, tzinfo=timezone.utc)

        papers = fetch_recent_papers(
            categories=config.categories,
            days_back=config.days_back,
            max_results=config.max_results,
            feed_text=feed_text,
            now=now,
        )
        self.assertEqual(len(papers), 3)

        annotated = annotate_papers(papers, config.topics)
        self.assertEqual(len(annotated), 3)

        _, landmarks = build_landmark_rankings(config)
        topic_reports = build_topic_reports(config, landmarks, annotated)
        editorial = build_weekly_editorial(topic_reports, now=now)
        analyses = {}
        for report in topic_reports:
            for item in report.landmark_papers + report.recent_papers:
                analyses[item.paper.paper_id] = fallback_analysis(item)

        with tempfile.TemporaryDirectory() as tmp_dir:
            output_root = Path(tmp_dir) / "reports"
            bundle_dir = write_report_bundle(output_root, now.date(), editorial, topic_reports, analyses)
            self.assertTrue((bundle_dir / "README.md").exists())
            self.assertTrue((bundle_dir / "manifest.json").exists())
            paper_files = sorted((bundle_dir / "papers").glob("*.md"))
            self.assertGreaterEqual(len(paper_files), 6)
            repo_readme = Path(tmp_dir) / "README.md"
            self.assertTrue(repo_readme.exists())
            content = repo_readme.read_text(encoding="utf-8")
            self.assertIn("长期重要论文", content)
            self.assertIn("Agentic AI", content)
            self.assertIn("文生图 + Agentic AI", content)
            self.assertIn("文生视频 + Agentic AI", content)


if __name__ == "__main__":
    unittest.main()
