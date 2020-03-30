# GameOfLife
My Python Implementation of Conway's Game of Life

# Logic 
Logic for game is written in LifeBoard.py and LifeEngine.py<br>
LifeBoard.py -> houses logic for getting neighbors and position in board<br>
LifeEngine.py -> uses LifeBoard.py to check the four rules of Conway's game and Run the simulation <br>

# Visualization 
Visualization can be done through the terminal by running LifeEngine.py<br>
A webpage is also provided for visualization which uses flask as the framework and sends request<br>
to the server to obtain data from the python scripts over how the simulation should progress<br>
*NOTE: NO game logic is written in the javascript for the webpage; all data is requested from the python script* 

