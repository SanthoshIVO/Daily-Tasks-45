from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

stream = client.chat.completions.create(
    messages=[{"role": "user", "content": "Write a short haiku about coding."}],
    model="llama-3.1-8b-instant",
    stream=True,
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print()