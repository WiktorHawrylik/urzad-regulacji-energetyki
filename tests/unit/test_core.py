from python_library_template.core import LibraryConfig, greet


def test_greet_defaults() -> None:
    assert greet("Codex") == "Hello, Codex!"


def test_greet_with_config() -> None:
    config = LibraryConfig(project_name="python-library-template", enable_experimental=True)
    assert greet("Codex", config=config) == "Hello, Codex! (experimental enabled)"
