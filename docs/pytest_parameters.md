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