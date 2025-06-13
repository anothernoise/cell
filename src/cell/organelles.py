"""Organelle definitions for the cell simulation."""

from __future__ import annotations

import pygame
import random
from src.logger_config import logger


class Organelle:
    """Base class for cell organelles."""

    def __init__(self, name: str, pos: pygame.math.Vector2):
        self.name = name
        self.pos = pos
        self.velocity = pygame.math.Vector2(0, 0)
        self.size = 10

    def step(self, dt: float, cell: "Cell") -> None:
        """Perform a simulation step."""
        self.pos += self.velocity * dt

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, (200, 200, 200), self.pos, self.size)


class Nucleus(Organelle):
    def __init__(self, pos: pygame.math.Vector2):
        super().__init__("nucleus", pos)
        self.size = 20

    def step(self, dt: float, cell: "Cell") -> None:
        super().step(dt, cell)
        # Example: manage genetic instructions

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, (150, 0, 200), self.pos, self.size)


class Mitochondrion(Organelle):
    def __init__(self, pos: pygame.math.Vector2):
        super().__init__("mitochondrion", pos)
        self.activity = 1.0

    def step(self, dt: float, cell: "Cell") -> None:
        super().step(dt, cell)
        # Generate ATP based on activity
        cell.atp += 0.1 * self.activity
        # Random walk movement
        self.velocity += pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.velocity *= 0.5

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, (255, 100, 100), self.pos, self.size)


class Ribosome(Organelle):
    def __init__(self, pos: pygame.math.Vector2):
        super().__init__("ribosome", pos)
        self.size = 5

    def step(self, dt: float, cell: "Cell") -> None:
        super().step(dt, cell)
        # Simple placeholder for protein synthesis
        if cell.atp > 10:
            cell.proteins += 0.05
            cell.atp -= 0.05

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, (100, 255, 100), self.pos, self.size)


class EndoplasmicReticulum(Organelle):
    def __init__(self, pos: pygame.math.Vector2):
        super().__init__("ER", pos)
        self.size = 15

    def step(self, dt: float, cell: "Cell") -> None:
        super().step(dt, cell)
        # Assist in protein folding

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, (100, 100, 255), self.pos, self.size)


class GolgiApparatus(Organelle):
    def __init__(self, pos: pygame.math.Vector2):
        super().__init__("Golgi", pos)
        self.size = 12

    def step(self, dt: float, cell: "Cell") -> None:
        super().step(dt, cell)
        # Package proteins

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, (255, 255, 100), self.pos, self.size)


class Cell:
    """A simple representation of a cell holding organelles."""

    def __init__(self):
        self.organelles = []
        self.atp = 50.0
        self.health = 100.0
        self.proteins = 0.0
        logger.info(f"Cell initialized with ATP: {self.atp}")

    def add_organelle(self, organelle: Organelle) -> None:
        self.organelles.append(organelle)
        logger.debug(f"Added organelle: {organelle.name} at position {organelle.pos}")

    def step(self, dt: float) -> None:
        for organelle in self.organelles:
            organelle.step(dt, self)
        self.atp = max(0.0, min(self.atp, 100.0))

    def draw(self, surface: pygame.Surface) -> None:
        logger.debug(f"Drawing {len(self.organelles)} organelles")
        for organelle in self.organelles:
            logger.debug(f"Drawing {organelle.name} at {organelle.pos}")
            organelle.draw(surface)
