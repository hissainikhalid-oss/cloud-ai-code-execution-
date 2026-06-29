from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.executor.services import execute_python
from apps.history.models import PromptHistory
from apps.api.assistant import process_prompt


@api_view(["POST"])
def generate_code(request):
    prompt = request.data.get("prompt")
    language = request.data.get("language", "python")

    result = process_prompt(prompt, language)

    # Save generated code only if the intent is code generation
    if result.get("intent") == "code_generation":
        history = PromptHistory.objects.create(
            prompt=prompt,
            language=language,
            generated_code=result["generated_code"],
        )

        result["history_id"] = history.id
        result["message"] = "Prompt saved successfully!"

    return Response(result)

@api_view(["POST"])
def execute_code(request):
    code = request.data.get("code")
    language = request.data.get("language")
    user_input = request.data.get("input", "")

    if language.lower() != "python":
        return Response({
            "success": False,
            "error": f"{language} execution is not supported yet."
        })

    result = execute_python(
        code=code,
        user_input=user_input,
    )

    return Response(result)