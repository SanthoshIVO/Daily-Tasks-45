"""
Visualise how a sentence is split into tokens.

Install:  pip install tiktoken
Run:      python tokenizer_demo.py
"""

import tiktoken

SENTENCES = [
    "Hello, I am learning Generative AI today.",
    "Unbelievability is a rare word.",
    "def add(a, b): return a + b",
    "ನಾನು ಇಂದು ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಕಲಿಯುತ್ತಿದ್ದೇನೆ",  # Kannada
]

# Two common OpenAI encodings. Compare how they split the same text.
ENCODINGS = ["cl100k_base", "o200k_base"]


def show_tokens(text: str, encoding_name: str) -> None:
    enc = tiktoken.get_encoding(encoding_name)
    token_ids = enc.encode(text)

    # Decode each token on its own. Some tokens are only part of a multi-byte
    # character (common for non-English text), so use errors="replace".
    pieces = [
        enc.decode_single_token_bytes(t).decode("utf-8", errors="replace")
        for t in token_ids
    ]

    print(f"  [{encoding_name}]  characters: {len(text)}  tokens: {len(token_ids)}")
    print("  pieces :", " | ".join(repr(p) for p in pieces))
    print("  ids    :", token_ids)
    print()


def main() -> None:
    for text in SENTENCES:
        print("=" * 70)
        print("TEXT:", text)
        for name in ENCODINGS:
            show_tokens(text, name)


if __name__ == "__main__":
    main()
