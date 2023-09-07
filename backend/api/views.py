from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action

from recipes.models import Ingredient, Recipe, Tag
from .serializers import IngredientSerializer, RecipeSerializer, TageSerializer
from django.shortcuts import get_object_or_404


class RecipeViewSet(ModelViewSet):
    """Работа с рецептами"""
    queryset = Recipe.objects.select_related('author').all()
    serializer_class = RecipeSerializer
    # filter_backends = [DjangoFilterBackend]
    # permission_classes = (IsAuthenticatedOrReadOnly)
    # pagination_class = PageNumberPagination

    
    @action(
        methods=['post', 'delete'], detail=False,
        permission_classes=IsAuthenticated
    )
    def favorite():
        pass

    @action(methods=['post', 'delete'], detail=False)
    def shopping_cart():
        pass

    @action(detail=False)
    def download_shopping_cart():
        pass
    




class TagViewSet(ModelViewSet):
    """Информация о тегах"""
    queryset = Tag.objects.all()
    serializer_class = TageSerializer


class IngredientViewSet(ModelViewSet):
    """Информация об ингредиентах"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
