# Generated by Django 4.1 on 2024-06-25 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_escala_valor_deslocamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='escala',
            name='status_fase1',
            field=models.CharField(blank=True, default='PENDENTE', max_length=100, null=True),
        ),
    ]
