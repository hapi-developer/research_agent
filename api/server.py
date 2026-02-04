"""FastAPI application."""
from __future__ import annotations

from fastapi import FastAPI

from api.routes import research, sources, citations, export, health


def create_app() -> FastAPI:
    app = FastAPI(title="Extreme Research Agent")
    app.include_router(research.router, prefix="/api/v1/research", tags=["research"])
    app.include_router(sources.router, prefix="/api/v1/sources", tags=["sources"])
    app.include_router(citations.router, prefix="/api/v1/citations", tags=["citations"])
    app.include_router(export.router, prefix="/api/v1/export", tags=["export"])
    app.include_router(health.router, prefix="/api/v1/health", tags=["health"])
    return app
