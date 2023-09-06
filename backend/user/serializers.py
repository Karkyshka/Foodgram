from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from .models import CustomUser, Subscriber


class CustomUserSerializers(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = ('__all__', 'following')


class SubscriberSerializers(serializers.Serializer):
    follower = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Subscriber
        fields = ('__all__', 'follower')