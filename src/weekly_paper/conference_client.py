from __future__ import annotations

from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import re
from urllib.parse import quote, urljoin
from urllib.request import urlopen

from weekly_paper.config import ConferenceSourceConfig
from weekly_paper.models import Paper


def fetch_conference_papers(
    sources: list[ConferenceSourceConfig],
    fixture_dir: str = "",
) -> list[Paper]:
    papers: list[Paper] = []
    for source in sources:
        try:
            if source.type == "openreview":
                papers.extend(fetch_openreview_papers(source, fixture_dir=fixture_dir))
            elif source.type == "cvf":
                papers.extend(fetch_cvf_papers(source, fixture_dir=fixture_dir))
        except Exception as exc:
            print(f"Conference source fetch failed for {source.name} {source.year}: {exc}")
    return papers


def fetch_openreview_papers(source: ConferenceSourceConfig, fixture_dir: str = "") -> list[Paper]:
    if fixture_dir:
        fixture_path = f"{fixture_dir}/{source.name.lower()}_{source.year}.json"
        with open(fixture_path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
        return parse_openreview_notes(payload, source)

    offset = 0
    limit = 1000
    all_notes: list[dict] = []

    while True:
        invitation = quote(source.invitation, safe="")
        url = f"{source.base_url}/notes?invitation={invitation}&limit={limit}&offset={offset}"
        with urlopen(url, timeout=60) as response:
            payload = json.loads(response.read().decode("utf-8"))
        notes = payload.get("notes", [])
        all_notes.extend(notes)
        if len(notes) < limit:
            break
        offset += limit

    return parse_openreview_notes({"notes": all_notes}, source)


def parse_openreview_notes(payload: dict, source: ConferenceSourceConfig) -> list[Paper]:
    papers: list[Paper] = []
    for note in payload.get("notes", []):
        content = note.get("content", {})
        title = extract_openreview_field(content, "title")
        if not title:
            continue

        venue = extract_openreview_field(content, "venue")
        if "withdraw" in venue.lower():
            continue
        if venue and str(source.year) not in venue:
            continue

        paper_id = note.get("forum") or note.get("id", title)
        abstract = extract_openreview_field(content, "abstract")
        authors = extract_openreview_list(content, "authors")
        paper_time = datetime.fromtimestamp(note.get("cdate", 0) / 1000, tz=timezone.utc)
        if paper_time.year < 2000:
            paper_time = datetime(source.year, 1, 1, tzinfo=timezone.utc)

        papers.append(
            Paper(
                paper_id=paper_id,
                source=source.name,
                venue=venue or f"{source.name} {source.year}",
                title=title,
                abstract=abstract,
                authors=authors,
                categories=[],
                published=paper_time,
                updated=paper_time,
                abs_url=f"https://openreview.net/forum?id={paper_id}",
                pdf_url=f"https://openreview.net/pdf?id={paper_id}",
                published_label=str(source.year),
            )
        )
    return papers


def fetch_cvf_papers(source: ConferenceSourceConfig, fixture_dir: str = "") -> list[Paper]:
    if fixture_dir:
        fixture_path = f"{fixture_dir}/{source.name.lower()}_{source.year}.html"
        with open(fixture_path, "r", encoding="utf-8") as handle:
            html = handle.read()
    else:
        urls = [source.all_papers_url]
        if source.all_papers_url.endswith(".py?day=all"):
            urls.append(source.all_papers_url.replace(".py?day=all", "?day=all"))
        elif source.all_papers_url.endswith("?day=all"):
            urls.append(source.all_papers_url.replace("?day=all", ".py?day=all"))

        html = ""
        last_error: Exception | None = None
        for url in urls:
            try:
                with urlopen(url, timeout=60) as response:
                    html = response.read().decode("utf-8", errors="ignore")
                break
            except Exception as exc:
                last_error = exc
        if not html and last_error is not None:
            raise last_error

    parser = CVFAllPapersParser(base_url=source.base_url)
    parser.feed(html)
    return parser.to_papers(source)


class CVFAllPapersParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.in_dt = False
        self.capture_title = False
        self.capture_authors = False
        self.current_link = ""
        self.current_title = ""
        self.current_authors = ""
        self.entries: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        attr_map = dict(attrs)
        if tag == "dt":
            self.in_dt = True
            self.current_link = ""
            self.current_title = ""
            self.current_authors = ""
        if self.in_dt and tag == "a":
            href = attr_map.get("href", "")
            if "/html/" in href:
                self.current_link = href
                self.capture_title = True
            elif "author" in href.lower():
                self.capture_authors = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "dt":
            self.in_dt = False
            if self.current_link and self.current_title:
                self.entries.append(
                    {
                        "title": normalize_space(self.current_title),
                        "authors": normalize_space(self.current_authors),
                        "link": self.current_link,
                    }
                )
        if tag == "a":
            self.capture_title = False
            self.capture_authors = False

    def handle_data(self, data: str) -> None:
        if self.capture_title:
            self.current_title += data
        elif self.capture_authors:
            self.current_authors += data

    def to_papers(self, source: ConferenceSourceConfig) -> list[Paper]:
        papers: list[Paper] = []
        published = datetime(source.year, 1, 1, tzinfo=timezone.utc)
        for entry in self.entries:
            title = entry["title"]
            if not title:
                continue
            abs_url = urljoin(self.base_url, entry["link"])
            pdf_url = re.sub(r"/html/", "/papers/", abs_url)
            pdf_url = re.sub(r"\.html$", ".pdf", pdf_url)
            slug = entry["link"].rsplit("/", 1)[-1].replace(".html", "")
            authors = [item.strip() for item in entry["authors"].split(",") if item.strip()]
            papers.append(
                Paper(
                    paper_id=f"{source.name.lower()}-{source.year}-{slug}",
                    source=source.name,
                    venue=f"{source.name} {source.year}",
                    title=title,
                    abstract=title,
                    authors=authors,
                    categories=[],
                    published=published,
                    updated=published,
                    abs_url=abs_url,
                    pdf_url=pdf_url,
                    published_label=str(source.year),
                )
            )
        return papers


def extract_openreview_field(content: dict, key: str) -> str:
    value = content.get(key, "")
    if isinstance(value, dict):
        inner = value.get("value", "")
        if isinstance(inner, list):
            return ", ".join(str(item) for item in inner)
        return str(inner)
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def extract_openreview_list(content: dict, key: str) -> list[str]:
    value = content.get(key, [])
    if isinstance(value, dict):
        inner = value.get("value", [])
        if isinstance(inner, list):
            return [str(item) for item in inner]
        return [str(inner)]
    if isinstance(value, list):
        return [str(item) for item in value]
    if value:
        return [str(value)]
    return []


def normalize_space(value: str) -> str:
    return " ".join(value.split())
