# Generated by Django 3.2.8 on 2023-06-13 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0073_auto_20230612_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
