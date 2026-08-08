# Autonomy and Authority

Autonomy is bounded execution under policy, not unrestricted agency. Actions are `AUTO_ALLOWED`, `POLICY_ALLOWED`, `USER_CONFIRMATION_REQUIRED`, `QUALIFIED_HUMAN_REQUIRED`, or `PROHIBITED`.

| Action | Initial authority |
|---|---|
| Public research, hypothesis generation, opportunity scoring | `AUTO_ALLOWED` within allowlists and evidence rules |
| Prototype, repository, staging deployment | `POLICY_ALLOWED`; staging may be auto only if policy proves full reversibility |
| Initial production launch | `USER_CONFIRMATION_REQUIRED` |
| Price within approved range, approved campaigns, rule-bounded refunds | `POLICY_ALLOWED` |
| Advertising spend | Budget-bounded `POLICY_ALLOWED` enforced outside prompts |
| Treasury/community payout | Strict policy plus human approval in v0.1 |
| Add `CommunityOrganization` | Verification and approval required |
| Change accounting formula | Human governance required |
| Modify 50/50 split | `PROHIBITED` for agents |

An `AuthorityGrant` identifies actor, capability, resources, environment, policy version, time window, amount/rate ceilings, approval, and revocation. It is least privilege and cannot widen parent authority.

Agents cannot approve their own grants, expand tool access, modify budgets, redefine denied action, suppress reviewers, treat silence as consent, or split work to evade aggregate limits. Greater consequence demands greater isolation, reversibility, observability, and human review. Every attempt creates a `RunReceipt`; humans and incident controls can revoke grants and freeze capabilities independently of the acting model.
