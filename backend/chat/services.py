import os
import requests
from .weaviate_helper import store_message, get_history
from .logger import log_event


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434/api/generate")


def process_chat(user_message):

    log_event(f"User: {user_message}")

    store_message("User", user_message)

    context = get_history()

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen2.5:1.5b",
            "prompt": context,
            "stream": False
        }
    )

    ai_reply = response.json()["response"]

    store_message("AI", ai_reply)

    log_event(f"AI: {ai_reply}")

    return ai_reply
