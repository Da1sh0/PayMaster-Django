# Generated by Django 5.0.6 on 2024-06-19 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangorest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salud', models.FloatField(blank=True, null=True)),
                ('pension', models.FloatField(blank=True, null=True)),
                ('arl', models.FloatField(blank=True, null=True)),
                ('salarioBase', models.FloatField(blank=True, null=True)),
                ('cajaCompensacion', models.FloatField(blank=True, null=True)),
                ('cesantias', models.FloatField(blank=True, null=True)),
                ('interesCesantias', models.FloatField(blank=True, null=True)),
                ('vacaciones', models.FloatField(blank=True, null=True)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangorest.independiente')),
            ],
        ),
    ]
