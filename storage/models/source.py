"""Source model."""
from __future__ import annotations

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, JSON, String, Text
from sqlalchemy.sql import func

from storage.models import Base


class Source(Base):
    __tablename__ = "sources"

    id = Column(String, primary_key=True)
    session_id = Column(String, index=True)
    url = Column(Text, index=True)
    title = Column(Text)
    content = Column(Text)
    content_hash = Column(String, index=True)
    metadata = Column(JSON)
    search_score = Column(Float)
    relevance_score = Column(Float)
    quality_score = Column(Float)
    final_score = Column(Float)
    is_top_10 = Column(Boolean, default=False, index=True)
    rank = Column(Integer)
    scrape_status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
