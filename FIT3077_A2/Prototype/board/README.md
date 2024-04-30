# Fiery Dragons
Author: Rohan Sivam 
Student ID: 32880316 
Date: 30-04-2024

## Overview
This directory contains all the classes I have used to setup the board for the game

## Navigation

- **Deliverables**: 
    - [**assets**](./assets/) : This folder contains all the assets that I have used including my tile images, chit card images and dragon token images
    - [**chit_cards**](./chit_cards/) : This folder contains all the classes I have used to implement the functionality of my chit cards. In this folder we have the classes : 
        - chit_card.py : This is the abstract parent class which defines the general methods and attributes that should be implemented by both chit cards
        - animal_chit_card.py : This is the child chit card class which implements the methods declared by the chit_card parent class to be used for the animal chit card types
        - dragon_pirate_chit_card.py : This is the child chit card class which implements the methods declared by the chit_card parent class to be used for the dragon pirate chit cards
    - [**tiles**](./tiles/) : This folder contains all the classes I have used to implement the functionality of my tiles. In this folder we have the classes :
        - tile.py : This is the abstract parent class which defines the general methods and attributes that should be implemented by both tile types
        - non_cave_tile.py : This is the child tile class that implements the tile method for the functionality of the regular game board tiles that make up the game board
        - cave_tile.py : This is the child tile class that implements the functionality of the cave tile to act as the caves which the dragons start the game and return to to win the game.
    - animal.py : This class is the enum that is used to represent each of the animals that are symbols on the chit cards and tiles. The animals represent strings which are used to access the image assets
    - dragon.py : This class is the class that represents the dragon pieces that act as each of the players way of interacting with the game board. The dragons start the game on a cave tile and players can win the game by returning the dragons to their cave tiles that they started the game from.
    - game_board.py : This class is the representation of the game board and implements all of it's functionality such as arranging the tiles, arranging the chit cards, placing the dragons on their starting cave tiles, moving the dragons on the board and flipping the chit cards. It handles all game board events.
    - settings.py : This is where all the constants for my game implementation has been declared. This includes how many of each animal tile, animal chit card, dragon pirate chit card and cave tiles should be included. I also declared all coordinates and the relative file path here.