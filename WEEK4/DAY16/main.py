"""Run the Day 16 hallucination probes and save responses as JSON Lines."""

import json
from pathlib import Path

from WEEK4.ollama_client import MODEL, chat


HERE = Path(__file__).resolve().parent
TEST_SET = HERE / "test_cases.json"
RESULTS = HERE / "results.jsonl"
SYSTEM_PROMPT = (
    "Answer accurately and briefly. Do not invent facts, quotations, citations, "
    "or events. If a premise is false or you cannot verify a claim, say so plainly "
    "and explain what is known. Do not pretend to have live web access. "
    "Use at most three concise sentences."
)


def main() -> None:
    test_cases = json.loads(TEST_SET.read_text(encoding="utf-8"))
    with RESULTS.open("w", encoding="utf-8") as output_file:
        for index, case in enumerate(test_cases, start=1):
            print(f"[{index}/{len(test_cases)}] {case['test_id']}: {case['category']}")
            response = chat(case["prompt"], system_prompt=SYSTEM_PROMPT)
            result = {
                **case,
                "model": MODEL,
                "response": response,
                "review_status": "needs human review",
            }
            output_file.write(json.dumps(result, ensure_ascii=False) + "\n")
            output_file.flush()
            print(response)
            print()

    print(f"Saved {len(test_cases)} responses to {RESULTS}")
    print("Review each response against its expected_behavior before marking it pass/fail.")


if __name__ == "__main__":
    main()
