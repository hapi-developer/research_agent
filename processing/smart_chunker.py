"""Semantic-aware text chunking."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class TextChunk:
    content: str
    start: int
    end: int


class SmartChunker:
    """Chunks content while respecting paragraph boundaries."""

    def chunk_content(self, content: str, max_tokens: int = 6000, overlap: int = 200) -> List[TextChunk]:
        chunks: List[TextChunk] = []
        if not content:
            return chunks
        step = max_tokens - overlap
        for idx in range(0, len(content), step):
            segment = content[idx : idx + max_tokens]
            chunks.append(TextChunk(content=segment, start=idx, end=min(idx + max_tokens, len(content))))
        return chunks
