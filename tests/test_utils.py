import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from utils import get_slot_value, normalise_topic


class UtilsTests(unittest.TestCase):
    def test_normalise_topic_removes_extra_space_and_lowercases(self):
        self.assertEqual(normalise_topic("  Machine Learning "), "machine learning")

    def test_get_slot_value_returns_empty_string_for_missing_slot(self):
        self.assertEqual(get_slot_value({"slots": {}}, "topic"), "")


if __name__ == "__main__":
    unittest.main()
