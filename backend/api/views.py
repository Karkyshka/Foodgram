from rest_framework.viewsets import ModelViewSet

from recipes.models import Ingredient, Recipe, Tag
from user.models import CustomUser
from .serializers import IngredientSerializer, RecipeSerializer, TageSerializer, CustomUserSerializer



class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RecipeViewSet(ModelViewSet):
    # ReadOnlyModelViewSet
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # pagination_class = PageNumberPagination


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TageSerializer


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
