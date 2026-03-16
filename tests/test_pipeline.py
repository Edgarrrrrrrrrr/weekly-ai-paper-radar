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
from weekly_paper.ranking import annotate_papers, heuristic_rank
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

        ranked, editorial = heuristic_rank(annotated, config)
        analyses = {
            item.paper.paper_id: fallback_analysis(item)
            for item in ranked
        }

        with tempfile.TemporaryDirectory() as tmp_dir:
            bundle_dir = write_report_bundle(Path(tmp_dir), now.date(), editorial, ranked, analyses)
            self.assertTrue((bundle_dir / "README.md").exists())
            self.assertTrue((bundle_dir / "manifest.json").exists())
            paper_files = sorted((bundle_dir / "papers").glob("*.md"))
            self.assertEqual(len(paper_files), len(ranked))


if __name__ == "__main__":
    unittest.main()
