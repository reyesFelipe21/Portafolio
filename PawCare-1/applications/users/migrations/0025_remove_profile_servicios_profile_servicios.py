# Generated by Django 4.2 on 2023-05-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='servicios',
        ),
        migrations.AddField(
            model_name='profile',
            name='servicios',
            field=models.ManyToManyField(to='users.tservicio', verbose_name='Tipos de servicios'),
        ),
    ]
