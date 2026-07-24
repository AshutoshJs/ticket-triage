from fastapi import FastAPI

from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version="0.1.0",
        debug=settings.DEBUG,
    )

    @app.get("/health", tags=["health"])
    async def health():
        return {
            "status": "ok",
            "app": settings.APP_NAME,
            "environment": settings.ENVIRONMENT,
        }

    return app


app = create_app()