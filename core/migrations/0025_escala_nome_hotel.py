# Generated by Django 4.1 on 2024-08-03 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_escala_tipo_quarto'),
    ]

    operations = [
        migrations.AddField(
            model_name='escala',
            name='nome_hotel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
