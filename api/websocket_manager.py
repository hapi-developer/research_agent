"""WebSocket connection management."""
from __future__ import annotations

from typing import Any, Dict


class WebSocketManager:
    """Manages websocket message formatting."""

    async def send_thought_log(self, session_id: str, message: str, level: str = "info", metadata: Dict[str, Any] | None = None) -> None:
        _ = {
            "type": "thought_log",
            "session_id": session_id,
            "message": message,
            "level": level,
            "metadata": metadata or {},
        }

    async def send_progress_update(self, session_id: str, phase: str, progress: float, message: str) -> None:
        _ = {
            "type": "progress_update",
            "session_id": session_id,
            "phase": phase,
            "progress": progress,
            "message": message,
        }
