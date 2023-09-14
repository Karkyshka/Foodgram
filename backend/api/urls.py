from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from api.views import IngredientViewSet, RecipeViewSet, TagViewSet

router = DefaultRouter()

# router.register('recipes', RecipeViewSet, basename='recipes')

# urlpatterns = [
#     path('recipes', RecipeViewSet, name='recipes')
# ]


app_name = 'api'

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet, 'recipes')
router.register('tags', TagViewSet, 'tags')
router.register('ingredients', IngredientViewSet, 'ingredients')


urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('djoser.urls.authtoken'))
    # path('api/', include('djoser.urls')),
    # path('api/', include('djoser.urls.authtoken')),
    # path('api/', include('djoser.urls.jwt')),
]
