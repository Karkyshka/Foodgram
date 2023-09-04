from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from .models import CustomUser, Subscriber


class CustomUserSerializers(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class SubscriberSerializers(serializers.Serializer):

    class Meta:
        model = Subscriber
        fields = '__all__'