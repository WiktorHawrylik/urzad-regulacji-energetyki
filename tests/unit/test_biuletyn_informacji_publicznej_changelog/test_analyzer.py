"""Unit tests for the analyzer module."""

from urzad_regulacji_energetyki.biuletyn_informacji_publicznej_changelog.analyzer import BulletinChangelogAnalyzer


class TestBulletinChangelogAnalyzer:
    """Test cases for BulletinChangelogAnalyzer."""

    def test_analyzer_initialization(self) -> None:
        """Test analyzer initialization."""
        analyzer = BulletinChangelogAnalyzer()
        assert analyzer.base_url == "https://bip.ure.gov.pl"

    def test_analyzer_context_manager(self) -> None:
        """Test analyzer as context manager."""
        with BulletinChangelogAnalyzer() as analyzer:
            assert analyzer is not None
