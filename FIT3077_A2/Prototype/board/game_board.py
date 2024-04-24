import pygame
from .settings import BLACK,ROWS,COLS,WHITE,SQUARE_SIZE, RED
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
        window.fill(BLACK)
        
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
