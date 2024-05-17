"""Utils that deal with data obtained from the os.

Author: Shen
"""

import os
import ctypes

from enum import Enum


class ScreenDimension(Enum):
    """Describes screen dimensions (either width or height).

    Author: Shen
    """

    WIDTH = 0
    HEIGHT = 1


def nt_safe_value_for_screen_dimension(dimension: ScreenDimension) -> int:
    """Gets a safe screen dimension value for a windows computer. Safe means accounting for window screen elements
    (e.g task bar, title bar, etc.), with some added buffer.

    Args:
        dimension: The dimension for which to get the safe screen size

    Raises:
        Exception if the os is not Windows
    """
    if os.name == "nt":
        # Windows resolution configuration
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()  # ignore ui scaling
        user_screen_width, user_screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        if dimension == ScreenDimension.HEIGHT:
            return user_screen_height - user_screen_height * 0.1
        return user_screen_width

    raise Exception("Called on a non-windows OS.")
