import pygame
from board.settings import WIDTH,HEIGHT,SQUARE_SIZE
from board.game_board import GameBoard
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Fiery Dragons')
FPS = 60

"""
This gets the tile that the mouse has clicked on and returns the column and row. This has been tested by flipping the correct tile when it is clicked on.
"""
def get_row_col_from_mouse(pos):
    x,y = pos
    row = x // SQUARE_SIZE
    col = y // SQUARE_SIZE
    return (row,col)

"""
This is the main game engine that runs the actual game. The game has ticks based on the fps which mean the game state is updated each tick.
"""
def main():
    run = True
    clock = pygame.time.Clock()
    board = GameBoard([],[],[])
    board.shuffle_chit_cards() # This shuffles the list of coordinates at the start of the game
    """
    This was the testing for my get_piece and flip cards methods
    """
    #chit_card = board.get_piece(2,6)
    #print(chit_card.x,chit_card.y)
    #board.flip_chit_card(chit_card)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get(): # this ends the game if the game window is closed.
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos() # gets the position of the mouse when the mouse is clicked
                row,col = get_row_col_from_mouse(position) # sets the row and column to be retrieved to be the mouse click position
                chit_card = board.get_piece(row,col) # gets the game piece at that point
                board.flip_chit_card(chit_card) # flips the card if it can be flipped
        board.draw_game(WINDOW) # This draws out all of the game board based on the current state
        pygame.display.update() # update the game state

    
    pygame.quit() #Ends the game after the loops have ended



main()# calls the main function