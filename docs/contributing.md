# Wkład w projekt

Dziękujemy za zainteresowanie wkładem w Bibliotekę Urzędu Regulacji Energetyki!

## Jak zacząć

1. **Fork repozytorium** na GitHubie
2. **Sklonuj** swój fork lokalnie
3. **Utwórz gałąź** dla swojej funkcji/poprawki
4. **Wprowadź zmiany** i dodaj testy
5. **Prześlij pull request**

Szczegółowe instrukcje znajdziesz w [CONTRIBUTING.md](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/blob/main/CONTRIBUTING.md).

## Środowisko deweloperskie

### Instalacja

```bash
git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
cd urzad-regulacji-energetyki

# Zainstaluj uv (jeśli jeszcze nie masz)
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS

# Zainstaluj projekt z wszystkimi zależnościami
uv sync --extra dev --extra test --extra docs

# Zainstaluj hooki pre-commit
uv run pre-commit install
```

### Dostępne komendy

```bash
# Formatowanie kodu
make format
# Lub: uv run ruff check --fix src tests && uv run ruff format src tests

# Sprawdzanie jakości kodu
make lint
# Lub: uv run ruff check src tests && uv run mypy src

# Uruchom testy
make test
# Lub: uv run pytest

# Testy z pokryciem
make test-cov
# Lub: uv run pytest --cov=urzad_regulacji_energetyki --cov-report=html

# Buduj dokumentację lokalnie
make docs
# Lub: uv run mkdocs serve

# Wyczyść artefakty
make clean
```

## Standardy kodowania

### Style kodu

- Używamy **ruff** do formatowania i lintingu (zastępuje black, isort, flake8)
- **mypy** w trybie strict dla sprawdzania typów
- Maksymalna długość linii: **120 znaków**
- Type hints wymagane dla wszystkich funkcji publicznych

### Testy

- Minimum **80% pokrycia kodu** testami
- Używamy **pytest** do testowania
- Testy jednostkowe w `tests/unit/`
- Testy integracyjne w `tests/integration/`

### Commity

Używamy [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

[optional body]
[optional footer]
```

**Typy:**
- `feat`: Nowa funkcjonalność
- `fix`: Poprawka błędu
- `docs`: Zmiany w dokumentacji
- `style`: Formatowanie kodu
- `refactor`: Refaktoryzacja kodu
- `test`: Dodanie/modyfikacja testów
- `chore`: Zmiany w narzędziach/konfiguracji

**Przykłady:**
```
feat(taryfy): add tariff comparison functionality
fix(biuletyn): handle missing bulletin dates
docs(readme): update installation instructions
```

## Git Flow

Projekt używa strategii **Git Flow**:

### Główne gałęzie

- `main` - kod produkcyjny, tylko wydania
- `develop` - gałąź rozwojowa

### Gałęzie robocze

- `feature/*` - nowe funkcje (rozgałęzienie z `develop`)
- `bugfix/*` - poprawki błędów (rozgałęzienie z `develop`)
- `hotfix/*` - pilne poprawki (rozgałęzienie z `main`)
- `release/*` - przygotowanie wydania (rozgałęzienie z `develop`)

### Proces pracy

1. Utwórz gałąź z `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/moja-funkcja
   ```

2. Wprowadź zmiany i commituj:
   ```bash
   git add .
   git commit -m "feat(scope): add new feature"
   ```

3. Prześlij do swojego forka:
   ```bash
   git push origin feature/moja-funkcja
   ```

4. Otwórz Pull Request na GitHubie

## Proces Code Review

- Wszystkie zmiany wymagają review przed mergem
- CI/CD musi przejść pomyślnie (testy, linting)
- Minimum jedno zatwierdzenie od maintainera
- Konflikty muszą być rozwiązane

## Dokumentacja

- Dodaj docstringi do wszystkich funkcji publicznych (styl Google)
- Zaktualizuj dokumentację w `docs/` jeśli wprowadzasz nowe funkcje
- Dodaj przykłady użycia w dokumentacji
- Zaktualizuj `CHANGELOG.md`

### Przykład docstring

```python
def analyze_tariffs(operator: str, year: int) -> list[TariffEntry]:
    """Analyze tariffs for a specific operator and year.

    Args:
        operator: Name of the energy operator
        year: Year for analysis (YYYY format)

    Returns:
        List of tariff entries for the specified operator and year

    Raises:
        ValueError: If year is invalid or operator not found
        DataFetchError: If data cannot be retrieved

    Example:
        ```python
        tariffs = analyze_tariffs("PGE", 2023)
        for tariff in tariffs:
            print(tariff.rate)
        ```
    """
```

## Budowanie dokumentacji lokalnie

```bash
# Zainstaluj zależności docs
uv sync --extra docs

# Uruchom serwer dokumentacji
uv run mkdocs serve

# Dokumentacja dostępna na http://127.0.0.1:8000
```

## Zasoby dla deweloperów

- **[Struktura Projektu](development/structure.md)** - Szczegółowa organizacja kodu i katalogów
- **[Narzędzia i Konfiguracja](development/tools.md)** - Przewodnik po narzędziach deweloperskich (ruff, mypy, pytest)
- **[API Reference](api/biuletyn.md)** - Automatycznie generowana dokumentacja API

## Zgłaszanie błędów

Używaj [GitHub Issues](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/issues) z szablonem:

```markdown
**Opis błędu**
Krótki opis problemu

**Jak odtworzyć**
1. Krok 1
2. Krok 2
3. Zobacz błąd

**Oczekiwane zachowanie**
Co powinno się stać

**Środowisko**
- OS: [np. macOS 14.0]
- Python: [np. 3.11]
- Wersja biblioteki: [np. 0.0.1]

**Dodatkowe informacje**
Logi, zrzuty ekranu, itp.
```

## Licencja

Wnosząc kod do tego projektu, zgadzasz się na licencję GPL-3.0.

## Pytania?

- Otwórz [Discussion](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/discussions)
- Napisz email: <wiktor.hawrylik@gmail.com>
