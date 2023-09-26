from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.db import models

from user.models import CustomUser


class Ingredient(models.Model):
    """Список ингредиентов. Поиска по имени."""
    name = models.CharField(
        'Ингредиент', max_length=200
    )
    measurement_unit = models.CharField(
        'Единицы измерения', max_length=200
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
    color = ColorField(
        verbose_name='HEX-код',
        max_length=7, unique=True
    )
    slug = models.SlugField(
        'Слаг', max_length=200, unique=True
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
        Tag, verbose_name='Теги', related_name='recipes',
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name='Автор рецета',
        related_name='recipes'
    )
    ingredients = models.ManyToManyField(
        # Всем связным полям лучше задать related_name
        Ingredient, through='IngredientRecipes', related_name='recipes',
        verbose_name='Ингредиенты'
    )
    name = models.CharField(
        verbose_name='Название блюда', max_length=200
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время готовки',
        validators=[MinValueValidator(limit_value=1)]
    )
    text = models.TextField(
        verbose_name='Описание рецепта'
    )
    image = models.ImageField(
        verbose_name='Фото блюда', upload_to='recipes/image/', blank=True
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date']
        default_related_name = 'recipes'

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='ingredientrecipes', verbose_name='Рецепт'
    )
    # related_name лучше делать во мн. ч.
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE,
        related_name='ingredientrecipes', verbose_name='Ингредиент'
    )
    amount = models.IntegerField(
        verbose_name='Количество ингредиента',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'
        default_related_name = 'ingredientrecipes'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='shoppingcarts'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='shoppingcarts'
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        default_related_name = 'shoppingcarts'

    def __str__(self):
        return (f'{self.recipe.name} добавлен в список покупок')


class Favorite(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='favorite'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favorite'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        default_related_name = 'favorite'

    def __str__(self):
        return f'{self.recipe.name} в избранном'
