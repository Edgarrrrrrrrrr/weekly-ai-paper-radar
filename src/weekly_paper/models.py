from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Paper:
    paper_id: str
    source: str
    title: str
    abstract: str
    authors: list[str]
    categories: list[str]
    published: datetime
    updated: datetime
    abs_url: str
    pdf_url: str
    matched_topics: list[str] = field(default_factory=list)
    keyword_score: float = 0.0


@dataclass
class RankedPaper:
    paper: Paper
    rank: int
    importance_score: int
    why_now: str
    direction_fit: str


@dataclass
class WeeklyEditorial:
    headline: str
    overview: str
    trend_signals: list[str]
    watchlist: list[str]


@dataclass
class PaperAnalysis:
    title_zh: str
    tagline: str
    importance: str
    core_innovation: str
    technical_takeaways: list[str]
    applications: list[str]
    limitations: list[str]
    who_should_read: list[str]
    follow_ups: list[str]
    one_line: str
