from ollama import chat


def generate_code(prompt: str, language: str) -> str:
    """
    Generate source code using Ollama.
    """

    response = chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert software engineer.\n"
                    "Return ONLY the source code.\n"
                    "Do not explain anything.\n"
                    "Do not use markdown.\n"
                    "Do not wrap the code inside triple backticks."
                ),
            },
            {
                "role": "user",
                "content": f"Write a {language} program.\n\n{prompt}",
            },
        ],
    )

    code = response["message"]["content"]

    # Remove Markdown code fences
    code = code.replace("```python", "")
    code = code.replace("```", "")
    code = code.strip()

    return code