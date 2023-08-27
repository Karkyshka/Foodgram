from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ingredient(models.Model):
    ...


class Tag(models.Model):
    ...


class Recipe(models.Model):
    """Рецепты. Страница доступна всем пользователям.
    Доступна фильтрация по избранному, автору, списку покупок и тегам."""
    # ingredients = models.ForeignKey('Ingredient', on_delete=models.SET_NULL)
    # tags = models.ForeignKey('Tag', on_delete=models.SET_NULL)
    # image = models.ImageField('Картинка')
    name = models.TextField()
    text = models.TextField()
    cooking_time = models.TimeField()
