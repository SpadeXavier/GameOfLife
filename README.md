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
A *webpage* is also provided for visualization which uses flask as the framework
- sends request to the server to obtain data from the python scripts over how the simulation should progress<br>

Visualization can optionally be done through terminal alone by running `python LifeEngine.py`
- ensure the termcolor package is installed, if not run `pip install termcolor`
- you can change variables in the file to test different configurations, generation numbers, etc...

*NOTE: NO game logic is written in the javascript for the webpage; all data is requested from the python script* 
# Usage
Flask activation instructions were extracted from:   
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

To start local flask server to run the webpage: 
1. Create a virtual environment by running `python -m venv ./venv`
2. Activate the virtual environment by running `source venv/bin/activate`
3. To download the required python packages run `pip install -r requirements.txt` 
4. If your FLASK_APP environmental variable is not set you must set it by running `export FLASK_APP=lifepage.py`
	* Optionally, you can run `pip install python-dotenv` and create a .flaskenv file in the top-level directory with the file having one line: FLASK_APP=microblog.py
	* This removes the need of having to use export every new terminal session 
5. Then simply run `flask run` to start the server 
	* Run `export FLASK_ENV=development` if you want to run the server and have it reload for code changes
6. Enjoy!




