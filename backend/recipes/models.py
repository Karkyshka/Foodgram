from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ingredient(models.Model):
    """Список ингредиентов с возможностью поиска по имени."""
    name = models.CharField(verbose_name = 'Ингредиент', max_length=10)
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения',max_length=3
      )
    
    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name', ) 

class Tag(models.Model):
    """Cписок тегов."""
    name = models.TextField(verbose_name= 'Тег', max_length=200)
    color = models.CharField(
        max_length=7, null=True
      )
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Recipe(models.Model):
    """Рецепты. Страница доступна всем пользователям.
    Доступна фильтрация по избранному, автору, списку покупок и тегам."""
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    author = models.ForeignKey(
        User, verbose_name='Автор рецета',
        on_delete=models.CASCADE, related_name='recipes'
      )
    ingredients = models.ManyToManyField(
        Ingredient, verbose_name='Ингредиенты'
      )
    name = models.TextField(verbose_name='Название блюда', max_length=200)
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время готовки'
      )
    text = models.TextField(verbose_name='Описание рецепта')
    image = models.ImageField()
    is_favorited = models.BooleanField()
    is_in_shopping_cart = models.BooleanField()

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
