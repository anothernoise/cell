"""Simple DSL for rule-based organelle behavior."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List


@dataclass
class Rule:
    """Represents a condition-action rule."""

    condition: str
    action: Callable[[Dict[str, float]], None]


class RuleEngine:
    """Evaluates rules based on the simulation state."""

    def __init__(self):
        self.rules: List[Rule] = []
        self.state: Dict[str, float] = {}

    def add_rule(self, condition: str, action: Callable[[Dict[str, float]], None]) -> None:
        self.rules.append(Rule(condition, action))

    def update_state(self, **kwargs: float) -> None:
        self.state.update(kwargs)

    def evaluate(self) -> None:
        for rule in self.rules:
            try:
                if eval(rule.condition, {}, self.state):
                    rule.action(self.state)
            except Exception:
                continue
