# Struktura Projektu

## 📁 Przegląd Katalogów

```
urzad-regulacji-energetyki/
├── src/urzad_regulacji_energetyki/          # Kod źródłowy biblioteki
│   ├── __init__.py                          # Główny pakiet
│   ├── biuletyn_informacji_publicznej_changelog/
│   ├── taryfy_i_inne_decyzje_energia_elektryczna/
│   └── rejestr_mioze/
├── tests/                                   # Testy
│   ├── unit/                                # Testy jednostkowe
│   └── integration/                         # Testy integracyjne
├── docs/                                    # Dokumentacja MkDocs
├── scripts/                                 # Skrypty pomocnicze
├── .github/workflows/                       # CI/CD pipelines
└── dist/                                    # Zbudowane pakiety (gitignored)
```

## 📦 Moduły Biblioteki

### 1. Biuletyn Informacji Publicznej - Changelog

**Lokalizacja**: `src/urzad_regulacji_energetyki/biuletyn_informacji_publicznej_changelog/`

**Struktura**:
```
biuletyn_informacji_publicznej_changelog/
├── __init__.py          # Eksporty publiczne
├── analyzer.py          # BulletinChangelogAnalyzer - główny analizator
├── models.py            # BulletinChange, ChangeType - modele danych
├── scrapers.py          # Web scraping utilities
└── utils.py             # Funkcje pomocnicze
```

**Funkcjonalność**:
- Śledzenie zmian publikowanych w BIP URE
- Analiza historii publikacji
- Kategoryzacja i wyszukiwanie wpisów

**Przykład użycia**:
```python
from urzad_regulacji_energetyki.biuletyn_informacji_publicznej_changelog import (
    BulletinChangelogAnalyzer
)
from datetime import date

analyzer = BulletinChangelogAnalyzer()
changes = analyzer.analyze_changes(
    start_date=date(2024, 1, 1),
    end_date=date(2024, 12, 31)
)
```

**Główne klasy**:
- `BulletinChangelogAnalyzer` - główny silnik analizy
- `BulletinChange` - model pojedynczej zmiany
- `ChangeType` - enum typów zmian (publication, update, removal)

---

### 2. Taryfy i Inne Decyzje - Energia Elektryczna

**Lokalizacja**: `src/urzad_regulacji_energetyki/taryfy_i_inne_decyzje_energia_elektryczna/`

**Struktura**:
```
taryfy_i_inne_decyzje_energia_elektryczna/
├── __init__.py          # Eksporty publiczne
├── analyzer.py          # TariffAnalyzer - analizator taryf
├── models.py            # Tariff, Decision, TariffType - modele
├── scrapers.py          # Web scraping utilities
└── utils.py             # Funkcje pomocnicze
```

**Funkcjonalność**:
- Analiza taryf na energię elektryczną
- Śledzenie decyzji regulacyjnych URE
- Porównywanie taryf między operatorami
- Analiza historyczna zmian

**Przykład użycia**:
```python
from urzad_regulacji_energetyki.taryfy_i_inne_decyzje_energia_elektryczna import (
    TariffAnalyzer
)

analyzer = TariffAnalyzer()
tariffs = analyzer.get_current_tariffs()
comparison = analyzer.compare_tariffs(
    operators=["PGE Dystrybucja", "Tauron"]
)
```

**Główne klasy**:
- `TariffAnalyzer` - analizator taryf i decyzji
- `Tariff` - model danych taryfowych
- `Decision` - model decyzji regulacyjnych
- `TariffType` - enum typów taryf

---

### 3. Rejestr MIOZE

**Lokalizacja**: `src/urzad_regulacji_energetyki/rejestr_mioze/`

**Struktura**:
```
rejestr_mioze/
├── __init__.py          # Eksporty publiczne
├── registry.py          # MIOZERegistry - obsługa rejestru
├── models.py            # MIOZEEntry, MIOZEStatus - modele
├── scrapers.py          # Web scraping utilities
└── utils.py             # Funkcje analizy i statystyk
```

**Funkcjonalność**:
- Monitoring małych instalacji wytwórczych (≤50kW)
- Analiza rozmieszczenia geograficznego
- Statystyki według typu instalacji i regionu
- Śledzenie trendów wdrażania MIOZE

**Przykład użycia**:
```python
from urzad_regulacji_energetyki.rejestr_mioze import MIOZERegistry

registry = MIOZERegistry()
mioze_entries = registry.get_mioze_by_region("mazowieckie")
stats = registry.generate_regional_statistics()
```

**Główne klasy**:
- `MIOZERegistry` - główny obsługiwacz rejestru
- `MIOZEEntry` - model wpisu instalacji
- `MIOZEStatus` - enum statusów (active, inactive, deregistered)
- `MIOZESource` - enum źródeł energii (PV, wind, hydro)

---

## 🧪 Struktura Testów

```
tests/
├── __init__.py
├── conftest.py                              # Fixtury pytest
├── unit/                                    # Testy jednostkowe
│   ├── test_biuletyn_informacji_publicznej_changelog/
│   │   ├── test_models.py
│   │   └── test_analyzer.py
│   ├── test_taryfy_i_inne_decyzje_energia_elektryczna/
│   │   ├── test_models.py
│   │   └── test_analyzer.py
│   └── test_rejestr_mioze/
│       ├── test_models.py
│       └── test_registry.py
└── integration/                             # Testy integracyjne
    └── test_full_workflow.py
```

**Uruchomienie testów**:
```bash
# Wszystkie testy
uv run pytest

# Tylko testy jednostkowe
uv run pytest tests/unit/

# Konkretny moduł
uv run pytest tests/unit/test_rejestr_mioze/

# Z pokryciem kodu
uv run pytest --cov=urzad_regulacji_energetyki --cov-report=html
```

---

## 📚 Dokumentacja

```
docs/
├── index.md                     # Strona główna
├── guide/
│   ├── installation.md          # Przewodnik instalacji
│   └── quickstart.md            # Szybki start
├── modules/                     # Dokumentacja modułów
│   ├── biuletyn.md
│   ├── taryfy.md
│   └── mioze.md
├── api/                         # Auto-generowane API reference
│   ├── biuletyn.md
│   ├── taryfy.md
│   └── mioze.md
├── development/                 # Dokumentacja deweloperska
│   ├── tools.md                 # Narzędzia i konfiguracja
│   └── structure.md             # Ten dokument
├── contributing.md              # Przewodnik wkładu
└── license.md                   # Informacje o licencji
```

**Budowanie dokumentacji**:
```bash
# Serwuj lokalnie
make docs-serve
# Lub: uv run mkdocs serve

# Zbuduj do plików HTML
make docs
# Lub: uv run mkdocs build

# Deploy na GitHub Pages
make docs-deploy
# Lub: uv run mkdocs gh-deploy
```

---

## 📋 Modele Danych

### BulletinChange

```python
class BulletinChange:
    id: str                    # Unikalny identyfikator
    title: str                 # Tytuł wpisu
    change_type: ChangeType    # Typ zmiany
    date_published: date       # Data publikacji
    category: str              # Kategoria wpisu
    url: str                   # Link do dokumentu
```

### Tariff

```python
class Tariff:
    operator: str              # Nazwa operatora
    name: str                  # Nazwa taryfy
    rate: float                # Stawka (PLN/MWh)
    effective_date: date       # Data wejścia w życie
    approval_date: date        # Data zatwierdzenia
    document_url: str          # Link do dokumentu
```

### MIOZEEntry

```python
class MIOZEEntry:
    id: str                         # ID rejestracyjny
    type: str                       # Typ instalacji (PV, wind, etc.)
    capacity_kw: float              # Moc zainstalowana (kW)
    region: str                     # Województwo
    district: str                   # Powiat
    municipality: str               # Gmina
    installation_date: date         # Data instalacji
    status: str                     # Status (active, inactive, etc.)
```

---

## 🔧 Pliki Konfiguracyjne

### pyproject.toml
Główna konfiguracja projektu:
- Metadane pakietu (nazwa, wersja, autorzy)
- Zależności
- Konfiguracja narzędzi (ruff, mypy, pytest, coverage)
- Build system (setuptools)

### Makefile
Wygodne skróty dla częstych operacji:
- `make install-dev` - instalacja zależności
- `make format` - formatowanie kodu
- `make lint` - sprawdzanie jakości
- `make test` - uruchomienie testów
- `make docs-serve` - serwowanie dokumentacji

### .pre-commit-config.yaml
Hooki git przed commitem:
- Automatyczne formatowanie (ruff)
- Linting (ruff)
- Sprawdzanie YAML/TOML

---

## 🚀 Workflow Developmentu

1. **Klonuj repo i zainstaluj**:
   ```bash
   git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
   cd urzad-regulacji-energetyki
   uv sync --extra dev --extra test --extra docs
   ```

2. **Utwórz feature branch**:
   ```bash
   git checkout develop
   git checkout -b feature/moja-funkcja
   ```

3. **Wprowadź zmiany**:
   - Dodaj kod w `src/urzad_regulacji_energetyki/`
   - Dodaj testy w `tests/`
   - Zaktualizuj dokumentację w `docs/`

4. **Sprawdź jakość**:
   ```bash
   make format  # Sformatuj kod
   make lint    # Sprawdź jakość
   make test    # Uruchom testy
   ```

5. **Commit i push**:
   ```bash
   git add .
   git commit -m "feat(scope): add new feature"
   git push origin feature/moja-funkcja
   ```

6. **Otwórz Pull Request** na GitHubie

---

## 📐 Konwencje

### Kod
- **Język**: Angielski (nazwy klas, funkcji, zmiennych)
- **Dokumentacja**: Polski (README, przewodniki użytkownika)
- **Type hints**: Wymagane dla wszystkich funkcji publicznych
- **Formatowanie**: ruff (120 znaków na linię)
- **Docstrings**: Google style

### Nazewnictwo
- **Klasy**: PascalCase (`BulletinChangelogAnalyzer`)
- **Funkcje/metody**: snake_case (`analyze_changes`)
- **Zmienne**: snake_case (`start_date`)
- **Stałe**: UPPER_SNAKE_CASE (`MAX_RETRIES`)
- **Pliki**: snake_case (`analyzer.py`)

### Importy
```python
# Standardowa biblioteka
from datetime import date
import json

# Zależności zewnętrzne
import pandas as pd
from pydantic import BaseModel

# Lokalne importy
from .models import BulletinChange
from .utils import parse_date
```

---

## 🔗 Zobacz Również

- [Narzędzia Deweloperskie](tools.md) - Konfiguracja i użycie narzędzi
- [Przewodnik Wkładu](../contributing.md) - Jak wnieść wkład do projektu
- [API Reference](../api/biuletyn.md) - Pełna dokumentacja API
