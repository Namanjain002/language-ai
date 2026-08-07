import os
from typing import Optional

from openai import OpenAI

from ai.base_client import AIClient


class OpenAIClient(AIClient):
    def __init__(self, model: str = "gpt-4o-mini", api_key: Optional[str] = None):
        self._client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))
        self._model = model

    def get_raw_response(self, system_prompt: str, user_message: str) -> str:
        completion = self._client.chat.completions.create(
            model=self._model,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        return completion.choices[0].message.content