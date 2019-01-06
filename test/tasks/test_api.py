"""Test the API."""

import pytest

import tasks

from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), "tiny")

    # Part, where the testing happens
    yield

    # Teardown : stop db
    tasks.stop_tasks_db()


def test_add_wrong_parameter_type():
    """Test add with wrong parameters."""
    with pytest.raises(TypeError):
        tasks.add(task="Not a task object")


def test_add_returns_valid_id():
    """Test add returning an integer."""
    new_task = Task("Learn Pytest")
    task_id = tasks.add(new_task)

    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id():
    """Test add should set id."""
    new_task = Task("Learn Pytest", owner="Florian", done=True)
    task_id = tasks.add(new_task)
    task_from_db = tasks.get(task_id)

    assert task_from_db.id == task_id


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


@pytest.mark.xfail(
    tasks.__version__ < "0.2.0", reason="Not supported until version 0.2.0"
)
def test_unique_id_1():
    """Test calling unique_id() twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()

    assert id_1 != id_2


def test_unique_id_2():
    """Test unique_id() should return an unused id."""
    ids = [
        tasks.add(Task("Learn Pytest")),
        tasks.add(Task("Master Pytest")),
        tasks.add(Task("Teach Pytest")),
    ]

    uid = tasks.unique_id()

    assert uid not in ids
