from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializers, SubscriberSerializers
from .models import CustomUser, Subscriber


# User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
    # pagination_class = CustomUserPaginator


class Subscriber(ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializers