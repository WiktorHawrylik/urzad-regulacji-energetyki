# Developer Tools

All tool configuration lives in `pyproject.toml`.

## Linting & formatting

```bash
make format
make lint
```

## Type checking

```bash
uv run mypy src
```

## Tests

```bash
make test
make test-cov
```
