from __future__ import annotations

import json
import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from weekly_paper.utils import safe_json_loads


class OpenAIJSONClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
        self.base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        self.api_style = os.getenv("OPENAI_API_STYLE", "chat_completions").strip().lower()

    @property
    def enabled(self) -> bool:
        return bool(self.api_key)

    def complete_json(self, system_prompt: str, user_prompt: str, temperature: float = 0.2) -> dict:
        if not self.enabled:
            raise RuntimeError("OPENAI_API_KEY is not configured.")

        last_error: Exception | None = None
        for style in self._style_order():
            try:
                data = self._post_by_style(style, system_prompt, user_prompt, temperature)
                return safe_json_loads(self._extract_text(data))
            except Exception as exc:
                last_error = exc

        if last_error is not None:
            raise last_error
        raise RuntimeError("No API style could be used.")

    def _style_order(self) -> list[str]:
        if self.api_style == "auto":
            return ["chat_completions", "responses"]
        if self.api_style in {"chat_completions", "responses"}:
            return [self.api_style]
        return ["chat_completions"]

    def _post_by_style(
        self,
        style: str,
        system_prompt: str,
        user_prompt: str,
        temperature: float,
    ) -> dict:
        if style == "responses":
            payload = {
                "model": self.model,
                "instructions": system_prompt,
                "input": user_prompt,
                "temperature": temperature,
                "text": {
                    "format": {
                        "type": "json_object",
                    }
                },
            }
            try:
                return self._post("responses", payload)
            except HTTPError as exc:
                if exc.code != 400:
                    raise
                payload.pop("text", None)
                return self._post("responses", payload)

        payload = {
            "model": self.model,
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "response_format": {"type": "json_object"},
        }
        try:
            return self._post("chat/completions", payload)
        except HTTPError as exc:
            if exc.code != 400:
                raise
            payload.pop("response_format", None)
            return self._post("chat/completions", payload)

    def _post(self, endpoint: str, payload: dict) -> dict:
        body = json.dumps(payload).encode("utf-8")
        request = Request(
            f"{self.base_url}/{endpoint}",
            data=body,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
        )
        with urlopen(request, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))

    def _extract_text(self, data: dict) -> str:
        if "choices" in data:
            content = data["choices"][0]["message"]["content"]
            if isinstance(content, str):
                return content
            if isinstance(content, list):
                parts = []
                for item in content:
                    if isinstance(item, dict) and "text" in item:
                        parts.append(item["text"])
                if parts:
                    return "\n".join(parts)

        output_text = data.get("output_text")
        if isinstance(output_text, str) and output_text.strip():
            return output_text

        parts: list[str] = []
        for item in data.get("output", []):
            content = item.get("content", [])
            if isinstance(content, str):
                parts.append(content)
                continue
            if not isinstance(content, list):
                continue
            for piece in content:
                if not isinstance(piece, dict):
                    continue
                text = piece.get("text")
                if isinstance(text, str):
                    parts.append(text)

        if parts:
            return "\n".join(parts)
        raise RuntimeError(f"Could not extract text from API response: {data}")
