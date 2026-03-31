from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class LandmarkPaperConfig:
    paper_id: str
    title: str
    abs_url: str
    pdf_url: str
    published_label: str
    authors: list[str]
    summary: str
    rationale: str


@dataclass(frozen=True)
class ConferenceSourceConfig:
    name: str
    type: str
    year: int
    base_url: str
    invitation: str = ""
    all_papers_url: str = ""


@dataclass(frozen=True)
class TopicConfig:
    name: str
    name_zh: str
    slug: str
    keyword_groups: list[list[str]]
    landmarks: list[LandmarkPaperConfig]


@dataclass(frozen=True)
class PipelineConfig:
    days_back: int
    max_results: int
    recent_papers_per_topic: int
    language: str
    categories: list[str]
    conference_sources: list[ConferenceSourceConfig]
    topics: list[TopicConfig]


def load_config(path: str | Path) -> PipelineConfig:
    config_path = Path(path)
    raw = json.loads(config_path.read_text(encoding="utf-8"))
    topics = [
        TopicConfig(
            name=topic["name"],
            name_zh=topic["name_zh"],
            slug=topic["slug"],
            keyword_groups=topic["keyword_groups"],
            landmarks=[LandmarkPaperConfig(**item) for item in topic["landmarks"]],
        )
        for topic in raw["topics"]
    ]
    conference_sources = [ConferenceSourceConfig(**item) for item in raw.get("conference_sources", [])]
    return PipelineConfig(
        days_back=raw["days_back"],
        max_results=raw["max_results"],
        recent_papers_per_topic=raw["recent_papers_per_topic"],
        language=raw["language"],
        categories=raw["categories"],
        conference_sources=conference_sources,
        topics=topics,
    )
