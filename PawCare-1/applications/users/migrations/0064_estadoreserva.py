# Generated by Django 3.2.8 on 2023-06-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0063_auto_20230612_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoReserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reservaEstado', models.CharField(max_length=15)),
            ],
        ),
    ]
