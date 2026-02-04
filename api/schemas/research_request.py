"""Research request schema."""
from __future__ import annotations

from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    user_id: str = Field(default="anonymous")
    preferences: dict = Field(default_factory=dict)
