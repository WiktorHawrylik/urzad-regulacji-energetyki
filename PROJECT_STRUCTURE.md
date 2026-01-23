# Struktura Projektu - Urząd Regulacji Energetyki

## 📁 Przegląd Struktury

```
urzad-regulacji-energetyki/
├── src/urzad_regulacji_energetyki/
│   ├── __init__.py                                    # Główny pakiet
│   ├── biuletyn_informacji_publicznej_changelog/     # Moduł 1: BIP Changelog
│   │   ├── __init__.py
│   │   ├── analyzer.py         # Główny analizator zmian
│   │   ├── models.py           # Modele danych (BulletinChange, ChangeType)
│   │   ├── scrapers.py         # Web scraping utilities
│   │   └── utils.py            # Funkcje pomocnicze
│   ├── taryfy_i_inne_decyzje_energia_elektryczna/   # Moduł 2: Taryfy
│   │   ├── __init__.py
│   │   ├── analyzer.py         # Analizator taryf i decyzji
│   │   ├── models.py           # Modele (Tariff, Decision, TariffType)
│   │   ├── scrapers.py         # Web scraping utilities
│   │   └── utils.py            # Funkcje pomocnicze
│   └── rejestr_mioze/                               # Moduł 3: Rejestr MIOZE
│       ├── __init__.py
│       ├── registry.py         # Obsługiwacz rejestru MIOZE
│       ├── models.py           # Modele (MIOZEEntry, MIOZEStatus, MIOZESource)
│       ├── scrapers.py         # Web scraping utilities
│       └── utils.py            # Funkcje pomocnicze
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Fixtury i konfiguracja pytest
│   ├── unit/                   # Testy jednostkowe
│   │   ├── test_biuletyn_informacji_publicznej_changelog/
│   │   │   ├── test_models.py
│   │   │   └── test_analyzer.py
│   │   ├── test_taryfy_i_inne_decyzje_energia_elektryczna/
│   │   │   ├── test_models.py
│   │   │   └── test_analyzer.py
│   │   └── test_rejestr_mioze/
│   │       ├── test_models.py
│   │       └── test_registry.py
│   └── integration/
│       └── test_full_workflow.py
├── docs/                       # Dokumentacja (do utworzenia)
├── .github/                    # GitHub konfiguracja
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── CHANGELOG.md                # Historia zmian (po polsku)
├── CONTRIBUTING.md             # Wytyczne wkładu (po polsku)
├── LICENSE                     # GPL-3.0
├── Makefile                    # Build targets
├── README.md                   # Dokumentacja główna (po polsku)
├── pyproject.toml              # Konfiguracja projektu
├── setup_dev_macos.sh          # Setup script dla macOS
├── setup_dev.sh                # Setup script dla Linux/Windows
├── tox.ini                     # Konfiguracja tox
└── .codecov.yml                # Konfiguracja code coverage
```

## 🎯 Moduły

### 1. Biuletyn Informacji Publicznej - Changelog

**Lokalizacja**: `src/urzad_regulacji_energetyki/biuletyn_informacji_publicznej_changelog/`

**Funkcjonalność**:
- Śledzenie zmian publikowanych w Biuletynie Informacji Publicznej URE
- Analiza historii publikacji
- Wyszukiwanie i kategoryzacja wpisów

**Główne klasy**:
- `BulletinChangelogAnalyzer`: Główny analizator
- `BulletinChange`: Model danych zmiany
- `ChangeType`: Enum typów zmian

**Ejemplo użycia**:
```python
from urzad_regulacji_energetyki.biuletyn_informacji_publicznej_changelog import BulletinChangelogAnalyzer

analyzer = BulletinChangelogAnalyzer()
changes = analyzer.analyze_changes(start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
```

---

### 2. Taryfy i Inne Decyzje - Energia Elektryczna

**Lokalizacja**: `src/urzad_regulacji_energetyki/taryfy_i_inne_decyzje_energia_elektryczna/`

**Funkcjonalność**:
- Analiza taryf na energię elektryczną
- Śledzenie decyzji regulacyjnych
- Porównywanie taryf dla różnych scenariuszy użycia
- Predykcja zmian

**Główne klasy**:
- `TariffAnalyzer`: Analizator taryf i decyzji
- `Tariff`: Model danych taryfnego
- `Decision`: Model danych decyzji
- `TariffType`: Enum typów taryf

**Ejemplo użycia**:
```python
from urzad_regulacji_energetyki.taryfy_i_inne_decyzje_energia_elektryczna import TariffAnalyzer

analyzer = TariffAnalyzer()
tariffs = analyzer.get_current_tariffs()
comparison = analyzer.compare_tariffs(tariff_ids=["G11", "G12"], annual_consumption_kwh=3500)
```

---

### 3. Rejestr MIOZE

**Lokalizacja**: `src/urzad_regulacji_energetyki/rejestr_mioze/`

**Funkcjonalność**:
- Monitoring małych instalacji wytwórczych (MIOZE - Mały Rejestr Instalacji Wytwórczych)
- Analiza rozpowszechnienia mikroinstalacji
- Śledzenie trendów wdrażania MIOZE
- Statystyki regionalne i branżowe

**Główne klasy**:
- `MIOZERegistry`: Obsługiwacz rejestru
- `MIOZEEntry`: Model danych wpisu MIOZE
- `MIOZEStatus`: Enum statusów instalacji
- `MIOZESource`: Enum źródeł energii

**Ejemplo użycia**:
```python
from urzad_regulacji_energetyki.rejestr_mioze import MIOZERegistry

registry = MIOZERegistry()
mioze_entries = registry.get_mioze_by_region("mazowieckie")
stats = registry.generate_regional_statistics()
```

---

## 📋 Typy Danych

### BulletinChange
- `id`: Unikalny identyfikator
- `title`: Tytuł wpisu
- `change_type`: Typ zmany (publication, update, removal, modification)
- `date_published`: Data publikacji
- `category`: Kategoria wpisu

### Tariff
- `tariff_code`: Kod taryfny (G11, B23, itp.)
- `tariff_type`: Typ taryfny (household, business, industrial, itp.)
- `operator_name`: Nazwa operatora
- `base_rate`: Stawka podstawowa (PLN/MWh)

### MIOZEEntry
- `registration_id`: ID rejestracyjny
- `energy_source`: Źródło energii (photovoltaic, wind, hydro, itp.)
- `installed_power_kw`: Moc zainstalowana (kW)
- `location_voivodeship`: Województwo
- `status`: Status instalacji (active, inactive, deregistered)

---

## 🧪 Testy

Projekt zawiera testy jednostkowe i integracyjne:

```bash
# Uruchom wszystkie testy
make test

# Uruchom testy z pokryciem
make test-cov

# Uruchom konkretny test
pytest tests/unit/test_rejestr_mioze/test_models.py
```

---

## 🔧 Konfiguracja

- **Python**: >= 3.9
- **Zależności**: requests, beautifulsoup4, pandas, pydantic, lxml
- **Dev-zależności**: pytest, black, mypy, flake8, isort
- **Dokumentacja**: Sphinx, myst-parser

---

## 📄 Konwencje Kodowania

- **Kod**: Angielski (nazwy, komentarze techniczne)
- **Dokumentacja**: Polski (README, CONTRIBUTING, user-facing)
- **Type hints**: Wymagane dla wszystkich publicznych funkcji
- **Formatowanie**: Black (120 znaków na linię)
- **Linting**: flake8 + mypy w trybie strict

---

## 🚀 Pierwsze Kroki

1. **Klonowanie**:
   ```bash
   git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
   cd urzad-regulacji-energetyki
   ```

2. **Setup (macOS)**:
   ```bash
   ./setup_dev_macos.sh
   ```

3. **Instalacja zależności**:
   ```bash
   make install-dev
   ```

4. **Pre-commit hooks**:
   ```bash
   make pre-commit
   ```

5. **Uruchomienie testów**:
   ```bash
   make test
   ```

---

Made with ❤️ dla społeczności analityki energii
