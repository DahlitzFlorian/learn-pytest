import pytest

import tasks

from tasks import Task


@pytest.fixture()
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), "tiny")

    # Part, where the testing happens
    yield

    # Teardown : stop db
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_few_samples():
    """Provide a few sample tasks, all with unique summaries and owners."""
    return (
        Task("Learn Pytest", "Florian", True),
        Task("Master Pytest", "Chris", False),
        Task("Teach Pytest", "Thomas", False)
    )


@pytest.fixture()
def db_with_three_tasks(initialized_tasks_db, tasks_few_samples):
    """Setup a connected db with three unique tasks."""
    for task in tasks_few_samples:
        tasks.add(task)


@pytest.fixture()
def tasks_samples_with_multiple_per_owner():
    """Provide samples with multiple tasks per owner."""
    return (
        Task("Learn Pytest", "Thomas"),
        Task("Master Pytest", "Thomas"),
        Task("Teach Pytest", "Thomas"),
        Task("Clean the house", "Florian"),
        Task("Wash the car", "Florian"),
        Task("Study mathematics", "Laura"),
        Task("Write a book", "Laura")
    )


@pytest.fixture()
def db_with_multiple_tasks_per_owner(initialized_tasks_db, tasks_samples_with_multiple_per_owner):
    """Setup connected db with multiple tasks per owner."""
    for task in tasks_samples_with_multiple_per_owner:
        tasks.add(task)
