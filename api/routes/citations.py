"""Citation endpoints."""
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/{session_id}")
async def list_citations(session_id: str) -> dict:
    return {"session_id": session_id, "citations": {}}


@router.get("/{session_id}/{format}")
async def list_citations_by_format(session_id: str, format: str) -> dict:
    return {"session_id": session_id, "format": format, "citations": []}


@router.post("/{session_id}/export")
async def export_citations(session_id: str) -> dict:
    return {"session_id": session_id, "status": "queued"}
