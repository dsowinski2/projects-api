import pytest
from fastapi.testclient import TestClient
from pytest_factoryboy import register
from sqlalchemy import create_engine
from sqlalchemy.engine import url
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from src.tests.factories import ProjectFactory

from backend.config import settings
from backend.config.server import app
from backend.src.models import Base

register(ProjectFactory)


url_params = {
    "drivername": "postgresql",
    "host": "postgresql-test",
    "port": 5432,
    "username": settings.TEST_POSTGRES_USER,
    "password": settings.TEST_POSTGRES_PASSWORD,
    "database": "db-test",
}
db_url = url.URL.create(**url_params)


@pytest.fixture(scope="function")
def db_session() -> Session:
    engine = create_engine(db_url)
    session = sessionmaker(engine, class_=Session, expire_on_commit=False)
    with session() as s:
        with engine.begin() as conn:
            Base.metadata.create_all(engine)
        yield s

    with engine.begin() as conn:
        Base.metadata.drop_all(bind=conn)

    engine.dispose()


@pytest.fixture(autouse=True)
def set_session_for_factories(db_session):
    ProjectFactory._meta.sqlalchemy_session = db_session


@pytest.fixture
def api_client():
    return TestClient(app)
