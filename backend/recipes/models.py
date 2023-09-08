from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

User = get_user_model()

class Ingredient(models.Model):
    """Список ингредиентов. Поиска по имени."""
    # Данные об ингредиентах должны храниться в нескольких связанных таблицах.
    name = models.CharField(
        'Ингредиент', max_length=200, null=True
      )
    measurement_unit = models.CharField(
        'Единицы измерения', max_length=200, null=True
      )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Cписок тегов. Поиск по тегу."""
    name = models.CharField(
        'Тег', max_length=200, unique=True
      )
    color = models.CharField(
        'Цвет', max_length=7, null=True, unique=True
      )
    slug = models.SlugField(
        'Слаг', max_length=200, unique=True, null=True
      )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Рецепты."""
    pub_date = models.DateTimeField(
        auto_now_add=True
      )
    tags = models.ManyToManyField(
        Tag, verbose_name='Теги', null=True
      )
    author = models.ForeignKey(
        User, verbose_name='Автор рецета',
        on_delete=models.CASCADE, related_name='recipes', null=True
      )
    # Ингредиенты. Множественное поле с выбором из предустановленного
    #  списка и с указанием количества и единицы измерения.
    ingredients = models.ManyToManyField(
        Ingredient,  through='IngredientRecipe',
        verbose_name='Ингредиенты', related_name='ingredients'
      )
    name = models.TextField(
        verbose_name='Название блюда', max_length=200, null=True
      )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время готовки', null=True,
        validators=[MinValueValidator(limit_value=1)]
      )
    text = models.TextField(
        verbose_name='Описание рецепта', null=True
      )
    image = models.ImageField(
        verbose_name='Фото блюда', upload_to='recipes/image/'
      )
    
    

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='ingredients_recipe',verbose_name='Рецепт'
      )
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE,
        related_name='ingredients_recipe', verbose_name='Ингредиент'
      )
    amount = models.IntegerField(
        verbose_name='Количество ингредиента', null=True
      )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'


class ShoppingCart(models.Model):
    pass