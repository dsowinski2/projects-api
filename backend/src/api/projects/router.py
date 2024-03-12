from typing import List
from fastapi import APIRouter, Depends
from backend.database.session import db_session
from sqlalchemy.orm import Session
from backend.src.controllers.projects import ProjectsController

from backend.src.repositories.projects.repo import ProjectRepository
from backend.src.utils.types import ProjectCreateType, ProjectType, ProjectUpdateType

projects_router = APIRouter()

def controler_builder(session: Session = Depends(db_session)):
    repository = ProjectRepository(session=session)
    controller = ProjectsController(repository=repository, data_model=ProjectType)
    return controller

@projects_router.get("/")
def get_projects(controller: ProjectsController = Depends(controler_builder)) -> List[ProjectType]:
    return controller.list_objects()

@projects_router.get("/{project_id}")
def get_project(project_id, controller: ProjectsController = Depends(controler_builder)):
    return controller.get_object_by_id(id=project_id)

@projects_router.post("/")
def create_project(project_data: ProjectCreateType, controller: ProjectsController = Depends(controler_builder)):
    return controller.create_object(data=project_data)

@projects_router.patch("/{project_id}")
def patch_project(project_id, project_data: ProjectUpdateType, controller: ProjectsController = Depends(controler_builder)):
    return controller.update_object(id=project_id, data=project_data)

@projects_router.delete("/{project_id}")
def delete_project(project_id, controller: ProjectsController = Depends(controler_builder)):
    return controller.delete_object(id=project_id)
