# ORCA — EFMW Zoo #34

**Operational Recursive Coordination Assessment**

ORCA is an experimental EFMW-inspired framework for evaluating coordination quality across multiple agents, humans, tools, and subsystems operating over shared or partially shared state.

## Core question

> Can multiple actors remain aligned on state, ownership, timing, dependencies, and goals while work is being passed among them?

ORCA focuses on operational coordination rather than isolated component capability.

## Primary outputs

- coordination coherence
- handoff integrity
- shared-state consistency
- conflict rate
- responsibility ambiguity
- synchronization lag
- recovery from coordination failure
- collective task completion

## Repository contents

- `theory.md`
- `architecture.md`
- `coordination_model.md`
- `limitations.md`
- `orca.py`
- `benchmark.py`
- `ablations.py`
- `test_orca.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_orca.py
```

## Zoo position

SALMON #33 traces present behavior back to its origins.

**ORCA #34 asks whether multiple actors can coordinate those states and histories into coherent joint action.**
