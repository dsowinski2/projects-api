from datetime import datetime
from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from backend.src.controllers.projects import ProjectsController
from backend.src.repositories.excepions import ObjectNotFoundException
from backend.src.repositories.projects.repo import ProjectRepository
from backend.src.utils.types import ProjectCreateType
from backend.src.utils.types import ProjectUpdateType

pytestmark = pytest.mark.usefixtures("db_session")

PROJECT_ID = 1


@pytest.fixture
def project_controller(db_session):
    repo = ProjectRepository(db_session)
    return ProjectsController(repository=repo)


def test_list_objects_repository_calls(mocker, project_controller):
    expected_value = MagicMock()
    repo_mock = mocker.patch(
        "backend.src.controllers.projects.ProjectRepository.all",
        return_value=expected_value,
    )

    result = project_controller.list_objects()

    assert result == expected_value
    repo_mock.assert_called_once


def test_get_object_by_id_repository_calls(mocker, project_controller):
    expected_value = MagicMock()
    repo_mock = mocker.patch(
        "backend.src.controllers.projects.ProjectRepository.get_by_id",
        return_value=expected_value,
    )

    result = project_controller.get_object_by_id(PROJECT_ID)

    assert result == expected_value
    repo_mock.assert_called_once_with(PROJECT_ID)


def test_update_object_repository_calls(mocker, project_controller):
    expected_value = MagicMock()
    update_data = ProjectUpdateType(**{"name": "new_name"})
    repo_mock = mocker.patch(
        "backend.src.controllers.projects.ProjectRepository.update",
        return_value=expected_value,
    )

    result = project_controller.update_object(PROJECT_ID, update_data)

    assert result == expected_value
    repo_mock.assert_called_once_with(PROJECT_ID, update_data)


def test_delete_object_repository_calls(mocker, project_controller):
    repo_mock = mocker.patch(
        "backend.src.controllers.projects.ProjectRepository.delete"
    )

    result = project_controller.delete_object(PROJECT_ID)

    assert result is None
    repo_mock.assert_called_once_with(PROJECT_ID)


def test_create_object_repository_calls(mocker, project_controller):
    create_data = ProjectCreateType(
        **{
            "name": "project_name",
            "description": "description",
            "date_end": datetime.now(),
            "date_start": datetime.now(),
            "geo_json": {"key": "value"},
        }
    )
    expected_value = MagicMock()
    repo_mock = mocker.patch(
        "backend.src.controllers.projects.ProjectRepository.create",
        return_value=expected_value,
    )

    result = project_controller.create_object(create_data)

    assert result == expected_value
    repo_mock.assert_called_once_with(create_data)


def test_error_handling_repo_nof_found_exception(mocker, project_controller):
    mocker.patch(
        "backend.src.controllers.projects.ProjectRepository.get_by_id",
        side_effect=ObjectNotFoundException,
    )

    with pytest.raises(HTTPException) as e:
        project_controller.get_object_by_id(PROJECT_ID)

    assert e._excinfo[1].status_code == 404
    assert e._excinfo[1].detail == "Not found."
