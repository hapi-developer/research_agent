"""Citation schema."""
from __future__ import annotations

from pydantic import BaseModel


class CitationSchema(BaseModel):
    format: str
    citation_text: str
