"""My Package - A modern Python package template.

This module provides a simple example function.
"""

from typing import Final

__version__: Final[str] = "0.1.0"


def hello_world() -> str:
    """Return a greeting message.

    Returns:
        str: A greeting message.
    """
    return "Hello, world!"
