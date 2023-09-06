from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializers, SubscriberSerializers
from .models import CustomUser, Subscriber
from recipes.models import Recipe


User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializers
    # pagination_class = CustomUserPaginator

    @action(
        detail=False,
        permission_classes=[IsAuthenticated,]
    )   
    def subscriptions(self, request):
        user = request.user
        author = Subscriber.objects.filter(author=user).all()
        serializer = SubscriberSerializers(author)
        return Response (serializer.data)