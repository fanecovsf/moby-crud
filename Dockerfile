# Use a imagem Alpine Linux como base
FROM python:3.8-alpine

# Instale as bibliotecas PostgreSQL e outras dependências necessárias
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Configuração da variável de ambiente para não exibir mensagens de aviso
ENV PYTHONUNBUFFERED 1

# Atualize o pip para a versão mais recente
RUN pip install --no-cache-dir --upgrade pip

# Defina o diretório de trabalho como /app
WORKDIR /

# Copie os arquivos de requisitos do projeto para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do projeto para o contêiner
COPY . .

# Execute as migrações do Django
RUN python moby/manage.py migrate

# Expõe a porta 8000
EXPOSE 3001

# Comando para iniciar o servidor Django
CMD ["python", "moby/manage.py", "runserver", "0.0.0.0:3001"]
