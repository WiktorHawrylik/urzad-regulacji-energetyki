"""Unit tests for the models module."""

from urzad_regulacji_energetyki.rejestr_mioze.models import MIOZEEntry, MIOZESource, MIOZEStatus


class TestMIOZEEntry:
    """Test cases for MIOZEEntry model."""

    def test_mioze_entry_creation(self, sample_mioze_entry_data: dict) -> None:
        """Test creating a MIOZE entry instance."""
        entry = MIOZEEntry(
            registration_id=sample_mioze_entry_data["registration_id"],
            owner_name=sample_mioze_entry_data["owner_name"],
            owner_type=sample_mioze_entry_data["owner_type"],
            energy_source=MIOZESource.PHOTOVOLTAIC,
            installed_power_kw=sample_mioze_entry_data["installed_power_kw"],
            location_voivodeship=sample_mioze_entry_data["location_voivodeship"],
            location_gmina=sample_mioze_entry_data["location_gmina"],
            status=MIOZEStatus.ACTIVE,
            registration_date="2023-06-15T00:00:00",
            connection_type=sample_mioze_entry_data["connection_type"],
            feed_in_type=sample_mioze_entry_data["feed_in_type"],
        )
        assert entry.registration_id == "mioze-001"
        assert entry.installed_power_kw == 8.5

    def test_mioze_sources(self) -> None:
        """Test available MIOZE energy sources."""
        assert MIOZESource.PHOTOVOLTAIC.value == "photovoltaic"
        assert MIOZESource.WIND.value == "wind"
        assert MIOZESource.HYBRID.value == "hybrid"

    def test_mioze_status(self) -> None:
        """Test available MIOZE statuses."""
        assert MIOZEStatus.ACTIVE.value == "active"
        assert MIOZEStatus.INACTIVE.value == "inactive"
        assert MIOZEStatus.DEREGISTERED.value == "deregistered"
