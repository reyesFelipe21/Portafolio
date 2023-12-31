# Generated by Django 4.2 on 2023-05-30 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_alter_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nombre del Patrocinador')),
                ('image', models.ImageField(blank=True, null=True, upload_to='colaboradores', verbose_name='Imagen del Patrocinador')),
                ('content', models.TextField(verbose_name='Descripccion del Colaborador')),
                ('url', models.URLField(blank=True, max_length=350, null=True, verbose_name='Enlace')),
                ('published', models.BooleanField(default=False, verbose_name='Estado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha en las que se nos unio')),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
                'ordering': ['-created'],
            },
        ),
    ]
