import sys
import pathlib

import pytest

# Ensure src directory is on path
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from cell.simulation import Simulation


def test_create_simulation():
    sim = Simulation(width=200, height=200)
    assert sim.cell is not None
    assert len(sim.cell.organelles) > 0
