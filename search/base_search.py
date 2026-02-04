"""Abstract search engine interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseSearchEngine(ABC):
    """Defines the interface for search engines."""

    @abstractmethod
    async def search(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        raise NotImplementedError
