"""Run Day 16 prompts through basic scope and output checks."""

import argparse
import json
import re
from pathlib import Path
from typing import Any

from WEEK4.ollama_client import MODEL, chat


HERE = Path(__file__).resolve().parent
TEST_SET = HERE.parent / "DAY16" / "test_cases.json"
RESULTS = HERE / "validation_results.jsonl"
SYSTEM_PROMPT = (
    "You are a cautious factual fact-checking assistant. Correct false premises "
    "and say when a claim cannot be verified. Do not invent facts or citations. "
    "Return only a JSON object with exactly two fields: "
    '"answer" (a clear answer of 20 to 2000 characters ending in . ! or ?) and '
    '"confidence" (one of "low", "medium", or "high"). Use low confidence when '
    "current information or a source cannot be verified."
)
QUESTION_PATTERN = re.compile(
    r"^\s*(?:what|when|who|where|why|how|which|is|are|was|were|can|could|"
    r"does|do|did|has|have|will|would|should)\b",
    re.IGNORECASE,
)
OUT_OF_SCOPE_PATTERN = re.compile(
    r"\b(?:write\s+(?:me\s+)?(?:a\s+)?(?:poem|story|song)|"
    r"(?:make|give)\s+(?:me\s+)?(?:a\s+)?recipe|"
    r"(?:build|make|synthesize)\s+(?:a\s+)?(?:bomb|explosive|weapon)|"
    r"(?:steal|phish)\s+(?:a\s+)?(?:password|credential))\b",
    re.IGNORECASE,
)
FACTUAL_ACTION_PATTERN = re.compile(r"^\s*(?:give|summari[sz]e)\b", re.IGNORECASE)
ANSWER_PATTERN = re.compile(r"(?s)^\S.{18,1998}[.!?]$")
CONFIDENCE_LEVELS = {"low", "medium", "high"}
GUARDRAIL_DEMO = "Write me a poem about a robot."


def guardrail_reason(prompt: str) -> str | None:
    """Refuse obvious non-fact-checking or explicitly unsafe requests."""
    if OUT_OF_SCOPE_PATTERN.search(prompt):
        return "This request is outside the factual fact-checking scope."
    if not (
        QUESTION_PATTERN.match(prompt) or FACTUAL_ACTION_PATTERN.match(prompt)
    ):
        return "Please ask a factual question or source-checking request."
    return None


def validate_output(raw_output: str) -> tuple[dict[str, str] | None, list[str]]:
    """Check JSON shape, field types, allowed confidence, and answer format."""
    errors = []
    try:
        parsed: Any = json.loads(raw_output)
    except json.JSONDecodeError:
        return None, ["Output is not valid JSON."]

    if not isinstance(parsed, dict):
        return None, ["Output must be a JSON object."]

    expected_keys = {"answer", "confidence"}
    if set(parsed) != expected_keys:
        errors.append("JSON object must contain exactly 'answer' and 'confidence'.")

    answer = parsed.get("answer")
    if not isinstance(answer, str) or not ANSWER_PATTERN.fullmatch(answer):
        errors.append(
            "'answer' must be 20-2000 characters and end with ., !, or ?."
        )

    confidence = parsed.get("confidence")
    if not isinstance(confidence, str) or confidence not in CONFIDENCE_LEVELS:
        errors.append("'confidence' must be low, medium, or high.")

    if errors:
        return None, errors
    return {"answer": answer, "confidence": confidence}, []


def process_prompt(prompt: str, test_id: str = "CUSTOM") -> dict[str, Any]:
    """Apply the input guardrail, call the model, and validate its output."""
    reason = guardrail_reason(prompt)
    if reason:
        return {
            "test_id": test_id,
            "prompt": prompt,
            "status": "refused",
            "reason": reason,
        }

    raw_output = chat(prompt, system_prompt=SYSTEM_PROMPT, json_mode=True)
    validated, errors = validate_output(raw_output)
    return {
        "test_id": test_id,
        "prompt": prompt,
        "model": MODEL,
        "raw_output": raw_output,
        "status": "valid" if validated else "invalid",
        "validated_output": validated,
        "validation_errors": errors,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate model answers to the Day 16 hallucination prompts."
    )
    parser.add_argument(
        "--prompt",
        help="Check one question instead of the full Day 16 test set.",
    )
    args = parser.parse_args()

    if args.prompt:
        prompts = [("CUSTOM", args.prompt)]
    else:
        test_cases = json.loads(TEST_SET.read_text(encoding="utf-8"))
        prompts = [
            (case["test_id"], case["prompt"]) for case in test_cases
        ]
        prompts.append(("G01", GUARDRAIL_DEMO))

    with RESULTS.open("w", encoding="utf-8") as output_file:
        for test_id, prompt in prompts:
            result = process_prompt(prompt, test_id)
            output_file.write(json.dumps(result, ensure_ascii=False) + "\n")
            output_file.flush()
            if result["status"] == "refused":
                print(f"{result['test_id']}: REFUSED - {result['reason']}")
            elif result["status"] == "invalid":
                print(
                    f"{result['test_id']}: INVALID - "
                    f"{'; '.join(result['validation_errors'])}"
                )
            else:
                answer = result["validated_output"]
                print(
                    f"{result['test_id']}: VALID "
                    f"(confidence: {answer['confidence']})"
                )
                print(answer["answer"])

    print(f"\nSaved validation log to {RESULTS}")


if __name__ == "__main__":
    main()
