"""Research report model."""
from __future__ import annotations

from sqlalchemy import Column, DateTime, JSON, String, Text
from sqlalchemy.sql import func

from storage.models import Base


class ResearchReport(Base):
    __tablename__ = "research_reports"

    id = Column(String, primary_key=True)
    session_id = Column(String, index=True)
    executive_summary = Column(Text)
    full_report = Column(JSON)
    key_findings = Column(JSON)
    gaps_and_limitations = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
