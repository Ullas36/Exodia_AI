import weaviate
import os

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")

client = weaviate.Client(WEAVIATE_URL)


CLASS_NAME = "ChatMessage"

def setup_schema():
    schema = {
        "class": CLASS_NAME,
        "description": "Chat history messages",
        "properties": [
            {
                "name": "role",
                "dataType": ["text"]
            },
            {
                "name": "content",
                "dataType": ["text"]
            }
        ]
    }

    try:
        client.schema.create_class(schema)
    except:
        pass


def store_message(role, content):
    data = {
        "role": role,
        "content": content
    }

    client.data_object.create(data, CLASS_NAME)


def get_history():
    result = client.query.get(
        CLASS_NAME,
        ["role", "content"]
    ).do()

    messages = result["data"]["Get"][CLASS_NAME]

    history = []

    for msg in messages:
        history.append(f"{msg['role']}: {msg['content']}")

    return "\n".join(history)


def clear_history():
    client.schema.delete_class(CLASS_NAME)
    setup_schema()
