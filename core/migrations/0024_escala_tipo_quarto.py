# Generated by Django 4.1 on 2024-07-29 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_escala_data_ida_escala_data_volta'),
    ]

    operations = [
        migrations.AddField(
            model_name='escala',
            name='tipo_quarto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]