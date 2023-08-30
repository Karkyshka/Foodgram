# Список покупок:
# http://localhost/api/recipes/download_shopping_cart/ GET
# http://localhost/api/recipes/{id}/shopping_cart/ POST, DEL

# Избранное:
# http://localhost/api/recipes/{id}/favorite/ POST, DEL
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RecipeViewSet

router = DefaultRouter()

router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('recipes', RecipeViewSet, name='recipes')
]


from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import IngredientViewSet, RecipeViewSet, TagViewSet, CustomUserViewSet


app_name = 'api'

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet, 'recipes')
router.register('tags', TagViewSet, 'tags')
router.register('ingredients', IngredientViewSet, 'ingredients')
router.register('users', CustomUserViewSet, 'users')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken'))
   # path('api/', include('djoser.urls')),
   # path('api/', include('djoser.urls.authtoken')),
    # path('api/', include('djoser.urls.jwt')),
]
