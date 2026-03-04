import random
import pygame
from assets.constants import *
from assets.pieces import Midfielder
from mechanics.movement import get_moves
from mechanics.passing import get_pass_targets
from mechanics.shooting import get_shoot_targets
from board.formation import create_433_formation
from assets.ball import Ball
from mechanics.game_rules import get_tackle_targets, resolve_tackle
import rendering.renderer as renderer

class Board:
    def __init__(self):
        self.pieces = create_433_formation()
        self.selected_piece = None
        self.possible_moves = []
        self.pass_targets = []
        self.shoot_targets = []
        self.pass_mode = False

        self.current_team = TEAM_RED
        self.action_points = 9
        self.turn_counter = 0

        self.ball = Ball()

        # SCORE
        self.red_score = 0
        self.blue_score = 0

        # GOAL STATE
        self.goal_scored = False
        self.goal_team = None
        self.goal_timer = 0
        self.goal_animation_done = False  # Track if we've processed the goal

        self.assign_starting_ball()

    def assign_starting_ball(self):
        team = random.choice([TEAM_RED, TEAM_BLUE])
        mids = [p for p in self.pieces if isinstance(p, Midfielder) and p.team == team]
        player = random.choice(mids)
        self.ball.give_to(player)
        self.current_team = team

    def get_piece_at(self, x, y):
        for p in self.pieces:
            if p.x == x and p.y == y:
                return p
        return None

    def get_moves(self, piece):
        return get_moves(piece, self)

    def get_pass_targets(self, piece):
        return [t for t in get_pass_targets(piece, self) if t != (piece.x, piece.y)]

    def get_shoot_targets(self, piece):
        if self.goal_scored:
            return []
        return [t for t in get_shoot_targets(piece, self) if t != (piece.x, piece.y)]

    def get_tackle_targets(self, piece):
        return get_tackle_targets(self, piece)

    def execute_shot(self, piece, x, y):
        if self.action_points < piece.shoot_cost:
            return False
        self.action_points -= piece.shoot_cost
        self.ball.owner = None
        self.ball.position = (x, y)

        if self.is_goal(x, y, piece.team):
            self.trigger_goal(piece.team)

        self.clear_selection()
        self.switch_turn_after_action()
        return True

    def is_goal(self, x, y, team):
        BORDER_CELLS = 2
        if team == TEAM_RED:
            return y == BORDER_CELLS - 1 and GOAL_START_X <= x <= GOAL_END_X
        else:
            return y == ROWS - BORDER_CELLS and GOAL_START_X <= x <= GOAL_END_X

    def trigger_goal(self, team):
        self.goal_scored = True
        self.goal_team = team
        self.goal_timer = pygame.time.get_ticks()
        self.goal_animation_done = False

    def update_goal_animation(self):
        if not self.goal_scored:
            return

        current_time = pygame.time.get_ticks()
        
        # Check if 5 seconds have passed (5000 milliseconds)
        if current_time - self.goal_timer >= 5000:
            if not self.goal_animation_done:
                # Process the goal - add score and reset
                if self.goal_team == TEAM_RED:
                    self.red_score += 1
                    conceding_team = TEAM_BLUE
                else:
                    self.blue_score += 1
                    conceding_team = TEAM_RED

                # Give ball to random midfielder on conceding team
                mids = [p for p in self.pieces if isinstance(p, Midfielder) and p.team == conceding_team]
                if mids:
                    player = random.choice(mids)
                    self.ball.give_to(player)

                # Switch to conceding team's turn
                self.current_team = conceding_team
                self.action_points = 9
                self.turn_counter += 1
                
                # Clear engaged status
                for piece in self.pieces:
                    if hasattr(piece, 'engaged') and piece.engaged:
                        if self.turn_counter > getattr(piece, 'engaged_turn', 0) + 1:
                            piece.engaged = False

                self.goal_animation_done = True
                self.goal_scored = False
                self.goal_team = None

    def attempt_tackle(self, attacker, defender):
        if self.action_points < attacker.tackle_cost:
            return False
        result = resolve_tackle(self, attacker, defender)
        if result:
            self.action_points -= attacker.tackle_cost
            self.clear_selection()
            self.switch_turn_after_action()
            return True
        else:
            self.action_points -= attacker.tackle_cost
            self.clear_selection()
            self.switch_turn_after_action()
            return False

    def switch_turn_after_action(self):
        if self.action_points <= 0:
            self.end_turn()

    def end_turn(self):
        if self.goal_scored:
            return
        self.action_points = 9
        self.current_team = TEAM_RED if self.current_team == TEAM_BLUE else TEAM_BLUE
        self.turn_counter += 1
        for piece in self.pieces:
            if hasattr(piece, 'engaged') and piece.engaged:
                if self.turn_counter > getattr(piece, 'engaged_turn', 0) + 1:
                    piece.engaged = False
        self.clear_selection()

    def select_piece(self, piece):
        if self.goal_scored:
            return
        self.selected_piece = piece
        self.possible_moves = self.get_moves(piece)
        self.pass_targets = []
        self.shoot_targets = []

    def clear_selection(self):
        self.selected_piece = None
        self.possible_moves = []
        self.pass_targets = []
        self.shoot_targets = []

    def draw(self, win):
        self.ball.update()
        self.update_goal_animation()
        renderer.draw(win, self)