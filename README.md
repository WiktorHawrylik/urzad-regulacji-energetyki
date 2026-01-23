# Biblioteka Urzędu Regulacji Energetyki

[![Licencja: GPL-3.0](https://img.shields.io/badge/Licencja-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Kompleksowa biblioteka Pythona do tworzenia analiz z publicznie dostępnych danych ze stron internetowych Urzędu Regulacji Energetyki (URE):
- [ure.gov.pl](https://ure.gov.pl)
- [bip.ure.gov.pl](https://bip.ure.gov.pl)

## 🚀 Funkcjonalności

To repozytorium zawiera 3 specjalistyczne moduły Pythona do analizy rynku energii:

### 📋 Biuletyn Informacji Publicznej - Rejestr Zmian
- Śledzenie i analiza zmian opublikowanych w BIP
- Wyszukiwanie dokumentów i decyzji
- Generowanie raportów zmian
- Analiza historyczna opublikowanych informacji

### ⚡ Taryfy i Inne Decyzje - Energia Elektryczna
- Analiza i śledzenie taryf na energię elektryczną
- Porównywanie struktur taryf
- Generowanie prognoz zmian
- Historyczna analiza decyzji regulacyjnych

### 🗂️ Rejestr MIOZE
- Monitorowanie małych instalacji wytwórczych (≤50kW)
- Śledzenie wdrażania systemu MIOZE
- Analiza rozpowszechnienia mikroinstalacji
- Ocena wpływu na sieci dystrybucyjne

## 📦 Instalacja

### Z PyPI (rekomendowane)
```bash
pip install urzad-regulacji-energetyki
```

### Ze źródła
```bash
git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
cd urzad-regulacji-energetyki
pip install -e .
```

### Instalacja dla deweloperów

#### MacOS z pyenv (rekomendowane dla macOS)
```bash
git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
cd urzad-regulacji-energetyki
./setup_dev_macos.sh
```

## 🔧 Szybki Start

### Analiza Biuletynu Informacji Publicznej
```python
from urzad_regulacji_energetyki.biuletyn_informacji_publicznej_changelog import BulletinChangelogAnalyzer
from datetime import date

# Inicjalizacja analizatora
analyzer = BulletinChangelogAnalyzer()

# Analiza zmian w biuletynie
changes = analyzer.analyze_changes(
    start_date=date(2023, 1, 1),
    end_date=date(2023, 12, 31)
)

print(f"Liczba zmian: {len(changes)}")
print(f"Średnia zmian na miesiąc: {len(changes) / 12}")
```

### Analiza Taryf na Energię Elektryczną
```python
from urzad_regulacji_energetyki.taryfy_i_inne_decyzje_energia_elektryczna import TariffAnalyzer

# Inicjalizacja analizatora
analyzer = TariffAnalyzer()

# Pobierz obowiązujące taryfy
current_tariffs = analyzer.get_current_tariffs()

for tariff in current_tariffs:
    print(f"Taryfa: {tariff.name}")
    print(f"Stawka: {tariff.rate} PLN/MWh")
```

### Analiza Rejestru MIOZE
```python
from urzad_regulacji_energetyki.rejestr_mioze import MIOZERegistry

# Inicjalizacja rejestru
registry = MIOZERegistry()

# Pobierz dane o MIOZE w województwie
mioze_data = registry.get_mioze_by_region("mazowieckie")
print(f"Liczba MIOZE w Mazowieckimi: {len(mioze_data)}")

# Generuj statystyki regionalne
regional_stats = registry.generate_regional_statistics()
for region, stats in regional_stats.items():
    print(f"{region}: {stats.total_capacity_kw:.2f} kW całkowitej mocy")
```

## 📋 Struktura Modułów

```
src/urzad_regulacji_energetyki/
├── biuletyn_informacji_publicznej_changelog/
│   ├── analyzer.py         # Główny silnik analizy
│   ├── models.py           # Modele danych
│   ├── scrapers.py         # Narzędzia web scrapingu
│   └── utils.py            # Funkcje pomocnicze
├── taryfy_i_inne_decyzje_energia_elektryczna/
│   ├── analyzer.py         # Analiza taryf
│   ├── models.py           # Modele danych taryf
│   ├── scrapers.py         # Web scraper taryf
│   └── utils.py            # Narzędzia pomocnicze
└── rejestr_mioze/
    ├── registry.py         # Silnik rejestru MIOZE
    ├── models.py           # Modele danych MIOZE
    ├── scrapers.py         # Web scraper MIOZE
    └── utils.py            # Narzędzia analizy
```

## 🧪 Testowanie

Uruchom testy za pomocą pytest:
```bash
# Uruchom wszystkie testy
make test

# Uruchom z pokryciem kodu
pytest --cov=urzad_regulacji_energetyki

# Uruchom konkretny plik testowy
pytest tests/unit/test_tariff_analyzer.py

# Uruchom testy na wszystkich wersjach Pythona
make test-all
```

## 🔍 Jakość kodu

Ten projekt utrzymuje wysokie standardy jakości kodu:

```bash
# Formatowanie kodu
make format

# Linting
make lint

# Sprawdzanie typów
mypy src

# Pre-commit hooks
make pre-commit
```

## 📚 Dokumentacja

Zbuduj dokumentację lokalnie:
```bash
make docs
```

## 🛠️ Środowisko Deweloperskie

### Szybka konfiguracja (Rekomendowane)

Dla **użytkowników macOS z pyenv**:
```bash
git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
cd urzad-regulacji-energetyki
./setup_dev_macos.sh
```

Dla **użytkowników Linux/Windows**:
```bash
git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
cd urzad-regulacji-energetyki
./setup_dev.sh
```

### Konfiguracja ręczna

1. **Klonowanie repozytorium**:
   ```bash
   git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
   cd urzad-regulacji-energetyki
   ```

2. **Tworzenie środowiska wirtualnego**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. **Instalacja zależności deweloperskich**:
   ```bash
   make install-dev
   ```

4. **Instalacja pre-commit hooks**:
   ```bash
   make pre-commit
   ```

### Wkład

Ten projekt podąża za strategią gałęziowania **Git Flow** dla zorganizowanego rozwoju i wydań. Zobacz [CONTRIBUTING.md](CONTRIBUTING.md) aby uzyskać szczegółowe instrukcje dotyczące przepływu pracy, konwencji nazewnictwa gałęzi i procesu przesyłania.

## 📄 Licencja

Ten projekt jest licencjonowany na warunkach licencji GPL-3.0 - zobacz plik [LICENSE](LICENSE) aby uzyskać szczegóły.

## 🤝 Pomoc

- **Problemy**: [GitHub Issues](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/issues)
- **Dyskusje**: [GitHub Discussions](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/discussions)
- **Email**: <wiktor.hawrylik@gmail.com>

## 📈 Plan Rozwoju

- [ ] Dodanie wsparcia dla analiz danych historycznych
- [ ] Implementacja modeli uczenia maszynowego do predykcji zmian
- [ ] Dodanie możliwości transmisji danych w czasie rzeczywistym
- [ ] Stworzenie interaktywnego pulpitu nawigacyjnego
- [ ] Rozszerzenie wsparcia na dane europejskiego rynku energii
- [ ] Implementacja automatycznego generowania raportów

## 🙏 Podziękowania

- Urząd Regulacji Energetyki za zapewnienie dostępu do danych publicznych
- Wspólnota oprogramowania open-source
- Ekosystem nauki o danych Python (pandas, requests, BeautifulSoup, itp.)

---

Wykonane z ❤️ dla społeczności analityki rynku energii
