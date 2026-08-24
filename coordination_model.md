# Coordination Model

## Actor schema

```json
{
  "id": "agent-A",
  "role": "planner",
  "local_version": 12,
  "known_owner": "agent-B"
}
```

## Task schema

```json
{
  "task_id": "T17",
  "owner": "agent-B",
  "status": "in_progress",
  "dependencies": ["T12"],
  "shared_version": 12
}
```

## Handoff schema

```json
{
  "id": "H8",
  "sender": "agent-A",
  "receiver": "agent-B",
  "task_id": "T17",
  "acknowledged": true,
  "payload_complete": true,
  "ownership_clear": true
}
```

## Shared-state disagreement

For scalar or encoded state variables:

`D_state = mean pairwise distance`

Consistency:

`S = 1 / (1 + D_state)`

## Handoff loss

A handoff can fail through:
- missing payload,
- missing acknowledgment,
- ambiguous owner,
- omitted dependency,
- stale state version.

## Conflict graph

Create a graph linking incompatible simultaneous actions.

High local conflict centrality can reveal coordination bottlenecks.
