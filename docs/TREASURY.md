# Treasury

Accounting Engine, Treasury Controller, and Profit Router are deterministic software. LLM output cannot create ledger truth, calculate authoritative balances, waive reconciliation, or authorize payout. Money uses integer minor currency units and explicit currency; floating-point accounting is prohibited.

```text
NetProductRevenue = Revenue - Refunds - Chargebacks - ProcessingFees
OperatingContribution = NetProductRevenue - DirectProductCosts - Infrastructure - Support - ApprovedAcquisitionSpend
DistributableProfit = OperatingContribution - TaxReserve - RequiredOperatingReserve
```

Only a closed reconciled `DistributionPeriod` with positive `DistributableProfit` is eligible.

```text
OrganizationAllocation = deterministic_half_policy(DistributableProfit)
CommunityAllocation = DistributableProfit - OrganizationAllocation
OrganizationAllocation + CommunityAllocation == DistributableProfit
abs(OrganizationAllocation - CommunityAllocation) <= 1 minor unit
```

The versioned policy states who receives an odd-unit remainder. Historical records retain their policy version. The community share is subsequently divided among food, housing, healthcare, education, and community space.

Set `TREASURY_STATE = FROZEN` and prohibit payout for incomplete reconciliation, non-integer money, currency conflict, formula/split failure, missing ledger provenance, absent approval, invalid recipient verification, uncertain write integrity, or incident freeze. Unfreezing requires independent authority, remediation, passing checks, and an auditable decision. Never edit ledger facts to force a pass; use compensating `LedgerEvent` records.

The split and formulas are not runtime preferences. Change requires human governance, policy/schema versioning, migration and rollback review, tests, and audit trail.
