# Generated by Django 3.2 on 2023-09-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0024_auto_20230908_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='amount',
            field=models.CharField(max_length=200, null=True, verbose_name='Количество ингредиента'),
        ),
    ]
