from as_api.main import hello_world


def test_hello_world():
    """Test that hello_world prints the expected message."""
    output = hello_world()
    assert output == "Hello World"
