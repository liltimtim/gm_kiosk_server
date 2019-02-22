from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Kiosk


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class KioskSerializer(serializers.ModelSerializer):
    players = UserSerializer(read_only=True, many=True)

    class Meta:
        fields = ('id', 'name', 'join_code', 'players')
        model = Kiosk
