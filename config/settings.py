"""Centralized configuration management."""
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    google_search_api_key: str = Field(default="", alias="GOOGLE_SEARCH_API_KEY")
    google_cse_id: str = Field(default="", alias="GOOGLE_CSE_ID")
    bing_search_api_key: str = Field(default="", alias="BING_SEARCH_API_KEY")
    brave_search_api_key: str = Field(default="", alias="BRAVE_SEARCH_API_KEY")
    serper_api_key: str = Field(default="", alias="SERPER_API_KEY")

    database_url: str = Field(
        default="postgresql://user:pass@localhost:5432/research_agent",
        alias="DATABASE_URL",
    )
    redis_url: str = Field(default="redis://localhost:6379", alias="REDIS_URL")
    environment: str = Field(default="development", alias="ENVIRONMENT")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    max_concurrent_scrapes: int = Field(default=20, alias="MAX_CONCURRENT_SCRAPES")
    enable_cache: bool = Field(default=True, alias="ENABLE_CACHE")


settings = Settings()
