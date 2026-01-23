"""Test the full workflow of the package."""


class TestIntegration:
    """Integration test cases."""

    def test_all_modules_importable(self) -> None:
        """Test that all main modules can be imported."""
        from urzad_regulacji_energetyki import (
            biuletyn_informacji_publicznej_changelog,
            rejestr_mioze,
            taryfy_i_inne_decyzje_energia_elektryczna,
        )

        assert biuletyn_informacji_publicznej_changelog is not None
        assert taryfy_i_inne_decyzje_energia_elektryczna is not None
        assert rejestr_mioze is not None
