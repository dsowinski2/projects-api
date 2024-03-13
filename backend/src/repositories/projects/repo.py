from backend.src.models import Project
from backend.src.repositories.base import BaseRepository
from backend.src.utils.types import ProjectCreateType
from backend.src.utils.types import ProjectUpdateType


class ProjectRepository(BaseRepository[Project, ProjectUpdateType, ProjectCreateType]):
    model = Project
    pass
