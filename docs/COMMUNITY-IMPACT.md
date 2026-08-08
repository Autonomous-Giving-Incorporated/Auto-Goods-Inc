# Community Impact

Half of positive `DistributableProfit` supports only services free to recipients in five domains: food, housing, healthcare, education, and community space. In v0.1, each receives 20% of the community allocation, equivalent to 10% of total distributable profit before minor-unit remainder handling. AI-determined weighting is prohibited in v0.1.

A `CommunityOrganization` records identifier, legal name, location, eligible domains, identity verification, legal status, bank verification, operating history, reporting state, programs, population, service, geography, capacity, evidence, source documents, and impact reports. Distribution requires current verification and an eligible `CommunityProgram`.

Organizations cannot self-score or verify eligibility, capacity, allocation, or impact. Impact Allocator and Impact Verifier are separate authorities.

A `CommunityAllocation` links source `ProfitDistribution`, domain, verified organization/program, integer amount, decision, approval, and expected output. An `ImpactReceipt` links allocation, source `DistributionPeriod`, source ventures, recipient, program, amount, domain, funded activity, expected and actual output, evidence, and verification state. Unknown output remains `NOT_COMPUTABLE`; failed or partial results remain visible.

Public aggregated lineage is `Product -> revenue cohort -> DistributionPeriod -> CommunityAllocation -> CommunityOrganization -> CommunityProgram -> ImpactReceipt`. Never publish private transactions, personal/bank data, or sensitive source documents.

Future evidence-driven weighting may consider demonstrated need, service gap, population, capacity, marginal dollar utility, evidence quality, and historical impact only after human governance, independent verification, versioning, fairness/gaming analysis, and migration rules. Commercial scoring remains separate.
