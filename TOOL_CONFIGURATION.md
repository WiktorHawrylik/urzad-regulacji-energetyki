# Tool Configuration Guide

This project uses **`pyproject.toml` as the single source of configuration** for all development tools.

## Philosophy: Single Source of Truth

All tool configurations live in `pyproject.toml`:
- ✅ ruff (formatter and linter - replaces black, isort, flake8)
- ✅ mypy (type checker)
- ✅ pytest (test framework)
- ✅ coverage (code coverage)

**No separate config files needed** - tools auto-discover their settings from `pyproject.toml`.

## Configuration Overview

### `pyproject.toml` - All Tool Settings

```toml
[tool.ruff]
line-length = 120
target-version = "py39"

[tool.ruff.lint]
select = ["E", "F", "I", "C90"]
ignore = ["E203", "W503"]

[tool.ruff.format]
quote-style = "double"

[tool.mypy]
python_version = "3.9"
disallow_untyped_defs = true
strict_equality = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["--strict-markers", "--cov=urzad_regulacji_energetyki"]

[tool.coverage.run]
source = ["src"]
branch = true
```

### `.vscode/settings.json` - Editor Behavior Only

Minimal VS Code configuration without hardcoded paths:

```json
{
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "python.testing.pytestEnabled": true
}
```

## Running Tools

All tools are run via `uv run` and auto-discover `pyproject.toml`:

```bash
# Format and lint code
uv run ruff check --fix .
uv run ruff format .

# Check code quality
uv run ruff check .
uv run ruff format --check .
uv run mypy src

# Run tests
uv run pytest
uv run pytest --cov

# Or use Makefile shortcuts
make format      # Format code
make lint        # Check all quality
make test        # Run tests
make test-cov    # Run tests with coverage
```

## How Auto-Discovery Works

Modern Python tools follow **PEP 518** and search for `pyproject.toml`:

1. Start in current directory
2. Check parent directories
3. Stop at first `pyproject.toml` found or repository root

**No config arguments needed!**

### Tool-Specific Notes:

- **ruff**: Native `pyproject.toml` support, 10-100x faster than black/isort/flake8 ✅
- **mypy**: Native support since v0.900 ✅
- **pytest**: Native support since v6.0 ✅

## Installation

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS
# Or: brew install uv  # macOS Homebrew
# Or: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Install project with all dev dependencies
uv sync --extra dev --extra test --extra docs

# This installs ruff, mypy, pytest
# All configured via pyproject.toml
```

## Pre-commit Hooks

`.pre-commit-config.yaml` runs tools without inline args:

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  hooks:
    - id: ruff
      args: [--fix]
    - id: ruff-format
```

## CI/CD Integration

GitHub Actions example:

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v4
  with:
    enable-cache: true

- name: Set up Python
  run: uv python install ${{ matrix.python-version }}

- name: Install dependencies
  run: uv sync --extra dev --extra test

- name: Check formatting and lint
  run: |
    uv run ruff check .
    uv run ruff format --check .

- name: Type check
  run: uv run mypy src

- name: Test
  run: uv run pytest
```

## What's Committed

```
✅ pyproject.toml              # Single source of truth
✅ .pre-commit-config.yaml     # Git hooks
✅ .vscode/settings.json       # Minimal editor config
✅ .vscode/extensions.json     # Recommended extensions
✅ Makefile                    # Convenient shortcuts
❌ tox.ini                     # Removed (use CI for multi-version)
❌ .editorconfig               # Removed (Black handles formatting)
❌ setup.cfg                   # Removed (use pyproject.toml)
❌ .flake8                     # Removed (use pyproject.toml)
```

## Multi-Python Version Testing

Instead of tox, use GitHub Actions matrix:

```yaml
strategy:
  matrix:
    python-version: ["3.9", "3.10", "3.11", "3.12"]
steps:
  - uses: actions/setup-python@v4
    with:
      python-version: ${{ matrix.python-version }}
  - run: python -m pytest
```

Local development uses your current Python version.

## Makefile Shortcuts

```bash
make install-dev    # Install with dev dependencies
make format         # Auto-format code
make lint           # Run all quality checks
make test           # Run tests
make test-cov       # Run tests with coverage report
make clean          # Remove build artifacts
make pre-commit     # Install git hooks
```

## Summary

✅ **Single config file**: `pyproject.toml` for all tools
✅ **Auto-discovery**: Tools find config automatically
✅ **Portable**: Works on any OS
✅ **Fast**: uv is 10-100x faster than pip
✅ **Simple**: Run with `uv run <tool>`
✅ **Editor-agnostic**: PyCharm, Vim, VS Code all use same rules
✅ **CI-ready**: Same commands locally and in CI/CD
✅ **Lockfile**: Reproducible builds with `uv.lock`
