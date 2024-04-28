Author: Rohan Sivam 32880316 29-04-2024

-This executable was built on a MAC using pyinstaller
- To build the executable on a device using the source code
- navigate to the directory Prototype so that Prototype is the active directory
- activate the virtual environment - on MAC I used source .venv/bin/activate
- run pyinstaller main.py 
- this will create a folder called dist with the folder main inside of it.
- inside the main folder, there will be another folder called _internal, inside the folder create a new folder called board
- copy the assets folder from the board folder inside Prototype to this new board folder
- Now the executable should be able to run.
- the executable created can be run independent of the source code.