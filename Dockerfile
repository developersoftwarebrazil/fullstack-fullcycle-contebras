# Usando uma imagem Python leve para otimizar o tamanho final
FROM python:3.12.6-slim

# Configurações de ambiente
ENV PYTHONDONTWRITEBYTECODE 1  # Impede a criação de arquivos pyc
ENV PYTHONFAULTHANDLER 1       # Torna os erros do Python mais verbosos
ENV PIPENV_VENV_IN_PROJECT 1   # Força o Pipenv a criar o ambiente virtual no projeto

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instalação do Pipenv para gerenciar dependências
RUN pip install --no-cache-dir pipenv

# Criação do usuário não-root
RUN useradd -ms /bin/bash my-user

# Troca para o novo usuário
USER my-user

# Define o diretório de trabalho no container
WORKDIR /home/my-user/app

# Copiar os arquivos do Pipenv para instalar dependências
COPY --chown=my-user:my-user Pipfile Pipfile.lock ./

# Instala as dependências do projeto em modo produção
RUN pipenv install --deploy --ignore-pipfile

# Copiar o restante dos arquivos do projeto
COPY --chown=my-user:my-user . .

# Expor a porta padrão do Django (o Railway configurará a porta final com a variável de ambiente `PORT`)
EXPOSE 8000

# Configura o comando padrão para rodar o servidor Django
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]




# FROM python:3.12.6-slim

# ENV PYTHONDONTWRITEBYTECODE 1 # Prevents Python from writing pyc files to disc
# ENV PYTHONFAULTHANDLER 1 # Makes Python more verbose in case of an error
# ENV PIPENV_VENV_IN_PROJECT 1

# RUN pip install pipenv

# RUN useradd -ms /bin/bash my-user

# USER my-user

# WORKDIR /home/my-user/app

# CMD tail -f /dev/null