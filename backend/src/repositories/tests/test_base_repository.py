import json
from datetime import datetime

import pytest

from backend.src.models import Project
from backend.src.repositories.excepions import ObjectNotFoundException
from backend.src.repositories.projects.repo import ProjectRepository
from backend.src.utils.types import ProjectCreateType
from backend.src.utils.types import ProjectUpdateType


pytestmark = pytest.mark.usefixtures("db_session")


@pytest.fixture()
def projects_repo(db_session):
    return ProjectRepository(db_session)


def test_get_by_id_returns_correct_object(projects_repo, project_factory):
    project = project_factory()

    obj = projects_repo.get_by_id(project.id)

    assert obj.id == project.id
    assert obj.name == project.name
    assert obj.date_end == project.date_end
    assert obj.date_start == project.date_start
    assert obj.geo_json == project.geo_json


def test_get_by_id_raises_not_found_error(projects_repo, project_factory):
    project_factory(id=1)

    with pytest.raises(ObjectNotFoundException) as e:
        projects_repo.get_by_id(2)

    assert e._excinfo[0].message == "Not found."


def test_no_projects_all_returns_empty_list(projects_repo):
    results = projects_repo.all()

    assert results == []


def test_all_returns_mltiple_projects(projects_repo, project_factory):
    projects = project_factory.create_batch(5)

    results = projects_repo.all()

    assert len(results) == 5
    assert all(
        [
            True if project.id in [obj.id for obj in results] else False
            for project in projects
        ]
    )


def test_create_insert_db_record(projects_repo, db_session):
    project_data = ProjectCreateType(
        **{
            "name": "project_name",
            "description": "description",
            "date_end": datetime.now(),
            "date_start": datetime.now(),
            "geo_json": {"key": "value"},
        }
    )

    obj = projects_repo.create(project_data)

    db_obj = db_session.query(Project).first()
    assert db_obj.name == obj.name
    assert db_obj.description == obj.description
    assert db_obj.date_end == obj.date_end
    assert db_obj.date_start == obj.date_start
    assert db_obj.geo_json == obj.geo_json


def test_create_allow_ommit_optional_fields(projects_repo, db_session):
    project_data = ProjectCreateType(
        **{
            "name": "project_name",
            "date_end": datetime.now(),
            "date_start": datetime.now(),
            "geo_json": {"key": "value"},
        }
    )

    obj = projects_repo.create(project_data)

    db_obj = db_session.query(Project).first()
    assert db_obj.description is None
    assert db_obj.name == obj.name
    assert db_obj.date_end == obj.date_end
    assert db_obj.date_start == obj.date_start
    assert db_obj.geo_json == obj.geo_json


def test_update_modify_row(projects_repo, db_session, project_factory):
    project = project_factory()
    update_data = ProjectUpdateType(
        **{
            "name": "project_name",
        }
    )

    obj = projects_repo.update(project.id, update_data)

    db_obj = db_session.query(Project).first()
    assert db_obj.name == "project_name"
    assert db_obj.description is obj.description
    assert db_obj.date_end == obj.date_end
    assert db_obj.date_start == obj.date_start
    assert db_obj.geo_json == obj.geo_json


def test_update_raises_not_found_error(projects_repo):
    update_data = ProjectUpdateType(
        **{
            "name": "project_name",
        }
    )

    with pytest.raises(ObjectNotFoundException) as e:
        projects_repo.update(1, update_data)

    assert e._excinfo[0].message == "Not found."


def test_update_can_set_optional_field_to_none(
    projects_repo, project_factory, db_session
):
    project = project_factory()
    update_data = ProjectUpdateType(**json.loads('{"description": null}'))

    projects_repo.update(project.id, update_data)

    db_obj = db_session.query(Project).first()
    assert db_obj.description is None


def test_delete_remove_object(projects_repo, db_session, project_factory):
    project = project_factory()

    projects_repo.delete(project.id)

    assert db_session.query(Project).first() is None


def test_delete_raises_not_found_error(projects_repo):
    with pytest.raises(ObjectNotFoundException) as e:
        projects_repo.delete(id=1)

    assert e._excinfo[0].message == "Not found."
