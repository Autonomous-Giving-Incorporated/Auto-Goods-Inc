# Key Lifecycle

This document specifies required controls. Implementation is pending.

Every credential, signing key, authentication key, Stripe secret, deployment token, webhook secret, email credential, model key, and bank-access credential must have an owner, purpose, environment, scope, storage location, creation time, rotation policy, consumers, last-use evidence, and revocation procedure.

## Lifecycle

1. **Create:** generate through the approved provider, never in prompts or source control.
2. **Store:** use an approved secret store and separate production from non-production.
3. **Grant:** issue least privilege to a named workload under an `AuthorityGrant`; agents cannot broaden scope.
4. **Use:** prevent logging, preserve access evidence, and enforce external tool allowlists and spend ceilings.
5. **Rotate:** rotate on schedule, personnel or workload changes, provider guidance, suspected exposure, and before expired overlap closes.
6. **Revoke:** immediately revoke on compromise, unauthorized use, abandoned integration, or grant expiry. Freeze affected writes and payouts when financial integrity may be involved.
7. **Verify:** confirm old credentials fail, new credentials work only in intended scope, dependent signatures remain verifiable where required, and a `RunReceipt` records the change.

Key material and private identifiers must never enter public impact provenance. Any unverified lifecycle step is `NOT_COMPUTABLE` and blocks production use where the missing control is material.
