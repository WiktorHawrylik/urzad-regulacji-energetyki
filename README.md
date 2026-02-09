# Python Library Template

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A **GPL-licensed Python library template** optimized for fast, agentic development with Codex, Copilot, and other LLM tools. This repository is designed to be used as a **GitHub template repo**.

> **For LLMs/agents**: Read and follow [AGENTS.md](AGENTS.md). Automated changes that ignore these rules are not accepted.

## Why this template?

- **Agent-ready**: Clear LLM instructions, repeatable dev workflow, and strong guardrails.
- **Modern tooling**: `pyproject.toml` as single source of truth, `uv`, `ruff`, `mypy`, `pytest`.
- **Docs-ready**: MkDocs site with a lightweight information architecture.
- **GPL by default**: Enforces copyleft compatibility.

## Quick start (local)

```bash
# 1) Create virtual environment + install dev/test/docs tooling
uv sync --extra dev --extra test --extra docs

# 2) Run checks
make format
make lint
make test
```

## Use as a GitHub template

1. Click **Use this template** on GitHub.
2. Rename identifiers using the checklist below.
3. Update links and metadata.

### Rename checklist

Search & replace the following placeholders:

- `python-library-template` → your project slug
- `python_library_template` → your import package
- `YOUR_GITHUB_ORG` / `YOUR_GITHUB_REPO` → your org/repo
- `Your Name` / `you@example.com` → your contact

Also update:

- `pyproject.toml` project name/version/urls
- `mkdocs.yml` site metadata
- `docs/index.md` and `README.md`

## Minimal usage example

```python
from python_library_template import LibraryConfig, greet

config = LibraryConfig(project_name="python-library-template", enable_experimental=True)
print(greet("Codex", config=config))
```

## Project layout

```
.
├── src/python_library_template
├── tests
├── docs
├── pyproject.toml
└── AGENTS.md
```

## License

GPL-3.0 — see [LICENSE](LICENSE).
