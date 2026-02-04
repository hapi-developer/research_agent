"""Redis caching layer."""
from __future__ import annotations

from typing import Any, Optional

import redis

from config.settings import settings


class CacheManager:
    """Multi-level cache manager."""

    def __init__(self) -> None:
        self.client = redis.from_url(settings.redis_url)

    def get(self, key: str) -> Optional[Any]:
        return self.client.get(key)

    def set(self, key: str, value: Any, ttl: int) -> None:
        self.client.set(name=key, value=value, ex=ttl)
