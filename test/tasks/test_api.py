"""Test the API."""

import pytest

import tasks

from helper import equivalent
from tasks import Task


def test_add_wrong_parameter_type():
    """Test add with wrong parameters."""
    with pytest.raises(TypeError):
        tasks.add(task="Not a task object")


def test_add_returns_valid_id(initialized_tasks_db):
    """Test add returning an integer."""
    new_task = Task("Learn Pytest")
    task_id = tasks.add(new_task)

    assert isinstance(task_id, int)


def test_add_equivalent(initialized_tasks_db):
    """Test whether tasks.get() using id returned from tasks.add() works."""
    task = Task("Learn Pytest", "Florian", True)
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)

    assert equivalent(task_from_db, task)


@pytest.mark.parametrize(
    "task",
    [
        Task("Learn Pytest", done=True),
        Task("Master Pytest", "Florian"),
        Task("Teach Pytest", "Florian", True),
        Task("Love Pytest", "Thomas", False),
    ],
)
def test_add_equivalent_one_parameter(initialized_tasks_db, task):
    """Test whether tasks.get() using id returned from tasks.add() works using parametrize."""
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)

    assert equivalent(task_from_db, task)


@pytest.mark.parametrize(
    "summary, owner, done",
    [
        ("Learn Pytest", None, True),
        ("Master Pytest", "Florian", False),
        ("Teach Pytest", "Florian", True),
        ("Love Pytest", "Thomas", False),
    ],
)
def test_add_equivalent_multiple_parameters(initialized_tasks_db, summary, owner, done):
    """Test whether tasks.get() using id returned from tasks.add() works using parametrize and multiple parameters."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)

    assert equivalent(task_from_db, task)


tasks_to_try = (
    Task("Learn Pytest", done=True),
    Task("Master Pytest", "Florian"),
    Task("Teach Pytest", "Florian", True),
    Task("Love Pytest", "Thomas", False),
)
task_ids = [f"Task({t.summary}, {t.owner}, {t.done}" for t in tasks_to_try]


@pytest.mark.parametrize("task", tasks_to_try, ids=task_ids)
def test_add_equivalent_parameters_using_external_variable(initialized_tasks_db, task):
    """Test using external variable."""
    task_id = tasks.add(task)
    task_from_db = tasks.get(task_id)

    assert equivalent(task_from_db, task)


def test_add_increases_count(db_with_three_tasks):
    """Test add() affect on tasks.count()."""
    tasks.add(Task("Throw a party"))

    assert tasks.count() == 4


@pytest.mark.smoke
def test_added_task_has_id(initialized_tasks_db):
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


class TestUniqueId:
    """Test the unique_id() method."""

    @pytest.mark.xfail(
        tasks.__version__ < "0.2.0", reason="Not supported until version 0.2.0"
    )
    def test_unique_id_1(self):
        """Test calling unique_id() twice should return different numbers."""
        id_1 = tasks.unique_id()
        id_2 = tasks.unique_id()

        assert id_1 != id_2

    def test_unique_id_2(self, initialized_tasks_db):
        """Test unique_id() should return an unused id."""
        ids = [
            tasks.add(Task("Learn Pytest")),
            tasks.add(Task("Master Pytest")),
            tasks.add(Task("Teach Pytest")),
        ]

        uid = tasks.unique_id()

        assert uid not in ids
