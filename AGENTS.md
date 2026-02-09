# Agent Instructions (Required)

This repository is a **template** for agentic Python library development. Any automated agent (LLM, bot, CI fixer) must follow these rules.

## Mandatory workflow

1. **Read before edit**: Review `README.md`, `pyproject.toml`, and docs before changes.
2. **Explain intent**: Provide a clear summary of changes and why they were made.
3. **Keep placeholders explicit**: Do not remove placeholder tokens (e.g., `YOUR_GITHUB_ORG`) without replacing them with real values.
4. **Update docs with code**: If you change public APIs, update `docs/` and `README.md`.
5. **Test or state why not**: Run relevant checks, or explicitly state why you could not.
6. **Avoid large, unrelated refactors**: Keep changes scoped to the request.

## Code quality expectations

- Use type hints and docstrings for public APIs.
- Keep formatting compatible with `ruff` (line length 120).
- Prefer small, composable functions.

## AI safety and provenance

- Do not add dependencies or network calls without justification.
- Do not include secrets, tokens, or personal data.
- If you generate content, ensure it is GPL-compatible.

By contributing, you agree to these rules and to the GPL-3.0 license.
