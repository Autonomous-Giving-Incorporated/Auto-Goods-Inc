# Venture Lifecycle

`SIGNAL -> DISCOVERED -> EVIDENCED -> VALIDATION_READY -> VALIDATING -> APPROVED -> BUILDING -> QA -> LAUNCH_READY -> LIVE -> REVENUE_GENERATING -> OPTIMIZING -> SCALE | HOLD | RETIRE`

No state is skipped. Each transition records a `PolicyDecision`, evidence, authority, and `RunReceipt`.

| Transition | Minimum gate |
|---|---|
| `SIGNAL -> DISCOVERED` | Three independent signals, concrete affected user, repeated problem |
| `DISCOVERED -> EVIDENCED` | Provenance, independence, labels, and contradictions reviewed |
| `EVIDENCED -> VALIDATION_READY` | Buyer, alternative, distribution, threshold, failure conditions, proof cost, basic economics |
| `VALIDATION_READY -> VALIDATING` | Bounded approved experiment, budget, independent judge, stop rules, data protection |
| `VALIDATING -> APPROVED` | Threshold met with real external validation and independent judgment |
| `APPROVED -> BUILDING` | Scope, owner, budget, security, acceptance tests, rollback |
| `BUILDING -> QA` | Smallest useful product complete and traceable to scope |
| `QA -> LAUNCH_READY` | Functional, security, privacy, payment, analytics, policy, rollback checks pass |
| `LAUNCH_READY -> LIVE` | Human confirmation, secrets, monitoring, rollback ready |
| `LIVE -> REVENUE_GENERATING` | Real settled payment and reconciled `LedgerEvent` evidence |
| `REVENUE_GENERATING -> OPTIMIZING` | Repeatable measurement and approved experiment bounds |
| `OPTIMIZING -> SCALE` | Evidence supports growth within capital, support, concentration, regulatory limits |
| `* -> HOLD` | Resolvable evidence, capacity, policy, or incident block |
| `* -> RETIRE` | Kill condition or approved responsible closure |

Validation outputs `PROMOTE`, `HOLD`, or `KILL`. Kill when budget is exhausted without threshold, buyer is falsified, acquisition or support breaks economics, legal/platform constraint invalidates the model, a substitute removes differentiation, or confidence collapses. Killed records stay auditable and require materially new evidence to reconsider.
