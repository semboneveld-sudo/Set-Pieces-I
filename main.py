import pygame
from board.board import Board
from assets.constants import *
from rendering.renderer import draw

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football Chess")

def main():
    clock = pygame.time.Clock()
    board = Board()
    running = True
    targeting_mode = False  # Are we showing pass/shoot targets?

    while running:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()
        gx = mx // CELL_SIZE
        gy = my // CELL_SIZE

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if board.goal_scored:
                continue

            panel_x = COLS*CELL_SIZE
            button_rect = pygame.Rect(panel_x+20, HEIGHT-60, PANEL_WIDTH-40, 40)

            if event.type == pygame.MOUSEBUTTONDOWN:

                # END TURN BUTTON
                if button_rect.collidepoint(mx, my):
                    board.end_turn()
                    targeting_mode = False
                    continue

                # LEFT CLICK
                if event.button == 1:
                    clicked_piece = board.get_piece_at(gx, gy)
                    
                    # If in targeting mode, left click cancels it
                    if targeting_mode:
                        targeting_mode = False
                        board.pass_targets = []
                        board.shoot_targets = []
                        board.possible_moves = []
                        if clicked_piece and clicked_piece.team == board.current_team:
                            board.select_piece(clicked_piece)
                        continue
                    
                    # Tackle check - if clicking on enemy with ball adjacent
                    if board.selected_piece:
                        attacker = board.selected_piece
                        defender = board.get_piece_at(gx, gy)
                        if defender and defender.team != attacker.team and board.ball.owner == defender:
                            if defender in board.get_tackle_targets(attacker):
                                board.attempt_tackle(attacker, defender)
                                continue
                    
                    # Move check
                    if board.selected_piece and (gx, gy) in board.possible_moves:
                        attacker = board.selected_piece
                        if board.action_points >= attacker.move_cost:
                            attacker.set_pos(gx, gy)
                            board.action_points -= attacker.move_cost
                            if board.ball.position == (gx, gy):
                                board.ball.give_to(attacker)
                            board.clear_selection()
                            board.switch_turn_after_action()
                            continue
                    
                    # Select piece
                    if clicked_piece and clicked_piece.team == board.current_team:
                        board.select_piece(clicked_piece)
                        targeting_mode = False

                # RIGHT CLICK - Toggle targeting mode
                if event.button == 3:
                    if not board.selected_piece:
                        continue
                    
                    piece = board.selected_piece
                    
                    # Must have ball to target
                    if board.ball.owner != piece:
                        targeting_mode = False
                        board.pass_targets = []
                        board.shoot_targets = []
                        continue
                    
                    # Toggle targeting mode on first right click
                    if not targeting_mode:
                        board.pass_targets = board.get_pass_targets(piece)
                        board.shoot_targets = board.get_shoot_targets(piece)
                        board.possible_moves = []
                        targeting_mode = True
                    else:
                        # Already in targeting mode - execute action
                        if (gx, gy) in board.pass_targets:
                            if board.action_points >= piece.pass_cost:
                                target_piece = board.get_piece_at(gx, gy)
                                if target_piece:
                                    board.ball.give_to(target_piece)
                                else:
                                    board.ball.place_on_field(gx, gy)
                                board.action_points -= piece.pass_cost
                                board.clear_selection()
                                targeting_mode = False
                                board.switch_turn_after_action()
                        
                        elif (gx, gy) in board.shoot_targets:
                            if board.action_points >= piece.shoot_cost:
                                board.execute_shot(piece, gx, gy)
                                targeting_mode = False

        draw(WIN, board)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()