from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Главная страница сайта. Содержимое главной — список
    первых шести рецептов, отсортированных по дате публикации
    «от новых к старым». На этой странице нужно реализовать
    постраничную пагинацию. Остальные рецепты должны быть
    доступны на следующих страницах."""
    class Meta:
        model = Recipe
        filed = '__all__'
