from benchmark import coherent_case, degraded_case
from orca import OrcaEvaluator

if __name__ == "__main__":
    ev = OrcaEvaluator()
    good = ev.evaluate(*coherent_case())
    bad = ev.evaluate(*degraded_case())

    print("full coherent:", good["coordination_score"])
    print("full degraded:", bad["coordination_score"])

    # Simple ablation: state consistency only.
    print("state-only coherent:", good["shared_state_consistency"])
    print("state-only degraded:", bad["shared_state_consistency"])
