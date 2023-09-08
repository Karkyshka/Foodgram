from rest_framework.serializers import ModelSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from django.shortcuts import get_object_or_404

from recipes.models import Ingredient, Recipe, Tag, IngredientRecipe
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



class IngredientSerializer(ModelSerializer):
    """Работа с ингедиентами."""
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeListSerializer(ModelSerializer):
    """Получение списка рецетов"""
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()


    ingredients = IngredientSerializer(many=True, read_only=True)
    author = CustomUserSerializers(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    image = Base64ImageField()
    class Meta:
        model = Recipe
        fields = (
            'tags', 'author', 'ingredients', 'name', 'cooking_time',
            'image', 'text', 'amount', 'id', 'is_favorited',
            'is_in_shopping_cart'
        )
    
    def get_is_in_shopping_cart(self, ingredient):
        """Список покупок"""
        pass

    def get_is_favorited(self,favorited):
        pass

class RecipeActionializer(serializers.ModelSerializer):
    """Работа с рецептами"""
    ingredients = IngredientSerializer(many=True) 
    tags = TagSerializer(many=True, read_only=True)
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'tags', 'ingredients', 'name', 'image', 'text', 'cooking_time'
            )

    def create(self, validated_data):
        """Изменение записей в связных таблицах"""
        # request = self.context.get('request')
        # tag = Tag.objects.create()
        # ingredients = Tag.objects.create()
        # recipe.tags.set(tag, ingredients)
        # recipe = Recipe.objects.create(author=request.user, **validated_data)
        # return recipe
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        request = self.context.get('request')
        recipe = Recipe.objects.create(author=request.user, **validated_data)
        recipe.tags.set(tags)
        ingredient_set = []
        for ingredient in ingredients:
            current_ingredient = get_object_or_404(
                Ingredient,id=ingredient.get('id')
            )
            ingredient_set.append(IngredientRecipe(recipe=recipe, ingredient=current_ingredient, tags=tags))
        return recipe 
        
    





