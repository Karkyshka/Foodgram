# from django.contrib.auth import get_user_model
# from django.db.models import Count
from djoser.serializers import UserSerializer
from rest_framework.serializers import SerializerMethodField

from .models import CustomUser, Subscriber


class CustomUserSerializers(UserSerializer):
    is_subscribed = SerializerMethodField(read_only=True)
    # recipe_count = SerializerMethodField()
    # recipe = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'email', 'id', 'username',
            'first_name', 'last_name', 'is_subscribed'
        )

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        return Subscriber.objects.filter(
            follower=request.user, following=obj
        ).exists()


class SubscriberSerializers(UserSerializer):
    """Получение списка подписок."""
    # is_subscribed = SerializerMethodField(read_only=True)
    recipes_count = SerializerMethodField()
    recipes = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'email', 'id', 'username', 'first_name',
            'last_name', 'is_subscribed', 'recipes_count', 'recipes'
        )
        read_only_fields = ('email', 'username', 'first_name', 'last_name')

    # def get_is_subscribed(self, obj):
    #     request = self.context.get('request')
    #     return Subscriber.objects.filter(
    #         follower=request.user, following=obj
    #     ).exists()

    def get_recipes_count(self, obj):
        return obj.recipes.count()

    def get_recipes(self, obj):
        request
