# Imersão Fullcycle 19 - Plataforma de streaming de vídeos

## Descrição

Repositório do Django (admin dos vídeos)

## Requerimentos

Instalar o Python 3.12.6:

- Mac: Baixe direto do site oficial
- Windows (WSL 2) e Linux: Use o asdf: [https://asdf-vm.com/](). Rode os seguintes comandos:

```bash
sudo apt update

sudo apt-get install build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev 

asdf plugin add python
asdf install python 3.12.6
asdf global python 3.12.6
```

## Rodar a aplicação

Coloque a variável `PIPENV_VENV_IN_PROJECT` no seu `.bashrc` ou `.zshrc`:

```bash
export PIPENV_VENV_IN_PROJECT=1
```

Levante os containers do PostgreSQL e PGAdmin:

```bash
docker-compose up -d
```

Instale o Pipenv:

```bash
pip install pipenv
```

Instale as dependências:

```bash
pipenv install
```

A partir daqui, precisamos sempre rodar os comandos dentro do ambiente virtual do Pipenv:

```bash
pipenv shell
```

Rode as migrações do Django:

```bash
python manage.py migrate
```

Crie um superusuário:

```bash
python manage.py createsuperuser
```

Rode o servidor:

```bash
python manage.py runserver
```

Acesse o admin em [http://localhost:8000/admin]().



