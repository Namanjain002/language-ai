from typing import Optional

from ai.base_client import AIClient
from ai.prompt_builder import build_prompt
from ai.validator import InvalidAIResponse, parse_ai_response
from core.model import AIResponse

MAX_ATTEMPTS = 2


def get_validated_response(client: AIClient, user_message: str) -> AIResponse:
    system_prompt, user_prompt = build_prompt(user_message)

    last_error: Optional[Exception] = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        raw_text = client.get_raw_response(system_prompt, user_prompt)
        try:
            return parse_ai_response(raw_text)
        except InvalidAIResponse as exc:
            last_error = exc
            print(f"[retry {attempt}/{MAX_ATTEMPTS}] invalid AI response: {exc}")

    raise InvalidAIResponse(
        f"AI response still invalid after {MAX_ATTEMPTS} attempts: {last_error}"
    )