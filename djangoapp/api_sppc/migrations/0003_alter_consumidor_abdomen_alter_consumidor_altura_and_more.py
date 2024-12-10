# Generated by Django 5.1.3 on 2024-11-26 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_sppc', '0002_alter_produto_peso_liquido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumidor',
            name='abdomen',
            field=models.DecimalField(db_column='abdomen', db_comment='Qual tamanho do abdômen do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho do abdômen em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='altura',
            field=models.DecimalField(db_column='altura', db_comment='Qual altura do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual altura em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='braco_direito',
            field=models.DecimalField(db_column='braco_direito', db_comment='Qual tamanho do braço direito do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho do braço direito em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='braco_esquerdo',
            field=models.DecimalField(db_column='braco_esquerdo', db_comment='Qual tamanho do braço esquerdo do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho do braço esquerdo em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='busto',
            field=models.DecimalField(db_column='busto', db_comment='Qual tamanho do busto do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho do busto em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='cintura',
            field=models.DecimalField(db_column='cintura', db_comment='Qual tamanho da cintura do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho da cintura em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='coxa_direita',
            field=models.DecimalField(db_column='coxa_direita', db_comment='Qual tamanho da coxa direita do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho da coxa direita em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='coxa_esquerda',
            field=models.DecimalField(db_column='coxa_esquerda', db_comment='Qual tamanho da coxa esquerda do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho da coxa esquerda em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='culote',
            field=models.DecimalField(db_column='culote', db_comment='Qual tamanho do culote do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho do culote em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='panturrilha_direita',
            field=models.DecimalField(db_column='panturrilha_direita', db_comment='Qual tamanho da panturrilha direita do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho da panturrilha direita em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='panturrilha_esquerda',
            field=models.DecimalField(db_column='panturrilha_esquerda', db_comment='Qual tamanho da panturrilha esquerda do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho da panturrilha esquerda em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='peso',
            field=models.DecimalField(db_column='peso', db_comment='Qual peso do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual peso em quilograma (Kg)?'),
        ),
        migrations.AlterField(
            model_name='consumidor',
            name='quadril',
            field=models.DecimalField(db_column='quadril', db_comment='Qual tamanho do quadril do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual tamanho do quadril em centímetros (cm)?'),
        ),
        migrations.AlterField(
            model_name='tratamento',
            name='peso_final',
            field=models.DecimalField(blank=True, db_column='peso_final', db_comment='Qual peso final do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual peso final em quilograma (Kg)?'),
        ),
        migrations.AlterField(
            model_name='tratamento',
            name='peso_inicial',
            field=models.DecimalField(blank=True, db_column='peso_inicial', db_comment='Qual peso inicial do consumidor, paciente ou cliente.', decimal_places=4, max_digits=8, verbose_name='Qual peso inicial em quilograma (Kg)?'),
        ),
    ]