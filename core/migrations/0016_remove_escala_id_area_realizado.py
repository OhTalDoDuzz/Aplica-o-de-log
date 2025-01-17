# Generated by Django 4.1 on 2024-06-26 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_escala_status_fase2_escala_status_fase3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escala',
            name='id_area',
        ),
        migrations.CreateModel(
            name='Realizado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_evento', models.CharField(blank=True, max_length=100, null=True)),
                ('data_evento', models.DateField(blank=True, null=True)),
                ('id_colaborador', models.CharField(blank=True, max_length=100, null=True)),
                ('colaborador_name', models.CharField(blank=True, max_length=100, null=True)),
                ('nome_area', models.CharField(blank=True, max_length=100, null=True)),
                ('nome_cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('contrato', models.CharField(blank=True, max_length=100, null=True)),
                ('origem', models.CharField(blank=True, max_length=100, null=True)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_final', models.DateField(blank=True, null=True)),
                ('qtd_diaria', models.IntegerField(blank=True, default=0, null=True)),
                ('r_qtd_diaria', models.IntegerField(blank=True, default=0, null=True)),
                ('qtd_dias_pgto', models.CharField(blank=True, max_length=100, null=True)),
                ('r_qtd_dias_pgto', models.CharField(blank=True, max_length=100, null=True)),
                ('unidade_diaria', models.CharField(blank=True, max_length=100, null=True)),
                ('r_unidade_diaria', models.CharField(blank=True, max_length=100, null=True)),
                ('total_diaria', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('r_total_diaria', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('passagem', models.BooleanField(blank=True, null=True)),
                ('valor_passagem', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('r_valor_passagem', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('alimentacao_semana_un', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('r_alimentacao_semana_un', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('alimentacao_semana_qtd', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('r_alimentacao_semana_qtd', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('alimentacao_fds_un', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('r_alimentacao_fds_un', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('alimentacao_fds_qtd', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('r_alimentacao_fds_qtd', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('alimentacao_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('r_alimentacao_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hora_ida', models.TimeField(blank=True, null=True)),
                ('r_hora_ida', models.TimeField(blank=True, null=True)),
                ('hora_volta', models.TimeField(blank=True, null=True)),
                ('r_hora_volta', models.TimeField(blank=True, null=True)),
                ('valor_mobilidade', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('r_valor_mobilidade', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('saida', models.CharField(blank=True, max_length=100, null=True)),
                ('r_saida', models.CharField(blank=True, max_length=100, null=True)),
                ('retorno', models.CharField(blank=True, max_length=100, null=True)),
                ('r_retorno', models.CharField(blank=True, max_length=100, null=True)),
                ('meio_transporte', models.CharField(blank=True, max_length=100, null=True)),
                ('r_meio_transporte', models.CharField(blank=True, max_length=100, null=True)),
                ('companhia_aerea', models.CharField(blank=True, max_length=100, null=True)),
                ('r_companhia_aerea', models.CharField(blank=True, max_length=100, null=True)),
                ('loc_voo', models.CharField(blank=True, max_length=100, null=True)),
                ('valor_deslocamento', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('r_valor_deslocamento', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status_fase1', models.CharField(blank=True, default='PENDENTE', max_length=100, null=True)),
                ('status_fase2', models.CharField(blank=True, default='PENDENTE', max_length=100, null=True)),
                ('status_fase3', models.CharField(blank=True, default='PENDENTE', max_length=100, null=True)),
                ('escala', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.escala')),
                ('id_cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cargo')),
                ('id_contrato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tipo_contrato')),
                ('id_evento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.evento')),
                ('id_origem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.origem')),
            ],
        ),
    ]
