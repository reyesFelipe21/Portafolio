# Generated by Django 3.2.8 on 2023-06-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0081_reservacliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='promediocalificacion',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]