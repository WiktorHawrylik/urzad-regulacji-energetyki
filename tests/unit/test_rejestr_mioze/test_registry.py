"""Unit tests for the registry module."""

from urzad_regulacji_energetyki.rejestr_mioze.registry import MIOZERegistry


class TestMIOZERegistry:
    """Test cases for MIOZERegistry."""

    def test_registry_initialization(self) -> None:
        """Test registry initialization."""
        registry = MIOZERegistry()
        assert registry.base_url == "https://mioze.ure.gov.pl"

    def test_registry_context_manager(self) -> None:
        """Test registry as context manager."""
        with MIOZERegistry() as registry:
            assert registry is not None
