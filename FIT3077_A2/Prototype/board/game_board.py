import pygame
import random
from .settings import BLACK,ROWS,COLS,WHITE,SQUARE_SIZE, RED, NON_CAVE_TILE_ANIMALS,NON_CAVE_TILE_COORDINATES, CAVE_TILE_ANIMALS,CAVE_TILE_COORDINATES, CHIT_CARD_COORDINATES, CHIT_CARD_ANIMALS, CHIT_CARD_DRAGON_PIRATES, CHIT_CARD_BACK
from .tiles.non_cave_tile import NonCaveTile
from .tiles.cave_tile import CaveTile
from .chit_cards.animal_chit_card import AnimalChitCard
from .chit_cards.dragon_pirate_chit_card import DragonPirateChitCard
from .animal import Animal
from .dragon import Dragon


class GameBoard:
    """
    This initialises the GameBoard class

    self.tiles : We initially set this to an empty list so that we can create the list of tiles based on the tile arrangement we want to use. 
    If we want to pass our own arrangement, we can just set it to the tiles being passed

    self.cave_tiles: like the list of tiles, this represents the cave tiles where the player dragons start their game

    self.chit_cards: this is the list of chit cards we will use for the game

    self.players: This is a list of dragon tokens that represent each player

    self.active_player : This is the currently active player.

    self.selected_chit_card : This allows us to check if the chit card matches the player number

    self.create_board: This initialises the game board with the chit cards assigned to their positions so we can flip them and the dragon tokens so we can move them.

    """
    def __init__(self,cave_tiles,chit_cards,players):
        self.tiles = []
        self.cave_tiles = cave_tiles
        self.chit_cards = []
        self.players = []
        self.active_player = None
        self.selected_chit_chard = None
        self.create_board()

    """
    This function is used to shuffle the chit card coordinates. We use this at the start of the game to get a randomised list of chit card coordinates and can
    use it each time a turn is passed to the next player
    """
    def shuffle_chit_cards(self):
        random.shuffle(CHIT_CARD_COORDINATES)
        return CHIT_CARD_COORDINATES


    """
    This function draws out the game tiles on the game window
    To test this method: I initially just ran draw_tiles in the main game window. First I created a tile that had fixed coordinates instead of an array. 
    Then I printed the tile to test that the printing of the tile works. As I gave the coordinates 1 and 0 this printed the tile at the 1 of the x axis and 0 of the 
    y axis. I also used a solid colour to test first that the tile was being printed correctly. Then i implemented my loop to print solid colours through the board
    and finally i implemented printing my assets. After all tests, the board prints all the tiles at fixed coordinates which i have declared in settings.py
    """
    def draw_tiles(self, window):
        window.fill(WHITE) # This fills the game screen background with a white colour
        for i in range(len(NON_CAVE_TILE_COORDINATES)): # Loop through the list of coordinates
            # Create a tile using the same index in the list of animals declared in settings.py
            tile = NonCaveTile(NON_CAVE_TILE_ANIMALS[i],None,NON_CAVE_TILE_COORDINATES[i][0],NON_CAVE_TILE_COORDINATES[i][1])  
            animal = pygame.image.load("./board/assets/"+tile.animal.value).convert_alpha() # Load the animal image by getting the tiles animal attribute
            animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE)) # Scale the image
            window.blit(animal,(tile.x*SQUARE_SIZE,tile.y*SQUARE_SIZE)) # render the image at the coordinates the tile has

        for i in range(len(CAVE_TILE_COORDINATES)): # do the same thing for the cave tiles
            tile = CaveTile(CAVE_TILE_ANIMALS[i],None,CAVE_TILE_COORDINATES[i][0],CAVE_TILE_COORDINATES[i][1])
            animal = pygame.image.load("./board/assets/"+tile.animal.value).convert_alpha()
            animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
            window.blit(animal,(tile.x*SQUARE_SIZE,tile.y*SQUARE_SIZE))

    """
    This function creates a 2D array that represents all of the chit cards, this determines which coordinates in the array are represented by chit cards
    To test this method, I created my board then used my flip method to display a tile at a fixed coordinate. A bug i experienced was the same tile being flipped but at
    different coordinates. This was because i was initially appending a certain number of 0's then appending the chit cards to the end of the list. This caused them
    to have the wrong coordinates. Instead I initialise an array of 0's to represent the places where chit cards are not on the game board then I replace the positions
    in the 2D array which are meant to represent chit cards. To test that this was finally working, in my main file, I used my get chit card function to retrieve a 
    chit card at a fixed coordinate. Then, I flip the chit card. I closed and opened the game to test that the same chit card was being flipped. I also used a print 
    statement to get the coordinates of the chit card being flipped. It was now correct.
    """
    def create_board(self):
        random.shuffle(CHIT_CARD_COORDINATES)
        for row in range(ROWS):
            self.chit_cards.append([])
            for col in range(COLS):
                self.chit_cards[row].append(0) # Initialises a 2D array filled with 0's representing the whole game board
        coordinate_pointer = 0
        for i in range(len(CHIT_CARD_ANIMALS)): # Place all the animal chit cards at their positions on the board in the array
            chit_card = AnimalChitCard(CHIT_CARD_ANIMALS[i][1],CHIT_CARD_ANIMALS[i][0],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            coordinate_pointer += 1 # This is used so that the same set of coordinates can be used for dragon pirate chit cards
            self.chit_cards[chit_card.x][chit_card.y] = chit_card
        
        for i in range(len(CHIT_CARD_DRAGON_PIRATES)): # Repeat the same thing with dragon pirate chit cards
            chit_card = DragonPirateChitCard(Animal.DRAGON_PIRATE,CHIT_CARD_DRAGON_PIRATES[i],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            coordinate_pointer += 1
            self.chit_cards[chit_card.x][chit_card.y] = chit_card

        for i in range(len(CAVE_TILE_COORDINATES)):
            dragon = Dragon(i,None,CAVE_TILE_COORDINATES[i][0],CAVE_TILE_COORDINATES[i][1])
            self.players.append(dragon)


    def draw_dragons(self,window):
        for i in range(len(self.players)):
            current_player = self.players[i]
            dragon = pygame.image.load("./board/assets/" + str(current_player.player_number+1) + "_" + current_player.animal)
            dragon = pygame.transform.scale(dragon,(SQUARE_SIZE - 30,SQUARE_SIZE - 30))
            window.blit(dragon,(SQUARE_SIZE * current_player.x + 15 , SQUARE_SIZE * current_player.y + 15))
        


    """
    This method draws out all the chit cards by iterating through the list of chit cards and drawing a chit card at the cards coordinates if the position in the 2D
    array is not a 0. To test this, I added chit cards to coordinates outside where i wanted them to be rendered and rendered them. The tiles rendered correctly which
    meant that this method works. I also want to draw the back of the tile if the tile is not flipped and show the correct image if the tile is flipped.
    This is done by checking the card is_flipped attribute
    """
    def draw_chit_cards(self,window):
        for row in range(ROWS):
            for col in range(COLS): # Goes through the whole 2D array
                chit_card = self.chit_cards[row][col]
                if chit_card != 0: #Checks that there is a chit card at the correct coordinates
                    if  chit_card.is_flipped == False: # If the card is not flipped , render the back of the chit card
                        window.blit(CHIT_CARD_BACK,(chit_card.x*SQUARE_SIZE,chit_card.y*SQUARE_SIZE))
                    else: # If it is flipped, render out the chit card based on the animal and the number of animals the chit card possesses. Using naming conventions
                        #for my assets I am able to retrieve the correct asset.
                        animal = pygame.image.load("./board/assets/chit_card_" + str(chit_card.number_of_animal) + "_" + chit_card.animal.value)
                        animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
                        window.blit(animal,(chit_card.x*SQUARE_SIZE,chit_card.y*SQUARE_SIZE))

    """
    This method just calls my draw tiles and chit cards together in one method
    """
    def draw_game(self,window):
        self.draw_tiles(window)
        self.draw_chit_cards(window)
        self.draw_dragons(window)

    """
    This method returns a chit card a specified coordinates based on the row and column desired. To test this, in my main file, i passed in hard coded coordinates to 
    see if the correct chit_card was being returned. The correct chit_card was returned so this method worked correctly
    """
    def get_piece(self,row,col):
        return self.chit_cards[row][col]           

    """
    This method will be implemented to add the dragon to the tile when starting the game
    """
    def set_player_start_tile(self,players):
        if len(self.players) == 4:
            self.cave_tiles[0].place_player_on_tile(players[0])
            self.cave_tiles[1].place_player_on_tile(players[1])
            self.cave_tiles[2].place_player_on_tile(players[2])
            self.cave_tiles[3].place_player_on_tile(players[3])
        elif len(self.players) == 3:
            self.cave_tiles[0].place_player_on_tile(players[0])
            self.cave_tiles[1].place_player_on_tile(players[1])
            self.cave_tiles[2].place_player_on_tile(players[2])
        elif len(self.players) == 2:
            self.cave_tiles[0].place_player_on_tile(players[0])
            self.cave_tiles[2].place_player_on_tile(players[1])
    
    """
    This method will be implemented to determine which dragon to move
    """
    def set_active_player(self,player):
        self.active_player = player

    """
    This method allows us to flip the chit card we have clicked on using the chit cards method.
    """
    def flip_chit_card(self,chit_card):
        chit_card.set_is_flipped()
        

