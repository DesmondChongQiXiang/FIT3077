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


def polygon_radius_given_side_length(side_length: float, sides: int) -> float:
    """Returns the radius of a regular polygon given the side length of one of its sides.

    Args:
        side_length: The side length
        sides: The number of sides composing the polygon

    Returns:
        The radius (length from center to vertex) of the polygon
    """
    return side_length / (2 * sin_deg(180 / sides))


def polygon_side_length_given_radius(radius: float, sides: int) -> float:
    """Returns the side length of a regular polygon given the radius (length from center to vertex) of the polygon.

    Args:
        radius: The radius
        sides: The number of sides composing the polygon

    Returns:
        The side length of the regular polygon
    """
    return 2 * radius * sin_deg(180 / sides)


def polygon_central_deg(sides: int) -> float:
    """Returns the central degrees of a regular polygon given the number of sides.

    Args:
        sides: The number of sides composing the polygon

    Returns:
        The central degrees of the polygon
    """
    return 360 / sides


def polygon_internal_deg(sides: int) -> float:
    """Returns the internal degrees of a regular polygon given the number of sides.

    Args:
        sides: The number of sides composing the polygon

    Returns:
        The central degrees of the polygon
    """
    return ((sides - 2) * 180) / sides


def square_in_circle_apothem(radius: float) -> float:
    """Returns the apothem (inradius) for a square that is in a circle.

    Args:
        radius: The radius of the bounding circle

    Returns:
        The apothem (inradius)
    """
    return (radius * math.sqrt(2)) / 2
