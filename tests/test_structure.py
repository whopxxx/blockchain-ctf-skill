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


if __name__ == "__main__":
    unittest.main()
