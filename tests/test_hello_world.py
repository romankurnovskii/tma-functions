from my_package import hello_world


def test_hello_world():
    """Test that hello_world returns the expected string."""
    assert hello_world() == "Hello, world!"
