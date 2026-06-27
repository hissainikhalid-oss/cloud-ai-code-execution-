from django.db import models
from django.contrib.auth.models import User


class PromptHistory(models.Model):
    LANGUAGE_CHOICES = [
        ("python", "Python"),
        ("c", "C"),
        ("cpp", "C++"),
        ("java", "Java"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    prompt = models.TextField()

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES
    )

    generated_code = models.TextField()

    output = models.TextField(
        blank=True,
        default=""
    )

    error = models.TextField(
        blank=True,
        default=""
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.language} - {self.prompt[:40]}"