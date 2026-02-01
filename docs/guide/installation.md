# Instalacja

## Wymagania

- Python 3.9 lub nowszy
- `uv` lub `pip` jako menedżer pakietów

## Instalacja z PyPI

Najprostszy sposób instalacji biblioteki to użycie PyPI:

```bash
# Używając uv (zalecane - najszybsze)
uv pip install urzad-regulacji-energetyki

# Lub używając pip
pip install urzad-regulacji-energetyki
```

## Instalacja ze źródła

### Instalacja standardowa

```bash
git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
cd urzad-regulacji-energetyki

# Używając uv
uv pip install .

# Lub używając pip
pip install .
```

### Instalacja w trybie edycji (dla deweloperów)

```bash
# Używając uv (tworzy dowiązania symboliczne do katalogu src)
uv pip install -e .

# Lub używając pip
pip install -e .
```

## Instalacja dla deweloperów

Jeśli planujesz wnosić zmiany do projektu:

```bash
git clone https://github.com/WiktorHawrylik/urzad-regulacji-energetyki.git
cd urzad-regulacji-energetyki

# Zainstaluj uv (jeśli jeszcze nie masz)
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS
# Lub na macOS z Homebrew: brew install uv

# Zainstaluj projekt z wszystkimi zależnościami deweloperskimi
uv sync --extra dev --extra test --extra docs

# Zainstaluj hooki pre-commit
uv run pre-commit install
```

## Weryfikacja instalacji

Sprawdź, czy instalacja przebiegła pomyślnie:

```python
import urzad_regulacji_energetyki

print(urzad_regulacji_energetyki.__version__)
```

## Opcjonalne zależności

Projekt oferuje kilka grup opcjonalnych zależności:

```bash
# Narzędzia deweloperskie
uv pip install urzad-regulacji-energetyki[dev]

# Narzędzia testowe
uv pip install urzad-regulacji-energetyki[test]

# Narzędzia do budowania dokumentacji
uv pip install urzad-regulacji-energetyki[docs]

# Wszystkie opcjonalne zależności
uv pip install urzad-regulacji-energetyki[dev,test,docs]
```

## Troubleshooting

### Problem z instalacją lxml

Jeśli napotkasz problemy z instalacją `lxml`, upewnij się, że masz zainstalowane wymagane biblioteki systemowe:

=== "Ubuntu/Debian"
    ```bash
    sudo apt-get install libxml2-dev libxslt-dev python3-dev
    ```

=== "macOS"
    ```bash
    brew install libxml2 libxslt
    ```

=== "Windows"
    Pobierz prekompilowane pakiety wheels z [https://www.lfd.uci.edu/~gohlke/pythonlibs/](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
