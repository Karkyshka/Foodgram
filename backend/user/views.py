# from django.contrib.auth import get_user_model
# from django.db.models import Count
# from django.shortcuts import get_object_or_404, redirect, render
from djoser.views import UserViewSet
# from recipes.models import Recipe
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.serializers import SlugRelatedField
# from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .serializers import CustomUserSerializers, SubscriberSerializers


class CustomUserViewSet(UserViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
    #  pagination_class

    @action(detail=False, permission_classes=[IsAuthenticated])
    # GET http://localhost/api/users/subscriptions/
    def subscriptions(self, request):
        """Просмотр ленты подписок."""
        user = request.user
        queryset = CustomUser.objects.filter(following__follower=user)
        page = self.paginate_queryset(queryset)
        serializes = SubscriberSerializers(
            page, many=True, context={'request': request}
            )
        return self.get_paginated_response(serializes.data)

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
