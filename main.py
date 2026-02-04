"""Application entry point for the Extreme Research Agent."""
from api.server import create_app

app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
