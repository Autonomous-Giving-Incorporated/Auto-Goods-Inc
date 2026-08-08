# Validation test specification

The executable acceptance suite is `python3 -m unittest discover -s tests -v`.
It proves both acceptance and rejection behavior rather than treating successful
parsing as sufficient.

| Concern | Positive fixture/check | Required rejection |
|---|---|---|
| JSON Schema validity | every `schemas/*.json` parses and passes the installed JSON Schema meta-validator | malformed JSON and invalid schema keyword types |
| YAML parsing | policies and valid YAML fixtures parse with `yaml.safe_load` | malformed YAML |
| Lifecycle | declared, contiguous, allowed transitions reach the expected final state | skipped, disconnected, or undeclared transitions |
| Evidence labels | canonical labels and label-specific provenance | unknown labels, duplicate IDs, missing source/basis |
| Treasury | integer minor units, non-negative values, exact per-entry sums and 50/50 split | floats/bools, imbalance, negative values, mismatched totals |
| Category totals | non-negative integer category values sum to declared grand total | wrong total or non-integer category value |
| Authority | actor has a role granted for the operation | unassigned or unauthorized operation |
| Separation of duties | requester and approver differ; incompatible roles are not co-assigned | self-approval or incompatible role co-assignment |

Repository discovery intentionally validates source `schemas/` and `policies/`
without rewriting them. Semantic fixtures define small, auditable examples for
cross-document invariants that JSON Schema alone cannot express.
