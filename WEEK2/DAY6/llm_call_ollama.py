"""Call a local Ollama model and print its response and token usage.

Run with Ollama installed and running, and the model pulled:
    ollama pull qwen2.5:1.5b
    python llm_call_ollama.py
"""

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:1.5b"
PROMPT = "Explain AI, machine learning, deep learning, and generative AI simply."


def main() -> None:
    request = Request(
        OLLAMA_CHAT_URL,
        data=json.dumps(
            {
                "model": MODEL,
                "messages": [{"role": "user", "content": PROMPT}],
                "stream": False,
            }
        ).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urlopen(request, timeout=120) as response:
            result = json.load(response)
    except HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        raise SystemExit(
            f"Ollama returned HTTP {error.code}: {details}"
        ) from error
    except URLError as error:
        raise SystemExit(
            f"Could not connect to Ollama at {OLLAMA_CHAT_URL}. "
            "Make sure Ollama is running."
        ) from error

    input_tokens = result["prompt_eval_count"]
    output_tokens = result["eval_count"]

    print("=== RESPONSE ===")
    print(result["message"]["content"])

    print("\n=== TOKEN USAGE ===")
    print("Model         :", result["model"])
    print("Input tokens  :", input_tokens)
    print("Output tokens :", output_tokens)
    print("Total tokens  :", input_tokens + output_tokens)


if __name__ == "__main__":
    main()

'''
(DAY6.venv) PS E:\Ivoyant\WEEK2\DAY6> py llm_call_ollama.py
=== RESPONSE ===
Sure, I'd be happy to explain AI, machine learning, deep learning, and generative AI in simple terms:

1. **Artificial Intelligence (AI)**:
   - AI is the broader concept of machines being able to perform tasks that traditionally require human intelligence. It encompasses everything from simple decision-making (like using a calculator to solve a math problem) to more complex reasoning, understanding context, and creativity.

2. **Machine Learning (ML)**:
   - Machine Learning is a subset of AI where algorithms are designed to automatically improve based on experience. Instead of being explicitly programmed, the machine learning algorithms learn from the data they process.
   - ML algorithms can learn patterns from data and then make predictions or decisions without being explicitly programmed to do so. This is done through a process called training, where the algorithm adjusts its parameters until it can make predictions as close as possible to the actual outcomes.

3. **Deep Learning (DL)**:
   - Deep Learning is a subfield of machine learning that uses neural networks with many layers to learn more abstract features from the data. These networks are inspired by the structure of the human brain and can learn to recognize complex patterns.
   - DL is often used to build powerful AI systems capable of tasks that require deep understanding of context, such as image and speech recognition, natural language processing, and more.

4. **Generative AI (or Generative Adversarial Networks, GANs)**:
   - Generative AI is a type of deep learning that is used to generate realistic-looking data that is similar to the training data. This is achieved by training two networks in a competition: a generator network that tries to create new data and a discriminator network that tries to tell real data from fake data.
   - The generator network learns to create data that is very close to the training data, while the discriminator network tries to distinguish between real and fake data. The two networks learn from each other, and as a result, the generator network improves its ability to create realistic data that looks very similar to the training data.

These concepts build on each other and can be combined in various ways to build powerful AI systems for tasks like image and speech recognition, natural language understanding, and much more.

=== TOKEN USAGE ===
Model         : qwen2.5:1.5b
Input tokens  : 45
Output tokens : 450
Total tokens  : 495'''