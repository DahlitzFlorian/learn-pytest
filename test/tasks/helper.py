"""Helper functions for testing."""

from tasks.api import Task

def equivalent(t1: Task, t2: Task):
    """Check to tasksfor equivalence."""
    return t1.summary == t2.summary and t1.owner == t2.owner and t1.done == t2.done