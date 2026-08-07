from dataclasses import dataclass, field
from typing import List, Optional

from core.error_categories import ErrorCategory


@dataclass
class ErrorDetail:
    category: ErrorCategory
    original: str
    corrected: str


@dataclass
class AIResponse:
    has_error: bool
    reply: str
    corrected_text: Optional[str] = None
    error_categories: List[ErrorDetail] = field(default_factory=list)
    explanation: Optional[str] = None