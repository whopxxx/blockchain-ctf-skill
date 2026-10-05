import tempfile
import unittest
from pathlib import Path

from scripts.validate_structure import ROOT, validate


class StructureTests(unittest.TestCase):
    def test_repository_structure_is_valid(self):
        self.assertEqual([], validate(ROOT))

    def test_missing_skill_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            errors = validate(Path(directory))
        self.assertIn("missing required file: SKILL.md", errors)

    def test_curated_reference_has_no_tracking_parameters(self):
        research = (ROOT / "reference.txt").read_text(encoding="utf-8")
        self.assertNotIn("utm_", research.lower())


if __name__ == "__main__":
    unittest.main()
