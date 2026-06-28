from ollama import chat


def explain_topic(prompt: str) -> str:
    """
    Explain programming concepts clearly.
    """

    response = chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert programming instructor.\n"
                    "Explain concepts clearly with simple examples.\n"
                    "Do not generate code unless necessary."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response["message"]["content"].strip()