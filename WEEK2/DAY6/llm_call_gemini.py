"""
Call the Gemini API and print the response + token usage.

Install:  pip install google-genai python-dotenv
Key:      set GEMINI_API_KEY (environment variable or .env file)
Run:      python llm_call_gemini.py
"""

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # reads .env if present

# If you get "model not found", check the current model names in Google AI Studio docs.
MODEL = "gemini-2.5-flash"

PROMPT = "Explain the difference between AI, ML, Deep Learning and Generative AI in 4 short lines."


def main() -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY is not set. Add it to your environment or .env file.")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=MODEL,
        contents=PROMPT,
        config=types.GenerateContentConfig(
            temperature=0.3,          # low = focused, repeatable
            max_output_tokens=500,    # cap on answer length
            system_instruction="You are a clear and concise AI tutor for beginners.",
        ),
    )

    print("=== RESPONSE ===")
    print(response.text)

    usage = response.usage_metadata
    print("\n=== TOKEN USAGE ===")
    print("Model          :", MODEL)
    print("Input tokens   :", usage.prompt_token_count)
    print("Output tokens  :", usage.candidates_token_count)
    print("Total tokens   :", usage.total_token_count)
    # Some models also report hidden "thinking" tokens; they may be counted in the total.
    thoughts = getattr(usage, "thoughts_token_count", None)
    if thoughts:
        print("Thinking tokens:", thoughts)


if __name__ == "__main__":
    main()
