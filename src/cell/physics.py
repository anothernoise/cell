"""Simple 2D motion physics for organelles."""

from __future__ import annotations

import pygame


def keep_inside_bounds(pos: pygame.math.Vector2, bounds: pygame.Rect) -> None:
    """Keep a position inside the given rectangle bounds."""
    if pos.x < bounds.left:
        pos.x = bounds.left
    if pos.x > bounds.right:
        pos.x = bounds.right
    if pos.y < bounds.top:
        pos.y = bounds.top
    if pos.y > bounds.bottom:
        pos.y = bounds.bottom
