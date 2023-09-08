from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.db.models import Count

from .models import Subscriber, CustomUser

class CustomUserSerializers(UserSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'


class SubscriberSerializers(UserSerializer):
    """Добавление пользователей в подписчки"""
    is_subscriber = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'email', 'id', 'username', 'first_name', 
            'last_name', 'is_subscribed'
            )
    
    def add_subscriber():
        pass