#!/usr/bin/env python3
"""Repository and governance-fixture validator.

Only PyYAML is optional. JSON Schema files are checked with jsonschema when it is
installed and otherwise receive structural meta-schema checks. Semantic fixture
validation uses the Python standard library exclusively.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

EVIDENCE_LABELS = {"OBSERVED", "INFERRED", "SPECULATIVE", "NOT_COMPUTABLE"}

@dataclass(frozen=True)
class Finding:
    path: Path
    message: str


def _load(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        return json.loads(text)
    if path.suffix in {".yaml", ".yml"}:
        if yaml is None:
            raise RuntimeError("PyYAML is required to parse YAML files")
        return yaml.safe_load(text)
    raise ValueError(f"unsupported input type: {path.suffix}")


def validate_schema(path: Path, value: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, dict):
        return ["JSON Schema root must be an object"]
    if "$schema" not in value:
        errors.append("JSON Schema must declare $schema")
    if jsonschema is not None:
        try:
            jsonschema.validators.validator_for(value).check_schema(value)
        except Exception as exc:
            errors.append(f"invalid JSON Schema: {exc}")
    elif not any(k in value for k in ("type", "$ref", "oneOf", "anyOf", "allOf")):
        errors.append("schema has no type, reference, or composition keyword")
    return errors


def _integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def validate_fixture(doc: Any) -> list[str]:
    if not isinstance(doc, dict):
        return ["fixture root must be a mapping"]
    kind = doc.get("kind")
    validators = {
        "lifecycle": _validate_lifecycle,
        "evidence": _validate_evidence,
        "treasury": _validate_treasury,
        "category_totals": _validate_categories,
        "authority": _validate_authority,
    }
    if kind not in validators:
        return [f"unknown fixture kind: {kind!r}"]
    return validators[kind](doc)


def _validate_lifecycle(doc: dict[str, Any]) -> list[str]:
    states = doc.get("states")
    transitions = doc.get("transitions")
    events = doc.get("events")
    if not isinstance(states, list) or not states or len(states) != len(set(states)):
        return ["states must be a non-empty unique list"]
    if not isinstance(transitions, dict) or not isinstance(events, list):
        return ["transitions must be a mapping and events must be a list"]
    errors: list[str] = []
    current = doc.get("initial")
    if current not in states:
        errors.append("initial state is not declared")
    for index, event in enumerate(events):
        if not isinstance(event, dict):
            errors.append(f"events[{index}] must be a mapping")
            continue
        source, target = event.get("from"), event.get("to")
        if source != current:
            errors.append(f"events[{index}] source {source!r} does not match current state {current!r}")
        allowed = transitions.get(source, [])
        if target not in allowed:
            errors.append(f"events[{index}] transition {source!r} -> {target!r} is not allowed")
        if source not in states or target not in states:
            errors.append(f"events[{index}] references undeclared state")
        current = target
    expected = doc.get("final")
    if expected is not None and current != expected:
        errors.append(f"final state {current!r} does not match expected {expected!r}")
    return errors


def _validate_evidence(doc: dict[str, Any]) -> list[str]:
    items = doc.get("items")
    if not isinstance(items, list):
        return ["items must be a list"]
    errors: list[str] = []
    ids: set[Any] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"items[{index}] must be a mapping")
            continue
        ident, label = item.get("id"), item.get("label")
        if not isinstance(ident, str) or not ident.strip():
            errors.append(f"items[{index}] requires a non-empty id")
        elif ident in ids:
            errors.append(f"duplicate evidence id {ident!r}")
        ids.add(ident)
        if label not in EVIDENCE_LABELS:
            errors.append(f"items[{index}] has invalid evidence label {label!r}")
        if label == "OBSERVED" and not item.get("source"):
            errors.append(f"items[{index}] OBSERVED evidence requires source")
        if label == "INFERRED" and not item.get("basis"):
            errors.append(f"items[{index}] INFERRED evidence requires observed basis")
        if label == "INFERRED" and item.get("basis") and not all(b in ids for b in item.get("basis", [])):
            errors.append(f"items[{index}] INFERRED basis must reference prior observed inputs")
        if label == "SPECULATIVE" and (item.get("authorizes_spend") or item.get("authorizes_promotion")):
            errors.append(f"items[{index}] SPECULATIVE evidence cannot authorize spend or promotion")
        if label == "NOT_COMPUTABLE" and item.get("substituted_value") is not None:
            errors.append(f"items[{index}] NOT_COMPUTABLE cannot contain an invented substitute")
    return errors


def _validate_treasury(doc: dict[str, Any]) -> list[str]:
    entries = doc.get("entries")
    if not isinstance(entries, list):
        return ["entries must be a list"]
    errors: list[str] = []
    total = community = organization = 0
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entries[{index}] must be a mapping")
            continue
        amounts = [entry.get(k) for k in ("distributable_profit", "community_allocation", "organization_allocation")]
        if not all(_integer(v) for v in amounts):
            errors.append(f"entries[{index}] monetary values must be integer minor units")
            continue
        amount, com, org = amounts
        if amount <= 0 or com < 0 or org < 0:
            errors.append(f"entries[{index}] distributable profit must be positive and allocations non-negative")
        if com + org != amount:
            errors.append(f"entries[{index}] allocations do not sum to distributable profit")
        if abs(com - org) > 1:
            errors.append(f"entries[{index}] violates 50/50 one-minor-unit tolerance")
        total += amount; community += com; organization += org
    declared = doc.get("totals", {})
    for name, actual in (("distributable_profit", total), ("community_allocation", community), ("organization_allocation", organization)):
        if declared.get(name) != actual:
            errors.append(f"declared total {name!r} is {declared.get(name)!r}, expected {actual}")
    return errors


def _validate_categories(doc: dict[str, Any]) -> list[str]:
    categories, expected = doc.get("categories"), doc.get("grand_total")
    if not isinstance(categories, dict) or not categories:
        return ["categories must be a non-empty mapping"]
    errors: list[str] = []
    required_categories = {"food", "housing", "healthcare", "education", "community_space"}
    if set(categories) != required_categories:
        errors.append(f"categories must be exactly {sorted(required_categories)!r}")
    actual = 0
    for name, amount in categories.items():
        if not isinstance(name, str) or not name:
            errors.append("category names must be non-empty strings")
        if not _integer(amount) or amount < 0:
            errors.append(f"category {name!r} total must be a non-negative integer")
        else:
            actual += amount
    if not _integer(expected) or expected != actual:
        errors.append(f"grand_total is {expected!r}, expected {actual}")
    return errors


def _validate_authority(doc: dict[str, Any]) -> list[str]:
    grants, actions = doc.get("grants"), doc.get("actions")
    incompatible = doc.get("incompatible_roles", [])
    assignments = doc.get("assignments", {})
    if not isinstance(grants, dict) or not isinstance(actions, list):
        return ["grants must be a mapping and actions must be a list"]
    errors: list[str] = []
    if not isinstance(assignments, dict) or not isinstance(incompatible, list):
        errors.append("assignments must be a mapping and incompatible_roles must be a list")
    else:
        for principal, roles in assignments.items():
            role_set = set(roles) if isinstance(roles, list) else set()
            for pair in incompatible:
                if isinstance(pair, list) and len(pair) == 2 and set(pair) <= role_set:
                    errors.append(f"principal {principal!r} holds incompatible roles {pair!r}")
    for index, action in enumerate(actions):
        if not isinstance(action, dict):
            errors.append(f"actions[{index}] must be a mapping")
            continue
        actor, operation = action.get("actor"), action.get("operation")
        roles = set(assignments.get(actor, []))
        permitted = set(grants.get(operation, []))
        if not roles & permitted:
            errors.append(f"actions[{index}] actor {actor!r} lacks authority for {operation!r}")
        requester, approver = action.get("requested_by"), action.get("approved_by")
        if requester is not None or approver is not None:
            if not requester or not approver:
                errors.append(f"actions[{index}] requires requester and approver")
            elif requester == approver:
                errors.append(f"actions[{index}] violates requester/approver separation of duties")
    return errors


def validate_paths(paths: Iterable[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        try:
            value = _load(path)
            messages = validate_schema(path, value) if path.suffix == ".json" and "schemas" in path.parts else (
                validate_fixture(value) if "fixtures" in path.parts else []
            )
            findings.extend(Finding(path, msg) for msg in messages)
        except Exception as exc:
            findings.append(Finding(path, str(exc)))
    return findings


def discover(root: Path, include_fixtures: bool = False) -> list[Path]:
    paths: list[Path] = []
    for dirname in ("schemas", "policies"):
        directory = root / dirname
        if directory.exists():
            paths.extend(p for p in directory.rglob("*") if p.suffix in {".json", ".yaml", ".yml"})
    if include_fixtures:
        paths.extend(p for p in (root / "tests" / "fixtures" / "valid").rglob("*") if p.suffix in {".json", ".yaml", ".yml"})
    return sorted(paths)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--include-valid-fixtures", action="store_true")
    args = parser.parse_args(argv)
    paths = args.paths or discover(args.root, args.include_valid_fixtures)
    findings = validate_paths(paths)
    for finding in findings:
        print(f"{finding.path}: {finding.message}", file=sys.stderr)
    if findings:
        print(f"validation failed: {len(findings)} finding(s)", file=sys.stderr)
        return 1
    print(f"validated {len(paths)} file(s)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
