from .projects import Project
from backend.database.base import Base

Base.metadata._add_table(name="project", schema=None, table=Project.__table__)
