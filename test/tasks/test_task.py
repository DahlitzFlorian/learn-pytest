"""Test the Task class."""

import pytest

from src.tasks.api import Task


@pytest.mark.run_please
def test_task_without_parameters():
    """Test Task without parameters."""
    task = Task()
    task_defaults = Task(None, None, False, None)

    assert task == task_defaults


@pytest.mark.run_please
def test_task_member_access():
    """Test Task member access."""
    task = Task("Learn Pytest", "Florian")

    assert task.summary == "Learn Pytest"
    assert task.owner == "Florian"
    assert (task.done, task.id) == (False, None)


def test_task_as_dict():
    """Test Task as dict."""
    task = Task("Learn Pytest", "Florian", True, 42)
    task_dict = task._asdict()

    expected = {
        "summary": "Learn Pytest",
        "owner": "Florian",
        "done": True,
        "id": 42
    }

    assert task_dict == expected


def test_task_replace():
    """Test Task replace fields."""
    task = Task("Learn Pytest", "Florian", False, 9)
    after = task._replace(done=True, id=10)
    expected = Task("Learn Pytest", "Florian", True, 10)

    assert after == expected
