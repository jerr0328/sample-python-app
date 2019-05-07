from sample.main import some_string


def test_some_string():
    assert "Hello, world" == some_string()


def test_failure():
    assert "" == some_string()
