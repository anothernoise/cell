import sys
import pathlib
import logging

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from dsl.rules import RuleEngine


def test_rule_condition_exception_logs_warning(caplog):
    engine = RuleEngine()
    # Add a rule with a condition that will raise an exception (division by zero)
    engine.add_rule("test", "1 / 0", lambda state: None)

    with caplog.at_level(logging.WARNING):
        engine.fire("test")

    # There should be exactly one warning log about the failed rule evaluation
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.levelname == "WARNING"
    assert "1 / 0" in record.getMessage()
    assert "division by zero" in record.getMessage()


def test_basic_rule_increases_health():
    engine = RuleEngine()
    from dsl.simple_rules import add_basic_rules

    engine.update_state(health=40)
    add_basic_rules(engine)
    engine.fire("maintenance")

    assert engine.state["health"] == 41.0


def test_organelle_rule_chain():
    engine = RuleEngine()
    from dsl.organelle_rules import add_organelle_rules

    engine.update_state(atp=10, nucleus_active=True)
    add_organelle_rules(engine)
    engine.fire("metabolism")
    engine.fire("protein_synthesis")

    assert engine.state["proteins_packaged"] == 1.0
    engine.evaluate()

    assert engine.state["health"] == 41.0
