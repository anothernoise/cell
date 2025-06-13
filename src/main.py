"""Entry point for the cell simulation."""

from __future__ import annotations

from cell.simulation import Simulation


if __name__ == "__main__":
    sim = Simulation()
    sim.run()
