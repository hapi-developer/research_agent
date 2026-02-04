"""Research session model."""
from __future__ import annotations

from sqlalchemy import Column, DateTime, String, Text, JSON
from sqlalchemy.sql import func

from storage.models import Base


class ResearchSession(Base):
    __tablename__ = "research_sessions"

    id = Column(String, primary_key=True)
    user_id = Column(String, index=True)
    query = Column(Text)
    query_analysis = Column(JSON)
    strategy = Column(JSON)
    status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    completed_at = Column(DateTime(timezone=True))
    metadata = Column(JSON)
