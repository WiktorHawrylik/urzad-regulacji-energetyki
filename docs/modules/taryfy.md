# Taryfy i Inne Decyzje - Energia Elektryczna

Moduł do analizy i śledzenia taryf na energię elektryczną oraz decyzji regulacyjnych URE.

## Przegląd

Moduł `taryfy_i_inne_decyzje_energia_elektryczna` umożliwia:

- Pobieranie aktualnych taryf na energię elektryczną
- Analizę historyczną zmian taryf
- Porównywanie taryf różnych operatorów
- Śledzenie decyzji regulacyjnych

## Główne komponenty

### TariffAnalyzer

Główna klasa do analizy taryf.

```python
from urzad_regulacji_energetyki.taryfy_i_inne_decyzje_energia_elektryczna import TariffAnalyzer

analyzer = TariffAnalyzer()

# Pobierz aktualne taryfy
current_tariffs = analyzer.get_current_tariffs()
```

### Modele danych

#### TariffEntry

Reprezentuje pojedynczą taryfę:

```python
class TariffEntry:
    operator: str           # Nazwa operatora
    name: str               # Nazwa taryfy
    rate: float             # Stawka w PLN/MWh
    effective_date: date    # Data wejścia w życie
    approval_date: date     # Data zatwierdzenia przez URE
    document_url: str       # Link do dokumentu
```

## Przykłady użycia

### Pobieranie aktualnych taryf

```python
from urzad_regulacji_energetyki.taryfy_i_inne_decyzje_energia_elektryczna import TariffAnalyzer

analyzer = TariffAnalyzer()

# Wszystkie aktualne taryfy
tariffs = analyzer.get_current_tariffs()

for tariff in tariffs:
    print(f"{tariff.operator}: {tariff.rate} PLN/MWh")
```

### Porównanie operatorów

```python
# Porównaj taryfy konkretnych operatorów
comparison = analyzer.compare_tariffs(
    operators=["PGE Dystrybucja", "Tauron Dystrybucja", "Enea Operator"]
)

for operator, tariff_info in comparison.items():
    print(f"{operator}:")
    print(f"  Średnia stawka: {tariff_info.average_rate:.2f} PLN/MWh")
    print(f"  Liczba taryf: {tariff_info.count}")
```

### Analiza historyczna

```python
from datetime import date

# Pobierz taryfy z określonego okresu
historical = analyzer.get_tariffs_by_date_range(
    start_date=date(2022, 1, 1),
    end_date=date(2023, 12, 31)
)

# Analiza trendu
import pandas as pd

df = pd.DataFrame([
    {'data': t.effective_date, 'stawka': t.rate, 'operator': t.operator}
    for t in historical
])

# Średnia stawka według miesiąca
monthly_avg = df.groupby(df['data'].dt.to_period('M'))['stawka'].mean()
print("Średnia miesięczna stawka:")
print(monthly_avg)
```

### Filtrowanie według operatora

```python
# Znajdź wszystkie taryfy konkretnego operatora
pge_tariffs = [
    t for t in tariffs
    if "PGE" in t.operator
]

print(f"Znaleziono {len(pge_tariffs)} taryf PGE")
```

## Typy taryf

Moduł obsługuje następujące typy taryf:

- **Taryfy dystrybucyjne** - za usługę przesyłu energii
- **Taryfy za przyłączenie** - opłaty przyłączeniowe
- **Taryfy dodatkowe** - inne opłaty

## Obsługa decyzji regulacyjnych

```python
# Pobierz decyzje dotyczące taryf
decisions = analyzer.get_regulatory_decisions(
    year=2023,
    decision_type="zatwierdzenie taryfy"
)

for decision in decisions:
    print(f"{decision.date}: {decision.title}")
    print(f"  Dotyczy: {decision.affected_operator}")
```

## Eksport danych

```python
import pandas as pd

# Eksport do CSV
df = pd.DataFrame([t.dict() for t in tariffs])
df.to_csv('taryfy_energia.csv', index=False, encoding='utf-8')

# Eksport do Excel z formatowaniem
with pd.ExcelWriter('taryfy_raport.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Taryfy', index=False)
```

## Obsługa błędów

```python
from urzad_regulacji_energetyki.exceptions import DataFetchError, InvalidOperatorError

try:
    tariffs = analyzer.get_current_tariffs()
except DataFetchError as e:
    print(f"Błąd pobierania danych: {e}")
except InvalidOperatorError as e:
    print(f"Nieprawidłowy operator: {e}")
```

## Zobacz również

- [API Reference](../api/taryfy.md) - Pełna dokumentacja API
- [Szybki start](../guide/quickstart.md) - Podstawowe przykłady
