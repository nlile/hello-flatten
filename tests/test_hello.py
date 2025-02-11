import pytest
from hello_flatten.hello.world import say_hello, Greeting

def test_greeting_model():
    # Test Pydantic model
    greeting = Greeting(name="Test")
    assert greeting.name == "Test"
    assert greeting.message == "Hello"
    assert greeting.format() == "Hello, Test!"

def test_say_hello():
    # Test with default parameter
    assert say_hello() == "Hello, World!"

    # Test with custom name
    assert say_hello("Developer") == "Hello, Developer!"

def test_greeting_validation():
    # Test Pydantic validation
    with pytest.raises(ValueError):
        Greeting(name=123)  # type: ignore  # Testing invalid type