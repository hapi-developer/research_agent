"""Source schema."""
from __future__ import annotations

from pydantic import BaseModel


class SourceSchema(BaseModel):
    id: str
    url: str
    title: str | None = None
