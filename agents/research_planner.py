"""Research planner agent."""
from __future__ import annotations

from typing import Any, Dict, List

from agents.base_agent import BaseAgent
from agents.master_agent import QueryAnalysis, ResearchStrategy
from config.constants import DEFAULT_TARGET_SOURCES


class ResearchPlanner(BaseAgent):
    """Agent responsible for query expansion and strategy development."""

    def __init__(self) -> None:
        super().__init__(name="research_planner")

    async def run(self, query: str) -> QueryAnalysis:
        return QueryAnalysis(
            core_question=query,
            research_type="exploratory",
            complexity_level="moderate",
            sub_questions=[],
            key_concepts=[],
            entities={"people": [], "organizations": [], "locations": [], "events": []},
            temporal_requirements={"requires_current_info": True, "date_range": None, "historical_context_needed": True},
            expected_source_types=[],
            disciplines=[],
            estimated_scope="40 sources",
            special_considerations=[],
        )

    async def develop_strategy(self, query: str, analysis: QueryAnalysis) -> ResearchStrategy:
        return ResearchStrategy(
            search_queries=self.generate_search_queries(query),
            source_targets=DEFAULT_TARGET_SOURCES,
            quality_threshold=0.7,
        )

    def generate_search_queries(self, query: str) -> List[str]:
        return [query, f"{query} latest research", f"{query} analysis"]
