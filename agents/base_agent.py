"""Abstract base class for all agents."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseAgent(ABC):
    """Defines the interface for all research agents."""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    async def run(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """Execute the agent's primary workflow."""
        raise NotImplementedError
