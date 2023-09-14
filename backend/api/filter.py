from django_filters import FilterSet

from recipes.models import Ingredient


class IngredientFilter(FilterSet):
    search_param = 'name'

    class Meta:
        model = Ingredient
        fields = ('name',)