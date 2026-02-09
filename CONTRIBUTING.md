# Contributing Guide

Thank you for contributing! This template is optimized for **agentic development** and repeatable workflows.

## Required for all contributors (including bots)

- Read and follow [AGENTS.md](AGENTS.md).
- Keep changes scoped and documented.
- Update docs when public APIs change.
- Run tests or explain why you couldn't.

## Development setup

```bash
# Install dependencies
uv sync --extra dev --extra test --extra docs

# Install pre-commit hooks
uv run pre-commit install
```

## Common commands

```bash
make format
make lint
make test
make test-cov
make docs
```

## Commit conventions

We use **Conventional Commits**:

```
<type>(<scope>): <subject>
```

Examples:

- `feat(core): add config model`
- `fix(docs): clarify template checklist`
- `chore(ci): update workflow`

## Template-specific guidelines

- Keep the rename checklist accurate.
- Use placeholders when the real project values are unknown.
- Document any new tooling in `pyproject.toml` and `README.md`.

By contributing, you agree that your work is licensed under GPL-3.0.
