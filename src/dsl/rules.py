"""Simple DSL for rule-based organelle behavior.

Errors raised while evaluating rule conditions are logged with the
failing condition string and the exception message, then evaluation
continues with the next rule.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List
import logging


logger = logging.getLogger(__name__)


@dataclass
class Rule:
    """Represents a triggered condition-action rule."""

    trigger: str
    condition: str
    action: Callable[[Dict[str, float]], None]


class RuleEngine:
    """Evaluates rules based on the simulation state."""

    def __init__(self):
        self.rules: List[Rule] = []
        self.state: Dict[str, float] = {}

    def add_rule(
        self, trigger: str, condition: str, action: Callable[[Dict[str, float]], None]
    ) -> None:
        """Register a rule tied to a trigger."""
        self.rules.append(Rule(trigger, condition, action))

    def update_state(self, **kwargs: float) -> None:
        self.state.update(kwargs)

    def fire(self, trigger: str) -> None:
        """Run all rules for the given trigger."""
        for rule in self.rules:
            if rule.trigger != trigger:
                continue
            try:
                if eval(rule.condition, {}, self.state):
                    rule.action(self.state)
            except Exception as exc:
                logger.warning(
                    "Error evaluating rule '%s': %s", rule.condition, exc
                )
                continue

    def evaluate(self) -> None:
        """Run all rules regardless of trigger."""
        for rule in self.rules:
            try:
                if eval(rule.condition, {}, self.state):
                    rule.action(self.state)
            except Exception as exc:
                logger.warning(
                    "Error evaluating rule '%s': %s", rule.condition, exc
                )
                continue

    def step(self, triggers: List[str]) -> None:
        """Evaluate rules for a sequence of triggers."""
        for trigger in triggers:
            self.fire(trigger)
