import pprint
import time

from Generator import generate_board

pp = pprint.PrettyPrinter(depth=6)

def missing_numbers(num_list):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(num_list)):
        for j in numbers:
            if num_list[i] == j:
                numbers.remove(j)
    return numbers

class Grid():
    board = generate_board()

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.model = None

    def column(self, j):
        array = []
        for i in range(len(self.board)):
            array.append(self.board[i][j])
        return array

    def cube(self, i, j): #returns a list of the indices the cube you are in.
        num_list = []

        cube_coord = (i//3, j//3) #1, 1 would be a range i(3, 5) and j(3, 5)

        i_range = (cube_coord[0]*3, cube_coord[0]*3+2)
        j_range = (cube_coord[1]*3, cube_coord[1]*3+2)

        for i in range(i_range[0], i_range[1]+1):
            for j in range(j_range[0], j_range[1]+1):
                num_list.append(self.board[i][j])
        return num_list

    def update(self, i, j, val):
        self.board[i][j] = val

    def solve(self, board):
        empty_coord = find_empty(self.board)
        if empty_coord is None:
            return True

        i, j = empty_coord         
        
        for num in range(1, 10):
            if valid(i, j, num, self):
                self.update(i, j, num)

                if self.solve(self.board):
                    return True
                self.update(i, j, 0)
        return False

        

    def __repr__(self):
        st = "--------------------------\n"
        for i in self.board:
            for j in i:
                st += str(j)
                st += "  "
            st += "\n"
        return st + "--------------------------"


    __str__ = __repr__



def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None

def missing_cube_numbers(i, j, grid):
    num_list = grid.cube(i, j)
    miss_n = missing_numbers(num_list)
    return miss_n

def missing_col_numbers(j, grid):
    num_list = grid.column(j)
    miss_n = missing_numbers(num_list)
    return miss_n

def missing_row_numbers(i, grid):
    num_list = grid.board[i]
    miss_n = missing_numbers(num_list)
    return miss_n

def intersecting_missing(i, j, grid):
    row = missing_row_numbers(i, grid)
    col = missing_col_numbers(j, grid)
    box = missing_cube_numbers(i, j, grid)
    common = set(row).intersection(set(col), set(box))
    return list(common)

def valid(i, j, num, grid):
    if num in intersecting_missing(i, j, grid):
        return True
    return False
'''
def main():
    grid = Grid(9, 9)
    print(grid)

    grid.solve(grid.board)
    print(grid)

main()'''