# ORCA Theory

## 1. Problem

Distributed systems often fail even when each participant is individually competent.

Failure modes include:
- duplicate work,
- dropped work,
- stale shared state,
- unclear ownership,
- contradictory actions,
- handoff loss,
- delayed synchronization,
- tool/human mismatch,
- unresolved conflict.

ORCA evaluates the relational structure of coordination.

## 2. Actor model

Let actors be:

`A = {a_1, ..., a_n}`

Actors may be:
- software agents,
- humans,
- services,
- tools,
- organizational roles.

Each actor has local state:

`s_i(t)`

and an estimate of shared state:

`g_i(t)`.

## 3. Shared-state consistency

For a canonical reference state `g*(t)`:

`S_t = 1 - mean_i dist(g_i(t), g*(t))`

Higher `S_t` means stronger shared-state agreement.

When no ground truth exists, pairwise consistency can be used.

## 4. Handoff integrity

A handoff is:

`h = (sender, receiver, payload, ownership, deadline, dependencies)`

A handoff succeeds when:
- payload arrives,
- receiver acknowledges,
- ownership transfers unambiguously,
- dependencies are preserved,
- no required information is lost.

`H = successful_handoffs / total_handoffs`

## 5. Responsibility ambiguity

For task `k`, let `r_ik` be actor `i`'s ownership probability or assignment weight.

High ambiguity occurs when ownership is diffuse or conflicting.

A simple concentration measure:

`R_k = max_i r_ik`

Low `R_k` indicates unclear ownership.

## 6. Coordination conflict

Conflict occurs when two actors issue incompatible actions against the same state or resource.

`C_t = conflicts_t / opportunities_for_conflict_t`

## 7. Synchronization lag

For shared update `u` created at time `t0`, define:

`L_sync(u) = max_i(t_i_received - t0)`

or a robust percentile.

## 8. Recursive coordination

Coordination is history-dependent.

A failed handoff can propagate:
- stale assumptions,
- duplicated work,
- later conflicts.

ORCA therefore tracks state recursively across handoff chains.

## 9. Composite score

A candidate operational score:

`O_t = w1*S_t + w2*H_t + w3*(1-C_t) + w4*(1-Ambiguity_t) - w5*Lag_t`

after normalization.

## 10. EFMW interpretation

The EFMW-inspired element is recursive relational tracking across actors and time.

The unit of analysis is not one agent.

It is the **coordination field among agents**.

## 11. Falsifiable prediction

ORCA should add value when:
- work is distributed,
- state is partially shared,
- handoffs are frequent,
- actor roles overlap,
- coordination errors compound over time.

If conventional workflow telemetry captures the same failures, ORCA's extra structure is unnecessary.
