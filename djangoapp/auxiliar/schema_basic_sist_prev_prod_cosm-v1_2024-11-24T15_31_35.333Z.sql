CREATE TABLE "produtos" (
	"id_produto" INTEGER NOT NULL UNIQUE GENERATED BY DEFAULT AS IDENTITY,
	-- Nome do produto
	"nome" VARCHAR(100),
	-- Marca ou linha do Fabricante, ex.: CeraVe, Novex, Lolla etc..
	"marca" VARCHAR(100),
	-- Função ou objetivo do produto, ex.: Creme para pentear, Creme corporal etc.
	"funcao" VARCHAR(150) NOT NULL,
	-- Capacidade da embalagem do produto em peso ou liquido.
	"peso_liquido" DECIMAL(4,4) NOT NULL,
	-- Métrica que compõe o peso/liquido, ex.: l, ml, kg, g etc.
	"unidade_medida" CHAR(2) NOT NULL CHECK(kg,l,ml,gr),
	PRIMARY KEY("id_produto")
);

COMMENT ON TABLE "produtos" IS 'Produtos';
COMMENT ON COLUMN produtos.nome IS 'Nome do produto';
COMMENT ON COLUMN produtos.marca IS 'Marca ou linha do Fabricante, ex.: CeraVe, Novex, Lolla etc..';
COMMENT ON COLUMN produtos.funcao IS 'Função ou objetivo do produto, ex.: Creme para pentear, Creme corporal etc.';
COMMENT ON COLUMN produtos.peso_liquido IS 'Capacidade da embalagem do produto em peso ou liquido.';
COMMENT ON COLUMN produtos.unidade_medida IS 'Métrica que compõe o peso/liquido, ex.: l, ml, kg, g etc.';

CREATE INDEX "produtos_index_0"
ON "produtos" ("id_produto");

CREATE TABLE "principios_ativos" (
	"id_principio_ativo" INTEGER NOT NULL UNIQUE GENERATED BY DEFAULT AS IDENTITY,
	"nome" VARCHAR(100) UNIQUE,
	PRIMARY KEY("id_principio_ativo")
);

CREATE INDEX "principios_ativos_index_0"
ON "principios_ativos" ("id_principio_ativo");

CREATE TABLE "produtos_principios_ativos" (
	"id_produto_principio_ativo" INTEGER NOT NULL UNIQUE GENERATED BY DEFAULT AS IDENTITY,
	"id_produto" INTEGER,
	"id_principio_ativo" INTEGER,
	PRIMARY KEY("id_produto_principio_ativo")
);


CREATE TABLE "consumidores" (
	"id_consumidor" INTEGER NOT NULL UNIQUE GENERATED BY DEFAULT AS IDENTITY,
	"nome" VARCHAR(150) NOT NULL,
	"data_nascimento" DATE NOT NULL,
	-- Profissão ou ocupação principal.
	"profissao" VARCHAR(100) NOT NULL,
	-- É fumante?
	"fumante" BOOLEAN NOT NULL,
	-- Possui algum distúrbio ou problema circulatório?
	"disturbio_circulatorio" BOOLEAN NOT NULL,
	-- É epilética?
	"epileptico" BOOLEAN NOT NULL,
	-- Ciclo de menstruação regular?
	"ciclo_menstrucao_regular" BOOLEAN NOT NULL,
	-- Funcionamento intestinal regular?
	"funcionamento_intestinal_regular" BOOLEAN NOT NULL,
	-- Possui alteração ou oscilações cardíaca?
	"alteracao_cardiaca" BOOLEAN NOT NULL,
	-- Possui distúrbio hormonal?
	"disturbio_hormonal" BOOLEAN NOT NULL,
	-- Possui hipotensão ou pressão baixa?
	"hipotensao" BOOLEAN NOT NULL,
	-- Possui hipertensão ou pressão alta?
	"hipertensao" BOOLEAN NOT NULL,
	-- Possui distúrbio renal?
	"disturbio_renal" BOOLEAN NOT NULL,
	-- Possui varizes ou lesões?
	"varizes_lesoes" BOOLEAN NOT NULL,
	-- Possui diabetes?
	"diabetes" BOOLEAN NOT NULL,
	-- Tipo de diabetes.
	"tipo_diabetes" CHAR(20) CHECK(pre_diabetes, diabetes_tipo_1, diabetes_tipo_2, diabetes_gestacional),
	-- Diabetes controlada?
	"diabetes_controlada" BOOLEAN,
	-- Está em algum tratamento médico?
	"tratamento_medico" BOOLEAN NOT NULL,
	-- Detalhe ou especificação do tratamento médico.
	"detalhe_tratamento_medico" VARCHAR(200),
	-- Fez alguma cirurgia recente?
	"cirurgia_recente" BOOLEAN NOT NULL,
	-- Detalhe ou especificação da cirurgia recente.
	"detalhe_cirurgia_recente" VARCHAR(200),
	-- Possui algum problema de pele?
	"problema_pele" BOOLEAN NOT NULL,
	-- Detalhe ou especificação do problema de pele.
	"detalhe_problema_pele" VARCHAR(200),
	-- Possui prótese corporal ou facial?
	"protese_corporal_facial" BOOLEAN NOT NULL,
	-- Detalhe ou especificação da prótese corporal ou facial.
	"detalhe_protese_corporal_facial" VARCHAR(200),
	-- É gestante?
	"gestante" BOOLEAN NOT NULL,
	-- Quantas semanas de gestação?
	"semanas_gestante" SMALLINT,
	-- Possui alguma alergia?
	"alergia" BOOLEAN NOT NULL,
	-- Detalhe ou especificação da alergia.
	"detalhe_alergia" VARCHAR(200),
	-- Possui algum tumor ou lesão pré-cancerosa?
	"tumor_lesao_precancerosa" BOOLEAN NOT NULL,
	-- Detalhe ou especificação do tumor ou lesão pré-cancerosa.
	"detalhe_tumor_lesao_precancerosa" VARCHAR(200),
	-- Possui algum problema ortopédico?
	"ortopedico" BOOLEAN NOT NULL,
	-- Detalhe ou especificação do problema ortopédico.
	"detalhe_ortopedico" VARCHAR(200),
	-- Está utilizando ácidos?
	"acido" BOOLEAN NOT NULL,
	-- Detalhe ou especificação do ácido.
	"detalhe_acido" VARCHAR(200),
	-- Possui algum outro problema que seja necessário relatar?
	"outro_problema" BOOLEAN NOT NULL,
	-- Detalhe ou especificação de algum outro problema.
	"detalhe_outro_problema" VARCHAR(200),
	-- Altura em centímetros (cm).
	"altura" DECIMAL(4,4),
	-- Peso em quilogramas (kg).
	"peso" DECIMAL(3,3),
	-- Busto em centímetros (cm).
	"busto" DECIMAL(3,3),
	-- Braço esquerdo em centímetros (cm).
	"braco_esquerdo" DECIMAL(3,3),
	-- Braço direito em centímetros (cm).
	"braco_direito" DECIMAL(3,3),
	-- Abdomen em centímetros (cm).
	"abdomen" DECIMAL(3,3),
	-- Cintura em centímetros (cm).
	"cintura" DECIMAL(3,3),
	-- Quadril em centímetros (cm).
	"quadril" DECIMAL(3,3),
	-- Culote em centímetros (cm).
	"culote" DECIMAL(3,3),
	-- Coxa esquerda em centímetros (cm).
	"coxa_esquerda" DECIMAL(3,3),
	-- Coxa direita em centímetros (cm).
	"coxa_direita" DECIMAL(3,3),
	-- Panturrilha esquerda em centímetros (cm).
	"panturrilha_esquerda" DECIMAL(3,3),
	-- Panturrilha direita em centímetros (cm).
	"panturrilha_direita" DECIMAL(3,3),
	PRIMARY KEY("id_consumidor")
);

COMMENT ON TABLE "consumidores" IS 'Clientes ou pacientes da clínica de estética ou salão de beleza.';
COMMENT ON COLUMN consumidores.profissao IS 'Profissão ou ocupação principal.';
COMMENT ON COLUMN consumidores.fumante IS 'É fumante?';
COMMENT ON COLUMN consumidores.disturbio_circulatorio IS 'Possui algum distúrbio ou problema circulatório?';
COMMENT ON COLUMN consumidores.epileptico IS 'É epilética?';
COMMENT ON COLUMN consumidores.ciclo_menstrucao_regular IS 'Ciclo de menstruação regular?';
COMMENT ON COLUMN consumidores.funcionamento_intestinal_regular IS 'Funcionamento intestinal regular?';
COMMENT ON COLUMN consumidores.alteracao_cardiaca IS 'Possui alteração ou oscilações cardíaca?';
COMMENT ON COLUMN consumidores.disturbio_hormonal IS 'Possui distúrbio hormonal?';
COMMENT ON COLUMN consumidores.hipotensao IS 'Possui hipotensão ou pressão baixa?';
COMMENT ON COLUMN consumidores.hipertensao IS 'Possui hipertensão ou pressão alta?';
COMMENT ON COLUMN consumidores.disturbio_renal IS 'Possui distúrbio renal?';
COMMENT ON COLUMN consumidores.varizes_lesoes IS 'Possui varizes ou lesões?';
COMMENT ON COLUMN consumidores.diabetes IS 'Possui diabetes?';
COMMENT ON COLUMN consumidores.tipo_diabetes IS 'Tipo de diabetes.';
COMMENT ON COLUMN consumidores.diabetes_controlada IS 'Diabetes controlada?';
COMMENT ON COLUMN consumidores.tratamento_medico IS 'Está em algum tratamento médico?';
COMMENT ON COLUMN consumidores.detalhe_tratamento_medico IS 'Detalhe ou especificação do tratamento médico.';
COMMENT ON COLUMN consumidores.cirurgia_recente IS 'Fez alguma cirurgia recente?';
COMMENT ON COLUMN consumidores.detalhe_cirurgia_recente IS 'Detalhe ou especificação da cirurgia recente.';
COMMENT ON COLUMN consumidores.problema_pele IS 'Possui algum problema de pele?';
COMMENT ON COLUMN consumidores.detalhe_problema_pele IS 'Detalhe ou especificação do problema de pele.';
COMMENT ON COLUMN consumidores.protese_corporal_facial IS 'Possui prótese corporal ou facial?';
COMMENT ON COLUMN consumidores.detalhe_protese_corporal_facial IS 'Detalhe ou especificação da prótese corporal ou facial.';
COMMENT ON COLUMN consumidores.gestante IS 'É gestante?';
COMMENT ON COLUMN consumidores.semanas_gestante IS 'Quantas semanas de gestação?';
COMMENT ON COLUMN consumidores.alergia IS 'Possui alguma alergia?';
COMMENT ON COLUMN consumidores.detalhe_alergia IS 'Detalhe ou especificação da alergia.';
COMMENT ON COLUMN consumidores.tumor_lesao_precancerosa IS 'Possui algum tumor ou lesão pré-cancerosa?';
COMMENT ON COLUMN consumidores.detalhe_tumor_lesao_precancerosa IS 'Detalhe ou especificação do tumor ou lesão pré-cancerosa.';
COMMENT ON COLUMN consumidores.ortopedico IS 'Possui algum problema ortopédico?';
COMMENT ON COLUMN consumidores.detalhe_ortopedico IS 'Detalhe ou especificação do problema ortopédico.';
COMMENT ON COLUMN consumidores.acido IS 'Está utilizando ácidos?';
COMMENT ON COLUMN consumidores.detalhe_acido IS 'Detalhe ou especificação do ácido.';
COMMENT ON COLUMN consumidores.outro_problema IS 'Possui algum outro problema que seja necessário relatar?';
COMMENT ON COLUMN consumidores.detalhe_outro_problema IS 'Detalhe ou especificação de algum outro problema.';
COMMENT ON COLUMN consumidores.altura IS 'Altura em centímetros (cm).';
COMMENT ON COLUMN consumidores.peso IS 'Peso em quilogramas (kg).';
COMMENT ON COLUMN consumidores.busto IS 'Busto em centímetros (cm).';
COMMENT ON COLUMN consumidores.braco_esquerdo IS 'Braço esquerdo em centímetros (cm).';
COMMENT ON COLUMN consumidores.braco_direito IS 'Braço direito em centímetros (cm).';
COMMENT ON COLUMN consumidores.abdomen IS 'Abdomen em centímetros (cm).';
COMMENT ON COLUMN consumidores.cintura IS 'Cintura em centímetros (cm).';
COMMENT ON COLUMN consumidores.quadril IS 'Quadril em centímetros (cm).';
COMMENT ON COLUMN consumidores.culote IS 'Culote em centímetros (cm).';
COMMENT ON COLUMN consumidores.coxa_esquerda IS 'Coxa esquerda em centímetros (cm).';
COMMENT ON COLUMN consumidores.coxa_direita IS 'Coxa direita em centímetros (cm).';
COMMENT ON COLUMN consumidores.panturrilha_esquerda IS 'Panturrilha esquerda em centímetros (cm).';
COMMENT ON COLUMN consumidores.panturrilha_direita IS 'Panturrilha direita em centímetros (cm).';


CREATE TABLE "tratamentos" (
	"id_tratamento" INTEGER NOT NULL UNIQUE GENERATED BY DEFAULT AS IDENTITY,
	-- Descrição do tratamento.
	"descricao" VARCHAR(200) NOT NULL,
	-- Data de início do tratamento.
	"data_inicio" DATE NOT NULL,
	-- Data fim do tratamento.
	"data_fim" DATE,
	-- Peso do início do tratamento em centímetros (cm).
	"peso_inicial" DECIMAL(3,3),
	-- Peso do final do tratamento em centímetros (cm).
	"peso_final" DECIMAL(3,3),
	-- Tratamento foi eficaz?
	"eficaz" BOOLEAN,
	PRIMARY KEY("id_tratamento")
);

COMMENT ON TABLE "tratamentos" IS 'Tratamentos estéticos.';
COMMENT ON COLUMN tratamentos.descricao IS 'Descrição do tratamento.';
COMMENT ON COLUMN tratamentos.data_inicio IS 'Data de início do tratamento.';
COMMENT ON COLUMN tratamentos.data_fim IS 'Data fim do tratamento.';
COMMENT ON COLUMN tratamentos.peso_inicial IS 'Peso do início do tratamento em centímetros (cm).';
COMMENT ON COLUMN tratamentos.peso_final IS 'Peso do final do tratamento em centímetros (cm).';
COMMENT ON COLUMN tratamentos.eficaz IS 'Tratamento foi eficaz?';


CREATE TABLE "consumidores_tratamentos_produtos" (
	"id_consumidor_tratamento" INTEGER NOT NULL UNIQUE GENERATED BY DEFAULT AS IDENTITY,
	-- Código do consumidor.
	"id_consumidor" INTEGER NOT NULL,
	-- Código do produto.
	"id_produto" INTEGER NOT NULL,
	-- Código do tratamento.
	"id_tratamento" INTEGER NOT NULL,
	PRIMARY KEY("id_consumidor_tratamento")
);

COMMENT ON TABLE "consumidores_tratamentos_produtos" IS 'Quais tratamentos os consumidores estão fazendo ou fizeram.';
COMMENT ON COLUMN consumidores_tratamentos_produtos.id_consumidor IS 'Código do consumidor.';
COMMENT ON COLUMN consumidores_tratamentos_produtos.id_produto IS 'Código do produto.';
COMMENT ON COLUMN consumidores_tratamentos_produtos.id_tratamento IS 'Código do tratamento.';


ALTER TABLE "principios_ativos"
ADD FOREIGN KEY("id_principio_ativo") REFERENCES "produtos_principios_ativos"("id_principio_ativo")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "produtos"
ADD FOREIGN KEY("id_produto") REFERENCES "produtos_principios_ativos"("id_produto")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "tratamentos"
ADD FOREIGN KEY("id_tratamento") REFERENCES "consumidores_tratamentos_produtos"("id_tratamento")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "consumidores"
ADD FOREIGN KEY("id_consumidor") REFERENCES "consumidores_tratamentos_produtos"("id_consumidor")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "produtos"
ADD FOREIGN KEY("id_produto") REFERENCES "consumidores_tratamentos_produtos"("id_produto")
ON UPDATE NO ACTION ON DELETE NO ACTION;