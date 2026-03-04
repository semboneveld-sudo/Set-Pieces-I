# Set Pieces I
### A Bonairo Project

> *A deterministic, chess-inspired football strategy game.*

---

## Overview

**Set Pieces I** is a two-player strategy game that sits at the intersection of football tactics and chess-like logic. Two teams of 11 pieces face off on a 13×18 tile pitch — every move, pass, tackle, and shot resolves with complete determinism. No dice. No probability. Just pure strategy.

The only randomness in the entire game: which Midfielder gets the ball at kickoff.

---

## How It Works

### The Teams
Each team fields **11 pieces** across four roles:

| Role | Symbol | Style |
|------|--------|-------|
| Goalkeeper | `GK` | King-range movement, penalty box only |
| Defender | `DF` | King-range movement, high strength |
| Midfielder | `MF` | Queen-range movement (up to 2 tiles), versatile passer |
| Attacker | `AT` | Free-range movement (5×5 area), best shooter |

### The Action Economy
Each turn, a player has **9 Action Points (AP)**. Every action — moving, passing, shooting, tackling — costs AP. Spend them wisely; your turn ends when AP hits zero (or you choose to stop).

### Winning
Score a goal. The game ends immediately. No saves, no keepers diving — if a shot reaches the goal tile unobstructed, it's in.

---

## Core Mechanics

**Movement** — Each piece type moves differently. GKs and DFs move like a chess king (1 tile, any direction). MFs glide like a queen up to 2 tiles. ATs jump freely within a 5×5 area, ignoring blocking pieces.

**Passing** — All pieces pass along straight lines (horizontal, vertical, diagonal). Passes can travel through enemy pieces but are blocked by allies. Balls can be left on empty tiles for teammates to pick up.

**Tackling** — Adjacent allies stack their Strength to overwhelm a ball-holder. If combined strength exceeds the holder's, the tackler swaps positions and gains the ball. A successful tackle leaves the tackler *Engaged* — immune to tackles for the opponent's next full turn.

**Shooting** — Only possible toward the opposing goal, in a straight line, within Shoot Range, with no pieces in the way. If it reaches the goal: game over.

---

## Project Structure

```
SetPiecesI/
├── assets/         # Game assets and piece definitions
├── board/          # Board and formation logic
├── mechanics/      # Game rules: movement, passing, shooting, tackling
├── rendering/      # Field, pieces, highlights, and sidebar renderers
├── main.py         # Main game loop
├── player.py       # Player logic
├── utils.py        # Utility functions
├── rules.txt       # Full game rules
└── Makefile        # Run and clean commands
```

---

## Running the Game

```bash
make run        # Launch the game
make clean      # Remove __pycache__, .pyc files, and temp results
make rebuild    # Clean then run
```

---

## Design Philosophy

Set Pieces I is built around **perfect information and full determinism**. Every outcome is the direct result of player decisions — there's no hidden luck to blame or rely on. The tension comes from positioning, resource management, and reading your opponent's setup before committing your AP.

Think of it less like football simulation and more like football as a puzzle.

---

*Set Pieces I — Part of the Bonairo project series.*