"""Duplicate detection utilities."""
from __future__ import annotations

from typing import List


def deduplicate(items: List[str]) -> List[str]:
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique
