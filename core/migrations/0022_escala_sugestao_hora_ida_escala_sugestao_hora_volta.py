# Generated by Django 4.1 on 2024-07-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_escala_valor_hotel_realizado_r_valor_hotel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='escala',
            name='sugestao_hora_ida',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='escala',
            name='sugestao_hora_volta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
