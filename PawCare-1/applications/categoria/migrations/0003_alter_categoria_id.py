# Generated by Django 4.2 on 2023-05-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0002_alter_categoria_name_alter_categoria_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
