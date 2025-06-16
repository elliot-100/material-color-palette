from material_2014_colors import COLORS


def test_color_value() -> None:
    # arrange
    # act
    col = COLORS["red"]["700"]
    # assert
    assert col == "#d32f2f"
