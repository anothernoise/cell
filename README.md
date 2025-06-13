# Cell Simulation Game

This project is a modular simulation of a simplified human cell using **Python** and **pygame**. Each organelle is implemented as a separate class and the simulation runs in a time-stepped loop with basic 2D motion physics.

## Features
- Organelles: Nucleus, Mitochondria, Ribosomes, Endoplasmic Reticulum, Golgi Apparatus
- Simple DSL-driven rule-based behavior via `dsl.rules`
- Placeholder autonomous mode for future ML integration
- Basic UI showing ATP and protein levels

## Running
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Start the simulation:
    ```bash
    python src/main.py
    ```

## Project Structure
```
src/
  cell/          # Simulation core and organelle logic
  dsl/           # Rule-based behavior definitions
  ml/            # Placeholders for ML-based autonomous mode
  ui/            # UI helpers
  main.py        # Entry point
```
