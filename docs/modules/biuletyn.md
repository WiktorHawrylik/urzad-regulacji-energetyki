# Biuletyn Informacji Publicznej - Rejestr Zmian

Moduł do śledzenia i analizy zmian opublikowanych w Biuletynie Informacji Publicznej URE.

## Przegląd

Moduł `biuletyn_informacji_publicznej_changelog` umożliwia:

- Automatyczne pobieranie zmian z BIP URE
- Analizę historyczną publikowanych dokumentów
- Filtrowanie i wyszukiwanie konkretnych decyzji
- Generowanie raportów o zmianach

## Główne komponenty

### BulletinChangelogAnalyzer

Główna klasa do analizy zmian w biuletynie.

```python
from urzad_regulacji_energetyki.biuletyn_informacji_publicznej_changelog import BulletinChangelogAnalyzer
from datetime import date

analyzer = BulletinChangelogAnalyzer()

# Analiza zmian w określonym okresie
changes = analyzer.analyze_changes(
    start_date=date(2023, 1, 1),
    end_date=date(2023, 12, 31)
)
```

### Modele danych

#### ChangelogEntry

Reprezentuje pojedynczą zmianę w BIP:

```python
class ChangelogEntry:
    date: date              # Data publikacji
    title: str              # Tytuł zmiany
    category: str           # Kategoria dokumentu
    url: str                # Link do pełnego dokumentu
    description: str        # Opis zmiany
```

## Przykłady użycia

### Podstawowe wyszukiwanie

```python
from urzad_regulacji_energetyki.biuletyn_informacji_publicznej_changelog import BulletinChangelogAnalyzer
from datetime import date, timedelta

analyzer = BulletinChangelogAnalyzer()

# Pobierz zmiany z ostatnich 30 dni
end_date = date.today()
start_date = end_date - timedelta(days=30)

recent_changes = analyzer.analyze_changes(
    start_date=start_date,
    end_date=end_date
)

for change in recent_changes:
    print(f"{change.date}: {change.title}")
```

### Filtrowanie według kategorii

```python
# Znajdź wszystkie decyzje regulacyjne
decisions = [
    change for change in changes
    if "decyzja" in change.category.lower()
]

print(f"Znaleziono {len(decisions)} decyzji")
```

### Generowanie raportu

```python
from collections import Counter

# Analiza według kategorii
categories = Counter(change.category for change in changes)

print("Rozkład zmian według kategorii:")
for category, count in categories.most_common():
    print(f"  {category}: {count}")
```

### Eksport do pandas

```python
import pandas as pd

# Konwersja do DataFrame
df = pd.DataFrame([
    {
        'data': change.date,
        'tytul': change.title,
        'kategoria': change.category,
        'url': change.url
    }
    for change in changes
])

# Zapisz do CSV
df.to_csv('zmiany_bip.csv', index=False, encoding='utf-8')
```

## Obsługiwane kategorie

Moduł rozpoznaje następujące kategorie dokumentów:

- Decyzje regulacyjne
- Obwieszczenia
- Komunikaty
- Zarządzenia
- Uchwały
- Inne dokumenty

## Obsługa błędów

```python
from urzad_regulacji_energetyki.exceptions import DataFetchError

try:
    changes = analyzer.analyze_changes(
        start_date=date(2023, 1, 1),
        end_date=date(2023, 12, 31)
    )
except DataFetchError as e:
    print(f"Nie udało się pobrać danych: {e}")
```

## Zobacz również

- [API Reference](../api/biuletyn.md) - Pełna dokumentacja API
- [Szybki start](../guide/quickstart.md) - Podstawowe przykłady
