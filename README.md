# My Package

A modern Python package template.

## Features

- Modern Python packaging using `pyproject.toml`
- Type hints and static type checking with mypy
- Code formatting and linting with Ruff
- Comprehensive testing setup
- GitHub Actions for CI/CD

## Installation

```bash
pip install my_package
```

## Usage

```python
from my_package import hello_world

# Use the function
result = hello_world()
print(result)  # Output: Hello, world!
```

## Development

This project uses modern Python development tools:

- [Hatch](https://hatch.pypa.io/) for project management
- [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
- [mypy](https://mypy.readthedocs.io/) for static type checking
- [pytest](https://pytest.org/) for testing

### Setup Development Environment

1. Install development dependencies:
```bash
pip install -e ".[dev]"
```

2. Run tests:
```bash
pytest
```

3. Run type checking:
```bash
mypy .
```

4. Run linting:
```bash
ruff check .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 