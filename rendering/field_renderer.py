import pygame
from assets.constants import *

BORDER_CELLS = 2

def draw_field(win):
    # Fill entire window with border color (gray)
    win.fill(GRAY)
    
    # Draw the field tiles (checkerboard) - only in field area
    for r in range(BORDER_CELLS, ROWS - BORDER_CELLS):
        for c in range(BORDER_CELLS, COLS - BORDER_CELLS):
            color = GREEN if (r + c) % 2 == 0 else DARK_GREEN
            pygame.draw.rect(win, color, (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw goal boxes (light green areas) - as part of field
    for r in range(GOAL_BOX_DEPTH):
        for c in range(GOAL_BOX_START_X, GOAL_BOX_END_X+1):
            # Top goal box (Blue's side)
            pygame.draw.rect(win, LIGHT_GRASS, (c*CELL_SIZE, (BORDER_CELLS + r)*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            # Bottom goal box (Red's side)
            pygame.draw.rect(win, LIGHT_GRASS, (c*CELL_SIZE, (ROWS - BORDER_CELLS - 1 - r)*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw goals (white cells in border) - 5x1 cut out from border
    # Top goal (Blue's goal)
    for c in range(GOAL_START_X, GOAL_END_X+1):
        pygame.draw.rect(win, WHITE, (c*CELL_SIZE, (BORDER_CELLS - 1)*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Bottom goal (Red's goal)
    for c in range(GOAL_START_X, GOAL_END_X+1):
        pygame.draw.rect(win, WHITE, (c*CELL_SIZE, (ROWS - BORDER_CELLS)*CELL_SIZE, CELL_SIZE, CELL_SIZE))