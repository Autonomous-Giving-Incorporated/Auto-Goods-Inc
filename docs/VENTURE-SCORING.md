# Venture Scoring

Scores prioritize validation. They do not predict success or replace external evidence.

## Normalization
Each primitive input is a deterministic integer 0 to 100 under a versioned rubric. Zero means evidence supports absence or severe weakness. Missing evidence is `NOT_COMPUTABLE`, never zero, and blocks formula evaluation. Retain precision until final display rounding.

- `MP = Frequency * Severity * Persistence * ExistingWorkaroundCost`
- `BR = BuyerIdentifiability * SpendingAuthority * ExistingSpend * PurchaseUrgency`
- `DA = BuyerReachability * ChannelIntent * ChannelControl / EstimatedAcquisitionFriction`
- `AF = BuildAutomation * DeploymentAutomation * SupportAutomation * SalesAutomation * MeasurementAutomation`
- `EQ = ExpectedGrossMargin * RevenueRecurrence * ExpansionPotential / SupportBurden`
- `EQS = SourceDiversity * SourceReliability * SignalRecency * BehavioralEvidence`
- `AGVS = (MP * BR * DA * AF * EQ * EQS) / (BuildComplexity * CompetitivePressure * RegulatoryExposure * CapitalRequirement)`

Denominators must be positive. Unknown or zero denominators block rather than produce infinity. Implementations scale terms consistently, avoid overflow, and retain raw inputs, evidence, rubric/policy/code versions, and blocked terms.

**Proof Cost** is money, time, and irreversible commitment needed to determine reality. **Need-to-Good Latency** runs from first reliable signal to usable product in customer hands. `CRT = TotalLaunchCost / ExpectedMonthlyContributionMargin`. Projections remain `INFERRED` or `SPECULATIVE` until transactions support them. Predictive validity is not claimed before empirical calibration.
