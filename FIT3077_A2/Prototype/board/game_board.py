import pygame
import random
from .settings import BLACK,ROWS,COLS,WHITE,SQUARE_SIZE, RED, NON_CAVE_TILE_ANIMALS,NON_CAVE_TILE_COORDINATES, CAVE_TILE_ANIMALS,CAVE_TILE_COORDINATES, CHIT_CARD_COORDINATES, CHIT_CARD_ANIMALS, CHIT_CARD_DRAGON_PIRATES, CHIT_CARD_BACK
from .tiles.non_cave_tile import NonCaveTile
from .tiles.cave_tile import CaveTile
from .chit_cards.animal_chit_card import AnimalChitCard
from .chit_cards.dragon_pirate_chit_card import DragonPirateChitCard
from .animal import Animal


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
        self.players = players
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
    This function creates a 2D array that represents all of the chit cards, this determines which 
    """
    def create_board(self):
        random.shuffle(CHIT_CARD_COORDINATES)
        for row in range(ROWS):
            self.chit_cards.append([])
            for col in range(COLS):
                self.chit_cards[row].append(0)
        coordinate_pointer = 0
        for i in range(len(CHIT_CARD_ANIMALS)):
            chit_card = AnimalChitCard(CHIT_CARD_ANIMALS[i][1],CHIT_CARD_ANIMALS[i][0],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            coordinate_pointer += 1
            self.chit_cards[chit_card.x][chit_card.y] = chit_card
        
        for i in range(len(CHIT_CARD_DRAGON_PIRATES)):
            chit_card = DragonPirateChitCard(Animal.DRAGON_PIRATE,CHIT_CARD_DRAGON_PIRATES[i],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            coordinate_pointer += 1
            self.chit_cards[chit_card.x][chit_card.y] = chit_card

    def draw_chit_cards(self,window):
        for row in range(ROWS):
            for col in range(COLS):
                chit_card = self.chit_cards[row][col]
                if chit_card != 0:
                    if  chit_card.is_flipped == False:
                        window.blit(CHIT_CARD_BACK,(chit_card.x*SQUARE_SIZE,chit_card.y*SQUARE_SIZE))
                    else:
                        animal = pygame.image.load("./board/assets/chit_card_" + str(chit_card.number_of_animal) + "_" + chit_card.animal.value)
                        animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
                        window.blit(animal,(chit_card.x*SQUARE_SIZE,chit_card.y*SQUARE_SIZE))


    def draw_game(self,window):
        self.draw_tiles(window)
        self.draw_chit_cards(window)


    def get_piece(self,row,col):
        return self.chit_cards[row][col]           

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
    
    
    def set_active_player(self,player):
        self.active_player = player

    def flip_chit_card(self,chit_card):
        chit_card.set_is_flipped()
        

