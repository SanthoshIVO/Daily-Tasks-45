"""Small standard-library client for a locally running Ollama server."""

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:4b")


def chat(prompt: str, system_prompt: str = "", json_mode: bool = False) -> str:
    """Send one prompt to Ollama and return the assistant's text."""
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "think": False,
        "options": {"temperature": 0, "num_predict": 256},
    }
    if json_mode:
        payload["format"] = "json"

    request = Request(
        f"{OLLAMA_URL}/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=180) as response:
            result = json.load(response)
    except HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Ollama returned HTTP {error.code}: {details}") from error
    except URLError as error:
        raise RuntimeError(
            f"Cannot connect to Ollama at {OLLAMA_URL}. Start Ollama and try again."
        ) from error

    content = result.get("message", {}).get("content")
    if not isinstance(content, str):
        raise RuntimeError("Ollama response did not contain assistant text.")
    return content
