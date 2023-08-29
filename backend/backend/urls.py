from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from recipes.views import IngredientViewSet, RecipeViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet, 'recipes')
router.register('tags', TagViewSet, 'tag')
router.register('ingredients', IngredientViewSet, 'ingredient')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
]
