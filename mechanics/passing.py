from assets.constants import *

BORDER_CELLS = 2

def get_pass_targets(piece, board):
    targets = []
    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]

    for dx, dy in directions:
        for step in range(1, piece.pass_range + 1):
            nx, ny = piece.x + dx*step, piece.y + dy*step
            if not (BORDER_CELLS <= nx < COLS - BORDER_CELLS and BORDER_CELLS <= ny < ROWS - BORDER_CELLS):
                break

            # Cannot pass into enemy goal box
            if piece.team == TEAM_RED and ny >= ROWS - BORDER_CELLS - GOAL_BOX_DEPTH:
                break
            if piece.team == TEAM_BLUE and ny < BORDER_CELLS + GOAL_BOX_DEPTH:
                break

            targets.append((nx, ny))
            # Stop if piece is in the way
            if board.get_piece_at(nx, ny):
                break

    return targets