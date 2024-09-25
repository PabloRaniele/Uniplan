# Projeto Django 
## Objetivo do projeto e implementar site de clinicas Veterinarias
## Membros do Projeto

##

<hr>

## Documentação do django
https://www.djangoproject.com/

## Instalando ambiente virtual
    python3 -m venv venv

## Ativando e desativando ambiente virtual
### Linux
    . venv/bin/activate
    deactivate

### Windows
    source venv\Scripts\Activate.ps1   # terminal powersheel        
    source venv\Scripts\Activate.bat   # terminal cmd

## Instalando django no ambiente virtual
    pip install django

## Iniciando project django
    django-admin startproject <nome-project> .

## Criar o arquivo requirements.txt
    pip freeze > requirements.txt

## Instale as dependências no projeto
    pip install -r requirements.txt

## Rodando django-admin
    python manage.py runserver

## Migrando a base de dados do Django
    python manage.py makemigrations
    python manage.py migrate

## Criando e modificando a senha de um super usuário
    python manage.py createsuperuser
    python manage.py changepassword USERNAME

## criando app
    python manage.py startapp <nomeapp>

## Configurar o git
    git config --global user.name 'Seu nome'
    git config --global user.email 'seu_email@gmail.com'
    git config --global init.defaultBranch main
    git init
    git add .
    git commit -m 'Mensagem'
    git remote add origin URL_DO_GIT

## Django-allauth
https://docs.allauth.org/en/latest/installation/quickstart.html

https://console.developers.google.com/