import pygame
import random
from .settings import BLACK,ROWS,COLS,WHITE,SQUARE_SIZE, RED, NON_CAVE_TILE_ANIMALS,NON_CAVE_TILE_COORDINATES, CAVE_TILE_ANIMALS,CAVE_TILE_COORDINATES, CHIT_CARD_COORDINATES, CHIT_CARD_ANIMALS, CHIT_CARD_DRAGON_PIRATES, CHIT_CARD_BACK
from .tiles.non_cave_tile import NonCaveTile
from .tiles.cave_tile import CaveTile
from .chit_cards.animal_chit_card import AnimalChitCard
from .chit_cards.dragon_pirate_chit_card import DragonPirateChitCard
from .animal import Animal


class GameBoard:
    def __init__(self,cave_tiles,chit_cards,players):
        self.tiles = []
        self.cave_tiles = cave_tiles
        self.chit_cards = []
        self.players = players
        self.active_player = None
        self.selected_chit_chard = None
        self.create_board()

    def shuffle_chit_cards(self):
        random.shuffle(CHIT_CARD_COORDINATES)
        return CHIT_CARD_COORDINATES

    def draw_tiles(self, window):
        window.fill(WHITE)
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

        #for i in range(len(CHIT_CARD_ANIMALS)):
            #chit_card = AnimalChitCard(CHIT_CARD_ANIMALS[i][1],CHIT_CARD_ANIMALS[i][0],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            #coordinate_pointer += 1
            #animal = pygame.image.load("./board/assets/chit_card_" + str(chit_card.number_of_animal) + "_" + chit_card.animal.value)
            #animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
            #window.blit(animal,(chit_card.x*SQUARE_SIZE,chit_card.y*SQUARE_SIZE))

        
        #for i in range(len(CHIT_CARD_DRAGON_PIRATES)):
            #chit_card = DragonPirateChitCard(CHIT_CARD_DRAGON_PIRATES[i],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            #coordinate_pointer += 1
            #animal = pygame.image.load("./board/assets/chit_card"+str(chit_card.number_of_animal) + chit_card.animal.value)
            #animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
            #window.blit(animal,(chit_card.x*SQUARE_SIZE,chit_card.y*SQUARE_SIZE))

        #pygame.draw.rect(window,baby_dragon_1.animal,(baby_dragon_1.x*SQUARE_SIZE,baby_dragon_1.y*SQUARE_SIZE))


    def create_board(self):
        random.shuffle(CHIT_CARD_COORDINATES) 
        for row in range(ROWS):
            self.chit_cards.append([])
            for col in range(COLS):
                coordinates = [row,col]
                if coordinates not in CHIT_CARD_COORDINATES:
                    self.chit_cards[row].append(0)
        coordinate_pointer = 0
        for i in range(len(CHIT_CARD_ANIMALS)):
            chit_card = AnimalChitCard(CHIT_CARD_ANIMALS[i][1],CHIT_CARD_ANIMALS[i][0],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            coordinate_pointer += 1
            self.chit_cards[chit_card.x].append(chit_card)
        
        for i in range(len(CHIT_CARD_DRAGON_PIRATES)):
            chit_card = DragonPirateChitCard(Animal.DRAGON_PIRATE,CHIT_CARD_DRAGON_PIRATES[i],CHIT_CARD_COORDINATES[coordinate_pointer][0],CHIT_CARD_COORDINATES[coordinate_pointer][1])
            coordinate_pointer += 1
            self.chit_cards[chit_card.x].append(chit_card)

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
