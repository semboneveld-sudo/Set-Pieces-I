# file: rendering/renderer.py

import pygame
from rendering.field_renderer import draw_field
from rendering.pieces_renderer import draw_pieces
from rendering.highlights_renderer import draw_highlights
from rendering.sidebar_renderer import draw_sidebar
from rendering.goal_overlay_renderer import draw_goal_overlay

def draw(win, board):
    draw_field(win)
    draw_highlights(win, board)
    draw_pieces(win, board)
    draw_sidebar(win, board)
    draw_goal_overlay(win, board)