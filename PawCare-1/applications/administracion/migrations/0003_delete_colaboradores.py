# Generated by Django 4.2 on 2023-05-30 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_alter_colaboradores_options_colaboradores_created'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Colaboradores',
        ),
    ]
