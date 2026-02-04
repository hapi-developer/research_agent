"""Citation formatter implementation."""
from __future__ import annotations

from typing import Any, Dict

from citation.formatters.base_formatter import BaseFormatter


class MLAFormatter(BaseFormatter):
    """Placeholder MLA formatter."""

    def format(self, metadata: Dict[str, Any]) -> str:
        return ""
