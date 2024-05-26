"""Math related utilities.

Author: Shen
"""

import math


def cos_deg(deg: float) -> float:
    """Calculates and returns cos(degrees).

    Args:
        deg: The degrees

    Returns:
        cos(degrees)
    """
    return math.cos(deg * (math.pi / 180))


def sin_deg(deg: float) -> float:
    """Calculates and returns sin(degrees).

    Args:
        deg: The degrees

    Returns:
        sin(degrees)
    """
    return math.sin(deg * (math.pi / 180))


def polygon_side_length_given_radius(radius: float, sides: int) -> float:
    """Returns the side length of a polygon given the radius and number of sides.

    Args:
        radius: The radius (length from center to vertex)
        sides: The number of sides composing the polygon

    Returns:
        The side length of the polygon
    """
    return 2 * radius * sin_deg(180 / sides)


def polygon_central_deg(sides: int) -> float:
    """Returns the central degrees of a polygon given the number of sides.

    Args:
        sides: The number of sides composing the polygon

    Returns:
        The central degrees of the polygon
    """
    return 360 / sides


def polygon_internal_deg(sides: int) -> float:
    """Returns the internal degrees of a polygon given the number of sides.

    Args:
        sides: The number of sides composing the polygon

    Returns:
        The central degrees of the polygon
    """
    return ((sides - 2) * 180) / sides
