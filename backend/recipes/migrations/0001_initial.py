# Generated by Django 3.2 on 2023-08-29 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Ингредиент')),
                ('measurement_unit', models.CharField(max_length=3, verbose_name='Единицы измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, verbose_name='Тег')),
                ('color', models.CharField(max_length=7, null=True, verbose_name='Цвет тега')),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, verbose_name='Название блюда')),
                ('cooking_time', models.PositiveSmallIntegerField(verbose_name='Время готовки')),
                ('text', models.TextField(verbose_name='Описание рецепта')),
                ('image', models.ImageField(upload_to='')),
                ('is_favorited', models.BooleanField()),
                ('is_in_shopping_cart', models.BooleanField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор рецета')),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient', verbose_name='Ингредиенты')),
                ('tags', models.ManyToManyField(to='recipes.Tag', verbose_name='Теги')),
            ],
        ),
    ]
