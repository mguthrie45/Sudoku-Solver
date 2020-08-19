from Main import *
import pygame, sys
import time
from pygame.locals import *

WIDTH = 500
HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

fps = 30

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Solver")
    win.fill(BLACK)

    clock = pygame.time.Clock()

    grid = Grid(9, 9)

    draw_grid(grid, win)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        solve_grid(grid, win)
        draw_grid(grid, win)
        pygame.display.update()
        clock.tick(fps)
    
    print(grid)
    
    pygame.quit()
    sys.exit()

def solve_grid(grid, window):
    empty_coord = find_empty(grid.board)
    if empty_coord is None:
        return True

    i, j = empty_coord         
        
    for num in range(1, 10):
        if valid(i, j, num, grid):
            grid.update(i, j, num)
            draw_grid(grid, window)
            fill_box(window, grid, GREEN, (i, j))
            pygame.display.update()
            pygame.event.pump()
            pygame.time.delay(60)

            if solve_grid(grid, window):
                return True
            grid.update(i, j, 0)
            draw_grid(grid, window)
            fill_box(window, grid, RED, (i, j))
            pygame.display.update()
            pygame.event.pump()
            pygame.time.delay(60)
    return False

def fill_box(window, grid, color, xy_tuple):
    vert_cell_px = HEIGHT//9
    horiz_cell_px = WIDTH//9
    x, y = xy_tuple
    rect = pygame.Rect(x*horiz_cell_px, y*vert_cell_px, horiz_cell_px-1, vert_cell_px-1)
    pygame.draw.rect(window, color, rect)

def draw_grid(grid, window):
    vert_cell_px = HEIGHT//9
    horiz_cell_px = WIDTH//9

    for x in range(9):
        for y in range(9):
            rect = pygame.Rect(x*horiz_cell_px, y*vert_cell_px, horiz_cell_px-1, vert_cell_px-1)
            pygame.draw.rect(window, WHITE, rect)

            num = str(grid.board[x][y])
            if num != "0":
                font = pygame.font.SysFont('Tahoma', 45, False, False)
                text = font.render(num, True, BLACK)
                window.blit(text, (x*horiz_cell_px+horiz_cell_px/4, y*vert_cell_px))


main()