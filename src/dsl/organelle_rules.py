"""Rule helpers modeling interactions between organelles."""

from __future__ import annotations

from typing import Dict

from .rules import RuleEngine


def add_organelle_rules(engine: RuleEngine) -> None:
    """Register a simple chain of organelle interaction rules."""

    def mitochondria_produce_atp(state: Dict[str, float]) -> None:
        state["atp"] = state.get("atp", 0.0) + 10.0 * state.get("mitochondria_activity", 1.0)

    engine.add_rule("metabolism", "atp < 20", mitochondria_produce_atp)

    def ribosomes_produce_proteins(state: Dict[str, float]) -> None:
        state["atp"] -= 1.0
        state["proteins_raw"] = state.get("proteins_raw", 0.0) + 1.0

    engine.add_rule("protein_synthesis", "nucleus_active and atp >= 1", ribosomes_produce_proteins)

    def er_fold_proteins(state: Dict[str, float]) -> None:
        state["proteins_raw"] -= 1.0
        state["proteins_folded"] = state.get("proteins_folded", 0.0) + 1.0

    engine.add_rule("protein_synthesis", "proteins_raw > 0", er_fold_proteins)

    def golgi_package_proteins(state: Dict[str, float]) -> None:
        state["proteins_folded"] -= 1.0
        state["proteins_packaged"] = state.get("proteins_packaged", 0.0) + 1.0

    engine.add_rule("protein_synthesis", "proteins_folded > 0", golgi_package_proteins)

    def membrane_remove_waste(state: Dict[str, float]) -> None:
        state["waste"] -= 1.0

    engine.add_rule("cleanup", "waste > 0", membrane_remove_waste)

    def nucleus_trigger_division(state: Dict[str, float]) -> None:
        state["divisions"] = state.get("divisions", 0.0) + 1.0
        state["atp"] -= 50.0

    engine.add_rule(
        "division",
        "atp >= 100 and proteins_packaged >= 20",
        nucleus_trigger_division,
    )
