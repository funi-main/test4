from test4 import hello


def test_hello():
    hello_str = hello.say_hello()
    assert "Hello" in hello_str
