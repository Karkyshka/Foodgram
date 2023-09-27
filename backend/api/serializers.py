from djoser.serializers import UserSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from recipes.models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                            ShoppingCart, Tag)
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
        queryset=Ingredient.objects.all()
    )
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit'
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


class RecipeActionializer(serializers.ModelSerializer):
    """Работа с рецептами. Создание, редакторование"""
    ingredients = IngredientRecipeSerializer(many=True)
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )
    image = Base64ImageField()
    author = UserSerializer(read_only=True)
    cooking_time = serializers.IntegerField()

    class Meta:
        model = Recipe
        fields = (
            'ingredients', 'tags', 'image', 'author', 'text',
            'cooking_time', 'name'
        )

    def create_ingredient(self, ingredients, recipe):
        for ingredient in ingredients:
            IngredientRecipe.objects.create(
                recipe=recipe,
                ingredient_id=ingredient.get('id'),
                amount=ingredient.get('amount'), )

    def create(self, validated_data):
        """Добавление записей в связных таблицах"""
        request = self.context.get('request')
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(author=request.user, **validated_data)
        recipe.tags.set(tags)
        self.create_ingredient(ingredients, recipe)
        return recipe

    def update(self, instance, validated_data):
        """Изменение записей в связных таблицах"""
        instance.tags.clear()
        IngredientRecipe.objects.filter(recipe=instance).delete()
        instance.tags.set(validated_data.pop('tags'))
        ingredients = validated_data.pop('ingredients')
        self.create_ingredient(ingredients, instance)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return RecipeListSerializer(instance, context={
            'request': self.context.get('request')
        }).data
