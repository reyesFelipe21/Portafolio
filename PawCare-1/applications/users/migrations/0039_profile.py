# Generated by Django 4.2 on 2023-05-29 00:51

import applications.users.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_merge_0019_alter_user_categoria_0037_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('picture', models.ImageField(default='users/user_default_profile.png', upload_to=applications.users.models.user_directory_path_profile)),
                ('descripcion', models.TextField(blank=True, max_length=2000, null=True)),
                ('servicios', models.ManyToManyField(related_name='servicios', to='users.servicio', verbose_name='Tipos de servicios')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
