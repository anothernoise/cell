"""Collection of simple example rules for the RuleEngine."""

from __future__ import annotations

from typing import Dict

from .rules import RuleEngine


def add_basic_rules(engine: RuleEngine) -> None:
    """Register a basic example rule on the given engine."""

    def restore_health(state: Dict[str, float]) -> None:
        state["health"] = state.get("health", 0.0) + 1.0

    engine.add_rule("maintenance", "health < 50", restore_health)

