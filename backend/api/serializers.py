from django.db import transaction
from django.shortcuts import get_object_or_404
from djoser.serializers import UserSerializer
from drf_extra_fields.fields import Base64ImageField
from recipes.models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                            ShoppingCart, Tag)
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user.models import CustomUser
from user.serializers import CustomUserSerializers


class RecipeSerializer(serializers.ModelSerializer):
    """Работа с рецептами.
    Избранное."""

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class TagSerializer(ModelSerializer):
    """Работа с тегми. Используется в тегах."""
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class UserActionSerializer(UserSerializer):
    """Работа с действиями юзера"""
    class Meta:
        model = CustomUser
        fields = '__all__'


class IngredienSerializer(ModelSerializer):
    """Базовый сериализатор. Используется в ингредиентах."""
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class FavoriteSerializer(ModelSerializer):
    """Работа с избранными рецептами"""
    class Meta:
        model = Favorite
        fields = '__all__'

    def validate(self, data):
        user = data['user']
        if user.favorite.filter(recipe=data['recipe']).exists():
            raise serializers.ValidationError('Рецепт уже в избранном')
        return data

    def to_representation(self, instance):
        return RecipeSerializer(
            instance.recipe,
            context={'request': self.context.get('request')}
        ).data


class ShoppingCartSerializer(ModelSerializer):
    """Работа со списком покупок"""
    class Meta:
        model = ShoppingCart
        fields = ('user', 'recipe')

    def to_representation(self, instance):
        return RecipeSerializer(
            instance.recipe,
            context={'request': self.context.get('request')}
        ).data

    def validate(self, data):
        user = data['user']
        if user.shoppingcarts.filter(recipe=data['recipe']).exists():
            raise serializers.ValidationError('Рецепт уже в корзине')
        return data


class IngredientRecipeListSerializer(ModelSerializer):
    """Ингредиенты в рецептах"""
    id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(), source='ingredient.id'
    )
    name = serializers.CharField(
        source='ingredient.name', read_only=True
    )
    measurement_unit = serializers.CharField(
        source='ingredient.measurement_unit', read_only=True
    )

    class Meta:
        model = IngredientRecipe
        fields = ('id', 'name', 'measurement_unit', 'amount')


class RecipeListSerializer(ModelSerializer):
    """Получение рецетов"""
    tags = TagSerializer(many=True, read_only=True)
    author = CustomUserSerializers(read_only=True)
    ingredients = IngredientRecipeListSerializer(
        many=True, source='ingredientrecipes'
    )
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients', 'is_favorited',
            'is_in_shopping_cart', 'name', 'image', 'text', 'cooking_time'
        )

    def get_is_in_shopping_cart(self, obj):
        """Список покупок"""
        request = self.context.get('request')
        if request is None or request.user.is_anonymous:
            return False
        return obj.shoppingcarts.filter(user=request.user).exists()

    def get_is_favorited(self, obj):
        """Избранное"""
        request = self.context.get('request')
        if request is None or request.user.is_anonymous:
            return False
        return obj.favorite.filter(user=request.user).exists()


class IngredientRecipeSerializer(ModelSerializer):
    """Добавление элемента."""
    id = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = Ingredient
        fields = ('id', 'amount',)


class IngredientsInResipeSerializer(ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        source='ingredient',
        queryset=Ingredient.objects.all()
    )
    recipe = serializers.PrimaryKeyRelatedField(read_only=True)
    amount = serializers.IntegerField(write_only=True)

    class Meta:
        model = IngredientRecipe
        fields = ('recipe', 'id', 'amount')


class RecipeActionializer(serializers.ModelSerializer):
    """Работа с рецептами. Создание, редакторование"""
    ingredients = IngredientsInResipeSerializer(many=True)
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )
    image = Base64ImageField()
    author = UserSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'ingredients', 'tags', 'image', 'author', 'text',
            'cooking_time', 'name'
        )

    def validate_ingredients(self, data):
        ingredients = self.initial_data.get('ingredients')
        if not ingredients:
            raise serializers.ValidationError({
                'ingredients': 'Нужен хоть один ингридиент для рецепта'})
        ingredient_list = []
        for ingredient_item in ingredients:
            ingredient = get_object_or_404(
                Ingredient, id=ingredient_item['id']
            )
            if ingredient in ingredient_list:
                raise serializers.ValidationError(
                    'Ингредиенты должны быть уникальными'
                )
            ingredient_list.append(ingredient)
            if int(ingredient_item['amount']) < 1:
                raise serializers.ValidationError({
                    'ingredients': ('Убедитесь, что значение количества '
                                    'ингредиента больше 1')
                })
        return data

    @transaction.atomic
    def create(self, validated_data):
        """Добавление записей в связных таблицах"""
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)
        create_ingredients = [
            IngredientRecipe(
                ingredient=ingredient['ingredient'],
                recipe=recipe,
                amount=ingredient['amount']
            )
            for ingredient in ingredients
        ]
        IngredientRecipe.objects.bulk_create(create_ingredients)
        return recipe

    @transaction.atomic
    def update(self, instance, validated_data):
        """Изменение записей в связных таблицах"""
        tags = validated_data.pop('tags')
        ingredients = validated_data.pop('ingredients')
        if tags is not None:
            instance.tags.set(tags)
        if ingredients is not None:
            instance.ingredients.clear()
        create_ingredients = [
            IngredientRecipe(
                ingredient=ingredient['ingredient'],
                recipe=instance,
                amount=ingredient['amount']
            )
            for ingredient in ingredients
        ]
        IngredientRecipe.objects.bulk_create(create_ingredients)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return RecipeListSerializer(instance, context={
            'request': self.context.get('request')
        }).data
