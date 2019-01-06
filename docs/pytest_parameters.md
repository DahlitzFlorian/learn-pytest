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

## Capture output ##
Normally, pytest captures everything that's directed to `stdout`. Only
if the test fails, the output will be shown as it may help. Sometimes
it's useful to not capture it to see the tests flow. Use `-s` to set
`--capture=no`:

```PowerShell
$ pytest -s
```

## Show locals using -l/--showlocals ##
Using `-l` prints the local variables in a test if the test fails.

```PowerShell
$ pytest -l
```

## Trace Back ##
To not show the trace back, simply use `--tb=no`:

```PowerShell
$ pytest --tb=no
```

Use `-q/--quiet` to get less information (opposite of `-v/--verbose`):
```PowerShell
$ pytest -q
```

Or simply use `--tb` to scale the length of the trace back:
- *long*: bunch of information
- *short*: less than normal
- *line*: just the line of the assertion

## Get time performance information ##
To get information about the time needed to *call*, *setup* or *teardown*
a test, use `--durations=N` where N is a natural number. Passing
`--durations=0` will report everything ordered from slowest to fastest.

```PowerShell
$ pytest --durations=0
```

## Skipping tests ##
Sometimes it can be helpful to skip certain tests, which an be achieved
using the marker `skip`:

```python3
@pytest.mark.skip(reason="Misunderstood the API")
def test_to_skip():
    """Test to skip."""
    assert (1, 2, 3) != (3, 2, 1)
```

If a test should only be skipped under certain circumstances, use
`skipif` instead:

```python3
@pytest.mark.skipif(
    tasks.__version__ < "0.2.0",
    reason="Not supported until version 0.2.0"
)
def test_feature():
    """Test unsupported before certain version."""
    assert (1, 2, 3) != (3, 2, 1)
```

As the `-v` flag does not show the reason for skipping the tests,
the `-rs` flags to show.
- `-r` (chars): show extra test summary

## xfail - Expected to fail ##
Marking tests as expected to fail is as easy as:

```python3
@pytest.mark.xfail()
def test_mark_as_expected_to_fail():
    """Test expected to fail."""
    assert (1, 2, 3) == (3, 2, 1)


@pytest.mark.xfail(
    tasks.__version__,
    reason="Not supported until version 0.2.0"
)
def test_mark_expected_to_fail_with_options():
    """Test expected to fail with options."""
    assert (1, 2, 3) == (3, 2, 1)
```

Pytest will put an **x** if it fails as expected (**XFAIL**) and an
**X** if expected to fail but passed (**XPASS**).

## Parametrize Tests ##
Testing a piece of code using only one pair of values may not be
sufficient in some cases. Therefore, it's possible to call a test
with multiple parameters.

```python3
@pytest.mark.parametrize(
    "task",
    [
        Task("Learn Pytest", "Florian"),
        Task("Master Pytest", None, True)
    ]
)
def test_using_parametrize(task):
    """Test using parametrize."""
    assert equivalent(task, task)
```

```python3
@pytest.mark.parametrize(
    "summary, owner, done",
    [
        ("Learn Pytest", "Thomas", False),
        ("Master Pytest", None, True),
        ("Teach Pytest", "Mark")
    ]
)
def test_using_parametrize_multiple_parameters(summary, owner, done):
    """Test using parametrize with multiple parameters."""
    assert equivalent(task, task)
```

To call only a single parameter set, use the node (whole test identifier):

```PowerShell
$ pytest -v "test_file.py::test_using_parametrize_multiple_parameters[Master Pytest-None-True]"
```

*Note: Quotes are needed if whitespaces are used!*