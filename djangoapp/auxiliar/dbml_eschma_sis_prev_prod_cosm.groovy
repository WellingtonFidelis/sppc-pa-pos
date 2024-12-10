// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table produtos {
  id_produto integer [primary key, increment]
  nome varchar(100) [not null]
  marca varchar(100) [note: 'Marca ou linha do Fabricante, ex.: CeraVe, Novex, Lolla etc..']
  funcao varchar(100) [note: 'Função ou objetivo do produto, ex.: Creme para pentear, Creme corporal etc.']
  peso_liquido decimal [note: 'Capacidade da embalagem do produto em peso ou liquido.']
  metrica char(2) [note: 'Métrica que compõe o peso/liquido, ex.: l, ml, kg, g etc.']
}

Enum produtos.metrica {
  ml
  l
  kg
  g
}

Table principios_ativos {
  id_principio_ativo integer [primary key, increment]
  nome varchar(100) [not null, note: 'Princípio ativo do produto, ex.: Mantega de Karite, Óleo de amendoas etc.']
}

Table produtos_principios_ativos {
  id_produto_principio_ativo integer [primary key, increment]
  id_produto integer [not null]
  id_principio_ativo integer [not null]

  Note {
    'Princípios ativos dos prodtuos.'
  }
}


Ref pode_ter: principios_ativos.id_principio_ativo < produtos_principios_ativos.id_principio_ativo
Ref pode_ter: produtos.id_produto < produtos_principios_ativos.id_produto

Table consumidores {
  id_consumidor integer [primary key, increment]
  nome varchar(150) [not null]
  data_nascimento date [not null]
  profissao varchar(100)
  fumante bool [not null, note: 'É fumante?']
  disturbio_circulatorio bool [not null, note: 'Possui distúrbio/problema circulatório?']
  epiletica bool [not null, note: 'É epilética?']
  ciclo_menstruacao_regular bool [not null, note: 'Ciclo de menstruação regular?']
  funcionamento_intestinal_regular bool [not null, note: 'Funcionamento instestinal regular?']
  alteracao_cardiaca bool [not null, note: 'Possui alteração ou oscilações cardíacas?']
  disturbio_hormonal bool [not null, note: 'Possui distúrbio hormonal?']
  hipotensao bool [not null, note: 'Possui hipotensão ou pressão baixa?']
  hipertensao bool [not null, note: 'Possui hipertensão ou pressão alta?']
  disturbio_renal bool [not null, note: 'Possui distúrbio renal?']
  varizes_lesoes bool [not null, note: 'Possui varizes ou lesões?']
  diabetes bool [not null, note: 'Possui diabetes?']
  tipo_diabetes varchar [not null, note: 'Tipo de diabetes.']
  diabetes_controlada bool [not null, note: 'Diabetes controlada?']
  tratamento_medico bool [not null, note: 'Está em tratamento médico?']
  detalhe_tratamento_medico varchar(200) [note: 'Detalhe ou especificação do tratamento médico.']
  cirurgia_recente bool [not null, note: 'Fez alguma cirurgia recente?']
  detalhe_cirurgia_recente varchar(200) [note: 'Detalhe ou especificação da cirurgia recente.']
  problema_pele bool [not null, note: 'Possui algum problema de pele?']
  detalhe_problema_pele varchar(200) [note: 'Detalhe ou especificação do problema de pele.']
  protese_corporal_facial bool [not null, note: 'Possui prótese corporal ou facial?']
  detalhe_protese_corporal_facial varchar(200) [note: 'Detalhe ou especificação da prótese corporal ou facial.']
  gestante bool [not null, note: 'É gestante?']
  semanas_gestante integer [note: 'Quantas semanas de gestação?']
  alergia bool [not null, note: 'Possui alguma alergia?']
  detalhe_alergia varchar(200) [note: 'Detalhe ou especificação da alergia.']
  tumor_lesao_precancerosa bool [not null, note: 'Possui algum tumor ou lesão pré-cancerosa?']
  detalhe_tumor_lesao_precancerosa varchar(200) [note: 'Detalhe ou especificação do tumor ou lesão pré-cancerosa.']
  ortopedico bool [not null, note: 'Possui alguma problema ortopédico?']
  detalhe_ortopedico varchar(200) [note: 'Detalhe ou especificação do problema ortopédico.']
  acido bool [not null, note: 'Está utilizando ácidos?']
  detalhe_acido varchar(200) [note: 'Detalhe ou especificação do ácido.']
  outro_problema bool [not null, note: 'Algum outro problema que seja necessário relatar?']
  detalhe_outro_problema varchar(200) [note: 'Detalhe ou especificação de algum outro problema.']
  altura decimal [note: 'Altura em centímetros (cm).']
  peso decimal [note: 'Peso em quilos (kg).']
  busto decimal [note: 'Busto em centímetros (cm).']
  braco_esquerdo decimal [note: 'Braço esquerdo em centímetros (cm).']
  braco_direito decimal [note: 'Braço direito em centímetros (cm).']
  abdomen decimal [note: 'Abdomen em centímetros (cm).']
  cintura decimal [note: 'Cintura em centímetros (cm).']
  quadril decimal [note: 'Quadril em centímetros (cm).']
  culote decimal [note: 'Culote em centímetros (cm).']
  coxa_esquerda decimal [note: 'Coxa esquerda em centímetros (cm).']
  coxa_direita decimal [note: 'Coxa direita em centímetros (cm).']
  panturilha_esquerda decimal [note: 'Panturilha esquerda em centímetros (cm).']
  panturilha_direita decimal [note: 'Panturilha direita em centímetros (cm).']

  Note {
    'Clientes ou pacientes das clínicas'
  }
}

Enum consumidores.tipo_diabetes {
  pre_diabetes
  diabetes_tipo_1
  diabetes_tipo_2
  diabetes_gestacional
}

Table tratamentos {
  id_tratamento integer [primary key, increment]
  descricao varchar(200) [not null]
  data_inicio date [not null, note: 'Data de início do tratamento.']
  data_fim date [not null, note: 'Data do fim do tratamento.']
  peso_inicial decimal [note: 'peso de início do tratamento.']
  peso_final decimal [note: 'peso do fim do tratamento.']
  eficaz bool [note: 'Tratamento foi eficaz?']

  Note {
    'Tratamentos.'
  }
}

Table consumidores_tratamentos {
  id_consumidor_tratamento integer [primary key, increment]
  id_consumidor integer [not null]
  id_tratamento integer [not null]

  Note {
    'Consumidores e seus tratamentos'
  }
}

Ref pode_ter: consumidores_tratamentos.id_consumidor > consumidores.id_consumidor
Ref pode_ter: consumidores_tratamentos.id_tratamento > tratamentos.id_tratamento

Table tratamentos_produtos {
  id_tratamentos_produtos integer [primary key, increment]
  id_tratamento integer [not null]
  id_produto integer [not null]

  Note {
    'Produtos usados no tratamento.'
  }
}

Ref pode_ter: tratamentos_produtos.id_tratamento > tratamentos.id_tratamento
Ref pode_ter: tratamentos_produtos.id_produto > produtos.id_produto