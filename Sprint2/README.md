# Fiery Dragon

Student Name: Desmond Chong Qi Xiang

Student ID: 33338248

## Overview
This repository includes the Sprint 2 file, which contains the UML class diagram, sequence diagram, and design rationale within the "design" folder, alongside the codebase located in the "src" folder.

## Navigation
- **deliverables**: This folder contains all project design(UML class diagram, sequence diagram, and design rationale).
    - [**UML Class Diagram**](https://git.infotech.monash.edu/FIT3077/fit3077-s1-2024/CL_Monday06pm_Team625/-/blob/DesmondChongQiXiang_33338248/Sprint2/Object-Oriented%20Design%20and%20Design%20Rationales/FIT3077%20Sprint%202%20UML%20class%20diagram.pdf?ref_type=heads)
    - [**Design Rationale**](https://git.infotech.monash.edu/FIT3077/fit3077-s1-2024/CL_Monday06pm_Team625/-/blob/DesmondChongQiXiang_33338248/Sprint2/Object-Oriented%20Design%20and%20Design%20Rationales/FIT3077%20Sprint%202%20Design%20Rationale.pdf?ref_type=heads)
    - [**REQ 1 Sequence Diagram**](https://git.infotech.monash.edu/FIT3077/fit3077-s1-2024/CL_Monday06pm_Team625/-/blob/DesmondChongQiXiang_33338248/Sprint2/Object-Oriented%20Design%20and%20Design%20Rationales/FIT3077%20Sprint%202%20Sequence%20Diagram%20REQ1.pdf?ref_type=heads)
    - [**REQ 2 Sequence Diagram**](https://git.infotech.monash.edu/FIT3077/fit3077-s1-2024/CL_Monday06pm_Team625/-/blob/DesmondChongQiXiang_33338248/Sprint2/Object-Oriented%20Design%20and%20Design%20Rationales/FIT3077%20Sprint%202%20Sequence%20Diagram%20REQ2.pdf?ref_type=heads)
    - [**REQ 3 Sequence Diagram**](https://git.infotech.monash.edu/FIT3077/fit3077-s1-2024/CL_Monday06pm_Team625/-/blob/DesmondChongQiXiang_33338248/Sprint2/Object-Oriented%20Design%20and%20Design%20Rationales/FIT3077%20Sprint%202%20Sequence%20Diagram%20REQ3.pdf?ref_type=heads)
    - [**REQ 4 Sequence Diagram**](https://git.infotech.monash.edu/FIT3077/fit3077-s1-2024/CL_Monday06pm_Team625/-/blob/DesmondChongQiXiang_33338248/Sprint2/Object-Oriented%20Design%20and%20Design%20Rationales/FIT3077%20Sprint%202%20Sequence%20Diagram%20REQ4.pdf?ref_type=heads)
    - [**REQ 5 Sequence Diagram**](https://git.infotech.monash.edu/FIT3077/fit3077-s1-2024/CL_Monday06pm_Team625/-/blob/DesmondChongQiXiang_33338248/Sprint2/Object-Oriented%20Design%20and%20Design%20Rationales/FIT3077%20Sprint%202%20Sequence%20Diagram%20REQ5.pdf?ref_type=heads)

- [**src**](./src/): This folder consist all of the game code and assets

## Tech Stack

- **Language:** Python
- **Framework:** PyGame

## Instructions for Building the Executable (runs on MacOS)
1. Begin by navigating to the **'src'** directory.

2. Activate the virtual environment by executing the following command in your terminal:

    - ` source .venv/bin/activate `

3. Convert the program into an executable by running this command in the terminal:

    - ` pyinstaller main.py `

4. This action generates a folder named **'dist'**, containing a bundled executable along with its necessary scripts and dependencies.

5. Within the **'dist'** directory, establish a new folder named **'game'** within the **'_internal'** directory.

6. Copy the **'assets'** folder into the newly created **'game'** folder.

7. The process of creating the executable is now complete, allowing it to be executed independently from the source code.