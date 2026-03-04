from assets.constants import *
from assets.pieces import Defender, Midfielder, Attacker, Goalkeeper

BORDER_CELLS = 2

def inside_board(x, y):
    return BORDER_CELLS <= x < COLS - BORDER_CELLS and BORDER_CELLS <= y < ROWS - BORDER_CELLS

def in_goal_box(x, y, team):
    """Check if position is in team's goal box"""
    if team == TEAM_RED:
        return y >= ROWS - BORDER_CELLS - GOAL_BOX_DEPTH and GOAL_BOX_START_X <= x <= GOAL_BOX_END_X
    else:
        return y < BORDER_CELLS + GOAL_BOX_DEPTH and GOAL_BOX_START_X <= x <= GOAL_BOX_END_X

def get_moves(piece, board):
    moves = []

    # DEFENDERS + GOALKEEPERS (1 tile in all directions)
    if isinstance(piece, (Defender, Goalkeeper)):
        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
        for dx, dy in directions:
            nx, ny = piece.x + dx, piece.y + dy
            if not inside_board(nx, ny):
                continue
            if board.get_piece_at(nx, ny):
                continue

            # GK restricted to goal box
            if isinstance(piece, Goalkeeper):
                if piece.team == TEAM_RED:
                    if not (ROWS - BORDER_CELLS - GOAL_BOX_DEPTH <= ny < ROWS - BORDER_CELLS):
                        continue
                elif piece.team == TEAM_BLUE:
                    if not (BORDER_CELLS <= ny < BORDER_CELLS + GOAL_BOX_DEPTH):
                        continue
            else:
                # Defenders cannot enter ANY goal box
                if in_goal_box(nx, ny, TEAM_RED) or in_goal_box(nx, ny, TEAM_BLUE):
                    continue

            moves.append((nx, ny))

    # MIDFIELDERS (can move up to move_range like a queen)
    elif isinstance(piece, Midfielder):
        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
        for dx, dy in directions:
            for step in range(1, piece.move_range + 1):
                nx, ny = piece.x + dx*step, piece.y + dy*step
                if not inside_board(nx, ny):
                    break
                if board.get_piece_at(nx, ny):
                    break
                # Midfielders cannot enter goal boxes
                if in_goal_box(nx, ny, TEAM_RED) or in_goal_box(nx, ny, TEAM_BLUE):
                    break
                moves.append((nx, ny))

    # ATTACKERS (ring at distance 2)
    elif isinstance(piece, Attacker):
        for dx in range(-2,3):
            for dy in range(-2,3):
                if max(abs(dx),abs(dy)) != 2:
                    continue
                nx, ny = piece.x + dx, piece.y + dy
                if not inside_board(nx, ny):
                    continue
                if board.get_piece_at(nx, ny):
                    continue
                # Attackers cannot enter goal boxes
                if in_goal_box(nx, ny, TEAM_RED) or in_goal_box(nx, ny, TEAM_BLUE):
                    continue
                moves.append((nx, ny))

    return moves