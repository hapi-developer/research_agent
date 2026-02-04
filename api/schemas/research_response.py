"""Research response schema."""
from __future__ import annotations

from pydantic import BaseModel


class ResearchResponse(BaseModel):
    session_id: str
    status: str
