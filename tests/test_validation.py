from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.validate import _load, validate_fixture, validate_paths, validate_schema  # noqa: E402

VALID = ROOT / "tests" / "fixtures" / "valid"
INVALID = ROOT / "tests" / "fixtures" / "invalid"


class FixtureTests(unittest.TestCase):
    def test_all_valid_fixtures_pass(self):
        files = sorted(p for p in VALID.iterdir() if p.suffix in {".json", ".yaml"})
        self.assertGreaterEqual(len(files), 5)
        for path in files:
            with self.subTest(path=path.name):
                self.assertEqual([], validate_fixture(_load(path)))

    def test_every_invalid_fixture_is_rejected(self):
        files = sorted(p for p in INVALID.iterdir() if p.name != "malformed.yaml")
        self.assertGreaterEqual(len(files), 7)
        for path in files:
            with self.subTest(path=path.name):
                self.assertTrue(validate_fixture(_load(path)), f"{path} unexpectedly passed")

    def test_malformed_yaml_is_rejected(self):
        self.assertTrue(validate_paths([INVALID / "malformed.yaml"]))

    def test_integer_rule_rejects_boolean(self):
        doc = {"kind": "category_totals", "categories": {"x": True}, "grand_total": 1}
        self.assertTrue(validate_fixture(doc))


class RepositoryFormatTests(unittest.TestCase):
    def test_schema_meta_validation_rejects_invalid_keyword_type(self):
        schema = {"$schema": "https://json-schema.org/draft/2020-12/schema", "type": 7}
        self.assertTrue(validate_schema(Path("schemas/bad.json"), schema))

    def test_cli_returns_nonzero_for_bad_fixture(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate.py"), str(INVALID / "treasury_split.yaml")],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(1, proc.returncode)
        self.assertIn("50/50", proc.stderr)

    def test_cli_validates_repository_inputs(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate.py"), "--root", str(ROOT), "--include-valid-fixtures"],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(0, proc.returncode, proc.stderr)

    def test_invalid_json_syntax_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "schemas" / "bad.json"
            path.parent.mkdir()
            path.write_text('{"type":', encoding="utf-8")
            self.assertTrue(validate_paths([path]))


if __name__ == "__main__":
    unittest.main()
