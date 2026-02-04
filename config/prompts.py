"""Prompt templates for LLM interactions."""

QUERY_ANALYSIS_PROMPT = """
You are an elite research strategist with expertise across all academic disciplines.

TASK: Analyze this research query and create a comprehensive research plan.

QUERY: {user_query}

Provide your analysis in JSON as described in the system prompt.
""".strip()

SOURCE_EVALUATION_PROMPT = """
You are an expert research librarian evaluating source quality.

RESEARCH CONTEXT:
Query: {query}
Key Concepts: {concepts}
Required Coverage: {sub_questions}

SOURCE TO EVALUATE:
Title: {title}
URL: {url}
Content Preview: {preview}
Metadata: {metadata}

Return JSON with evaluation fields.
""".strip()

QUOTE_EXTRACTION_PROMPT = """
You are an expert at identifying the most important and relevant quotes from source material.

RESEARCH CONTEXT:
Query: {query}
Source Title: {title}
Source Type: {type}

CONTENT:
{content_chunk}

Return JSON with up to 5 quotes.
""".strip()

SUMMARY_PROMPT = """
You are a professional research analyst creating source summaries.

SOURCE:
Title: {title}
URL: {url}
Full Content: {content}

RESEARCH CONTEXT:
Query: {query}
Key Questions: {sub_questions}

Return JSON with summary fields.
""".strip()

SYNTHESIS_PROMPT = """
You are a senior research analyst synthesizing research findings into a comprehensive report.

RESEARCH QUERY: {original_query}
SUB-QUESTIONS ADDRESSED:
{sub_questions}
ANALYZED SOURCES:
{source_summaries_and_quotes}

Return JSON with report fields.
""".strip()
