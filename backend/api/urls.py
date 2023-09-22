from api.views import IngredientViewSet, RecipeViewSet, TagViewSet
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'api'

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet, 'recipes')
router.register('tags', TagViewSet, 'tags')
router.register('ingredients', IngredientViewSet, 'ingredients')


urlpatterns = [
    path('', include(router.urls)),
]
