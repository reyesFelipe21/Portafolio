# Generated by Django 3.2.8 on 2023-06-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0083_alter_user_tipodeusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tipodeusuario',
        ),
        migrations.AlterField(
            model_name='user',
            name='categoria',
            field=models.CharField(choices=[('1', 'Administrador'), ('2', 'Cliente'), ('3', 'Cuidador')], default=2, max_length=2, null=True),
        ),
    ]
