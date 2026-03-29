"""Tests for select_option tool."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from gnome_ui_mcp.desktop import accessibility


class TestSelectOption:
    def test_selects_child(self) -> None:
        mock_accessible = MagicMock()
        mock_sel = MagicMock()
        mock_accessible.get_selection_iface.return_value = mock_sel
        mock_sel.select_child.return_value = True
        mock_sel.get_n_selected_children.return_value = 1
        mock_child = MagicMock()
        mock_child.get_name.return_value = "Option A"
        mock_child.get_role_name.return_value = "list item"
        mock_sel.get_selected_child.return_value = mock_child

        with patch.object(accessibility, "_resolve_element", return_value=mock_accessible):
            result = accessibility.select_option("0/1/2", 0)

        assert result["success"] is True
        mock_sel.select_child.assert_called_once_with(0)

    def test_no_selection_iface_error(self) -> None:
        mock_accessible = MagicMock()
        mock_accessible.get_selection_iface.return_value = None

        with patch.object(accessibility, "_resolve_element", return_value=mock_accessible):
            result = accessibility.select_option("0/1/2", 0)

        assert result["success"] is False
        assert "selection" in result["error"].lower()

    def test_invalid_index_error(self) -> None:
        mock_accessible = MagicMock()
        mock_sel = MagicMock()
        mock_accessible.get_selection_iface.return_value = mock_sel
        mock_sel.select_child.return_value = False

        with patch.object(accessibility, "_resolve_element", return_value=mock_accessible):
            result = accessibility.select_option("0/1/2", 999)

        assert result["success"] is False

    def test_returns_selected_item(self) -> None:
        mock_accessible = MagicMock()
        mock_sel = MagicMock()
        mock_accessible.get_selection_iface.return_value = mock_sel
        mock_sel.select_child.return_value = True
        mock_sel.get_n_selected_children.return_value = 1
        mock_child = MagicMock()
        mock_child.get_name.return_value = "Item B"
        mock_child.get_role_name.return_value = "menu item"
        mock_sel.get_selected_child.return_value = mock_child

        with patch.object(accessibility, "_resolve_element", return_value=mock_accessible):
            result = accessibility.select_option("0/1/2", 1)

        assert result["selected_item"]["name"] == "Item B"
        assert result["selected_item"]["role"] == "menu item"
