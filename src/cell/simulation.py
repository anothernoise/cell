"""Simulation loop and environment management."""

from __future__ import annotations

import pygame

from .organelles import (
    Cell,
    Nucleus,
    Mitochondrion,
    Ribosome,
    EndoplasmicReticulum,
    GolgiApparatus,
)
from .physics import keep_inside_bounds


class Simulation:
    """Manages the cell and runs the time-stepped loop."""

    def __init__(self, width: int = 800, height: int = 600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Cell Simulation")
        self.clock = pygame.time.Clock()
        self.bounds = self.screen.get_rect()
        self.cell = self._create_cell()
        self.running = False

    def _create_cell(self) -> Cell:
        cell = Cell()
        center = pygame.math.Vector2(self.bounds.center)
        cell.add_organelle(Nucleus(center))
        import random
        for _ in range(3):
            offset = pygame.math.Vector2(
                self.bounds.width * 0.2 * (0.5 - random.random()),
                self.bounds.height * 0.2 * (0.5 - random.random()),
            )
            cell.add_organelle(Mitochondrion(center + offset))
        cell.add_organelle(Ribosome(center + pygame.math.Vector2(30, 0)))
        cell.add_organelle(EndoplasmicReticulum(center + pygame.math.Vector2(-30, 0)))
        cell.add_organelle(GolgiApparatus(center + pygame.math.Vector2(0, 30)))
        return cell

    def step(self, dt: float) -> None:
        for organelle in self.cell.organelles:
            keep_inside_bounds(organelle.pos, self.bounds)
        self.cell.step(dt)

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.cell.draw(self.screen)
        self._draw_ui()
        pygame.display.flip()

    def _draw_ui(self) -> None:
        font = pygame.font.SysFont(None, 24)
        text = font.render(
            f"ATP: {self.cell.atp:.1f} Proteins: {self.cell.proteins:.1f}",
            True,
            (255, 255, 255),
        )
        self.screen.blit(text, (10, 10))

    def run(self) -> None:
        self.running = True
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.step(dt)
            self.draw()

        pygame.quit()
