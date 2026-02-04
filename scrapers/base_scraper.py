"""Abstract scraper with retry logic."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseScraper(ABC):
    """Base class for all scrapers."""

    @abstractmethod
    async def extract_content(self, url: str) -> Dict[str, Any]:
        raise NotImplementedError
