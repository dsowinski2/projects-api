from fastapi import APIRouter
from .projects.router import projects_router

router = APIRouter()
router.include_router(projects_router,prefix="/projects")

__all__ = ["router"]