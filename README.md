# GameOfLife
My Python Implementation of Conway's Game of Life

Conway's Game of Life:
> The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:<br>
> **Rules:**
> 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
> 2. Any live cell with two or three live neighbours lives on to the next generation.
> 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
> 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Logic 
Logic for game is written in **LifeBoard.py** and **LifeEngine.py**<br>
**LifeBoard.py:** houses logic for getting neighbors and position in board<br>
**LifeEngine.py:** uses LifeBoard.py to check the four rules of Conway's game and run the simulation <br>

# Visualization 
A webpage is also provided for visualization which uses flask as the framework and sends request to the server to obtain data from the python scripts over how the simulation should progress<br>
Visualization can be done through the terminal by running LifeEngine.py

*NOTE: NO game logic is written in the javascript for the webpage; all data is requested from the python script* 

