# Governance

Governance protects mission, evidence integrity, users, customers, recipients, and the 50/50 invariant. Authority is deny-by-default.

## Authority classes
`AUTO_ALLOWED` permits bounded reversible action. `POLICY_ALLOWED` requires matching versioned policy and active `AuthorityGrant`. `USER_CONFIRMATION_REQUIRED` requires a designated accountable user. `QUALIFIED_HUMAN_REQUIRED` requires appropriate expertise. `PROHIBITED` grants no agent authority.

No agent may self-escalate, issue its own grant, change its own budget ceiling, reinterpret denial as approval, or split actions to evade limits.

## Separation of duties
Hypothesis creation and grading are separate. Validation operation and promotion approval are attributable separately. Allocator cannot verify its own impact. A venture cannot control treasury. Marketing cannot control accounting. Portfolio cannot change financial invariants. Recipients cannot score or verify themselves. Code authors cannot unilaterally approve high-consequence production or finance changes.

## Financial invariants and freeze
Positive `DistributableProfit` is split 50/50 within deterministic one-minor-unit tolerance, using integer minor units. The split is immutable through ordinary configuration. Treasury enters `FROZEN` when reconciliation is incomplete, an invariant fails, ledger integrity is uncertain, approval is absent, recipient verification expires, or an incident freeze is invoked. No payout proceeds while frozen.

Changing the split, accounting formula, eligible domains, or freeze semantics requires explicit human governance, versioned policy, security/migration/user/key-lifecycle review, tests, and immutable audit trail. Agents cannot authorize it.

## Change control
1. Record the proposal and affected contracts.
2. Map security, migration, user, key, financial, and community impact.
3. Identify human authority and independent reviewers.
4. Version policies and schemas without reinterpreting history.
5. Validate denied paths, rounding, freeze, migration, and rollback.
6. Record approval as `PolicyDecision` and execution as `RunReceipt`.
7. Monitor and retain freeze or rollback capability.

Policy precedence is constitution and human governance, company policy, venture policy, then task grants. Lower levels cannot widen higher authority. Consequential actions record actor, class, grant, policy version, evidence, timestamp, result, and denial reason. Financial and impact corrections use compensating entries.

Initial production launch, treasury payout, community payout, recipient approval, accounting changes, and constitutional changes require designated human authority. Qualified review applies to legal, tax, accounting, security, healthcare, and regulated matters.
