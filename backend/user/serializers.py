from rest_framework import serializers

from .models import User


class CustomUserSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = '__all__'

