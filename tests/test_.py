"""The tests module."""

import pytest

from material_2014_colors import Color


def test_construct_color() -> None:
    """`Color` can be constructed from `name` and `shade` string."""
    # arrange
    # act
    c = Color("red", "700")
    # assert
    assert c.rgb == (211, 47, 47)


def test_construct_color__int_shade() -> None:
    """`Color` can be constructed from `name` and `shade` int."""
    # arrange
    # act
    c = Color("pink", 900)
    # assert
    assert c.rgb == (136, 14, 79)


def test_construct_color__color_only() -> None:
    """`Color` can be constructed from `name` alone for some values."""
    # arrange
    # act
    c0 = Color("black")
    c1 = Color("white")
    # assert
    assert c0.rgb == (0, 0, 0)
    assert c1.rgb == (255, 255, 255)


def test_construct_color__missing_shade_raises_exception() -> None:
    """When `Color` can't be constructed from `name` alone, exception is raised."""
    # arrange
    # act, assert
    with pytest.raises(
        ValueError, match="Shade must be specified for Material color 'lime'."
    ):
        Color("lime")


def test_construct_color__incorrect_name_raises_exception() -> None:
    """When `name` isn't valid, exception is raised."""
    # arrange
    # act, assert
    with pytest.raises(
        ValueError, match="'dark_blue' isn't a valid Material color name."
    ):
        Color("dark_blue", "300")


def test_construct_color__incorrect_shade_raises_exception() -> None:
    """When `shade` isn't valid for `name`, exception is raised."""
    # arrange
    # act, assert
    with pytest.raises(
        ValueError, match="'250' isn't a valid shade for Material color 'blue_gray'."
    ):
        Color("blue_gray", "250")
