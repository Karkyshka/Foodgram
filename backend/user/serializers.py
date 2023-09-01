from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from .models import CustomUser


class CustomUserSerializers(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
