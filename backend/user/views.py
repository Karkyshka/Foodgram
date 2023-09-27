from api.permission import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser, Subscriber
from .pagination import CustomPagination
from .serializers import CustomUserSerializers, SubscriberSerializers


class CustomUserViewSet(UserViewSet):
    queryset = CustomUser.objects.select_related('auth_token').all()
    serializer_class = CustomUserSerializers
    pagination_class = CustomPagination
    permission_classes = (IsOwnerOrReadOnly,)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def subscriptions(self, request):
        """Просмотр ленты подписок."""
        user = request.user
        queryset = CustomUser.objects.prefetch_related(
            'auth_token').filter(following__follower=user)
        page = self.paginate_queryset(queryset)
        serializes = SubscriberSerializers(
            page, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializes.data)

    @action(methods=['POST', 'DELETE'],
            detail=True, permission_classes=[IsAuthenticated])
    def subscribe(self, request, id):
        """Обновление статуса подписчика."""
        follower = request.user
        following = get_object_or_404(CustomUser, pk=id)

        if request.method == 'POST':
            serialaizer = SubscriberSerializers(
                following, data=request.data, context={'request': request}
            )
            serialaizer.is_valid()
            Subscriber.objects.create(follower=follower, following=following)
            return Response(serialaizer.data, status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            get_object_or_404(
                Subscriber, follower=follower, following=following
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
