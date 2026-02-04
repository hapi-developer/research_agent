"""Quote model."""
from __future__ import annotations

from sqlalchemy import Column, DateTime, Float, Integer, JSON, String, Text
from sqlalchemy.sql import func

from storage.models import Base


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(String, primary_key=True)
    source_id = Column(String, index=True)
    text = Column(Text)
    context_before = Column(Text)
    context_after = Column(Text)
    position_start = Column(Integer)
    position_end = Column(Integer)
    importance_score = Column(Float)
    category = Column(String)
    relevance_explanation = Column(Text)
    related_concepts = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
