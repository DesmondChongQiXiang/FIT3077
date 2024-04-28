import pygame
import random
from .settings import BLACK,ROWS,COLS,WHITE,SQUARE_SIZE, RED, NON_CAVE_TILE_ANIMALS,NON_CAVE_TILE_COORDINATES, CAVE_TILE_ANIMALS,CAVE_TILE_COORDINATES, CHIT_CARD_COORDINATES, CHIT_CARD_ANIMALS, CHIT_CARD_DRAGON_PIRATES
from .tiles.non_cave_tile import NonCaveTile
from .tiles.cave_tile import CaveTile
from .chit_cards.animal_chit_card import AnimalChitCard
from .chit_cards.dragon_pirate_chit_card import DragonPirateChitCard


class GameBoard:
    def __init__(self,cave_tiles,chit_cards,players):
        self.tiles = []
        self.cave_tiles = cave_tiles
        self.chit_cards = chit_cards
        self.players = players
        self.active_player = None
        self.selected_chit_chard = None

    def draw_board(self, window):
        coordinate_pointer = 0
        window.fill(WHITE)
        random.shuffle(CHIT_CARD_COORDINATES)
        for i in range(len(NON_CAVE_TILE_COORDINATES)):
            tile = NonCaveTile(NON_CAVE_TILE_ANIMALS[i],None,NON_CAVE_TILE_COORDINATES[i][0],NON_CAVE_TILE_COORDINATES[i][1])
            #pygame.draw.rect(window,tile.animal.value,(tile.x*SQUARE_SIZE,tile.y*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
            animal = pygame.image.load("./board/assets/"+tile.animal.value).convert_alpha()
            animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
            window.blit(animal,(tile.x*SQUARE_SIZE,tile.y*SQUARE_SIZE))
        for i in range(len(CAVE_TILE_COORDINATES)):
            tile = CaveTile(CAVE_TILE_ANIMALS[i],None,CAVE_TILE_COORDINATES[i][0],CAVE_TILE_COORDINATES[i][1])
            animal = pygame.image.load("./board/assets/"+tile.animal.value).convert_alpha()
            animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
            window.blit(animal,(tile.x*SQUARE_SIZE,tile.y*SQUARE_SIZE))

        for i in range(len(CHIT_CARD_ANIMALS)):
            chit_card = AnimalChitCard(CHIT_CARD_ANIMALS[i][1],CHIT_CARD_ANIMALS[i][0],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            coordinate_pointer += 1
            animal = pygame.image.load("./board/assets/chit_card_" + str(chit_card.number_of_animal) + "_" + chit_card.animal.value)
            animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
            window.blit(animal,(chit_card.x*SQUARE_SIZE,chit_card.y*SQUARE_SIZE))

        
        for i in range(len(CHIT_CARD_DRAGON_PIRATES)):
            chit_card = DragonPirateChitCard(CHIT_CARD_DRAGON_PIRATES[i],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            coordinate_pointer += 1
            #animal = pygame.image.load("./board/assets/chit_card"+str(chit_card.number_of_animal) + chit_card.animal.value)
            #animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
            #window.blit(animal,(chit_card.x*SQUARE_SIZE,chit_card.y*SQUARE_SIZE))

        #pygame.draw.rect(window,baby_dragon_1.animal,(baby_dragon_1.x*SQUARE_SIZE,baby_dragon_1.y*SQUARE_SIZE))


    def create_board(self):
        pass

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
