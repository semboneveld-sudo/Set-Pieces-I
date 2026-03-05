# file: assets/pieces.py

from assets.constants import *

class Piece:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        self.kind = "P"
        self.strength = 5
        self.move_range = 1
        self.pass_range = 2
        self.tackle_cost = 2
        self.move_cost = 2
        self.pass_cost = 2
        self.engaged = False

        self.shoot_cost = 5
        self.shoot_range = 3

    def set_pos(self, x, y):
        self.x = x
        self.y = y

class Goalkeeper(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self.kind = "GK"
        self.strength = 6
        self.move_range = 1
        self.pass_range = 4
        self.tackle_cost = 3
        self.move_cost = 2
        self.pass_cost = 2
        self.shoot_cost = 5
        self.shoot_range = 3

class Defender(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self.kind = "DF"
        self.strength = 6
        self.move_range = 1
        self.pass_range = 2

class Midfielder(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self.kind = "MF"
        self.strength = 5
        self.move_range = 2
        self.pass_range = 4
        self.move_cost = 3
        self.pass_cost = 2
        self.shoot_cost = 4
        self.shoot_range = 3

class Attacker(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self.kind = "AT"
        self.strength = 4
        self.move_range = 2
        self.pass_range = 2
        self.move_cost = 3
        self.pass_cost = 2
        self.shoot_cost = 3
        self.shoot_range = 4