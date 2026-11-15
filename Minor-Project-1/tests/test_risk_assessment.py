import tempfile
import unittest
from pathlib import Path

from risk_assessment import (
    RISK_REGISTER, assess_risk, build_assessment, export_csv,
    export_json, risk_level,
)

class RiskAssessmentTests(unittest.TestCase):
    def test_risk_bands(self):
        self.assertEqual(risk_level(1), "Low")
        self.assertEqual(risk_level(5), "Moderate")
        self.assertEqual(risk_level(10), "High")
        self.assertEqual(risk_level(17), "Critical")

    def test_invalid_score_rejected(self):
        with self.assertRaises(ValueError):
            risk_level(0)
        with self.assertRaises(ValueError):
            assess_risk({"id": "X", "likelihood": 6, "impact": 2})

    def test_score_is_likelihood_times_impact(self):
        row = assess_risk({"id": "X", "likelihood": 3, "impact": 4})
        self.assertEqual(row["risk_score"], 12)
        self.assertEqual(row["risk_level"], "High")

    def test_default_register_sorted_descending(self):
        rows = build_assessment()
        scores = [row["risk_score"] for row in rows]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertEqual(len(rows), len(RISK_REGISTER))

    def test_exports(self):
        rows = build_assessment()
        with tempfile.TemporaryDirectory() as temp:
            json_path = Path(temp) / "assessment.json"
            csv_path = Path(temp) / "assessment.csv"
            export_json(rows, json_path)
            export_csv(rows, csv_path)
            self.assertIn('"risk_score"', json_path.read_text(encoding="utf-8"))
            self.assertIn("threat", csv_path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
