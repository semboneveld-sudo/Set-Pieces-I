from assets.constants import *

BORDER_CELLS = 2

def get_shoot_targets(piece, board):
    targets = []

    # Red shoots UP toward Blue's goal (row BORDER_CELLS - 1)
    # Blue shoots DOWN toward Red's goal (row ROWS - BORDER_CELLS)
    if piece.team == TEAM_RED:
        goal_row = BORDER_CELLS - 1
        valid_directions = [(0,-1), (-1,-1), (1,-1)]
    else:
        goal_row = ROWS - BORDER_CELLS
        valid_directions = [(0,1), (-1,1), (1,1)]

    for dx, dy in valid_directions:
        for step in range(1, piece.shoot_range + 1):
            nx, ny = piece.x + dx*step, piece.y + dy*step
            
            # Check bounds (include the goal row which is outside field)
            in_field = BORDER_CELLS <= nx < COLS - BORDER_CELLS and BORDER_CELLS <= ny < ROWS - BORDER_CELLS
            in_goal = GOAL_START_X <= nx <= GOAL_END_X and ny == goal_row
            
            if not (in_field or in_goal):
                break
            
            # Check if this is a valid shooting target (goal box or goal)
            is_valid_target = False
            
            if in_goal:
                is_valid_target = True
            elif in_field:
                # Check if in enemy goal box
                if piece.team == TEAM_RED:
                    # Red shoots to top - Blue's goal box
                    if ny < BORDER_CELLS + GOAL_BOX_DEPTH and GOAL_BOX_START_X <= nx <= GOAL_BOX_END_X:
                        is_valid_target = True
                else:
                    # Blue shoots to bottom - Red's goal box
                    if ny >= ROWS - BORDER_CELLS - GOAL_BOX_DEPTH and GOAL_BOX_START_X <= nx <= GOAL_BOX_END_X:
                        is_valid_target = True
            
            if is_valid_target:
                targets.append((nx, ny))
            
            # Stop if blocked by piece (but goal row has no pieces)
            if in_field and board.get_piece_at(nx, ny):
                break

    return targets