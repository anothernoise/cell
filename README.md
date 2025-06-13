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

## Logging

The rule engine in `dsl.rules` relies on Python's standard `logging` module.
If evaluating a rule condition raises an exception, the error is caught and a
warning is emitted with the failing condition text. The logger is obtained with
`logging.getLogger(__name__)` so it inherits the configuration of your
application.

You can enable basic logging output at program start-up, for example in
`src/main.py`:

```python
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s:%(name)s:%(message)s")
```
