# Generated by Django 3.2 on 2023-08-31 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=254, verbose_name='Адрес электронной почты'),
        ),
    ]