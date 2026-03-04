class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.pieces = []  # List of pieces owned
    
    def take_turn(self, board, ball):
        """Select which piece to move, pass, or shoot."""