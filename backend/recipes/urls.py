# Рецепты:
# http://localhost/recipes/ GET, PUT
# http://localhost/api/recipes/{id}/ GET, PUT, DEL

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
