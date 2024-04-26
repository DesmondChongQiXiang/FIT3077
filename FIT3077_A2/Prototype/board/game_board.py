import pygame
from .settings import BLACK,ROWS,COLS,WHITE,SQUARE_SIZE, RED, NON_CAVE_TILE_ANIMALS,NON_CAVE_TILE_COORDINATES
from .non_cave_tile import NonCaveTile


class GameBoard:
    def __init__(self,cave_tiles,chit_cards,players):
        self.tiles = []
        self.cave_tiles = cave_tiles
        self.chit_cards = chit_cards
        self.players = players
        self.active_player = None
        self.selected_chit_chard = None

    def draw_board(self, window):
        window.fill(WHITE)
        for i in range(len(NON_CAVE_TILE_COORDINATES)):
            tile = NonCaveTile(NON_CAVE_TILE_ANIMALS[i],None,NON_CAVE_TILE_COORDINATES[i][0],NON_CAVE_TILE_COORDINATES[i][1])
            #pygame.draw.rect(window,tile.animal.value,(tile.x*SQUARE_SIZE,tile.y*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
            animal = pygame.image.load("./board/assets/"+tile.animal.value).convert_alpha()
            animal = pygame.transform.scale(animal,(SQUARE_SIZE,SQUARE_SIZE))
            window.blit(animal,(tile.x*SQUARE_SIZE,tile.y*SQUARE_SIZE))
        """
        for row in range(ROWS):
            if row == 0:
                pygame.draw.rect(window,RED,(row*SQUARE_SIZE,4*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                pygame.draw.rect(window,WHITE,(row*SQUARE_SIZE,4*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),1)
            if row == 8:
                pygame.draw.rect(window,RED,(row*SQUARE_SIZE,4*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                pygame.draw.rect(window,WHITE,(row*SQUARE_SIZE,4*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),1)
            elif row == 1:
                for col in range(1,COLS-1):
                    pygame.draw.rect(window,RED,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                    pygame.draw.rect(window,WHITE,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),1)
            elif row == 7:
                for col in range(1,COLS-1):
                    pygame.draw.rect(window,RED,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                    pygame.draw.rect(window,WHITE,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),1)
            elif 1 < row < 7:
                if row == 4:
                    pygame.draw.rect(window,RED,(4*SQUARE_SIZE,0*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                    pygame.draw.rect(window,WHITE,(4*SQUARE_SIZE,0*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),1)
                    pygame.draw.rect(window,RED,(4*SQUARE_SIZE,8*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                    pygame.draw.rect(window,WHITE,(4*SQUARE_SIZE,8*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),1)
                for col in range(0,COLS):
                    if col == 1 :
                        pygame.draw.rect(window,RED,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                        pygame.draw.rect(window,WHITE,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),1)
                    elif col == 7:
                        pygame.draw.rect(window,RED,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                        pygame.draw.rect(window,WHITE,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE),1)
        """
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
