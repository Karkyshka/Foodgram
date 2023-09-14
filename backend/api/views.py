from api.serializers import (FavoriteSerializer, IngredienSerializer,
                             RecipeActionializer, RecipeListSerializer,
                             ShoppingCartSerializer, TagSerializer,
                             RecipeSerializer)
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from recipes.models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                            ShoppingCart, Tag)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from .filter import IngredientFilter, RecipeFilter
from .permission import AuthorPermission
from django.db.models import Sum


class RecipeViewSet(ModelViewSet):
    """Работа с рецептами.
    Получение списка рецептов.
    Создание и редактирование объекта.
    Добавлние в избранное/корзину.
    отправка файла."""
    queryset = Recipe.objects.select_related('author').all()
    serializer_class = RecipeActionializer
    permission_classes = [AuthorPermission]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RecipeListSerializer
        return RecipeActionializer

    @action(methods=['GET'], detail=False)
    def download_shopping_cart(self, request):
        """Скачать файл со списком покупок."""
        shopping_cart = 'Список покупок:'
        ingredients = IngredientRecipe.objects.filter(
            recipe__shoppingcart__user=request.user).values(
                'ingredient__name', 'ingredient__measurement_unit'
            ).annotate(amount=Sum('amount'))
        # не отображается сам список
        return Response(shopping_cart, content_type='text/plain')

    @action(methods=['post', 'delete'], detail=True)
    def shopping_cart(self, request, pk):
        """Добавление, удаление в список покупок."""
        if request.method == 'POST':
            recipe = get_object_or_404(Recipe, id=pk)
            context = {'request': request}
            data = {
                'user': request.user.id,
                'recipe': recipe.id
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
    def favorite(self, request, pk):
        """Добавление, удаление в избранное."""
        if request.method == 'POST':
            recipe = get_object_or_404(Recipe, id=pk)
            context = {'request': request}
            data = {
                'user': request.user.id,
                'recipe': recipe.id
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None


class IngredientViewSet(ReadOnlyModelViewSet):
    """Информация об ингредиентах."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredienSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [IngredientFilter]
    search_fields = ('^name', )
    pagination_class = None
























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
