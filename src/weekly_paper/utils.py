from __future__ import annotations

from datetime import date, datetime
import json
import re
from typing import Any


def parse_iso_datetime(value: str) -> datetime:
    normalized = value.replace("Z", "+00:00")
    return datetime.fromisoformat(normalized)


def slugify(value: str, max_length: int = 72) -> str:
    lowered = value.lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = lowered.strip("-")
    if not lowered:
        lowered = "paper"
    return lowered[:max_length].rstrip("-")


def strip_fenced_json(text: str) -> str:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
        cleaned = re.sub(r"```$", "", cleaned).strip()
    return cleaned


def safe_json_loads(text: str) -> Any:
    return json.loads(strip_fenced_json(text))


def week_folder_name(target_date: date) -> str:
    iso_year, iso_week, _ = target_date.isocalendar()
    return f"{iso_year}/week-{iso_week:02d}"


def display_date(value: datetime) -> str:
    return value.strftime("%Y-%m-%d")
