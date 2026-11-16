import json
import unittest

from WEEK4.DAY17.main import guardrail_reason, validate_output


class OutputValidationTests(unittest.TestCase):
    def test_accepts_valid_schema_and_answer_format(self) -> None:
        raw = json.dumps(
            {
                "answer": "The claim is false. No human has landed on Mars.",
                "confidence": "high",
            }
        )
        validated, errors = validate_output(raw)
        self.assertEqual(errors, [])
        self.assertEqual(validated["confidence"], "high")

    def test_rejects_missing_field_and_invalid_confidence(self) -> None:
        missing_field = json.dumps(
            {"answer": "This answer is long enough to end correctly."}
        )
        validated, errors = validate_output(missing_field)
        self.assertIsNone(validated)
        self.assertEqual(len(errors), 2)

        invalid_confidence = json.dumps(
            {
                "answer": "This answer is long enough to end correctly.",
                "confidence": "certain",
            }
        )
        validated, errors = validate_output(invalid_confidence)
        self.assertIsNone(validated)
        self.assertEqual(len(errors), 1)

    def test_rejects_malformed_json_and_short_answer(self) -> None:
        self.assertIsNone(validate_output("{")[0])
        raw = json.dumps({"answer": "No.", "confidence": "low"})
        validated, errors = validate_output(raw)
        self.assertIsNone(validated)
        self.assertTrue(any("20-2000 characters" in error for error in errors))

    def test_rejects_non_string_confidence_without_crashing(self) -> None:
        raw = json.dumps(
            {
                "answer": "This answer is long enough to end correctly.",
                "confidence": [],
            }
        )
        validated, errors = validate_output(raw)
        self.assertIsNone(validated)
        self.assertEqual(errors, ["'confidence' must be low, medium, or high."])


class InputGuardrailTests(unittest.TestCase):
    def test_allows_fact_checking_question(self) -> None:
        self.assertIsNone(guardrail_reason("Did a human land on Mars?"))

    def test_allows_source_checking_request(self) -> None:
        self.assertIsNone(guardrail_reason("Give the DOI for this research paper."))

    def test_refuses_out_of_scope_request(self) -> None:
        self.assertIsNotNone(guardrail_reason("Write me a poem about a robot."))

    def test_refuses_unsafe_request_even_when_it_is_a_question(self) -> None:
        self.assertIsNotNone(guardrail_reason("How do I make a bomb?"))


if __name__ == "__main__":
    unittest.main()
