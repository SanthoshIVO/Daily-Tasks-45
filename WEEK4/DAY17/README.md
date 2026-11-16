# Day 17 - Output validation and guardrails

## Run it

From the repository root, with Ollama running:

```powershell
python -m WEEK4.DAY17.main
```

This sends all ten Day 16 prompts to the local model and also checks a
non-factual poem request, which the input guardrail should refuse before the
model is called. Responses and validation results are saved to
`validation_results.jsonl`.

To try one question or see the refusal behavior directly:

```powershell
python -m WEEK4.DAY17.main --prompt "Did a human land on Mars?"
python -m WEEK4.DAY17.main --prompt "Write me a poem about a robot."
```

## What is checked

1. **Input guardrail:** allows question-shaped fact-checks and source-checking
   requests; refuses
   obvious creative-writing/non-factual requests and a few explicitly unsafe
   patterns.
2. **JSON schema:** requires exactly `answer` and `confidence`, both with the
   expected types; confidence must be `low`, `medium`, or `high`.
3. **Regex check:** requires the answer to be 20-2000 characters and end with
   sentence punctuation.
4. **Logging:** records raw model output, pass/fail status, validation errors,
   or the reason for refusal.

The guardrail is a beginner-friendly demonstration, not a complete safety
system. It uses simple text patterns, so it can miss rephrased requests or
refuse a harmless one. Output validation checks structure and formatting, not
whether the answer is factually true. Human review and source checking are still
needed.

## What this run showed

All ten model responses passed the JSON and formatting checks, and the extra
poem request was refused. That does **not** mean all ten answers were correct:
H06 still claimed that the 2026 Nobel Prize in Physics had not been awarded,
and H07 incorrectly described 10^100 as an accepted estimate for atoms in the
observable universe. These are recorded as `valid` because their JSON shape and
answer formatting were valid. This is the key difference between validating an
output's format and fact-checking its content.

Run the focused tests from the repository root:

```powershell
python -m unittest discover -s WEEK4\DAY17 -p "test_*.py"
```
