"""Pytest configuration and shared fixtures."""

from typing import Any

import pytest


@pytest.fixture  # type: ignore[misc]
def sample_bulletin_change_data() -> dict[str, Any]:
    """Provide sample bulletin change data for testing."""
    return {
        "id": "test-001",
        "title": "Test Bulletin Entry",
        "description": "Test description",
        "change_type": "publication",
        "date_published": "2024-01-15T10:00:00",
        "category": "tariffs",
    }


@pytest.fixture  # type: ignore[misc]
def sample_tariff_data() -> dict[str, Any]:
    """Provide sample tariff data for testing."""
    return {
        "tariff_id": "tar-001",
        "tariff_code": "G11",
        "tariff_name": "Households - Standard",
        "tariff_type": "household",
        "operator_name": "Enea",
        "valid_from": "2024-01-01T00:00:00",
        "base_rate": 450.0,
    }


@pytest.fixture  # type: ignore[misc]
def sample_mioze_entry_data() -> dict[str, Any]:
    """Provide sample MIOZE entry data for testing."""
    return {
        "registration_id": "mioze-001",
        "owner_name": "John Doe",
        "owner_type": "individual",
        "energy_source": "photovoltaic",
        "installed_power_kw": 8.5,
        "location_voivodeship": "Mazovia",
        "location_gmina": "Warsaw",
        "status": "active",
        "registration_date": "2023-06-15T00:00:00",
        "connection_type": "grid",
        "feed_in_type": "net_metering",
    }
