# Fiery Dragon Board Game

Author: Zhan Hung Fu 

Student ID: 33049394

## Overview

Welcome to the Fiery Dragon Board Game repository! This project houses the codebase for the Fiery Dragon Board Game, along the UML class diagrams, sequence diagrams, and design rationale. 

## Navigation

- **deliverables**: This folder contains all project deliverables.
    - [**UML Class Diagram**](./deliverables/FIT3077%20Sprint%202%20UML%20Class%20Diagram.pdf)
    - [**Design Rationale**](./deliverables/FIT3077%20Sprint%202%20Design%20Rationale.pdf)
    - [**REQ 1 Sequence Diagram**](./deliverables/FIT3077%20Sprint%202%20REQ%201%20Sequence%20Diagram.pdf)
    - [**REQ 2 Sequence Diagram**](./deliverables/FIT3077%20Sprint%202%20REQ%202%20Sequence%20Diagram.pdf)
    - [**REQ 3 & 4 Sequence Diagram**](./deliverables/FIT3077%20Sprint%202%20REQ%203%20&%204%20Sequence%20Diagram.pdf)
    - [**REQ 5 Sequence Diagram**](./deliverables/FIT3077%20Sprint%202%20Design%20Rationale.pdf)

- [**src**](./src/): This folder contains all the game's code and assets.

## Tech Stack

- **Language:** Python
- **Libraries:** PyGame

## Building the Executable (runs on MacOS)

1. Navigate into the **'src'** folder.

2. Activate the virtual environment by running the following command in the terminal:

    - ` source .venv/bin/activate `

3. Turn the program into an executable by running this command in the terminal:

    - ` pyinstaller Game.py `

4. This creates a folder called **'dist'** which is a bundled executable that includes its scripts, dependencies and etc.

5. Inside the **'dist'** folder, create a new folder called **'board'** under the **'_internal'** folder.

6. Copy the **'assets'** folder into the newly created **'board'** folder.

7. The creation of the executable is complete, and it can be run independently of the source code.