from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User

from core.models import Movie
from .serializers import CreateUserSerializer, CreateMovieSerializer, ListMovieSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class CreateMovieView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = CreateMovieSerializer
    permission_classes = (IsAuthenticated,)


class ListMovieView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = ListMovieSerializer
    permission_classes = (IsAuthenticated,)
