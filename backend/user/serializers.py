# from django.contrib.auth import get_user_model
# from django.db.models import Count
from djoser.serializers import UserSerializer
from rest_framework.serializers import SerializerMethodField

from .models import CustomUser, Subscriber


class CustomUserSerializers(UserSerializer):
    is_subscribed = SerializerMethodField()
    # recipe_count = SerializerMethodField()
    # recipe = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'email', 'id', 'username',
            'first_name', 'last_name', 'is_subscribed', 'recipes_count',
            'recipe',
            )

    def get_is_subscriber(self, subscriber):
        pass


class SubscriberSerializers(UserSerializer):
    """Получение списка подписок."""
    recipe_count = SerializerMethodField()
    recipe = SerializerMethodField()
    is_subscribed = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'email', 'id', 'username', 'first_name',
            'last_name', 'is_subscribed', 'recipes_count',
            'recipe',
        )
        read_only_fields = ('email', 'username', 'first_name', 'last_name')

    def add_subscriber():
        pass