"""Export endpoints."""
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.post("/{session_id}/pdf")
async def export_pdf(session_id: str) -> dict:
    return {"session_id": session_id, "status": "queued", "format": "pdf"}


@router.post("/{session_id}/docx")
async def export_docx(session_id: str) -> dict:
    return {"session_id": session_id, "status": "queued", "format": "docx"}


@router.post("/{session_id}/markdown")
async def export_markdown(session_id: str) -> dict:
    return {"session_id": session_id, "status": "queued", "format": "markdown"}
