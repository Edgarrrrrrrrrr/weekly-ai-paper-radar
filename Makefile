PYTHON ?= python3

.PHONY: run test demo

run:
	$(PYTHON) scripts/generate_weekly_report.py --config config/pipeline.json

test:
	PYTHONPATH=src $(PYTHON) -m unittest discover -s tests -p "test_*.py"

demo:
	PYTHONPATH=src $(PYTHON) scripts/generate_weekly_report.py --config config/pipeline.json --feed-file tests/fixtures/arxiv_sample.xml --offline --today 2026-03-16
