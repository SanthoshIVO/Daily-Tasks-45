"""
Call the Claude API and print the response + token usage.

Install:  pip install anthropic python-dotenv
Key:      set ANTHROPIC_API_KEY (environment variable or .env file)
Run:      python llm_call_claude.py
"""



# import anthropic

# client = anthropic.Anthropic()


# for block in message.content:
#     if block.type == "text":
        # print(block.text)

import os

import anthropic
from dotenv import load_dotenv

load_dotenv()  # reads .env if present

# If you get "model not found", check the current model names in the Anthropic docs.
MODEL = "claude-haiku-5-5"

PROMPT = "Explain the difference between AI, ML, Deep Learning and Generative AI in 4 short lines."


def main() -> None:
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise SystemExit("ANTHROPIC_API_KEY is not set. Add it to your environment or .env file.")

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY automatically

    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": PROMPT,
            }
        ],
    )

    print("=== RESPONSE ===")
    print(message.content[0].text)

    print("\n=== TOKEN USAGE ===")
    print("Model          :", message.model)
    print("Input tokens   :", message.usage.input_tokens)
    print("Output tokens  :", message.usage.output_tokens)
    print("Total tokens   :", message.usage.input_tokens + message.usage.output_tokens)
    print("Stop reason    :", message.stop_reason)


if __name__ == "__main__":
    main()
