# Generated by Django 4.1 on 2024-06-21 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_escala_qtd_dias_pgto'),
    ]

    operations = [
        migrations.AddField(
            model_name='escala',
            name='id_contrato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tipo_contrato'),
        ),
    ]
