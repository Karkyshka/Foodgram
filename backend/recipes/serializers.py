from rest_framework import serializers

from .models import Ingredient, Recipe, Tag


class RecipeSerializer(serializers.ModelSerializer):
    """Главная страница сайта. Содержимое главной — список
    первых шести рецептов, отсортированных по дате публикации
    «от новых к старым». На этой странице нужно реализовать
    постраничную пагинацию. Остальные рецепты должны быть
    доступны на следующих страницах."""
    class Meta:
        model = Recipe
        filed = '__all__'


class TageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        filed = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        filed = '__all__'
