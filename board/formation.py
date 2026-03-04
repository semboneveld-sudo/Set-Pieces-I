from assets.pieces import Goalkeeper, Defender, Midfielder, Attacker
from assets.constants import *

BORDER_CELLS = 2

def create_433_formation():
    pieces = []
    center_x = COLS // 2
    
    # Field bounds
    field_top = BORDER_CELLS
    field_bottom = ROWS - BORDER_CELLS - 1
    
    # BLUE TEAM (top)
    blue_goalie_row = field_top + GOAL_BOX_DEPTH - 1
    pieces.append(Goalkeeper(center_x, blue_goalie_row, TEAM_BLUE))
    
    # Defenders - right after goal box
    blue_def_row = field_top + GOAL_BOX_DEPTH + 1
    pieces += [
        Defender(center_x - 4, blue_def_row, TEAM_BLUE),
        Defender(center_x - 1, blue_def_row, TEAM_BLUE),
        Defender(center_x + 1, blue_def_row, TEAM_BLUE),
        Defender(center_x + 4, blue_def_row, TEAM_BLUE)
    ]
    
    # Midfielders - 1 row gap from defenders
    blue_mid_row = blue_def_row + 2
    pieces += [
        Midfielder(center_x - 3, blue_mid_row, TEAM_BLUE),
        Midfielder(center_x, blue_mid_row, TEAM_BLUE),
        Midfielder(center_x + 3, blue_mid_row, TEAM_BLUE)
    ]
    
    # Attackers - 1 row gap from midfielders
    blue_atk_row = blue_mid_row + 2
    pieces += [
        Attacker(center_x - 3, blue_atk_row, TEAM_BLUE),
        Attacker(center_x, blue_atk_row, TEAM_BLUE),
        Attacker(center_x + 3, blue_atk_row, TEAM_BLUE)
    ]

    # RED TEAM (bottom)
    red_goalie_row = field_bottom - GOAL_BOX_DEPTH + 1
    pieces.append(Goalkeeper(center_x, red_goalie_row, TEAM_RED))
    
    # Defenders - right after goal box (going up)
    red_def_row = field_bottom - GOAL_BOX_DEPTH - 1
    pieces += [
        Defender(center_x - 4, red_def_row, TEAM_RED),
        Defender(center_x - 1, red_def_row, TEAM_RED),
        Defender(center_x + 1, red_def_row, TEAM_RED),
        Defender(center_x + 4, red_def_row, TEAM_RED)
    ]
    
    # Midfielders - 1 row gap from defenders
    red_mid_row = red_def_row - 2
    pieces += [
        Midfielder(center_x - 3, red_mid_row, TEAM_RED),
        Midfielder(center_x, red_mid_row, TEAM_RED),
        Midfielder(center_x + 3, red_mid_row, TEAM_RED)
    ]
    
    # Attackers - 1 row gap from midfielders
    red_atk_row = red_mid_row - 2
    pieces += [
        Attacker(center_x - 3, red_atk_row, TEAM_RED),
        Attacker(center_x, red_atk_row, TEAM_RED),
        Attacker(center_x + 3, red_atk_row, TEAM_RED)
    ]

    return pieces