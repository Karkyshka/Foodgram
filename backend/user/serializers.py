from api import serializers
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from djoser.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import CustomUser, Subscriber


class CustomUserSerializers(UserSerializer):
    is_subscribed = SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request is None or request.user.is_anonymous:
            return False
        return Subscriber.objects.filter(
            follower=request.user, following=obj
        ).exists()


class SubscriberSerializers(UserSerializer):
    """Получение списка подписок."""
    recipes_count = SerializerMethodField()
    recipes = SerializerMethodField()
    is_subscribed = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'email', 'id', 'username', 'first_name',
            'last_name', 'is_subscribed', 'recipes', 'recipes_count'
        )

        def validate(self, data):
            following_id = self.context.get(
                'request').parser_context.get('kwargs').get('id')
            request = self.context.get('request')
            follower = request.user
            following = get_object_or_404(CustomUser, id=following_id)
            if request.method == 'POST':
                if Subscriber.objects.filter(
                    follower=follower, following=following
                ):
                    raise ValidationError('Вы уже подписаны на этого автора')
            return data

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        return Subscriber.objects.filter(
            follower=request.user, following=obj
        ).exists()

    def get_recipes_count(self, obj):
        return obj.recipes.count()

    def get_recipes(self, obj):
        request = self.context.get('request')
        recipes_limit = None
        if request:
            recipes_limit = request.query_params.get('recipes_limit')
        recipes = obj.recipes.all()
        if recipes_limit:
            recipes = obj.recipes.all()[:int(recipes_limit)]
        return serializers.RecipeSerializer(
            recipes, many=True, context={'request': request}
        ).data
