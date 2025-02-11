from hello_flatten.hello.world import say_hello

def test_say_hello():
    result = say_hello("Tester")
    assert result == "Hello, Tester!"