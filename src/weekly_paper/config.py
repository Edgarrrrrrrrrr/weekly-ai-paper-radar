from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class TopicConfig:
    name: str
    slug: str
    keywords: list[str]


@dataclass(frozen=True)
class PipelineConfig:
    days_back: int
    max_results: int
    candidate_pool: int
    max_papers: int
    language: str
    categories: list[str]
    topics: list[TopicConfig]


def load_config(path: str | Path) -> PipelineConfig:
    config_path = Path(path)
    raw = json.loads(config_path.read_text(encoding="utf-8"))
    topics = [TopicConfig(**topic) for topic in raw["topics"]]
    return PipelineConfig(
        days_back=raw["days_back"],
        max_results=raw["max_results"],
        candidate_pool=raw["candidate_pool"],
        max_papers=raw["max_papers"],
        language=raw["language"],
        categories=raw["categories"],
        topics=topics,
    )
