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
