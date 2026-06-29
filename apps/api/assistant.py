from apps.llm.router import classify_intent
from apps.llm.services import generate_code
from apps.llm.explain import explain_topic
from apps.llm.chat import general_chat


def process_prompt(prompt: str, language: str = "python"):
    """
    Process the user's prompt based on the detected intent.
    """

    intent = classify_intent(prompt)

    if intent == "code_generation":
        return {
            "success": True,
            "intent": intent,
            "generated_code": generate_code(prompt, language),
        }

    elif intent == "explanation":
        return {
            "success": True,
            "intent": intent,
            "answer": explain_topic(prompt),
        }

    elif intent == "general_chat":
        return {
            "success": True,
            "intent": intent,
            "answer": general_chat(prompt),
        }

    return {
        "success": False,
        "message": "Unable to classify prompt."
    }