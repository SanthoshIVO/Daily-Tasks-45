from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

stream = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": (
            # "Explain AI, machine learning, deep learning, and generative AI simply,  print the response + token usage"
            "Explain Promt Engieering  with all 8 types of prompt engineering, print the response + token usage"
        ),
    }],
    model="qwen/qwen3.8-27b",
    stream=True,
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print()