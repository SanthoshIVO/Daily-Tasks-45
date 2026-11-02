import os
import requests
from dotenv import load_dotenv

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv['HF_TOKEN']}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = query({
    "messages": [
        {
            "role": "user",
            "content": "Explain the difference between AI, ML, Deep Learning and Generative AI in 4 short lines."

        }
    ],
    "model": "openai/gpt-oss-120b:groq"
})

print(response["choices"][0]["message"])