# utils.py

def get_piece_at(pos, pieces):
    x,y = pos
    for piece in pieces:
        if piece.x==x and piece.y==y:
            return piece
    return None