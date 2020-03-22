from termcolor import colored

class LifeBoard:

    def __init__(self, boardsize, arrangement):
        size = boardsize.split("x");
        self.board = self.get_empty_board(int(size[0]),int(size[1]));
        self.update_board(arrangement);

    def update_board(self, arrangement):
        for pos,status in arrangement.items():
            x = pos[0];
            y = pos[1];
            if status == "Alive":
                self.board[x][y] = "|O|";
            else:
                self.board[x][y] = "|X|";

    def __str__(self):
        to_print = ""
        to_print += "GAMEBOARD:\n"
        # to_print += "-" * (self.getColSize() * 4 - 1) + "\n"
        for i in range(self.getRowSize()):
            for j in range(self.getColSize()):
                content = self.board[i][j]
                if content == "|O|":
                    to_print += colored("| |", "green") + " ";
                #elif content == "|X|":
                #    # to_print += colored(content, "red") + " ";
                #    to_print += "| |" + " "; 
                #elif content == "|.|":
                #    # to_print += colored(content, "grey") + " ";
                #    to_print += content + " "
                else:
                    # to_print += content + " ";
                    to_print += "   " + " ";
            to_print += "\n" + " " * (self.getColSize() * 4 - 1) + "\n"

        return to_print 


    def get_empty_board(self, row_size, col_size):
        board = [];
        for i in range(row_size):
            new_arr = ["|.|"] * col_size;
            board.append(new_arr);
        return board 

    def getRowSize(self):
        return len(self.board);

    def getColSize(self):
        return len(self.board[0]);

    def get_cell(self, cell):
        cell_formatted = self.board[cell[0]][cell[1]]
        return cell_formatted[1];

    def get_neighbor(self, cell, direction):
        x = cell[0];
        y = cell[1];
        row_counter = 0;
        col_counter = 0;
        # cardinal directions 
        if(direction=="l"):
            col_counter = -1;
        if(direction=="r"):
            col_counter = 1;
        if(direction=="u"):
            row_counter = -1;
        if(direction=="d"):
            row_counter = 1;
        # diagonals directions 
        if(direction=="ur"):
            col_counter = 1;
            row_counter = -1;
        if(direction=="ul"):
            col_counter = -1;
            row_counter = -1;
        if(direction=="dr"):
            col_counter = +1;
            row_counter = 1;
        if(direction=="dl"):
            col_counter = -1;
            row_counter = 1;
        # getting cell
        try:
            neighbor = self.get_cell((x+row_counter,y+col_counter));
            return neighbor;
        except IndexError:
            return "."

    def isAlive(self, cell):
        if isinstance(cell, str):
            return cell=="O"
        return self.get_cell(cell) == "O";

    def isDead(self, cell):
        if isinstance(cell, str):
            return cell=="X"
        return self.get_cell(cell) == "X";

    def isEmpty(self, cell):
        if isinstance(cell, str):
            return cell=="."
        return self.get_cell(Cell) == ".";

    def getNumAliveNeighbors(self, cell):
        directions = ["l", "r", "u", "d", "ul", "ur", "dl", "dr"]
        counter = 0;
        for d in directions:
            if self.isAlive(self.get_neighbor(cell, d)):
                counter += 1;
        return counter

    def __iter__(self):
        return _BoardIterator(self.board)


class _BoardIterator:

    def __init__(self, board):
        self._boardRef = board;
        self._rowIndex = 0;
        self._colIndex = 0;
        # self.temp = 0;

    def __iter__(self):
        return self;

    def __next__(self):
        # if self._rowIndex > len(self._boardRef) or self.temp > 20:
        if self._rowIndex == len(self._boardRef):
            raise StopIteration

        if self._colIndex < len(self._boardRef[self._rowIndex]):
            row_index = self._rowIndex;
            col_index = self._colIndex;

            if self._colIndex+1 == len(self._boardRef[self._rowIndex]):
                self._colIndex = 0;
                self._rowIndex += 1;
            else:
                self._colIndex += 1;
        
            # self.temp += 1;

            return (row_index, col_index); 







if __name__ == "__main__":
    b = LifeBoard("10x10", {(0,0): "Alive", (2,3): "Dead"});
    print(b)
    print("(0,0) should be Alive, (2,3) should be Dead");
    print("Left Neighbor of (0,1): " + b.get_neighbor((0,1),"l") + " <- should be alive");
    print("Upper Right  Neighbor of (3,2): " + b.get_neighbor((3,2),"ur") + " <- should be dead");
    print("Should say HIT WALL: ", end="")
    print("Gettng right neighbor of (0,9) should say HIT WALL above and return \".\": " 
            + b.get_neighbor((0,9), "r"));
    print("Alive neighbors of (1,4) should be 0: " 
            + str(b.getNumAliveNeighbors((1,4))));
    print("Alive Neighbors of (1,1) should be 1: " +
            str(b.getNumAliveNeighbors((1,1)))); 
    print("Alive Neighbors of (1,0) should be 1: " +
            str(b.getNumAliveNeighbors((1,0)))); 
    
    counter = 0
    for cell in b:
        print(cell)
        counter += 1;

    print("Iterator should give us " + str(b.getRowSize() * b.getColSize()) 
            + " values: " + str(counter));
