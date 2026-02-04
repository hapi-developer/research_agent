"""Base formatter interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseFormatter(ABC):
    """Base class for citation formatters."""

    @abstractmethod
    def format(self, metadata: Dict[str, Any]) -> str:
        raise NotImplementedError
