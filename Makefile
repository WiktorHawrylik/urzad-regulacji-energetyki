.PHONY: help install install-dev test test-cov lint format clean docs pre-commit

# Default target
help:
	@echo "Available targets:"
	@echo "  install        - Install package in development mode"
	@echo "  install-dev    - Install package with development dependencies"
	@echo "  test           - Run tests"
	@echo "  test-cov       - Run tests with coverage report"
	@echo "  lint           - Run all code quality checks"
	@echo "  format         - Format code with ruff"
	@echo "  format-check   - Check code formatting without modifying"
	@echo "  clean          - Clean build artifacts and caches"
	@echo "  docs           - Build documentation with MkDocs"
	@echo "  docs-serve     - Serve documentation locally"
	@echo "  docs-deploy    - Deploy documentation to GitHub Pages"
	@echo "  pre-commit     - Install pre-commit hooks"

install:
	uv pip install -e .

install-dev:
	uv sync --extra dev --extra test --extra docs

test:
	uv run pytest

test-cov:
	uv run pytest --cov=urzad_regulacji_energetyki --cov-report=html --cov-report=term

lint:
	@echo "Running code quality checks..."
	uv run ruff check src tests
	uv run ruff format --check src tests
	uv run mypy src

format:
	@echo "Formatting code..."
	uv run ruff check --fix src tests
	uv run ruff format src tests

format-check:
	uv run ruff format --check src tests

clean:
	@echo "Cleaning build artifacts and caches..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docs:
	@echo "Building documentation with MkDocs..."
	uv run mkdocs build

docs-serve:
	@echo "Serving documentation locally at http://127.0.0.1:8000"
	@lsof -ti :8000 | xargs kill -9 2>/dev/null || true
	uv run mkdocs serve

docs-deploy:
	@echo "Deploying documentation to GitHub Pages..."
	uv run mkdocs gh-deploy --force

pre-commit:
	uv run pre-commit install
