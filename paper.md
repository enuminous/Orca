# ORCA: Operational Recursive Coordination Assessment

## Abstract

ORCA is an experimental framework for evaluating coordination across distributed actors, including software agents, humans, tools, and services. It measures shared-state consistency, handoff integrity, conflict, ownership ambiguity, and synchronization lag while preserving coordination history over time.

## 1. Motivation

Individual competence does not guarantee collective competence.

Distributed work can fail through:
- stale state,
- poor handoffs,
- role ambiguity,
- duplicated action,
- contradiction,
- delayed synchronization.

## 2. Model

Actors maintain local estimates of shared state:

`g_i(t)`

Shared-state consistency:

`S = 1/(1 + mean pairwise distance)`

Handoff integrity:

`H = successful handoff checks / total required checks`

Conflict rate:

`C = conflicts / conflict opportunities`

Ownership ambiguity:

`A = 1 - dominant ownership agreement`

Composite coordination score:

`O = w1*S + w2*H + w3*(1-C) + w4*(1-A) - w5*Lag`

## 3. Metrics

- shared-state consistency
- handoff integrity
- synchronization lag
- ownership ambiguity
- conflict rate
- collective completion
- recovery after coordination breakdown

## 4. Baselines

- workflow completion metrics
- distributed tracing
- project/task telemetry
- communication latency
- multi-agent success rate
- centralized orchestration baselines

## 5. Ablations

- remove handoff integrity
- remove shared-state consistency
- remove ownership analysis
- remove version lag
- remove conflict tracking
- remove longitudinal recursion

## 6. Falsification

If conventional workflow telemetry predicts collective failures equally well under equivalent information access, ORCA's additional structure is not justified.

## 7. Claim boundary

ORCA evaluates observable coordination structure. It does not infer intent, loyalty, trust, or consciousness.
