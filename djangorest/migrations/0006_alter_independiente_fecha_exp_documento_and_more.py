# Generated by Django 4.2.6 on 2024-06-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangorest', '0005_alter_independiente_fecha_exp_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='independiente',
            name='fecha_exp_documento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
