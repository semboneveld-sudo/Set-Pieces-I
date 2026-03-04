from assets.constants import *

def get_adjacent_positions(x, y):
    positions = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            positions.append((x + dx, y + dy))
    return positions

def get_tackle_targets(board, piece):
    targets = []

    for pos in get_adjacent_positions(piece.x, piece.y):
        x, y = pos
        target = board.get_piece_at(x, y)

        if not target:
            continue

        if target.team == piece.team:
            continue

        if board.ball.owner != target:
            continue

        if target.engaged:
            continue

        targets.append(target)

    return targets

def resolve_tackle(board, tackler, defender):
    # Calculate attack strength
    attack_strength = tackler.strength

    for pos in get_adjacent_positions(defender.x, defender.y):
        supporter = board.get_piece_at(*pos)

        if not supporter:
            continue

        if supporter.team != tackler.team:
            continue

        if supporter == tackler:
            continue

        if supporter.engaged:
            continue

        attack_strength += supporter.strength

    defense_strength = defender.strength

    # SUCCESS
    if attack_strength > defense_strength:

        # Swap positions
        tx, ty = tackler.x, tackler.y
        dx, dy = defender.x, defender.y

        tackler.set_pos(dx, dy)
        defender.set_pos(tx, ty)

        # Give ball
        board.ball.give_to(tackler)

        # Engage tackler
        tackler.engaged = True
        tackler.engaged_turn = board.turn_counter

        return True

    return False