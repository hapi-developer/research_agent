"""Search query optimization utilities."""
from __future__ import annotations

from typing import List


def optimize_queries(queries: List[str]) -> List[str]:
    """Deduplicate and normalize search queries."""
    seen = set()
    optimized = []
    for query in queries:
        normalized = query.strip().lower()
        if normalized and normalized not in seen:
            seen.add(normalized)
            optimized.append(query)
    return optimized
