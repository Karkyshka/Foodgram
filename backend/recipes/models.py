from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

User = get_user_model()

class Fvorite(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')

  class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'object_id', 'content_type'],
                name='unique_user_content_type_object_id'
            )
        ]

class Ingredient(models.Model):
    """Список ингредиентов с возможностью поиска по имени."""
    name = models.CharField(
        verbose_name='Ингредиент', max_length=200, null=True
      )
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения', max_length=200, null=True
      )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество ингредиента', null=True
      )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Cписок тегов."""
    name = models.CharField(
        verbose_name='Тег', max_length=200
      )
    color = models.CharField(
        max_length=7, null=True
      )
    slug = models.CharField(
        unique=True, null=True, max_length=200
      )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Рецепты."""
    favorites = GenericRelation('Favorite')
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
    ingredients = models.ManyToManyField(
        Ingredient, verbose_name='Ингредиенты'
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
  
    is_in_shopping_cart = models.BooleanField()

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name
