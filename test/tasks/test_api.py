"""Test the API."""

import pytest

from src import tasks


def test_add_wrong_parameter_type():
    """Test add with wrong parameters."""
    with pytest.raises(TypeError):
        tasks.add(task="Not a task object")


def test_start_tasks_db():
    """Test whether unsupported db raises an exception."""
    with pytest.raises(ValueError) as exc_info:
        tasks.start_tasks_db("some/great/path", "mysql")
        exc_msg = exc_info.value.args[0]

        assert exc_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_tasks_wrong_parameter_type():
    """Test list with wrong parameters."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.smoke
@pytest.mark.get
def test_get_task_wrong_parameter_type():
    """Test get using wrong parameters."""
    with pytest.raises(TypeError):
        tasks.get(task_id="123")
