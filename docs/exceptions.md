# Exceptions #
## Expect an exception to be raised ##
Sometimes it's helpful to test, whether an exception is raised.
This can be useful when dealing with APIs. Therefore, the context
manager `pytest.raises()` can be used:

```python3
with pytest.raises(ValueError):
    # Test code raising an exception
```

## Checking for exception message ##
After an exception is caught, it can be compared with the expected
exception message

```python3
with pytest.raises(ValueError) as exc_info:
    # Code raising an exception
    exc_msg = exc_info.value.args[0]

    assert exc_msg == "expected exception message"
```