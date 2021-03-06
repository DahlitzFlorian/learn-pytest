# Fixtures #
## Basic fixture explanation ##
Fixtures are simply functions running before or after certain
test functions to set up a specific state or deliver data to
test functions. Naming is important at this point. A fixture is given
as parameter with the name of the fixture as parameter name to the
tests functions (at least at this basic level):

```python3
@pytest.fixture()
def deliver_number():
    """Deliver a certain number for tests."""
    return 23


def test_data_delivery(deliver_number):
    """Test checking for number delivered by fixture."""
    assert deliver_number == 23
```

## conftest.py ##
To make fixtures available for all test files in a certain directory
and for its subdirectories, put them into a `conftest.py` file located
in the directory. It's considered as a local **plugin** by pytest, so
never import it in any test file using `import conftest`!