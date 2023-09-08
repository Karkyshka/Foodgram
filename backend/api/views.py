from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import AllowAny

from recipes.models import Recipe, Ingredient, Tag
from api.serializers import RecipeListSerializer, RecipeActionializer


class RecipeViewSet(ModelViewSet):
    """Работа с рецептами.
    При сериализации не записывает при POST и PATCH:
    - "ingredients": [],
    - "is_in_shopping_cart": null,
    - "is_favorited": null"""
    queryset = Recipe.objects.select_related('author').all()
    # serializer_class = RecipeListSerializer

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RecipeListSerializer
        return RecipeActionializer



class TagViewSet(ReadOnlyModelViewSet):
    """Информация о тегах"""
    queryset = Tag.objects.all()
    # serializer_class = TagSerializer
    permission_classes = [AllowAny]


class IngredientViewSet(ReadOnlyModelViewSet):
    """Информация об ингредиентах."""
    queryset = Ingredient.objects.all()
    # serializer_class = IngredientSerializer
    permission_classes = [AllowAny]
    # filter_backends = [DjangoFilterBackend]
























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
