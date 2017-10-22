from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User

from core.models import Movie
from core import serializers as core_serializers


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = core_serializers.CreateUserSerializer
    permission_classes = (AllowAny,)


class ListCreateMovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = core_serializers.MovieSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    # def get_queryset(self):
    #     movie = Movie.objects.all()
    #     name = self.request.query_params.get('name')
    #     year = self.request.query_params.get('year')
    #
    #     if name:
    #         movie = movie.filter(name=name)
    #     if year:
    #         movie = movie.filter(year=year)
    #
    #     return movie


class MovieByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = core_serializers.MovieSerializer
