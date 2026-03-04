import pygame
from assets.constants import *

def draw_goal_overlay(win, board):
    if board.goal_scored:
        # Pulsing effect
        pulse = (pygame.time.get_ticks() % 1000) / 1000.0
        scale = 1.0 + 0.1 * abs(pulse - 0.5) * 2
        
        big_font = pygame.font.SysFont(None, int(120 * scale))
        color = RED if board.goal_team == TEAM_RED else BLUE
        
        # Draw semi-transparent background
        overlay = pygame.Surface((COLS*CELL_SIZE, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        win.blit(overlay, (0, 0))
        
        # Draw GOAL text
        text = big_font.render("GOAL!", True, color)
        text_rect = text.get_rect(center=(COLS*CELL_SIZE//2, HEIGHT//2))
        win.blit(text, text_rect)
        
        # Draw team name
        small_font = pygame.font.SysFont(None, 48)
        team_name = "RED SCORES!" if board.goal_team == TEAM_RED else "BLUE SCORES!"
        team_text = small_font.render(team_name, True, WHITE)
        team_rect = team_text.get_rect(center=(COLS*CELL_SIZE//2, HEIGHT//2 + 80))
        win.blit(team_text, team_rect)