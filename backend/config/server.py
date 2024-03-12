from fastapi import FastAPI

from backend.src.api import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Projects API",
        description="Projects API docs",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        dependencies=[],
    )
    app.include_router(router, prefix="/api")
    return app


app = create_app()
