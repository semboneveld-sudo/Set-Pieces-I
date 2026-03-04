import pygame
from assets.constants import *

def draw_pieces(win, board):
    # Draw ball if on field - with blink
    if board.ball.position is not None and board.ball.owner is None:
        bx, by = board.ball.position
        ball_x = bx * CELL_SIZE + CELL_SIZE // 2
        ball_y = by * CELL_SIZE + CELL_SIZE // 2
        
        # Blink the ball
        blink = (board.ball.blink_timer // 10) % 2 == 0
        ball_color = WHITE if blink else (200, 200, 200)  # White to gray blink
        pygame.draw.circle(win, ball_color, (ball_x, ball_y), CELL_SIZE//3)
        pygame.draw.circle(win, BLACK, (ball_x, ball_y), CELL_SIZE//3, 2)

    for piece in board.pieces:
        color = RED if piece.team == TEAM_RED else BLUE
        
        # FULL CELL
        pygame.draw.rect(win, color, (piece.x*CELL_SIZE, piece.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        font = pygame.font.SysFont(None, 24)
        
        # Blink name black/white if holding ball
        has_ball = board.ball.owner == piece
        if has_ball:
            blink = (pygame.time.get_ticks() // 300) % 2 == 0
            text_color = BLACK if blink else WHITE
        else:
            text_color = WHITE
            
        text = font.render(piece.kind, True, text_color)
        win.blit(text, text.get_rect(center=(piece.x*CELL_SIZE+CELL_SIZE//2, 
                                             piece.y*CELL_SIZE+CELL_SIZE//2)))

        # Engaged blink (yellow border)
        if piece.engaged:
            if (pygame.time.get_ticks() // 250) % 2 == 0:
                pygame.draw.rect(win, YELLOW, (piece.x*CELL_SIZE, piece.y*CELL_SIZE, 
                                              CELL_SIZE, CELL_SIZE), 3)