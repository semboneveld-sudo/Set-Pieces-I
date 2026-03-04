# =============================
# BOARD DIMENSIONS
# =============================
COLS = 17          # Reduced by 2 (was 19)
ROWS = 22          # Keep same for border + field

CELL_SIZE = 40

# =============================
# PANEL SETTINGS
# =============================
PANEL_WIDTH = 180
WIDTH = COLS * CELL_SIZE + PANEL_WIDTH
HEIGHT = ROWS * CELL_SIZE

# =============================
# GOAL SETTINGS
# =============================
GOAL_WIDTH = 5
GOAL_DEPTH = 1

GOAL_BOX_WIDTH = 7
GOAL_BOX_DEPTH = 2

GOAL_START_X = (COLS - GOAL_WIDTH) // 2
GOAL_END_X = GOAL_START_X + GOAL_WIDTH - 1

GOAL_BOX_START_X = (COLS - GOAL_BOX_WIDTH) // 2
GOAL_BOX_END_X = GOAL_BOX_START_X + GOAL_BOX_WIDTH - 1

# =============================
# TEAM IDS
# =============================
TEAM_RED = 1
TEAM_BLUE = 2

# =============================
# COLORS
# =============================
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
LIGHT_GRASS = (124, 252, 0)

GRAY = (60, 60, 60)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 40, 40)
BLUE = (40, 40, 200)
RED_SHOOT = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
PURPLE = (150, 0, 200)