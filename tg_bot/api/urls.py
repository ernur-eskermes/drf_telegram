from django.urls import path

from .views import (
    MessageListAPIView,
    MessageCreateAPIView,
    ChatCreateAPIView
)

urlpatterns = [
    path('chats/create/', ChatCreateAPIView.as_view()),

    path('messages/', MessageListAPIView.as_view()),
    path('messages/create/', MessageCreateAPIView.as_view()),
]
