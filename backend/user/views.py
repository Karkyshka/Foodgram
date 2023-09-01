from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializers


User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializers
    # pagination_class = CustomUserPaginator
