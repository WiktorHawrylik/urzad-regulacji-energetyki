#!/bin/bash
# Script to verify which config files tools are using

echo "=== Black Configuration ==="
python -m black --verbose --check src 2>&1 | grep -i "configuration\|pyproject"
echo

echo "=== isort Configuration ==="
python -m isort --verbose --check-only src 2>&1 | grep -i "config\|pyproject" || echo "isort is using pyproject.toml (use --verbose to see details)"
echo

echo "=== flake8 Configuration ==="
python -m flake8 --version
echo "Note: Requires flake8-pyproject plugin to read pyproject.toml"
echo

echo "=== mypy Configuration ==="
python -m mypy --version
python -m mypy --verbose src 2>&1 | grep -i "config\|pyproject" | head -5 || echo "Check mypy output for config source"
echo

echo "=== pytest Configuration ==="
python -m pytest --version
python -m pytest --collect-only -q 2>&1 | head -5
echo

echo "=== Summary ==="
echo "All tools should be reading from: $(pwd)/pyproject.toml"
ls -la pyproject.toml
