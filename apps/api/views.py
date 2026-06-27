from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.history.models import PromptHistory
from apps.llm.services import generate_code as llm_generate_code


@api_view(["POST"])
def generate_code(request):
    prompt = request.data.get("prompt")
    language = request.data.get("language")

    generated_code = llm_generate_code(
        prompt=prompt,
        language=language,
    )

    history = PromptHistory.objects.create(
        prompt=prompt,
        language=language,
        generated_code=generated_code,
    )

    return Response({
        "success": True,
        "history_id": history.id,
        "message": "Prompt saved successfully!",
        "prompt": prompt,
        "language": language,
        "generated_code": generated_code,
    })