"""Quote extraction utilities."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Quote:
    text: str
    context_before: str
    context_after: str
    quote_start_pos: int
    quote_end_pos: int
    importance_score: float
    category: str
    relevance_to_query: str
    why_important: str
    related_concepts: List[str]


class QuoteExtractor:
    """Placeholder quote extraction implementation."""

    async def extract_quotes(self, content: str, query_context: str, max_quotes: int = 5) -> List[Quote]:
        return []
