# Generated by Django 3.2.8 on 2023-06-21 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0092_comuna_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='comuna',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comuna', to='users.comuna'),
        ),
        migrations.AddField(
            model_name='profile',
            name='direccion',
            field=models.CharField(max_length=100, null=True, verbose_name='Direccion'),
        ),
        migrations.AddField(
            model_name='profile',
            name='region',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Region', to='users.region'),
        ),
    ]
