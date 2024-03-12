from backend.src.controllers.base import BaseController
from backend.src.models.projects import Project
from backend.src.repositories.projects.repo import ProjectRepository
from backend.src.utils.types import ProjectCreateType
from backend.src.utils.types import ProjectUpdateType


class ProjectsController(
    BaseController[Project, ProjectUpdateType, ProjectCreateType, ProjectRepository]
):
    pass
