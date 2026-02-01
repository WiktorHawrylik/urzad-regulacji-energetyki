# Szybki Start

Ten przewodnik pomoże Ci szybko rozpocząć pracę z biblioteką Urzędu Regulacji Energetyki.

## Podstawowe użycie

### Biuletyn Informacji Publicznej - Rejestr Zmian

Moduł do śledzenia i analizy zmian opublikowanych w BIP URE.

```python
from urzad_regulacji_energetyki.biuletyn_informacji_publicznej_changelog import BulletinChangelogAnalyzer
from datetime import date

# Inicjalizacja analizatora
analyzer = BulletinChangelogAnalyzer()

# Analiza zmian w określonym okresie
changes = analyzer.analyze_changes(
    start_date=date(2023, 1, 1),
    end_date=date(2023, 12, 31)
)

# Wyświetl statystyki
print(f"Liczba zmian: {len(changes)}")
print(f"Średnia zmian na miesiąc: {len(changes) / 12:.2f}")

# Filtrowanie zmian
important_changes = [
    change for change in changes
    if "decyzja" in change.title.lower()
]
print(f"Decyzje: {len(important_changes)}")
```

### Taryfy i Inne Decyzje - Energia Elektryczna

Moduł do analizy i śledzenia taryf na energię elektryczną.

```python
from urzad_regulacji_energetyki.taryfy_i_inne_decyzje_energia_elektryczna import TariffAnalyzer

# Inicjalizacja analizatora
analyzer = TariffAnalyzer()

# Pobierz aktualnie obowiązujące taryfy
current_tariffs = analyzer.get_current_tariffs()

# Wyświetl informacje o taryfach
for tariff in current_tariffs:
    print(f"Operator: {tariff.operator}")
    print(f"Taryfa: {tariff.name}")
    print(f"Stawka: {tariff.rate} PLN/MWh")
    print(f"Data obowiązywania: {tariff.effective_date}")
    print("-" * 50)

# Porównaj taryfy różnych operatorów
comparison = analyzer.compare_tariffs(
    operators=["Operator A", "Operator B"]
)
```

### Rejestr MIOZE

Moduł do monitorowania małych instalacji odnawialnych źródeł energii.

```python
from urzad_regulacji_energetyki.rejestr_mioze import MIOZERegistry

# Inicjalizacja rejestru
registry = MIOZERegistry()

# Pobierz dane o MIOZE w województwie
mioze_data = registry.get_mioze_by_region("mazowieckie")
print(f"Liczba instalacji MIOZE w Mazowieckim: {len(mioze_data)}")

# Generuj statystyki regionalne
regional_stats = registry.generate_regional_statistics()

for region, stats in regional_stats.items():
    print(f"{region}:")
    print(f"  Liczba instalacji: {stats.count}")
    print(f"  Całkowita moc: {stats.total_capacity_kw:.2f} kW")
    print(f"  Średnia moc: {stats.average_capacity_kw:.2f} kW")

# Analiza według typu instalacji
by_type = registry.analyze_by_installation_type()
for install_type, count in by_type.items():
    print(f"{install_type}: {count} instalacji")
```

## Zaawansowane przykłady

### Analiza trendów czasowych

```python
from urzad_regulacji_energetyki.biuletyn_informacji_publicznej_changelog import BulletinChangelogAnalyzer
from datetime import date, timedelta
import pandas as pd

analyzer = BulletinChangelogAnalyzer()

# Pobierz dane za ostatni rok
end_date = date.today()
start_date = end_date - timedelta(days=365)

changes = analyzer.analyze_changes(
    start_date=start_date,
    end_date=end_date
)

# Konwertuj do DataFrame dla analizy
df = pd.DataFrame([
    {
        'date': change.date,
        'title': change.title,
        'category': change.category
    }
    for change in changes
])

# Analiza miesięczna
monthly_stats = df.groupby(df['date'].dt.to_period('M')).size()
print("Zmiany według miesięcy:")
print(monthly_stats)
```

### Eksport danych

```python
from urzad_regulacji_energetyki.rejestr_mioze import MIOZERegistry
import json

registry = MIOZERegistry()

# Pobierz wszystkie dane
all_data = registry.get_all_installations()

# Eksport do JSON
with open('mioze_data.json', 'w', encoding='utf-8') as f:
    json.dump(
        [install.dict() for install in all_data],
        f,
        ensure_ascii=False,
        indent=2
    )

# Eksport do CSV
import pandas as pd
df = pd.DataFrame([install.dict() for install in all_data])
df.to_csv('mioze_data.csv', index=False, encoding='utf-8')
```

## Obsługa błędów

```python
from urzad_regulacji_energetyki.taryfy_i_inne_decyzje_energia_elektryczna import TariffAnalyzer
from urzad_regulacji_energetyki.exceptions import DataFetchError, ParseError

analyzer = TariffAnalyzer()

try:
    tariffs = analyzer.get_current_tariffs()
except DataFetchError as e:
    print(f"Błąd pobierania danych: {e}")
except ParseError as e:
    print(f"Błąd parsowania danych: {e}")
except Exception as e:
    print(f"Nieoczekiwany błąd: {e}")
```

## Następne kroki

- Przeczytaj szczegółową dokumentację [modułów](../modules/biuletyn.md)
- Zobacz pełne [API Reference](../api/biuletyn.md)
- Zapoznaj się z [przykładami](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki/tree/main/examples)
