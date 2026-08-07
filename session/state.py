from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple

from core.error_categories import ErrorCategory
from core.model import AIResponse


class ChatSession:
    def __init__(self) -> None:
        self.history: List[Tuple[str, AIResponse]] = []
        self.error_tally: Dict[ErrorCategory, int] = defaultdict(int)
        self.last_activity: datetime = datetime.now()

    def record(self, user_message: str, response: AIResponse) -> None:
        self.history.append((user_message, response))
        self.last_activity = datetime.now()

        if response.has_error:
            for detail in response.error_categories:
                self.error_tally[detail.category] += 1

    def seconds_since_last_activity(self) -> float:
        return (datetime.now() - self.last_activity).total_seconds()