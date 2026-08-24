# ORCA Architecture

## Pipeline

1. Actor Registry
2. Shared-State Collector
3. Task/Ownership Ledger
4. Handoff Monitor
5. State Consistency Engine
6. Conflict Detector
7. Synchronization-Lag Tracker
8. Coordination Recovery Analyzer
9. Audit Reporter

## Inputs

- actor states
- shared task states
- ownership assignments
- handoff records
- dependency graphs
- action logs
- timestamps

## Outputs

```json
{
  "shared_state_consistency": 0.91,
  "handoff_integrity": 0.88,
  "conflict_rate": 0.06,
  "ownership_ambiguity": 0.11,
  "sync_lag": 2.4,
  "coordination_score": 0.84
}
```

## Design principle

ORCA separates:
- individual competence
from
- collective coordination.

A team of strong actors can still fail as a system.

## Integration

ELEPHANT can preserve long coordination histories.

SALMON can trace a coordination failure back to its originating handoff.

MAGPIE can audit whether actors share the same evidence base.

WOLF can detect emerging distributed coordination degradation.
