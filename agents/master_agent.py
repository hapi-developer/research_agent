"""Master Research Agent orchestrating the full workflow."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from agents.base_agent import BaseAgent
from agents.research_planner import ResearchPlanner
from agents.source_evaluator import SourceEvaluator
from agents.content_analyzer import ContentAnalyzer
from agents.synthesis_agent import SynthesisAgent
from agents.citation_agent import CitationAgent
from config.constants import DEFAULT_TOP_SOURCES


@dataclass
class QueryAnalysis:
    core_question: str
    research_type: str
    complexity_level: str
    sub_questions: List[Dict[str, Any]]
    key_concepts: List[Dict[str, Any]]
    entities: Dict[str, List[str]]
    temporal_requirements: Dict[str, Any]
    expected_source_types: List[Dict[str, Any]]
    disciplines: List[str]
    estimated_scope: str
    special_considerations: List[str]


@dataclass
class ResearchStrategy:
    search_queries: List[str]
    source_targets: int
    quality_threshold: float


class MasterResearchAgent(BaseAgent):
    """Supreme orchestrator of the research lifecycle."""

    def __init__(self) -> None:
        super().__init__(name="master_agent")
        self.research_planner = ResearchPlanner()
        self.source_evaluator = SourceEvaluator()
        self.content_analyzer = ContentAnalyzer()
        self.synthesis_agent = SynthesisAgent()
        self.citation_agent = CitationAgent()

    async def run(self, query: str, user_id: str, preferences: Dict[str, Any]) -> Dict[str, Any]:
        analysis = await self.analyze_query(query)
        strategy = await self.develop_strategy(query, analysis)
        await self.stream_thought("Executing multi-phase search", "info", {"phase": "search"})
        raw_sources: List[Dict[str, Any]] = []
        top_sources = await self.select_top_sources(raw_sources, analysis, DEFAULT_TOP_SOURCES)
        detailed_analysis = await self.deep_analyze_sources(top_sources, analysis)
        report = await self.synthesize_report(detailed_analysis, analysis)
        citations = await self.citation_agent.run(top_sources)
        return {
            "analysis": analysis,
            "strategy": strategy,
            "sources": top_sources,
            "detailed_analysis": detailed_analysis,
            "report": report,
            "citations": citations,
        }

    async def analyze_query(self, query: str) -> QueryAnalysis:
        await self.stream_thought("Analyzing query", "info", {"query": query})
        return await self.research_planner.run(query)

    async def develop_strategy(self, query: str, analysis: QueryAnalysis) -> ResearchStrategy:
        await self.stream_thought("Developing strategy", "info", {"query": query})
        return await self.research_planner.develop_strategy(query, analysis)

    async def select_top_sources(
        self,
        candidates: List[Dict[str, Any]],
        analysis: QueryAnalysis,
        n: int = DEFAULT_TOP_SOURCES,
    ) -> List[Dict[str, Any]]:
        await self.stream_thought("Selecting top sources", "info", {"candidate_count": len(candidates)})
        return await self.source_evaluator.select_top_sources(candidates, analysis, n)

    async def deep_analyze_sources(
        self,
        sources: List[Dict[str, Any]],
        analysis: QueryAnalysis,
    ) -> Dict[str, Any]:
        await self.stream_thought("Deep analyzing sources", "info", {"source_count": len(sources)})
        return await self.content_analyzer.run(sources, analysis)

    async def synthesize_report(
        self,
        analysis_results: Dict[str, Any],
        analysis: QueryAnalysis,
    ) -> Dict[str, Any]:
        await self.stream_thought("Synthesizing report", "info", {"phase": "synthesis"})
        return await self.synthesis_agent.run(analysis_results, analysis)

    async def stream_thought(self, message: str, level: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        _ = {
            "message": message,
            "level": level,
            "metadata": metadata or {},
        }
