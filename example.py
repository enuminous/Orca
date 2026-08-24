from orca import ActorState, Handoff, OrcaEvaluator

actors = [
    ActorState("planner", 0.80, "executor", 5),
    ActorState("executor", 0.82, "executor", 5),
    ActorState("reviewer", 0.79, "executor", 4)
]

handoffs = [
    Handoff(
        sender="planner",
        receiver="executor",
        task_id="build-17",
        acknowledged=True,
        payload_complete=True,
        ownership_clear=True,
        dependency_complete=True
    )
]

print(OrcaEvaluator().evaluate(
    actors,
    handoffs,
    conflict_count=0,
    conflict_opportunities=3
))
