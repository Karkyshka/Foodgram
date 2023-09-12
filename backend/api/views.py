from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework import status

from recipes.models import Recipe, Ingredient, Tag, Favorite, IngredientRecipe, ShoppingCart
from api.serializers import (TagSerializer, RecipeListSerializer,
                             RecipeActionializer, IngredienSerializer,
                             FavoriteSerializer, ShoppingCartSerializer)


class RecipeViewSet(ModelViewSet):
    """Работа с рецептами.
    Получение списка рецептов.
    Создание и редактирование объекта.
    Добавлние в избранное/корзину.
    отправка файла."""
    queryset = Recipe.objects.select_related('author').all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RecipeListSerializer
        return RecipeActionializer

    @action(methods=['get'], detail=False)
    def download_shopping_cart(self, request):
        """Скачать файл со списком покупок."""
        pass

    @action(methods=['post', 'delete'], detail=True)
    def shopping_cart(self, request, pk):
        """Добавление, удаление в список покупок."""
        if request.method == 'POST':
            recipe = get_object_or_404(Recipe, id=pk)
            context = {'request': request}
            data = {
                'user': request.user.id,
                'recipe' : recipe.id
            }
            serializer = ShoppingCartSerializer(context=context, data=data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == "DELETE":
            recipe = get_object_or_404(Recipe, id=pk)
            get_object_or_404(
                ShoppingCart, user=request.user, recipe=recipe).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post', 'delete'], detail=True)
    # FavoriteSerializer
    def favorite(self, request, pk):
        """Добавление, удаление в избранное"""  
        if request.method == 'POST':
            recipe = get_object_or_404(Recipe, id=pk)
            context = {'request': request}
            data = {
                'user': request.user.id,
                'recipe' : recipe.id
            }
            serializer = FavoriteSerializer(context=context, data=data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == "DELETE":
            recipe = get_object_or_404(Recipe, id=pk)
            get_object_or_404(
                Favorite, user=request.user, recipe=recipe).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class TagViewSet(ReadOnlyModelViewSet):
    """Информация о тегах"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class IngredientViewSet(ReadOnlyModelViewSet):
    """Информация об ингредиентах."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredienSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
























# from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.decorators import action

# from recipes.models import Ingredient, Recipe, Tag
# from api.serializers import IngredientSerializer, RecipeActionializer, TagSerializer, RecipeListSerializer

# class RecipeActionViewSet(ModelViewSet):
#     """Работа с рецептами"""
#     queryset = Recipe.objects.select_related('author').all()
#     # serializer_class = RecipeListSerializer
#     filter_backends = [DjangoFilterBackend]
#     permission_classes = (IsAuthenticated,)
#     # pagination_class = PageNumberPagination

#     def get_serializer_class(self):
#         if self.action in ('list', 'retrieve'):
#             return RecipeListSerializer
#         return RecipeActionializer
    
#     @action(
#         methods=['post', 'delete'], detail=False,
#         permission_classes=IsAuthenticated
#     )
#     def shopping_cart():
#         pass

#     @action(
#         methods=['get'], detail=False,
#         permission_classes=IsAuthenticated
#     )
#     def download_shopping_cart():
#         pass
    


# class RecipeViewSet(ModelViewSet):
#     """Работа со списком рецептов"""
#     queryset = Recipe.objects.select_related('author').all()
#     serializer_class = RecipeListSerializer
#     filter_backends = [DjangoFilterBackend]
#     permission_classes = [IsAuthenticated]
#     # pagination_class = PageNumberPagination

# class TagViewSet(ReadOnlyModelViewSet):
#     """Информация о тегах"""
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = [AllowAny]


# class IngredientViewSet(ReadOnlyModelViewSet):
#     """Информация об ингредиентах."""
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
#     permission_classes = [AllowAny]
#     filter_backends = [DjangoFilterBackend]
