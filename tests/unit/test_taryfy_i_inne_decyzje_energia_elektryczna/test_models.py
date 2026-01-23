"""Unit tests for the models module."""


from urzad_regulacji_energetyki.taryfy_i_inne_decyzje_energia_elektryczna.models import Tariff, TariffType


class TestTariff:
    """Test cases for Tariff model."""

    def test_tariff_creation(self, sample_tariff_data: dict) -> None:
        """Test creating a tariff instance."""
        tariff = Tariff(
            tariff_id=sample_tariff_data["tariff_id"],
            tariff_code=sample_tariff_data["tariff_code"],
            tariff_name=sample_tariff_data["tariff_name"],
            tariff_type=TariffType.HOUSEHOLD,
            operator_name=sample_tariff_data["operator_name"],
            valid_from="2024-01-01T00:00:00",
            base_rate=sample_tariff_data["base_rate"],
        )
        assert tariff.tariff_code == "G11"
        assert tariff.base_rate == 450.0

    def test_tariff_types(self) -> None:
        """Test available tariff types."""
        assert TariffType.HOUSEHOLD.value == "household"
        assert TariffType.BUSINESS.value == "business"
        assert TariffType.INDUSTRIAL.value == "industrial"
