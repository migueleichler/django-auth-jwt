from rest_framework import serializers
from django.contrib.auth.models import User

from core.models import Movie


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()

        return user


class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ListMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'year', 'duration')
