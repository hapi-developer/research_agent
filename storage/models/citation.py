"""Citation model."""
from __future__ import annotations

from sqlalchemy import Column, DateTime, JSON, String, Text
from sqlalchemy.sql import func

from storage.models import Base


class Citation(Base):
    __tablename__ = "citations"

    id = Column(String, primary_key=True)
    source_id = Column(String, index=True)
    format = Column(String)
    citation_text = Column(Text)
    in_text_key = Column(String)
    metadata = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
