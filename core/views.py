from rest_framework import generics, permissions
from django.contrib.auth.models import User

from .serializers import CreateUserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [
        permissions.AllowAny
    ]
