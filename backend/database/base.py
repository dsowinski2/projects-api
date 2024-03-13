from sqlalchemy.orm import declarative_base

from backend.config import settings

Base = declarative_base()

postgres_uri = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@localhost:5432/db"
