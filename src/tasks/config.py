"""Handle configuration files for tasks CLI."""

from collections import namedtuple
from pathlib import Path

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

TasksConfig = namedtuple("TasksConfig", ["db_path", "db_type"])


def get_config():
    """Return TasksConfig object after reading config file."""
    parser = ConfigParser()
    config_file = Path.home() / ".tasks.config"
    if not config_file.exists():
        tasks_db_path = Path.home() / "tasks_db"
        tasks_db_type = "tiny"
    else:
        parser.read(config_file)
        tasks_db_path = parser.get("TASKS", "tasks_db_path")
        tasks_db_type = parser.get("TASKS", "tasks_db_type")
    tasks_db_path = Path.home() / tasks_db_path
    return TasksConfig(tasks_db_path, tasks_db_type)
