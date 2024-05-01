Intended platform: Windows


How to build the executable from the source code

1. Ensure you are on a Windows computer. 

2. Clone the repo, open VSCode and ensure you open the folder corresponding to the repo. You should see the three folders: Project, Sprint2_Deliverables, Sprint2_Game.

2. Open up a terminal in VSCode (Terminal > New Terminal).

3. Navigate to the directory Sprint2_Game within the terminal.

3. Activate the virtual environment by running within the terminal: '.venv/Scripts/Activate' without the apostrophe marks.

3. Run 'pyinstaller main.py' in the terminal, again without the apostrophe marks. 

4. Wait for pyinstaller to finish running completely.

5. Make a copy of the assets folder in the Sprint2_Game directory, and move it into the directory Sprint2_Game/dist/main/_internal

6. Now main.exe (the executable) located in Sprint2_Game/dist/main can be run.