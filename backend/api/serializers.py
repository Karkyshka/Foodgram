from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from recipes.models import Ingredient, Recipe, Tag
from user.serializers import CustomUserSerializers
from user.models import CustomUser
from djoser.serializers import UserSerializer


class UserActionSerializer(UserSerializer):
    """Работа с действиями юзера"""
    class Meta:
        model = CustomUser
        fields = '__all__'

class TageSerializer(serializers.ModelSerializer):
    """Работа с тегми"""
    class Meta:
        model = Tag
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    """Работа с рецептами"""
    

    author = UserActionSerializer(read_only=True)


    ingredients = IngredientSerializer(many=True, read_only=True) 

    tags = TageSerializer(many=True, read_only=True)


    image = Base64ImageField()
    class Meta:
        model = Recipe
        fields = '__all__'






