from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    pass

