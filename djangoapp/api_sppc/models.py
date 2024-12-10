from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class PrincipioAtivo(models.Model):
    nome = models.CharField(
        verbose_name="Nome do princípo ativo",
        max_length=100,
        blank=False,
        db_column="nome",
        db_comment="Nome do princípio ativo",
    )


class Produto(models.Model):
    nome = models.CharField(
        verbose_name="Nome do produto",
        max_length=100,
        blank=False,
        db_column="nome",
        db_comment="Nome do produto",
    )
    marca = models.CharField(
        verbose_name="Marca ou linha do produto",
        max_length=100,
        blank=True,
        db_column="marca",
        db_comment="Marca ou linha do produto",
    )
    funcao = models.CharField(
        verbose_name="Função do produto",
        max_length=100,
        blank=True,
        db_column="funcao",
        db_comment="Função ou objetivo do produto, ex.: Creme para pentear, Creme corporal etc.",
    )
    peso_liquido = models.DecimalField(
        verbose_name="Peso/liquido do produto",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="peso_liquido",
        db_comment="Capacidade da embalagem do produto em peso ou liquido.",
    )
    OPCAO_UNIDADE_MEDIDA = {
        "g": "Grama",
        "Kg": "Quilograma",
        "L": "Litro",
        "mL": "Mililitro",
    }
    unidade_medida = models.CharField(
        verbose_name="Unidade de medida do produto",
        max_length=2,
        choices=OPCAO_UNIDADE_MEDIDA,
        blank=False,
        db_column="unidade_medida",
        db_comment="Unidade de medida que compõe o peso/liquido do produto",
    )
    principios_ativos = models.ManyToManyField(to=PrincipioAtivo)


class Consumidor(models.Model):
    nome = models.CharField(
        verbose_name="Nome do consumidor",
        max_length=150,
        blank=False,
        db_column="nome",
        db_comment="Nome do consumidor, paciente ou cliente.",
    )
    data_nascimento = models.DateField(
        verbose_name="Data de nascimento do consumidor",
        blank=False,
        db_column="data_nascimento",
        db_comment="Data de nascimento do consumidor, paciente ou cliente.",
    )
    profissao = models.CharField(
        verbose_name="Profissão do consumidor",
        max_length=100,
        blank=True,
        db_column="profissao",
        db_comment="Profissão ou ocupação principal do consumidor, paciente ou cliente.",
    )
    fumante = models.BooleanField(
        verbose_name="É fumante?",
        blank=True,
        db_column="fumante",
        db_comment="Questiona se o consumidor, paciente ou cliente é fumante.",
    )
    disturbio_circulatorio = models.BooleanField(
        verbose_name="Possui algum distúrbio circulátorio?",
        blank=True,
        db_column="disturbio_circulatorio",
        db_comment="Questiona se o consumidor, paciente ou cliente possui algum distúrbio circulátorio.",
    )
    epiletico = models.BooleanField(
        verbose_name="É epilético(a)?",
        blank=True,
        db_column="epiletico",
        db_comment="Questiona se o consumidor, paciente ou cliente é epiláptico(a).",
    )
    ciclo_intestinal_regular = models.BooleanField(
        verbose_name="Ciclo de menstruação regular?",
        blank=True,
        db_column="ciclo_intestinal_regular",
        db_comment="Questiona se o consumidor, paciente ou cliente está com o ciclo menstrual regular.",
    )
    funcionamento_intestinal_regular = models.BooleanField(
        verbose_name="Funcionamento intestinal regular?",
        blank=True,
        db_column="funcionamento_intestinal_regular",
        db_comment="Questiona se o consumidor, paciente ou cliente está com o funcionamento instestinal regular.",
    )
    alteracao_cardiaca = models.BooleanField(
        verbose_name="Possui alterações ou oscilações cardiácas?",
        blank=True,
        db_column="alteracao_cardiaca",
        db_comment="Questiona se o consumidor, paciente ou cliente possui alterações ou oscilações cardiácas.",
    )
    disturbio_hormonal = models.BooleanField(
        verbose_name="Possui distúrbio hormonal?",
        blank=True,
        db_column="disturbio_hormonal",
        db_comment="Questiona se o consumidor, paciente ou cliente possui distúrbio hormonal.",
    )
    hipotensao = models.BooleanField(
        verbose_name="Possui hipotensão ou pressão baixa?",
        blank=True,
        db_column="hipotensao",
        db_comment="Questiona se o consumidor, paciente ou cliente possui hipotensão ou pressão baixa.",
    )
    hipertensao = models.BooleanField(
        verbose_name="Possui hipertensão ou pressão alta?",
        blank=True,
        db_column="hipertensao",
        db_comment="Questiona se o consumidor, paciente ou cliente possui hipertensão ou pressão alta.",
    )
    disturbio_renal = models.BooleanField(
        verbose_name="Possui distúrbio renal?",
        blank=True,
        db_column="disturbio_renal",
        db_comment="Questiona se o consumidor, paciente ou cliente possui distúrbio renal.",
    )
    varizes_lesoes = models.BooleanField(
        verbose_name="Possui varizes ou lesões",
        blank=True,
        db_column="varizes_lesoes",
        db_comment="Questiona se o consumidor, paciente ou cliente possui varizes ou lesões.",
    )
    diabetes = models.BooleanField(
        verbose_name="Possui diabetes?",
        blank=True,
        db_column="diabetes",
        db_comment="Questiona se o consumidor, paciente ou cliente possui diabetes.",
    )
    OPCAO_DIABETES = {
        "pre_diabetes": "Pré diabetes",
        "diabetes_tipo_1": "Diabetes do tipo 1",
        "diabetes_tipo_2": "Diabetes do tipo 2",
        "diabetes_gestacional": "Diabetes gestacional",
    }
    tipo_diabetes = models.CharField(
        verbose_name="Tipo de diabetes",
        max_length=20,
        choices=OPCAO_DIABETES,
        blank=True,
        db_column="tipo_diabetes",
        db_comment="Questiona qual o tipo de diabetes do consumidor, paciente ou cliente possui.",
    )
    diabetes_controlada = models.BooleanField(
        verbose_name="Diabetes controlada?",
        blank=True,
        db_column="diabetes_controlada",
        db_comment="Questiona se o consumidor, paciente ou cliente está com a diabetes controlada.",
    )
    tratamento_medico = models.BooleanField(
        verbose_name="Está em algum tratamento médico?",
        blank=True,
        db_column="tratamento_medico",
        db_comment="Questiona se o consumidor, paciente ou cliente está em algum tratamento médico.",
    )
    detalhe_tratamento_medico = models.CharField(
        verbose_name="Detalhe do tratamento médico",
        max_length=200,
        blank=True,
        db_column="detalhe_tratamento_medico",
        db_comment="Questiona qual o tratamento médico o consumidor, paciente ou cliente está fazendo.",
    )
    cirurgia_recente = models.BooleanField(
        verbose_name="Fez alguma cirurgia recente?",
        blank=True,
        db_column="cirurgia_recente",
        db_comment="Questiona se o consumidor, paciente ou cliente fez alguma cirurgia recente.",
    )
    detalhe_cirurgia_recente = models.CharField(
        verbose_name="Detalhe da cirurgia recente.",
        max_length=200,
        blank=True,
        db_column="detalhe_cirurgia_recente",
        db_comment="Questiona qual a cirurgia recente o consumidor, paciente ou cliente fez.",
    )
    problema_pele = models.BooleanField(
        verbose_name="Possui algum problema de pele?",
        blank=True,
        db_column="problema_pele",
        db_comment="Questiona se o consumidor, paciente ou cliente possui algum problema de pele.",
    )
    detalhe_problema_pele = models.CharField(
        verbose_name="Detalhe do problema de pele.",
        max_length=200,
        blank=True,
        db_column="detalhe_problema_pele",
        db_comment="Questiona qual o problema de pelo do consumidor, paciente ou cliente.",
    )
    protese_corporal_facial = models.BooleanField(
        verbose_name="Possui prótese corporal ou facial?",
        blank=True,
        db_column="protese_corporal_facial",
        db_comment="Questiona se o consumidor, paciente ou cliente possui alguma prótese corporal ou facial.",
    )
    detalhe_protese_corporal_facial = models.CharField(
        verbose_name="Detalhe da prótese corporal ou facial.",
        max_length=200,
        blank=True,
        db_column="detalhe_protese_corporal_facial",
        db_comment="Questiona qual a prótese corporal ou facial do consumidor, paciente ou cliente.",
    )
    gestante = models.BooleanField(
        verbose_name="É gestante?",
        blank=True,
        db_column="gestante",
        db_comment="Questiona se o consumidor, paciente ou cliente é gestante.",
    )
    semanas_gestante = models.SmallIntegerField(
        verbose_name="Quantas semanas de gestação",
        validators=[MaxValueValidator(50), MinValueValidator(0)],
        null=False,
        default=0,
        db_column="semanas_gestante",
        db_comment="Questiona quantas semanas de gestação o consumidor, paciente ou cliente tem.",
    )
    alergia = models.BooleanField(
        verbose_name="Possui alguma alergia?",
        blank=True,
        db_column="alergia",
        db_comment="Questiona se o consumidor, paciente ou cliente possui alguma alergia.",
    )
    detalhe_alergia = models.CharField(
        verbose_name="Detalhe da alergia.",
        max_length=200,
        blank=True,
        db_column="detalhe_alergia",
        db_comment="Questiona qual a alergia do consumidor, paciente ou cliente.",
    )
    tumor_lesao_precancerosa = models.BooleanField(
        verbose_name="Possui algum tumor ou lesão pré-cancerosa?",
        blank=True,
        db_column="tumor_lesao_precancerosa",
        db_comment="Questiona se o consumidor, paciente ou cliente possui alguma tumor ou lesão pré-cancerosa.",
    )
    detalhe_tumor_lesao_precancerosa = models.CharField(
        verbose_name="Detalhe do tumor ou lesão pré-cancerosa.",
        max_length=200,
        blank=True,
        db_column="detalhe_tumor_lesao_precancerosa",
        db_comment="Questiona qual o tumor ou lesão pré-cancerosa do consumidor, paciente ou cliente.",
    )
    ortopedico = models.BooleanField(
        verbose_name="Possui algum problema ortopédico?",
        blank=True,
        db_column="ortopedico",
        db_comment="Questiona se o consumidor, paciente ou cliente possui algum problema ortopédico.",
    )
    detalhe_ortopedico = models.CharField(
        verbose_name="Detalhe do problema ortopédico.",
        max_length=200,
        blank=True,
        db_column="detalhe_ortopedico",
        db_comment="Questiona qual o problema ortopédico do consumidor, paciente ou cliente.",
    )
    acido = models.BooleanField(
        verbose_name="Faz uso de ácido?",
        blank=True,
        db_column="acido",
        db_comment="Questiona se o consumidor, paciente ou cliente faz uso de ácido.",
    )
    detalhe_acido = models.CharField(
        verbose_name="Detalhe do ácido.",
        max_length=200,
        blank=True,
        db_column="detalhe_acido",
        db_comment="Questiona qual ácido do consumidor, paciente ou cliente faz uso.",
    )
    outro_problema = models.BooleanField(
        verbose_name="Possui algum outro problema que seja necessário relatar?",
        blank=True,
        db_column="outro_problema",
        db_comment="Questiona se o consumidor, paciente ou cliente possui algum outro problema que seja necessário relatar.",
    )
    detalhe_outro_problema = models.CharField(
        verbose_name="Detalhe de outro problema.",
        max_length=200,
        blank=True,
        db_column="detalhe_outro_problema",
        db_comment="Questiona qual outro problema o consumidor, paciente ou cliente tem.",
    )
    altura = models.DecimalField(
        verbose_name="Qual altura em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="altura",
        db_comment="Qual altura do consumidor, paciente ou cliente.",
    )
    peso = models.DecimalField(
        verbose_name="Qual peso em quilograma (Kg)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="peso",
        db_comment="Qual peso do consumidor, paciente ou cliente.",
    )
    busto = models.DecimalField(
        verbose_name="Qual tamanho do busto em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="busto",
        db_comment="Qual tamanho do busto do consumidor, paciente ou cliente.",
    )
    braco_esquerdo = models.DecimalField(
        verbose_name="Qual tamanho do braço esquerdo em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="braco_esquerdo",
        db_comment="Qual tamanho do braço esquerdo do consumidor, paciente ou cliente.",
    )
    braco_direito = models.DecimalField(
        verbose_name="Qual tamanho do braço direito em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="braco_direito",
        db_comment="Qual tamanho do braço direito do consumidor, paciente ou cliente.",
    )
    abdomen = models.DecimalField(
        verbose_name="Qual tamanho do abdômen em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="abdomen",
        db_comment="Qual tamanho do abdômen do consumidor, paciente ou cliente.",
    )
    cintura = models.DecimalField(
        verbose_name="Qual tamanho da cintura em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="cintura",
        db_comment="Qual tamanho da cintura do consumidor, paciente ou cliente.",
    )
    quadril = models.DecimalField(
        verbose_name="Qual tamanho do quadril em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="quadril",
        db_comment="Qual tamanho do quadril do consumidor, paciente ou cliente.",
    )
    culote = models.DecimalField(
        verbose_name="Qual tamanho do culote em milimetros (mm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="culote",
        db_comment="Qual tamanho do culote do consumidor, paciente ou cliente.",
    )
    coxa_esquerda = models.DecimalField(
        verbose_name="Qual tamanho da coxa esquerda em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="coxa_esquerda",
        db_comment="Qual tamanho da coxa esquerda do consumidor, paciente ou cliente.",
    )
    coxa_direita = models.DecimalField(
        verbose_name="Qual tamanho da coxa direita em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="coxa_direita",
        db_comment="Qual tamanho da coxa direita do consumidor, paciente ou cliente.",
    )
    panturrilha_esquerda = models.DecimalField(
        verbose_name="Qual tamanho da panturrilha esquerda em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="panturrilha_esquerda",
        db_comment="Qual tamanho da panturrilha esquerda do consumidor, paciente ou cliente.",
    )
    panturrilha_direita = models.DecimalField(
        verbose_name="Qual tamanho da panturrilha direita em centímetros (cm)?",
        max_digits=8,
        decimal_places=4,
        blank=False,
        db_column="panturrilha_direita",
        db_comment="Qual tamanho da panturrilha direita do consumidor, paciente ou cliente.",
    )


class Tratamento(models.Model):
    descricao = models.CharField(
        verbose_name="Descrição do tratamento.",
        max_length=200,
        blank=False,
        db_column="descricao",
        db_comment="Descrição do tratamento do consumidor, paciente ou cliente.",
    )
    data_inicio = models.DateField(
        verbose_name="Data de início do tratamento",
        blank=False,
        db_column="data_inicio",
        db_comment="Data de início do tratamento do consumidor, paciente ou cliente.",
    )
    data_fim = models.DateField(
        verbose_name="Data de fim do tratamento",
        blank=True,
        null=True,
        db_column="data_fim",
        db_comment="Data do fim do tratamento do consumidor, paciente ou cliente.",
    )
    peso_inicial = models.DecimalField(
        verbose_name="Qual peso inicial em quilograma (Kg)?",
        max_digits=8,
        decimal_places=4,
        blank=True,
        null=True,
        db_column="peso_inicial",
        db_comment="Qual peso inicial do consumidor, paciente ou cliente.",
    )
    peso_final = models.DecimalField(
        verbose_name="Qual peso final em quilograma (Kg)?",
        max_digits=8,
        decimal_places=4,
        blank=True,
        null=True,
        db_column="peso_final",
        db_comment="Qual peso final do consumidor, paciente ou cliente.",
    )
    eficaz = models.BooleanField(
        verbose_name="Tratamento foi eficaz?",
        blank=False,
        null=True,
        db_column="eficaz",
        db_comment="Questiona se o tratamendo no consumidor, paciente ou cliente foi eficaz.",
    )
    consumidores = models.ForeignKey(
        to=Consumidor,
        on_delete=models.CASCADE,
        blank=False,
    )
    produtos = models.ManyToManyField(to=Produto, blank=False)
