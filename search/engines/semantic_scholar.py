"""Search engine client."""
from __future__ import annotations

from typing import Any, Dict, List

from search.base_search import BaseSearchEngine


class SearchEngine(BaseSearchEngine):
    """Placeholder search engine client."""

    async def search(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        return []
