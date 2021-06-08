from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import (
    UserCreateSerializer,
)


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
