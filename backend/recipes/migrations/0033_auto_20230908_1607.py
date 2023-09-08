# Generated by Django 3.2 on 2023-09-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0032_recipe_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='amount',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.IntegerField(null=True, verbose_name='Количество ингредиента'),
        ),
    ]
