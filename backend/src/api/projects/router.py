from fastapi import APIRouter


projects_router = APIRouter()

@projects_router.get("/")
def get_projects():
    return "Hello World"