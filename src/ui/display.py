"""UI helpers using pygame."""

from __future__ import annotations

import pygame


class UIButton:
    def __init__(self, rect: pygame.Rect, text: str):
        self.rect = rect
        self.text = text
        self.font = pygame.font.SysFont(None, 24)
        self.color = (50, 50, 50)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)
        txt = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(txt, (self.rect.x + 5, self.rect.y + 5))
