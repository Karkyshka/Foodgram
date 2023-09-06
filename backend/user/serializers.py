from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.db.models import Count

from .models import Subscriber, CustomUser

User = get_user_model

class CustomUserSerializers(UserSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'


class SubscriberSerializers(UserSerializer):

    class Meta:
        model = Subscriber
        fields = '__all__'