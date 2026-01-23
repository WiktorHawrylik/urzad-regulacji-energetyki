"""Unit tests for the analyzer module."""

from urzad_regulacji_energetyki.taryfy_i_inne_decyzje_energia_elektryczna.analyzer import TariffAnalyzer


class TestTariffAnalyzer:
    """Test cases for TariffAnalyzer."""

    def test_analyzer_initialization(self) -> None:
        """Test analyzer initialization."""
        analyzer = TariffAnalyzer()
        assert analyzer.base_url == "https://ure.gov.pl"

    def test_analyzer_context_manager(self) -> None:
        """Test analyzer as context manager."""
        with TariffAnalyzer() as analyzer:
            assert analyzer is not None
