#!/bin/sh

# Comando para o shell encerrar a operação em casos de falhas
set -e

# while ! nmap -Pn -p $POSTGRES_HOST $POSTGRES_PORT | grep -q open; do
# while ! nmap -Pn -p $POSTGRES_PORT $POSTGRES_HOST | grep -q open; do
# while ! nmap -sn -n -v $POSTGRES_HOST | grep -q 'Nmap scan report for ' $POSTGRES_HOST; do
# while ! nmap -Pn -p $POSTGRES_PORT $POSTGRES_HOST | grep -q open; do
#    echo "Aguardando a iniciliazação do Banco de dados PostGres ($POSTGRES_HOST:$POSTGRES_PORT) ..."
#    sleep 2
#done

# echo "Banco de dados PostGres inicializado com sucesso ($POSTGRES_HOST:$POSTGRES_PORT)"

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000