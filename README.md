# hello-flatten

A dummy repository for debugging and testing GitHub repo filtering functionality.

## Installation

```bash
poetry install
```

## Usage

```python
from hello_flatten.hello.world import say_hello

# Generate a greeting
greeting = say_hello("Developer")
print(greeting)  # Output: Hello, Developer!
```

Or use the CLI:

```bash
poetry run hello-flatten
```

## Development

### Setup

1. Install Poetry
2. Clone the repository
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Install pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

### Testing

```bash
poetry run pytest
```

### Code Quality

```bash
# Format code
poetry run black .
poetry run isort .

# Lint
poetry run ruff check .

# Type check
poetry run mypy .
```

## Project Structure

```
hello_flatten/
├── hello/
│   └── world.py      # Main greeting functionality
├── world/
│   └── hello.py      # Mirror module for testing
└── __init__.py       # Package initialization
```

## License

MIT

