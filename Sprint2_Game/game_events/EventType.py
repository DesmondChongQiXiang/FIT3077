from enum import Enum


class EventType(Enum):
    """Represents the events that can occur in the game"""

    WIN = 1                     # Represents a win by a player
    MOVE_ACTION_FIRED = 2       # Represents a move action (i.e action to move a character) that was fired