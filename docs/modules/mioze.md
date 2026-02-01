# Rejestr MIOZE

Moduł do monitorowania i analizy małych instalacji odnawialnych źródeł energii (MIOZE).

## Przegląd

Moduł `rejestr_mioze` umożliwia:

- Pobieranie danych o małych instalacjach wytwórczych (≤50kW)
- Analizę rozmieszczenia geograficznego instalacji
- Statystyki według typu instalacji
- Monitoring rozwoju odnawialnych źródeł energii

## Główne komponenty

### MIOZERegistry

Główna klasa do pracy z rejestrem MIOZE.

```python
from urzad_regulacji_energetyki.rejestr_mioze import MIOZERegistry

registry = MIOZERegistry()

# Pobierz wszystkie instalacje
all_installations = registry.get_all_installations()
```

### Modele danych

#### MIOZEInstallation

Reprezentuje pojedynczą instalację MIOZE:

```python
class MIOZEInstallation:
    id: str                         # Unikalny identyfikator
    type: str                       # Typ instalacji (PV, wiatrowa, itp.)
    capacity_kw: float              # Moc zainstalowana w kW
    region: str                     # Województwo
    district: str                   # Powiat
    municipality: str               # Gmina
    installation_date: date         # Data instalacji
    status: str                     # Status (aktywna, zawieszona, itp.)
```

## Przykłady użycia

### Analiza regionalna

```python
from urzad_regulacji_energetyki.rejestr_mioze import MIOZERegistry

registry = MIOZERegistry()

# Pobierz instalacje w województwie
mazowieckie = registry.get_mioze_by_region("mazowieckie")
print(f"Liczba instalacji: {len(mazowieckie)}")

# Statystyki regionalne
regional_stats = registry.generate_regional_statistics()

for region, stats in regional_stats.items():
    print(f"\n{region}:")
    print(f"  Liczba instalacji: {stats.count}")
    print(f"  Całkowita moc: {stats.total_capacity_kw:.2f} kW")
    print(f"  Średnia moc: {stats.average_capacity_kw:.2f} kW")
    print(f"  Mediana mocy: {stats.median_capacity_kw:.2f} kW")
```

### Analiza według typu instalacji

```python
# Pobierz statystyki według typu
by_type = registry.analyze_by_installation_type()

print("Instalacje według typu:")
for install_type, data in by_type.items():
    print(f"\n{install_type}:")
    print(f"  Liczba: {data.count}")
    print(f"  Całkowita moc: {data.total_capacity_kw:.2f} kW")
    print(f"  Udział: {data.percentage:.1f}%")
```

### Analiza trendu instalacji

```python
from datetime import date, timedelta
import pandas as pd

# Pobierz instalacje z ostatniego roku
end_date = date.today()
start_date = end_date - timedelta(days=365)

recent = registry.get_installations_by_date_range(
    start_date=start_date,
    end_date=end_date
)

# Konwersja do DataFrame
df = pd.DataFrame([inst.dict() for inst in recent])

# Trend miesięczny
monthly_trend = df.groupby(
    df['installation_date'].dt.to_period('M')
).agg({
    'id': 'count',
    'capacity_kw': 'sum'
})

print("Nowe instalacje według miesięcy:")
print(monthly_trend)
```

### Mapa cieplna mocy zainstalowanej

```python
# Analiza na poziomie powiatów
district_data = registry.get_district_level_statistics()

import pandas as pd

df = pd.DataFrame([
    {
        'powiat': d.district,
        'województwo': d.region,
        'liczba': d.count,
        'moc_kW': d.total_capacity_kw
    }
    for d in district_data
])

# Top 10 powiatów według mocy
top_districts = df.nlargest(10, 'moc_kW')
print("\nTop 10 powiatów według mocy zainstalowanej:")
print(top_districts)
```

## Typy instalacji MIOZE

Rejestr obsługuje następujące typy instalacji:

- **PV (Fotowoltaika)** - panele słoneczne
- **Wiatrowe** - małe turbiny wiatrowe
- **Wodne** - mikroelektrownie wodne
- **Biogazowe** - instalacje biogazowe
- **Kogeneracja** - jednostki kogeneracyjne
- **Inne** - pozostałe OZE

## Filtrowanie danych

```python
# Znajdź instalacje według kryteriów
filtered = registry.filter_installations(
    min_capacity_kw=10.0,
    max_capacity_kw=50.0,
    installation_type="PV",
    region="małopolskie",
    status="aktywna"
)

print(f"Znaleziono {len(filtered)} instalacji spełniających kryteria")
```

## Statystyki i raporty

```python
# Generuj kompleksowy raport
report = registry.generate_comprehensive_report()

print(f"Całkowita liczba instalacji: {report.total_count}")
print(f"Całkowita moc zainstalowana: {report.total_capacity_mw:.2f} MW")
print(f"Średni rok instalacji: {report.average_installation_year}")

# Raport według województw
print("\nRozkład regionalny:")
for region_report in report.regional_breakdown:
    print(f"  {region_report.region}: {region_report.count} instalacji")
```

## Eksport danych

```python
import pandas as pd

# Pobierz wszystkie dane
all_data = registry.get_all_installations()

# Eksport do CSV
df = pd.DataFrame([inst.dict() for inst in all_data])
df.to_csv('mioze_rejestr.csv', index=False, encoding='utf-8')

# Eksport przestrzenny (GeoJSON) - jeśli dostępne współrzędne
if hasattr(registry, 'export_to_geojson'):
    registry.export_to_geojson('mioze_mapa.geojson')
```

## Obsługa błędów

```python
from urzad_regulacji_energetyki.exceptions import DataFetchError, InvalidRegionError

try:
    data = registry.get_mioze_by_region("nieprawidlowe_wojewodztwo")
except InvalidRegionError as e:
    print(f"Nieprawidłowa nazwa województwa: {e}")
except DataFetchError as e:
    print(f"Błąd pobierania danych: {e}")
```

## Zobacz również

- [API Reference](../api/mioze.md) - Pełna dokumentacja API
- [Szybki start](../guide/quickstart.md) - Podstawowe przykłady
- [Województwa Polski](https://pl.wikipedia.org/wiki/Podzia%C5%82_administracyjny_Polski) - Lista województw
