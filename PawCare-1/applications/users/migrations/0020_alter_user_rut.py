# Generated by Django 4.2 on 2023-05-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_user_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(max_length=9),
        ),
    ]
