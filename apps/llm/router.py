from ollama import chat


def classify_intent(prompt: str) -> str:
    """
    Classify the user's prompt into one of three intents.
    """

    response = chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an intent classifier.\n"
                    "Respond with ONLY one of these words:\n"
                    "- code_generation\n"
                    "- explanation\n"
                    "- general_chat"
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response["message"]["content"].strip().lower()