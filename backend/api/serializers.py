from rest_framework.serializers import ModelSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import transaction
from recipes.models import Ingredient, Recipe, Tag, IngredientRecipe, Favorite
from user.serializers import CustomUserSerializers
from user.models import CustomUser
from djoser.serializers import UserSerializer


class TagSerializer(ModelSerializer):
    """Работа с тегми."""
    class Meta:
        model = Tag
        fields = '__all__'

class UserActionSerializer(UserSerializer):
    """Работа с действиями юзера"""
    
    class Meta:
        model = CustomUser
        fields = '__all__'

class IngredienSerializer(ModelSerializer):
    """Базовый сериализатор"""
    class Meta:
        model = Ingredient
        fields = '__all__'






class IngredientRecipeListSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    measurement_unit = serializers.CharField(read_only=True)
    
    class Meta:
        model = IngredientRecipe
        fields = ('id', 'name', 'measurement_unit', 'amount')

class RecipeListSerializer(ModelSerializer):
    """Получение рецетов"""
    tags = TagSerializer(many=True, read_only=True)
    author = CustomUserSerializers(read_only=True)
    ingredients = IngredientRecipeListSerializer(
        many=True, read_only=True, source='ingredientrecipe'
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
    
    def get_is_in_shopping_cart(self, ingredient):
        """Список покупок"""
        pass

    def get_is_favorited(self, recipe):
        request = self.context.get('request')
        favorite = (
            request and request.user.is_authenticated 
            and Favorite.objects.filter(
                user=request.user, recipe=recipe
                ).exists()
            )
        return favorite

class IngredientRecipeSerializer(ModelSerializer):
    """Добавление элемента."""
    id = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = IngredientRecipe
        fields = ('id', 'amount')


class RecipeActionializer(serializers.ModelSerializer):
    """Работа с рецептами. СОздание, редакторование"""
    # добавление ингедиентов работать перестало
    # не хваатет еще сериализаторов?
    ingredients = IngredientRecipeSerializer(
        many=True, source='ingredientrecipe'
    ) 
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'ingredients', 'tags', 'image', 'name', 'text', 'cooking_time'
        )


    def create_ingredient(self, recipe, ingredients):
        ingredient_set = []
        for ingredient in ingredients:
            ingredient_set.append(
                IngredientRecipe(ingredient=ingredient.pop('id')),
                amount = ingredient.pop('amount'), recipe=recipe)
            IngredientRecipe.objects.bulk_create(ingredient_set)

    def create(self, validated_data):
        """Добавление записей в связных таблицах"""
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        request = self.context.get('request')
        recipe = Recipe.objects.create(author=request.user, **validated_data)
        recipe.tags.set(tags)
        self.create_ingredient(recipe, ingredients)
        return recipe

    # Вынести в отдельную функцию?

    def update(self, instance, validated_data):
        """Изменение записей в связных таблицах"""
        instance.tags.clear()
        IngredientRecipe.objects.filter(recipe=instance).delete()
        instance.tags.set(validated_data.pop('tags'))
        ingredients = validated_data.pop('ingredients')
        self.create_ingredient(instance, ingredients)
        return super().update(instance, validated_data)
    
        # ingredients = validated_data.pop('ingredients')
        # tags = validated_data.pop('tags')
        
        # instance.tags.set(tags)
        
        # super().update(instance, validated_data)
        # ingredient_set = []
        # for ingredient in ingredients:
        #     current_ingredient = get_object_or_404(
        #         Ingredient,id=ingredient.get('id')
        #     )
        #     amount = ingredient.get('amount')
        #     ingredient_set.append(IngredientRecipe(
        #         recipe=instance, ingredient=current_ingredient, amount=amount)
        #     )
        #     IngredientRecipe.objects.bulk_create(ingredient_set)
        # return instance
        
    def to_representation(self, instance):
        return RecipeListSerializer(instance, context={
            'request': self.context.get('request')
        }).data





