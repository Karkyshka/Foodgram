from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.serializers import SlugRelatedField
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializers, SubscriberSerializers
from .models import CustomUser, Subscriber
from recipes.models import Recipe
from django.shortcuts import get_object_or_404, redirect, render
from recipes.models import Recipe
from django.db.models import Count

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializers

    @action(
            detail=False,
            permission_classes=[IsAuthenticated]
        )
    def subscription(self, request):
        """Просмотр ленты подписок.
        Авторизация по токену. Все запросы от имени пользователя должны 
        выполняться с заголовком Authorization: Token TOKENVALUE"""
        pass

    @action(
            methods=['POST', 'DELETE'],
            detail=True,
            permission_classes=[IsAuthenticated]
        )
    def update_subscriber(self, request):
        """Обновление статуса подписчика.
        Авторизация по токену. Все запросы от имени пользователя должны 
        выполняться с заголовком Authorization: Token TOKENVALUE"""
        pass