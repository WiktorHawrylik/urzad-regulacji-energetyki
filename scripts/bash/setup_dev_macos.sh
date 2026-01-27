#!/bin/bash
# Development setup script for Polish Energy Regulatory Office library (using uv)

set -e

echo "🚀 Setting up Polish Energy Regulatory Office development environment with uv..."

# Check if Homebrew is installed (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew is not installed. Please install it first:"
        echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi
    echo "✅ Homebrew is available"
fi

# Check if uv is installed, install if not
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install uv
    else
        curl -LsSf https://astral.sh/uv/install.sh | sh
    fi
    echo "✅ uv installed successfully"
else
    echo "✅ uv is already installed ($(uv --version))"
fi

# Define Python version
PYTHON_VERSION="3.9"

# Verify Python version with uv
echo "🔧 Using Python $PYTHON_VERSION..."
python_version=$(uv run python --version 2>&1 | cut -d' ' -f2)
echo "✅ Using Python version: $python_version"

# Sync dependencies with uv
echo "📚 Installing package and all dependencies with uv..."
uv sync --extra dev --extra test --extra docs

# Install pre-commit hooks
echo "🪝 Installing pre-commit hooks..."
uv run pre-commit install

# Run initial checks
echo "🧪 Running initial checks..."
echo "  - Code formatting check..."
uv run black --check src tests || echo "    ⚠️ Code formatting issues found. Run 'make format' to fix."

echo "  - Import sorting check..."
uv run isort --check-only src tests || echo "    ⚠️ Import sorting issues found. Run 'make format' to fix."

echo "  - Linting check..."
uv run flake8 src tests || echo "    ⚠️ Linting issues found. Review and fix manually."

echo "  - Type checking..."
uv run mypy src || echo "    ⚠️ Type checking issues found. Review and fix manually."

echo "  - Running tests..."
uv run pytest || echo "    ⚠️ Some tests failed. Review and fix manually."

echo ""
echo "🎉 Development environment setup complete!"
echo ""
echo "Environment details:"
echo "  - Python version: $python_version"
echo "  - Package manager: uv ($(uv --version))"
echo "  - Virtual environment: managed by uv (.venv/)"
echo ""
echo "Next steps:"
echo "  1. Run commands with: uv run <command>"
echo "  2. Or use make shortcuts: make test, make lint, make format"
echo "  3. Start developing!"
echo ""
echo "Quick commands:"
echo "  uv run python        # Run Python with project dependencies"
echo "  uv run pytest        # Run tests"
echo "  uv run black .       # Format code"
echo "  make test            # Run tests (uses uv internally)"
echo "  make lint            # Check code quality"
echo ""
echo "Happy coding! 🐍"
