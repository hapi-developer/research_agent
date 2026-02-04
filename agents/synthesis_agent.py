"""Synthesis agent for final report generation."""
from __future__ import annotations

from typing import Any, Dict

from agents.base_agent import BaseAgent
from agents.master_agent import QueryAnalysis


class SynthesisAgent(BaseAgent):
    """Synthesizes analysis into a final report."""

    def __init__(self) -> None:
        super().__init__(name="synthesis_agent")

    async def run(self, analysis_results: Dict[str, Any], analysis: QueryAnalysis) -> Dict[str, Any]:
        return {
            "executive_summary": "",
            "key_findings": [],
            "thematic_sections": [],
            "contradictions_and_debates": [],
            "gaps_and_limitations": [],
            "conclusion": "",
            "confidence_assessment": "",
            "suggested_further_reading": [],
        }
