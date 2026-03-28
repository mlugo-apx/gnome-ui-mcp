"""Tests for key combination parsing and modifier validation."""

from __future__ import annotations

import pytest

from gnome_ui_mcp.desktop.input import _parse_key_combo, _validate_modifiers


class TestParseKeyCombo:
    """_parse_key_combo must split modifier+key combos and reject invalid input."""

    def test_empty_string_raises(self) -> None:
        with pytest.raises(ValueError, match="must not be empty"):
            _parse_key_combo("")

    def test_whitespace_only_raises(self) -> None:
        with pytest.raises(ValueError, match="must not be empty"):
            _parse_key_combo("   ")

    def test_single_modifier_returns_no_principal(self) -> None:
        modifiers, principal = _parse_key_combo("ctrl")
        assert len(modifiers) == 1
        assert principal is None

    def test_modifier_plus_key(self) -> None:
        modifiers, principal = _parse_key_combo("ctrl+c")
        assert len(modifiers) == 1
        assert principal is not None

    def test_multiple_modifiers_plus_key(self) -> None:
        modifiers, principal = _parse_key_combo("ctrl+shift+t")
        assert len(modifiers) == 2
        assert principal is not None

    def test_non_modifier_in_middle_raises(self) -> None:
        with pytest.raises(ValueError, match="must be the last token"):
            _parse_key_combo("ctrl+x+shift")

    def test_unknown_key_raises(self) -> None:
        with pytest.raises(ValueError, match="Unknown key"):
            _parse_key_combo("ctrl+NOT_A_REAL_KEY_12345")

    def test_duplicate_modifiers_deduplicated(self) -> None:
        modifiers, _ = _parse_key_combo("ctrl+control")
        assert len(modifiers) == 1

    def test_single_key_no_modifiers(self) -> None:
        modifiers, principal = _parse_key_combo("Return")
        assert modifiers == []
        assert principal is not None


class TestValidateModifiers:
    """_validate_modifiers must map names to keyvals and reject unknowns."""

    def test_valid_modifier(self) -> None:
        keyvals = _validate_modifiers(["ctrl"])
        assert len(keyvals) == 1
        assert all(isinstance(kv, int) for kv in keyvals)

    def test_unknown_modifier_raises(self) -> None:
        with pytest.raises(ValueError, match="Unknown modifier"):
            _validate_modifiers(["not_a_modifier"])

    def test_duplicates_deduplicated(self) -> None:
        keyvals = _validate_modifiers(["ctrl", "control"])
        assert len(keyvals) == 1

    def test_multiple_distinct_modifiers(self) -> None:
        keyvals = _validate_modifiers(["ctrl", "shift", "alt"])
        assert len(keyvals) == 3
