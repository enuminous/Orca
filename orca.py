from dataclasses import dataclass
from typing import Dict, List, Optional
from statistics import mean

@dataclass
class ActorState:
    actor_id: str
    shared_value: float
    task_owner_view: Optional[str] = None
    state_version: int = 0

@dataclass
class Handoff:
    sender: str
    receiver: str
    task_id: str
    acknowledged: bool
    payload_complete: bool
    ownership_clear: bool
    dependency_complete: bool = True

class OrcaEvaluator:
    def state_consistency(self, actors: List[ActorState]) -> float:
        if len(actors) <= 1:
            return 1.0
        vals = [a.shared_value for a in actors]
        diffs = []
        for i in range(len(vals)):
            for j in range(i+1, len(vals)):
                diffs.append(abs(vals[i]-vals[j]))
        d = mean(diffs) if diffs else 0.0
        return 1.0/(1.0+d)

    def handoff_integrity(self, handoffs: List[Handoff]) -> float:
        if not handoffs:
            return 1.0
        scores = []
        for h in handoffs:
            checks = [
                h.acknowledged,
                h.payload_complete,
                h.ownership_clear,
                h.dependency_complete
            ]
            scores.append(sum(bool(x) for x in checks)/len(checks))
        return mean(scores)

    def ownership_ambiguity(self, actors: List[ActorState]) -> float:
        views = [a.task_owner_view for a in actors if a.task_owner_view is not None]
        if not views:
            return 0.0
        counts = {}
        for v in views:
            counts[v] = counts.get(v,0)+1
        max_agree = max(counts.values())
        return 1.0 - max_agree/len(views)

    def version_lag(self, actors: List[ActorState]) -> float:
        if not actors:
            return 0.0
        versions = [a.state_version for a in actors]
        return max(versions)-min(versions)

    def evaluate(self, actors: List[ActorState], handoffs: List[Handoff], conflict_count=0, conflict_opportunities=1):
        s = self.state_consistency(actors)
        h = self.handoff_integrity(handoffs)
        a = self.ownership_ambiguity(actors)
        lag = self.version_lag(actors)
        c = conflict_count/max(1, conflict_opportunities)
        lag_norm = min(1.0, lag/10.0)

        score = (
            0.30*s +
            0.30*h +
            0.20*(1.0-c) +
            0.10*(1.0-a) +
            0.10*(1.0-lag_norm)
        )

        return {
            "shared_state_consistency": s,
            "handoff_integrity": h,
            "conflict_rate": c,
            "ownership_ambiguity": a,
            "version_lag": lag,
            "coordination_score": score
        }
