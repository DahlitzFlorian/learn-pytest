# Pytest Parameters #
## --collect-only ##
Collects all tests and list them with their modules without
running them. Useful to see, whether the correct tests were found.

```PowerShell
(dev) P:\Python\learn-pytest>pytest --collect-only
============================= test session starts =============================
platform win32 -- Python 3.6.8rc1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: P:\Python\learn-pytest, inifile:
collected 4 items
<Module 'test/tasks/test_task.py'>
  <Function 'test_task_without_parameters'>
  <Function 'test_task_member_access'>
  <Function 'test_task_as_dict'>
  <Function 'test_task_replace'>
```

## -k for Selection ##
Use the `-k` option to select certain tests.

```PowerShell
(dev) P:\Python\learn-pytest>pytest -k "without or replace" --collect-only
============================= test session starts =============================
platform win32 -- Python 3.6.8rc1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: P:\Python\learn-pytest, inifile:
collected 4 items / 2 deselected
<Module 'test/tasks/test_task.py'>
  <Function 'test_task_without_parameters'>
  <Function 'test_task_replace'>

======================== 2 deselected in 0.06 seconds =========================
```

## -m for Markers ##
Use `-m` followed by marker(s) to only run marked tests. Tests can be
marked as follows:

```python3
import pytest

@pytest.mark.run_please
def test_function():
    """Sample Function."""
    assert (1, 2, 3) == (1, 2, 3)
```

Below is the output of `pytest -m`. As you can see, two functions
were marked as *run_please*.

```PowerShell
(dev) P:\Python\learn-pytest>pytest -m "run_please" --collect-only
============================= test session starts =============================
platform win32 -- Python 3.6.8rc1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: P:\Python\learn-pytest, inifile:
collected 4 items / 2 deselected
<Module 'test/tasks/test_task.py'>
  <Function 'test_task_without_parameters'>
  <Function 'test_task_member_access'>
```

Markers can be combined:
- `pytest -m "run_please and marker2"` will run those with both markers applied
- `pytest -m "run_please and not marker2"` those with *run_please* and
without *marker2*
- `pytest -m "run_please or marker2"` those having either of both applied
- ...

## -x for --exitfirst ##
Using this flag stops pytest from further executions right after the
first test fails. Normally, pytest will continue with the other
tests and tell you afterwards, which one failed. This flag is good
for debugging purposes.

```PowerShell
$ pytest -x
```