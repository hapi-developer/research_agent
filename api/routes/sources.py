"""Source management endpoints."""
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/{session_id}")
async def list_sources(session_id: str) -> dict:
    return {"session_id": session_id, "sources": []}


@router.get("/{session_id}/top10")
async def list_top_sources(session_id: str) -> dict:
    return {"session_id": session_id, "sources": []}


@router.get("/{session_id}/{source_id}")
async def get_source(session_id: str, source_id: str) -> dict:
    return {"session_id": session_id, "source_id": source_id}


@router.post("/{session_id}/{source_id}/analyze")
async def analyze_source(session_id: str, source_id: str) -> dict:
    return {"session_id": session_id, "source_id": source_id, "status": "queued"}
