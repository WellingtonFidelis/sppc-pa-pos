# Arquivo será executado apenas na criação dos containers
#

# FROM python:3.11.3-alpine3.18
FROM python:3.11.3-slim-buster
LABEL mantainer="wellingtonf20@gmail.com"

# Variável para o python não gravar em disco os arquivo .pyc
# 1 = Não grava e 0 = Gravar
ENV PYTHONDONTWRITEBUTECODE=1

# Variável para o python não armazenar as saídas dos programas em buffer colocando-os direto no console
ENV PYTHONUNBUFFERED=1

# Copia a pasta do django e scripts para dentro do container
COPY ./djangoapp /djangoapp
COPY ./scripts /scripts

# Usa a pasta djangoapp como principal pasta
WORKDIR /djangoapp

# Porta que o container irá expor para acesso externo
# Essa porta será usada pelo app Django
EXPOSE 8000

# Comandos de console que serão executado na criação do container
# RUN apk add --no-cache build-base libgcc libstdc++ gcc-fortran && \
RUN apt-get update && apt-get install -y nmap && \
  python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

# Adicionando os binários do ambiente virtual criado acima no PATH do OS do Container
ENV PATH="/scripts:/venv/bin:$PATH"

# Alterando para o usuário django criado acima
USER duser

# Comando para executar os arquivos da pasta scripts
CMD ["commands.sh"]