"""Rule helpers modeling interactions between organelles."""

from __future__ import annotations

from typing import Dict

from .rules import RuleEngine


def add_organelle_rules(engine: RuleEngine) -> None:
    """Register a simple chain of organelle interaction rules."""

    def mitochondria_produce_atp(state: Dict[str, float]) -> None:
        state["atp"] = state.get("atp", 0.0) + 10.0 * state.get("mitochondria_activity", 1.0)

    engine.add_rule("atp < 20", mitochondria_produce_atp)

    def ribosomes_produce_proteins(state: Dict[str, float]) -> None:
        state["atp"] -= 1.0
        state["proteins_raw"] = state.get("proteins_raw", 0.0) + 1.0

    engine.add_rule("nucleus_active and atp >= 1", ribosomes_produce_proteins)

    def er_fold_proteins(state: Dict[str, float]) -> None:
        state["proteins_raw"] -= 1.0
        state["proteins_folded"] = state.get("proteins_folded", 0.0) + 1.0

    engine.add_rule("proteins_raw > 0", er_fold_proteins)

    def golgi_package_proteins(state: Dict[str, float]) -> None:
        state["proteins_folded"] -= 1.0
        state["proteins_packaged"] = state.get("proteins_packaged", 0.0) + 1.0

    engine.add_rule("proteins_folded > 0", golgi_package_proteins)
