# file: rendering/sidebar_renderer.py

import pygame
from assets.constants import *

def draw_sidebar(win, board):
    panel_x = COLS*CELL_SIZE
    pygame.draw.rect(win, (30,30,30), (panel_x, 0, PANEL_WIDTH, HEIGHT))

    font = pygame.font.SysFont(None, 28)
    small = pygame.font.SysFont(None, 22)
    big = pygame.font.SysFont(None, 36)

    y = 30

    # SCORE
    red_score = big.render(str(board.red_score), True, RED)
    dash = big.render("-", True, WHITE)
    blue_score = big.render(str(board.blue_score), True, BLUE)
    win.blit(red_score, (panel_x+40, y))
    win.blit(dash, (panel_x+80, y))
    win.blit(blue_score, (panel_x+110, y))
    y += 60

    # TURN
    turn_color = RED if board.current_team == TEAM_RED else BLUE
    turn_text = "RED TURN" if board.current_team == TEAM_RED else "BLUE TURN"
    win.blit(font.render(turn_text, True, turn_color), (panel_x+20, y))
    y += 40

    win.blit(font.render(f"AP: {board.action_points}", True, YELLOW), (panel_x+20, y))
    y += 40

    # PIECE INFO
    if board.selected_piece:
        p = board.selected_piece
        info_top = [f"Strength: {p.strength}", f"Move Range: {p.move_range}", f"Pass Range: {p.pass_range}", f"Shoot Range: {p.shoot_range}"]
        for line in info_top:
            win.blit(small.render(line, True, WHITE), (panel_x+20, y))
            y += 24
        y += 10
        info_bottom = [f"Tackle Cost: {p.tackle_cost}", f"Move Cost: {p.move_cost}", f"Pass Cost: {p.pass_cost}", f"Shoot Cost: {p.shoot_cost}"]
        for line in info_bottom:
            win.blit(small.render(line, True, WHITE), (panel_x+20, y))
            y += 24

    # END TURN BUTTON
    button_rect = pygame.Rect(panel_x+20, HEIGHT-60, PANEL_WIDTH-40, 40)
    pygame.draw.rect(win, ORANGE, button_rect)
    text = font.render("END TURN", True, BLACK)
    win.blit(text, text.get_rect(center=button_rect.center))