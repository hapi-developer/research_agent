"""Citation agent for generating formatted citations."""
from __future__ import annotations

from typing import Any, Dict, List

from agents.base_agent import BaseAgent


class CitationAgent(BaseAgent):
    """Generates citations for sources."""

    def __init__(self) -> None:
        super().__init__(name="citation_agent")

    async def run(self, sources: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {"mla": [], "apa": [], "chicago": [], "ieee": [], "harvard": [], "bibtex": []}
