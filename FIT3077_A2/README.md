# Fiery Dragons
Author: Rohan Sivam 
Student ID: 32880316 
Date: 29-04-2024

## Overview
This repository contains the UML class diagrams, Sequence Diagram, Design Rational and working prototype. To set up the executable for this project, follow the following steps.
1. Navigate to the active directory Prototype
2. Activate the virtual environment. On Mac , this is : source .venv/bin/activate
3. Make sure that pyinstaller is installed, if not install by typing the command on mac : pip install pyinstaller 
4. Type the following command in the terminal : pyinstaller main.py
5. After this has run, there should be 2 new folders : build and dist in the prototype directory
6. Inside the dist folder, there should be a folder called main. Inside the main folder there should be a folder called internal. The relative file path should be:
[**Prototype**](./Prototype/)/dist/main/_internal.
7. Create a new folder inside this _internal folder called board.
8. Copy the [**assets**](./Prototype/board/assets/) folder from inside [**board**](./Prototype/board/) originally in prototype to this new board folder. The file path for the copy of assets should be : Prototype/dist/main/_internal/board/assets. The original assets folder can be gotten from : [**Prototype/board/assets**](./Prototype/board/assets/)
9. Now the executable is ready to run. Go to the main folder inside dist in your main laptop file directory. On mac this is finder. Inside this folder should be an executable called main. Click on it to run the executable.

Notes: The Creation and Running of the Executable has been tested on 3 different laptops. One is a windows OS device and two are MAC OS devices. This means that there should be no problem creating and running the executable.

## Navigation

- **Deliverables**: This folder contains all deliverables for Sprint 2. Click on the link to go to the deliverable
    - [**UML Class Diagram**](./A2_Task1_ObjectOrientedDesign_And_DesignRationales/FIT3077%20A2%20Class%20Diagram%2025_4_24.pdf)
    - [**Sequence Diagram for REQ1**](./A2_Task1_ObjectOrientedDesign_And_DesignRationales/FIT3077%20A2%20Sequence%20Diagram%20REQ%201%2025_4_24.pdf)
    - [**Sequence Diagram for REQ2**](./A2_Task1_ObjectOrientedDesign_And_DesignRationales/FIT3077%20A2%20Sequence%20Diagram%20REQ%202%20%2025_4_24.pdf)
    - [**Sequence Diagram for REQ3**](./A2_Task1_ObjectOrientedDesign_And_DesignRationales/FIT3077%20A2%20Sequence%20Diagram%20REQ%203%20%2025_4_24.pdf)
    - [**Sequence Diagram for REQ4**](./A2_Task1_ObjectOrientedDesign_And_DesignRationales/FIT3077%20A2%20Sequence%20Diagram%20REQ%204%20%2025_4_24.pdf)
    - [**Sequence Diagram for REQ5**](./A2_Task1_ObjectOrientedDesign_And_DesignRationales/FIT3077%20A2%20Sequence%20Diagram%20REQ%205%2025_4_24.pdf)
    - [**Working Prototype**](./Prototype/)
