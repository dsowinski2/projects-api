from backend.src.models.projects import Project
from backend.src.repositories.base import BaseRepository
from backend.src.utils.types import ProjectCreateType, ProjectUpdateType


class ProjectRepository(BaseRepository[Project, ProjectUpdateType, ProjectCreateType]):
    model = Project
    pass