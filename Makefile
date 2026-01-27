.PHONY: help install install-dev test test-cov lint format clean docs pre-commit

# Default target
help:
	@echo "Available targets:"
	@echo "  install        - Install package in development mode"
	@echo "  install-dev    - Install package with development dependencies"
	@echo "  test           - Run tests"
	@echo "  test-cov       - Run tests with coverage report"
	@echo "  lint           - Run all code quality checks"
	@echo "  format         - Format code with black and isort"
	@echo "  format-check   - Check code formatting without modifying"
	@echo "  clean          - Clean build artifacts and caches"
	@echo "  docs           - Build documentation"
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
	uv run black --check --diff src tests
	uv run isort --check-only --diff src tests
	uv run flake8 src tests
	uv run mypy src

format:
	@echo "Formatting code..."
	uv run black src tests
	uv run isort src tests

format-check:
	uv run black --check src tests
	uv run isort --check-only src tests

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
	uv run sphinx-build -W -b html docs docs/_build/html

pre-commit:
	uv run pre-commit install
