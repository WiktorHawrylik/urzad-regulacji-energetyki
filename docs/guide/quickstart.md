# Quickstart

```python
from python_library_template import LibraryConfig, greet

config = LibraryConfig(project_name="python-library-template", enable_experimental=True)
print(greet("Codex", config=config))
```

Run tests:

```bash
make test
```
