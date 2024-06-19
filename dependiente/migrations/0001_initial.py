# Generated by Django 5.0.6 on 2024-06-19 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('nit', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('razon_social', models.CharField(max_length=100)),
                ('telefono_entidad', models.CharField(max_length=15)),
                ('correo_entidad', models.EmailField(max_length=254)),
                ('imagen', models.ImageField(upload_to='photos')),
            ],
        ),
    ]