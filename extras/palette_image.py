"""Generate a palette image.

Run with: `uv run extras/palette_image.py --reinstall-package material_color_palette`
"""

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pillow>=12.2.0",
#     "material-color-palette>=1.1.0",
# ]
# ///
from itertools import batched

from PIL import Image, ImageDraw

from material_color_palette import _COLORS, Color, _shades

WIDTH = 1240
COLUMN_COUNT = 6
GRID_CELL_SIZE = 32
COL_WIDTH_CELLS = 6
SPACING_FACTOR = 0.5

_MAX_SHADES = max(len(shades) for shades in _COLORS.values())
_ROW_HEIGHT = int((_MAX_SHADES + SPACING_FACTOR) * GRID_CELL_SIZE)
_ROW_COUNT = len(_COLORS.keys()) // COLUMN_COUNT
_HEIGHT = _ROW_COUNT * _ROW_HEIGHT
_TEXT_OFFSET = GRID_CELL_SIZE / 4, GRID_CELL_SIZE / 3


def main() -> None:
    """Run the script."""
    image = Image.new("RGB", (WIDTH, _HEIGHT), "white")
    with image:
        draw = ImageDraw.Draw(image)
        for row_index, color_names_batch in enumerate(
            batched(_COLORS.keys(), COLUMN_COUNT)  # `batched` requires Python 3.12
        ):
            row_y = row_index * _ROW_HEIGHT

            for column_index, color_name in enumerate(color_names_batch):
                col_x = (
                    column_index * (COL_WIDTH_CELLS + SPACING_FACTOR) * GRID_CELL_SIZE
                )
                _draw_color(draw, color_name, col_x, row_y)

        image.show()


def _draw_color(draw: ImageDraw.Draw, color_name: str, x: float, y: int) -> None:
    """Draw all shades of a color."""
    color_name_display = color_name.replace("_", " ").title()

    for shade_row_index, shade in enumerate(_shades(color_name)):
        color = Color(color_name, shade)
        shade_y = y + (shade_row_index * GRID_CELL_SIZE)
        draw.rectangle(
            [
                (x, shade_y),
                (x + COL_WIDTH_CELLS * GRID_CELL_SIZE, shade_y + GRID_CELL_SIZE),
            ],
            color.rgb,
        )
        label_ = f"{color_name_display} {shade}" if shade_row_index == 0 else f"{shade}"
        fill_ = "white" if shade in (700, 800, 900) else "black"

        draw.text(
            (x + _TEXT_OFFSET[0], shade_y + _TEXT_OFFSET[1]),
            text=label_,
            fill=fill_,
        )


if __name__ == "__main__":
    main()
