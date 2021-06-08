from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    MessageSerializer,
    ChatSerializer,
)
from tg_bot.models import (
    Message,
    Chat,
)


class MessageCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ChatCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
