# 1. Usar uma imagem oficial do Python como base
FROM python:3.11-slim

# 2. Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# 3. Copiar o arquivo de dependências primeiro (para otimizar o cache)
COPY requirements.txt .

# 4. Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo o resto do código do seu projeto para o contêiner
COPY . .

# 6. Comando para iniciar sua API quando o contêiner rodar
#    Atenção: Use --host 0.0.0.0 para que a API seja acessível de fora do contêiner
CMD ["uvicorn", "workout_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]