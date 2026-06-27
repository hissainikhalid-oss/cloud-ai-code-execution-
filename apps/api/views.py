from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def generate_code(request):
    prompt = request.data.get("prompt")
    language = request.data.get("language")

    return Response({
        "success": True,
        "message": "API is working!",
        "prompt": prompt,
        "language": language,
        "generated_code": "print('Hello World')"
    })