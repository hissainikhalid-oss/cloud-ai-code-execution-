from ollama import chat


def general_chat(prompt: str) -> str:
    """
    Handle general conversations.
    """

    response = chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response["message"]["content"].strip()