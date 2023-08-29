from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from recipes.views import RecipeViewSet


router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)


urlpatterns = [
    path('recipes/', include(router.urls)),
    path('admin/', admin.site.urls),
]
