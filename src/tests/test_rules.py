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
    engine.add_rule("1 / 0", lambda state: None)

    with caplog.at_level(logging.WARNING):
        engine.evaluate()

    # There should be exactly one warning log about the failed rule evaluation
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.levelname == "WARNING"
    assert "1 / 0" in record.getMessage()
    assert "division by zero" in record.getMessage()
