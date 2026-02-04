"""Session persistence utilities."""
from __future__ import annotations

from typing import Dict


class SessionManager:
    """Placeholder session manager."""

    def create_session(self, user_id: str, query: str) -> Dict[str, str]:
        return {"session_id": "", "user_id": user_id, "query": query}
