# Generated by Django 5.0.6 on 2024-06-19 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangorest', '0003_novedades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='independiente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]