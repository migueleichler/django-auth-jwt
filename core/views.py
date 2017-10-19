from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User

from core.models import Movie
from core.serializers import serializers as serializers


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.CreateUserSerializer
    permission_classes = (AllowAny,)


class CreateMovieView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.CreateMovieSerializer
    permission_classes = (IsAuthenticated,)


class ListMovieView(generics.ListApiView):
    queryset = Movie.objects.all()
    serializer_class = serializers.ListMovieSerializer
    permission_classes = (IsAuthenticated,)
