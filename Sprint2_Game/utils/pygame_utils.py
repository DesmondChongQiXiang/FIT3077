"""
Utilities for pygame.

Author: Shen
"""


def get_coords_for_center_drawing_in_rect(rect_coords: tuple[int, int], rect_size: tuple[int, int], draw_size: tuple[int, int]) -> tuple[int, int]:
    """
    Get the coordinates to draw at to draw the element in the center for a rectangle shaped container.

    Args:
        rect_coords: The coordinates of the rectangle in form (x, y)
        rect_size: The size of the rectangle in form in pixels in form (width, height)
        draw_size: The size of the element to draw in pixels in form (width, height)

    Returns:
        The coordinates to draw at in form (x, y)
    """
    rect_x, rect_y = rect_coords
    rect_width, rect_height = rect_size
    draw_width, draw_height = draw_size

    rect_x0, rect_y0, rect_x1, rect_y1 = rect_x, rect_y, rect_x + rect_width, rect_y + rect_height
    rect_center_x, rect_center_y = int((rect_x0 + rect_x1) / 2), int((rect_y0 + rect_y1) / 2)
    draw_to_center_width, draw_to_center_height = int(draw_width / 2), int(draw_height / 2)

    return (rect_center_x - draw_to_center_width, rect_center_y - draw_to_center_height)
