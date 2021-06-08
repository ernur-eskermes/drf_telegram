from django.contrib import admin

from .models import (
    Message,
    Chat,
)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'created',
    )
    search_fields = (
        'message',
    )


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
    )
    search_fields = (
        'user__username',
        'user__first_name',
    )
