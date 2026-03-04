# file: assets/ball.py

import pygame
from assets.constants import *

class Ball:
    def __init__(self):
        self.owner = None
        self.position = None
        self.blink_timer = 0

    def give_to(self, piece):
        self.owner = piece
        self.position = None

    def place_on_field(self, x, y):
        self.owner = None
        self.position = (x, y)

    def clear(self):
        self.owner = None
        self.position = None

    def update(self):
        self.blink_timer += 1