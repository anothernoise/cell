"""Entry point for the cell simulation."""

from __future__ import annotations

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import os
from config import DISABLE_SOUND

if DISABLE_SOUND:
    os.environ["SDL_AUDIODRIVER"] = "dummy"

from cell.simulation import Simulation
import logging

# Example logging configuration. The rule engine in ``dsl.rules`` uses a logger
# named after its module, so configuring logging here controls its output.
logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s:%(name)s:%(message)s")


if __name__ == "__main__":
    sim = Simulation()
    sim.run()
