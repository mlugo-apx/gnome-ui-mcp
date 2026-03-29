"""Tests for click_element button parameter."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from gnome_ui_mcp.desktop import interaction


def _mock_target_resolution(element_id: str = "0/1/2") -> tuple:
    return (
        element_id,
        {"target_id": element_id, "target_role": "push button"},
        None,
    )


def _mock_accessible() -> MagicMock:
    mock = MagicMock()
    mock.do_action.return_value = True
    return mock


class TestClickElementButton:
    def test_default_left_uses_action(self) -> None:
        mock_accessible = _mock_accessible()

        with (
            patch.object(
                interaction,
                "_resolve_target_with_recovery",
                return_value=_mock_target_resolution(),
            ),
            patch.object(
                interaction.accessibility,
                "_resolve_element",
                return_value=mock_accessible,
            ),
            patch.object(
                interaction.accessibility,
                "_find_action_index",
                return_value=0,
            ),
            patch.object(interaction, "_effect_context", return_value={}),
            patch.object(
                interaction,
                "_verify_effect",
                return_value=(True, {"reason": "changed"}),
            ),
            patch.object(
                interaction.accessibility,
                "_safe_call",
                return_value="click",
            ),
        ):
            result = interaction.click_element("0/1/2")

        assert result["method"] == "action"

    def test_right_button_skips_action_uses_mouse(self) -> None:
        mock_accessible = _mock_accessible()
        bounds = {"x": 100, "y": 100, "width": 50, "height": 30}
        mouse_result = {"success": True, "x": 125, "y": 115}
        mock_mouse = MagicMock(return_value=mouse_result)

        with (
            patch.object(
                interaction,
                "_resolve_target_with_recovery",
                return_value=_mock_target_resolution(),
            ),
            patch.object(
                interaction.accessibility,
                "_resolve_element",
                return_value=mock_accessible,
            ),
            patch.object(
                interaction.accessibility,
                "_element_bounds",
                return_value=bounds,
            ),
            patch.object(
                interaction.accessibility,
                "_center",
                return_value=(125, 115),
            ),
            patch.object(interaction, "_effect_context", return_value={}),
            patch.object(
                interaction,
                "_verify_effect",
                return_value=(True, {"reason": "changed"}),
            ),
            patch.object(
                interaction.input,
                "perform_mouse_click",
                mock_mouse,
            ),
        ):
            result = interaction.click_element("0/1/2", button="right")

        assert result["method"] == "mouse"
        mock_mouse.assert_called_once_with(125, 115, button="right", click_count=1)

    def test_middle_button_works(self) -> None:
        mock_accessible = _mock_accessible()
        bounds = {"x": 50, "y": 50, "width": 100, "height": 40}
        mouse_result = {"success": True, "x": 100, "y": 70}
        mock_mouse = MagicMock(return_value=mouse_result)

        with (
            patch.object(
                interaction,
                "_resolve_target_with_recovery",
                return_value=_mock_target_resolution(),
            ),
            patch.object(
                interaction.accessibility,
                "_resolve_element",
                return_value=mock_accessible,
            ),
            patch.object(
                interaction.accessibility,
                "_element_bounds",
                return_value=bounds,
            ),
            patch.object(
                interaction.accessibility,
                "_center",
                return_value=(100, 70),
            ),
            patch.object(interaction, "_effect_context", return_value={}),
            patch.object(
                interaction,
                "_verify_effect",
                return_value=(True, {"reason": "changed"}),
            ),
            patch.object(
                interaction.input,
                "perform_mouse_click",
                mock_mouse,
            ),
        ):
            result = interaction.click_element("0/1/2", button="middle")

        assert result["method"] == "mouse"
        mock_mouse.assert_called_once_with(100, 70, button="middle", click_count=1)
