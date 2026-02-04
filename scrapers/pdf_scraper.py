"""Specialized scraper."""
from __future__ import annotations

from typing import Any, Dict

from scrapers.base_scraper import BaseScraper


class PDFScraper(BaseScraper):
    """Placeholder PDF scraper implementation."""

    async def extract_content(self, url: str) -> Dict[str, Any]:
        return {
            "url": url,
            "title": None,
            "content": "",
            "metadata": {},
            "success": False,
            "error": "not_implemented",
        }
