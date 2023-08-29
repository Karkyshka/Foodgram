# Рецепты:
# http://localhost/recipes/ GET, PUT
# http://localhost/api/recipes/{id}/ GET, PUT, DEL

# Список покупок:
# http://localhost/api/recipes/download_shopping_cart/ GET
# http://localhost/api/recipes/{id}/shopping_cart/ POST, DEL

# Избранное:
# http://localhost/api/recipes/{id}/favorite/ POST, DEL
from django.urls import path

from . import views

urlpatterns = [
    path('', views.RecipeViewSet, name='recipes')
]
