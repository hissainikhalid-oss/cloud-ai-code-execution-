from django.urls import path
from .views import generate_code

urlpatterns = [
    path("generate/", generate_code, name="generate-code"),
]