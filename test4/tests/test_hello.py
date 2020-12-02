from test4 import hello


def test_hello():
    ju = "Juliana"
    hello_str = hello.say_hello(ju)
    assert "Hello" in hello_str
    assert ju in hello_str
