# Generated by Django 3.2.8 on 2023-06-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0079_alter_cronograma_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tipodeusuario',
            field=models.CharField(choices=[('0', 'Administrador'), ('1', 'Cliente'), ('2', 'Cuidador')], max_length=2, null=True),
        ),
    ]
