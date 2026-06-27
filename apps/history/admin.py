from django.contrib import admin
from .models import PromptHistory


@admin.register(PromptHistory)
class PromptHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "language",
        "created_at",
    )

    search_fields = (
        "prompt",
        "language",
    )

    list_filter = (
        "language",
        "created_at",
    )