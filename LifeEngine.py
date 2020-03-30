from LifeBoard import LifeBoard 
import time

"""
The game uses an infinite-sized rectangular grid of cells in which each cell is either
empty or occupied by an organism. The occupied cells are said to be alive, whereas
the empty ones are dead. The game is played over a specific period of time with each
turn creating a new “generation” based on the arrangement of live organisms in
the current configuration. The status of a cell in the next generation is determined
by applying the following four basic rules to each cell in the current configuration:

1. If a cell is alive and has either two or three live neighbors, the cell
remains alive in the next generation. The neighbors are the eight cells
immediately surrounding a cell: vertically, horizontally, and diagonally 

2. A living cell that has no live neighbors or a single live neighbor dies from
isolation in the next generation 

3. A living cell that has four or more live neighbors dies from overpopulation
in the next generation 

4. A dead cell with exactly three live neighbors results in a birth and becomes
alive in the next generation. All other dead cells remain dead in the next
generation 

""" 

class LifeEngine:

    def __init__(self, board_size, arrangement):
        self.lb = LifeBoard(board_size, arrangement)
        self._curr_dict = arrangement;

    def run_generation(self):
        # iterate through board 
        for cell in self.lb:
            if self.lb.isAlive(cell):
                self.checkRules(cell, "Alive");
            elif self.lb.isDead(cell):
                self.checkRules(cell, "Dead");
            else:
                self.checkRules(cell, "Empty");

        # update for next generation 
        self.lb.update_board(self._curr_dict);

    def checkRules(self,cell,status):
        alive_neighbors = self.lb.getNumAliveNeighbors(cell);
        if status == "Alive":
            # Rule 1
            if alive_neighbors == 2 or alive_neighbors == 3:
                return 
            # Rule 2
            if alive_neighbors == 0 or alive_neighbors == 1:
                self._curr_dict[cell] = "Dead";
                return 
            # Rule 3
            if alive_neighbors >= 4:
                self._curr_dict[cell] = "Dead";
                return 

        if status == "Dead" or status == "Empty":
            # Rule 4
            if alive_neighbors == 3:
                self._curr_dict[cell] = "Alive";
                return 

    def print_board(self):
        print(self.lb);

    def simulate(self, num_gens=1, visual=False, interactive=False, time_delay=False):
        if visual:
            print("-- Generation 0 -- ")
            print(self.lb)
            if interactive:
                input("Press ENTER to evolve next generation")

        for curr_gen in range(num_gens):
            self.run_generation()

            if visual and curr_gen != num_gens-1:
                print("-- Generation {} -- ".format(curr_gen));
                print(self.lb)

                if time_delay:
                    time.sleep(1)

                if interactive:
                    user = input("Press ENTER to evolve next generation or \"x\" to quick evolve to last generation\n>> ");

                    if user == "x":
                        interactive = False

        if visual:
            print("-- Generation {} -- ".format(num_gens));
            print(self.lb)

    def convertDictForJSON(self, curr_dict):
        new_dict = {};
        for pos,status in curr_dict.items():
            # have to format position for json (can't be tuple so we make it a string) 
            better_pos = str(pos[0]) + "," + str(pos[1])
            new_dict[better_pos] = status

        return new_dict

    # for webpage to work 
    def get_complete_simulation(self, num_gens=1):
        complete_arr = []
        complete_arr.append(self.convertDictForJSON(self._curr_dict))
        for x in range(num_gens):
            self.run_generation()
            complete_arr.append(self.convertDictForJSON(self._curr_dict))

        return complete_arr


if __name__ == '__main__':
    # different state configurations 
    start = {(0,0): "Alive", (2,3): "Dead"}
    simple = {(15,30): "Alive", (15,31): "Alive", (16,32): "Alive"}    # all die out 
    stable = {(15,30): "Alive", (15,31): "Alive", (16,31): "Alive"}    # stable population emerges 
    oscillating = {(15,30): "Alive", (15,31): "Alive", (15,32): "Alive"} # alternates between successive generations 
    glider = {(15,30): "Alive", (15,32): "Alive", (14,32): "Alive", (16,32): "Alive", (16,31): "Alive"};
    
    penta_arr = [(15,31), (15,32), (15,33), (14,31), (14,32), (14,33), (16,31), (16,32), (16,33), (17,31), (17,32), (17,33), 
            (18,31), (18,33), (19,31), (19,32), (19,33), (13,31), (13,33), (12,31), (12,32), (12,33)]
    penta = {}
    for x in penta_arr:
        penta[x] = "Alive";
    
    test = [(15,30), (16,31), (16,32), (16,33)]
    test_d = {}
    for x in test:
        test_d[x] = "Alive";

    oscillating_test = {(8,15): "Alive", (8,16): "Alive", (8,17): "Alive"}
    # running the engine 
    engine = LifeEngine("28x60", oscillating_test) 
    # engine.simulate(num_gens=60, visual=True, interactive=False, time_delay=True)
    print(engine.get_complete_simulation(num_gens=10))



