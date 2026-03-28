"""Tests for geometric helper functions used in hit-testing and click targeting."""

from __future__ import annotations

import pytest

from gnome_ui_mcp.desktop.accessibility import _center, _contains_point
from gnome_ui_mcp.desktop.input import _StageArea


class TestContainsPoint:
    """_contains_point checks whether (x, y) falls within a bounding rectangle."""

    def test_none_bounds_returns_false(self) -> None:
        assert _contains_point(None, 10, 10) is False

    def test_point_inside(self) -> None:
        bounds = {"x": 0, "y": 0, "width": 100, "height": 100}
        assert _contains_point(bounds, 50, 50) is True

    def test_point_outside_right(self) -> None:
        bounds = {"x": 0, "y": 0, "width": 100, "height": 100}
        assert _contains_point(bounds, 100, 50) is False

    def test_point_outside_bottom(self) -> None:
        bounds = {"x": 0, "y": 0, "width": 100, "height": 100}
        assert _contains_point(bounds, 50, 100) is False

    def test_point_at_origin(self) -> None:
        bounds = {"x": 10, "y": 20, "width": 100, "height": 50}
        assert _contains_point(bounds, 10, 20) is True

    def test_point_outside_left(self) -> None:
        bounds = {"x": 10, "y": 20, "width": 100, "height": 50}
        assert _contains_point(bounds, 9, 25) is False

    def test_point_outside_above(self) -> None:
        bounds = {"x": 10, "y": 20, "width": 100, "height": 50}
        assert _contains_point(bounds, 50, 19) is False


class TestCenter:
    """_center computes the midpoint of a bounding rectangle."""

    def test_none_bounds_returns_none(self) -> None:
        assert _center(None) is None

    def test_empty_dict_returns_none(self) -> None:
        assert _center({}) is None

    def test_normal_bounds(self) -> None:
        bounds = {"x": 0, "y": 0, "width": 100, "height": 50}
        assert _center(bounds) == (50, 25)

    def test_offset_bounds(self) -> None:
        bounds = {"x": 100, "y": 200, "width": 40, "height": 20}
        assert _center(bounds) == (120, 210)

    def test_zero_width_uses_min_one(self) -> None:
        bounds = {"x": 50, "y": 50, "width": 0, "height": 10}
        cx, cy = _center(bounds)
        assert cx == 50
        assert cy == 55


class TestStageAreaLocalCoordinates:
    """_StageArea.local_coordinates transforms absolute to stage-local coords."""

    def test_origin_maps_to_zero(self) -> None:
        stage = _StageArea(origin_x=100, origin_y=200, width=1920, height=1080)
        assert stage.local_coordinates(100, 200) == (0.0, 0.0)

    def test_offset_maps_correctly(self) -> None:
        stage = _StageArea(origin_x=0, origin_y=0, width=1920, height=1080)
        assert stage.local_coordinates(960, 540) == (960.0, 540.0)

    def test_outside_raises(self) -> None:
        stage = _StageArea(origin_x=0, origin_y=0, width=1920, height=1080)
        with pytest.raises(ValueError, match="outside the desktop stage"):
            stage.local_coordinates(1920, 540)

    def test_negative_origin_outside_raises(self) -> None:
        stage = _StageArea(origin_x=100, origin_y=100, width=800, height=600)
        with pytest.raises(ValueError, match="outside the desktop stage"):
            stage.local_coordinates(50, 150)
