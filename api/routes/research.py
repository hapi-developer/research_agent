"""Research endpoints."""
from __future__ import annotations

from fastapi import APIRouter

from api.schemas.research_request import ResearchRequest
from api.schemas.research_response import ResearchResponse

router = APIRouter()


@router.post("/start", response_model=ResearchResponse)
async def start_research(request: ResearchRequest) -> ResearchResponse:
    return ResearchResponse(session_id="", status="planning")


@router.get("/{session_id}/status", response_model=ResearchResponse)
async def get_status(session_id: str) -> ResearchResponse:
    return ResearchResponse(session_id=session_id, status="planning")


@router.get("/{session_id}/result", response_model=ResearchResponse)
async def get_result(session_id: str) -> ResearchResponse:
    return ResearchResponse(session_id=session_id, status="complete")


@router.delete("/{session_id}/cancel", response_model=ResearchResponse)
async def cancel(session_id: str) -> ResearchResponse:
    return ResearchResponse(session_id=session_id, status="cancelled")
