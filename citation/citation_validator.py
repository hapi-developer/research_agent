"""Citation validation utilities."""
from __future__ import annotations

from typing import Any, Dict


def validate_metadata(metadata: Dict[str, Any]) -> bool:
    return bool(metadata.get("title") and metadata.get("url"))
