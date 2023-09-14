# from django.contrib.auth import get_user_model
# from django.db.models import Count
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from djoser.serializers import UserSerializer
# from rest_framework import status
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from recipes.models import Recipe

from .models import CustomUser, Subscriber


class RecipeSerializers(ModelSerializer):
    """Отображение рецептов в подписках"""
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class CustomUserSerializers(UserSerializer):
    is_subscribed = SerializerMethodField()

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
    recipes_count = SerializerMethodField()
    recipes = SerializerMethodField()
    is_subscribed = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'email', 'id', 'username', 'first_name',
            'last_name', 'is_subscribed', 'recipes', 'recipes_count'
        )
        # read_only_fields = ('email', 'username', 'first_name', 'last_name')
        #     following_id = self.context.get(
        #         'request').parser_context.get('kwargs').get('id')
        #     following = get_object_or_404(CustomUser, id=following_id)
        #     user = self.context.get('request').user
        #     if user.follower.filter(following=following_id).exists():
        #         raise ValidationError('Вы уже подписаны на автора')
        #     if user == following:
        #         raise ValidationError('Нельзя подписаться на самого себя')
        #     return data

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
        return RecipeSerializers(
            recipes, many=True, context={'request': request}
        ).data
