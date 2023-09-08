# Generated by Django 3.2 on 2023-09-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0025_alter_ingredientrecipe_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='amount',
            field=models.TextField(max_length=200, null=True, verbose_name='Количество ингредиента'),
        ),
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='measurement_unit',
            field=models.TextField(max_length=200, verbose_name='Единица измерения'),
        ),
    ]
