"""Factory for selecting appropriate scraper."""
from __future__ import annotations

from typing import Optional

from scrapers.base_scraper import BaseScraper
from scrapers.general_web_scraper import GeneralWebScraper
from scrapers.pdf_scraper import PDFScraper
from scrapers.academic_paper_scraper import AcademicPaperScraper
from scrapers.news_article_scraper import NewsArticleScraper
from scrapers.javascript_scraper import JavaScriptScraper


class ScraperFactory:
    """Selects the best scraper based on URL and content type."""

    def get_scraper(self, url: str, content_type: Optional[str] = None) -> BaseScraper:
        if url.endswith(".pdf") or content_type == "application/pdf":
            return PDFScraper()
        if "arxiv" in url or "doi" in url:
            return AcademicPaperScraper()
        if "news" in url:
            return NewsArticleScraper()
        if "javascript" in (content_type or ""):
            return JavaScriptScraper()
        return GeneralWebScraper()
