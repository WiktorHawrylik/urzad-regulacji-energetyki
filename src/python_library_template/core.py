"""Core primitives for the template project."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class LibraryConfig:
    """Configuration for the template library."""

    project_name: str
    enable_experimental: bool = False


def greet(name: str, config: Optional[LibraryConfig] = None) -> str:
    """Return a friendly greeting.

    Args:
        name: Name to greet.
        config: Optional configuration metadata.

    Returns:
        A greeting message.
    """

    config_suffix = " (experimental enabled)" if config and config.enable_experimental else ""
    return f"Hello, {name}!{config_suffix}"
