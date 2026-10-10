# ORCA — EFMW Zoo #34

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Orca) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

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
