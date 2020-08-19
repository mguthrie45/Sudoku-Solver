from Main import *

def solve(grid):
    empty_coord = find_empty(grid.board)
    if empty_coord is None:
        return True

    i, j = empty_coord         
        
    for num in range(1, 10):
        if valid(i, j, num, grid):
            grid.update(i, j, num)

            if solve(grid):
                return True
            grid.update(i, j, 0)
    return False