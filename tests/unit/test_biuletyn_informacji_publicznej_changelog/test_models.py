"""Unit tests for the models module."""

from urzad_regulacji_energetyki.biuletyn_informacji_publicznej_changelog.models import BulletinChange, ChangeType


class TestBulletinChange:
    """Test cases for BulletinChange model."""

    def test_bulletin_change_creation(self, sample_bulletin_change_data: dict) -> None:
        """Test creating a bulletin change instance."""
        change = BulletinChange(
            id=sample_bulletin_change_data["id"],
            title=sample_bulletin_change_data["title"],
            change_type=ChangeType.PUBLICATION,
            date_published="2024-01-15T10:00:00",
        )
        assert change.id == "test-001"
        assert change.title == "Test Bulletin Entry"

    def test_bulletin_change_types(self) -> None:
        """Test all available change types."""
        assert ChangeType.PUBLICATION.value == "publication"
        assert ChangeType.UPDATE.value == "update"
        assert ChangeType.REMOVAL.value == "removal"
        assert ChangeType.MODIFICATION.value == "modification"
