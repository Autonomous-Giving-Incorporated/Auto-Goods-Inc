# Security

## Status and reporting
This repository specifies future controls and does not claim a production security program is implemented. Do not disclose sensitive vulnerabilities publicly. Until a private channel is published, ask repository owners through GitHub for a secure reporting channel without including sensitive details.

## Principles
Use least privilege, deny by default, capability isolation, short-lived credentials where supported, explicit spend ceilings, tool allowlists, verified provenance, and fail-closed financial behavior. Separate public transparency from customer, recipient, banking, and operational secrets.

## Required controls
- Never commit Stripe, deployment, email, model, signing, or authentication secrets. Use approved secret stores, scope, rotate, and revoke keys.
- Isolate agent tools, datasets, environments, credentials, and budgets. Prevent self-escalation.
- Enforce spend limits outside prompts and allowlist external hosts, methods, repositories, and deployment targets.
- Treat research content as untrusted data, not instructions. Sanitize, preserve source provenance, and mitigate prompt injection.
- Verify webhook signatures, timestamps, replay windows, event identity, and idempotency before ledger mutation.
- Pin and review supply-chain dependencies and actions, provenance, licenses, and updates.
- Keep tamper-evident audit logs separated from acting capabilities.
- Isolate treasury writes, reconcile before distribution, require approval, and freeze on integrity failure.
- Verify recipient identity, legal status, bank control, eligibility, capacity, reporting, and independent impact evidence.

All controls above are specified; implementation is pending unless verified elsewhere.

## Key lifecycle and data
Inventory owner, purpose, environment, scope, creation, rotation, storage, consumers, and revocation for each key. Never share production keys with non-production. Preserve historical signature verification. Public reporting may contain aggregate cohorts, totals, verified recipients/programs, and outcomes, but excludes private transactions, personal or bank data, credentials, raw payment payloads, and sensitive due diligence.

## Incident freeze
Credential compromise, unauthorized spend, ledger inconsistency, webhook forgery, recipient fraud, audit tampering, or treasury invariant failure may freeze affected writes and payouts. Preserve evidence, revoke keys, identify blast radius, reconcile, obtain human approval, and document recovery before unfreezing.

Before real money or personal data, verify secret management, isolation, authorization, webhooks, idempotency, logs, backup/recovery, dependencies, monitoring, incident response, treasury write protection, recipient verification, and qualified legal/accounting review. Missing evidence is `NOT_COMPUTABLE`.
