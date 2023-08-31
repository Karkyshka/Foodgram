from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Ingredient, Recipe, Tag


@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    pass
