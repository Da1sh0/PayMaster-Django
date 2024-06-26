# Generated by Django 5.0.6 on 2024-06-19 11:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependiente', '0003_calculos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Novedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HorasExDiu', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(48), django.core.validators.MinValueValidator(0)])),
                ('HorasExNoc', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(48), django.core.validators.MinValueValidator(0)])),
                ('HorasExFestivaDiu', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(48), django.core.validators.MinValueValidator(0)])),
                ('HorasExFestivaNoc', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(48), django.core.validators.MinValueValidator(0)])),
                ('recargoDiuFes', models.IntegerField(blank=True, null=True)),
                ('recargoNoc', models.IntegerField(blank=True, null=True)),
                ('recargoNocFest', models.IntegerField(blank=True, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dependiente.empleado')),
            ],
        ),
    ]
