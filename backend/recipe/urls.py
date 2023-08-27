# Рецепты:
# http://localhost/api/recipes/ GET, PUT
# http://localhost/api/recipes/{id}/ GET, PUT, DEL

# Список покупок:
# http://localhost/api/recipes/download_shopping_cart/ GET
# http://localhost/api/recipes/{id}/shopping_cart/ POST, DEL

# Избранное:
# http://localhost/api/recipes/{id}/favorite/ POST, DEL
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<int:id>', views.recipes_detail, name='recipes_detail'),
    path('recipes/download_shopping_cart',
         views.download_shopping_cart,
         name='download_shopping_cart'),
    path('recipes/<int:id>/shopping_cart',
         views.shopping_cart,
         name='shopping_cart'),
    path('recipes/<int:id>/favorite', views.favorite, name='favorite')
]
