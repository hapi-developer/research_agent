"""Coordinates multi-engine search workflows."""
from __future__ import annotations

from typing import Any, Dict, List

from search.base_search import BaseSearchEngine


class MultiSearchOrchestrator:
    """Executes parallel searches across configured engines."""

    def __init__(self, engines: List[BaseSearchEngine]) -> None:
        self.engines = engines

    async def execute_comprehensive_search(self, queries: List[str], target_total: int = 40) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        for query in queries:
            for engine in self.engines:
                results.extend(await engine.search(query))
        return results[:target_total]
