from screen.PygameScreenController import PygameScreenController

"""
Module containing all the singletons of the app.

TODO: Singletons may be moved into metaclasses at a later date

Author: Shen
"""

# Private singleton variables
__PygameScreenController_shared = None


# Singleton instantiations
def PygameScreenController_instance() -> PygameScreenController:
    """Returns the PygameScreenController instance. Creates the pygame screen controller instance if it doesn't exist 
    and returns it."""
    global __PygameScreenController_shared

    if __PygameScreenController_shared is not None:
        return __PygameScreenController_shared
    else:
        __PygameScreenController_shared = PygameScreenController()
        return __PygameScreenController_shared
