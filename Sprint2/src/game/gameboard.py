import random
from .constants import CELL_WIDTH,CELL_HEIGHT, TILES_ANIMAL_ORDERING,TILES_POS,TILES_NUM,CAVES_ANIMAL,CAVES_DRAGON_POS,CHITCARD_COL_RANGE,CHITCARD_ROW_RANGE
from .chitcard import ForwardChitCard
from .chitcard import BackwardChitCard
from .cave import Cave
from .tile import Tile
from .animal import Animal
from .dragontoken import DragonToken

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
        for i in range(TILES_NUM):
            tile = Tile(TILES_ANIMAL_ORDERING[i], TILES_POS[i][0], TILES_POS[i][1])
            tiles.append(tile)
        self.drawables.extend(tiles)
        return tiles


    def _randomise_chit_card_position(self):
        """
        Randomizes the position of chit cards on the game board.

        Returns:
            list: List of randomized positions.
        """
        range_list = [(i, j) for i in CHITCARD_ROW_RANGE for j in CHITCARD_COL_RANGE] # the available position for chitcards is only from row 2 to 7 and column 2 to 7
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
        for i in range(4): # create the 4 caves
            caves.append(Cave(i+1,CAVES_ANIMAL[i],CAVES_DRAGON_POS[i])) # create cave with id, animal and position
        self.drawables.extend(caves) # also extend to drawable list to draw the gameboard later
        return caves[:player_num] # return the obtained caves back to game class  based on the number of player

    def create_dragon_token(self,player_num):
        """
        Creates and returns a list of dragon token objects.

        Args:
            player_num (int): Number of players.

        Returns:
            list: List of dragon token objects.
        """
        dragon_tokens = [] # a list to store dragon token to return back to game class
        for i in range(4): # create 4 dragon token
            dragon_tokens.append(DragonToken(i + 1, CAVES_DRAGON_POS[i])) # create dragontoken with id and position
        self.drawables.extend(dragon_tokens) # also extend to drawable list to draw the gameboard later
        return dragon_tokens[:player_num] # return the obtained dragon token back to game class based on the number of player



    def draw_gameboard(self):
        """
        Draws the game board by calling the draw method of each drawable object.
        """
        # loop through all the drawable item that obtained when creating object to call the draw function
        for drawable in self.drawables:
            drawable.draw()