from rest_framework.serializers import ModelSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

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
    ingredients = IngredientSerializer(many=True, read_only=True)
    author = CustomUserSerializers(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()
    image = Base64ImageField()
    class Meta:
        model = Recipe
        fields = (
            'tags', 'author', 'ingredients', 'name', 'cooking_time',
            'image', 'text', 'amount', 'id', 'is_favorited', 'is_in_shopping_cart'
        )
    
    def create(self, validated_data):
        """Изменение записей в связных таблицах"""
        # Уберем список достижений из словаря validated_data и сохраним его
        ingredients_recipe = validated_data.pop('ingredients_recipe')

        # Создадим нового котика пока без достижений, данных нам достаточно
        recipe = Recipe.objects.create(**validated_data)

        # Для каждого достижения из списка достижений
        for ingredient in ingredients:
            # Создадим новую запись или получим существующий экземпляр из БД
            current_ingredients, status = Ingredient.objects.get_or_create(
                **ingredient)
            # Поместим ссылку на каждое достижение во вспомогательную таблицу
            # Не забыв указать к какому котику оно относится
            IngredientRecipe.objects.create(
                ingredients=current_ingredients, recipe=recipe)
        return recipe 
    
    def get_is_in_shopping_cart(self, ingredient):
        """Список покупок"""
        pass

    def get_is_favorited(self,favorited):
        pass

class RecipeActionializer(serializers.ModelSerializer):
    """Работа с рецептами"""
    author = UserActionSerializer(read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True) 
    tags = TagSerializer(many=True, read_only=True)
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients',
            'name', 'image', 'text', 'cooking_time'
            )

    





