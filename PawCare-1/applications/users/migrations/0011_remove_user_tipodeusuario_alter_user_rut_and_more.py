# Generated by Django 4.2 on 2023-05-17 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tipodeusuario',
        ),
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]
