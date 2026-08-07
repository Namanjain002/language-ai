import json

from core.error_categories import ErrorCategory
from core.model import AIResponse, ErrorDetail


class InvalidAIResponse(Exception):
    """Raised when the AI's response is malformed or incomplete."""


def parse_ai_response(raw_text: str) -> AIResponse:
    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise InvalidAIResponse(f"Not valid JSON: {exc}") from exc

    if "has_error" not in data or "reply" not in data:
        raise InvalidAIResponse("Missing required fields: has_error/reply")

    has_error = data["has_error"]
    if has_error:
        required = ("corrected_text", "explanation", "error_categories")
        missing = [f for f in required if not data.get(f)]
        if missing:
            raise InvalidAIResponse(f"has_error=True but missing: {missing}")

    details = [_parse_error_detail(item) for item in data.get("error_categories", [])]
    return AIResponse(
        has_error=has_error,
        reply=data["reply"],
        corrected_text=data.get("corrected_text"),
        error_categories=details,
        explanation=data.get("explanation"),
    )


def _parse_error_detail(item: dict) -> ErrorDetail:
    try:
        category = ErrorCategory(item["category"])
    except (KeyError, ValueError) as exc:
        raise InvalidAIResponse(f"Bad error_categories entry: {item}") from exc
    return ErrorDetail(category=category, original=item["original"], corrected=item["corrected"])