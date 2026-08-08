# Deployment Runbook

This is a deployment plan, not evidence that deployment controls are implemented.

## Preconditions

1. A versioned `PolicyDecision` authorizes the release and an active `AuthorityGrant` covers every automated action.
2. Staging build, schema and policy validation, tests, security review, privacy review, dependency review, observability, backup, and rollback evidence are attached to a `RunReceipt`.
3. Production credentials are isolated from staging, least-privileged, inventoried, and revocable.
4. Payment webhooks have signature, replay, identity, and idempotency checks before any `LedgerEvent` write.
5. Treasury and community payout paths remain disabled unless separately approved.

## Initial launch

Initial production launch is `USER_CONFIRMATION_REQUIRED`. Record approver, release identifier, policy versions, commit, deployment target, checks, timestamp, and rollback point. Deploy the smallest reversible change. Run smoke checks through the public Product path without using real customer data in logs.

## Abort and rollback

Abort on authorization mismatch, failed health check, unexpected data migration, key exposure, payment reconciliation error, privacy leak, or treasury invariant failure. Disable affected writes, preserve evidence, revoke exposed keys, restore the last verified release, and issue compensating `LedgerEvent` records rather than rewriting history. Treasury enters `FROZEN` for any financial-integrity uncertainty.

## Post-deployment

Confirm monitoring, webhook processing, ledger reconciliation, support routing, spend ceilings, and public/private data boundaries. Record outcomes and unresolved checks as `NOT_COMPUTABLE`. Production launch does not establish autonomy or profitability.
