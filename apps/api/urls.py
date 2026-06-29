from django.urls import path
from .views import generate_code, execute_code

urlpatterns = [
    path("generate/", generate_code, name="generate-code"),
    path("execute/", execute_code, name="execute-code"),
]