from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import IngredientViewSet, RecipeViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet, 'recipes')
router.register('tags', TagViewSet, 'tags')
router.register('ingredients', IngredientViewSet, 'ingredients')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('users/', include('djoser.urls.jwt')),
    path('users/', include('djoser.urls')),
]
