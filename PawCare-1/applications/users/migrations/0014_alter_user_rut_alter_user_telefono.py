# Generated by Django 4.2 on 2023-05-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_rut_alter_user_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.CharField(max_length=9),
        ),
    ]
