"""Entry point for the cell simulation."""

from __future__ import annotations

import os
from config import DISABLE_SOUND

if DISABLE_SOUND:
    os.environ["SDL_AUDIODRIVER"] = "dummy"

from cell.simulation import Simulation


if __name__ == "__main__":
    sim = Simulation()
    sim.run()
