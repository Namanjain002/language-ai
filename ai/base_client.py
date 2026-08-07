from abc import ABC, abstractmethod


class AIClient(ABC):
    @abstractmethod
    def get_raw_response(self, system_prompt: str, user_message: str) -> str:
        raise NotImplementedError