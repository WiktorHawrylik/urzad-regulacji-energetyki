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

```bash
# Using uv (recommended)
uv pip install urzad-regulacji-energetyki

# Or using pip
pip install urzad-regulacji-energetyki
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
print(f"Liczba MIOZE w Mazowieckim: {len(mioze_data)}")
```

## 📚 Dokumentacja

Pełna dokumentacja dostępna pod adresem: [https://wiktorhawrylik.github.io/urzad-regulacji-energetyki/](https://wiktorhawrylik.github.io/urzad-regulacji-energetyki/)

## 🛠️ Rozwój

Szczegółowe informacje o konfiguracji środowiska deweloperskiego i narzędziach znajdziesz w [dokumentacji dla deweloperów](https://wiktorhawrylik.github.io/urzad-regulacji-energetyki/contributing/).

## 📄 Licencja

Ten projekt jest licencjonowany na warunkach licencji GPL-3.0 - zobacz plik [LICENSE](LICENSE) aby uzyskać szczegóły.

## 🤝 Pomoc

- **Problemy**: [GitHub Issues](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/issues)
- **Dyskusje**: [GitHub Discussions](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/discussions)
- **Autor**: Wiktor Hawrylik
- **Email**: <wiktor.hawrylik@gmail.com>

---

Wykonane z ❤️ dla społeczności analityki rynku energii
