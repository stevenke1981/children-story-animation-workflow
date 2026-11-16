import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_plan", ROOT / "scripts" / "validate_plan.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.plan = json.loads((ROOT / "templates" / "story-plan.json").read_text(encoding="utf-8-sig"))

    def test_valid_timing_and_optional_files(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(module.validate(self.plan, Path(directory)), [])
            self.assertTrue(any("file not found" in e for e in module.validate(self.plan, Path(directory), True)))

    def test_rejects_gap_duplicate_missing_narration_and_escape(self):
        plan = copy.deepcopy(self.plan)
        plan["scenes"][1].update(id="01", start_seconds=40, image="../outside.jpg", narration={"en": "Hello"})
        errors = module.validate(plan, ROOT)
        self.assertTrue(any("duplicate" in e for e in errors))
        self.assertTrue(any("expected start" in e for e in errors))
        self.assertTrue(any("missing narration" in e for e in errors))
        self.assertTrue(any("inside" in e for e in errors))


if __name__ == "__main__": unittest.main()
