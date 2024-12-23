# Generated by Django 5.1.3 on 2024-11-27 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_sppc', '0004_alter_consumidor_acido_alter_consumidor_alergia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamento',
            name='data_fim',
            field=models.DateField(blank=True, db_column='data_fim', db_comment='Data do fim do tratamento do consumidor, paciente ou cliente.', null=True, verbose_name='Data de fim do tratamento'),
        ),
    ]
