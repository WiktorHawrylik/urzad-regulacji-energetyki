# Wkład w Projekt

Dziękujemy za zainteresowanie wkładem w ten projekt! Ten dokument opisuje nasz proces i wytyczne.

## Nasze Standardy

### Kod

- **Style**: Stosujemy [PEP 8](https://www.python.org/dev/peps/pep-0008/) z wyjątkami określonymi przez black
- **Formatowanie**: Kod jest formatowany za pomocą [black](https://github.com/psf/black) z długością linii 120
- **Import sorty**: Używamy [isort](https://github.com/PyCPA/isort) z profilem kompatybilnym z black
- **Linting**: Wymagany [flake8](https://flake8.pycqa.org/) bez błędów
- **Type hints**: Wszystkie funkcje publiczne muszą mieć type hints; mypy sprawdza to z opcją `strict`
- **Testy**: Kod powinien być pokryty testami (minimum 80% pokrycia)

### Zatwierdzenia (Commits)

- Używamy konwencji [Conventional Commits](https://www.conventionalcommits.org/)
- Format: `<type>(<scope>): <subject>`
  - **type**: feat, fix, docs, style, refactor, perf, test, chore, ci
  - **scope**: Opcjonalny, np. `biuletyn`, `taryfy`, `mioze`
  - **subject**: Imperatywny, małe litery, bez kropki na koniec, maks. 50 znaków

### Przykłady zatwierdzenia

```
feat(taryfy): add tariff comparison functionality
fix(biuletyn): handle missing bulletin dates
docs(readme): update installation instructions
test(mioze): add registry query tests
```

## Git Flow

Projekt podąża za strategią [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/):

### Główne gałęzie

- **main**: Produkcja, zawiera tylko wydania
- **develop**: Narzędzie do integracji, zawiera gotowe funkcje do następnego wydania

### Gałęzie pomocnicze

- **feature/\***: Nowe funkcje
  - Rozgałęzienie z: `develop`
  - Scala się z powrotem do: `develop`
  - Konwencja nazewnictwa: `feature/opisowa-nazwa`

- **bugfix/\***: Poprawki błędów
  - Rozgałęzienie z: `develop`
  - Scala się z powrotem do: `develop`
  - Konwencja nazewnictwa: `bugfix/opisowa-nazwa`

- **release/\***: Przygotowanie wydania
  - Rozgałęzienie z: `develop`
  - Scala się z powrotem do: `main` i `develop`
  - Konwencja nazewnictwa: `release/x.y.z`

- **hotfix/\***: Hotfixy dla produkcji
  - Rozgałęzienie z: `main`
  - Scala się z powrotem do: `main` i `develop`
  - Konwencja nazewnictwa: `hotfix/opisowa-nazwa`

## Proces Wkładu

1. **Fork** repozytorium
2. **Sklonuj** swój fork:
   ```bash
   git clone https://github.com/twoja-nazwa/urzad-regulacji-energetyki.git
   cd urzad-regulacji-energetyki
   ```

3. **Dodaj upstream**:
   ```bash
   git remote add upstream https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
   ```

4. **Utwórz gałąź funkcji**:
   ```bash
   git checkout -b feature/moja-funkcja develop
   ```

5. **Zainstaluj pre-commit hooks**:
   ```bash
   make pre-commit
   ```

6. **Wprowadź zmiany** i zatwierdzaj regularnie:
   ```bash
   git add .
   git commit -m "feat(modul): description"
   ```

7. **Pushuj zmiany** do swojego forka:
   ```bash
   git push origin feature/moja-funkcja
   ```

8. **Utwórz Pull Request** na GitHub:
   - Tytuł: Użyj tego samego formatu co commit message
   - Opis: Wyjaśnij **co** i **dlaczego**
   - Referencje: Dodaj numery issues, np. "Fixes #123"

## Wytyczne Pull Request

### Przed wysłaniem

- [ ] Aktualizujesz gałąź z upstreamem: `git pull upstream develop`
- [ ] Testy przechodzą: `make test`
- [ ] Kod jest sformatowany: `make format`
- [ ] Linting przechodzi: `make lint`
- [ ] Type checking przechodzi: `mypy src`
- [ ] Changelog jest aktualizowany
- [ ] Dokumentacja jest aktualizowana

### Wymagania do zatwierdzenia

- [ ] Minimum 2 recenzentów zatwierdza
- [ ] Wszystkie CI checks przechodzą
- [ ] Brak konfliktów z `develop`
- [ ] Pokrycie kodu nie spada
- [ ] Wszystkie dyskusje są rozwiązane

## Ustawienia Lokalne

### Konfiguracja Narzędzi - Pojedyncze Źródło Prawdy

Projekt używa **`pyproject.toml` jako jedynego źródła konfiguracji** dla wszystkich narzędzi deweloperskich.

#### 📋 Wszystkie reguły w `pyproject.toml`

```toml
[tool.black]          # Formatowanie kodu
[tool.isort]          # Sortowanie importów
[tool.flake8]         # Linting
[tool.mypy]           # Sprawdzanie typów
[tool.pytest.ini_options]  # Testy
[tool.coverage.run]   # Pokrycie kodu
```

Wszystkie narzędzia **automatycznie odkrywają** `pyproject.toml` - nie trzeba przekazywać argumentów `--config`.

#### ⚙️ `.vscode/settings.json` - Tylko zachowanie edytora

Minimalna konfiguracja VS Code bez zakodowanych ścieżek:

```json
{
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

### Uruchamianie Narzędzi

Wszystkie narzędzia uruchamiane przez `uv run`:

```bash
# Formatowanie
uv run black .
uv run isort .

# Sprawdzanie jakości
uv run flake8 src tests
uv run mypy src

# Testy
uv run pytest

# Lub skróty Makefile
make format      # Formatuj kod
make lint        # Sprawdź jakość
make test        # Uruchom testy
make test-cov    # Testy z pokryciem
```

**Dlaczego `uv run`?**
- Automatycznie używa prawid\u0142owego środowiska wirtualnego
- 10-100x szybszy niż pip
- Działa na Windows/Linux/macOS
- Reprodukowalne instalacje z lockfile

### Setup i Instalacja

```bash
# Klonowanie
git clone https://github.com/twoja-nazwa/urzad-regulacji-energetyki.git
cd urzad-regulacji-energetyki

# Instalacja uv (jeśli nie zainstalowane)
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS
# Lub: brew install uv  # macOS Homebrew

# Instalacja projektu z wszystkimi zależnościami
uv sync --extra dev --extra test --extra docs

# Instalacja pre-commit hooks
uv run pre-commit install
```

**Co zostanie zainstalowane**:
- `black`, `isort` - formatowanie
- `flake8` + `flake8-pyproject` - linting (plugin dla pyproject.toml)
- `mypy` - sprawdzanie typów
- `pytest` - testy
- `pre-commit` - git hooks



### Komendy Deweloperskie

```bash
# Uruchom wszystkie testy
make test

# Uruchom testy z pokryciem
make test-cov

# Format kodu
make format

# Sprawdź jakość kodu
make lint

# Type checking
mypy src

# Zbuduj dokumentację
make docs

# Uruchom pre-commit na wszystkich plikach
make pre-commit

# Czyszczenie artefaktów
make clean
```

## Dodawanie Nowych Modułów

Jeśli dodajesz nowy moduł, upewnij się, że:

1. **Struktura folderów**:
   ```
   src/urzad_regulacji_energetyki/nowy_modul/
   ├── __init__.py
   ├── models.py
   ├── scrapers.py
   ├── analyzer.py (lub odpowiadająca główna klasa)
   └── utils.py
   ```

2. **Dokumentacja**:
   - Docstrings w stylu Google
   - Typ hints dla wszystkich funkcji publicznych
   - README w folderze modułu

3. **Testy**:
   ```
   tests/unit/test_nowy_modul/
   ├── test_models.py
   ├── test_scrapers.py
   ├── test_analyzer.py
   └── test_utils.py
   ```

4. **Rejestracja** w `src/urzad_regulacji_energetyki/__init__.py`

5. **Dokumentacja** w `docs/api/index.rst`

## Tłumaczenie i Internacjonalizacja

- **Kod**: Tylko angielski (nazwy zmiennych, funkcji, komentarze techniczne)
- **Dokumentacja**: Polska (README, CONTRIBUTING, comments dla użytkowników)
- **Docstrings**: Angielski
- **Wiadomości Błędów**: Mogą być w angielskim dla spójności technicznej

## Przynależność i Licencje

Przesyłając kod do tego projektu, zgadzasz się na licencjonowanie go na warunkach licencji GPL-3.0.

## Pytania?

- Otwórz [GitHub Issue](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/issues)
- Dołącz do [GitHub Discussions](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/discussions)
- Wyślij email: wiktor.hawrylik@gmail.com

Dziękujemy za wkład! ❤️
