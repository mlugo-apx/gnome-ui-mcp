"""Tests for BUG-9: _verified_result_after_settle overwrites verified=True when shell unsettled."""

from __future__ import annotations

from typing import Any
from unittest.mock import patch

from gnome_ui_mcp.desktop.interaction import (
    _verified_result_after_settle,
    _verify_effect,
)

JsonDict = dict[str, Any]


class TestVerifyEffect:
    """Baseline: _verify_effect behavior is correct on its own."""

    def test_popup_change_returns_true(self) -> None:
        before: JsonDict = {"shell_popups": ["popup-A"]}
        after: JsonDict = {"shell_popups": ["popup-A", "popup-B"]}
        verified, detail = _verify_effect(before, after)
        assert verified is True
        assert detail["reason"] == "shell_popups_changed"

    def test_no_change_returns_none(self) -> None:
        before: JsonDict = {"shell_popups": []}
        after: JsonDict = {"shell_popups": []}
        verified, detail = _verify_effect(before, after)
        assert verified is None
        assert detail["reason"] == "no_observable_change"

    def test_target_disappeared_returns_true(self) -> None:
        before: JsonDict = {"shell_popups": [], "element": {"id": "e1", "exists": True}}
        after: JsonDict = {"shell_popups": [], "element": {"id": "e1", "exists": False}}
        verified, detail = _verify_effect(before, after)
        assert verified is True
        assert detail["reason"] == "target_disappeared"


class TestVerifiedResultAfterSettle:
    """The core bug: settle failure must not overwrite a positive verification."""

    def _mock_settle(
        self,
        *,
        verify_result: tuple[bool | None, JsonDict],
        settled_success: bool,
    ) -> JsonDict:
        """Call _verified_result_after_settle with controlled mocks."""
        settled_response: JsonDict = {
            "success": settled_success,
            "stable_for_ms": 250,
            "popups": [],
            "popup_count": 0,
            "signature": [],
        }
        after_context: JsonDict = {"shell_popups": []}

        with (
            patch(
                "gnome_ui_mcp.desktop.interaction._settled_effect_context",
                return_value=(after_context, settled_response),
            ),
            patch(
                "gnome_ui_mcp.desktop.interaction._verify_effect",
                return_value=verify_result,
            ),
        ):
            return _verified_result_after_settle(
                {"method": "test"},
                before={"shell_popups": []},
                element_id=None,
                input_injected=True,
            )

    def test_verified_true_and_settled_true_gives_success(self) -> None:
        result = self._mock_settle(
            verify_result=(True, {"reason": "shell_popups_changed"}),
            settled_success=True,
        )
        assert result["effect_verified"] is True
        assert result["success"] is True

    def test_verified_true_and_settled_false_preserves_verified(self) -> None:
        """THE BUG: verified=True must NOT be overwritten to False."""
        result = self._mock_settle(
            verify_result=(True, {"reason": "shell_popups_changed"}),
            settled_success=False,
        )
        assert result["effect_verified"] is True
        assert result["success"] is True

    def test_verified_none_and_settled_false_gives_failure(self) -> None:
        """When no positive evidence exists, settle failure should downgrade."""
        result = self._mock_settle(
            verify_result=(None, {"reason": "no_observable_change"}),
            settled_success=False,
        )
        assert result["effect_verified"] is False
        assert result["success"] is False

    def test_verified_false_and_settled_false_stays_false(self) -> None:
        result = self._mock_settle(
            verify_result=(False, {"reason": "no_observable_change_in_gnome_shell"}),
            settled_success=False,
        )
        assert result["effect_verified"] is False
        assert result["success"] is False
