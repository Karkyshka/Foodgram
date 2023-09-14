from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag)


@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name', 'author')


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    pass


@admin.register(IngredientRecipe)
class IngredientRecipe(ImportExportModelAdmin):
    pass
    # list_display = ('pk', 'recipe', 'ingrediens', 'amount')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')
