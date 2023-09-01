from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser):
    """Определеяет пользовательскую модель"""
    email = models.EmailField(
        verbose_name='Адрес электронной почты', max_length=254, unique=True,
    )
    username = models.CharField(
        verbose_name='Уникальный юзернейм', max_length=150, unique=True,
    )

    password = models.CharField(
        verbose_name='Пароль', max_length=150
    )

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', ]
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def token(self):
        """Позволяет нам получить токен пользователя, вызвав `user.token`
        вместо user.generate_jwt_token()."""
        return self._generate_jwt_token()