from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Iterable
from urllib.parse import urlencode
from urllib.request import urlopen
import xml.etree.ElementTree as ET

from weekly_paper.models import Paper
from weekly_paper.utils import parse_iso_datetime

ARXIV_ENDPOINT = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def build_query(categories: Iterable[str]) -> str:
    return " OR ".join(f"cat:{category}" for category in categories)


def load_feed(search_query: str, max_results: int, feed_text: str | None = None) -> str:
    if feed_text is not None:
        return feed_text

    params = {
        "search_query": search_query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_ENDPOINT}?{urlencode(params)}"
    with urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_arxiv_feed(feed_text: str) -> list[Paper]:
    root = ET.fromstring(feed_text)
    papers: list[Paper] = []

    for entry in root.findall("atom:entry", ATOM_NS):
        paper_id_url = _read_text(entry, "atom:id")
        paper_id = paper_id_url.rsplit("/", 1)[-1]
        title = _normalize_text(_read_text(entry, "atom:title"))
        abstract = _normalize_text(_read_text(entry, "atom:summary"))
        authors = [
            _normalize_text(author.findtext("atom:name", default="", namespaces=ATOM_NS))
            for author in entry.findall("atom:author", ATOM_NS)
        ]
        categories = [item.attrib["term"] for item in entry.findall("atom:category", ATOM_NS)]
        published = parse_iso_datetime(_read_text(entry, "atom:published"))
        updated = parse_iso_datetime(_read_text(entry, "atom:updated"))

        pdf_url = ""
        for link in entry.findall("atom:link", ATOM_NS):
            if link.attrib.get("title") == "pdf":
                pdf_url = link.attrib.get("href", "")
                break

        if not pdf_url:
            pdf_url = paper_id_url.replace("/abs/", "/pdf/") + ".pdf"

        papers.append(
            Paper(
                paper_id=paper_id,
                source="arXiv",
                title=title,
                abstract=abstract,
                authors=authors,
                categories=categories,
                published=published,
                updated=updated,
                abs_url=paper_id_url,
                pdf_url=pdf_url,
            )
        )

    return papers


def fetch_recent_papers(
    categories: list[str],
    days_back: int,
    max_results: int,
    feed_text: str | None = None,
    now: datetime | None = None,
) -> list[Paper]:
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days_back)
    query = build_query(categories)
    papers = parse_arxiv_feed(load_feed(query, max_results=max_results, feed_text=feed_text))
    return [paper for paper in papers if paper.published >= cutoff]


def _read_text(entry: ET.Element, path: str) -> str:
    value = entry.findtext(path, namespaces=ATOM_NS)
    if value is None:
        return ""
    return value


def _normalize_text(value: str) -> str:
    return " ".join(value.split())
