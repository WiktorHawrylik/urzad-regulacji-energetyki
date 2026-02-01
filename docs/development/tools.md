# Narzędzia Deweloperskie

Projekt używa **`pyproject.toml` jako pojedynczego źródła konfiguracji** dla wszystkich narzędzi deweloperskich.

## Filozofia: Single Source of Truth

Wszystkie konfiguracje narzędzi znajdują się w `pyproject.toml`:

- ✅ **ruff** - formatowanie i linting (zastępuje black, isort, flake8)
- ✅ **mypy** - sprawdzanie typów
- ✅ **pytest** - testy
- ✅ **coverage** - pokrycie kodu

**Nie potrzeba oddzielnych plików konfiguracyjnych** - narzędzia automatycznie odkrywają ustawienia z `pyproject.toml`.

## Instalacja Środowiska

```bash
# Zainstaluj uv (jeśli jeszcze nie masz)
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS
# Lub: brew install uv  # macOS Homebrew

# Zainstaluj projekt z wszystkimi zależnościami deweloperskimi
uv sync --extra dev --extra test --extra docs

# Zainstaluj hooki pre-commit
uv run pre-commit install
```

## Uruchamianie Narzędzi

Wszystkie narzędzia uruchamiane są przez `uv run` i automatycznie odkrywają `pyproject.toml`:

### Formatowanie i Linting

```bash
# Sformatuj i napraw kod automatycznie
uv run ruff check --fix .
uv run ruff format .

# Sprawdź kod bez modyfikacji
uv run ruff check .
uv run ruff format --check .
uv run mypy src
```

### Testy

```bash
# Uruchom wszystkie testy
uv run pytest

# Testy z pokryciem kodu
uv run pytest --cov

# Uruchom konkretny test
uv run pytest tests/unit/test_rejestr_mioze/test_models.py
```

### Skróty Makefile

```bash
make format       # Sformatuj kod
make lint         # Sprawdź jakość kodu
make test         # Uruchom testy
make test-cov     # Testy z pokryciem
make clean        # Wyczyść artefakty
make docs-serve   # Serwuj dokumentację lokalnie
```

## Konfiguracja Narzędzi

### Ruff

Konfiguracja w `pyproject.toml`:

```toml
[tool.ruff]
line-length = 120
target-version = "py39"

[tool.ruff.lint]
select = ["E", "F", "I", "C90"]  # pycodestyle, Pyflakes, isort, mccabe
ignore = ["E203"]                # Kompatybilność z Black

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

**Dlaczego ruff?**
- 10-100x szybszy niż black/isort/flake8
- Zastępuje wiele narzędzi jednym
- Kompatybilny z Black
- Natywne wsparcie dla `pyproject.toml`

### Mypy

Konfiguracja w `pyproject.toml`:

```toml
[tool.mypy]
python_version = "3.9"
warn_return_any = true
disallow_untyped_defs = true
check_untyped_defs = true
strict_equality = true
```

**Tryb strict**: Wszystkie publiczne funkcje muszą mieć type hints.

### Pytest

Konfiguracja w `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = [
    "--strict-markers",
    "--cov=urzad_regulacji_energetyki",
    "--cov-report=html",
]
markers = [
    "slow: testy wolne",
    "integration: testy integracyjne",
    "unit: testy jednostkowe",
]
```

### Coverage

Konfiguracja w `pyproject.toml`:

```toml
[tool.coverage.run]
source = ["src"]
branch = true
omit = ["*/tests/*", "*/__init__.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
]
```

## Pre-commit Hooks

`.pre-commit-config.yaml` uruchamia narzędzia automatycznie przed commitem:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

Instalacja:

```bash
uv run pre-commit install
```

## VS Code

Minimalna konfiguracja w `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "python.testing.pytestEnabled": true
}
```

Zalecane rozszerzenia (`.vscode/extensions.json`):

```json
{
  "recommendations": [
    "charliermarsh.ruff",
    "ms-python.python",
    "ms-python.mypy-type-checker"
  ]
}
```

## CI/CD Integration

Przykład GitHub Actions:

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v4
  with:
    enable-cache: true

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

## Testowanie Wielu Wersji Pythona

Zamiast tox, używamy GitHub Actions matrix:

```yaml
strategy:
  matrix:
    python-version: ["3.9", "3.10", "3.11", "3.12", "3.13"]
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: ${{ matrix.python-version }}
  - run: uv sync --extra dev --extra test
  - run: uv run pytest
```

Lokalny development używa Twojej bieżącej wersji Pythona.

## Jak Działa Auto-Discovery

Nowoczesne narzędzia Pythona podążają za **PEP 518** i szukają `pyproject.toml`:

1. Zacznij w bieżącym katalogu
2. Sprawdź katalogi nadrzędne
3. Zatrzymaj się przy pierwszym znalezionym `pyproject.toml` lub rootcie repozytorium

**Nie potrzeba argumentów konfiguracyjnych!**

## Co Jest w Repozytorium

```
✅ pyproject.toml              # Pojedyncze źródło prawdy
✅ .pre-commit-config.yaml     # Git hooks
✅ .vscode/settings.json       # Minimalna konfiguracja edytora
✅ Makefile                    # Wygodne skróty
❌ tox.ini                     # Usunięte (używaj CI dla wielu wersji)
❌ setup.cfg                   # Usunięte (używaj pyproject.toml)
❌ .flake8                     # Usunięte (używaj pyproject.toml)
```

## Podsumowanie

✅ **Jeden plik konfiguracyjny**: `pyproject.toml` dla wszystkich narzędzi
✅ **Auto-discovery**: Narzędzia znajdują konfigurację automatycznie
✅ **Szybkie narzędzia**: ruff jest 10-100x szybszy niż alternatywy
✅ **Strict typing**: mypy wymusza type hints
✅ **CI/CD ready**: Łatwa integracja z GitHub Actions
