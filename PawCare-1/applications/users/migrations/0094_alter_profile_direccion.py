# Generated by Django 3.2.8 on 2023-06-22 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0093_auto_20230621_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='direccion',
            field=models.TextField(null=True, verbose_name='Direccion'),
        ),
    ]
