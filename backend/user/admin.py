from django.contrib import admin

from .models import CustomUser, Subscriber

# admin.site.register(CustomUser)

from django.contrib import admin
from django.contrib.auth import get_user_model

# User = get_user_model()


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'email',
        'first_name', 'last_name', 'password',
        )
    search_fields = ('email', 'username', 'first_name', 'last_name')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'follower', 'following',
    )
