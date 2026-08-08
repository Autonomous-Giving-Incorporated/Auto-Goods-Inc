# Policy and Schema Migration

Policies and schemas are append-only versioned contracts. A new version must not reinterpret a historical `LedgerEvent`, `DistributionPeriod`, `ProfitDistribution`, `CommunityAllocation`, `ImpactReceipt`, `PolicyDecision`, or `RunReceipt`.

## Change map

Every migration records the source and target versions, affected records and components, authority change, security impact, user and community impact, key impact, financial impact, compatibility window, backfill plan, rollback or forward-fix plan, and evidence required for acceptance.

## Procedure

1. Freeze affected consequential writes when mixed-version behavior could violate authority, accounting, privacy, or recipient eligibility.
2. Add the new schema or policy version without mutating historical artifacts.
3. Validate old records under their recorded version and new records under the target version.
4. Run read-only migration analysis. Unknown or irrecoverable mappings remain `NOT_COMPUTABLE`.
5. Require qualified human governance for accounting formulas, the 50/50 split, eligible community domains, treasury freeze semantics, or authority boundaries.
6. Backfill only derivable fields with provenance. Never invent commercial, financial, customer, or impact data.
7. Deploy with a compatibility window and explicit observability.
8. Record approval in `PolicyDecision` and execution, counts, failures, and checks in `RunReceipt`.

Treasury remains `FROZEN` whenever a migration leaves financial invariants, reconciliation, or version attribution uncertain. Financial corrections use compensating `LedgerEvent` records rather than destructive history edits.
