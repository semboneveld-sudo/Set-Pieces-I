import pygame
from assets.constants import *

def draw_highlights(win, board):
    # MOVES
    for x, y in board.possible_moves:
        pygame.draw.rect(win, ORANGE, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # PASSES
    for x, y in board.pass_targets:
        pygame.draw.rect(win, PURPLE, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # SHOOTS
    for x, y in board.shoot_targets:
        pygame.draw.rect(win, RED_SHOOT, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # TACKLE TARGETS
    if board.selected_piece:
        blink = (pygame.time.get_ticks() // 300) % 2 == 0
        if blink:
            for t in board.get_tackle_targets(board.selected_piece):
                pygame.draw.rect(win, (0, 255, 255), (t.x*CELL_SIZE, t.y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)