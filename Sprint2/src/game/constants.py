from .animal import Animal
# Window Configuration
WIDTH, HEIGHT = 1280, 720 # Width and height of the game window
SCREEN_WIDTH = 1280 # Width of the game screen
SCREEN_HEIGHT = 720 # Height of the game screen

# Number of rows and columns in the screen
ROWS = 9 # Number of rows in the grid
COLS = 9 # Number of columns in the grid

# Calculate cell dimensions
CELL_WIDTH = SCREEN_WIDTH // COLS # Width of each grid cell
CELL_HEIGHT = SCREEN_HEIGHT // ROWS # Height of each grid cell

# the number of tiles
TILES_NUM = 24
# Define the tiles row and column order from top-left clockwise until the end
TILES_ROW_COLUMN = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
                    (1,7),(2,7),(3,7),(4,7),(5,7),(6,7),
                    (7,7),(7,6),(7,5),(7,4),(7,3),(7,2),
                    (7,1),(6,1),(5,1),(4,1),(3,1),(2,1)]
# tiles position
TILES_POS = [(row_column[1] * CELL_WIDTH, row_column[0] * CELL_HEIGHT) for row_column in TILES_ROW_COLUMN]

# Define the tiles animal order from top-left clockwise until the end
TILES_ANIMAL_ORDERING = [Animal.BABYDRAGON,Animal.SPIDER,Animal.BABYDRAGON,Animal.BAT,Animal.SPIDER,Animal.SPIDER,
                         Animal.BAT,Animal.SALAMANDER,Animal.SALAMANDER,Animal.SPIDER,Animal.BAT,Animal.BABYDRAGON,
                         Animal.SALAMANDER,Animal.BAT,Animal.SPIDER,Animal.SALAMANDER,Animal.BABYDRAGON,Animal.BAT,
                         Animal.BABYDRAGON,Animal.SALAMANDER,Animal.BAT,Animal.SPIDER,Animal.BABYDRAGON,Animal.SALAMANDER]

# caves and dragon row and column
CAVES_DRAGON_ROW_COLUMN = [(4, 0), (4, 8), (0, 4), (8, 4)]
# caves and dragonposition
CAVES_DRAGON_POS = [(row_column[1] * CELL_WIDTH, row_column[0] * CELL_HEIGHT) for row_column in CAVES_DRAGON_ROW_COLUMN]
# caves's animal(from cave 1 to cave 4)
CAVES_ANIMAL = [Animal.SALAMANDER,Animal.SPIDER,Animal.BAT,Animal.BABYDRAGON]

# chit card row position range
CHITCARD_ROW_RANGE = range(2,7)
# chit card column position range
CHITCARD_COL_RANGE = range(2,7)


