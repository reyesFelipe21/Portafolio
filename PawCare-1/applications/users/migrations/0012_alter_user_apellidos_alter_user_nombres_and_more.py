# Generated by Django 4.2 on 2023-05-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_user_tipodeusuario_alter_user_rut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apellidos',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombres',
            field=models.CharField(max_length=100),
        ),
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