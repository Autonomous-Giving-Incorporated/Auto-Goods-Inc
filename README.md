# Auto Goods Inc

Auto Goods Inc is a specification-first foundation for a for-profit autonomous software company. It is intended to discover real digital market friction, validate opportunities with external evidence, build the smallest useful digital goods, sell them, reconcile verified costs, and distribute positive profit under an immutable 50/50 contract.

> **Status:** Phase 0, Constitution. This repository defines the operating contract, policies, schemas, and verification expectations. It does not claim demonstrated autonomy, revenue, profit, or impact.

## Venture loop

`MarketSignal -> MarketGap -> Opportunity -> ValidationExperiment -> VentureCandidate -> Venture -> Product -> Customer -> Transaction -> LedgerEvent -> DistributionPeriod -> ProfitDistribution -> CommunityAllocation -> ImpactReceipt -> learning`

A candidate proceeds only through explicit evidence and authority gates. Real external validation is required before promotion. A correctly killed venture is a successful outcome when evidence falsifies its thesis.

## The 50/50 contract

Only positive `DistributableProfit` is eligible. Accounting uses integer minor currency units. Exactly 50% goes to Auto Goods Inc and 50% to community wellness, with at most a deterministic one-minor-unit rounding difference. Agents, ventures, growth systems, product code, and runtime configuration cannot change the split. An invariant failure freezes treasury activity.

The community half supports only free food, housing, healthcare, education, and community space. In v0.1, these five categories share the community allocation equally.

## Evidence and autonomy

Material claims are `OBSERVED`, `INFERRED`, `SPECULATIVE`, or `NOT_COMPUTABLE`. Observations require provenance. Inferences identify observed inputs. Speculation cannot independently authorize spending or promotion. Missing facts remain unresolved.

Autonomy is bounded by authority grants, budgets, lifecycle gates, least privilege, and separation of duties. Agents cannot self-escalate, change their own budgets, modify treasury invariants, or verify their own allocations.

## Architecture and roadmap

Intelligence, Validation, Production, Commercial, Executive, Finance, Community, and Governance capabilities are separated. Accounting and routing are deterministic. Initial production launches and payouts require human approval. See [ARCHITECTURE.md](ARCHITECTURE.md).

The roadmap moves from constitution through market intelligence, validation, a goods foundry, bounded growth, a closed economic loop, and a verified community loop. The first system milestone is [`AUTO_GOODS_LOOP_001`](docs/MVP.md). See [ROADMAP.md](ROADMAP.md).

## Documentation

- [Canonical context](CONTEXT.md)
- [Product contract](docs/PRODUCT-CONTRACT.md)
- [Domain model](docs/DOMAIN-MODEL.md)
- [Autonomy](docs/AUTONOMY.md)
- [Venture lifecycle](docs/VENTURE-LIFECYCLE.md)
- [Market intelligence](docs/MARKET-INTELLIGENCE.md)
- [Venture scoring](docs/VENTURE-SCORING.md)
- [Portfolio](docs/PORTFOLIO.md)
- [Treasury](docs/TREASURY.md)
- [Community impact](docs/COMMUNITY-IMPACT.md)
- [Policy and schema migration](docs/POLICY-MIGRATIONS.md)
- [Deployment runbook](docs/DEPLOYMENT-RUNBOOK.md)
- [Key lifecycle](docs/KEY-LIFECYCLE.md)
- [Governance](GOVERNANCE.md)
- [Security](SECURITY.md)

## Local validation

Install the validation-only dependencies and run the same public commands used by continuous integration:

```sh
python -m pip install --requirement requirements-dev.txt
python tools/validate.py --include-valid-fixtures
python -m unittest discover -s tests -v
```

JSON Schema syntax also has a standard-library fallback check: `python -S tools/validate.py schemas/*.json`. YAML policy validation intentionally fails closed when PyYAML is unavailable.
