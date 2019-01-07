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
