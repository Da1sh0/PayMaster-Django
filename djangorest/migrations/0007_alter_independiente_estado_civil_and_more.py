# Generated by Django 4.2.6 on 2024-06-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangorest', '0006_alter_independiente_fecha_exp_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='independiente',
            name='estado_civil',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='fecha_exp_documento',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='fecha_ingreso',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='fecha_nacimiento',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='genero',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='tipo_documento',
            field=models.CharField(max_length=50),
        ),
    ]
