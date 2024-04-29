import random
from constants import CELL_WIDTH,CELL_HEIGHT
from chitcard import ForwardChitCard, BackwardChitCard
from cave import Cave
from tile import Tile
from animal import Animal
from dragontoken import DragonToken

class GameBoard:
    """
    GameBoard Class

    Represents the game board containing tiles, chit cards, caves, and dragon tokens.

    Attributes:
        drawables (list): List of drawable objects on the game board.
    """
    def __init__(self):
        """
        Initializes the GameBoard instance.
        """
        self.drawables = [] # List to store drawable objects

    def create_tiles(self):
        """
        Creates and returns a list of tile objects.

        Returns:
            list: List of tile objects.
        """
        tiles = [] # tiles list for return back to game class
        # top row of the animal order
        top_row = [Animal.BABYDRAGON,Animal.SPIDER,Animal.BABYDRAGON,Animal.BAT,Animal.SPIDER,Animal.SPIDER]
        row_range = range(1,2)  # loop through row 1
        col_range = range(1,7)  # loop through column 1 to column 7
        tiles.extend(self._create_tiles_rowcolumn(row_range, col_range, top_row)) # extend the returned list into the tiles list

        # right column of animal order
        right_column = [Animal.BAT,Animal.SALAMANDER,Animal.SALAMANDER,Animal.SPIDER,Animal.BAT,Animal.BABYDRAGON]
        row_range = range(1,7) # loop through row 1 to 7
        col_range = range(7,8) # only focus on column 7
        tiles.extend(self._create_tiles_rowcolumn(row_range, col_range, right_column, False))

        # bottom row of animal order
        bottom_row = [None,Animal.BAT, Animal.BABYDRAGON,Animal.SALAMANDER,Animal.SPIDER,Animal.BAT,Animal.SALAMANDER]
        row_range = range(7,8) # only focus on row 7
        col_range = range(7,1,-1) # loop through column 2 to 7 reversely
        tiles.extend(self._create_tiles_rowcolumn(row_range, col_range, bottom_row))

        # left column
        left_column = [None,Animal.SALAMANDER, Animal.BABYDRAGON,Animal.SPIDER,Animal.BAT,Animal.SALAMANDER,Animal.BABYDRAGON]
        row_range = range(7,1,-1) # loop through row 2 to 7 reversely
        col_range = range(1,2) # only focus on column 1
        tiles.extend(self._create_tiles_rowcolumn(row_range, col_range, left_column, False))
        self.drawables.extend(tiles) # also extend to drawable list to draw the gameboard later
        return tiles # return the obtained tiles back to game class

    def _create_tiles_rowcolumn(self, row_range, col_range, animal_list, is_row = True):
        """
        Creates and returns a list of tile objects based on row and column ranges.

        Args:
            row_range (range): Range of rows.
            col_range (range): Range of columns.
            animal_list (list): List of animals for the tiles.
            is_row (bool): Whether we are loop through row or column

        Returns:
            list: List of tile objects.
        """
        tiles = [] # list of tile for row or column
        for row in row_range:
            for col in col_range:
                if is_row:
                    tile = Tile(animal_list[col - 1], col * CELL_WIDTH, row * CELL_HEIGHT) # create tile with ordering of animal and the position
                else:
                    tile = Tile(animal_list[row - 1], col * CELL_WIDTH, row * CELL_HEIGHT)
                tiles.append(tile)
        return tiles


    def _randomise_chit_card_position(self):
        """
        Randomizes the position of chit cards on the game board.

        Returns:
            list: List of randomized positions.
        """
        range_list = [(i, j) for i in range(2, 7) for j in range(2, 7)] # the available position for chitcards is only from row 2 to 7 and column 2 to 7
        rowcol_list = random.sample(range_list, 16) # get 16 random position because we have only 16 chitcards

        # Pre-calculate positions
        positions = [(pos[1] * CELL_WIDTH, pos[0] * CELL_HEIGHT) for pos in rowcol_list] # calculate the position corresponding to cell size
        return positions # return the position

    def create_chit_cards(self):
        """
        Creates and returns a list of chit card objects.

        Returns:
            list: List of chit card objects.
        """
        chit_cards = [] # a list to store chit card to return back to game class
        positions = self._randomise_chit_card_position() # get the list of randomised chit card position
        animal_list = [Animal.BABYDRAGON,Animal.BAT,Animal.SPIDER,Animal.SALAMANDER] # a list of forward chit card animal list
        quantity_list = [1, 2, 3] # every animal have 1,2,3 of quantity in chit card
        for animal in animal_list:# loop through the animal
            for quantity in quantity_list: # loop through the quantity of animal to ensure each animal have each of the quantity chit card
                pos = positions.pop() # get a position from the randomised position list
                chit_card = ForwardChitCard(animal,pos[0], pos[1],quantity) # create a ForwardChitCard with a animal type and position and animal quantity
                chit_cards.append(chit_card) # append every chit card into the list

        for quantity in range(2): # loop through 2 times because we have 2 dragonpirate*1 chit card and 2 dragonpirate*2 chit card
            pos = positions.pop() # get a position from the randomised position list
            one_dragon_pirate = BackwardChitCard(Animal.DRAGONPIRATE,pos[0], pos[1],1) # create backward chitcard which is dragon pirate and this is creating dragonpirate*1 chit card
            chit_cards.append(one_dragon_pirate)

            pos = positions.pop()
            two_dragon_pirate = BackwardChitCard(Animal.DRAGONPIRATE,pos[0], pos[1],2) # create backward chitcard which is dragon pirate and this is creating dragonpirate*2 chit card
            chit_cards.append(two_dragon_pirate)
        self.drawables.extend(chit_cards) # also extend to drawable list to draw the gameboard later
        return chit_cards # return the obtained chit cards back to game class

    def create_caves(self,player_num):
        """
        Creates and returns a list of cave objects.

        Args:
            player_num (int): Number of players.

        Returns:
            list: List of cave objects.
        """
        caves = [] # a list to store caves to return back to game class
        caves_animal = [Animal.SALAMANDER,Animal.SPIDER,Animal.BAT,Animal.BABYDRAGON] # the ordering of animal from cave1 to cave4 have
        cave_pos = [(4,0),(4,8),(0,4),(8,4)] # the row and column of the cave1 to cave 4
        cave_pos = [(pos[1] * CELL_WIDTH, pos[0] * CELL_HEIGHT) for pos in cave_pos] # calculate the actual position on the screen
        for i in range(player_num): # create the number of caves based on the number of players
            caves.append(Cave(i+1,caves_animal[i],cave_pos[i])) # create cave with id, animal and position
        self.drawables.extend(caves) # also extend to drawable list to draw the gameboard later
        return caves # return the obtained caves back to game class

    def create_dragon_token(self,player_num):
        """
        Creates and returns a list of dragon token objects.

        Args:
            player_num (int): Number of players.

        Returns:
            list: List of dragon token objects.
        """
        dragon_tokens = [] # a list to store dragon token to return back to game class
        dragon_token_pos = [(4, 0), (4, 8), (0, 4), (8, 4)] # the row and column of the dragontoken1 to dragontoken4
        dragon_token_pos = [(pos[1] * CELL_WIDTH, pos[0] * CELL_HEIGHT) for pos in dragon_token_pos] # calculate the actual position on the screen
        for i in range(player_num): # create the number of dragon token based on the number of players
            dragon_tokens.append(DragonToken(i + 1, dragon_token_pos[i])) # create dragontoken with id and position
        self.drawables.extend(dragon_tokens) # also extend to drawable list to draw the gameboard later
        return dragon_tokens # return the obtained dragon token back to game class



    def draw_gameboard(self):
        """
        Draws the game board by calling the draw method of each drawable object.
        """
        # loop through all the drawable item that obtained when creating object to call the draw function
        for drawable in self.drawables:
            drawable.draw()